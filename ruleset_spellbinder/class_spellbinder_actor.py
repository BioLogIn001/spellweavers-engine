from ruleset_core.class_actor import Actor
from ruleset_core.class_spellbook import Spell


class SpellbinderActor(Actor):
    """Expands Actor class with Bartle's Spellbinder-specific effects and states."""

    def __init__(self, actor_type: int, gender: int, hp: int, max_hp: int,
                 turn_created: int, attack_all: bool, attack_damage: int, damage_type: str,
                 turn_num: int, permanent_duration: int) -> None:
        """Set defaults for Actor + init effects and states.

        Arguments:
            actor_type (int): {1: participant, 2: monster}
            gender (int): actor (for pronouns)
            hp (int): participant's current hit points
            max_hp (int): participant's maximum hit points
            turn_created (int): turn on which the participant was created
            attack_all (bool): attack all flag
            attack_damage (int): amount of damage attack deals
            damage_type (string): 'Physical', 'Fire', 'Ice'
            turn_num (int): turn number
            permanent_duration (int): constant value for permanent effect duration inherited from match_data
        """
        super().__init__(actor_type, hp, max_hp)
        self.starting_hp = hp
        self.turn_created = turn_created
        self.turn_destroyed = -1
        self.turn_surrendered = -1
        self.gender = gender
        self.effects: dict[int, dict] = {}
        self.states: dict[int, dict] = {}

        # Attack type and damage (for stabs)
        self.attack_all = attack_all
        self.attack_damage = attack_damage
        self.damage_type = damage_type

        # In order to function, engine needs to have effects and states arrays prepared
        # for the current turn and the turn after. So a participant needs to have effects and states
        # from the turn of creation to the current turn (is the match is ongoing).
        for i in range(self.turn_created, turn_num + 2):
            self.init_effects_and_states(i)
        # We also need to dump hp into states[0], since we do not do EOT maintenance for turn 0
        if turn_num == 1:
            self.states[0]['hp'] = self.hp
        self.permanent_duration = permanent_duration

    def init_effects_and_states(self, turn_num: int, preserve_visibility: bool=False) -> None:
        """Initiate effects and states that affect the participant.

        Arguments:
            turn_num (int): turn number
            preserve_visibility (bool, optional): flag to preserve visibility states for dispel magic
        """
        if preserve_visibility:
            state_blind = self.states[turn_num]['blind']
            state_invisible = self.states[turn_num]['invisible']
            state_outatime = self.states[turn_num]['outatime']

        self.effects[turn_num] = self.get_effects_template()

        self.states[turn_num] = self.get_states_template()

        if preserve_visibility:
            self.states[turn_num]['blind'] = state_blind
            self.states[turn_num]['invisible'] = state_invisible
            self.states[turn_num]['outatime'] = state_outatime

    def decrease_effect(self, effect_name: str, turn_num: int) -> None:
        """Decrease the current value of a requested effect.

        Decrease value by one, if the effect existed and not permanent

        Arguments:
            effect_name (string): effect code for self.effects
            turn_num (int): turn number
        """
        if effect_name in self.effects[turn_num]:
            if (self.effects[turn_num][effect_name] != self.permanent_duration
                    and self.effects[turn_num][effect_name] > 0):
                self.effects[turn_num][effect_name] -= 1

    def remove_enchantments(self, turn_num: int) -> None:
        """Reset effects that are affected by Remove Enchantment spell.

        Both for this turn and next turn due to the fact that some spells start
        affecting a participant only from the next turn.

        Arguments:
            turn_num (int): turn number
        """
        self.effects[turn_num]['Haste'] = 0
        self.effects[turn_num]['TimeStop'] = 0
        self.effects[turn_num]['Protection'] = 0
        self.effects[turn_num]['ResistHeat'] = 0
        self.effects[turn_num]['ResistCold'] = 0

        self.effects[turn_num]['Paralysis'] = 0
        self.effects[turn_num]['Amnesia'] = 0
        self.effects[turn_num]['Fear'] = 0
        self.effects[turn_num]['Confusion'] = 0
        self.effects[turn_num]['CharmPerson'] = 0

        self.effects[turn_num]['Disease'] = 0
        self.effects[turn_num]['Poison'] = 0
        self.effects[turn_num]['Blindness'] = 0
        self.effects[turn_num]['Invisibility'] = 0
        self.effects[turn_num]['Permanency'] = 0
        self.effects[turn_num]['DelayEffect'] = 0

        self.effects[turn_num + 1]['Haste'] = 0
        self.effects[turn_num + 1]['TimeStop'] = 0

        self.effects[turn_num + 1]['Paralysis'] = 0
        self.effects[turn_num + 1]['Amnesia'] = 0
        self.effects[turn_num + 1]['Fear'] = 0
        self.effects[turn_num + 1]['Confusion'] = 0
        self.effects[turn_num + 1]['CharmPerson'] = 0

        self.effects[turn_num + 1]['Disease'] = 0
        self.effects[turn_num + 1]['Poison'] = 0
        self.effects[turn_num + 1]['Blindness'] = 0
        self.effects[turn_num + 1]['Invisibility'] = 0
        self.effects[turn_num + 1]['Permanency'] = 0
        self.effects[turn_num + 1]['DelayEffect'] = 0

    def remove_mindspell_effects(self, turn_num: int) -> None:
        """Reset mindspell-related effects (in case if mindspells clash).

        Arguments:
            turn_num (int): turn number
        """
        self.effects[turn_num]['Paralysis'] = 0
        self.effects[turn_num]['Amnesia'] = 0
        self.effects[turn_num]['Fear'] = 0
        self.effects[turn_num]['Confusion'] = 0
        self.effects[turn_num]['CharmPerson'] = 0

        self.effects[turn_num + 1]['Paralysis'] = 0
        self.effects[turn_num + 1]['Amnesia'] = 0
        self.effects[turn_num + 1]['Fear'] = 0
        self.effects[turn_num + 1]['Confusion'] = 0
        self.effects[turn_num + 1]['CharmPerson'] = 0

    def affected_by_permanent_mindspell(self, turn_num: int) -> bool:
        """Check if actor is affected by a permanent mindspell.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        if (self.effects[turn_num]['Paralysis'] == self.permanent_duration
                or self.effects[turn_num]['Amnesia'] == self.permanent_duration
                or self.effects[turn_num]['Fear'] == self.permanent_duration
                or self.effects[turn_num]['Confusion'] == self.permanent_duration
                or self.effects[turn_num]['CharmPerson'] == self.permanent_duration):
            return True
        return False

    def affected_by_blindness(self, turn_num: int) -> bool:
        """Check if actor is affected by Blindness.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Blindness'] in [1, 2, 3, self.permanent_duration] or self.states[turn_num]['blind']

    def affected_by_invisibility(self, turn_num: int) -> bool:
        """Check if actor is affected by Invisibility.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Invisibility'] in [1, 2, 3, self.permanent_duration] or self.states[turn_num]['invisible']

    def affected_by_haste(self, turn_num: int) -> bool:
        """Check if actor is affected by Haste.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Haste'] in [1, 2, 3, self.permanent_duration]

    def affected_by_haste_permanent(self, turn_num: int) -> bool:
        """Check if actor is affected by Haste permanently.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Haste'] in [self.permanent_duration]

    def affected_by_timestop(self, turn_num: int) -> bool:
        """Check if actor is affected by Timestop.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['TimeStop'] in [1] or self.states[turn_num]['outatime']

    def affected_by_paralysis(self, turn_num: int) -> bool:
        """Check if actor is affected by Paralysis.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Paralysis'] in [1, self.permanent_duration]

    def affected_by_paralysis_permanent(self, turn_num: int) -> bool:
        """Check if actor is affected by Paralysis permanently.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Paralysis'] in [self.permanent_duration]

    def affected_by_fear(self, turn_num: int) -> bool:
        """Check if actor is affected by Fear.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Fear'] in [1, self.permanent_duration]

    def affected_by_fear_permanent(self, turn_num: int) -> bool:
        """Check if actor is affected by Fear permanently.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Fear'] in [self.permanent_duration]

    def affected_by_amnesia(self, turn_num: int) -> bool:
        """Check if actor is affected by Amnesia.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Amnesia'] in [1, self.permanent_duration]

    def affected_by_amnesia_permanent(self, turn_num: int) -> bool:
        """Check if actor is affected by Amnesia permanently.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Amnesia'] in [self.permanent_duration]

    def affected_by_confusion(self, turn_num: int) -> bool:
        """Check if actor is affected by Confusion.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Confusion'] in [1, self.permanent_duration]

    def affected_by_confusion_permanent(self, turn_num: int) -> bool:
        """Check if actor is affected by Confusion permanently.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Confusion'] in [self.permanent_duration]

    def affected_by_charm_person(self, turn_num: int) -> bool:
        """Check if actor is affected by Charm Person.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['CharmPerson'] in [1, self.permanent_duration]

    def affected_by_charm_person_permanent(self, turn_num: int) -> bool:
        """Check if actor is affected by Charm Person permanently.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['CharmPerson'] in [self.permanent_duration]

    def affected_by_resist_heat_permanent(self, turn_num: int) -> bool:
        """Check if actor is affected by Resist Heat.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['ResistHeat'] in [self.permanent_duration]

    def affected_by_resist_cold_permanent(self, turn_num: int) -> bool:
        """Check if actor is affected by Resist Cold.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['ResistCold'] in [self.permanent_duration]

    def affected_by_pshield(self, turn_num: int, check_pshield: bool=True, check_protection: bool=True) -> bool:
        """Check if actor is affected by Shield or Protection.

        The distinction is important for edge cases, like during timestop.

        Arguments:
            turn_num (int): turn number
            check_pshield (bool, optional): flag to check Shield
            check_protection (bool, optional): flag to check Protection

        Returns:
            bool: False: not affected, True: affected
        """
        if check_pshield and self.effects[turn_num]['PShield'] in [1]:
            return True
        else:
            return check_protection and self.effects[turn_num]['Protection'] in [1, 2, 3, self.permanent_duration]

    def affected_by_pshield_permanent(self, turn_num: int, check_pshield: bool=True, check_protection: bool=True) -> bool:
        """Check if actor is affected by Protection permanently.

        Arguments:
            turn_num (int): turn number
            check_pshield (bool, optional): ignored, since PShield cannot be permanent
            check_protection (bool, optional): flag to check Protection

        Returns:
            bool: False: not affected, True: affected
        """
        return check_protection and self.effects[turn_num]['Protection'] in [self.permanent_duration]

    def affected_by_mshield(self, turn_num: int) -> bool:
        """Check if actor is affected by MShield (Counter Spell).

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['MShield'] in [1]

    def affected_by_mmirror(self, turn_num: int) -> bool:
        """Check if actor is affected by MMirror (Magic Mirror).

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['MagicMirror'] in [1]

    def affected_by_permanency(self, turn_num: int) -> bool:
        """Check if actor is affected by Permanency.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Permanency'] in [1, 2, 3, self.permanent_duration]

    def affected_by_delay_effect(self, turn_num: int) -> bool:
        """Check if actor is affected by Delay Effect.

        Notice that this does check for the effect that allows to delay spells,
        not for already delayed (stored) spells.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['DelayEffect'] in [1, 2, 3, self.permanent_duration]

    def affected_by_disease(self, turn_num: int) -> bool:
        """Check if actor is affected by Disease.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Disease'] in [1, 2, 3, 4, 5, 6]

    def affected_by_poison(self, turn_num: int) -> bool:
        """Check if actor is affected by Poison.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Poison'] in [1, 2, 3, 4, 5, 6]


class SpellbinderParticipant(SpellbinderActor):
    """Expands SpellbinderActor class with functions specific to participants (human players)."""

    def __init__(self, player_id: int, player_gender: int, player_name: str, 
                    team_id: int, turn_num: int, permanent_duration: int) -> None:
        """Init participant.

        Arguments:
            player_id (int): user ID
            player_gender (int): player gender (for pronouns)
            player_name (string): user name
            team_id (int): team ID for the match (1..8)
            turn_num (int): participant creation turn (to init effects and states; always 1 for participants)
            permanent_duration (int): constant value for permanent effect duration inherited from match_data
        """
        participant_starting_hp = 15
        participant_max_hp = 15
        actor_type = self.ACTOR_TYPE_PLAYER

        # Attack type and damage (for stabs)
        attack_all = False
        attack_damage = 1
        damage_type = 'Physical'
        turn_created = 0

        super().__init__(actor_type, player_gender,
                              participant_starting_hp, participant_max_hp,
                              turn_created, attack_all, attack_damage, damage_type,
                              turn_num, permanent_duration)

        # User ID, to link to website profile
        self.player_id = player_id
        # Team ID for the match
        self.team_id = team_id
        # Username
        self.name = player_name

        # Flags for current turn
        self.state_surrender = False
        self.destroy_eot = False

    def get_effects_template(self) -> dict:
        """Return initial dictionary for participants effects.

        Returns:
            dict: a dictionary with Spellbinder participant effects
        """
        return {
            'PShield': 0,
            'Protection': 0,
            'MShield': 0,
            'MagicMirror': 0,
            'Haste': 0,
            'TimeStop': 0,
            'ResistHeat': 0,
            'ResistCold': 0,

            'Paralysis': 0,
            'Amnesia': 0,
            'Fear': 0,
            'Confusion': 0,
            'CharmPerson': 0,

            'Disease': 0,
            'Poison': 0,
            'Blindness': 0,
            'Invisibility': 0,
            'Permanency': 0,
            'DelayEffect': 0,
        }

    def get_states_template(self) -> dict:
        """Return initial dictionary for participants states.

        Returns:
            dict: a dictionary with Spellbinder participant states
        """
        return {
            'hp': 0,
            'is_alive': False,
            'mindspells_this_turn': 0,
            'paralyzed_by_id': 0,
            'paralyzed_hand_id': 0,
            'confused_hand_id': 0,
            'confused_gesture': '',
            'confused_same_gestures': 0,
            'charmed_by_id': 0,
            'charmed_hand_id': 0,
            'charmed_same_gestures': 0,
            'blind': 0,
            'invisible': 0,
            'outatime': 0,
            'fireballed': 0,
            'antispelled': 0,
            'risenfromdead': 0,
            'clap_of_lightning': 0,
            'delayed_spell': None,
        }

    def set_hands_ids(self, offset: int) -> None:
        """Set IDs for participant's hands.

        Current implementation would set IDs to 21 and 22 for participant with ID 2, etc.

        Arguments:
            offset (int): offset for hand IDs (for Spellbinder set to 10)
        """
        self.lh_id = self.id * offset + 1
        self.rh_id = self.id * offset + 2

    def get_lh_id(self) -> int:
        """Get ID of participant's LH.

        Returns:
            int: left hand ID
        """
        return self.lh_id

    def get_rh_id(self) -> int:
        """Get ID of participant's RH.

        Returns:
            int: right hand ID
        """
        return self.rh_id

    def set_destroy_eot(self) -> None:
        """Set flag to destroy participant at the end of this turn."""
        self.destroy_eot = True

    def set_delayed_spell(self, turn_num: int, spell: Spell) -> None:
        """Save a spell for future cast.

        Arguments:
            turn_num (int): turn number
            spell (object): an instance of Spell class
        """
        self.states[turn_num]['delayed_spell'] = spell

    def get_delayed_spell(self, turn_num: int) -> Spell | None:
        """Load a stored spell to cast it.

        Arguments:
            turn_num (int): turn number

        Returns:
            spell (object): an instance of Spell class
        """
        return self.states[turn_num]['delayed_spell'] # type: ignore[arg-type, no-any-return]

    def clear_delayed_spell(self, turn_num: int) -> None:
        """Clear the stored spell.

        Arguments:
            turn_num (int): turn number
        """
        self.states[turn_num]['delayed_spell'] = None


class SpellbinderMonster(SpellbinderActor):
    """Expands SpellbinderActor class with functions specific to monsters."""

    def __init__(self, monster_types: dict[int, dict], controller_id: int, monster_type: int, summoner_id: int,
                 summoner_hand_id: int, summon_turn: int, gender: int, turn_num: int, permanent_duration: int) -> None:
        """Init Monster.

        Arguments:
            monster_types (dict): Dict of allowed monster types
            controller_id (int): ID of participant that controls the monster
            monster_type (int): Type of the monster according to monster_types
            summoner_id (int): ID of participant that summoned the monster
            summoner_hand_id (int): ID of hand that summoned the monster
            summon_turn (int): turn number on which the monster was summoned
            gender (int): monster gender (for pronouns)
            turn_num (int): turn number
            permanent_duration (int): constant value for permanent effect duration inherited from match_data
        """
        actor_type = self.ACTOR_TYPE_MONSTER

        # Physical, Fire, Ice
        attack_all = monster_types[monster_type]['attack_all']
        attack_damage = monster_types[monster_type]['attack_damage']
        damage_type = monster_types[monster_type]['damage_type']

        super().__init__(actor_type, gender,
                              monster_types[monster_type]['start_hp'],
                              monster_types[monster_type]['max_hp'],
                              summon_turn, attack_all, attack_damage, damage_type,
                              turn_num, permanent_duration)

        self.summoner_id = summoner_id
        self.summoner_hand_id = summoner_hand_id
        self.controller_id = controller_id
        self.monster_type = monster_type
        self.attack_id = 0

        self.destroy_before_attack = False
        self.destroy_eot = False

        # This is to initialize monsters with pre-defined effects, f.e.
        # Fire Elems come with built-in Resist Heat
        if monster_types[monster_type]['initial_effects']:
            for s in monster_types[monster_type]['initial_effects']:
                self.effects[turn_num][s] = monster_types[monster_type]['initial_effects'][s]

    def get_effects_template(self) -> dict:
        """Return initial dictionary for monsters effects.

        Returns:
            dict: a dictionary with Spellbinder monster effects
        """
        return {
            'PShield': 0,
            'Protection': 0,
            'MShield': 0,
            'MagicMirror': 0,
            'Haste': 0,
            'TimeStop': 0,
            'ResistHeat': 0,
            'ResistCold': 0,

            'Paralysis': 0,
            'Amnesia': 0,
            'Fear': 0,
            'Confusion': 0,
            'CharmPerson': 0,

            'Disease': 0,
            'Poison': 0,
            'Blindness': 0,
            'Invisibility': 0,
            'Permanency': 0,
            'DelayEffect': 0,
        }

    def get_states_template(self) -> dict:
        """Return initial dictionary for monsters states.

        Returns:
            dict: a dictionary with Spellbinder monster states
        """
        return {
            'hp': 0,
            'is_alive': False,
            'controller_id': 0,
            'attack_id': 0,
            'mindspells_this_turn': 0,
            'blind': 0,
            'invisible': 0,
            'outatime': 0,
            'fireballed': 0,
            'risenfromdead': 0,
        }

    def destroy_now(self) -> None:
        """Destroy monster immediately."""
        self.is_alive = False

    def set_destroy_before_attack(self) -> None:
        """Flag monster to be destroyed this turn before attack phase."""
        self.destroy_before_attack = True

    def set_destroy_eot(self) -> None:
        """Flag monster to be destroyed before the end of this turn."""
        self.destroy_eot = True
