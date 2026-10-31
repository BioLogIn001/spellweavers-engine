from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from spellweavers.default.class_default_orders import DefaultOrders

from spellweavers.core.class_actor import Actor
from spellweavers.default.class_default_actor import DefaultActor, DefaultMonster, DefaultParticipant
from spellweavers.default.class_default_matchdata import DefaultMatchData
from spellweavers.warlocks.class_warlocks_actor import WarlocksMonster, WarlocksParticipant
from spellweavers.warlocks.class_warlocks_spellbook import WarlocksSpellBook


class WarlocksMatchData(DefaultMatchData):
    """Thin Warlocks wrapper over Default MatchData."""

    # Under RavenBlack's rules, a player can stab themselves.
    STAB_SELF_ALLOWED = True

    participant_class = WarlocksParticipant
    monster_class = WarlocksMonster
    spellbook_class = WarlocksSpellBook

    def __init__(self, match_id: int) -> None:
        """Overrides DefaultMatchData.__init__: calls it, then replaces monster_types to set max_hp to start_hp + 1.
        Init match data.

        Arguments:
            match_id (int): match ID
        """
        super().__init__(match_id)

        self.monster_types = {
            1: {'start_hp': 1, 'max_hp': 2, 'attack_damage': 1, 'damage_type': DefaultActor.DAMAGE_TYPE_PHYSICAL, 'attack_all': False, 'initial_effects': {}},
            2: {'start_hp': 2, 'max_hp': 3, 'attack_damage': 2, 'damage_type': DefaultActor.DAMAGE_TYPE_PHYSICAL, 'attack_all': False, 'initial_effects': {}},
            3: {'start_hp': 3, 'max_hp': 4, 'attack_damage': 3, 'damage_type': DefaultActor.DAMAGE_TYPE_PHYSICAL, 'attack_all': False, 'initial_effects': {}},
            4: {'start_hp': 4, 'max_hp': 5, 'attack_damage': 4, 'damage_type': DefaultActor.DAMAGE_TYPE_PHYSICAL, 'attack_all': False, 'initial_effects': {}},
            5: {'start_hp': 3, 'max_hp': 4, 'attack_damage': 3, 'damage_type': DefaultActor.DAMAGE_TYPE_FIRE, 'attack_all': True, 
                'initial_effects': {'ResistHeat': self.DATA_PERMANENT_DURATION}},
            6: {'start_hp': 3, 'max_hp': 4, 'attack_damage': 3, 'damage_type': DefaultActor.DAMAGE_TYPE_ICE, 'attack_all': True, 
                'initial_effects': {'ResistCold': self.DATA_PERMANENT_DURATION}}
        }

    def attack_action(self, a: DefaultParticipant | DefaultMonster, d: DefaultParticipant | DefaultMonster | None,
                      check_mindspells: bool=True, check_visibility: bool=True, check_shields: bool=True) -> None:
        """Overrides DefaultMatchData.attack_action: 
        Monster mindspells: Amnesia skips the attack (default: repeats last target);
        Fear prevents the attack (default: attacks anyway); 
        Maladroitness prevents the attack (default: Confusion picks a random target).
        Resolve a single attack action.

        Arguments:
            a (object): WarlocksParticipant or WarlocksMonster instance, attacker
            d (object): WarlocksParticipant or WarlocksMonster instance or None, defender
            check_mindspells (bool, optional): flag to check mindspell effects that prevent attack
            check_visibility (bool, optional): flag to check visibility (Blindness, Invis)
            check_shields (bool, optional): flag to chech shields (PShield, Protection, Resists)
        """
        # If we check shields and other effects that prevent attacks,
        # we check for mindspells on attacker, but only for monsters
        if check_mindspells and a.type == Actor.ACTOR_TYPE_MONSTER and a.affected_by_paralysis(self.current_turn):
            self.add_log_entry(self.LOG_MINDSPELLS, 'effectParalysis2', actor_id=a.id)
            return
        if check_mindspells and a.type == Actor.ACTOR_TYPE_MONSTER and a.affected_by_amnesia(self.current_turn):
            self.add_log_entry(self.LOG_MINDSPELLS, 'effectAmnesia2', actor_id=a.id)
            return
        if check_mindspells and a.type == Actor.ACTOR_TYPE_MONSTER and a.affected_by_fear(self.current_turn):
            self.add_log_entry(self.LOG_MINDSPELLS, 'effectFear2', actor_id=a.id)
            return
        if check_mindspells and isinstance(a, WarlocksMonster) and a.affected_by_maladroitness(self.current_turn):
            self.add_log_entry(self.LOG_MINDSPELLS, 'effectMaladroitness2', actor_id=a.id)
            return

        if d is None:
            self.add_log_entry(self.LOG_COUNTERS_AND_DEFLECTS, 'attackMissesNobody', actor_id=a.id)
            return

        # If we check visibility, we check visibility between attacker and defender
        if check_visibility and a.affected_by_blindness(self.current_turn):
            self.add_log_entry(self.LOG_COUNTERS_AND_DEFLECTS, 'attackMissesBlindness',
                               actor_id=a.id, attack_id=d.id)
            return
        if check_visibility and d.affected_by_invisibility(self.current_turn):
            self.add_log_entry(self.LOG_COUNTERS_AND_DEFLECTS, 'attackMissesInvisibility',
                               actor_id=a.id, attack_id=d.id)
            return

        # If we got here, we can actually attack.
        # a = Fire elem
        if a.damage_type == a.DAMAGE_TYPE_FIRE:
            if check_shields and d.affected_by_resist_heat_permanent(self.current_turn):
                self.add_log_entry(self.LOG_SHIELDS, 'effectResistHeat',
                                   actor_id=a.id, attack_id=d.id)
            elif check_shields and d.affected_by_pshield(self.current_turn):
                self.add_log_entry(
                    self.LOG_COUNTERS_AND_DEFLECTS, 'effectShieldFromElemental', actor_id=a.id, attack_id=d.id)
            else:
                d.decrease_hp(a.attack_damage)
                self.add_log_entry(self.LOG_DAMAGE_AND_POISON, 'damagedByFireElem', actor_id=a.id,
                                   attack_id=d.id, damage_amount=a.attack_damage)
        # a = Ice elem
        elif a.damage_type == a.DAMAGE_TYPE_ICE:
            if check_shields and d.affected_by_resist_cold_permanent(self.current_turn):
                self.add_log_entry(self.LOG_SHIELDS, 'effectResistCold',
                                   actor_id=a.id, attack_id=d.id)
            elif check_shields and d.affected_by_pshield(self.current_turn):
                self.add_log_entry(
                    self.LOG_COUNTERS_AND_DEFLECTS, 'effectShieldFromElemental', actor_id=a.id, attack_id=d.id)
            else:
                d.decrease_hp(a.attack_damage)
                self.add_log_entry(self.LOG_DAMAGE_AND_POISON, 'damagedByIceElem', actor_id=a.id,
                                   attack_id=d.id, damage_amount=a.attack_damage)
        # a = monster or stabbing participant
        elif a.damage_type == a.DAMAGE_TYPE_PHYSICAL:
            # if a is a timestopped (check_shields = 0) monster, then it deals damage anyways
            # if a is a timestopped (check_shields = 0) participant,
            #   then we check d.affected_by_pshield(1, 0) - shield, but not protection
            # if a is a regular participant (check_shields = 1), then we check
            #   d.affected_by_pshield(1, 1) or simply d.affected_by_pshield()
            if ((not check_shields and a.type == Actor.ACTOR_TYPE_MONSTER)
                    or (not check_shields and a.type == Actor.ACTOR_TYPE_PLAYER and not d.affected_by_pshield(self.current_turn, True, False))
                    or (check_shields and not d.affected_by_pshield(self.current_turn))):
                d.decrease_hp(a.attack_damage)
                self.add_log_entry(self.LOG_DAMAGE_AND_POISON, 'damagedByMonster', actor_id=a.id,
                                   attack_id=d.id, damage_amount=a.attack_damage)
            else:
                self.add_log_entry(self.LOG_COUNTERS_AND_DEFLECTS, 'effectShieldFromMonster',
                                   actor_id=a.id, attack_id=d.id)

    def process_turn_phase_cleanup(self, match_orders: 'DefaultOrders') -> None:
        """Overrides DefaultMatchData.process_turn_phase_cleanup: 
        No revive_risen_participants (no Raise Dead).
        Process turn phase 3 - clean-up.

        Arguments:
            match_orders (object): WarlocksOrders instance, match orders
        """
        # Step 3.1 - remove monsters killed in combat or by slow spells
        self.kill_monsters_eot()

        # Step 3.2 - check spell effects that occur EOT
        self.check_sickness_effects()

        # Step 3.3 - remove players killed in combat or by spells
        self.kill_participants_eot()

        # Step 3.4 - check suicide
        self.kill_suicided_participants(match_orders)

        # Step 3.5 - check surrender
        self.kill_surrendered_participants(self.current_turn)

        # Step 3.6 - check for game over
        self.check_match_end_eot()

        # Step 3.7 - update effects on monsters
        self.update_effects_on_monsters_eot()

        # Step 3.8 - update effects on participants
        self.set_next_turn_type()
        self.update_effects_on_participants_eot()

    def revive_risen_participants(self, turn_num: int) -> None:
        """Overrides DefaultMatchData.revive_risen_participants: not part of Warlocks rules (no Raise Dead)."""
        raise NotImplementedError('Raise Dead is not part of Warlocks rules')
