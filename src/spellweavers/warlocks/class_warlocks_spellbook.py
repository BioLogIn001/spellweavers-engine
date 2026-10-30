from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from spellweavers.default.class_default_matchdata import DefaultMatchData
    from spellweavers.default.class_default_orders import DefaultOrders
    from spellweavers.warlocks.class_warlocks_matchdata import WarlocksMatchData

from spellweavers.core.class_actor import Actor
from spellweavers.core.class_spellbook import Spell, SpellDefinition
from spellweavers.default.class_default_spellbook import DefaultSpellBook
from spellweavers.warlocks.class_warlocks_actor import WarlocksParticipant


class WarlocksSpellBook(DefaultSpellBook):
    """Thin Warlocks wrapper over Default SpellBook."""

    # For Warlocks, no spell can target the dead (no Raise Dead in spellbook)
    SPELL_TARGET_ALIVE_ONLY = True

    def __init__(self) -> None:
        """Overrides DefaultSpellBook.__init__: 
        Title/code; 
        ParaFC table (gesture_dict_paralysis, F->C, C->C) instead of ParaFF;
        Init spellbook."""
        super().__init__()

        self.title = "Ravenblack's Warlocks (ParaFC Maladroit)"
        self.spellbook_code = 'Warlocks'

        self.gesture_dict_paralysis = {'C': 'C', 'D': 'D', 'F': 'C', 'P': 'P', 'S': 'D', 'W': 'P', '>': '>'}

    def get_spell_definitions(self) -> list[SpellDefinition]:
        """Overrides DefaultSpellBook.get_spell_definitions: Warlocks spell table
        Spell table: Maladroitness (18) instead of Confusion, 
        Clap of Lightning as its own spell (37; default: second Lightning Bolt pattern), 
        no Raise Dead (41), Fire Elemental has its own pattern cWSSW (Bartle: one Summon Elemental cSWWS, target chooses), 
        extra patterns Time Stop SPPFD and Blindness DFWFd, Antispell SPFP (Bartle SPF), 
        priorities without Raise Dead.
        Return this spellbook's spell table (a fresh list on every call)."""
        return [
            {'id': 1, 'priority': 1, 'patterns': ["cDPW"], 'default_target': 'self', 'duration': 1, 
                'code': 'dispel_magic', 'tags': []},
            {'id': 2, 'priority': 2, 'patterns': ["WPP", "WWS"], 'default_target': 'self', 'duration': 1, 
                'code': 'counter_spell', 'tags': []},
            {'id': 3, 'priority': 3, 'patterns': ["cw"], 'default_target': 'self', 'duration': 1, 
                'code': 'magic_mirror', 'tags': []},
            {'id': 4, 'priority': 4, 'patterns': ["SFW"], 'default_target': 'self', 'duration': 1, 
                'code': 'summon_goblin', 'tags': ["summon", ]},
            {'id': 5, 'priority': 5, 'patterns': ["PSFW"], 'default_target': 'self', 'duration': 1, 
                'code': 'summon_ogre', 'tags': ["summon", ]},
            {'id': 6, 'priority': 6, 'patterns': ["FPSFW"], 'default_target': 'self', 'duration': 1, 
                'code': 'summon_troll', 'tags': ["summon", ]},
            {'id': 7, 'priority': 7, 'patterns': ["WFPSFW"], 'default_target': 'self', 'duration': 1, 
                'code': 'summon_giant', 'tags': ["summon", ]},
            {'id': 8, 'priority': 8, 'patterns': ["cWSSW"], 'default_target': 'nobody', 'duration': 1, 
                'code': 'summon_fire_elemental', 'tags': ["summon", ]},
            {'id': 9, 'priority': 9, 'patterns': ["cSWWS"], 'default_target': 'nobody', 'duration': 1, 
                'code': 'summon_ice_elemental', 'tags': ["summon", ]},
            {'id': 10, 'priority': 10, 'patterns': ["PWPWWc"], 'default_target': 'self', 'duration': 3, 
                'code': 'haste', 'tags': ["permanentable", ]},
            {'id': 11, 'priority': 11, 'patterns': ["SPPc", "SPPFD"], 'default_target': 'self', 'duration': 1, 
                'code': 'time_stop', 'tags': []},
            {'id': 12, 'priority': 12, 'patterns': ["WWP"], 'default_target': 'self', 'duration': 3, 
                'code': 'protection', 'tags': ["permanentable", ]},
            {'id': 13, 'priority': 13, 'patterns': ["WWFP"], 'default_target': 'self', 'duration': 9999, 
                'code': 'resist_heat', 'tags': []},
            {'id': 14, 'priority': 14, 'patterns': ["SSFP"], 'default_target': 'self', 'duration': 9999, 
                'code': 'resist_cold', 'tags': []},
            {'id': 15, 'priority': 15, 'patterns': ["FFF"], 'default_target': 'opponent', 'duration': 1, 
                'code': 'paralysis', 'tags': ["permanentable", "mindspell", ]},
            {'id': 16, 'priority': 16, 'patterns': ["DPP"], 'default_target': 'opponent', 'duration': 1, 
                'code': 'amnesia', 'tags': ["permanentable", "mindspell", ]},
            {'id': 17, 'priority': 17, 'patterns': ["SWD"], 'default_target': 'opponent', 'duration': 1, 
                'code': 'fear', 'tags': ["permanentable", "mindspell", ]},
            {'id': 18, 'priority': 18, 'patterns': ["DSF"], 'default_target': 'opponent', 'duration': 1, 
                'code': 'maladroitness', 'tags': ["permanentable", "mindspell", ]},
            {'id': 19, 'priority': 19, 'patterns': ["PSDD"], 'default_target': 'self', 'duration': 1, 
                'code': 'charm_monster', 'tags': ["mindspell", ]},
            {'id': 20, 'priority': 20, 'patterns': ["PSDF"], 'default_target': 'opponent', 'duration': 1, 
                'code': 'charm_person', 'tags': ["permanentable", "mindspell", ]},
            {'id': 21, 'priority': 21, 'patterns': ["DSFFFc"], 'default_target': 'opponent', 'duration': 6, 
                'code': 'disease', 'tags': []},
            {'id': 22, 'priority': 22, 'patterns': ["DWWFWD"], 'default_target': 'opponent', 'duration': 6, 
                'code': 'poison', 'tags': []},
            {'id': 23, 'priority': 23, 'patterns': ["DFW"], 'default_target': 'self', 'duration': 1, 
                'code': 'cure_light_wounds', 'tags': []},
            {'id': 24, 'priority': 24, 'patterns': ["DFPW"], 'default_target': 'self', 'duration': 1, 
                'code': 'cure_heavy_wounds', 'tags': []},
            {'id': 25, 'priority': 25, 'patterns': ["SPFP"], 'default_target': 'opponent', 'duration': 1, 
                'code': 'antispell', 'tags': []},
            {'id': 26, 'priority': 26, 'patterns': ["DFWFd", "DWFFd"], 'default_target': 'opponent', 'duration': 3, 
                'code': 'blindness', 'tags': ["permanentable", ]},
            {'id': 27, 'priority': 27, 'patterns': ["PPws"], 'default_target': 'self', 'duration': 3, 
                'code': 'invisibility', 'tags': ["permanentable", ]},
            {'id': 28, 'priority': 28, 'patterns': ["SPFPSDW"], 'default_target': 'self', 'duration': 3, 
                'code': 'permanency', 'tags': ["permanentable", ]},
            {'id': 29, 'priority': 29, 'patterns': ["DWSSSP"], 'default_target': 'self', 'duration': 3, 
                'code': 'delay_effect', 'tags': ["permanentable", ]},
            {'id': 30, 'priority': 30, 'patterns': ["PDWP"], 'default_target': 'opponent', 'duration': 1, 
                'code': 'remove_enchantment', 'tags': []},
            {'id': 31, 'priority': 31, 'patterns': ["P"], 'default_target': 'self', 'duration': 1, 
                'code': 'shield', 'tags': []},
            {'id': 32, 'priority': 32, 'patterns': ["SD"], 'default_target': 'opponent', 'duration': 1, 
                'code': 'magic_missile', 'tags': []},
            {'id': 33, 'priority': 33, 'patterns': ["WFP"], 'default_target': 'opponent', 'duration': 1, 
                'code': 'cause_light_wounds', 'tags': []},
            {'id': 34, 'priority': 34, 'patterns': ["WPFD"], 'default_target': 'opponent', 'duration': 1, 
                'code': 'cause_heavy_wounds', 'tags': []},
            {'id': 35, 'priority': 35, 'patterns': ["FSSDD"], 'default_target': 'opponent', 'duration': 1, 
                'code': 'fireball', 'tags': []},
            {'id': 36, 'priority': 36, 'patterns': ["DFFDD"], 'default_target': 'opponent', 'duration': 1, 
                'code': 'lightning_bolt', 'tags': []},
            {'id': 37, 'priority': 37, 'patterns': ["WDDc"], 'default_target': 'opponent', 'duration': 1, 
                'code': 'clap_of_lightning', 'tags': []},
            {'id': 38, 'priority': 38, 'patterns': ["PWPFSSSD"], 'default_target': 'opponent', 'duration': 1, 
                'code': 'finger_of_death', 'tags': []},
            {'id': 39, 'priority': 39, 'patterns': ["SWWc"], 'default_target': 'nobody', 'duration': 1, 
                'code': 'fire_storm', 'tags': ["storm", ]},
            {'id': 40, 'priority': 40, 'patterns': ["WSSc"], 'default_target': 'nobody', 'duration': 1, 
                'code': 'ice_storm', 'tags': ["storm", ]}
        ]

    def log_effects_bot(self, match_orders: 'DefaultOrders', match_data: 'DefaultMatchData') -> None:
        """Overrides DefaultSpellBook.log_effects_bot: 
        Maladroitness log instead of Confusion logs.
        Log messages related to effects that are checked at the Beginning of the Turn.

        Arguments:
            match_orders (object): WarlocksOrders instance, match orders
            match_data (object): WarlocksMatchData instance, match data
        """
        # Save visibility-related effects to states to keep them intact till EOT
        # This is used if the effect is removed or dispelled mid-turn
        for participant_id in match_data.get_ids_participants():
            p = match_data.get_participant_by_id(participant_id)
            if p is None:
                continue
            if p.affected_by_blindness(match_data.current_turn):
                p.states[match_data.current_turn]['blind'] = 1
            if p.affected_by_invisibility(match_data.current_turn):
                p.states[match_data.current_turn]['invisible'] = 1
            if p.affected_by_timestop(match_data.current_turn):
                p.states[match_data.current_turn]['outatime'] = 1

        # Log entries for timestopped and hasted turns
        if match_data.is_current_turn_timestopped():
            match_data.add_log_entry(match_data.LOG_SHIELDS, 'effectTimeStop')
        if match_data.is_current_turn_hasted():
            match_data.add_log_entry(match_data.LOG_SHIELDS, 'effectHaste')

        # Check other turn effects
        # Ignore all effects on timestopped turn
        if not match_data.is_current_turn_timestopped():
            for participant_id in match_data.get_ids_participants():
                p = match_data.get_participant_by_id(participant_id)
                if p is None:
                    continue

                # Check participant for Disease and Poison
                if p.affected_by_disease(match_data.current_turn):
                    strtmp = 'effectSickness' + str(p.effects[match_data.current_turn]['Disease'])
                    match_data.add_log_entry(match_data.LOG_DAMAGE_AND_POISON, strtmp, actor_id=p.id)
                if p.affected_by_poison(match_data.current_turn):
                    strtmp = 'effectSickness' + str(p.effects[match_data.current_turn]['Poison'])
                    match_data.add_log_entry(match_data.LOG_DAMAGE_AND_POISON, strtmp, actor_id=p.id)

                # Check participant for mindspells
                if (p.affected_by_paralysis(match_data.current_turn)
                        and p.states[match_data.current_turn]['paralyzed_by_id'] in match_data.get_ids_participants_active()):
                    if p.states[match_data.current_turn]['paralyzed_hand_id'] == p.get_lh_id():
                        hand_type = Actor.PLAYER_LEFT_HAND_ID
                    # Default to RH para if for some reasons there were no clear order
                    else:
                        hand_type = Actor.PLAYER_RIGHT_HAND_ID
                    match_data.add_log_entry(match_data.LOG_MINDSPELLS, 'effectParalysis1', actor_id=p.id, target_id=p.id, hand_type=hand_type)
                if p.affected_by_amnesia(match_data.current_turn):
                    match_data.add_log_entry(match_data.LOG_MINDSPELLS, 'effectAmnesia1', actor_id=p.id, target_id=p.id)
                if p.affected_by_fear(match_data.current_turn):
                    match_data.add_log_entry(match_data.LOG_MINDSPELLS, 'effectFear1', actor_id=p.id, target_id=p.id)
                if isinstance(p, WarlocksParticipant) and p.affected_by_maladroitness(match_data.current_turn):
                    match_data.add_log_entry(match_data.LOG_MINDSPELLS, 'effectMaladroitness1', actor_id=p.id, target_id=p.id)
                if (p.affected_by_charm_person(match_data.current_turn)
                        and p.states[match_data.current_turn]['charmed_by_id'] in match_data.get_ids_participants_active()):
                    if p.states[match_data.current_turn]['charmed_hand_id'] == p.get_lh_id():
                        hand_type = Actor.PLAYER_LEFT_HAND_ID
                    # Default to RH para if for some reasons there were no clear order
                    else:
                        hand_type = Actor.PLAYER_RIGHT_HAND_ID
                    if p.states[match_data.current_turn]['charmed_same_gestures']:
                        match_data.add_log_entry(match_data.LOG_MINDSPELLS, 'effectCharmPerson2',
                                                 actor_id=p.id, target_id=p.id, pronoun_owner_id=p.id)
                    else:
                        match_data.add_log_entry(match_data.LOG_MINDSPELLS, 'effectCharmPerson1',
                                                 actor_id=p.id, target_id=p.id, hand_type=hand_type, pronoun_owner_id=p.id)

    def determine_gestures(self, match_orders: 'DefaultOrders', match_data: 'DefaultMatchData') -> None:
        """Overrides DefaultSpellBook.determine_gestures: 
        Paralysis and amnesia respect antispell; 
        Maladroitness (LH copies RH) instead of Confusion (random hand/gesture);
        no permanent Charm Person repeat.
        Determine participants gesture for the turn.

        Based on the orders and effects they are affected with.

        Arguments:
            match_orders (object): WarlocksOrders instance, match orders
            match_data (object): WarlocksMatchData instance, match data
        """
        for participant_id in match_data.get_ids_participants_active():
            # For each participant consider their orders
            p = match_data.get_participant_by_id(participant_id)
            if p is None:
                continue

            order = match_orders.search_orders(match_data.match_id,
                                               match_data.current_turn, participant_id)
            if order is None:
                # raise Exception('No orders = no gestures')
                continue
            gesture_lh = order.gesture_lh
            gesture_rh = order.gesture_rh
            # We ignore all effects on timestop turn,
            # so we check only normal and hasted turns here
            if not match_data.is_current_turn_timestopped():
                # For Paralysis we check if the caster is active this turn
                # This happens if caster is dead or not active during hasted or timestopped turn
                if (p.affected_by_paralysis(match_data.current_turn)
                        and p.states[match_data.current_turn]['paralyzed_by_id'] in match_data.get_ids_participants_active()):
                    # If participant is affected by Para, alter gestures in
                    # paralysed hand using spellbook rules
                    if p.states[match_data.current_turn]['paralyzed_by_id'] == p.states[match_data.current_turn - 1]['paralyzed_by_id']:
                        p.states[match_data.current_turn]['paralyzed_hand_id'] = p.states[match_data.current_turn - 1]['paralyzed_hand_id']
                    else:
                        order_opponent = match_orders.search_orders(match_data.match_id,
                                                                    match_data.current_turn,
                                                                    p.states[match_data.current_turn]['paralyzed_by_id'])
                        if order_opponent and p.id in order_opponent.paralyze_orders:
                            p.states[match_data.current_turn]['paralyzed_hand_id'] = order_opponent.paralyze_orders[p.id]
                    respect_antispell = True
                    if p.states[match_data.current_turn]['paralyzed_hand_id'] == p.get_lh_id():
                        prev_gesture = match_data.get_gesture_filtered(
                            participant_id, match_data.current_turn - 1, Actor.PLAYER_LEFT_HAND_ID, respect_antispell)
                        gesture_lh = self.effect_paralysis(prev_gesture)
                    # elif paralyzeHandID == p.get_rh_id():
                    else:
                        prev_gesture = match_data.get_gesture_filtered(
                            participant_id, match_data.current_turn - 1, Actor.PLAYER_RIGHT_HAND_ID, respect_antispell)
                        gesture_rh = self.effect_paralysis(prev_gesture)
                if p.affected_by_amnesia(match_data.current_turn):
                    # If participant is affected by Amnesia, for both hands
                    # use their previous gestures
                    respect_antispell = True
                    gesture_lh = match_data.get_gesture_filtered(
                        participant_id, match_data.current_turn - 1, Actor.PLAYER_LEFT_HAND_ID, respect_antispell)
                    gesture_rh = match_data.get_gesture_filtered(
                        participant_id, match_data.current_turn - 1, Actor.PLAYER_RIGHT_HAND_ID, respect_antispell)
                if p.affected_by_fear(match_data.current_turn):
                    # If participant is affected by Fear, alter gestures in
                    # both hands using spellbook rules
                    gesture_lh = self.effect_fear(gesture_lh)
                    gesture_rh = self.effect_fear(gesture_rh)
                if isinstance(p, WarlocksParticipant) and p.affected_by_maladroitness(match_data.current_turn):
                    # If participant is affected by Maladroitness, use RH gesture
                    # for both hands
                    gesture_lh = gesture_rh
                # For Charm Person we check if the caster is active this turn
                # This happens if caster is dead or not active during hasted or timestopped turn
                if (p.affected_by_charm_person(match_data.current_turn)
                        and p.states[match_data.current_turn]['charmed_by_id'] in match_data.get_ids_participants_active()):
                    # If participant is affected by Charm Person, use gesture
                    # selected by charmer for selected hand
                    order_opponent = match_orders.search_orders(match_data.match_id,
                                                                match_data.current_turn,
                                                                p.states[match_data.current_turn]['charmed_by_id'])
                    if order_opponent and p.id in order_opponent.charm_orders:
                        charm_order = order_opponent.charm_orders[p.id]
                        if charm_order[0] == p.lh_id:
                            p.states[match_data.current_turn]['charmed_hand_id'] = p.lh_id
                            if charm_order[1] == gesture_lh:
                                p.states[match_data.current_turn]['charmed_same_gestures'] = True
                            gesture_lh = charm_order[1]
                        elif charm_order[0] == p.rh_id:
                            p.states[match_data.current_turn]['charmed_hand_id'] = p.rh_id
                            if charm_order[1] == gesture_rh:
                                p.states[match_data.current_turn]['charmed_same_gestures'] = True
                            gesture_rh = charm_order[1]
                        else:
                            p.states[match_data.current_turn]['charmed_hand_id'] = p.rh_id
                            gesture_rh = '-'
            # Save updated gestures
            match_data.add_gestures(
                participant_id, match_data.current_turn, gesture_lh, gesture_rh)

    def cast_spell_maladroitness(self, spell: Spell, match_data: 'WarlocksMatchData') -> None:

        self.cast_spell_mind_spell(spell, match_data)

    def resolve_spell_maladroitness(self, spell: Spell, match_data: 'WarlocksMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(match_data.LOG_TARGET_NOBODY, 'castMindSpellNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(match_data.LOG_COUNTERS_AND_DEFLECTS, 'castMindSpellCountered', actor_id=spell.caster_id, target_id=target.id)
        elif target.affected_by_permanent_mindspell(match_data.current_turn):
            match_data.add_log_entry(match_data.LOG_ATTACK_AND_SPECIALS, 'castMindSpellOverridenByPermanent',
                                     actor_id=spell.caster_id, target_id=target.id, spell_id=spell.id)
        else:
            if target.type == Actor.ACTOR_TYPE_PLAYER:
                target.effects[match_data.current_turn + 1]['Maladroitness'] = spell.duration
            else:
                target.effects[match_data.current_turn]['Maladroitness'] = spell.duration
            match_data.add_log_entry(match_data.LOG_MINDSPELLS, 'castMaladroitnessResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_clap_of_lightning(self, spell: Spell, match_data: 'WarlocksMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, True, True, True)

    def resolve_spell_clap_of_lightning(self, spell: Spell, match_data: 'WarlocksMatchData') -> None:

        caster = match_data.require_actor(spell.caster_id)
        if caster.states[match_data.current_turn]['clap_of_lightning'] > 0:
            match_data.add_log_entry(match_data.LOG_COUNTERS_AND_DEFLECTS, 'castClapOfLightningFizzle', actor_id=spell.caster_id)
        else:
            caster.states[match_data.current_turn]['clap_of_lightning'] += 1
            target = match_data.get_actor_by_id(spell.target_id)
            if target is None:
                match_data.add_log_entry(match_data.LOG_TARGET_NOBODY, 'castLightningBoltNobody', actor_id=spell.caster_id)
            elif target.affected_by_mshield(match_data.current_turn):
                match_data.add_log_entry(match_data.LOG_COUNTERS_AND_DEFLECTS, 'castLightningBoltCountered', actor_id=spell.caster_id, target_id=target.id)
            else:
                target.decrease_hp(5)
                match_data.add_log_entry(match_data.LOG_DAMAGE_AND_POISON, 'castLightningBoltResolved', actor_id=spell.caster_id, target_id=target.id)

    def resolve_spell_lightning_bolt(self, spell: Spell, match_data: 'DefaultMatchData') -> None:
        """Overrides DefaultSpellBook.resolve_spell_lightning_bolt: 
        No once-per-match WDDc branch (Warlocks has Clap of Lightning instead)."""

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(match_data.LOG_TARGET_NOBODY, 'castLightningBoltNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(match_data.LOG_COUNTERS_AND_DEFLECTS, 'castLightningBoltCountered', actor_id=spell.caster_id, target_id=target.id)
        else:
            target.decrease_hp(5)
            match_data.add_log_entry(match_data.LOG_DAMAGE_AND_POISON, 'castLightningBoltResolved', actor_id=spell.caster_id, target_id=target.id)

    def resolve_spell_finger_of_death(self, spell: Spell, match_data: 'DefaultMatchData') -> None:
        """Overrides DefaultSpellBook.resolve_spell_finger_of_death: 
        No risen-from-dead immunity."""

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(match_data.LOG_TARGET_NOBODY, 'castFingerOfDeathNobody', actor_id=spell.caster_id)
        else:
            match_data.set_destroy_actor_eot_by_id(spell.target_id)
            match_data.add_log_entry(match_data.LOG_DAMAGE_AND_POISON, 'castFingerOfDeathResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_confusion(self, spell: Spell, match_data: 'DefaultMatchData') -> None:
        """Overrides DefaultSpellBook.cast_spell_confusion: not part of Warlocks rules (Maladroitness replaces Confusion)."""
        raise NotImplementedError('Confusion is not part of Warlocks rules')

    def resolve_spell_confusion(self, spell: Spell, match_data: 'DefaultMatchData') -> None:
        """Overrides DefaultSpellBook.resolve_spell_confusion: not part of Warlocks rules (Maladroitness replaces Confusion)."""
        raise NotImplementedError('Confusion is not part of Warlocks rules')

    def cast_spell_raise_dead(self, spell: Spell, match_data: 'DefaultMatchData') -> None:
        """Overrides DefaultSpellBook.cast_spell_raise_dead: not part of Warlocks rules."""
        raise NotImplementedError('Raise Dead is not part of Warlocks rules')

    def resolve_spell_raise_dead(self, spell: Spell, match_data: 'DefaultMatchData') -> None:
        """Overrides DefaultSpellBook.resolve_spell_raise_dead: not part of Warlocks rules."""
        raise NotImplementedError('Raise Dead is not part of Warlocks rules')
