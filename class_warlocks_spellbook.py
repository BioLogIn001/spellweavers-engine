from class_spellbook import SpellBook


class WarlocksSpellBook(SpellBook):
    def __init__(self, spell_names):
        """Init spellbook.
        
        Args:
            spell_names (dict): a dictionary with localized spell names
        """
        title = "Ravenblack's Warlocks (ParaFC Maladroit)"
        spell_dict = {'C': '.', 'D': '.', 'F': '.',
                      'P': '.', 'S': '.', 'W': '.', 'T': '.'}
        SpellBook.__init__(self, title, spell_dict)

        self.spell_dict_parafc = {'C': 'C', 'D': 'D',
                                  'F': 'C', 'P': 'P', 'S': 'D', 'W': 'P', 'T': 'T'}
        self.spell_dict_fear = {'C': 'W', 'D': 'W',
                                'F': 'W', 'P': 'P', 'S': 'W', 'W': 'W', 'T': 'T'}
        self.valid_gestures = ['C', 'D', 'F', 'P', 'S', 'W', '>', '-']
        self.valid_spell_ids = range(1, 41)

        self.max_spell_length = 8

        self.spell_definitions = [
            {'id': 1, 'priority': 1, 'patterns': [
                "cDPW"], 'default_target':'self', 'duration':1, 'code':'dispel_magic'},
            {'id': 2, 'priority': 2, 'patterns': [
                "WPP", "WWS"], 'default_target':'self', 'duration':1, 'code':'counter_spell'},
            {'id': 3, 'priority': 3, 'patterns': [
                "cw"], 'default_target':'self', 'duration':1, 'code':'magic_mirror'},
            {'id': 4, 'priority': 4, 'patterns': [
                "SFW"], 'default_target':'self', 'duration':1, 'code':'summon_goblin'},
            {'id': 5, 'priority': 5, 'patterns': [
                "PSFW"], 'default_target':'self', 'duration':1, 'code':'summon_ogre'},
            {'id': 6, 'priority': 6, 'patterns': [
                "FPSFW"], 'default_target':'self', 'duration':1, 'code':'summon_troll'},
            {'id': 7, 'priority': 7, 'patterns': [
                "WFPSFW"], 'default_target':'self', 'duration':1, 'code':'summon_giant'},
            {'id': 8, 'priority': 8, 'patterns': [
                "cWSSW"], 'default_target':'nobody', 'duration':1, 'code':'summon_fire_elemental'},
            {'id': 9, 'priority': 9, 'patterns': [
                "cSWWS"], 'default_target':'nobody', 'duration':1, 'code':'summon_ice_elemental'},
            {'id': 10, 'priority': 10, 'patterns': [
                "PWPWWc"], 'default_target':'self', 'duration':3, 'code':'haste'},
            {'id': 11, 'priority': 11, 'patterns': [
                "SPPc", "SPPFD"], 'default_target':'self', 'duration':1, 'code':'time_stop'},
            {'id': 12, 'priority': 12, 'patterns': [
                "WWP"], 'default_target':'self', 'duration':3, 'code':'protection'},
            {'id': 13, 'priority': 13, 'patterns': [
                "WWFP"], 'default_target':'self', 'duration':9999, 'code':'resist_heat'},
            {'id': 14, 'priority': 14, 'patterns': [
                "SSFP"], 'default_target':'self', 'duration':9999, 'code':'resist_cold'},
            {'id': 15, 'priority': 15, 'patterns': [
                "FFF"], 'default_target':'opponent', 'duration':1, 'code':'paralysis'},
            {'id': 16, 'priority': 16, 'patterns': [
                "DPP"], 'default_target':'opponent', 'duration':1, 'code':'amnesia'},
            {'id': 17, 'priority': 17, 'patterns': [
                "SWD"], 'default_target':'opponent', 'duration':1, 'code':'fear'},
            {'id': 18, 'priority': 18, 'patterns': [
                "DSF"], 'default_target':'opponent', 'duration':1, 'code':'maladroitness'},
            {'id': 19, 'priority': 19, 'patterns': [
                "PSDD"], 'default_target':'self', 'duration':1, 'code':'charm_monster'},
            {'id': 20, 'priority': 20, 'patterns': [
                "PSDF"], 'default_target':'opponent', 'duration':1, 'code':'charm_person'},
            {'id': 21, 'priority': 21, 'patterns': [
                "DSFFFc"], 'default_target':'opponent', 'duration':6, 'code':'disease'},
            {'id': 22, 'priority': 22, 'patterns': [
                "DWWFWD"], 'default_target':'opponent', 'duration':6, 'code':'poison'},
            {'id': 23, 'priority': 23, 'patterns': [
                "DFW"], 'default_target':'self', 'duration':1, 'code':'cure_light_wounds'},
            {'id': 24, 'priority': 24, 'patterns': [
                "DFPW"], 'default_target':'self', 'duration':1, 'code':'cure_heavy_wounds'},
            {'id': 25, 'priority': 25, 'patterns': [
                "SPFP"], 'default_target':'opponent', 'duration':1, 'code':'antispell'},
            {'id': 26, 'priority': 26, 'patterns': [
                "DFWFd", "DWFFd"], 'default_target':'opponent', 'duration':3, 'code':'blindness'},
            {'id': 27, 'priority': 27, 'patterns': [
                "PPws"], 'default_target':'self', 'duration':3, 'code':'invisibility'},
            {'id': 28, 'priority': 28, 'patterns': [
                "SPFPSDW"], 'default_target':'self', 'duration':3, 'code':'permanency'},
            {'id': 29, 'priority': 29, 'patterns': [
                "DWSSSP"], 'default_target':'self', 'duration':3, 'code':'delay_effect'},
            {'id': 30, 'priority': 30, 'patterns': [
                "PDWP"], 'default_target':'opponent', 'duration':1, 'code':'remove_enchantment'},
            {'id': 31, 'priority': 31, 'patterns': [
                "P"], 'default_target':'self', 'duration':1, 'code':'shield'},
            {'id': 32, 'priority': 32, 'patterns': [
                "SD"], 'default_target':'opponent', 'duration':1, 'code':'magic_missile'},
            {'id': 33, 'priority': 33, 'patterns': [
                "WFP"], 'default_target':'opponent', 'duration':1, 'code':'cause_light_wounds'},
            {'id': 34, 'priority': 34, 'patterns': [
                "WPFD"], 'default_target':'opponent', 'duration':1, 'code':'cause_heavy_wounds'},
            {'id': 35, 'priority': 35, 'patterns': [
                "FSSDD"], 'default_target':'opponent', 'duration':1, 'code':'fireball'},
            {'id': 36, 'priority': 36, 'patterns': [
                "DFFDD"], 'default_target':'opponent', 'duration':1, 'code':'lightning_bolt'},
            {'id': 37, 'priority': 37, 'patterns': [
                "WDDc"], 'default_target':'opponent', 'duration':1, 'code':'clap_of_lightning'},
            {'id': 38, 'priority': 38, 'patterns': [
                "PWPFSSSD"], 'default_target':'opponent', 'duration':1, 'code':'finger_of_death'},
            {'id': 39, 'priority': 39, 'patterns': [
                "SWWc"], 'default_target':'nobody', 'duration':1, 'code':'fire_storm'},
            {'id': 40, 'priority': 40, 'patterns': [
                "WSSc"], 'default_target':'nobody', 'duration':1, 'code':'ice_storm'}
        ]

        for spell_definition in self.spell_definitions:
            self.add_spell(spell_definition, spell_names)

    def get_ids_spells_permanentable(self):
        """
        Return a list of spell IDs that can be made permanent:
            Haste, Protection, Paralysis, Amnesia, Maladroitness, Fear, Charm Person, 
            Blindness, Invisibility, Permanency, Delay Effect
        
        Returns:
            list: IDs of spells
        """

        return [10, 12, 15, 16, 17, 18, 20, 26, 27, 28, 29]

    def get_ids_mindspells(self):
        """
        Return a list of spell IDs that are considered mind spells:
            Paralysis, Amnesia, Fear, Maladroitness, Charm Monster, Charm Person
        
        Returns:
            list: IDs of spells
        """

        return [15, 16, 17, 18, 19, 20]

    def get_ids_spells_storms(self):
        """
        Return a list of spell IDs that are considered storms:
            Fire Storm, Ice Storm
        
        Returns:
            list: IDs of spells
        """

        return [39, 40]

    def get_ids_spells_dispel_magic(self):
        """
        Return a list of spell IDs that are considered Dispel Magic:
            Dispel Magic
        
        Returns:
            list: IDs of spells
        """

        return [1]

    def get_ids_spells_fire_storm(self):
        """
        Return a list of spell IDs that are considered Fire Storm:
            Fire Storm
        
        Returns:
            list: IDs of spells
        """

        return [39]

    def get_ids_spells_ice_storm(self):
        """
        Return a list of spell IDs that are considered Ice Storm:
            Ice Storm
        
        Returns:
            list: IDs of spells
        """

        return [40]

    def effect_paralysis(self, gesture):
        """Filter gestures according to ParaFC Paralysis effect
        
        Arguments:
            gesture (string): gesture to be filtered
        
        Returns:
            newGesture (string): filtered gesture
        """

        new_gesture = gesture.translate(
            gesture.maketrans(self.spell_dict_parafc))
        return new_gesture

    def effect_fear(self, gesture):
        """Filter gestures according to Fear effect
        
        Arguments:
            gesture (string): gesture to be filtered
        
        Returns:
            newGesture (string): filtered gesture
        """

        newGesture = gesture.translate(gesture.maketrans(self.spell_dict_fear))
        return newGesture

    def log_effects_sot(self, match_orders, match_data):
        """Log messages related to effects that are checked at the Start of the Turn
        
        Arguments:
            match_orders (object): WarlocksOrders instance, match orders
            match_data (object): WarlocksMatchData instance, match data
        """

        # Log entries for timestopped and hasted turns
        if match_data.is_current_turn_timestopped():
            match_data.add_log_entry(0, 7, 'effectTimeStop')
        if match_data.is_current_turn_hasted():
            match_data.add_log_entry(0, 7, 'effectHaste')

        # Check other turn effects
        # Ignore all effects on timestopped turn
        if not match_data.is_current_turn_timestopped():
            for participant_id in match_data.get_ids_participants():
                p = match_data.get_participant_by_id(participant_id)

                # Check participant for Disease and Poison
                if p.affected_by_disease(match_data.current_turn):
                    if p.effects[match_data.current_turn]['Disease'] in [1, 2, 3, 4, 5, 6]:
                        strtmp = 'effectSickness' + str(p.effects[match_data.current_turn]['Disease'])
                        match_data.add_log_entry(p.id, 9, strtmp,
                                                 name=p.name)
                if p.affected_by_poison(match_data.current_turn):
                    if p.effects[match_data.current_turn]['Poison'] in [1, 2, 3, 4, 5, 6]:
                        strtmp = 'effectSickness' + str(p.effects[match_data.current_turn]['Poison'])
                        match_data.add_log_entry(p.id, 9, strtmp,
                                                 name=p.name)

                # Check participant for mindspells
                if (p.affected_by_paralysis(match_data.current_turn)
                        and p.states[match_data.current_turn]['paralyzed_by_id'] in match_data.get_ids_participants_active()):
                    if p.states[match_data.current_turn]['paralyzed_hand_id'] == p.get_lh_id():
                        handname = match_data.get_text_strings_by_code(
                            'nameLeftHand')
                    # Default to RH para if for some reasons there were no clear order
                    else:
                        handname = match_data.get_text_strings_by_code(
                            'nameRightHand')
                    match_data.add_log_entry(p.id, 8, 'effectParalysis1',
                                             targetname=p.name, handname=handname)
                if p.affected_by_amnesia(match_data.current_turn):
                    match_data.add_log_entry(p.id, 8, 'effectAmnesia1',
                                             targetname=p.name)
                if p.affected_by_fear(match_data.current_turn):
                    match_data.add_log_entry(p.id, 8, 'effectFear1',
                                             targetname=p.name)
                if p.affected_by_maladroitness(match_data.current_turn):
                    match_data.add_log_entry(p.id, 8, 'effectMaladroitness1',
                                             targetname=p.name)
                if (p.affected_by_charm_person(match_data.current_turn)
                        and p.states[match_data.current_turn]['charmed_by_id'] in match_data.get_ids_participants_active()):
                    if p.states[match_data.current_turn]['charmed_hand_id'] == p.get_lh_id():
                        handname = match_data.get_text_strings_by_code(
                            'nameLeftHand')
                    # Default to RH charm if for some reasons there were no clear order
                    else:
                        handname = match_data.get_text_strings_by_code(
                            'nameRightHand')
                    if p.states[match_data.current_turn]['charmed_same_gestures'] == 1:
                        match_data.add_log_entry(p.id, 8, 'effectCharmPerson2',
                                                 targetname=p.name, pronoun=p.pronoun_a)
                    else:
                        match_data.add_log_entry(p.id, 8, 'effectCharmPerson1',
                                                 targetname=p.name, pronoun=p.pronoun_c, handname=handname)

    def log_gesture_messages(self, match_data):
        """Log messages related to shown gestures
        
        Arguments:
            match_data (object): WarlocksMatchData instance, match data
        """

        for participant_id in match_data.get_ids_participants_active():
            p = match_data.get_participant_by_id(participant_id)
            # For each participant taking action this turn get gestures
            gesture_lh = match_data.get_gesture_last(participant_id, 1)
            gesture_rh = match_data.get_gesture_last(participant_id, 2)
            # Get respective unformatted text strings
            gesture_texts = match_data.get_gesture_log_entry(
                gesture_lh, gesture_rh)
            handname = match_data.get_text_strings_by_code('nameLeftHand')
            # Log entried for LH (and RH if available)
            # For Warlocks, RH is omitted in case of a clap
            match_data.add_log_entry(p.id, 1, gesture_texts[0],
                                     name=p.name, pronoun=p.pronoun_c, handname=handname)
            if gesture_texts[1]:
                handname = match_data.get_text_strings_by_code('nameRightHand')
                match_data.add_log_entry(p.id, 1, gesture_texts[1],
                                         name=p.name, pronoun=p.pronoun_c, handname=handname)

    def determine_gestures(self, match_orders, match_data):
        """Determine participants gesture for the turn based on the orders and
        effects they are affected with.
        
        Arguments:
            match_orders (object): WarlocksOrders instance, match orders
            match_data (object): WarlocksMatchData instance, match data
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
                    if p.states[match_data.current_turn]['paralyzed_hand_id'] == p.get_lh_id():
                        prev_gesture = match_data.get_gesture(
                            participant_id, match_data.current_turn-1, 1)
                        gesture_lh = self.effect_paralysis(prev_gesture)
                    # elif paralyzeHandID == p.get_rh_id():
                    else:
                        prev_gesture = match_data.get_gesture(
                            participant_id, match_data.current_turn-1, 2)
                        gesture_rh = self.effect_paralysis(prev_gesture)
                    # match_data.add_log_entry(p.id, 8, 'effect_paralysis1',
                    #                           targetname = p.name, handname = handname)
                if p.affected_by_amnesia(match_data.current_turn):
                    # If participant is affected by Amnesia, for both hands
                    # use their previous gestures
                    gesture_lh = match_data.get_gesture(
                        participant_id, match_data.current_turn-1, 1)
                    gesture_rh = match_data.get_gesture(
                        participant_id, match_data.current_turn-1, 2)
                if p.affected_by_fear(match_data.current_turn):
                    # If participant is affected by Fear, alter gestures in
                    # paralysed hand using spellbook rules
                    gesture_lh = self.effect_fear(gesture_lh)
                    gesture_rh = self.effect_fear(gesture_rh)
                if p.affected_by_maladroitness(match_data.current_turn):
                    # If participant is affected by Maladroitness, use RH gesture
                    # for both hands
                    gesture_lh = gesture_rh
                # For Charm Person we check if the caster is active this turn
                # This happens if caster is dead or not active during hasted or timestopped turn
                if (p.affected_by_charm_person(match_data.current_turn)
                        and p.states[match_data.current_turn]['charmed_by_id'] in match_data.get_ids_participants_active()):
                    # If participant is affected by Charm Person, use gesture
                    # selected by charmer for selected hand
                    handname = ''
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

    def make_precast_target_checks(self, spell, match_data,
                                   check_blindness=1, check_invisibility=1, check_mmirror=1):
        """Make pre-cast checks for the spell target.
        The first type of checks is checking target ID (hand, monster, participant) and getting target object.
        The second type of checks is target visibility and mirrors.
        
        Arguments:
            spell (object): Spell Instance, spell to be checked
            match_data (object): WarlocksMatchData instance, match data
            check_blindness (bool, optional): flag to check Blindness
            check_invisibility (bool, optional): flag to check Invisibililty
            check_mmirror (bool, optional): flag to check Magic Mirror
        """

        # For timestopped turns all existing effects are ignored.
        if match_data.is_current_turn_timestopped():
            check_blindness = 0
            check_invisibility = 0
            check_mmirror = 0

        caster = match_data.get_actor_by_id(spell.caster_id)
        target = None

        if spell.target_id in match_data.get_ids_participants():
            # target is a participant
            target = match_data.get_participant_by_id(spell.target_id)
            if spell.delayed == 0:
                match_data.add_log_entry(caster.id, 2, 'castGenericPoM',
                                         name=caster.name,
                                         spellname=spell.name,
                                         targetname=target.name)
            else:
                match_data.add_log_entry(caster.id, 2, 'castDelayedPoM',
                                         name=caster.name,
                                         spellname=spell.name,
                                         targetname=target.name)
        elif spell.target_id in match_data.get_ids_monsters():
            # target is a monster
            target = match_data.get_monster_by_id(spell.target_id)
            if spell.delayed == 0:
                match_data.add_log_entry(caster.id, 2, 'castGenericPoM',
                                         name=caster.name,
                                         spellname=spell.name,
                                         targetname=target.name)
            else:
                match_data.add_log_entry(caster.id, 2, 'castDelayedPoM',
                                         name=caster.name,
                                         spellname=spell.name,
                                         targetname=target.name)
        elif spell.target_id in match_data.get_ids_hands():
            # target is a hand
            if spell.target_id % 2 == 1:
                handname = match_data.get_text_strings_by_code('nameLeftHand')
            else:
                handname = match_data.get_text_strings_by_code('nameRightHand')
            handowner = match_data.get_participant_by_id(
                spell.target_id // match_data.hand_id_offset)
            if spell.delayed == 0:
                match_data.add_log_entry(caster.id, 2, 'castGenericHand',
                                         name=caster.name,
                                         spellname=spell.name,
                                         targetname=handowner.name,
                                         pronoun=handowner.pronoun_c,
                                         handname=handname)
            else:
                match_data.add_log_entry(caster.id, 2, 'castDelayedHand',
                                         name=caster.name,
                                         spellname=spell.name,
                                         targetname=handowner.name,
                                         pronoun=handowner.pronoun_c,
                                         handname=handname)
        else:
            # target is incorrect or nobody
            spell.target_id = 0
            if spell.delayed == 0:
                match_data.add_log_entry(caster.id, 2, 'castGenericNobody',
                                         name=caster.name,
                                         spellname=spell.name)
            else:
                match_data.add_log_entry(caster.id, 2, 'castDelayedNobody',
                                         name=caster.name,
                                         spellname=spell.name)

        # Blindness checked for participants, monsters and hands
        if (spell.target_id != 0 and (spell.caster_id != spell.target_id) 
            and check_blindness and caster.affected_by_blindness(match_data.current_turn)):
                match_data.add_log_entry(caster.id, 2, 'castMissesBlindness',
                                         spellname=spell.name,
                                         targetname=target.name)
        # Invisibility checked for participants and monsters
        elif (target is not None and (spell.caster_id != spell.target_id) 
            and check_invisibility and target.affected_by_invisibility(match_data.current_turn)):
                match_data.add_log_entry(caster.id, 2, 'castMissesInvisibility',
                                         spellname=spell.name,
                                         targetname=target.name)
        # Magic Mirror checked for participants and monsters
        elif (target is not None and (spell.caster_id != spell.target_id) 
            and check_mmirror and target.affected_by_mmirror(match_data.current_turn)):
            if target.affected_by_blindness(match_data.current_turn):
                match_data.add_log_entry(caster.id, 2, 'castReflectedBlindness',
                                         spellname=spell.name,
                                         targetname=target.name)
            elif caster.affected_by_invisibility(match_data.current_turn):
                match_data.add_log_entry(caster.id, 2, 'castReflectedInvisibility',
                                         spellname=spell.name,
                                         targetname=target.name)
            elif caster.affected_by_mmirror(match_data.current_turn):
                match_data.add_log_entry(caster.id, 2, 'castReflectedInfinite',
                                         name=caster.name,
                                         spellname=spell.name,
                                         targetname=target.name)
            else:
                spell.resolve = 1
                spell.caster_id = spell.target_id
                spell.target_id = caster.id
                match_data.add_log_entry(caster.id, 2, 'castReflected',
                                         name=caster.name,
                                         spellname=spell.name,
                                         targetname=target.name)
        else:
            spell.resolve = 1

    def select_spells_for_stack(self, match_orders, match_data):
        """Select spells to be cast this turn by this participant 
        from those they theoretically could cast based on their spellflow. 
        
        Arguments:
            match_orders (object): WarlocksOrders instance, match orders
            match_data (object): WarlocksMatchData instance, match data
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
                cast_spell_lh.target_id = self.select_spell_target(player_orders.order_target_lh,
                                                                   cast_spell_lh.default_target,
                                                                   player_orders.participant_id,
                                                                   match_data)
                cast_spell_lh.caster_id = player_orders.participant_id
                cast_spell_lh.cast_turn = match_data.current_turn
                caster = match_data.get_participant_by_id(
                    cast_spell_lh.caster_id)
                # Check if it should be made permanent
                if ((cast_spell_lh.id in self.get_ids_spells_permanentable())
                        and (caster.affected_by_permanency(match_data.current_turn))
                        and (player_orders.make_spell_permanent == caster.lh_id)):
                    cast_spell_lh.duration = 9999
                    caster.effects[match_data.current_turn]['Permanency'] = 0
                    match_data.add_log_entry(caster.id, 7, 'effectPermanency',
                                             name=caster.name)
                # Check if it should be made delayed
                if ((caster.affected_by_delay_effect(match_data.current_turn))
                        and (player_orders.delay_spell == caster.lh_id)):
                    caster.state_delayed_spell = cast_spell_lh
                    caster.state_delayed_spell.delayed = 1
                    caster.effects[match_data.current_turn]['DelayEffect'] = 0
                    match_data.add_log_entry(caster.id, 7, 'effectDelaySpell',
                                             name=caster.name)
                # Else add it to stack
                else:
                    self.add_spell_to_stack(cast_spell_lh)

            # Repeat the same process for spell(s) selected from other hands.
            if cast_spell_rh:
                cast_spell_rh.target_id = self.select_spell_target(player_orders.order_target_rh,
                                                                   cast_spell_rh.default_target,
                                                                   player_orders.participant_id,
                                                                   match_data)
                cast_spell_rh.caster_id = player_orders.participant_id
                cast_spell_rh.cast_turn = match_data.current_turn
                caster = match_data.get_participant_by_id(
                    cast_spell_rh.caster_id)
                if ((cast_spell_rh.id in self.get_ids_spells_permanentable())
                        and (caster.affected_by_permanency(match_data.current_turn))
                        and (player_orders.make_spell_permanent == caster.rh_id)):
                    cast_spell_rh.duration = 9999
                    caster.effects[match_data.current_turn]['Permanency'] = 0
                    match_data.add_log_entry(caster.id, 7, 'effectPermanency',
                                             name=caster.name)
                if ((caster.affected_by_delay_effect(match_data.current_turn))
                        and (player_orders.delay_spell == caster.rh_id)):
                    caster.state_delayed_spell = cast_spell_rh
                    caster.state_delayed_spell.delayed = 1
                    caster.effects[match_data.current_turn]['DelayEffect'] = 0
                    match_data.add_log_entry(caster.id, 7, 'effectDelaySpell',
                                             name=caster.name)
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
                                                                       match_data)
                elif cast_spell_bh.used_hand == 2:
                    cast_spell_bh.target_id = self.select_spell_target(player_orders.order_target_rh,
                                                                       cast_spell_bh.default_target,
                                                                       player_orders.participant_id,
                                                                       match_data)
                if ((cast_spell_bh.id in self.get_ids_spells_permanentable())
                        and (caster.affected_by_permanency(match_data.current_turn))
                        and (player_orders.make_spell_permanent == caster.rh_id
                             or player_orders.make_spell_permanent == caster.lh_id)):
                    cast_spell_bh.duration = 9999
                    caster.effects[match_data.current_turn]['Permanency'] = 0
                    match_data.add_log_entry(caster.id, 7, 'effectPermanency',
                                             name=caster.name)
                cast_spell_bh.caster_id = player_orders.participant_id
                cast_spell_bh.cast_turn = match_data.current_turn
                if ((caster.affected_by_delay_effect(match_data.current_turn))
                     and (player_orders.delay_spell == caster.lh_id
                          or player_orders.delay_spell == caster.rh_id)):
                    caster.state_delayed_spell = cast_spell_bh
                    caster.state_delayed_spell.delayed = 1
                    caster.effects[match_data.current_turn]['DelayEffect'] = 0
                    match_data.add_log_entry(caster.id, 7, 'effectDelaySpell',
                                             name=caster.name)
                else:
                    self.add_spell_to_stack(cast_spell_bh)

    def check_delayed_spell_cast(self, match_orders, match_data):
        """Put delayed spell in queue if participant had a delayed spell 
        and gave respective orders. 
        
        Arguments:
            match_orders (object): WarlocksOrders instance, match orders
            match_data (object): WarlocksMatchData instance, match data
        """

        for participant_id in match_data.get_ids_participants_active():

            player_orders = match_orders.search_orders(match_data.match_id,
                                                       match_data.current_turn, participant_id)

            if player_orders.cast_delayed_spell == 1:
                caster = match_data.get_participant_by_id(participant_id)
                if caster.state_delayed_spell is not None:
                    target = match_data.get_actor_by_id(
                        caster.state_delayed_spell.target_id)
                    if target is not None:
                        targetname = target.name
                    else:
                        targetname = 'nobody'
                        spell.target_id = 0
                    self.add_spell_to_stack(caster.state_delayed_spell)
                    caster.state_delayed_spell = None

    def check_mindspells_clash(self, match_data):
        """Mind spells (that alter gestures for the next turn) clash 
        and fizzle (i.e. negate each other) if cast at the same target. 
        When we attempt to cast a mind spell (for example with .castSpellFear())
        we increase .state_mindspells_this_turn counter for the mind spell target.
        After resolving those spells (f.e. calling .resolveSpellFear()) we check
        for clashes here and remove effects for all actors that have a clash.
        
        Arguments:
            match_data (object): WarlocksMatchData instance, match data
        """

        for p in match_data.participant_list:
            if p.is_alive and p.states[match_data.current_turn]['mindspells_this_turn'] > 1:
                p.remove_mindspell_effects(match_data.current_turn)
                match_data.add_log_entry(p.id, 6, 'effectMindSpellCancel',
                                         targetname=p.name, pronoun=p.pronoun_c)
        for m in match_data.monster_list:
            if m.is_alive and m.states[match_data.current_turn]['mindspells_this_turn'] > 1:
                m.remove_mindspell_effects(match_data.current_turn)
                match_data.add_log_entry(m.ID, 6, 'effectMindSpellCancel',
                                         targetname=m.name, pronoun=m.pronoun_c)

    def check_elemental_spells_clash(self, match_data):
        """Elemental spells (storms and elementals) clash 
        and fizzle (i.e. negate each other) if cast / present at the turn. 
        When we attempt to cast an elemental spell, we increase 
        .stateFireStormsThisTurn counter for the caster. Here we tally all these
        counters and check here for clashes before resolving those spells.
        
        Arguments:
            match_data (object): WarlocksMatchData instance, match data
        """

        if match_data.current_turn_elementals_clash:
            match_data.add_log_entry(
                spell.caster_id, 10, 'effectFireElementalIceElementalCancel')

        fire_elemental_ids = match_data.get_ids_monsters_by_type(5)
        fire_elemental_exists = len(fire_elemental_ids)
        ice_elemental_ids = match_data.get_ids_monsters_by_type(6)
        ice_elemental_exists = len(ice_elemental_ids)

        if match_data.current_turn_fire_storms and match_data.current_turn_ice_storms:
            # If both Firestorm(s) and Icestorm(s) were cast, fizzle storms
            for s in self.stack:
                if s.resolve == 1 and s.id in self.get_ids_spells_storms():
                    s.resolve = 0
            match_data.add_log_entry(0, 10, 'effectFireStormIceStormCancel')

        if fire_elemental_exists:
            if match_data.current_turn_fire_storms:
                # If Firestorm(s) were cast and Ice Elemental present, absorb elem
                for e in fire_elemental_ids:
                    match_data.set_destroy_monster_now_by_id(e)
                elemname = match_data.monster_names[5][0]
                match_data.add_log_entry(0, 10, 'effectElementalAbsorbedByStorm',
                                         name=elemname)
            elif match_data.current_turn_ice_storms:
                # If Icestorm(s) were cast and Fire Elemental present, fizzle storms and destroy elem
                for s in self.stack:
                    if s.resolve == 1 and s.id in self.get_ids_spells_ice_storm():
                        s.resolve = 0
                for e in fire_elemental_ids:
                    match_data.set_destroy_monster_now_by_id(e)
                match_data.add_log_entry(
                    0, 10, 'effectIceStormFireElementalCancel')

        if ice_elemental_exists:
            if match_data.current_turn_ice_storms:
                # If Icestorm(s) were cast and Ice Elemental present, absorb elem
                for e in ice_elemental_ids:
                    match_data.set_destroy_monster_now_by_id(e)
                elemname = match_data.monster_names[6][0]
                match_data.add_log_entry(0, 10, 'effectElementalAbsorbedByStorm',
                                         name=elemname)
            elif match_data.current_turn_fire_storms:
                # If Firestorm(s) were cast and Ice Elemental present, fizzle storms and destroy elem
                for s in self.stack:
                    if s.resolve == 1 and s.id in self.get_ids_spells_fire_storm():
                        s.resolve = 0
                for e in ice_elemental_ids:
                    match_data.set_destroy_monster_now_by_id(e)
                match_data.add_log_entry(
                    0, 10, 'effectFireStormIceElementalCancel')

        match_data.current_turn_fire_storms = 0
        match_data.current_turn_ice_storms = 0
        match_data.current_turn_elementals_clash = 0

    # SPELL CAST section

    """ All spells are cast in two stage - 'cast' (or 'fired' or 'started') and 'resolve'. 
    This is because some spells interact with each other before taking effect 
    (for example, Ice Storm and Fire Storm negate each other and produce a single message).
    This means we have to 'start' casting all spells, then take note of such collisions, then resolve all.

    However, this approach had to be modified due to the way targetting works (specifically we need 
    to track effects on monsters that are not yet summoned - and might not be resolved - 
    and were targeted by hand ID).

    To avoid having additional target list that would have to be mapped to existing targets later,
    we not resolve Dispel Magic, CounterSpell, Magic Mirror and all Summons (i.e. spell with IDs 1..9) 
    during cast phase, then do checks, then resolve everything else. It is not elegant, but it gets job done.

    Some similar spell might user common functions - f.e. Summon Goblin and Summon Ogre 
    both use resolve_spell_summon_monster().

    For all function below that match patterns cast_spell_[spellcode] or resolve_spell_[spellcode] 
    the same Args are used:
        spell (object): Spell instance, spell that is being cast
        match_data (object): WarlocksMatchData instance, match data
    """

    def cast_spell_dispel_magic(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 0)

        match_data.add_log_entry(spell.caster_id, 7, 'castDispelMagicResolved')

        # Remove all non-DispelMagic spells from queue
        for s in self.stack:
            if s.id not in self.get_ids_spells_dispel_magic():
                self.stack.remove(s)
                #s.resolve = 0

        # Remove all effects from all participants
        for p in match_data.participant_list:
            if p.is_alive:
                p.init_effects_and_states(match_data.current_turn)
                p.init_effects_and_states(match_data.current_turn + 1)

        # Shield target
        target = match_data.get_actor_by_id(spell.target_id)
        if target is not None:
            target.effects[match_data.current_turn]['PShield'] = 1
            match_data.add_log_entry(spell.caster_id, 7, 'castShieldResolved',
                                     targetname=target.name)

        # Destroy all monsters EOT
        for m in match_data.monster_list:
            if m.is_alive:
                m.set_destroy_eot()

    def resolve_spell_dispel_magic(self, spell, match_data):

        return

    def cast_spell_counter_spell(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 0)

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castCounterSpellNobody')
        else:
            match_data.add_log_entry(spell.caster_id, 7, 'castCounterSpellResolved',
                                     targetname=target.name)
            target.effects[match_data.current_turn]['PShield'] = 1
            target.effects[match_data.current_turn]['MShield'] = 1

    def resolve_spell_counter_spell(self, spell, match_data):

        return

    def cast_spell_magic_mirror(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 0)

        target = match_data.get_actor_by_id(spell.target_id)
        caster = match_data.get_actor_by_id(spell.caster_id)

        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castMagicMirrorNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castMagicMirrorCountered',
                                     name=caster.name)
        else:  # cast at target
            match_data.add_log_entry(spell.caster_id, 7, 'castMagicMirrorResolved',
                                     targetname=target.name)
            target.effects[match_data.current_turn]['MagicMirror'] = 1

    def resolve_spell_magic_mirror(self, spell, match_data):

        return

    def cast_spell_summon_goblin(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

        caster = match_data.get_participant_by_id(spell.caster_id)
        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'сastSummonMonsterNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castSummonMonsterCountered',
                                     name=caster.name, targetname=spell.name)
        else:
            monster_type = 1
            self.resolve_spell_summon_monster(spell, monster_type, match_data)

    def resolve_spell_summon_goblin(self, spell, match_data):

        return

    def cast_spell_summon_ogre(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

        caster = match_data.get_participant_by_id(spell.caster_id)
        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'сastSummonMonsterNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castSummonMonsterCountered',
                                     name=caster.name, targetname=spell.name)
        else:
            monster_type = 2
            self.resolve_spell_summon_monster(spell, monster_type, match_data)

    def resolve_spell_summon_ogre(self, spell, match_data):

        return

    def cast_spell_summon_troll(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

        caster = match_data.get_participant_by_id(spell.caster_id)
        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'сastSummonMonsterNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castSummonMonsterCountered',
                                     name=caster.name, targetname=spell.name)
        else:
            monster_type = 3
            self.resolve_spell_summon_monster(spell, monster_type, match_data)

    def resolve_spell_summon_troll(self, spell, match_data):

        return

    def cast_spell_summon_giant(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

        caster = match_data.get_participant_by_id(spell.caster_id)
        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'сastSummonMonsterNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castSummonMonsterCountered',
                                     name=caster.name, targetname=spell.name)
        else:
            monster_type = 4
            self.resolve_spell_summon_monster(spell, monster_type, match_data)

    def resolve_spell_summon_giant(self, spell, match_data):

        return

    def cast_spell_summon_fire_elemental(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 0, 0, 0)

        monster_type = 5
        self.resolve_spell_summon_monster(spell, monster_type, match_data)

    def resolve_spell_summon_fire_elemental(self, spell, match_data):

        return

    def cast_spell_summon_ice_elemental(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 0, 0, 0)

        monster_type = 6
        self.resolve_spell_summon_monster(spell, monster_type, match_data)

    def resolve_spell_summon_ice_elemental(self, spell, match_data):

        return

    def resolve_spell_summon_monster(self, spell, monster_type, match_data):
        """This is template monster summon function that is called by
        specific monster summon functions.
        
        Args:
            spell (object): Spell instance, spell that is being cast
            monster_type (int): monster type
            match_data (object): WarlocksMatchData instance, match data
        """

        # Get random pronouns and create a temporary monster.
        # Provide seed to select pronouns.
        pronouns = match_data.get_pronouns(-1,
                                           match_data.match_id + spell.cast_turn + spell.caster_id + spell.used_hand)
        new_monster = match_data.create_monster(spell.caster_id, monster_type,
                                                spell.caster_id,
                                                spell.caster_id * match_data.hand_id_offset + spell.used_hand,
                                                spell.cast_turn,
                                                pronouns[0], pronouns[1], pronouns[2])

        # For Goblins, Ogres, Trolls, Giants
        if monster_type in [1, 2, 3, 4]:
            target = match_data.get_actor_by_id(spell.target_id)
            # Determine monster controller - if monster is summoned
            # at another monster, they share controller
            if target.type == 1:  # player
                new_monster.controller_id = target.id
            elif target.type == 2:  # monster
                new_monster.controller_id = target.controller_id
            controller = match_data.get_participant_by_id(
                new_monster.controller_id)
            monster_id = match_data.get_next_monster_id()
            # Get new ID
            new_monster.set_actor_id(monster_id)
            # Get a random attack target (might be overridden with orders later)
            new_monster.attack_id = match_data.get_random_opponent_id(
                controller.id)
            # Get name
            name = match_data.get_new_monster_name(monster_type)
            new_monster.set_name(name)
            # Add monster to the list and log the event
            match_data.monster_list.append(new_monster)
            match_data.add_log_entry(spell.caster_id, 3, 'castSummonMonsterResolved',
                                     name=controller.name, targetname=new_monster.name)

        # For Fire and Ice elementals
        elif monster_type in [5, 6]:
            new_monster.controller_id = 0  # spell.caster_id
            # Check for other elems present on the field.
            fire_elemental_ids = match_data.get_ids_monsters_by_type(5)
            fire_elemental_exists = len(fire_elemental_ids)
            ice_elemental_ids = match_data.get_ids_monsters_by_type(6)
            ice_elemental_exists = len(ice_elemental_ids)
            # Remove previous elem of the same type right now
            if monster_type == 5 and fire_elemental_exists:  # there are previous fire elems
                for e in fire_elemental_ids:
                    elem = match_data.get_monster_by_id(e)
                    elem.destroy_now()
            if monster_type == 6 and ice_elemental_exists:  # there are previous ice elems
                for e in ice_elemental_ids:
                    elem = match_data.get_monster_by_id(e)
                    elem.destroy_now()

            # Request ID and name
            monster_id = match_data.get_next_monster_id()
            new_monster.set_actor_id(monster_id)
            name = match_data.get_new_monster_name(monster_type)
            new_monster.set_name(name)
            # Add monster to the list and log the event
            match_data.monster_list.append(new_monster)
            if monster_type == 5:
                match_data.add_log_entry(
                    spell.caster_id, 4, 'castFireElementalResolved2')
                if fire_elemental_exists:  # there are previous fire elems
                    match_data.add_log_entry(
                        spell.caster_id, 6, 'effectFireElementalsMerge')
            elif monster_type == 6:
                match_data.add_log_entry(
                    spell.caster_id, 4, 'castIceElementalResolved2')
                if ice_elemental_exists:  # there are previous ice elems
                    match_data.add_log_entry(
                        spell.caster_id, 6, 'effectIceElementalsMerge')

            # If both types of elems present, mark them for death before attacks
            # We do not kill them now because other elems might resolve later, and they need to merge
            fire_elemental_ids = match_data.get_ids_monsters_by_type(5)
            fire_elemental_exists = len(fire_elemental_ids)
            ice_elemental_ids = match_data.get_ids_monsters_by_type(6)
            ice_elemental_exists = len(ice_elemental_ids)

            if fire_elemental_exists and ice_elemental_exists:
                for e in fire_elemental_ids:
                    match_data.set_destroy_monster_before_attack_by_id(e)
                for e in ice_elemental_ids:
                    match_data.set_destroy_monster_before_attack_by_id(e)
                match_data.current_turn_elementals_clash = 1

    def cast_spell_haste(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_haste(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)

        if target is None:
            match_data.add_log_entry(spell.caster_id, 5, 'castHasteNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(
                spell.caster_id, 10, 'castHasteCountered', targetname=target.name)
        elif target.type == 2:
            target.effects[match_data.current_turn]['Haste'] = spell.duration
        else:
            if (target.effects[match_data.current_turn]['Haste'] < 9999 
                    and target.effects[match_data.current_turn + 1]['Haste'] < 9999):
                target.effects[match_data.current_turn + 1]['Haste'] = spell.duration
                match_data.add_log_entry(
                    spell.caster_id, 7, 'castHasteResolved', targetname=target.name)

    def cast_spell_time_stop(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_time_stop(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)

        if target is None:
            match_data.add_log_entry(spell.caster_id, 5, 'castTimeStopNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(
                spell.caster_id, 10, 'castTimeStopCountered', targetname=target.name)
        else:
            if target.type == 1:
                target.effects[match_data.current_turn + 1]['TimeStop'] = 1
            else:
                target.effects[match_data.current_turn]['TimeStop'] = 1
            match_data.add_log_entry(spell.caster_id, 7, 'castTimeStopResolved',
                                     targetname=target.name)

    def cast_spell_protection(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_protection(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)

        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castProtectionNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castProtectionCountered',
                                     targetname=target.name)
        else:
            if target.effects[match_data.current_turn]['Protection'] < 9999:
                target.effects[match_data.current_turn]['Protection'] = spell.duration
                match_data.add_log_entry(spell.caster_id, 7, 'castProtectionResolved',
                                         targetname=target.name)

    def cast_spell_resist_heat(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_resist_heat(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castResistHeatNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castResistHeatCountered',
                                     targetname=target.name)
        elif target.type == 2 and target.monster_type == 5:
            match_data.set_destroy_monster_before_attack_by_id(spell.target_id)
            match_data.add_log_entry(
                spell.caster_id, 6, 'castResistHeatDestroysFireElemental')
        else:
            target.effects[match_data.current_turn]['ResistHeat'] = spell.duration
            match_data.add_log_entry(spell.caster_id, 7, 'castResistHeatResolved',
                                     targetname=target.name)

    def cast_spell_resist_cold(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_resist_cold(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castResistColdNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castResistColdCountered',
                                     targetname=target.name)
        elif target.type == 2 and target.monster_type == 6:
            match_data.set_destroy_monster_before_attack_by_id(spell.target_id)
            match_data.add_log_entry(
                spell.caster_id, 6, 'castResistColdDestroysIceElemental')
        else:
            target.effects[match_data.current_turn]['ResistCold'] = spell.duration
            match_data.add_log_entry(spell.caster_id, 7, 'castResistColdResolved',
                                     targetname=target.name)

    def cast_spell_mind_spell(self, spell, match_data):
        """First cast phase for all mindspells: 
        Paralysis, Fear, Maladroitness, Amnesia, Charm Monster, Charm Person
        
        Args:
            spell (object): Spell instance, spell that is being cast
            match_data (object): WarlocksMatchData instance, match data
        """

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)
        target = match_data.get_actor_by_id(spell.target_id)
        if target is not None:
            target.states[match_data.current_turn]['mindspells_this_turn'] += 1

    def cast_spell_paralysis(self, spell, match_data):

        self.cast_spell_mind_spell(spell, match_data)

    def resolve_spell_paralysis(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(spell.caster_id, 5, 'castMindSpellNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castMindSpellCountered',
                                     targetname=target.name)
        elif target.affected_by_permanent_mindspell(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 6, 'castMindSpellOverridenByPermanent',
                                     targetname=target.name, spellname=spell.name)
        else:
            if target.type == 1:  # participant
                target.effects[match_data.current_turn + 1]['Paralysis'] = spell.duration
                target.states[match_data.current_turn + 1]['paralyzed_by_id'] = spell.caster_id
            else:
                target.effects[match_data.current_turn]['Paralysis'] = spell.duration
            match_data.add_log_entry(spell.caster_id, 8, 'castParalysisResolved',
                                     targetname=target.name)

    def cast_spell_amnesia(self, spell, match_data):

        self.cast_spell_mind_spell(spell, match_data)

    def resolve_spell_amnesia(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(spell.caster_id, 5, 'castMindSpellNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castMindSpellCountered',
                                     targetname=target.name)
        elif target.affected_by_permanent_mindspell(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 6, 'castMindSpellOverridenByPermanent',
                                     targetname=target.name, spellname=spell.name)
        else:
            if target.type == 1:  # participant
                target.effects[match_data.current_turn + 1]['Amnesia'] = spell.duration
            else:
                target.effects[match_data.current_turn]['Amnesia'] = spell.duration
            match_data.add_log_entry(spell.caster_id, 8, 'castAmnesiaResolved',
                                     targetname=target.name)

    def cast_spell_fear(self, spell, match_data):

        self.cast_spell_mind_spell(spell, match_data)

    def resolve_spell_fear(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(spell.caster_id, 5, 'castMindSpellNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castMindSpellCountered',
                                     targetname=target.name)
        elif target.affected_by_permanent_mindspell(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 6, 'castMindSpellOverridenByPermanent',
                                     targetname=target.name, spellname=spell.name)
        else:
            if target.type == 1:  # participant
                target.effects[match_data.current_turn + 1]['Fear'] = spell.duration
            else:
                target.effects[match_data.current_turn]['Fear'] = spell.duration
            match_data.add_log_entry(spell.caster_id, 8, 'castFearResolved',
                                     targetname=target.name)

    def cast_spell_maladroitness(self, spell, match_data):

        self.cast_spell_mind_spell(spell, match_data)

    def resolve_spell_maladroitness(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(spell.caster_id, 5, 'castMindSpellNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castMindSpellCountered',
                                     targetname=target.name)
        elif target.affected_by_permanent_mindspell(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 6, 'castMindSpellOverridenByPermanent',
                                     targetname=target.name, spellname=spell.name)
        else:
            if target.type == 1:  # participant
                target.effects[match_data.current_turn + 1]['Maladroitness'] = spell.duration
            else:
                target.effects[match_data.current_turn]['Maladroitness'] = spell.duration
            match_data.add_log_entry(spell.caster_id, 8, 'castMaladroitnessResolved',
                                     targetname=target.name)

    def cast_spell_charm_monster(self, spell, match_data):

        self.cast_spell_mind_spell(spell, match_data)

    def resolve_spell_charm_monster(self, spell, match_data):

        caster = match_data.get_actor_by_id(spell.caster_id)
        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(spell.caster_id, 5, 'castMindSpellNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castMindSpellCountered',
                                     targetname=target.name)
        elif target.affected_by_permanent_mindspell(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 6, 'castMindSpellOverridenByPermanent',
                                     targetname=target.name, spellname=spell.name)
        else:
            if target.type == 1:  # participant
                match_data.add_log_entry(spell.caster_id, 8, 'castCharmMonsterWrongTargetType',
                                         targetname=target.name, pronoun=target.pronoun_c, name=caster.name)
            # RB allows charming elems, but it has no real effect
            # (except for the weird like Ice Elemental looks, glassy-eyed, at caster).
            # Meanwhile, elems having no controllers is useful in other places.
            elif target.monster_type in [1, 2, 3, 4]:
                target.controller_id = caster.id
                match_data.add_log_entry(spell.caster_id, 8, 'castCharmMonsterResolved',
                                         targetname=target.name, name=caster.name)
            else:
                match_data.add_log_entry(spell.caster_id, 8, 'castCharmMonsterElemental',
                                         targetname=target.name, name=caster.name)

    def cast_spell_charm_person(self, spell, match_data):

        self.cast_spell_mind_spell(spell, match_data)

    def resolve_spell_charm_person(self, spell, match_data):

        caster = match_data.get_actor_by_id(spell.caster_id)
        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(spell.caster_id, 5, 'castMindSpellNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castMindSpellCountered',
                                     targetname=target.name)
        elif target.affected_by_permanent_mindspell(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 6, 'castMindSpellOverridenByPermanent',
                                     targetname=target.name, spellname=spell.name)
        else:
            if target.type == 2:  # monster
                match_data.add_log_entry(spell.caster_id, 8, 'castCharmPersonWrongTargetType',
                                         targetname=target.name, name=caster.name)
            else:
                target.effects[match_data.current_turn + 1]['CharmPerson'] = spell.duration
                target.states[match_data.current_turn + 1]['charmed_by_id'] = caster.id
                match_data.add_log_entry(spell.caster_id, 8, 'castCharmPersonResolved',
                                         targetname=target.name, name=caster.name)

    def resolve_spell_sickness(self, spell, match_data, sickness_type):
        """Resolving Disease and Poison
        
        Args:
            spell (object): Spell instance, spell that is being cast
            match_data (object): WarlocksMatchData instance, match data
            sickness_type (string): 'Disease' or 'Poison'
        """

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(spell.caster_id, 5, 'castSicknessNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castSicknessCountered',
                                     targetname=target.name)
        else:
            if target.type == 2:
                match_data.set_destroy_actor_eot_by_id(spell.target_id)
                target.effects[match_data.current_turn][sickness_type] = 1
                match_data.add_log_entry(spell.caster_id, 9, 'effectSickness1',
                                         name=target.name)
            else:
                target.effects[match_data.current_turn + 1][sickness_type] = spell.duration
                match_data.add_log_entry(spell.caster_id, 9, 'castSicknessResolved',
                                         targetname=target.name)

    def cast_spell_disease(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_disease(self, spell, match_data):

        sickness_type = 'Disease'
        self.resolve_spell_sickness(spell, match_data, sickness_type)

    def cast_spell_poison(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_poison(self, spell, match_data):

        sickness_type = 'Poison'
        self.resolve_spell_sickness(spell, match_data, sickness_type)

    def resolve_spell_cure_wounds(self, spell, match_data, heal_amount):
        """Summary
        
        Args:
            spell (object): Spell instance, spell that is being cast
            match_data (object): WarlocksMatchData instance, match data
            heal_amount (int): Amount of HP healed
        """
        target = match_data.get_actor_by_id(spell.target_id)

        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castCureWoundsNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castCureWoundsCountered',
                                     targetname=target.name)
        else:
            target.increase_hp(heal_amount)
            if heal_amount == 2:
                target.effects[match_data.current_turn]['Disease'] = 0
            match_data.add_log_entry(spell.caster_id, 7, 'castCureWoundsResolved',
                                     targetname=target.name)

    def cast_spell_cure_light_wounds(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_cure_light_wounds(self, spell, match_data):

        heal_amount = 1
        self.resolve_spell_cure_wounds(spell, match_data, heal_amount)

    def cast_spell_cure_heavy_wounds(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_cure_heavy_wounds(self, spell, match_data):

        heal_amount = 2
        self.resolve_spell_cure_wounds(spell, match_data, heal_amount)

    def cast_spell_antispell(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_antispell(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(spell.caster_id, 5, 'castAntiSpellNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castAntiSpellCountered',
                                     targetname=target.name)
        else:
            if target.type == 1:  # participant
                target.effects[match_data.current_turn]['AntiSpell'] = 1
                #target.setLastGestures(spell.target_id, '-', '-')
                match_data.add_log_entry(spell.caster_id, 8, 'castAntiSpellResolved',
                                         targetname=target.name)

    def cast_spell_blindness(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_blindness(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(spell.caster_id, 5, 'castBlindnessNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castBlindnessCountered',
                                     targetname=target.name)
        else:
            if (target.type == 1 
                    and target.effects[match_data.current_turn]['Blindness'] < 9999
                    and target.effects[match_data.current_turn + 1]['Blindness'] < 9999):
                target.effects[match_data.current_turn + 1]['Blindness'] = spell.duration
                match_data.add_log_entry(spell.caster_id, 8, 'castBlindnessResolved',
                                         targetname=target.name)
            elif target.type == 2:  # monster
                match_data.set_destroy_monster_before_attack_by_id(
                    spell.target_id)
                match_data.add_log_entry(spell.caster_id, 11, 'castBlindnessResolvedMonster',
                                         targetname=target.name)

    def cast_spell_invisibility(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_invisibility(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castInvisibilityNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castInvisibilityCountered',
                                     targetname=target.name)
        else:
            if (target.type == 1 and target.effects[match_data.current_turn]['Invisibility'] < 9999
                    and target.effects[match_data.current_turn + 1]['Invisibility'] < 9999):
                target.effects[match_data.current_turn + 1]['Invisibility'] = spell.duration
                match_data.add_log_entry(spell.caster_id, 8, 'castInvisibilityResolved',
                                         targetname=target.name)
            elif target.type == 2:  # monster
                match_data.set_destroy_monster_before_attack_by_id(
                    spell.target_id)
                match_data.add_log_entry(spell.caster_id, 11, 'castInvisibilityResolvedMonster',
                                         targetname=target.name)

    def cast_spell_permanency(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_permanency(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castPermanencyAndDelayNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castPermanencyAndDelayCountered',
                                     targetname=target.name)
        else:
            if (target.type == 1 and target.effects[match_data.current_turn]['Permanency'] < 9999
                    and target.effects[match_data.current_turn + 1]['Permanency'] < 9999):
                target.effects[match_data.current_turn + 1]['Permanency'] = spell.duration
                match_data.add_log_entry(spell.caster_id, 7, 'castPermanencyAndDelayResolved',
                                         targetname=target.name)

    def cast_spell_delay_effect(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_delay_effect(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castPermanencyAndDelayNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castPermanencyAndDelayCountered',
                                     targetname=target.name)
        else:
            if (target.type == 1 and target.effects[match_data.current_turn]['DelayEffect'] < 9999
                    and target.effects[match_data.current_turn + 1]['DelayEffect'] < 9999):
                target.effects[match_data.current_turn + 1]['DelayEffect'] = spell.duration
                match_data.add_log_entry(spell.caster_id, 7, 'castPermanencyAndDelayResolved',
                                         targetname=target.name)

    def cast_spell_remove_enchantment(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_remove_enchantment(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castRemoveEnchantmentNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castRemoveEnchantmentCountered',
                                     targetname=target.name)
        else:
            target.remove_enchantments(match_data.current_turn)
            if target.type == 1:  # participant
                match_data.add_log_entry(spell.caster_id, 8, 'castRemoveEnchantmentResolved',
                                         targetname=target.name)
            elif target.type == 2:  # monster
                match_data.set_destroy_actor_eot_by_id(spell.target_id)
                match_data.add_log_entry(spell.caster_id, 11, 'castRemoveEnchantmentResolvedMonster',
                                         targetname=target.name)

    def cast_spell_shield(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_shield(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(spell.caster_id, 5, 'castShieldNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(
                spell.caster_id, 10, 'castShieldCountered')
        else:
            target.effects[match_data.current_turn]['PShield'] = 1
            match_data.add_log_entry(spell.caster_id, 7, 'castShieldResolved',
                                     targetname=target.name)

    def cast_spell_magic_missile(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_magic_missile(self, spell, match_data):

        # ignore protection during timestopped turns, but still check shields
        check_pshield = 1
        check_protection = not match_data.is_current_turn_timestopped()

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castMagicMissileNobody')
        elif target.affected_by_pshield(match_data.current_turn, check_pshield, check_protection):
            match_data.add_log_entry(spell.caster_id, 9, 'castMagicMissileCountered',
                                     targetname=target.name)
        else:
            target.decrease_hp(1)
            match_data.add_log_entry(spell.caster_id, 9, 'castMagicMissileResolved',
                                     targetname=target.name)

    def resolve_spell_cause_wounds(self, spell, match_data, damage_amount):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castCauseWoundsNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castCauseWoundsCountered',
                                     targetname=target.name)
        else:
            target.decrease_hp(damage_amount)
            match_data.add_log_entry(spell.caster_id, 9, 'castCauseWoundsResolved',
                                     targetname=target.name)

    def cast_spell_cause_light_wounds(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_cause_light_wounds(self, spell, match_data):

        damage_amount = 2
        self.resolve_spell_cause_wounds(spell, match_data, damage_amount)

    def cast_spell_cause_heavy_wounds(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_cause_heavy_wounds(self, spell, match_data):

        damage_amount = 3
        self.resolve_spell_cause_wounds(spell, match_data, damage_amount)

    def cast_spell_fireball(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_fireball(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(spell.caster_id, 5, 'castFireballNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castFireballCountered',
                                     targetname=target.name)
        else:
            if target.type == 2 and target.monster_type == 6:
                match_data.set_destroy_monster_before_attack_by_id(
                    spell.target_id)
                match_data.add_log_entry(
                    spell.caster_id, 11, 'castFireballIceElemental')
            elif ((not match_data.is_current_turn_timestopped()) 
                   and target.affected_by_resist_heat_permanent(match_data.current_turn)):
                match_data.add_log_entry(spell.caster_id, 7, 'castFireballResistHeat',
                                         targetname=target.name, pronoun=target.pronoun_a.capitalize())
            else:
                target.decrease_hp(5)
                match_data.add_log_entry(spell.caster_id, 9, 'castFireballResolved',
                                         targetname=target.name, pronoun=target.pronoun_b)

    def cast_spell_lightning_bolt(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_lightning_bolt(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castLightningBoltNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castLightningBoltCountered',
                                     targetname=target.name)
        else:
            target.decrease_hp(5)
            match_data.add_log_entry(spell.caster_id, 9, 'castLightningBoltResolved',
                                     targetname=target.name)

    def cast_spell_clap_of_lightning(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_clap_of_lightning(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castLightningBoltNobody')
        elif target.affected_by_mshield(match_data.current_turn):
            match_data.add_log_entry(spell.caster_id, 10, 'castLightningBoltCountered',
                                     targetname=target.name)
        else:
            caster = match_data.get_actor_by_id(spell.caster_id)
            if caster.state_cast_clap_of_lightning == 0:
                target.decrease_hp(5)
                match_data.add_log_entry(spell.caster_id, 9, 'castLightningBoltResolved',
                                         targetname=target.name)
                caster.state_cast_clap_of_lightning += 1
            else:
                match_data.add_log_entry(spell.caster_id, 10, 'castClapOfLightningFizzle',
                                         name=caster.name)

    def cast_spell_finger_of_death(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 1, 1, 1)

    def resolve_spell_finger_of_death(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is None:
            match_data.add_log_entry(
                spell.caster_id, 5, 'castFingerOfDeathNobody')
        else:
            # if target.type == 2:
            #   match_data.setDestroyEOTByID(spell.target_id)
            # elif target.type == 1:
            match_data.set_destroy_actor_eot_by_id(spell.target_id)
            match_data.add_log_entry(spell.caster_id, 9, 'castFingerOfDeathResolved',
                                     targetname=target.name)

    def cast_spell_fire_storm(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 0, 0, 0)
        caster = match_data.get_participant_by_id(spell.caster_id)
        match_data.current_turn_fire_storms += 1

    def resolve_spell_fire_storm(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is not None:
            targetname = target.name
        else:
            targetname = match_data.get_text_strings_by_code('nameNobody')

        match_data.add_log_entry(spell.caster_id, 9, 'castFireStormResolved')
        for p in match_data.participant_list:
            if p.is_alive:
                if ((not match_data.is_current_turn_timestopped()) 
                     and p.affected_by_resist_heat_permanent(match_data.current_turn)):
                    match_data.add_log_entry(spell.caster_id, 9, 'effectResistHeat',
                                             name=p.name)
                elif p.affected_by_mshield(match_data.current_turn):
                    match_data.add_log_entry(spell.caster_id, 9, 'effectStormProtectedByMShield',
                                             name=p.name)
                else:
                    p.decrease_hp(5)
                    match_data.add_log_entry(spell.caster_id, 9, 'effectFireStormDamaged',
                                             targetname=p.name)
        for m in match_data.monster_list:
            if m.is_alive:
                if ((not match_data.is_current_turn_timestopped()) 
                     and m.affected_by_resist_heat_permanent(match_data.current_turn)):
                    match_data.add_log_entry(spell.caster_id, 9, 'effectResistHeat',
                                             name=m.name)
                elif m.affected_by_mshield(match_data.current_turn):
                    match_data.add_log_entry(spell.caster_id, 9, 'effectStormProtectedByMShield',
                                             name=m.name)
                else:
                    m.decrease_hp(5)
                    match_data.add_log_entry(spell.caster_id, 9, 'effectFireStormDamaged',
                                             targetname=m.name)

    def cast_spell_ice_storm(self, spell, match_data):

        self.make_precast_target_checks(spell, match_data, 0, 0, 0)
        caster = match_data.get_participant_by_id(spell.caster_id)
        match_data.current_turn_ice_storms += 1

    def resolve_spell_ice_storm(self, spell, match_data):

        target = match_data.get_actor_by_id(spell.target_id)
        if target is not None:
            targetname = target.name
        else:
            targetname = match_data.get_text_strings_by_code('nameNobody')

        match_data.add_log_entry(spell.caster_id, 9, 'castIceStormResolved')

        for p in match_data.participant_list:
            if p.is_alive:
                if ((not match_data.is_current_turn_timestopped()) 
                     and p.affected_by_resist_cold_permanent(match_data.current_turn)):
                    match_data.add_log_entry(spell.caster_id, 9, 'effectResistCold',
                                             name=p.name)
                elif p.affected_by_mshield(match_data.current_turn):
                    match_data.add_log_entry(spell.caster_id, 9, 'effectStormProtectedByMShield',
                                             name=p.name)
                else:
                    p.decrease_hp(5)
                    match_data.add_log_entry(spell.caster_id, 9, 'effectIceStormDamaged',
                                             targetname=p.name)
        for m in match_data.monster_list:
            if m.is_alive:
                if ((not match_data.is_current_turn_timestopped()) 
                     and m.affected_by_resist_cold_permanent(match_data.current_turn)):
                    match_data.add_log_entry(spell.caster_id, 9, 'effectResistCold',
                                             name=m.name)
                elif m.affected_by_mshield(match_data.current_turn):
                    match_data.add_log_entry(spell.caster_id, 9, 'effectStormProtectedByMShield',
                                             name=m.name)
                else:
                    m.decrease_hp(5)
                    match_data.add_log_entry(spell.caster_id, 9, 'effectIceStormDamaged',
                                             targetname=m.name)
