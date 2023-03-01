import random


class MatchData:
    """Base class for various match data.
    
    Contains:
        match ID: match ID
        match_status:  match status {0: ongoing, 1: finished}
        current_turn: current turn number
        participant_list: lists of participants
        monster_list: list of monsters
        match_gestures: log of match gestures for all players
        match_log: log of match events for output
        text_strings: localized text strings for output
        spell_names, effect_names, monster_names, monster_classes: additional localized text for output
        output_strings: output text buffer
    """

    def __init__(self, match_id):
        """Init MatchData
        
        Arguments:
            match_id (int): match ID
        """

        self.match_id = match_id
        self.match_status = 0 
        self.current_turn = 0

        self.participant_list = []
        self.monster_list = []
        self.match_log = []

        self.monster_classes = {}
        
        self.monster_name_codes = {}
        self.monster_names = {}
        
        self.match_gestures = {}
        self.text_strings = {}
        self.spell_names = {}
        self.effect_names = {}
        self.output_strings = []

    def init_text_vars(self, text_strings_loc, spell_names_loc,
                       effect_names_loc, monster_names_loc, monster_classes_loc):
        """This function imports localized text string patterns (for user's language), 
        which would later be formatted and used to display in-game messages.
        
        It also shuffle imported localized monster names using match_id
        as a seed, so that for each match order of names is different,
        but it is always the same if loading the same match data.
        
        Arguments:
            text_strings_loc (dict): text strings patterns
            spell_names_loc (dict): spell names
            effect_names_loc (dict): effect names
            monster_names_loc (dict): list of names for each monster_type
            monster_classes_loc (list): monster class names
        """

        self.text_strings = text_strings_loc
        self.spell_names = spell_names_loc
        self.effect_names = effect_names_loc

        for monster_type in monster_names_loc:
            self.monster_names[monster_type] = monster_names_loc[monster_type]
            self.monster_name_codes[monster_type] = [*range(len(monster_names_loc[monster_type]))]
            random.Random(self.match_id).shuffle(self.monster_name_codes[monster_type])

        for monster_type in monster_classes_loc:
            self.monster_classes[monster_type] = monster_classes_loc[monster_type]

    def init_actors_tmp(self, participants):
        """Populate self.participant_list with match participants.
        
        Arguments:
            participants (list): participants initial data
        """

        for p in participants:
            # Create new Participant instance
            new_participant = self.create_participant(
                p['player_id'], p['gender'], p['player_name'], p['team_id'])
            # Set participant ID and hand IDs
            new_participant.set_actor_id(self.get_next_participant_id())
            new_participant.set_hands_ids(self.hand_id_offset)
            # Add participant to the match
            self.participant_list.append(new_participant)

    def add_gestures(self, participant_id, turn_num, gesture_lh, gesture_rh):
        """Add gestures to the match history, i.e. to self.match_gestures.
        These gestures were taken from player_orders, 
        validated in match_orders.validate_orders(), 
        and possibly changed by spell effects in match_spellbook.determine_gestures().
        
        Arguments:
            participant_id (int): ID of the participant who made gestures
            turn_num (int): number of turn on which the gestures were made
            gesture_lh (string): left hand gesture from SpellBook.valid_gestures set
            gesture_rh (string): right hand gesture from SpellBook.valid_gestures set
        """

        g = {
            'gLH': gesture_lh,
            'gRH': gesture_rh,
        }

        if participant_id not in self.match_gestures:
            self.match_gestures.update({participant_id: {}})
        self.match_gestures[participant_id].update({turn_num: g})

    # GET functions

    def get_match_status(self):
        """Return current match status
        
        Returns:
            bool: {0: ongoing, 1: finished}
        """

        return self.match_status

    def get_effect_name(self, code):
        """Summary
        
        Arguments:
            code (string): effect code for loc file
        
        Returns:
            string: effect text string
        """
        for s in self.effect_names:
            if s == code:
                return self.effect_names[s]
        return ''

    def get_pronoun_code(self, code_id):
        """Return a pronoun code corresponding to ID
        
        Arguments:
            code_id (int): ID
        
        Returns:
            string: pronoun code
        """

        pronoun_codes = {
            1: 'pronounThey',
            2: 'pronounThem',
            3: 'pronounTheir',
            11: 'pronounShe',
            12: 'pronounHer',
            13: 'pronounHers',
            21: 'pronounHe',
            22: 'pronounHim',
            23: 'pronounHis',
        }

        return pronoun_codes[code_id]

    def get_text_strings_by_code(self, code):
        """Return a string template for later formatting and output.
        
        Arguments:
            code (string): text code name of a localized unformatted string
        
        Returns:
            string: localized unformatted string if the code is found, empty string otherwise
        """

        if code in self.text_strings:
            return self.text_strings[code]
        else:
            # Debug
            #raise NameError('Missing Loc String ' + code + '!')
            return ''

    def get_gesture_last(self, participant_id, hand):
        """Return the last gesture for this participand and hand.
        Note that on some turns a participant might not have made any gestures,
        so we have to go through all gestures and check turn_num each time.
        
        Arguments:
            participant_id (int): ID of the participant who made the gesture
            hand (int): {1: left hand, 2: right hand}
        
        Returns:
            string: gesture str(1) that was shown by this participant with this hand if any, empty string otherwise
        """

        g = ''
        turn_prev = 0
        for turn_num in self.match_gestures[participant_id]:
            if turn_num > turn_prev:
                if hand == 1:
                    g = self.match_gestures[participant_id][turn_num]['gLH']
                elif hand == 2:
                    g = self.match_gestures[participant_id][turn_num]['gRH']
                turn_prev = turn_num

        return g

    def get_gesture(self, participant_id, turn_num, hand):
        """Return the gesture for this participand and this turn and hand.
        
        Arguments:
            participant_id (int): ID of the participant who made the gesture
            turn_num (int): the number of the turn
            hand (int): {1: left hand, 2: right hand}
        
        Returns:
            string: gesture str(1) that was shown by this participant with this hand if any, empty string otherwise
        """

        g = ''
        if ((participant_id in self.match_gestures)
                and (turn_num in self.match_gestures[participant_id])):
            if hand == 1:
                g = self.match_gestures[participant_id][turn_num]['gLH']
            elif hand == 2:
                g = self.match_gestures[participant_id][turn_num]['gRH']
        return g

    def get_gesture_history(self, participant_id, hand, spaced=0, pov_id=0):
        """Return all gestures shown by this participand with this hand during this match.
        Note that on some turns a participant might not have made any gestures,
        and depending on 'spaced' flag we either ignore these turns (if this string is used to match spells)
        or add ' ' (if this string is used for user output / turn log).
        
        Arguments:
            participant_id (int): ID of the participant who made the gesture
            hand (int): {1: left hand, 2: right hand}
            spaced (bool, optional): flag for using spaces instead of missing gestures
            pov_id (int): ID of participant to output for
        
        Returns:
            string: gesture history string that was shown by this participant with this hand if any, empty string otherwise
        """

        g = ''
        if participant_id in self.match_gestures:
            for turn_num in range(1, self.current_turn + 1):
                if turn_num in self.match_gestures[participant_id]:
                    # Determine visibiliyy
                    print_flag = 1
                    # If we use global vision or if actor is pov
                    if (pov_id == 0 or participant_id == pov_id):
                        print_flag = 1
                    else:
                        # Check visibility between actors
                        # 
                        search_alive_only = 0
                        pov_actor = self.get_participant_by_id(pov_id, search_alive_only)
                        log_actor = self.get_participant_by_id(participant_id, search_alive_only)
                        if (pov_actor.affected_by_blindness(turn_num) 
                                or log_actor.affected_by_invisibility(turn_num) 
                                or log_actor.affected_by_timestop(turn_num)):
                            print_flag = 0
                        else:
                            print_flag = 1
                    # Output gestures respecting visibility
                    if print_flag:
                        if hand == 1:
                            g += self.match_gestures[participant_id][turn_num]['gLH']
                        elif hand == 2:
                            g += self.match_gestures[participant_id][turn_num]['gRH']
                    else:
                        g += '?'
                elif spaced == 1:
                    g += ' '
        return g

    def get_next_participant_id(self):
        """Return next free ID for a participant (normally in [1..8] range)
        
        Returns:
            int: next free ID
        """

        return len(self.participant_list) + 1

    def get_next_monster_id(self):
        """Return next free ID for a monster (normally in [101..] range)
        
        Returns:
            int: next free ID
        """

        return self.monster_id_offset + len(self.monster_list) + 1

    def get_actor_by_id(self, actor_id, search_alive_only=1):
        """Return an instance of SpellBook-specific inheritant of an Actor class.
        
        Arguments:
            actor_id (int): actor ID, can be participant_id, hand_id or monster_id.
            search_alive_only (bool, optional): flag to search only for alive actors or for all actors.
        
        Returns:
            object: an instance of Spellbook-specific Participant or Monster class.
        """

        target = None
        if actor_id in self.get_ids_participants(search_alive_only):
            target = self.get_participant_by_id(actor_id, search_alive_only)
        elif actor_id in self.get_ids_monsters(search_alive_only):
            target = self.get_monster_by_id(actor_id, search_alive_only)
        elif actor_id in self.get_ids_hands(search_alive_only):
            target = self.get_monster_by_turn_and_hand(
                self.current_turn, actor_id, search_alive_only)
        return target

    def get_name_by_id(self, actor_id):
        """Return a string with actor's name for correct actor IDs, 
        
        Arguments:
            actor_id (int): actor ID, can be participant_id or monster_id.
        
        Returns:
            string: actor's name or 'nobody' in appropriate locale
        """

        name = ''
        search_alive_only = 0
        if actor_id in self.get_ids_participants(search_alive_only):
            target = self.get_participant_by_id(actor_id, search_alive_only)
            name = target.name
        elif actor_id in self.get_ids_monsters(search_alive_only):
            target = self.get_monster_by_id(actor_id, search_alive_only)
            name = ((self.get_text_strings_by_code('nameMonsterExtra') + ' ') * target.name_multiplier 
                    + self.monster_names[target.monster_type][target.name_code] + ' ' 
                    + self.monster_classes[target.monster_type])
        else:
            name = self.get_text_strings_by_code('nameNobody')

        return name

    def get_ids_targets(self, search_alive_only=1):
        """Return a list of all viable target IDs (participants, hands, monsters).
        
        Arguments:
            search_alive_only (bool, optional): flag to search only for alive actors or for all actors.
        
        Returns:
            list: a list of integer IDs.
        """

        return (self.get_ids_participants(search_alive_only)
                + self.get_ids_hands(search_alive_only)
                + self.get_ids_monsters(search_alive_only))

    def get_ids_participants(self, search_alive_only=1):
        """Return a list of all viable IDs of participants.
        
        Arguments:
            search_alive_only (bool, optional): flag to search only for alive actors or for all actors.
        
        Returns:
            list: a list of integer IDs.
        """

        l = []
        for p in self.participant_list:
            if (not search_alive_only) or (search_alive_only and p.is_alive):
                l.append(p.id)
        return l

    def get_ids_opponents(self, participant_id, search_alive_only=1):
        """Return a list of all viable IDs of opponents (i.e. participants with a different team number)
        of a specific participant.
        
        Arguments:
            participant_id (int):  a participant that wants to know IDs of their opponents
            search_alive_only (bool, optional): flag to search only for alive actors or for all actors.
        
        Returns:
            list: a list of integer IDs.
        """

        p = self.get_participant_by_id(participant_id)
        team_id = p.team_id
        l = []
        for p in self.participant_list:
            if p.team_id != team_id:
                if (not search_alive_only) or (search_alive_only and p.is_alive):
                    l.append(p.id)
        return l

    def get_random_opponent_id(self, participant_id):
        """Return an ID of a randomly-selected opponent.
        
        Arguments:
            participant_id (int): a participant that wants to know ID of their random opponent
        
        Returns:
            integer: opponent's ID
        """

        return random.Random(self.match_id + self.current_turn + participant_id).choice(
            self.get_ids_opponents(participant_id))

    def get_ids_hands(self, search_alive_only=1):
        """Return a list of all viable IDs of participants' hands.
        
        Arguments:
            search_alive_only (bool, optional): flag to search only for alive actors or for all actors.
        
        Returns:
            list: a list of integer IDs.
        """

        l = []
        for p in self.participant_list:
            if (not search_alive_only) or (search_alive_only and p.is_alive):
                l.append(p.lh_id)
                l.append(p.rh_id)
        return l

    def get_ids_monsters_by_type(self, type, search_alive_only=1):
        """Return a list of all viable IDs of monsters of specified type.
        This is mostly used to control the population of elementals (types 5 and 6).
        
        Arguments:
            type (int): requested monster type. For Warlocks it would be in range [1..6]
            search_alive_only (bool, optional): flag to search only for alive actors or for all actors.
        
        Returns:
            list: a list of integer IDs.
        """

        l = []
        for m in self.monster_list:
            if m.monster_type == type:
                if (not search_alive_only) or (search_alive_only and m.is_alive):
                    l.append(m.id)
        return l

    def get_ids_monsters(self, search_alive_only=1):
        """Return a list of all viable IDs of monsters.
        
        Arguments:
            search_alive_only (bool, optional): flag to search only for alive actors or for all actors.
        
        Returns:
            A list of integer IDs.
        """

        l = []
        for m in self.monster_list:
            if (not search_alive_only) or (search_alive_only and m.is_alive):
                l.append(m.id)
        return l

    def get_participant_by_id(self, participant_id, search_alive_only=1):
        """Return an instance of SpellBook-specific inheritant of Participant class.
        
        Arguments:
            participant_id (int): ID of participant
            search_alive_only (bool, optional): flag to search only for alive actors or for all actors.
        
        Returns:
            object: An instance of a SpellBook-specific inheritant of Participant class.
        """

        for p in self.participant_list:
            if p.id == participant_id:
                if (not search_alive_only) or (search_alive_only and p.is_alive):
                    return p
                else:
                    break

    def get_monster_by_id(self, monster_id, search_alive_only=1):
        """Return an instance of SpellBook-specific inheritant of Monster object.
        
        Arguments:
            monster_id (int): ID of monster
            search_alive_only (bool, optional): flag to search only for alive actors or for all actors.
        
        Returns:
            object: An instance of a SpellBook-specific inheritant of Participant class.
        """

        for m in self.monster_list:
            if m.id == monster_id:
                if (not search_alive_only) or (search_alive_only and m.is_alive):
                    return m
                else:
                    break

    def get_monster_by_turn_and_hand(self, turn_num, hand_id, search_alive_only=1):
        """Return an instance of SpellBook-specific inheritant of Monster class.
        This is used if the monster is summoned this turn, and it was originally targeted by hand ID.
        
        Arguments:
            turn_num (int): the number of the turn
            hand_id (int): id of the hand used to summon
            search_alive_only (bool, optional): flag to search only for alive actors or for all actors.
        
        Returns:
            object: An instance of a SpellBook-specific inheritant of Participant class.
        """

        for m in self.monster_list:
            if (m.summoner_hand_id == hand_id) and (m.summon_turn == turn_num):
                if (not search_alive_only) or (search_alive_only and m.is_alive):
                    return m
                else:
                    break

    # SET functions

    def set_match_status(self, status):
        """Update current match status.
        
        Arguments:
            status (bool): {0: ongoing, 1: finished}
        """

        self.match_status = status

    def set_current_turn(self, turn_num):
        """Update current turn number.
        
        Arguments:
            turn_num (int): turn number
        """

        self.current_turn = turn_num

    def set_destroy_monster_now_by_id(self, monster_id):
        """Mark monster as dead.
        
        Arguments:
            monster_id (int): monster ID
        """

        for m in self.monster_list:
            if m.is_alive and (m.id == monster_id):
                m.is_alive = 0
                break

    def set_destroy_monster_before_attack_by_id(self, monster_id):
        """Flag monster to die this turn before attacks.
        We do not kill them right away as they still might be a target of another spell or interact somehow.
        
        Arguments:
            monster_id (int): monster ID
        """

        if monster_id in self.get_ids_monsters():
            m = self.get_monster_by_id(monster_id)
            m.set_destroy_before_attack()
        elif monster_id in self.get_ids_hands():
            m = self.get_monster_by_turn_and_hand(
                self.current_turn, monster_id)
            m.set_destroy_before_attack()

    def set_destroy_actor_eot_by_id(self, actor_id):
        """Flag actor to die in the end of the turn.
        They still get to attack or do something else.
        
        Arguments:
            actor_id (int): actor ID
        """

        for participant_id in self.get_ids_participants():
            if participant_id == actor_id:
                p = self.get_participant_by_id(participant_id)
                p.set_destroy_eot()
                break

        for monster_id in self.get_ids_monsters():
            if monster_id == actor_id:
                m = self.get_monster_by_id(monster_id)
                m.set_destroy_eot()
                break

        for hand_id in self.get_ids_hands():
            if hand_id == actor_id:
                m = self.get_monster_by_turn_and_hand(
                    self.current_turn, hand_id)
                m.set_destroy_eot()
                break

    def set_gestures(self, participant_id, turn_num, gesture_lh, gesture_rh):
        """Save gestures made by participant_id on turn_num
        
        Arguments:
            participant_id (int): participant ID
            turn_num (int): turn number
            gesture_lh (string): left hand gesture
            gesture_rh (string): right hand gesture
        """

        g = {
            'gLH': gesture_lh,
            'gRH': gesture_rh,
        }

        self.match_gestures[participant_id].update({turn_num: g})

    def kill_monsters_before_attack(self):
        """Set is_alive to 0 for monsters marked to be destroyed before attack phase.
        """

        for m in self.monster_list:
            if m.is_alive and (m.destroy_before_attack == 1):
                m.is_alive = 0
                self.add_log_entry(11, 'resultActorDies', actor_id=m.id)

    def kill_monsters_eot(self):
        """Set is_alive to 0 for monsters marked to be destroyed in the end of turn.
        """

        for m in self.monster_list:
            if m.is_alive and (m.hp <= 0 or m.destroy_eot == 1):
                m.is_alive = 0
                self.add_log_entry(11, 'resultActorDies', actor_id=m.id)

    def kill_participants_eot(self):
        """Set is_alive to 0 for participants marked to be destroyed in the end of turn.
        """

        for p in self.participant_list:
            if p.is_alive and (p.hp <= 0 or p.destroy_eot == 1):
                p.is_alive = 0
                self.add_log_entry(11, 'resultActorDies', actor_id=p.id)

    def check_match_end_eot(self):
        """End of Turn check for match end. Match end is triggered 
        and match status is updated if all alive players belong to the same team.
        """

        # Make a list to flag teams still present in the match
        # max 8 teams, l[0] and l[9] not used
        l = [0] * self.hand_id_offset
        for p in self.participant_list:
            if p.is_alive:
                l[p.team_id] = 1

        # If more than one team left, do nothing.

        # If only one team left, get tead ID, then get participant names,
        # and log names of all participants (even dead) of the team.
        if sum(l) == 1:
            team_won = 0
            for i in range(len(l)):
                if l[i] == 1:
                    team_won = i
                    break
            names = []
            if team_won:
                for p in self.participant_list:
                    if p.team_id == team_won:
                        names.append(p.name)
            if len(names) == 1:
                namestr = names[0]
                self.add_log_entry(12, 'resultActorVictorious', tmpstr=namestr)
            else:
                namestr = ', '.join(names[0:-1:1]) + ' & ' + names[-1]
                self.add_log_entry(12, 'resultTeamVictorious', tmpstr=namestr)
            self.set_match_status(1)

        # If no teams left, declare a draw.
        elif sum(l) == 0:
            self.add_log_entry(12, 'resultDraw')
            self.set_match_status(1)

    def give_single_attack_order(self, m, attack_id):
        """Process single attack order for a single monster.
        
        Arguments:
            m (object): an instance of SpellBook-specific Monster-inherited class
            attack_id (int): ID of attack target (from Orders)
        """

        target = None
        search_alive_only = 1
        attack_id_prev = m.attack_id
        order_counted = 0
        # If there are no orders this turn
        if attack_id == -1:
            # if there are no orders from previous turn as well
            # choose random opponent as a target.
            if attack_id_prev == -1:
                attack_id = self.get_random_opponent_id(m.controller_id)
                target = self.get_participant_by_id(attack_id)
            # else take orders from previous turn.
            else:
                attack_id = attack_id_prev
                target = self.get_participant_by_id(attack_id)
        # else (if there are orders this turn)
        else:
            # Try to find requested target among valid targets
            if attack_id == 0:
                order_counted = 1
            else:
                target = self.get_actor_by_id(attack_id)
                if target is not None:
                    # Update attack_id (useful if target was hand)
                    attack_id = target.id
                    order_counted = 1
                else:
                    # If target not found, redirect to nobody
                    attack_id = 0
        # save updated target
        m.attack_id = attack_id

        # log report if a valid order was given
        if order_counted:
            if target is None:
                target_id = 0
            else:
                target_id = target.id
            controller = self.get_participant_by_id(m.controller_id)
            self.add_log_entry(6, 'attackOrder',
                               actor_id=controller.id,
                               target_id=m.id,
                               attack_id=target_id)

    def give_attack_orders(self, match_orders):
        """Process portion of turn Orders related to attacks.
        
        Arguments:
            match_orders (object): an instance of Spellbook-specific Orders-inherited class, match orders
        """

        search_alive_only = 1
        # checking all attack orders for participants acting this turn
        for participant_id in self.get_ids_participants_active():
            player_orders = match_orders.search_orders(self.match_id,
                                                       self.current_turn, participant_id)
            if player_orders.attack_orders:
                for order_id in player_orders.attack_orders:
                    # trying to locate the object this order belongs to among monsters
                    if order_id in self.get_ids_monsters(search_alive_only):
                        m = self.get_monster_by_id(order_id)
                    # trying to locate the object this order belongs to among new summons
                    elif order_id in self.get_ids_hands(search_alive_only):
                        m = self.get_monster_by_turn_and_hand(
                            self.current_turn, order_id)
                    # if object found, check check if order source is correct
                    # ignore orders that do not come from anyone other than monster controller
                    if m and (m.controller_id == participant_id):
                        attack_id = player_orders.attack_orders[order_id]
                        self.give_single_attack_order(m, attack_id)

    def add_log_entry(self, str_type, str_code, actor_id=0, pronoun_code='', target_id=0, 
                      spell_id=0, attack_id=0, damage_amount=0, hand_type=0, tmpstr=''):
        """Log a game action.
        
        Arguments:
            str_type (int): type of action
            str_code (string): code to fetch unformatted string from localization files
            actor_id (int): ID of actor related to the action (i.e. caster of a spell)
            pronoun_code (str, optional): pronoun code
            target_id (int, optional): target ID
            spell_id (int, optional): spell ID
            attack_id (int, optional): ID of attack target
            damage_amount (int, optional): amount of damage dealt
            hand_type (int, optional): hand type {1: left, 2: right}
            tmpstr (str, optional): a string, for edge cases
        """

        new_log_id = len(self.match_log)
        log_entry = {'log_id': new_log_id, 'match_id': self.match_id,
                     'turn_num': self.current_turn, 'str_type': str_type, 'str_code': str_code,
                     'actor_id': actor_id, 'pronoun_code': pronoun_code, 'target_id': target_id, 
                     'spell_id': spell_id, 'attack_id': attack_id, 
                     'damage_amount': damage_amount, 'hand_type': hand_type, 'tmpstr': tmpstr
                     }
        self.match_log.append(log_entry)

    # OUTPUT functions

    def get_status_string_actor_by_id(self, actor_id):
        """Return a string with actor status, including name, HP, effects, 
        controller and attack target (for monsters), etc.
        
        This is a placeholder that should be reworked for future front-end implementation.
        
        Arguments:
            actor_id (int): actor ID
        
        Returns:
            string: a string with actor's status
        """

        a = self.get_actor_by_id(actor_id, 0)

        slist = []
        s = self.get_text_strings_by_code('statusName').format(name=self.get_name_by_id(actor_id))
        if a.is_alive == 0:
            s += self.get_text_strings_by_code('statusDead')
        slist.append(s)
        s = self.get_text_strings_by_code('statusHP').format(damage=a.hp)
        slist.append(s)

        if a.type == 2 and a.controller_id:
            controller = self.get_participant_by_id(a.controller_id, 0)
            s = self.get_text_strings_by_code(
                'statusController').format(name=controller.name)
            slist.append(s)

            attack_target = self.get_actor_by_id(a.attack_id)
            if attack_target:
                attack_target_name = attack_target.name
            else:
                attack_target_name = self.get_text_strings_by_code(
                    'nameNobody')
            s = self.get_text_strings_by_code(
                'statusAttacking').format(attackname=attack_target_name)
            slist.append(s)

        for key in a.effects[self.current_turn]:
            if a.effects[self.current_turn][key] > 0:
                s1 = self.get_effect_name(key)
                if a.effects[self.current_turn][key] == self.permanent_duration:
                    s2 = self.get_text_strings_by_code('statusPermanent')
                else:
                    s2 = str(a.effects[self.current_turn][key])
                s = self.get_text_strings_by_code(
                    'statusEffectLength').format(spellname=s1, damage=s2)
                slist.append(s)
        if a.type == 1 and a.get_delayed_spell(self.current_turn) is not None:
            s = self.get_text_strings_by_code('statusStored').format(
                spellname=self.spell_names[a.get_delayed_spell(self.current_turn).id])
            slist.append(s)

        s = ', '.join(slist)
        return s

    def get_gestures_string_actor_by_id(self, actor_id, pov_id):
        """Return a string with actor gestures using current POV.
        
        This is a placeholder that should be reworked for future front-end implementation.
        
        Arguments:
            actor_id (int): actor ID
            pov_id (int): ID of participant to output for

        Returns:
            list: strings with gestures of actor_id
        """
        
        s=''
        spaced_gesture_history = 1
        tstr = ''
        for i in range(0, self.current_turn + 1):
            tstr += str(i % 10)
        s += self.get_text_strings_by_code('statusTurn') + tstr + '\n'
        s += (self.get_text_strings_by_code('statusLH') + 'B' +
              self.get_gesture_history(actor_id, 1, spaced_gesture_history, pov_id)) + '\n'
        s += (self.get_text_strings_by_code('statusRH') + 'B' +
              self.get_gesture_history(actor_id, 2, spaced_gesture_history, pov_id))
        return s

    def get_log_string_by_log_id(self, log_id, pov_id):
        """Format and output a log entry.
        
        This is a placeholder that should be reworked for future front-end implementation.
        
        Arguments:
            log_id (int): log entry ID
            pov_id (int): ID of participant to output for
        
        Returns:
            string: formatted log string
        """

        log_entry = self.match_log[log_id]

        print_flag = 1
        # If POV is global or log is not about gestures or log belongs to POV, then print
        # We also ignore log_entry['actor_id'] == 0 - this happens on zero turn during bows
        if (pov_id == 0 
                or log_entry['actor_id'] == 0
                or log_entry['str_type'] != 1 
                or log_entry['actor_id'] == pov_id):
            print_flag = 1
        else:
            pov_actor = self.get_participant_by_id(pov_id)
            log_actor = self.get_participant_by_id(log_entry['actor_id'])
            if (pov_actor.affected_by_blindness(self.current_turn) 
                    or log_actor.affected_by_invisibility(self.current_turn) 
                    or log_actor.affected_by_timestop(self.current_turn)):
                print_flag = 0
            else:
                print_flag = 1

        if print_flag:
            strt = self.get_text_strings_by_code(log_entry['str_code'])
            if strt:

                actor_name = self.get_name_by_id(log_entry['actor_id'])
                target_name = self.get_name_by_id(log_entry['target_id'])
                attack_name = self.get_name_by_id(log_entry['attack_id'])
                if log_entry['spell_id']:
                    spell_name = self.spell_names[log_entry['spell_id']]
                else:
                    spell_name = ''
                hand_name = ''
                if log_entry['hand_type'] == 1:
                    hand_name = self.get_text_strings_by_code('nameLeftHand')
                elif log_entry['hand_type'] == 2:
                    hand_name = self.get_text_strings_by_code('nameRightHand')
                if log_entry['pronoun_code']:
                    pronoun_text = self.get_text_strings_by_code(log_entry['pronoun_code'])
                else:
                    pronoun_text = ''

                strf = strt.format(name=actor_name,
                                   pronoun=pronoun_text,
                                   targetname=target_name,
                                   spellname=spell_name,
                                   attackname=attack_name,
                                   damage=log_entry['damage_amount'],
                                   handname=hand_name,
                                   tmpstr=log_entry['tmpstr'])
                """
                RB uses the following style options:
                01 gestures #CCCCCC
                02 spellcast #88FF88
                03 successfull summons #FF88FF
                04 successfull elem summons #FFAA00
                05 spells at nobody, monsters summoned at nobody, attacks at not summoned monsters #FFCC00
                06 attack orders, attacks at nobody, invis and blind disappears and reappears, special elemental shite #FFFFFF
                07 shield effects (mmirror,dispel,shield), heals #88FFFF
                08 mindspell effects, antispell, blindness, invis, remove enchantment #FFFF88
                09 damage, poison, disease #FF8888
                10 spells countered, monsters attack nobody, deflected attacks, ClapOfLightning fizzles #88AAFF
                11 monster death (for all reasons), surrender, player death #FF6666
                12 victory, draw #FFFFFF bold
                """
                return strf
        return ''

    def clear_log(self):
        """Clear log entries
        """
        self.match_log = []

    def output_match_actors_status(self, pov_id):
        """Output effects for all actors and gesture history for all participants).
        
        This is a placeholder that should be reworked for future front-end implementation.

        Arguments:
            pov_id (int): ID of participant to output for
        """

        for participant_id in self.get_ids_participants(0):
            self.output_strings.append(self.get_status_string_actor_by_id(participant_id))
            self.output_strings.append(self.get_gestures_string_actor_by_id(participant_id, pov_id))
        for monster_id in self.get_ids_monsters():
            self.output_strings.append(self.get_status_string_actor_by_id(monster_id))

    def output_log_entries_by_turn(self, turn_num, pov_id):
        """Select log entried related to a specific turn and print them.
        
        This is a placeholder that should be reworked for future front-end implementation.
        
        Arguments:
            turn_num (int): turn number
            pov_id (int): ID of participant to output for
        """

        for l in self.match_log:
            if l['turn_num'] == turn_num:
                    s = self.get_log_string_by_log_id(l['log_id'], pov_id)
                    if s:
                        self.output_strings.append(s)

    def print_output_strings(self):
        """Print output buffer
        """
        for s in self.output_strings:
            print(s)
        self.output_strings = []