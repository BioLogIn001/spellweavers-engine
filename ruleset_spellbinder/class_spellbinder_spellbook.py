import random
from typing import Final
from ruleset_core.class_spellbook import Spell, SpellBook
from ruleset_core.class_actor import Actor


class SpellbinderSpellBook(SpellBook):
    """Spellbinder SpellBook class."""

    MAX_SPELL_LENGTH: Final[int] = 8

    def __init__(self) -> None:
        """Init spellbook.

        Arguments:
            spell_names (dict): a dictionary with localized spell names
        """
        title = "Bartle's Spellbinder"
        gesture_dict = {'C': '.', 'D': '.', 'F': '.',
                        'P': '.', 'S': '.', 'W': '.', 'T': '.'}
        super().__init__(title, gesture_dict)

        self.spellbook_code = 'Spellbinder'

        self.gesture_dict_paraff = {'C': 'F', 'D': 'D',
                                    'F': 'F', 'P': 'P', 'S': 'D', 'W': 'P', 'T': 'T'}
        self.gesture_dict_fear = {'C': 'W', 'D': 'W',
                                  'F': 'W', 'P': 'P', 'S': 'W', 'W': 'W', 'T': 'T'}
        self.valid_gestures = ['C', 'D', 'F', 'P', 'S', 'W', '>', '-']
        self.valid_gestures_feared = ['P', 'W', '>', '-']

        self.valid_spell_ids = range(1, 41)
        self.spell_definitions = [
            {'id': 1, 'priority': 1, 'patterns': [
                "cDPW"], 'default_target': 'self', 'duration': 1, 'code': 'dispel_magic'},
            {'id': 2, 'priority': 2, 'patterns': [
                "WPP", "WWS"], 'default_target': 'self', 'duration': 1, 'code': 'counter_spell'},
            {'id': 3, 'priority': 3, 'patterns': [
                "cw"], 'default_target': 'self', 'duration': 1, 'code': 'magic_mirror'},
            {'id': 41, 'priority': 4, 'patterns': [
                "DWWFWc"], 'default_target': 'nobody', 'duration': 1, 'code': 'raise_dead'},
            {'id': 4, 'priority': 5, 'patterns': [
                "SFW"], 'default_target': 'self', 'duration': 1, 'code': 'summon_goblin'},
            {'id': 5, 'priority': 6, 'patterns': [
                "PSFW"], 'default_target': 'self', 'duration': 1, 'code': 'summon_ogre'},
            {'id': 6, 'priority': 7, 'patterns': [
                "FPSFW"], 'default_target': 'self', 'duration': 1, 'code': 'summon_troll'},
            {'id': 7, 'priority': 8, 'patterns': [
                "WFPSFW"], 'default_target': 'self', 'duration': 1, 'code': 'summon_giant'},
            {'id': 8, 'priority': 9, 'patterns': [
                "cSWWS"], 'default_target': 'nobody', 'duration': 1, 'code': 'summon_fire_elemental'},
            {'id': 9, 'priority': 10, 'patterns': [
                "cSWWS"], 'default_target': 'nobody', 'duration': 1, 'code': 'summon_ice_elemental'},
            {'id': 10, 'priority': 11, 'patterns': [
                "PWPWWc"], 'default_target': 'self', 'duration': 3, 'code': 'haste'},
            {'id': 11, 'priority': 12, 'patterns': [
                "SPPc"], 'default_target': 'self', 'duration': 1, 'code': 'time_stop'},
            {'id': 12, 'priority': 13, 'patterns': [
                "WWP"], 'default_target': 'self', 'duration': 3, 'code': 'protection'},
            {'id': 13, 'priority': 14, 'patterns': [
                "WWFP"], 'default_target': 'self', 'duration': 9999, 'code': 'resist_heat'},
            {'id': 14, 'priority': 15, 'patterns': [
                "SSFP"], 'default_target': 'self', 'duration': 9999, 'code': 'resist_cold'},
            {'id': 15, 'priority': 16, 'patterns': [
                "FFF"], 'default_target': 'opponent', 'duration': 1, 'code': 'paralysis'},
            {'id': 16, 'priority': 17, 'patterns': [
                "DPP"], 'default_target': 'opponent', 'duration': 1, 'code': 'amnesia'},
            {'id': 17, 'priority': 18, 'patterns': [
                "SWD"], 'default_target': 'opponent', 'duration': 1, 'code': 'fear'},
            {'id': 18, 'priority': 19, 'patterns': [
                "DSF"], 'default_target': 'opponent', 'duration': 1, 'code': 'confusion'},
            {'id': 19, 'priority': 20, 'patterns': [
                "PSDD"], 'default_target': 'self', 'duration': 1, 'code': 'charm_monster'},
            {'id': 20, 'priority': 21, 'patterns': [
                "PSDF"], 'default_target': 'opponent', 'duration': 1, 'code': 'charm_person'},
            {'id': 21, 'priority': 22, 'patterns': [
                "DSFFFc"], 'default_target': 'opponent', 'duration': 6, 'code': 'disease'},
            {'id': 22, 'priority': 23, 'patterns': [
                "DWWFWD"], 'default_target': 'opponent', 'duration': 6, 'code': 'poison'},
            {'id': 23, 'priority': 24, 'patterns': [
                "DFW"], 'default_target': 'self', 'duration': 1, 'code': 'cure_light_wounds'},
            {'id': 24, 'priority': 25, 'patterns': [
                "DFPW"], 'default_target': 'self', 'duration': 1, 'code': 'cure_heavy_wounds'},
            {'id': 25, 'priority': 26, 'patterns': [
                "SPF"], 'default_target': 'opponent', 'duration': 1, 'code': 'antispell'},
            {'id': 26, 'priority': 27, 'patterns': [
                "DWFFd"], 'default_target': 'opponent', 'duration': 3, 'code': 'blindness'},
            {'id': 27, 'priority': 28, 'patterns': [
                "PPws"], 'default_target': 'self', 'duration': 3, 'code': 'invisibility'},
            {'id': 28, 'priority': 29, 'patterns': [
                "SPFPSDW"], 'default_target': 'self', 'duration': 3, 'code': 'permanency'},
            {'id': 29, 'priority': 30, 'patterns': [
                "DWSSSP"], 'default_target': 'self', 'duration': 3, 'code': 'delay_effect'},
            {'id': 30, 'priority': 31, 'patterns': [
                "PDWP"], 'default_target': 'opponent', 'duration': 1, 'code': 'remove_enchantment'},
            {'id': 31, 'priority': 32, 'patterns': [
                "P"], 'default_target': 'self', 'duration': 1, 'code': 'shield'},
            {'id': 32, 'priority': 33, 'patterns': [
                "SD"], 'default_target': 'opponent', 'duration': 1, 'code': 'magic_missile'},
            {'id': 33, 'priority': 34, 'patterns': [
                "WFP"], 'default_target': 'opponent', 'duration': 1, 'code': 'cause_light_wounds'},
            {'id': 34, 'priority': 35, 'patterns': [
                "WPFD"], 'default_target': 'opponent', 'duration': 1, 'code': 'cause_heavy_wounds'},
            {'id': 35, 'priority': 36, 'patterns': [
                "FSSDD"], 'default_target': 'opponent', 'duration': 1, 'code': 'fireball'},
            {'id': 36, 'priority': 37, 'patterns': [
                "DFFDD", "WDDc"], 'default_target': 'opponent', 'duration': 1, 'code': 'lightning_bolt'},
            {'id': 38, 'priority': 38, 'patterns': [
                "PWPFSSSD"], 'default_target': 'opponent', 'duration': 1, 'code': 'finger_of_death'},
            {'id': 39, 'priority': 39, 'patterns': [
                "SWWc"], 'default_target': 'nobody', 'duration': 1, 'code': 'fire_storm'},
            {'id': 40, 'priority': 40, 'patterns': [
                "WSSc"], 'default_target': 'nobody', 'duration': 1, 'code': 'ice_storm'}
        ]

        for spell_definition in self.spell_definitions:
            self.add_spell(spell_definition)

    def get_spell_definition_by_id(self, spell_id: int) -> dict:
        """Get spell definition by ID.

        Arguments:
            spell_id (int): spell ID

        Returns:
            dict: spell definition, if found
        """
        for spell_definition in self.spell_definitions:
            if spell_definition['id'] == spell_id:
                return spell_definition

        return {}

    def get_new_spell_by_id(self, spell_id: int) -> Spell | None:
        """Return a spell template using spell definition found by spell_id.

        Arguments:
            spell_id (id): spell ID

        Returns:
            obj or None: Spell object if spell definition is found; None otherwise
        """
        spell_definition = self.get_spell_definition_by_id(spell_id)

        if not spell_definition:
            return None

        new_spell = Spell(spell_definition['id'],
                          spell_definition['priority'],
                          spell_definition['patterns'],
                          spell_definition['default_target'],
                          spell_definition['duration'],
                          self.dictionary)
        return new_spell

    def get_ids_spells_permanentable(self) -> list[int]:
        """Return a list of spell IDs that can be made permanent.

        List of permanentable spells:
            Haste, Protection, Paralysis, Amnesia, Confusion, Fear, Charm Person,
            Blindness, Invisibility, Permanency, Delay Effect

        Returns:
            list: IDs of spells
        """
        return [10, 12, 15, 16, 17, 18, 20, 26, 27, 28, 29]

    def get_ids_summons(self) -> list[int]:
        """Return a list of spell IDs that summon monsters.

        Returns:
            list: IDs of spells
        """
        return [4, 5, 6, 7, 8, 9]

    def get_ids_mindspells(self) -> list[int]:
        """Return a list of spell IDs that are considered mind spells.

        Mind spells:
            Paralysis, Amnesia, Fear, Confusion, Charm Monster, Charm Person

        Returns:
            list: IDs of spells
        """
        return [15, 16, 17, 18, 19, 20]

    def get_ids_spells_storms(self) -> list[int]:
        """Return a list of spell IDs that are considered storms.

        Storms:
            Fire Storm, Ice Storm

        Returns:
            list: IDs of spells
        """
        return [39, 40]

    def get_ids_spells_dispel_magic(self) -> list[int]:
        """Return a list of spell IDs that are considered Dispel Magic.

        Returns:
            list: IDs of spells
        """
        return [1]

    def get_ids_spells_fire_storm(self) -> list[int]:
        """Return a list of spell IDs that are considered Fire Storm.

        Returns:
            list: IDs of spells
        """
        return [39]

    def get_ids_spells_ice_storm(self) -> list[int]:
        """Return a list of spell IDs that are considered Ice Storm.

        Returns:
            list: IDs of spells
        """
        return [40]

    def effect_paralysis(self, gesture: str) -> str:
        """Filter gestures according to ParaFF Paralysis effect.

        Arguments:
            gesture (string): gesture to be filtered

        Returns:
            new_gesture (string): filtered gesture
        """
        new_gesture = gesture.translate(
            gesture.maketrans(self.gesture_dict_paraff))
        return new_gesture

    def effect_fear(self, gesture: str) -> str:
        """Filter gestures according to Fear effect.

        Arguments:
            gesture (string): gesture to be filtered

        Returns:
            new_gesture (string): filtered gesture
        """
        new_gesture = gesture.translate(
            gesture.maketrans(self.gesture_dict_fear))
        return new_gesture

    def log_effects_bot(self, match_orders: 'SpellbinderOrders', match_data: 'SpellbinderMatchData') -> None:
        """Log messages related to effects that are checked at the Beginning of the Turn.

        Arguments:
            match_orders (object): SpellbinderOrders instance, match orders
            match_data (object): SpellbinderMatchData instance, match data
        """
        # Save visibility-related effects to states to keep them intact till EOT
        # This is used if the effect is removed or dispelled mid-turn
        for participant_id in match_data.get_ids_participants():
            p = match_data.get_participant_by_id(participant_id)
            if p.affected_by_blindness(match_data.current_turn):
                p.states[match_data.current_turn]['blind'] = 1
            if p.affected_by_invisibility(match_data.current_turn):
                p.states[match_data.current_turn]['invisible'] = 1
            if p.affected_by_timestop(match_data.current_turn):
                p.states[match_data.current_turn]['outatime'] = 1

        # Log entries for timestopped and hasted turns
        if match_data.is_current_turn_timestopped():
            match_data.add_log_entry(7, 'effectTimeStop')
        if match_data.is_current_turn_hasted():
            match_data.add_log_entry(7, 'effectHaste')

        # Check other turn effects
        # Ignore all effects on timestopped turn
        if not match_data.is_current_turn_timestopped():
            for participant_id in match_data.get_ids_participants():
                p = match_data.get_participant_by_id(participant_id)

                # Check participant for Disease and Poison
                if p.affected_by_disease(match_data.current_turn):
                    strtmp = 'effectSickness' + str(p.effects[match_data.current_turn]['Disease'])
                    match_data.add_log_entry(9, strtmp, actor_id=p.id)
                if p.affected_by_poison(match_data.current_turn):
                    strtmp = 'effectSickness' + str(p.effects[match_data.current_turn]['Poison'])
                    match_data.add_log_entry(9, strtmp, actor_id=p.id)

                # Check participant for mindspells
                if (p.affected_by_paralysis(match_data.current_turn)
                        and p.states[match_data.current_turn]['paralyzed_by_id'] in match_data.get_ids_participants_active()):
                    if p.states[match_data.current_turn]['paralyzed_hand_id'] == p.get_lh_id():
                        hand_type = 1
                    # Default to RH para if for some reasons there were no clear order
                    else:
                        hand_type = 2
                    match_data.add_log_entry(8, 'effectParalysis1', actor_id=p.id, target_id=p.id, hand_type=hand_type)
                if p.affected_by_amnesia(match_data.current_turn):
                    match_data.add_log_entry(8, 'effectAmnesia1', actor_id=p.id, target_id=p.id)
                if p.affected_by_fear(match_data.current_turn):
                    match_data.add_log_entry(8, 'effectFear1', actor_id=p.id, target_id=p.id)
                if p.affected_by_confusion(match_data.current_turn):
                    if p.states[match_data.current_turn]['confused_hand_id'] == p.get_lh_id():
                        hand_type = 1
                    else:
                        hand_type = 2
                    if p.states[match_data.current_turn]['confused_same_gestures'] == 1:
                        match_data.add_log_entry(8, 'effectConfusion2',
                                                    actor_id=p.id, target_id=p.id, pronoun_owner_id=p.id)
                    else:
                        match_data.add_log_entry(8, 'effectConfusion1',
                                                    actor_id=p.id, target_id=p.id, hand_type=hand_type, pronoun_owner_id=p.id)
                if (p.affected_by_charm_person(match_data.current_turn)
                        and p.states[match_data.current_turn]['charmed_by_id'] in match_data.get_ids_participants_active()):
                    if p.states[match_data.current_turn]['charmed_hand_id'] == p.get_lh_id():
                        hand_type = 1
                    # Default to RH para if for some reasons there were no clear order
                    else:
                        hand_type = 2
                    if p.states[match_data.current_turn]['charmed_same_gestures'] == 1:
                        match_data.add_log_entry(8, 'effectCharmPerson2',
                                                 actor_id=p.id, target_id=p.id, pronoun_owner_id=p.id)
                    else:
                        match_data.add_log_entry(8, 'effectCharmPerson1',
                                                 actor_id=p.id, target_id=p.id, hand_type=hand_type, pronoun_owner_id=p.id)

    def log_gesture_messages(self, match_data: 'SpellbinderMatchData') -> None:
        """Log messages related to shown gestures.

        Arguments:
            match_data (object): SpellbinderMatchData instance, match data
        """
        for participant_id in match_data.get_ids_participants_active():
            p = match_data.get_participant_by_id(participant_id)
            # For each participant taking action this turn get gestures
            gesture_lh = match_data.get_gesture_last(participant_id, 1)
            gesture_rh = match_data.get_gesture_last(participant_id, 2)
            # Get respective unformatted text strings
            gesture_texts = match_data.get_gesture_log_entry(
                gesture_lh, gesture_rh)
            # Log entried for LH (and RH if available)
            # For Spellbinder, RH is omitted in case of a clap
            match_data.add_log_entry(1, gesture_texts[0], actor_id=p.id, pronoun_owner_id=p.id, hand_type=1)
            if gesture_texts[1]:
                match_data.add_log_entry(1, gesture_texts[1], actor_id=p.id, pronoun_owner_id=p.id, hand_type=2)

    def determine_gestures(self, match_orders: 'SpellbinderOrders', match_data: 'SpellbinderMatchData') -> None:
        """Determine participants gesture for the turn.

        Based on the orders and effects they are affected with.

        Arguments:
            match_orders (object): SpellbinderOrders instance, match orders
            match_data (object): SpellbinderMatchData instance, match data
        """
        for participant_id in match_data.get_ids_participants_active():
            # For each participant consider their orders
            p = match_data.get_participant_by_id(participant_id)

            order = match_orders.search_orders(match_data.match_id,
                                               match_data.current_turn, participant_id)
            gesture_lh = order.gesture_lh
            gesture_rh = order.gesture_rh
            # We ignore all effects on timestop turn,
            # so we check only normal and hasted turns here
            if match_data.is_current_turn_timestopped() == 0:
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
                        if p.id in order_opponent.paralyze_orders:
                            p.states[match_data.current_turn]['paralyzed_hand_id'] = order_opponent.paralyze_orders[p.id]
                    respect_antispell = 0
                    if p.states[match_data.current_turn]['paralyzed_hand_id'] == p.get_lh_id():
                        prev_gesture = match_data.get_gesture_filtered(
                            participant_id, match_data.current_turn - 1, 1, respect_antispell)
                        gesture_lh = self.effect_paralysis(prev_gesture)
                    # elif paralyzeHandID == p.get_rh_id():
                    else:
                        prev_gesture = match_data.get_gesture_filtered(
                            participant_id, match_data.current_turn - 1, 2, respect_antispell)
                        gesture_rh = self.effect_paralysis(prev_gesture)
                if p.affected_by_amnesia(match_data.current_turn):
                    # If participant is affected by Amnesia, for both hands
                    # use their previous gestures
                    respect_antispell = 0
                    gesture_lh = match_data.get_gesture_filtered(
                        participant_id, match_data.current_turn - 1, 1, respect_antispell)
                    gesture_rh = match_data.get_gesture_filtered(
                        participant_id, match_data.current_turn - 1, 2, respect_antispell)
                if p.affected_by_fear(match_data.current_turn):
                    # If participant is affected by Fear, alter gestures in
                    # paralysed hand using spellbook rules
                    gesture_lh = self.effect_fear(gesture_lh)
                    gesture_rh = self.effect_fear(gesture_rh)
                if p.affected_by_confusion(match_data.current_turn):
                    # If participant is permanently confused, the effect is repeated from the previous turn
                    if (p.affected_by_confusion_permanent(match_data.current_turn) and
                            p.affected_by_confusion_permanent(match_data.current_turn - 1)):
                        p.states[match_data.current_turn]['confused_hand_id'] = p.states[match_data.current_turn - 1]['confused_hand_id']
                        p.states[match_data.current_turn]['confused_gesture'] = p.states[match_data.current_turn - 1]['confused_gesture']
                    else:
                        # If participant is affected by Confusion,
                        # their random hand does a random gesture ['C', 'D', 'F', 'P', 'S', 'W']
                        p.states[match_data.current_turn]['confused_hand_id'] = random.Random(match_data.match_id
                                                                                              + match_data.current_turn
                                                                                              + p.id).choice([1, 2])
                        p.states[match_data.current_turn]['confused_gesture'] = random.Random(match_data.match_id
                                                                                              + match_data.current_turn
                                                                                              + p.id).choice(['C', 'D', 'F', 'P', 'S', 'W'])
                    if p.states[match_data.current_turn]['confused_hand_id'] == 1:
                        if gesture_lh == p.states[match_data.current_turn]['confused_gesture']:
                            p.states[match_data.current_turn]['confused_same_gestures'] = 1
                        else:
                            gesture_lh = p.states[match_data.current_turn]['confused_gesture']
                    else:
                        if gesture_rh == p.states[match_data.current_turn]['confused_gesture']:
                            p.states[match_data.current_turn]['confused_same_gestures'] = 1
                        else:
                            gesture_rh = p.states[match_data.current_turn]['confused_gesture']
                # For Charm Person we check if the caster is active this turn
                # This happens if caster is dead or not active during hasted or timestopped turn
                if (p.affected_by_charm_person(match_data.current_turn)
                        and p.states[match_data.current_turn]['charmed_by_id'] in match_data.get_ids_participants_active()):
                    # If participant is permanently charmed, the effect is repeated from the previous turn
                    if (p.affected_by_charm_person_permanent(match_data.current_turn) and
                            p.affected_by_charm_person_permanent(match_data.current_turn - 1)):
                        p.states[match_data.current_turn]['charmed_hand_id'] = p.states[match_data.current_turn - 1]['charmed_hand_id']
                        if p.states[match_data.current_turn]['charmed_hand_id'] == p.lh_id:
                            gesture_lh = match_data.get_gesture_filtered(p.id, match_data.current_turn - 1, 1)
                        else:
                            gesture_rh = match_data.get_gesture_filtered(p.id, match_data.current_turn - 1, 2)
                    else:
                        # If participant is affected by Charm Person, use gesture
                        # selected by charmer for selected hand
                        charm_order = ()
                        order_opponent = match_orders.search_orders(match_data.match_id,
                                                                    match_data.current_turn,
                                                                    p.states[match_data.current_turn]['charmed_by_id'])
                        if p.id in order_opponent.charm_orders:
                            charm_order = order_opponent.charm_orders[p.id]
                        if charm_order[0] == p.lh_id:
                            p.states[match_data.current_turn]['charmed_hand_id'] = p.lh_id
                            if charm_order[1] == gesture_lh:
                                p.states[match_data.current_turn]['charmed_same_gestures'] = 1
                            gesture_lh = charm_order[1]
                        elif charm_order[0] == p.rh_id:
                            p.states[match_data.current_turn]['charmed_hand_id'] = p.rh_id
                            if charm_order[1] == gesture_rh:
                                p.states[match_data.current_turn]['charmed_same_gestures'] = 1
                            gesture_rh = charm_order[1]
                        else:
                            p.states[match_data.current_turn]['charmed_hand_id'] = p.rh_id
                            gesture_rh = '-'
            # Save updated gestures
            match_data.add_gestures(
                participant_id, match_data.current_turn, gesture_lh, gesture_rh)

    def make_precast_target_checks(self, spell: Spell, match_data: 'WarlocksMatchData',
                                   check_blindness: bool=True, check_invisibility: bool=True, 
                                   check_mmirror: bool=True, search_alive_only: bool=True) -> None:
        """Make pre-cast checks for the spell target.

        The first type of checks is checking target ID (hand, monster, participant) and getting target object.
        The second type of checks is target visibility and mirrors.

        Arguments:
            spell (object): Spell Instance, spell to be checked
            match_data (object): SpellbinderMatchData instance, match data
            check_blindness (bool, optional): flag to check Blindness
            check_invisibility (bool, optional): flag to check Invisibililty
            check_mmirror (bool, optional): flag to check Magic Mirror
            search_alive_only (bool, optional): flag to search for dead actors
        """
        # For timestopped turns all existing effects are ignored.
        if match_data.is_current_turn_timestopped():
            check_blindness = False
            check_invisibility = False
            check_mmirror = False

        caster = match_data.get_actor_by_id(spell.caster_id)
        target = None

        if spell.target_id in match_data.get_ids_participants(search_alive_only):
            # target is a participant
            target = match_data.get_participant_by_id(spell.target_id, search_alive_only)
            if spell.delayed == 0:
                match_data.add_log_entry(2, 'castGenericPoM',
                                         actor_id=caster.id,
                                         spell_id=spell.id,
                                         target_id=target.id)
            else:
                match_data.add_log_entry(2, 'castDelayedPoM',
                                         actor_id=caster.id,
                                         spell_id=spell.id,
                                         target_id=target.id)
        elif spell.target_id in match_data.get_ids_monsters(search_alive_only):
            # target is a monster
            target = match_data.get_monster_by_id(spell.target_id, search_alive_only)
            if spell.delayed == 0:
                match_data.add_log_entry(2, 'castGenericPoM',
                                         actor_id=caster.id,
                                         spell_id=spell.id,
                                         target_id=target.id)
            else:
                match_data.add_log_entry(2, 'castDelayedPoM',
                                         actor_id=caster.id,
                                         spell_id=spell.id,
                                         target_id=target.id)
        elif spell.target_id in match_data.get_ids_hands():
            # target is a hand
            if spell.target_id % 2 == 1:
                hand_type = Actor.PLAYER_LEFT_HAND_ID
            else:
                hand_type = Actor.PLAYER_RIGHT_HAND_ID
            handowner = match_data.get_participant_by_id(
                spell.target_id // match_data.DATA_HAND_ID_OFFSET)
            if spell.delayed == 0:
                match_data.add_log_entry(2, 'castGenericHand',
                                         actor_id=caster.id,
                                         spell_id=spell.id,
                                         target_id=handowner.id,
                                         pronoun_owner_id=handowner.id,
                                         hand_type=hand_type)
            else:
                match_data.add_log_entry(2, 'castDelayedHand',
                                         actor_id=caster.id,
                                         spell_id=spell.id,
                                         target_id=handowner.id,
                                         pronoun_owner_id=handowner.id,
                                         hand_type=hand_type)
        else:
            # target is incorrect or nobody
            spell.target_id = 0
            if spell.delayed == 0:
                match_data.add_log_entry(2, 'castGenericNobody',
                                         actor_id=caster.id,
                                         spell_id=spell.id)
            else:
                match_data.add_log_entry(2, 'castDelayedNobody',
                                         actor_id=caster.id,
                                         spell_id=spell.id)

        # Blindness checked for participants, monsters and hands
        if (spell.target_id != 0 and (spell.caster_id != spell.target_id)
                and check_blindness and caster.affected_by_blindness(match_data.current_turn)):
            match_data.add_log_entry(2, 'castMissesBlindness',
                                     actor_id=caster.id,
                                     spell_id=spell.id,
                                     target_id=target.id)
        # Invisibility checked for participants and monsters
        elif (target is not None and (spell.caster_id != spell.target_id)
                and check_invisibility and target.affected_by_invisibility(match_data.current_turn)):
            match_data.add_log_entry(2, 'castMissesInvisibility',
                                     actor_id=caster.id,
                                     spell_id=spell.id,
                                     target_id=target.id)
        # Magic Mirror checked for participants and monsters
        elif (target is not None and (spell.caster_id != spell.target_id)
                and check_mmirror and target.affected_by_mmirror(match_data.current_turn)):
            if target.affected_by_blindness(match_data.current_turn):
                match_data.add_log_entry(2, 'castReflectedBlindness',
                                         actor_id=caster.id,
                                         spell_id=spell.id,
                                         target_id=target.id)
            elif caster.affected_by_invisibility(match_data.current_turn):
                match_data.add_log_entry(2, 'castReflectedInvisibility',
                                         actor_id=caster.id,
                                         spell_id=spell.id,
                                         target_id=target.id)
            elif caster.affected_by_mmirror(match_data.current_turn):
                # Undefined behavoir under core rules
                # RavenBlack did not check for the second mirror -
                # in that implementation reflected spells ignore Magic Mirror on the caster.
                # I decided that this is a bug that can be fixed in this implementation.
                match_data.add_log_entry(2, 'castReflectedInfinite',
                                         actor_id=caster.id,
                                         spell_id=spell.id,
                                         target_id=target.id)
            else:
                spell.resolve = 1
                # If the mirror was on a monster, we set new caster to be monster owner
                # This affects casts which require orders for effects to take place,
                # like Paralysis and Charm Person.
                # It is not the best solution, but it seems better than simply ignoring such effects.
                if target.type == Actor.ACTOR_TYPE_PLAYER:
                    spell.caster_id = spell.target_id
                else:
                    spell.caster_id = target.controller_id
                spell.target_id = caster.id
                match_data.add_log_entry(2, 'castReflected',
                                         actor_id=caster.id,
                                         spell_id=spell.id,
                                         target_id=target.id)
        else:
            spell.resolve = 1

    def select_spells_for_stack(self, match_orders: 'SpellbinderOrders', match_data: 'SpellbinderMatchData') -> None:
        """Select spells to be cast this turn by this participant.

        Select from which they theoretically could cast based on their spellflow.

        Arguments:
            match_orders (object): SpellbinderOrders instance, match orders
            match_data (object): SpellbinderMatchData instance, match data
        """
        for participant_id in match_data.get_ids_participants_active():

            player_orders = match_orders.search_orders(match_data.match_id,
                                                       match_data.current_turn, participant_id)

            cast_spell_lh = None
            cast_spell_rh = None
            cast_spell_bh = None
            # If participant ordered to cast a spell with a specific ID
            # search for it in the heap for each hand
            if player_orders.order_spell_lh > 0:
                cast_spell_lh = self.search_spell_set_by_id(1,
                                                            player_orders.order_spell_lh,
                                                            player_orders.participant_id)
            if player_orders.order_spell_rh > 0:
                cast_spell_rh = self.search_spell_set_by_id(2,
                                                            player_orders.order_spell_rh,
                                                            player_orders.participant_id)

            # If no valid orders were given, start selecting the spell from heap(s)
            # based on the following criteria:
            # - number of hands required (2-handed get priority over 1-handed)
            # - length of spell pattern (longer gets priority)
            # This way WPP is cast over P, PWPWWc over SWWc, and DWWFWD over DFWFd.
            # check if we can cast a spell from both hands
            if (cast_spell_lh is None) and (cast_spell_rh is None):
                cast_spell_bh = self.search_spell_set_by_length(1, cast_spell_bh,
                                                                2, player_orders.participant_id)
                cast_spell_bh = self.search_spell_set_by_length(2, cast_spell_bh,
                                                                2, player_orders.participant_id)
            # we cannot cast anything from BH and nothing pre-selected for LH
            if (cast_spell_bh is None) and (cast_spell_lh is None):
                cast_spell_lh = self.search_spell_set_by_length(1, cast_spell_lh,
                                                                1, player_orders.participant_id)
            # we cannot cast anything from BH and nothing pre-selected for RH
            if (cast_spell_bh is None) and (cast_spell_rh is None):
                cast_spell_rh = self.search_spell_set_by_length(2, cast_spell_rh,
                                                                1, player_orders.participant_id)

            if cast_spell_lh:
                # If the spell was selected, choose it's target.
                # For Spellbinder we use search_alive_only=0 because Raise Dead can target dead
                cast_spell_lh.target_id = self.select_spell_target(player_orders.order_target_lh,
                                                                   cast_spell_lh.default_target,
                                                                   player_orders.participant_id,
                                                                   match_data,
                                                                   search_alive_only=0)
                cast_spell_lh.caster_id = player_orders.participant_id
                cast_spell_lh.cast_turn = match_data.current_turn
                caster = match_data.get_participant_by_id(
                    cast_spell_lh.caster_id)
                # Check if it should be made permanent
                if ((cast_spell_lh.id in self.get_ids_spells_permanentable())
                        and (caster.affected_by_permanency(match_data.current_turn))
                        and (player_orders.make_spell_permanent == caster.lh_id)):
                    cast_spell_lh.duration = match_data.DATA_PERMANENT_DURATION
                    caster.effects[match_data.current_turn]['Permanency'] = 0
                    match_data.add_log_entry(7, 'effectPermanency',
                                             actor_id=caster.id)
                # Check if it should be made delayed
                if ((caster.affected_by_delay_effect(match_data.current_turn))
                        and (player_orders.delay_spell == caster.lh_id)):
                    cast_spell_lh.delayed = 1
                    caster.set_delayed_spell(match_data.current_turn, cast_spell_lh)
                    caster.effects[match_data.current_turn]['DelayEffect'] = 0
                    match_data.add_log_entry(7, 'effectDelaySpell',
                                             actor_id=caster.id)
                # Else add it to stack
                else:
                    self.add_spell_to_stack(cast_spell_lh)

            # Repeat the same process for spell(s) selected from other hands.
            if cast_spell_rh:
                cast_spell_rh.target_id = self.select_spell_target(player_orders.order_target_rh,
                                                                   cast_spell_rh.default_target,
                                                                   player_orders.participant_id,
                                                                   match_data,
                                                                   search_alive_only=0)
                cast_spell_rh.caster_id = player_orders.participant_id
                cast_spell_rh.cast_turn = match_data.current_turn
                caster = match_data.get_participant_by_id(
                    cast_spell_rh.caster_id)
                if ((cast_spell_rh.id in self.get_ids_spells_permanentable())
                        and (caster.affected_by_permanency(match_data.current_turn))
                        and (player_orders.make_spell_permanent == caster.rh_id)):
                    cast_spell_rh.duration = match_data.DATA_PERMANENT_DURATION
                    caster.effects[match_data.current_turn]['Permanency'] = 0
                    match_data.add_log_entry(7, 'effectPermanency',
                                             actor_id=caster.id)
                if ((caster.affected_by_delay_effect(match_data.current_turn))
                        and (player_orders.delay_spell == caster.rh_id)):
                    cast_spell_rh.delayed = 1
                    caster.set_delayed_spell(match_data.current_turn, cast_spell_rh)
                    caster.effects[match_data.current_turn]['DelayEffect'] = 0
                    match_data.add_log_entry(7, 'effectDelaySpell',
                                             actor_id=caster.id)
                else:
                    self.add_spell_to_stack(cast_spell_rh)

            # Repeat the same process for spell(s) selected from other hands.
            if cast_spell_bh:
                caster = match_data.get_participant_by_id(
                    cast_spell_bh.caster_id)
                if cast_spell_bh.used_hand == 1:
                    cast_spell_bh.target_id = self.select_spell_target(player_orders.order_target_lh,
                                                                       cast_spell_bh.default_target,
                                                                       player_orders.participant_id,
                                                                       match_data,
                                                                       search_alive_only=0)
                elif cast_spell_bh.used_hand == 2:
                    cast_spell_bh.target_id = self.select_spell_target(player_orders.order_target_rh,
                                                                       cast_spell_bh.default_target,
                                                                       player_orders.participant_id,
                                                                       match_data,
                                                                       search_alive_only=0)
                if ((cast_spell_bh.id in self.get_ids_spells_permanentable())
                        and (caster.affected_by_permanency(match_data.current_turn))
                        and (player_orders.make_spell_permanent == caster.rh_id
                             or player_orders.make_spell_permanent == caster.lh_id)):
                    cast_spell_bh.duration = match_data.DATA_PERMANENT_DURATION
                    caster.effects[match_data.current_turn]['Permanency'] = 0
                    match_data.add_log_entry(7, 'effectPermanency',
                                             actor_id=caster.id)
                cast_spell_bh.caster_id = player_orders.participant_id
                cast_spell_bh.cast_turn = match_data.current_turn
                if ((caster.affected_by_delay_effect(match_data.current_turn))
                        and (player_orders.delay_spell == caster.lh_id
                             or player_orders.delay_spell == caster.rh_id)):
                    cast_spell_bh.delayed = 1
                    caster.set_delayed_spell(match_data.current_turn, cast_spell_bh)
                    caster.effects[match_data.current_turn]['DelayEffect'] = 0
                    match_data.add_log_entry(7, 'effectDelaySpell',
                                             actor_id=caster.id)
                else:
                    self.add_spell_to_stack(cast_spell_bh)

    def check_delayed_spell_cast(self, match_orders: 'SpellbinderOrders', match_data: 'SpellbinderMatchData') -> None:
        """Put delayed spell in queue.

        If participant had a delayed spell and gave respective orders.

        Arguments:
            match_orders (object): SpellbinderOrders instance, match orders
            match_data (object): SpellbinderMatchData instance, match data
        """
        for participant_id in match_data.get_ids_participants_active():

            player_orders = match_orders.search_orders(match_data.match_id,
                                                       match_data.current_turn, participant_id)

            if player_orders.cast_delayed_spell == 1:
                caster = match_data.get_participant_by_id(participant_id)
                if caster.get_delayed_spell(match_data.current_turn) is not None:
                    delayed_spell = caster.get_delayed_spell(match_data.current_turn)
                    target = match_data.get_actor_by_id(delayed_spell.target_id)
                    if target is None:
                        delayed_spell.target_id = 0
                    self.add_spell_to_stack(delayed_spell)
                    caster.clear_delayed_spell(match_data.current_turn)

    def check_mindspells_clash(self, match_data: 'SpellbinderMatchData') -> None:
        """Check mind spells clashes.

        Mind spells (that alter gestures for the next turn) clash
        and fizzle (i.e. negate each other) if cast at the same target.
        When we attempt to cast a mind spell (for example with .cast_spell_fear())
        we increase .states['mindspells_this_turn'] counter for the mind spell target.
        After resolving those spells (f.e. calling .resolve_spell_fear()) we check
        for clashes here and remove effects for all actors that have a clash.

        Arguments:
            match_data (object): SpellbinderMatchData instance, match data
        """
        for p in match_data.participant_list:
            if p.is_alive and p.states[match_data.current_turn]['mindspells_this_turn'] > 1:
                p.remove_mindspell_effects(match_data.current_turn)
                match_data.add_log_entry(6, 'effectMindSpellCancel',
                                         actor_id=p.id, target_id=p.id, pronoun_owner_id=p.id)
        for m in match_data.monster_list:
            if m.is_alive and m.states[match_data.current_turn]['mindspells_this_turn'] > 1:
                m.remove_mindspell_effects(match_data.current_turn)
                match_data.add_log_entry(6, 'effectMindSpellCancel',
                                         actor_id=m.id, target_id=m.id, pronoun_owner_id=m.id)

    def check_elemental_spells_clash(self, match_data: 'SpellbinderMatchData') -> None:
        """Check elemental spells clashes.

        Elemental spells (storms and elementals) clash
        and fizzle (i.e. negate each other) if cast / present at the turn.
        When we attempt to cast an elemental spell, we increase
        .turn_info['fire_storms'] counter for the turn. Here we check all these
        counters and account for clashes before resolving those spells.

        Arguments:
            match_data (object): SpellbinderMatchData instance, match data
        """
        if match_data.turns_info[match_data.current_turn]['elementals_clash']:
            match_data.add_log_entry(10, 'effectFireElementalIceElementalCancel')

        fire_elemental_ids = match_data.get_ids_monsters(monster_type=match_data.MONSTER_TYPE_FIREELEM)
        fire_elemental_exists = len(fire_elemental_ids)
        ice_elemental_ids = match_data.get_ids_monsters(monster_type=match_data.MONSTER_TYPE_ICEELEM)
        ice_elemental_exists = len(ice_elemental_ids)

        if (match_data.turns_info[match_data.current_turn]['fire_storms']
                and match_data.turns_info[match_data.current_turn]['ice_storms']):
            # If both Firestorm(s) and Icestorm(s) were cast, fizzle storms
            for s in self.stack:
                if s.resolve == 1 and s.id in self.get_ids_spells_storms():
                    s.resolve = 0
            match_data.turns_info[match_data.current_turn]['fire_storms'] = 0
            match_data.turns_info[match_data.current_turn]['ice_storms'] = 0
            match_data.add_log_entry(10, 'effectFireStormIceStormCancel')

        if fire_elemental_exists:
            if match_data.turns_info[match_data.current_turn]['fire_storms']:
                # If Firestorm(s) were cast and Ice Elemental present, absorb elem
                for e in fire_elemental_ids:
                    match_data.set_destroy_monster_now_by_id(e)
                match_data.add_log_entry(10, 'effectElementalAbsorbedByStorm', actor_id=e)
            elif match_data.turns_info[match_data.current_turn]['ice_storms']:
                # If Icestorm(s) were cast and Fire Elemental present, fizzle storms and destroy elem
                for s in self.stack:
                    if s.resolve == 1 and s.id in self.get_ids_spells_ice_storm():
                        s.resolve = 0
                match_data.turns_info[match_data.current_turn]['ice_storms'] = 0
                for e in fire_elemental_ids:
                    match_data.set_destroy_monster_now_by_id(e)
                match_data.add_log_entry(10, 'effectIceStormFireElementalCancel')

        if ice_elemental_exists:
            if match_data.turns_info[match_data.current_turn]['ice_storms']:
                # If Icestorm(s) were cast and Ice Elemental present, absorb elem
                for e in ice_elemental_ids:
                    match_data.set_destroy_monster_now_by_id(e)
                match_data.add_log_entry(10, 'effectElementalAbsorbedByStorm', actor_id=e)
            elif match_data.turns_info[match_data.current_turn]['fire_storms']:
                # If Firestorm(s) were cast and Ice Elemental present, fizzle storms and destroy elem
                for s in self.stack:
                    if s.resolve == 1 and s.id in self.get_ids_spells_fire_storm():
                        s.resolve = 0
                match_data.turns_info[match_data.current_turn]['fire_storms'] = 0
                for e in ice_elemental_ids:
                    match_data.set_destroy_monster_now_by_id(e)
                match_data.add_log_entry(10, 'effectFireStormIceElementalCancel')

    # SPELL CAST section

    """All spells are cast in two stage - 'cast' (or 'fired' or 'started') and 'resolve'.
    This is because some spells interact with others before taking effect
    (for example, Ice Storm and Fire Storm negate each other and produce a single message).
    This means we have to 'start' casting all spells, then take note of such collisions, then resolve all.

    However, this approach had to be modified due to the way targetting works (specifically we need
    to track effects on monsters that are not yet summoned - and might not be resolved -
    and were targeted by hand ID). To avoid having additional target list that would have to be
    mapped to existing targets later, we resolve Dispel Magic, CounterSpell, Magic Mirror and all Summons
    (i.e. spell with IDs 1..9) during cast phase, then do checks, then resolve everything else.
    It is not elegant, but it gets job done.

    Similar spells might use common functions:
    Goblins, Ogres, Troll and Giants use resolve_spell_summon_monster()
    Disease and Poison use resolve_spell_sickness()
    Mindspells use cast_spell_mind_spell
    Cause and Cure wounds spells use resolve_spell_cause_wounds() and resolve_spell_cure_wounds()

    All functions below that match patterns cast_spell_[spellcode] or resolve_spell_[spellcode]
    use the same Arguments:
        spell (object): Spell instance, spell that is being cast
        match_data (object): SpellbinderMatchData instance, match data
    """

    def cast_spell_dispel_magic(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 0)

        match_data.add_log_entry(7, 'castDispelMagicResolved', actor_id=spell.caster_id)

        # Remove all non-DispelMagic spells from queue
        self.stack[:] = [s for s in self.stack if s.id in self.get_ids_spells_dispel_magic()]

        # Remove all effects from all participants
        for p in match_data.participant_list:
            if p.is_alive:
                preserve_visibility = 1
                p.init_effects_and_states(match_data.current_turn, preserve_visibility)
                p.init_effects_and_states(match_data.current_turn + 1, preserve_visibility)

        # Remove all effects from all monsters
        for m in match_data.monster_list:
            if m.is_alive:
                preserve_visibility = 1
                m.init_effects_and_states(match_data.current_turn, preserve_visibility)
                m.init_effects_and_states(match_data.current_turn + 1, preserve_visibility)

        # Shield target
        target = match_data.get_actor_by_id(spell.target_id)
        if target is not None:
            target.effects[match_data.current_turn]['PShield'] = 1
            match_data.add_log_entry(7, 'castShieldResolved', actor_id=spell.caster_id, target_id=target.id)

        # Destroy all monsters EOT
        for m in match_data.monster_list:
            if m.is_alive:
                m.set_destroy_eot()

    def resolve_spell_dispel_magic(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        return

    def cast_spell_counter_spell(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 0)

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castCounterSpellNobody', actor_id=spell.caster_id)
        else:
            match_data.add_log_entry(7, 'castCounterSpellResolved', actor_id=spell.caster_id, target_id=target.id)
            target.effects[match_data.current_turn]['PShield'] = 1
            target.effects[match_data.current_turn]['MShield'] = 1

    def resolve_spell_counter_spell(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        return

    def cast_spell_magic_mirror(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 0)

        target = match_data.get_actor_by_id(spell.target_id)
        caster = match_data.get_actor_by_id(spell.caster_id)

        if target is None:
            match_data.add_log_entry(5, 'castMagicMirrorNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castMagicMirrorCountered', actor_id=spell.caster_id)
        else:  # cast at target
            match_data.add_log_entry(7, 'castMagicMirrorResolved', actor_id=spell.caster_id, target_id=target.id)
            target.effects[match_data.current_turn]['MagicMirror'] = 1

    def resolve_spell_magic_mirror(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        return

    def cast_spell_raise_dead(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1, search_alive_only=0)

        target = match_data.get_actor_by_id(spell.target_id, search_alive_only=0)
        caster = match_data.get_actor_by_id(spell.caster_id)

        if target is None:
            match_data.add_log_entry(5, 'castRaiseDeadNobody', actor_id=spell.caster_id)
        elif target.turn_surrendered > -1:
            match_data.add_log_entry(5, 'castRaiseDeadSurrendered', actor_id=spell.caster_id, 
                                                                    target_id=target.id, 
                                                                    pronoun_owner_id=target.id)
        elif target.is_alive and target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castRaiseDeadCountered', actor_id=spell.caster_id)
        elif target.is_alive:
            target.increase_hp(5)
            target.states[match_data.current_turn]['risenfromdead'] = spell.caster_id
            match_data.add_log_entry(7, 'castRaiseDeadAtAliveActor', actor_id=spell.caster_id, target_id=target.id)
        else:
            if target.type == Actor.ACTOR_TYPE_MONSTER:
                target.is_alive = True
                target.destroy_eot = False
                target.hp = target.starting_hp
                target.destroy_before_attack = False
                target.controller_id = spell.caster_id
                target.init_effects_and_states(match_data.current_turn)
                target.init_effects_and_states(match_data.current_turn + 1)
                match_data.add_log_entry(10, 'castRaiseDeadActorRisen', actor_id=spell.caster_id, 
                                                                        target_id=target.id)
            else:
                match_data.add_log_entry(7, 'castRaiseDeadResolved', actor_id=spell.caster_id, target_id=target.id)
                target.states[match_data.current_turn]['risenfromdead'] = spell.caster_id


    def resolve_spell_raise_dead(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        return

    def cast_spell_summon_goblin(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

        caster = match_data.get_participant_by_id(spell.caster_id)
        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castSummonMonsterNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castSummonMonsterCountered',
                                     actor_id=spell.caster_id, spell_id=spell.id)
        else:
            monster_type = match_data.MONSTER_TYPE_GOBLIN
            self.resolve_spell_summon_monster(spell, monster_type, match_data)

    def resolve_spell_summon_goblin(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        return

    def cast_spell_summon_ogre(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

        caster = match_data.get_participant_by_id(spell.caster_id)
        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castSummonMonsterNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castSummonMonsterCountered',
                                     actor_id=spell.caster_id, spell_id=spell.id)
        else:
            monster_type = match_data.MONSTER_TYPE_OGRE
            self.resolve_spell_summon_monster(spell, monster_type, match_data)

    def resolve_spell_summon_ogre(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        return

    def cast_spell_summon_troll(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

        caster = match_data.get_participant_by_id(spell.caster_id)
        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castSummonMonsterNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castSummonMonsterCountered',
                                     actor_id=spell.caster_id, spell_id=spell.id)
        else:
            monster_type = match_data.MONSTER_TYPE_TROLL
            self.resolve_spell_summon_monster(spell, monster_type, match_data)

    def resolve_spell_summon_troll(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        return

    def cast_spell_summon_giant(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

        caster = match_data.get_participant_by_id(spell.caster_id)
        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castSummonMonsterNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castSummonMonsterCountered',
                                     actor_id=spell.caster_id, spell_id=spell.id)
        else:
            monster_type = match_data.MONSTER_TYPE_GIANT
            self.resolve_spell_summon_monster(spell, monster_type, match_data)

    def resolve_spell_summon_giant(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        return

    def cast_spell_summon_fire_elemental(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 0, 0, 0)

        monster_type = match_data.MONSTER_TYPE_FIREELEM
        self.resolve_spell_summon_monster(spell, monster_type, match_data)

    def resolve_spell_summon_fire_elemental(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        return

    def cast_spell_summon_ice_elemental(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 0, 0, 0)

        monster_type = match_data.MONSTER_TYPE_ICEELEM
        self.resolve_spell_summon_monster(spell, monster_type, match_data)

    def resolve_spell_summon_ice_elemental(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        return

    def resolve_spell_summon_monster(self, spell: Spell, monster_type: int, match_data: 'SpellbinderMatchData') -> None:
        """Template monster summon function.

        Called by specific monster summon functions.

        Arguments:
            spell (object): Spell instance, spell that is being cast
            monster_type (int): monster type
            match_data (object): SpellbinderMatchData instance, match data
        """
        # Get random pronouns and create a temporary monster.
        # Provide seed to select pronouns.
        gender = random.Random(match_data.match_id + spell.cast_turn
                               + spell.caster_id + spell.used_hand).choice([0, 1, 2])
        new_monster = match_data.create_monster(spell.caster_id, monster_type,
                                                spell.caster_id,
                                                spell.caster_id * match_data.DATA_HAND_ID_OFFSET + spell.used_hand,
                                                spell.cast_turn,
                                                gender)

        # For Goblins, Ogres, Trolls, Giants
        if monster_type in [match_data.MONSTER_TYPE_GOBLIN, match_data.MONSTER_TYPE_OGRE, 
                            match_data.MONSTER_TYPE_TROLL, match_data.MONSTER_TYPE_GIANT]:
            target = match_data.get_actor_by_id(spell.target_id)
            # Determine monster controller - if monster is summoned
            # at another monster, they share controller
            if target.type == Actor.ACTOR_TYPE_PLAYER:
                new_monster.controller_id = target.id
            elif target.type == Actor.ACTOR_TYPE_MONSTER:
                new_monster.controller_id = target.controller_id
            controller = match_data.get_participant_by_id(
                new_monster.controller_id)
            monster_id = match_data.get_next_monster_id()
            # Get new ID
            new_monster.set_actor_id(monster_id)
            # Get a random attack target (might be overridden with orders later)
            new_monster.attack_id = match_data.get_random_opponent_id(
                controller.id)
            # Add monster to the list and log the event
            match_data.monster_list.append(new_monster)
            match_data.add_log_entry(3, 'castSummonMonsterResolved',
                                     actor_id=spell.caster_id, target_id=controller.id, attack_id=new_monster.id)

        # For Fire and Ice elementals
        elif monster_type in [match_data.MONSTER_TYPE_FIREELEM, match_data.MONSTER_TYPE_ICEELEM]:
            new_monster.controller_id = 0  # spell.caster_id
            # Check for other elems present on the field.
            fire_elemental_ids = match_data.get_ids_monsters(monster_type=match_data.MONSTER_TYPE_FIREELEM)
            fire_elemental_exists = len(fire_elemental_ids)
            ice_elemental_ids = match_data.get_ids_monsters(monster_type=match_data.MONSTER_TYPE_ICEELEM)
            ice_elemental_exists = len(ice_elemental_ids)
            # Remove previous elem of the same type right now
            if monster_type == match_data.MONSTER_TYPE_FIREELEM and fire_elemental_exists:  # there are previous fire elems
                for e in fire_elemental_ids:
                    elem = match_data.get_monster_by_id(e)
                    elem.destroy_now()
            if monster_type == match_data.MONSTER_TYPE_ICEELEM and ice_elemental_exists:  # there are previous ice elems
                for e in ice_elemental_ids:
                    elem = match_data.get_monster_by_id(e)
                    elem.destroy_now()

            # Request and set ID
            monster_id = match_data.get_next_monster_id()
            new_monster.set_actor_id(monster_id)
            # Add monster to the list and log the event
            match_data.monster_list.append(new_monster)
            if monster_type == match_data.MONSTER_TYPE_FIREELEM:
                match_data.add_log_entry(4, 'castFireElementalResolved2', actor_id=spell.caster_id)
                if fire_elemental_exists:  # there are previous fire elems
                    match_data.add_log_entry(6, 'effectFireElementalsMerge', actor_id=spell.caster_id)
            elif monster_type == match_data.MONSTER_TYPE_ICEELEM:
                match_data.add_log_entry(4, 'castIceElementalResolved2', actor_id=spell.caster_id)
                if ice_elemental_exists:  # there are previous ice elems
                    match_data.add_log_entry(6, 'effectIceElementalsMerge', actor_id=spell.caster_id)

            # If both types of elems present, mark them for death before attacks
            # We do not kill them now because other elems might resolve later, and they need to merge
            fire_elemental_ids = match_data.get_ids_monsters(monster_type=match_data.MONSTER_TYPE_FIREELEM)
            fire_elemental_exists = len(fire_elemental_ids)
            ice_elemental_ids = match_data.get_ids_monsters(monster_type=match_data.MONSTER_TYPE_ICEELEM)
            ice_elemental_exists = len(ice_elemental_ids)

            if fire_elemental_exists and ice_elemental_exists:
                for e in fire_elemental_ids:
                    match_data.set_destroy_monster_before_attack_by_id(e)
                for e in ice_elemental_ids:
                    match_data.set_destroy_monster_before_attack_by_id(e)
                match_data.turns_info[match_data.current_turn]['elementals_clash'] = 1

    def cast_spell_haste(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_haste(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)

        if target is None:
            match_data.add_log_entry(5, 'castHasteNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castHasteCountered', actor_id=spell.caster_id, target_id=target.id)
        elif target.type == Actor.ACTOR_TYPE_MONSTER:
            target.effects[match_data.current_turn]['Haste'] = spell.duration
        else:
            if (target.effects[match_data.current_turn]['Haste'] < match_data.DATA_PERMANENT_DURATION
                    and target.effects[match_data.current_turn + 1]['Haste'] < match_data.DATA_PERMANENT_DURATION):
                target.effects[match_data.current_turn + 1]['Haste'] = spell.duration
                match_data.add_log_entry(7, 'castHasteResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_time_stop(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_time_stop(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)

        if target is None:
            match_data.add_log_entry(5, 'castTimeStopNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castTimeStopCountered', actor_id=spell.caster_id, target_id=target.id)
        else:
            if target.type == Actor.ACTOR_TYPE_PLAYER:
                target.effects[match_data.current_turn + 1]['TimeStop'] = 1
            else:
                target.effects[match_data.current_turn]['TimeStop'] = 1
            match_data.add_log_entry(7, 'castTimeStopResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_protection(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_protection(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)

        if target is None:
            match_data.add_log_entry(5, 'castProtectionNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castProtectionCountered', actor_id=spell.caster_id, target_id=target.id)
        else:
            if target.effects[match_data.current_turn]['Protection'] < match_data.DATA_PERMANENT_DURATION:
                target.effects[match_data.current_turn]['Protection'] = spell.duration
                match_data.add_log_entry(7, 'castProtectionResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_resist_heat(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_resist_heat(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castResistHeatNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castResistHeatCountered', actor_id=spell.caster_id, target_id=target.id)
        elif target.type == Actor.ACTOR_TYPE_MONSTER and target.monster_type == match_data.MONSTER_TYPE_FIREELEM:
            match_data.set_destroy_monster_before_attack_by_id(spell.target_id)
            match_data.add_log_entry(6, 'castResistHeatDestroysFireElemental', actor_id=spell.caster_id)
        else:
            target.effects[match_data.current_turn]['ResistHeat'] = spell.duration
            match_data.add_log_entry(7, 'castResistHeatResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_resist_cold(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_resist_cold(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castResistColdNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castResistColdCountered', actor_id=spell.caster_id, target_id=target.id)
        elif target.type == Actor.ACTOR_TYPE_MONSTER and target.monster_type == match_data.MONSTER_TYPE_ICEELEM:
            match_data.set_destroy_monster_before_attack_by_id(spell.target_id)
            match_data.add_log_entry(6, 'castResistColdDestroysIceElemental', actor_id=spell.caster_id)
        else:
            target.effects[match_data.current_turn]['ResistCold'] = spell.duration
            match_data.add_log_entry(7, 'castResistColdResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_mind_spell(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:
        """First cast phase for all mind spells.

        Mind spells:
        Paralysis, Fear, Confusion, Amnesia, Charm Monster, Charm Person

        Arguments:
            spell (object): Spell instance, spell that is being cast
            match_data (object): SpellbinderMatchData instance, match data
        """
        self.make_precast_target_checks(spell, match_data, 1, 1, 1)
        target = match_data.get_actor_by_id(spell.target_id)
        if target is not None:
            target.states[match_data.current_turn]['mindspells_this_turn'] += 1

    def cast_spell_paralysis(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.cast_spell_mind_spell(spell, match_data)

    def resolve_spell_paralysis(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castMindSpellNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castMindSpellCountered', actor_id=spell.caster_id, target_id=target.id)
        elif target.affected_by_permanent_mindspell(match_data.current_turn):
            match_data.add_log_entry(6, 'castMindSpellOverridenByPermanent',
                                     actor_id=spell.caster_id, target_id=target.id, spell_id=spell.id)
        else:
            if target.type == Actor.ACTOR_TYPE_PLAYER:
                target.effects[match_data.current_turn + 1]['Paralysis'] = spell.duration
                target.states[match_data.current_turn + 1]['paralyzed_by_id'] = spell.caster_id
            else:
                target.effects[match_data.current_turn]['Paralysis'] = spell.duration
            match_data.add_log_entry(8, 'castParalysisResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_amnesia(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.cast_spell_mind_spell(spell, match_data)

    def resolve_spell_amnesia(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castMindSpellNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castMindSpellCountered', actor_id=spell.caster_id, target_id=target.id)
        elif target.affected_by_permanent_mindspell(match_data.current_turn):
            match_data.add_log_entry(6, 'castMindSpellOverridenByPermanent',
                                     actor_id=spell.caster_id, target_id=target.id, spell_id=spell.id)
        else:
            if target.type == Actor.ACTOR_TYPE_PLAYER:
                target.effects[match_data.current_turn + 1]['Amnesia'] = spell.duration
            else:
                target.effects[match_data.current_turn]['Amnesia'] = spell.duration
            match_data.add_log_entry(8, 'castAmnesiaResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_fear(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.cast_spell_mind_spell(spell, match_data)

    def resolve_spell_fear(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castMindSpellNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castMindSpellCountered', actor_id=spell.caster_id, target_id=target.id)
        elif target.affected_by_permanent_mindspell(match_data.current_turn):
            match_data.add_log_entry(6, 'castMindSpellOverridenByPermanent',
                                     actor_id=spell.caster_id, target_id=target.id, spell_id=spell.id)
        else:
            if target.type == Actor.ACTOR_TYPE_PLAYER:
                target.effects[match_data.current_turn + 1]['Fear'] = spell.duration
            else:
                target.effects[match_data.current_turn]['Fear'] = spell.duration
            match_data.add_log_entry(8, 'castFearResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_confusion(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.cast_spell_mind_spell(spell, match_data)

    def resolve_spell_confusion(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castMindSpellNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castMindSpellCountered', actor_id=spell.caster_id, target_id=target.id)
        elif target.affected_by_permanent_mindspell(match_data.current_turn):
            match_data.add_log_entry(6, 'castMindSpellOverridenByPermanent',
                                     actor_id=spell.caster_id, target_id=target.id, spell_id=spell.id)
        else:
            if target.type == Actor.ACTOR_TYPE_PLAYER:
                target.effects[match_data.current_turn + 1]['Confusion'] = spell.duration
            else:
                target.effects[match_data.current_turn]['Confusion'] = spell.duration
            match_data.add_log_entry(8, 'castConfusionResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_charm_monster(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.cast_spell_mind_spell(spell, match_data)

    def resolve_spell_charm_monster(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        caster = match_data.get_actor_by_id(spell.caster_id)
        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castMindSpellNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castMindSpellCountered', actor_id=spell.caster_id, target_id=target.id)
        elif target.affected_by_permanent_mindspell(match_data.current_turn):
            match_data.add_log_entry(6, 'castMindSpellOverridenByPermanent',
                                     actor_id=spell.caster_id, target_id=target.id, spell_id=spell.id)
        else:
            if target.type == Actor.ACTOR_TYPE_PLAYER:
                match_data.add_log_entry(8, 'castCharmMonsterWrongTargetType',
                                         actor_id=spell.caster_id, target_id=target.id, pronoun_owner_id=target.id)
            # RB allows charming elems, but it has no real effect
            # (except for the weird like Ice Elemental looks, glassy-eyed, at caster).
            # Meanwhile, elems having no controllers is useful in other places.
            elif target.monster_type in [match_data.MONSTER_TYPE_GOBLIN, match_data.MONSTER_TYPE_OGRE, 
                                          match_data.MONSTER_TYPE_TROLL, match_data.MONSTER_TYPE_GIANT]:
                target.controller_id = caster.id
                match_data.add_log_entry(8, 'castCharmMonsterResolved', actor_id=spell.caster_id, target_id=target.id)
            else:
                match_data.add_log_entry(8, 'castCharmMonsterElemental', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_charm_person(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.cast_spell_mind_spell(spell, match_data)

    def resolve_spell_charm_person(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        caster = match_data.get_actor_by_id(spell.caster_id)
        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castMindSpellNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castMindSpellCountered', actor_id=spell.caster_id, target_id=target.id)
        elif target.affected_by_permanent_mindspell(match_data.current_turn):
            match_data.add_log_entry(6, 'castMindSpellOverridenByPermanent', 
                                     actor_id=spell.caster_id, target_id=target.id, spell_id=spell.id)
        else:
            if target.type == Actor.ACTOR_TYPE_MONSTER:
                match_data.add_log_entry(8, 'castCharmPersonWrongTargetType', actor_id=spell.caster_id, target_id=target.id)
            else:
                target.effects[match_data.current_turn + 1]['CharmPerson'] = spell.duration
                target.states[match_data.current_turn + 1]['charmed_by_id'] = caster.id
                match_data.add_log_entry(8, 'castCharmPersonResolved', actor_id=spell.caster_id, target_id=target.id)

    def resolve_spell_sickness(self, spell: Spell, match_data: 'SpellbinderMatchData', sickness_type: str):
        """Resolve Disease and Poison.

        Arguments:
            spell (object): Spell instance, spell that is being cast
            match_data (object): SpellbinderMatchData instance, match data
            sickness_type (string): 'Disease' or 'Poison'
        """
        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castSicknessNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castSicknessCountered', actor_id=spell.caster_id, target_id=target.id)
        else:
            if target.type == Actor.ACTOR_TYPE_MONSTER:
                match_data.set_destroy_actor_eot_by_id(spell.target_id)
                target.effects[match_data.current_turn][sickness_type] = 1
                match_data.add_log_entry(9, 'effectSickness1', actor_id=spell.caster_id, target_id=target.id)
            else:
                target.effects[match_data.current_turn + 1][sickness_type] = spell.duration
                match_data.add_log_entry(9, 'castSicknessResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_disease(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_disease(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        sickness_type = 'Disease'
        self.resolve_spell_sickness(spell, match_data, sickness_type)

    def cast_spell_poison(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_poison(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        sickness_type = 'Poison'
        self.resolve_spell_sickness(spell, match_data, sickness_type)

    def resolve_spell_cure_wounds(self, spell: Spell, match_data: 'SpellbinderMatchData', heal_amount: int) -> None:
        """Resolve cure wounds.

        Arguments:
            spell (object): Spell instance, spell that is being cast
            match_data (object): SpellbinderMatchData instance, match data
            heal_amount (int): Amount of HP healed
        """
        target = match_data.get_actor_by_id(spell.target_id)

        if target is None:
            match_data.add_log_entry(5, 'castCureWoundsNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castCureWoundsCountered', actor_id=spell.caster_id, target_id=target.id)
        else:
            target.increase_hp(heal_amount)
            if heal_amount == 2:
                target.effects[match_data.current_turn]['Disease'] = 0
            match_data.add_log_entry(7, 'castCureWoundsResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_cure_light_wounds(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_cure_light_wounds(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        heal_amount = 1
        self.resolve_spell_cure_wounds(spell, match_data, heal_amount)

    def cast_spell_cure_heavy_wounds(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_cure_heavy_wounds(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        heal_amount = 2
        self.resolve_spell_cure_wounds(spell, match_data, heal_amount)

    def cast_spell_antispell(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_antispell(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castAntiSpellNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castAntiSpellCountered', actor_id=spell.caster_id, target_id=target.id)
        else:
            if target.type == Actor.ACTOR_TYPE_PLAYER:
                target.states[match_data.current_turn]['antispelled'] = 1
                match_data.add_log_entry(8, 'castAntiSpellResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_blindness(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_blindness(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castBlindnessNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castBlindnessCountered', actor_id=spell.caster_id, target_id=target.id)
        else:
            if (target.type == Actor.ACTOR_TYPE_PLAYER
                    and target.effects[match_data.current_turn]['Blindness'] < match_data.DATA_PERMANENT_DURATION
                    and target.effects[match_data.current_turn + 1]['Blindness'] < match_data.DATA_PERMANENT_DURATION):
                target.effects[match_data.current_turn + 1]['Blindness'] = spell.duration
                match_data.add_log_entry(8, 'castBlindnessResolved', actor_id=spell.caster_id, target_id=target.id)
            elif target.type == Actor.ACTOR_TYPE_MONSTER:
                match_data.set_destroy_monster_before_attack_by_id(
                    spell.target_id)
                match_data.add_log_entry(11, 'castBlindnessResolvedMonster', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_invisibility(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_invisibility(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castInvisibilityNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castInvisibilityCountered', actor_id=spell.caster_id, target_id=target.id)
        else:
            if (target.type == Actor.ACTOR_TYPE_PLAYER 
                    and target.effects[match_data.current_turn]['Invisibility'] < match_data.DATA_PERMANENT_DURATION
                    and target.effects[match_data.current_turn + 1]['Invisibility'] < match_data.DATA_PERMANENT_DURATION):
                target.effects[match_data.current_turn + 1]['Invisibility'] = spell.duration
                match_data.add_log_entry(8, 'castInvisibilityResolved', actor_id=spell.caster_id, target_id=target.id)
            elif target.type == Actor.ACTOR_TYPE_MONSTER:
                match_data.set_destroy_monster_before_attack_by_id(spell.target_id)
                match_data.add_log_entry(11, 'castInvisibilityResolvedMonster', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_permanency(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_permanency(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castPermanencyAndDelayNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castPermanencyAndDelayCountered', actor_id=spell.caster_id, target_id=target.id)
        else:
            if (target.type == Actor.ACTOR_TYPE_PLAYER
                    and target.effects[match_data.current_turn]['Permanency'] < match_data.DATA_PERMANENT_DURATION
                    and target.effects[match_data.current_turn + 1]['Permanency'] < match_data.DATA_PERMANENT_DURATION):
                target.effects[match_data.current_turn + 1]['Permanency'] = spell.duration
                match_data.add_log_entry(7, 'castPermanencyAndDelayResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_delay_effect(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_delay_effect(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castPermanencyAndDelayNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castPermanencyAndDelayCountered', actor_id=spell.caster_id, target_id=target.id)
        else:
            if (target.type == Actor.ACTOR_TYPE_PLAYER 
                    and target.effects[match_data.current_turn]['DelayEffect'] < match_data.DATA_PERMANENT_DURATION
                    and target.effects[match_data.current_turn + 1]['DelayEffect'] < match_data.DATA_PERMANENT_DURATION):
                target.effects[match_data.current_turn + 1]['DelayEffect'] = spell.duration
                match_data.add_log_entry(7, 'castPermanencyAndDelayResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_remove_enchantment(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_remove_enchantment(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castRemoveEnchantmentNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castRemoveEnchantmentCountered', actor_id=spell.caster_id, target_id=target.id)
        else:
            target.remove_enchantments(match_data.current_turn)
            if target.type == Actor.ACTOR_TYPE_PLAYER:
                match_data.add_log_entry(8, 'castRemoveEnchantmentResolved', actor_id=spell.caster_id, target_id=target.id)
            elif target.type == Actor.ACTOR_TYPE_MONSTER:
                match_data.set_destroy_actor_eot_by_id(spell.target_id)
                match_data.add_log_entry(11, 'castRemoveEnchantmentResolvedMonster', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_shield(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_shield(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castShieldNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castShieldCountered', actor_id=spell.caster_id)
        else:
            target.effects[match_data.current_turn]['PShield'] = 1
            match_data.add_log_entry(7, 'castShieldResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_magic_missile(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_magic_missile(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        # ignore protection during timestopped turns, but still check shields
        check_pshield = True
        check_protection = not match_data.is_current_turn_timestopped()

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castMagicMissileNobody', actor_id=spell.caster_id)
        elif target.affected_by_pshield(match_data.current_turn, check_pshield, check_protection):
            match_data.add_log_entry(9, 'castMagicMissileCountered', actor_id=spell.caster_id, target_id=target.id)
        else:
            target.decrease_hp(1)
            match_data.add_log_entry(9, 'castMagicMissileResolved', actor_id=spell.caster_id, target_id=target.id)

    def resolve_spell_cause_wounds(self, spell: Spell, match_data: 'SpellbinderMatchData', damage_amount: int) -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castCauseWoundsNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castCauseWoundsCountered', actor_id=spell.caster_id, target_id=target.id)
        else:
            target.decrease_hp(damage_amount)
            match_data.add_log_entry(9, 'castCauseWoundsResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_cause_light_wounds(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_cause_light_wounds(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        damage_amount = 2
        self.resolve_spell_cause_wounds(spell, match_data, damage_amount)

    def cast_spell_cause_heavy_wounds(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_cause_heavy_wounds(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        damage_amount = 3
        self.resolve_spell_cause_wounds(spell, match_data, damage_amount)

    def cast_spell_fireball(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_fireball(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castFireballNobody', actor_id=spell.caster_id)
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(10, 'castFireballCountered', actor_id=spell.caster_id, target_id=target.id)
        else:
            if target.type == Actor.ACTOR_TYPE_MONSTER and target.monster_type == match_data.MONSTER_TYPE_ICEELEM:
                match_data.set_destroy_monster_before_attack_by_id(
                    spell.target_id)
                match_data.add_log_entry(11, 'castFireballIceElemental', actor_id=spell.caster_id)
            elif match_data.turns_info[match_data.current_turn]['ice_storms']:
                # will be handled during Ice Storm resolution
                target.states[match_data.current_turn]['fireballed'] = 1
            elif ((not match_data.is_current_turn_timestopped())
                    and target.affected_by_resist_heat_permanent(match_data.current_turn)):
                match_data.add_log_entry(7, 'castFireballResistHeat',
                                         actor_id=spell.caster_id, target_id=target.id, pronoun_owner_id=target.id)
            else:
                target.decrease_hp(5)
                match_data.add_log_entry(9, 'castFireballResolved',
                                         actor_id=spell.caster_id, target_id=target.id, pronoun_owner_id=target.id)

    def cast_spell_lightning_bolt(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_lightning_bolt(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        caster = match_data.get_actor_by_id(spell.caster_id)
        if spell.used_pattern['notation'] == 'WDDc' and caster.states[match_data.current_turn]['clap_of_lightning'] > 0:
            match_data.add_log_entry(10, 'castClapOfLightningFizzle', actor_id=spell.caster_id)
        else:
            if spell.used_pattern['notation'] == 'WDDc':
                caster.states[match_data.current_turn]['clap_of_lightning'] += 1
            target = match_data.get_actor_by_id(spell.target_id)
            if target is None:
                match_data.add_log_entry(5, 'castLightningBoltNobody')
            elif target.affected_by_mshield(match_data.current_turn):
                match_data.add_log_entry(10, 'castLightningBoltCountered', actor_id=spell.caster_id, target_id=target.id)
            else:
                target.decrease_hp(5)
                match_data.add_log_entry(9, 'castLightningBoltResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_finger_of_death(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_finger_of_death(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(5, 'castFingerOfDeathNobody', actor_id=spell.caster_id)
        elif target.states[match_data.current_turn]['risenfromdead'] == 1:
            match_data.add_log_entry(10, 'castRaiseDeadFoD', actor_id=spell.caster_id, target_id=target.id)
        else:
            match_data.set_destroy_actor_eot_by_id(spell.target_id)
            match_data.add_log_entry(9, 'castFingerOfDeathResolved', actor_id=spell.caster_id, target_id=target.id)

    def cast_spell_fire_storm(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 0, 0, 0)
        caster = match_data.get_participant_by_id(spell.caster_id)
        match_data.turns_info[match_data.current_turn]['fire_storms'] += 1

    def resolve_spell_fire_storm(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        match_data.add_log_entry(9, 'castFireStormResolved', actor_id=spell.caster_id)
        for p in match_data.participant_list:
            if p.is_alive:
                if ((not match_data.is_current_turn_timestopped())
                        and p.affected_by_resist_heat_permanent(match_data.current_turn)):
                    match_data.add_log_entry(9, 'effectResistHeat', actor_id=spell.caster_id, attack_id=p.id)
                elif p.affected_by_mshield(match_data.current_turn):
                    match_data.add_log_entry(9, 'effectStormProtectedByMShield', actor_id=spell.caster_id, target_id=p.id)
                else:
                    p.decrease_hp(5)
                    match_data.add_log_entry(9, 'effectFireStormDamaged', actor_id=spell.caster_id, target_id=p.id)
        for m in match_data.monster_list:
            if m.is_alive:
                if ((not match_data.is_current_turn_timestopped())
                        and m.affected_by_resist_heat_permanent(match_data.current_turn)):
                    match_data.add_log_entry(9, 'effectResistHeat', actor_id=spell.caster_id, attack_id=m.id)
                elif m.affected_by_mshield(match_data.current_turn):
                    match_data.add_log_entry(9, 'effectStormProtectedByMShield', actor_id=spell.caster_id, target_id=m.id)
                else:
                    m.decrease_hp(5)
                    match_data.add_log_entry(9, 'effectFireStormDamaged', actor_id=spell.caster_id, target_id=m.id)

    def cast_spell_ice_storm(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        self.make_precast_target_checks(spell, match_data, 0, 0, 0)
        caster = match_data.get_participant_by_id(spell.caster_id)
        match_data.turns_info[match_data.current_turn]['ice_storms'] += 1

    def resolve_spell_ice_storm(self, spell: Spell, match_data: 'SpellbinderMatchData') -> None:

        target = match_data.get_actor_by_id(spell.target_id)
        match_data.add_log_entry(9, 'castIceStormResolved')
        for p in match_data.participant_list:
            if p.is_alive:
                if ((not match_data.is_current_turn_timestopped())
                        and p.affected_by_resist_cold_permanent(match_data.current_turn)):
                    match_data.add_log_entry(9, 'effectResistCold', actor_id=spell.caster_id, attack_id=p.id)
                elif p.affected_by_mshield(match_data.current_turn):
                    match_data.add_log_entry(9, 'effectStormProtectedByMShield', actor_id=spell.caster_id, target_id=p.id)
                elif p.states[match_data.current_turn]['fireballed']:
                    match_data.add_log_entry(7, 'castFireballIceStorm', actor_id=spell.caster_id, target_id=p.id)
                else:
                    p.decrease_hp(5)
                    match_data.add_log_entry(9, 'effectIceStormDamaged', actor_id=spell.caster_id, target_id=p.id)
        for m in match_data.monster_list:
            if m.is_alive:
                if ((not match_data.is_current_turn_timestopped())
                        and m.affected_by_resist_cold_permanent(match_data.current_turn)):
                    match_data.add_log_entry(9, 'effectResistCold', actor_id=spell.caster_id, attack_id=m.id)
                elif m.affected_by_mshield(match_data.current_turn):
                    match_data.add_log_entry(9, 'effectStormProtectedByMShield', actor_id=spell.caster_id, target_id=m.id)
                elif m.states[match_data.current_turn]['fireballed']:
                    match_data.add_log_entry(7, 'castFireballIceStorm', actor_id=spell.caster_id, target_id=m.id)
                else:
                    m.decrease_hp(5)
                    match_data.add_log_entry(9, 'effectIceStormDamaged', actor_id=spell.caster_id, target_id=m.id)
