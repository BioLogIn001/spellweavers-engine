import re


class Spell:
    ''' Class for Spells (duh).

    Each spell has a lot of stuff, see comments below for now.
    '''

    def __init__(self, spell_id, spell_priority, spell_name, spell_gestures,
                 spell_default_target, spell_duration, spellbook_dictionary):

        # Spell ID
        self.id = spell_id
        # spell priority, the lower priority = the earlier spell is cast
        self.priority = spell_priority
        # A string with spell name
        self.name = spell_name
        # A string with default target types {nobody, self, opponent}
        self.default_target = spell_default_target
        # Integer, spell duration in turns
        self.duration = spell_duration
        # Gesture pattern(s) that can be used to cast this spell
        self.patterns = []

        # Transform ingame pattern notation to (reversed) patterns for both hands.
        # For example, 'SWDDc' is transformed into 'CDDWS' for the main hand
        # and 'C....' for the offhand.
        for spell_notation in spell_gestures:
            notation_reversed = spell_notation[::-1]
            offhand_pattern_reversed_tmp = notation_reversed.translate(
                notation_reversed.maketrans(spellbook_dictionary)
            )
            mainhand_reversed = notation_reversed.upper()
            offhand_reversed = offhand_pattern_reversed_tmp.upper()
            requires_both_hands_tmp = (offhand_reversed[0] != '.') + 1
            pattern = {'notation': spell_notation,
                       'mainhand_reversed': mainhand_reversed,
                       'offhand_reversed': offhand_reversed,
                       'length': len(spell_notation),
                       'hands_required': requires_both_hands_tmp}
            self.patterns.append(pattern)

        # Dictionary entry with info about pattern used to cast an instance of a spell
        self.used_pattern = {}

        # Integer ID of caster
        self.caster_id = 0
        # Integer ID of target
        self.target_id = 0
        # Integer [1, 2] of [left, right] hand used to cast the spell
        self.used_hand = 0
        # Integer, number of the turn on which the spell was cast
        self.cast_turn = 0
        # Boolean flag to mark spell for future resolution
        self.resolve = 0
        # Boolean flag to check if the spell was mirrored during the resolution
        self.mirrored = 0
        # Boolean flag to check if the spell was delayed and later fired
        self.delayed = 0


class SpellBook:
    ''' Basic SpellBook class. To be inherited by different spellbook implementations.

    Mostly has spell roster and gesture dictionary (for the match), 
    and two heaps and a stack of spells to cast (for the turn)
    '''

    def __init__(self, spellbook_title, spellbook_dictionary):

        self.title = spellbook_title
        # Dictionary of possible gestures
        self.dictionary = spellbook_dictionary
        # List of Spell instances possible for this spellbook
        self.spells = []

        # Lists of Spell instances that were matched with gestures on a specific turn for a specific player
        self.possible_spells_lh = []
        self.possible_spells_rh = []

        # List of Spell instances that were selected to cast for a specific turn
        self.stack = []

        # default value to be overridden by custom spellbooks
        self.max_spell_length = 10

    def add_spell(self, spell_definition, spell_names):
        ''' Import spell information and populate self.spells

        Arguments:
        spell_definition -- a dictionary with spell definitions
        spell_names -- dictionary with loc string names of spells
        '''

        spell = Spell(spell_definition['id'],
                      spell_definition['priority'],
                      spell_names[spell_definition['id']],
                      spell_definition['patterns'],
                      spell_definition['default_target'],
                      spell_definition['duration'],
                      self.dictionary)
        self.spells.append(spell)

    def select_spell_target(self, order_target_id, spell_default_target,
                            participant_id, match_data):
        ''' Select target for the spell based on participant's orders and the 
        default target for this particular spell. 

        Arguments:
        order_target_id -- int, target_id submitted by the participant
        spell_default_target -- str, default target type of the spell (self, opponent, nobody)
        participant_id -- int, ID of caster
        match_data -- match_data-inherited object, match data

        Returns:
        target_id -- int, selected spell target
        '''

        target_id = -1
        if order_target_id == 0:
            # Target nobody
            target_id = 0
        elif (order_target_id > 0) and (order_target_id in match_data.get_list_of_targets_ids()):
            # target existing actor or hand
            target_id = order_target_id
        elif spell_default_target == 'self':
            # target caster
            target_id = participant_id
        elif spell_default_target == 'opponent':
            # target random opponent
            target_id = match_data.get_random_opponent_id(participant_id)
        else:  # castSpellLH.defaulTarget == 'nobody':
            # Target nobody
            target_id = 0
        return target_id

    def clear_stack(self):
        ''' Clear stack and heaps. To be called between turns.

        This placeholder is unlikely to be used after switching to web version, 
        but we need this for JSON-fed version of engine.
        '''

        self.stack = []
        self.possible_spells_lh = []
        self.possible_spells_rh = []

    def add_spell_to_stack(self, spell):
        ''' Add a spell to the self.stack to be cast this turn.

        Arguments:
        spell -- an Spell object to be added to the list
        '''

        self.stack.append(spell)

    def sort_spells_by_priority(self):
        '''Sort spells in spell.stack by priority.
        (Spells with lesser priority get cast first, so technically this is 
        not a stack, but queue.)
        '''

        self.stack.sort(key=lambda spell: spell.priority)

    def cast_spells(self, match_data):
        ''' Cast spells waiting in the queue, calling spell-specific function
        For example, for Dispel Magic spell we use SpellDispelMagic parameter
        from Definitions to call self.castSpellDispelMagic()

        Arguments:
        match_data -- match_data-inherited object, match data
        '''

        for spell in self.stack:
            for d in self.spell_definitions:
                if spell.id == d['id']:
                    func_name = getattr(self, 'cast_spell_' + d['code'])
                    func_name(spell, match_data)
                    break

    def resolve_spells(self, match_data):
        ''' Resolve spells waiting in the queue, calling spell-specific function
        For example, for Dispel Magic spell we use SpellDispelMagic parameter
        from Definitions to call self.resolveSpellDispelMagic()

        We resolve only spells with spell.resolve == 1, which allows to omit 
        some of the previously cast spells that were countered, clashed, etc.

        Arguments:
        match_data -- match_data-inherited object, match data
        '''

        for spell in self.stack:
            if spell.resolve == 1:
                for d in self.spell_definitions:
                    if spell.id == d['id']:
                        func_name = getattr(self, 'resolve_spell_' + d['code'])
                        func_name(spell, match_data)
                        break

    def match_spell_pattern(self, match_data):
        '''Check participant's gestures to form two lists (possible_spells_lh 
        and possible_spells_rh) of matched spells, that could potentially be cast 
        by participant this turn.

        Arguments:
        participant_id -- ID of the participant 
        match_data -- match_data-inherited object, match data
        spells -- dictionary of spells from match spellBook 
        '''

        for participant_id in match_data.get_list_of_participants_ids():
            # Cycle through all (reversed) patterns of all spells.
            # Check these patterns against current player (reversed) pattern.
            # If specific pattern is matches, add spell to the list of
            # possible spells for the respective hand.
            gestures_lh = match_data.get_gesture_history(participant_id, 1)
            gestures_rh = match_data.get_gesture_history(participant_id, 2)
            # We cut all patterns to max_spell_length cause we do not need more for matching
            pattern_lh_reversed = gestures_lh[:-self.max_spell_length-1:-1]
            pattern_rh_reversed = gestures_rh[:-self.max_spell_length-1:-1]
            for spell in self.spells:
                for pattern in spell.patterns:
                    # check spell pattern for LH as mainhand
                    mainhand_match = re.search('^' + pattern['mainhand_reversed']
                                               + '.*$', pattern_lh_reversed)
                    offhand_match = re.search('^' + pattern['offhand_reversed']
                                              + '.*$', pattern_rh_reversed)
                    if mainhand_match and offhand_match:
                        l = [pattern['notation']]
                        spell_tmp = Spell(spell.id,
                                          spell.priority,
                                          spell.name,
                                          l,
                                          spell.default_target,
                                          spell.duration,
                                          self.dictionary)
                        spell_tmp.used_pattern = pattern
                        spell_tmp.caster_id = participant_id
                        self.possible_spells_lh.append(spell_tmp)
                    # check spell pattern for RH as mainhand
                    mainhand_match = re.search('^' + pattern['mainhand_reversed']
                                               + '.*$', pattern_rh_reversed)
                    offhand_match = re.search('^' + pattern['offhand_reversed']
                                              + '.*$', pattern_lh_reversed)
                    if mainhand_match and offhand_match:
                        #spell_tmp = spell
                        l = [pattern['notation']]
                        spell_tmp = Spell(spell.id,
                                          spell.priority,
                                          spell.name,
                                          l,
                                          spell.default_target,
                                          spell.duration,
                                          self.dictionary)
                        spell_tmp.used_pattern = pattern
                        spell_tmp.caster_id = participant_id
                        self.possible_spells_rh.append(spell_tmp)

    def search_spell_set_by_id(self, hand, ordered_spell_id, caster_id):
        '''Search previously formed spell lists by ID.
        This is used to choose the spell to cast if
        - the player ordered this spell for this hand,
        - and this spell exists in the list of spells with matched patterns.

        Arguments:
        hand -- 1 for LH, 2 for RH
        ordered_spell_id -- spell ID from participant's orders for the turn
        caster_id -- ID of the participant that cast this spell

        Returns:
        selected_spell -- an instance of of Spell class if spell is found,
        None otherwise.
        '''

        selected_spell = None
        if hand == 1:
            for spell in self.possible_spells_lh:
                if (spell.id == ordered_spell_id) and (spell.caster_id == caster_id):
                    # return fresh instance of Spell since possible_spells_lh is mutable
                    l = [spell.used_pattern['notation']]
                    selected_spell = Spell(spell.id,
                                           spell.name,
                                           l,
                                           spell.default_target,
                                           spell.duration,
                                           self.dictionary)
                    selected_spell.used_pattern = spell.used_pattern
                    selected_spell.caster_id = spell.caster_id
                    selected_spell.used_hand = hand
                    break
        elif hand == 2:
            for spell in self.possible_spells_rh:
                if (spell.id == ordered_spell_id) and (spell.caster_id == caster_id):
                    # return fresh instance of Spell since possible_spells_rh is mutable
                    l = [spell.used_pattern['notation']]
                    selected_spell = Spell(spell.id,
                                           spell.name,
                                           l,
                                           spell.default_target,
                                           spell.duration,
                                           self.dictionary)
                    selected_spell.used_pattern = spell.used_pattern
                    selected_spell.caster_id = spell.caster_id
                    selected_spell.used_hand = hand
                    break
        return selected_spell

    def search_spell_set_by_length(self, hand, selected_spell, hand_count, caster_id):
        '''Search previously formed spell lists by length and number of hands.
        This is used to choose the spell to cast if
        - the player ordered nothing 
        - or we didn't find what player ordered in the lists.
        The longest spell gets selected.

        Arguments:
        hand -- 1 for LH, 2 for RH
        selected_spell -- Spell instance previously selected by other means
        hand_count -- 1 to look for 1-handed patterns only, 
        2 to look for 2-handed patterns
        caster_id -- ID of the participant that cast this spell

        Returns:
        selected_spell -- updated value for argument, None or spell.
        '''

        if hand == 1:
            possible_spells = self.possible_spells_lh
        elif hand == 2:
            possible_spells = self.possible_spells_rh
        for spell in possible_spells:
            if ((spell.used_pattern['hands_required'] == hand_count)
                    and (spell.caster_id == caster_id)):
                if ((selected_spell is None) or (selected_spell.used_pattern['length']
                                                 < spell.used_pattern['length'])):
                    # return fresh instance of Spell since possible_spells is mutable
                    l = [spell.used_pattern['notation']]
                    selected_spell = Spell(spell.id,
                                           spell.priority,
                                           spell.name,
                                           l,
                                           spell.default_target,
                                           spell.duration,
                                           self.dictionary)
                    selected_spell.used_pattern = spell.used_pattern
                    selected_spell.caster_id = spell.caster_id
                    selected_spell.used_hand = hand
        return selected_spell
