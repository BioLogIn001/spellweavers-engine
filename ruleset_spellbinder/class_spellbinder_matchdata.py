from ruleset_core.class_matchdata import MatchData
from ruleset_spellbinder.class_spellbinder_actor import SpellbinderParticipant, SpellbinderMonster


class SpellbinderMatchData(MatchData):
    """Expands MatchData with Spellbinder-specific data.

    turns_info (dictionary): with additional info about each turn, described in get_turn_info_template()
    hand_id_offset (int): offset that is used to calculate hand IDs [11,12,21,22,31,32,..]
    monster_id_offset (int): offset that is used to calculate monster IDs [101,102,...]
    permanent_duration (int): a constant that is used to mark permanent spells
    """

    def __init__(self, match_id):
        """Init match data.

        Arguments:
            match_id (int): match ID
        """
        MatchData.__init__(self, match_id)

        self.turns_info = {}
        self.turns_info[0] = self.get_turn_info_template()
        self.turns_info[1] = self.get_turn_info_template()

        self.hand_id_offset = 10
        self.monster_id_offset = 100

        self.permanent_duration = 9999

        self.monster_types = {
            1: {'start_hp': 1, 'max_hp': 1, 'attack_damage': 1, 'damage_type': 'Physical', 'attack_all': 0, 'initial_effects': {}},
            2: {'start_hp': 2, 'max_hp': 2, 'attack_damage': 2, 'damage_type': 'Physical', 'attack_all': 0, 'initial_effects': {}},
            3: {'start_hp': 3, 'max_hp': 3, 'attack_damage': 3, 'damage_type': 'Physical', 'attack_all': 0, 'initial_effects': {}},
            4: {'start_hp': 4, 'max_hp': 4, 'attack_damage': 4, 'damage_type': 'Physical', 'attack_all': 0, 'initial_effects': {}},
            5: {'start_hp': 3, 'max_hp': 3, 'attack_damage': 3, 'damage_type': 'Fire', 'attack_all': 1, 'initial_effects': {'ResistHeat': self.permanent_duration}},
            6: {'start_hp': 3, 'max_hp': 3, 'attack_damage': 3, 'damage_type': 'Ice', 'attack_all': 1, 'initial_effects': {'ResistCold': self.permanent_duration}}
        }

    def get_turn_info_template(self):
        """Return a template for turn info.

        Returns:
            dict: a template for turn info
        """
        return {
            'turn_type': 1,  # 1 - normal, 2 - hasted, 3 - timestopped
            'fire_storms': 0,
            'ice_storms': 0,
            'elementals_clash': 0
        }

    # INIT and ADD functions

    def create_participant(self, player_id, player_gender, player_name, team_id):
        """Create an instance of Participant-inherited class.

        Arguments:
            player_id (int): a user ID to link game profile to in-match participant ID
            player_gender (int): player gender (for pronouns)
            player_name (string): player name to display
            team_id (int): participant's team ID for the match

        Returns:
            An instance of SpellbinderParticipant class.
        """
        start_turn = 1
        new_participant = SpellbinderParticipant(player_id, player_gender, player_name,
                                              team_id, start_turn, self.permanent_duration)
        return new_participant

    def create_monster(self, controller_id, monster_type,
                       summoner_id, summoner_hand_id, summon_turn,
                       gender):
        """Create an instance of Monster-inherited class.

        Arguments:
            controller_id (int): ID of the participant that controls the monster
            monster_type (int): monster type
            summoner_id (int): ID of the participant that summoned the monster
            summoner_hand_id (int): ID of the hand that was used to summon monster
            summon_turn (int): the number of turn when the monster was summoned
            gender (int): gender for pronouns {0: they/them/their, 1: she/her/hers, 2: he/him/his}

        Returns:
            An instance of SpellbinderMonster class.
        """
        new_monster = None
        if monster_type in self.monster_types:
            new_monster = SpellbinderMonster(self.monster_types, controller_id, monster_type,
                                          summoner_id, summoner_hand_id, summon_turn,
                                          gender, self.current_turn, self.permanent_duration)
        return new_monster

    # GET functions

    def get_gesture_log_entry(self, gesture_lh, gesture_rh):
        """Get codes for localized strings for LH and RH gestures to use in log.

        Arguments:
            gesture_lh (str): gesture for left hand
            gesture_rh (str): gesture for right hand

        Returns:
            tuple: codes of localization text strings associated with gestures
        """
        code_lh = ''
        code_rh = ''

        if gesture_lh == 'C' and gesture_rh == 'C':
            code_lh = 'gestureC'
            return (code_lh, code_rh)

        match gesture_lh:
            case '-':
                code_lh = 'gestureN'
            case 'C':
                code_lh = 'gestureC2'
            case 'D':
                code_lh = 'gestureD'
            case 'F':
                code_lh = 'gestureF'
            case 'P':
                code_lh = 'gestureP'
            case 'S':
                code_lh = 'gestureS'
            case 'W':
                code_lh = 'gestureW'
            case '>':
                code_lh = 'gestureT'

        match gesture_rh:
            case '-':
                code_rh = 'gestureN'
            case 'C':
                code_rh = 'gestureC2'
            case 'D':
                code_rh = 'gestureD'
            case 'F':
                code_rh = 'gestureF'
            case 'P':
                code_rh = 'gestureP'
            case 'S':
                code_rh = 'gestureS'
            case 'W':
                code_rh = 'gestureW'
            case '>':
                code_rh = 'gestureT'

        return (code_lh, code_rh)

    def get_turn_type(self, turn_num):
        """Get current turn type.

        Arguments:
            turn_num (int): turn number

        Returns:
            turn_type (int): type of the turn (1: normal, 2: hasted, 3: timestopped)
        """
        return self.turns_info[turn_num]['turn_type']

    def get_ids_participants_hasted(self):
        """Get list of participants that are affected by Haste this turn.

        Returns:
            list: interger IDs of participants
        """
        plist = []
        for participant_id in self.get_ids_participants():
            p = self.get_participant_by_id(participant_id)
            if p.affected_by_haste(self.current_turn):
                plist.append(participant_id)
        return plist

    def get_ids_participants_timestopped(self):
        """Get list of participants that are affected by Timestop this turn.

        Returns:
            list: interger IDs of participants
        """
        plist = []
        for participant_id in self.get_ids_participants():
            p = self.get_participant_by_id(participant_id)
            if p.affected_by_timestop(self.current_turn):
                plist.append(participant_id)
        return plist

    def get_participant_turn_active_status(self, participant_id):
        """Check if participant is active (can submit orders) this turn.

        Args:
            participant_id (int): participant ID

        Returns:
            bool: active flag
        """
        if self.get_match_status_finished():
            return 0

        p = self.get_participant_by_id(participant_id)
        if self.is_current_turn_timestopped():
            if p.is_alive and p.affected_by_timestop(self.current_turn):
                return 1
            else:
                return 0
        elif self.is_current_turn_hasted():
            if p.is_alive and p.affected_by_haste(self.current_turn):
                return 1
            else:
                return 0
        else:
            if p.is_alive:
                return 1
            else:
                return 0

    def get_ids_participants_active(self):
        """Get list of participants that are active this turn.

        Returns:
            list: interget IDs of participants
        """
        if self.is_current_turn_timestopped():
            return self.get_ids_participants_timestopped()
        if self.is_current_turn_hasted():
            return self.get_ids_participants_hasted()
        return self.get_ids_participants()

    def is_current_turn_hasted(self):
        """Check if the current turn is Hasted.

        Returns:
            bool: 1 if turn is Hasted, 0 otherwise
        """
        if self.get_turn_type(self.current_turn) == 2:
            return 1
        else:
            return 0

    def is_current_turn_timestopped(self):
        """Check if the current turn is Timestopped.

        Returns:
            bool: 1 if turn is Timestopped, 0 otherwise
        """
        if self.get_turn_type(self.current_turn) == 3:
            return 1
        else:
            return 0

    def check_gesture_visibility(self, turn_num, participant_id, pov_id):
        """Check visibility between two participants.

        Arguments:
            turn_num (int): turn number
            participant_id (int): ID of the participant who made the gesture
            pov_id (int): ID of participant to output for

        Returns:
            bool: 1 for visible gesture, 0 otherwise
        """
        # Determine visibility
        print_flag = 1
        # If we use global vision or if actor is pov
        if (pov_id == -1 or participant_id == pov_id):
            print_flag = 1
        # If we use common vision
        elif pov_id == 0:
            search_alive_only = 0
            log_actor = self.get_participant_by_id(
                participant_id, search_alive_only)
            if (log_actor.affected_by_invisibility(turn_num)
                    or log_actor.affected_by_timestop(turn_num)):
                print_flag = 0
            else:
                print_flag = 1
                for participant in self.participant_list:
                    if participant.affected_by_blindness(turn_num):
                        print_flag = 0
                        break
        # If we use POV of specific participant
        else:
            # Check visibility between actors
            search_alive_only = 0
            pov_actor = self.get_participant_by_id(
                pov_id, search_alive_only)
            log_actor = self.get_participant_by_id(
                participant_id, search_alive_only)
            if pov_actor.affected_by_timestop(turn_num):
                print_flag = 1
            elif (pov_actor.affected_by_blindness(turn_num)
                    or log_actor.affected_by_invisibility(turn_num)
                    or log_actor.affected_by_timestop(turn_num)):
                print_flag = 0
            else:
                print_flag = 1
        return print_flag

    def get_gesture_filtered(self, participant_id, turn_num, hand, respect_antispell=1, respect_spaces=0, pov_id=-1):
        """Return the gesture for this participand and this turn and hand.

        Arguments:
            participant_id (int): ID of the participant who made the gesture
            turn_num (int): the number of the turn
            hand (int): {1: left hand, 2: right hand}
            respect_antispell (bool, optional): flag to replace AntiSpelled gestures with '-'
            respect_spaces (bool, optional): flag for using spaces instead of missing gestures
            pov_id (int, optional): ID of participant to output for

        Returns:
            string: gesture str(1) that was shown by this participant with this hand if any, empty string otherwise
        """
        g = ''
        if turn_num in self.match_gestures[participant_id]:
            print_flag = self.check_gesture_visibility(turn_num, participant_id, pov_id)
            # Output gestures respecting visibility
            if print_flag:
                participant = self.get_participant_by_id(participant_id, 0)
                if respect_antispell and participant.states[turn_num]['antispelled']:
                    g = '-'
                else:
                    g = self.get_gesture(participant_id, turn_num, hand)
            else:
                g = '?'
        elif respect_spaces == 1:
            participant = self.get_participant_by_id(participant_id, 0)
            if respect_antispell and participant.states[turn_num]['antispelled']:
                g = '-'
            else:
                g = ' '

        return g

    def get_gesture_last(self, participant_id, hand, respect_antispell=1, respect_spaces=0, pov_id=-1):
        """Return the last gesture for this participand and hand.

        Note that on some turns a participant might not have made any gestures,
        so we have to go through all gestures and check turn_num each time.

        Arguments:
            participant_id (int): ID of the participant who made the gesture
            hand (int): {1: left hand, 2: right hand}
            respect_antispell (bool, optional): flag to replace AntiSpelled gestures with '-'
            respect_spaces (bool, optional): flag for using spaces instead of missing gestures
            pov_id (int, optional): ID of participant to output for

        Returns:
            string: gesture str(1) that was shown by this participant with this hand if any, empty string otherwise
        """
        turn_num = max(self.match_gestures[participant_id])
        g = self.get_gesture_filtered(participant_id, turn_num, hand, respect_antispell, respect_spaces, pov_id)
        return g

    def get_gesture_history(self, participant_id, hand, respect_spaces=0, pov_id=-1):
        """Return all gestures shown by this participand with this hand.

        Note that on some turns a participant might not have made any gestures,
        and depending on 'spaced' flag we either ignore these turns (if this string is used to match spells)
        or add ' ' (if this string is used for user output / turn log).

        Arguments:
            participant_id (int): ID of the participant who made the gesture
            hand (int): {1: left hand, 2: right hand}
            respect_spaces (bool, optional): flag for using spaces instead of missing gestures
            pov_id (int, optional): ID of participant to output for

        Returns:
            string: gesture history string that was shown by this participant with this hand if any, empty string otherwise
        """
        g = ''
        respect_antispell = 1
        if participant_id in self.match_gestures:
            for turn_num in range(1, self.current_turn + 1):
                g += self.get_gesture_filtered(participant_id, turn_num, hand, respect_antispell, respect_spaces, pov_id)
        return g

    def get_gesture_history_reversed_for_matching(self, participant_id, hand, max_spell_length, pov_id=-1):
        """Return all gestures shown by this participand with this hand.

        Note that on some turns a participant might not have made any gestures,
        and depending on 'spaced' flag we either ignore these turns (if this string is used to match spells)
        or add ' ' (if this string is used for user output / turn log).

        Arguments:
            participant_id (int): ID of the participant who made the gesture
            hand (int): {1: left hand, 2: right hand}
            max_spell_length (int): max spell length defined by the spellbook
            pov_id (int, optional): ID of participant to output for

        Returns:
            string: gesture history string that was shown by this participant with this hand if any, empty string otherwise
        """
        g = ''
        respect_antispell = 0
        respect_spaces = 0
        # pov_id = -1
        if participant_id in self.match_gestures:
            participant = self.get_participant_by_id(participant_id)
            for turn_num in range(self.current_turn, self.current_turn - max_spell_length - 1, -1):
                if turn_num not in participant.states or participant.states[turn_num]['is_alive'] == 0 or participant.states[turn_num]['antispelled'] == 1:
                    break
                g += self.get_gesture_filtered(participant_id, turn_num, hand, respect_antispell, respect_spaces, pov_id)
        return g

    # TURN LOGIC functions

    def set_next_turn_type(self):
        """Set the type of the next turn."""
        self.turns_info[self.current_turn + 1] = self.get_turn_info_template()

        next_turn_type = 1
        next_turn_haste_counter = 0
        next_turn_timestop_counter = 0
        # Count all participants that are hasted or timestopped during the next turn
        for p in self.participant_list:
            if p.is_alive:
                if p.effects[self.current_turn + 1]['TimeStop'] > 0:
                    next_turn_timestop_counter += 1
                if self.get_turn_type(self.current_turn) == 1 and (p.effects[self.current_turn]['Haste'] > 0
                                                                   or p.effects[self.current_turn + 1]['Haste'] > 0):
                    next_turn_haste_counter += 1
        # Timestop has priority over haste
        if next_turn_timestop_counter:
            next_turn_type = 3
        elif next_turn_haste_counter:
            next_turn_type = 2
        self.turns_info[self.current_turn + 1]['turn_type'] = next_turn_type

    def check_sickness_effects(self):
        """Check participants affected by Disease or Poison.

        Those who reached effect value 1, die EOT.
        """
        for p in self.participant_list:
            if p.is_alive:
                if p.effects[self.current_turn]['Disease'] == 1:
                    self.add_log_entry(9, 'effectDiseaseFatal', actor_id=p.id)
                    p.destroy_eot = 1
                if p.effects[self.current_turn]['Poison'] == 1:
                    self.add_log_entry(9, 'effectPoisonFatal', actor_id=p.id)
                    p.destroy_eot = 1

    def kill_suicided_participants(self, match_orders):
        """Kill suicided participants.

        Set is_alive to 0 for participants that are affected by perm mindspell and that gave the suicide order.

        Arguments:
            match_orders (object): SpellbinderOrders instance, orders for this turn
        """
        for participant_id in self.get_ids_participants():
            order = match_orders.search_orders(
                self.match_id, self.current_turn, participant_id)
            p = self.get_participant_by_id(participant_id)
            if (p.affected_by_permanent_mindspell(self.current_turn)
                    and (order.commit_suicide == 1)):
                p.is_alive = 0
                p.turn_destroyed = self.current_turn
                self.add_log_entry(11, 'resultActorSuicides',
                                   actor_id=p.id, pronoun_owner_id=p.id)

    def kill_surrendered_participants(self, turn_num):
        """Set is_alive to 0 for participants who showed P/P.

        Arguments:
            turn_num (int): turn number
        """
        respect_antispell = 0
        for p in self.participant_list:
            if (p.is_alive
                    and self.get_gesture_filtered(p.id, turn_num, 1, respect_antispell) == 'P'
                    and self.get_gesture_filtered(p.id, turn_num, 2, respect_antispell) == 'P'):
                p.is_alive = 0
                p.turn_destroyed = self.current_turn
                p.turn_surrendered = self.current_turn
                self.add_log_entry(11, 'resultActorSurrenders', actor_id=p.id)

    def revive_risen_participants(self, turn_num):
        """Set is_alive to 1 and do other revival procedures for participants that were affected with Raise Dead.

        Arguments:
            turn_num (int): turn number
        """        
        for p in self.participant_list:
            if p.states[turn_num]['risenfromdead']:
                p.is_alive = 1
                p.destroy_eot = 0
                p.hp = p.starting_hp
                p.init_effects_and_states(turn_num)
                p.init_effects_and_states(turn_num + 1)
                self.add_log_entry(10, 'castRaiseDeadActorRisen', actor_id=p.states[turn_num]['risenfromdead'], 
                                                                  target_id=p.id)


    def update_effects_on_monsters_eot(self):
        """EOT tick down all effects on monsters.

        Skipped for timestopped turns.
        """
        for m in self.monster_list:
            # Decrease length of all effects on non-timestopped turns
            if m.is_alive:
                for s in m.effects[self.current_turn]:
                    if not self.is_current_turn_timestopped():
                        m.decrease_effect(s, self.current_turn)
            # Pass remaining effects to the next turn
            for s in m.effects[self.current_turn]:
                if m.effects[self.current_turn][s] > m.effects[self.current_turn + 1][s]:
                    m.effects[self.current_turn +
                              1][s] = m.effects[self.current_turn][s]
            # Store hp and is_alive
            m.states[self.current_turn]['hp'] = m.hp
            m.states[self.current_turn]['is_alive'] = m.is_alive
            # Store controlled id and attack target id
            m.states[self.current_turn]['controller_id'] = m.controller_id
            m.states[self.current_turn]['attack_id'] = m.attack_id

    def update_effects_on_participants_eot(self):
        """EOT tick down all effects on participants.

        Skipped for turns that are followed by hasted or timestopped turns.
        """
        for p in self.participant_list:
            if p.is_alive:

                # If the next turn is normal, we log the end or start of Blindness & Invisibility
                # Otherwise (the next turn is hasted or timestopped) we do not log now
                if self.get_turn_type(self.current_turn + 1) == 1:
                    if p.effects[self.current_turn]['Blindness'] == 1:
                        self.add_log_entry(8, 'effectBlindness2', actor_id=p.id)
                    if p.effects[self.current_turn]['Invisibility'] == 1:
                        self.add_log_entry(8, 'effectInvisibility2', actor_id=p.id)

                    if p.effects[self.current_turn + 1]['Blindness'] in [3, self.permanent_duration]:
                        self.add_log_entry(8, 'effectBlindness1', actor_id=p.id)
                    if p.effects[self.current_turn + 1]['Invisibility'] in [3, self.permanent_duration]:
                        self.add_log_entry(8, 'effectInvisibility1', actor_id=p.id)

                for s in p.effects[self.current_turn]:

                    decrease_this_effect = 0
                    if s in ['PShield', 'MShield']:
                        # PShield and MShield always expire in 1 turn, unless next turn is hasted
                        if self.get_turn_type(self.current_turn + 1) in [1, 3]:
                            decrease_this_effect = 1
                    elif s in ['Fear', 'Confusion', 'Paralysis', 'Amnesia', 'CharmPerson']:
                        # MindSpell effects tick down if current turn is normal
                        if (self.get_turn_type(self.current_turn) == 1
                                and p.effects[self.current_turn][s] < self.permanent_duration):
                            decrease_this_effect = 1
                    else:
                        # All other effects tick down if the next turn is normal
                        if (self.get_turn_type(self.current_turn + 1) == 1
                                and p.effects[self.current_turn][s] < self.permanent_duration):
                            decrease_this_effect = 1

                    # If there are effects remaining this turn, pass them to the next turn
                    if (p.effects[self.current_turn][s]
                            - decrease_this_effect
                            > p.effects[self.current_turn + 1][s]):
                        p.effects[self.current_turn +
                                  1][s] = p.effects[self.current_turn][s] - decrease_this_effect

                # If participant is permanently paralyzed, pass info about current para to the next turn
                if p.affected_by_paralysis_permanent(self.current_turn):
                    p.states[self.current_turn +
                             1]['paralyzed_by_id'] = p.states[self.current_turn]['paralyzed_by_id']
                    p.states[self.current_turn +
                             1]['paralyzed_hand_id'] = p.states[self.current_turn]['paralyzed_hand_id']

                # If participant is permanently charmed, pass info about current charm to the next turn
                if p.affected_by_charm_person_permanent(self.current_turn):
                    p.states[self.current_turn +
                             1]['charmed_by_id'] = p.states[self.current_turn]['charmed_by_id']

                # If current turn is hasted or timestopped, pass info about paralyzer to next turn so that paralyze would work
                if self.get_turn_type(self.current_turn) in [2, 3] and p.states[self.current_turn]['paralyzed_by_id']:
                    caster = self.get_participant_by_id(
                        p.states[self.current_turn]['paralyzed_by_id'])
                    if caster.affected_by_haste(self.current_turn) == 0:
                        p.states[self.current_turn +
                                 1]['paralyzed_by_id'] = p.states[self.current_turn]['paralyzed_by_id']
                # If current turn is hasted or timestopped, pass info about charmer to next turn so that charm would work
                if self.get_turn_type(self.current_turn) in [2, 3] and p.states[self.current_turn]['charmed_by_id']:
                    caster = self.get_participant_by_id(
                        p.states[self.current_turn]['charmed_by_id'])
                    if caster.affected_by_haste(self.current_turn) == 0:
                        p.states[self.current_turn +
                                 1]['charmed_by_id'] = p.states[self.current_turn]['charmed_by_id']

                # If next turn is hasted or timestopped, preserve mindspell counter to allow clashes
                if self.get_turn_type(self.current_turn + 1) in [2, 3]:
                    p.states[self.current_turn +
                             1]['mindspells_this_turn'] = p.states[self.current_turn]['mindspells_this_turn']
                # Pass delayed spell, if any, and CoL counter to the next turn
                if p.get_delayed_spell(self.current_turn) is not None:
                    p.set_delayed_spell(
                        self.current_turn + 1, p.get_delayed_spell(self.current_turn))
                p.states[self.current_turn +
                         1]['clap_of_lightning'] = p.states[self.current_turn]['clap_of_lightning']

            # Update hp and is_alive for current turn - it could have changed during the turn
            p.states[self.current_turn]['hp'] = p.hp
            p.states[self.current_turn]['is_alive'] = p.is_alive
            # Save hp and is_alive as init values for next turn start (used by web version)
            p.states[self.current_turn + 1]['hp'] = p.hp
            p.states[self.current_turn + 1]['is_alive'] = p.is_alive

    def attack_action(self, a, d, check_mindspells=1, check_visibility=1, check_shields=1):
        """Resolve a single attack action.

        Arguments:
            a (object): SpellbinderParticipant or SpellbinderMonster instance, attacker
            d (object): SpellbinderParticipant or SpellbinderMonster instance or None, defender
            check_mindspells (bool, optional): flag to check mindspell effects that prevent attack
            check_visibility (bool, optional): flag to check visibility (Blindness, Invis)
            check_shields (bool, optional): flag to chech shields (PShield, Protection, Resists)
        """
        # If we check shields and other effects that prevent attacks,
        # we check for mindspells on attacker, but only for monsters
        if check_mindspells == 1 and a.type == 2 and a.affected_by_paralysis(self.current_turn):
            self.add_log_entry(8, 'effectParalysis2', actor_id=a.id)
            return
        # In Spellbinder, Amnesia does not prevent monsters from attacking, instead they attack prev target
        if check_mindspells == 1 and a.type == 2 and a.affected_by_amnesia(self.current_turn):
            if self.current_turn - 1 in a.states:
                a.states[self.current_turn]['attack_id'] = a.states[self.current_turn - 1]['attack_id']
                d = self.get_actor_by_id(a.states[self.current_turn - 1]['attack_id'])
            else:
                a.states[self.current_turn]['attack_id'] = 0
                d = None
            self.add_log_entry(8, 'effectAmnesia2', actor_id=a.id, pronoun_owner_id=a.id)
            # return
        # In Spellbinder, Fear does not prevent monsters from attacking, so we just log it and pass
        if check_mindspells == 1 and a.type == 2 and a.affected_by_fear(self.current_turn):
            self.add_log_entry(8, 'effectFear3', actor_id=a.id)
        # In Spellbinder, Confused monsters attack random targets
        # However, permanent Confusion should inherit targets from previous turn
        if (check_mindspells == 1 and
                a.type == 2 and
                a.affected_by_confusion_permanent(self.current_turn) and
                a.affected_by_confusion_permanent(self.current_turn - 1)):
            self.add_log_entry(8, 'effectConfusion4', actor_id=a.id)
            defender_id = self.states[self.current_turn - 1]['attack_id']
            d = self.get_actor_by_id(defender_id)
        elif check_mindspells == 1 and a.type == 2 and a.affected_by_confusion(self.current_turn):
            self.add_log_entry(8, 'effectConfusion3', actor_id=a.id)
            defender_id = self.get_random_actor_id(a.id)
            d = self.get_actor_by_id(defender_id)

        if d is None:
            self.add_log_entry(10, 'attackMissesNobody', actor_id=a.id)
            return

        # If we check visibility, we check visibility between attacker and defender
        if check_visibility == 1 and a.affected_by_blindness(self.current_turn):
            self.add_log_entry(10, 'attackMissesBlindness',
                               actor_id=a.id, attack_id=d.id)
            return
        if check_visibility == 1 and d.affected_by_invisibility(self.current_turn):
            self.add_log_entry(10, 'attackMissesInvisibility',
                               actor_id=a.id, attack_id=d.id)
            return

        # If we got here, we can actually attack.
        # a = Fire elem
        if a.damage_type == 'Fire':
            if check_shields == 1 and d.affected_by_resist_heat_permanent(self.current_turn):
                self.add_log_entry(7, 'effectResistHeat',
                                   actor_id=a.id, attack_id=d.id)
            elif check_shields == 1 and d.affected_by_pshield(self.current_turn):
                self.add_log_entry(
                    10, 'effectShieldFromElemental', actor_id=a.id, attack_id=d.id)
            else:
                d.decrease_hp(a.attack_damage)
                self.add_log_entry(9, 'damagedByFireElem', actor_id=a.id,
                                   attack_id=d.id, damage_amount=a.attack_damage)
        # a = Ice elem
        elif a.damage_type == 'Ice':
            if check_shields == 1 and d.affected_by_resist_cold_permanent(self.current_turn):
                self.add_log_entry(7, 'effectResistCold',
                                   actor_id=a.id, attack_id=d.id)
            elif check_shields == 1 and d.affected_by_pshield(self.current_turn):
                self.add_log_entry(
                    10, 'effectShieldFromElemental', actor_id=a.id, attack_id=d.id)
            else:
                d.decrease_hp(a.attack_damage)
                self.add_log_entry(9, 'damagedByIceElem', actor_id=a.id,
                                   attack_id=d.id, damage_amount=a.attack_damage)
        # a = monster or stabbing participant
        elif a.damage_type == 'Physical':
            # if a is a timestopped (check_shields = 0) monster, then it deals damage anyways
            # if a is a timestopped (check_shields = 0) participant,
            #   then we check d.affected_by_pshield(1, 0) - shield, but not protection
            # if a is a regular participant (check_shields = 1), then we check
            #   d.affected_by_pshield(1, 1) or simply d.affected_by_pshield()
            if ((check_shields == 0 and a.type == 2)
                    or (check_shields == 0 and a.type == 1 and d.affected_by_pshield(self.current_turn, 1, 0) == 0)
                    or (check_shields == 1 and d.affected_by_pshield(self.current_turn) == 0)):
                d.decrease_hp(a.attack_damage)
                self.add_log_entry(9, 'damagedByMonster', actor_id=a.id,
                                   attack_id=d.id, damage_amount=a.attack_damage)
            else:
                self.add_log_entry(10, 'effectShieldFromMonster',
                                   actor_id=a.id, attack_id=d.id)

    def check_stabs(self, match_orders):
        """Check for stab orders and resolve them.

        Arguments:
            match_orders (object): SpellbinderOrders instance, match orders
        """
        for p in self.participant_list:
            if p.is_alive:
                respect_antispell = 0
                gesture_lh = self.get_gesture_filtered(p.id, self.current_turn, 1, respect_antispell)
                gesture_rh = self.get_gesture_filtered(p.id, self.current_turn, 2, respect_antispell)
                player_orders = match_orders.search_orders(self.match_id,
                                                           self.current_turn, p.id)
                # Get current turn gestures for all participants
                attack_id = 0
                stab_hand = 0
                # If RH or LH tried to stab, use that as an order.
                # If both stabbed, Lh is ignored, consider that dagger is in RH.
                if gesture_rh == '>':
                    attack_id = player_orders.order_target_rh
                    stab_hand = 1
                elif gesture_lh == '>':
                    attack_id = player_orders.order_target_lh
                    stab_hand = 2
                else:
                    continue
                # Check if there was a target order. If not, get random opponent ID.
                if attack_id == -1:
                    attack_id = self.get_random_opponent_id(p.id)
                # Get target object
                if attack_id > 0:
                    target = self.get_actor_by_id(attack_id)
                    if target is None:
                        attack_id = 0
                # Adjust shield and visibility checks based on turn type.
                if stab_hand:
                    if self.is_current_turn_timestopped():
                        check_visibility = 0
                        check_shields = 0
                    else:
                        check_visibility = 1
                        check_shields = 1
                    # Commence stab
                    if attack_id > 0:
                        if attack_id == p.id:
                            self.add_log_entry(
                                10, 'stabSelf', actor_id=p.id, pronoun_owner_id=p.id)
                        else:
                            check_mindspells = 0
                            self.attack_action(
                                p, target, check_mindspells, check_visibility, check_shields)
                    else:
                        self.add_log_entry(
                            10, 'stabMissesNobody', actor_id=p.id)

    def attack_phase(self, phase_type):
        """Process attack phase of a normal turn (and skip phase for hasted and timestopped turns).

        Note the difference:
        On timestopped or hasted turns (turns with hasted or timestopped participants)
        there is no attack phase at all.
        But on normal turns there can be up to 3 attack phases, first for normal monsters,
        second for hasted monsters and third for timestopped monsters.

        Arguments:
            phase_type (int): {1: Normal monsters; 2: Hasted monsters; 3: Timestopped monsters}
        """
        # Skip attack phase entirely if turn is for timestopped or hasted participants
        # Note that a monster summoned during timestopped turn would not attack as well.
        if self.is_current_turn_hasted() or self.is_current_turn_timestopped():
            return

        # For all monsters alive and of effect appropriate to phase_type
        for m in self.monster_list:
            if m.is_alive and (phase_type == 1
                               or (phase_type == 2 and m.affected_by_haste(self.current_turn))
                               or (phase_type == 3 and m.affected_by_timestop(self.current_turn))):
                # If monsters attacks everyone
                if m.attack_all:

                    check_visibility = 0
                    if phase_type == 1:
                        if m.monster_type == 5:
                            self.add_log_entry(
                                9, 'attackFireElem', actor_id=m.id)
                        elif m.monster_type == 6:
                            self.add_log_entry(
                                9, 'attackIceElem', actor_id=m.id)
                        check_shields = 1
                    elif phase_type == 2:
                        if m.monster_type == 5:
                            self.add_log_entry(
                                9, 'attackFireElemHasted', actor_id=m.id)
                        elif m.monster_type == 6:
                            self.add_log_entry(
                                9, 'attackIceElemHasted', actor_id=m.id)
                        check_shields = 1
                    elif phase_type == 3:
                        if m.monster_type == 5:
                            self.add_log_entry(
                                9, 'attackFireElemTimestopped', actor_id=m.id)
                        elif m.monster_type == 6:
                            self.add_log_entry(
                                9, 'attackIceElemTimestopped', actor_id=m.id)
                        check_shields = 0
                    check_mindspells = 1
                    # Try to attack all participants
                    for p in self.participant_list:
                        if p.is_alive:
                            self.attack_action(
                                m, p, check_mindspells, check_visibility, check_shields)
                    # Try to attack all monsters (except self)
                    for mm in self.monster_list:
                        if mm.is_alive and m.id != mm.id:
                            self.attack_action(
                                m, mm, check_mindspells, check_visibility, check_shields)
                # If monster attacks one target
                else:
                    # Get target
                    if m.attack_id > 0:
                        target = self.get_actor_by_id(m.attack_id)
                        if target is None:
                            m.attack_id = 0
                    else:
                        target = None
                    # Determine if visibility and shields affect attacks in this phase
                    if phase_type == 1:
                        check_visibility = 1
                        check_shields = 1
                    elif phase_type == 2:
                        self.add_log_entry(
                            9, 'attackMonsterHasted', actor_id=m.id)
                        check_visibility = 1
                        check_shields = 1
                    elif phase_type == 3:
                        self.add_log_entry(
                            9, 'attackMonsterTimestopped', actor_id=m.id)
                        check_visibility = 0
                        check_shields = 0
                    check_mindspells = 1
                    self.attack_action(
                        m, target, check_mindspells, check_visibility, check_shields)

    def process_match_start(self):
        """Start the match.

        Initiate turn counter and log match start actions for all participants.
        """
        # Set match_status to 1 and current_turn to 0
        self.set_match_status_ongoing()
        self.set_current_turn(0)

        # log 'bows' for all participants
        for participant_id in self.get_ids_participants_active():
            self.add_log_entry(1, 'actorBows', actor_id=participant_id)

        # Finish turn 0 and update statuses for turn 1
        self.update_effects_on_participants_eot()

        # Set current_turn to 1
        self.set_current_turn(1)

    def process_match_turn(self, match_orders, match_spellbook):
        """Process match turn.

        Arguments:
            match_orders (object): SpellbinderOrders instance, match orders
            match_spellbook (object): SpellbinderSpellBook instance, match spellbook
        """
        # Turn startup
        self.process_turn_phase_startup()

        # Spellcasting
        self.process_turn_phase_cast(match_orders, match_spellbook)

        # Combat
        self.process_turn_phase_attack(match_orders)

        # Clean-up
        self.process_turn_phase_cleanup(match_orders)

    def process_turn_phase_startup(self):
        """Process turn phase 0 - initiation."""
        # Init EnS for the upcoming turn
        for p in self.participant_list:
            # Init storage for the next turn
            p.init_effects_and_states(self.current_turn + 1)

        for m in self.monster_list:
            # Init storage for the next turn
            m.init_effects_and_states(self.current_turn + 1)

    def process_turn_phase_cast(self, match_orders, match_spellbook):
        """Process turn phase 1 - spellcasting.

        Arguments:
            match_orders (object): SpellbinderOrders instance, match orders
            match_spellbook (object): SpellbinderSpellBook instance, match spellbook

        Returns:
            int: phase completion status; 1: success
        """
        # Step 1.0 - clear stack
        match_spellbook.clear_stack()

        # Step 1.1 - determine gestures for the turn
        match_spellbook.determine_gestures(match_orders, self)

        # Step 1.2 - log effects and gestures events for the turn
        match_spellbook.log_effects_bot(match_orders, self)
        match_spellbook.log_gesture_messages(self)

        # Step 1.3 - make a list of spells that match gestures for all participants
        match_spellbook.match_spell_pattern(self)

        # Step 1.4 - cast delayed spells, if any and if ordered, for all participants
        match_spellbook.check_delayed_spell_cast(match_orders, self)

        # Step 1.5 - select spells to cast (and their targets) for all participants
        match_spellbook.select_spells_for_stack(match_orders, self)

        # Step 1.6 - sort spell queue by priority
        match_spellbook.sort_spells_by_priority()

        # Step 1.7 - cast spells in queue
        match_spellbook.cast_spells(self)

        # Step 1.8 - pre-resolution checks (elem)
        match_spellbook.check_elemental_spells_clash(self)

        # Step 1.9 - resolve spells
        match_spellbook.resolve_spells(self)

        # Step 1.10 - post-resolution checks (mindspells)
        match_spellbook.check_mindspells_clash(self)

    def process_turn_phase_attack(self, match_orders):
        """Process turn phase 2 - combat.

        Arguments:
            match_orders (object): SpellbinderOrders instance, match orders

        Returns:
            int: phase completion status; 1: success
        """
        # Step 2.1 - remove monsters killed by fast spells
        self.kill_monsters_before_attack()

        # Step 2.2 - determine attack targets
        self.give_attack_orders(match_orders)

        # Step 2.3 - regular monster attacks
        self.attack_phase(1)

        # Step 2.4 - stabs
        self.check_stabs(match_orders)

        # Step 2.5 - hasted monster attacks
        self.attack_phase(2)

        # Step 2.6 - timestopped monster attacks
        self.attack_phase(3)

    def process_turn_phase_cleanup(self, match_orders):
        """Process turn phase 3 - clean-up.

        Arguments:
            match_orders (object): SpellbinderOrders instance, match orders

        Returns:
            int: phase completion status; 1: success, -1: match already finished
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

        # Step 3.6 - check raise dead
        self.revive_risen_participants(self.current_turn)

        # Step 3.7 - check for game over
        self.check_match_end_eot()

        # Step 3.8 - update effects on monsters
        self.update_effects_on_monsters_eot()

        # Step 3.9 - update effects on participants
        self.set_next_turn_type()
        self.update_effects_on_participants_eot()

        return
