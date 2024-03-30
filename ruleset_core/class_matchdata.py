import random
from common.tools_engine import import_name


class MatchData:
    """Base class for various match data.

    Contains:
        match ID: match ID
        match_status: match status {0: created, -1: cancelled, 1: started=ongoing, 2: finished}
        current_turn: current turn number
        participant_list: lists of participants
        monster_list: list of monsters
        match_gestures: log of match gestures for all players
        match_log: log of match events for output
        text_strings: localized text strings for output
        spell_names, effect_names, monster_names, monster_classes: additional localized text for output
    """

    def __init__(self, match_id):
        """Init MatchData.

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
        """Return current match status.

        Returns:
            bool: {0: ongoing, 1: finished}
        """
        return self.match_status

    def get_match_status_ongoing(self):
        """Return 1 if the match is ongoing, 0 otherwise.

        Returns:
            bool: match ongoing flag
        """
        if self.match_status == 1:
            return 1
        else:
            return 0

    def get_match_status_finished(self):
        """Return 1 if the match is finished, 0 otherwise.

        Returns:
            bool: match finished flag
        """
        if self.match_status == 2:
            return 1
        else:
            return 0

    def get_effect_name(self, code):
        """Return effect name.

        Arguments:
            code (string): effect code for loc file

        Returns:
            string: effect text string
        """
        for s in self.effect_names:
            if s == code:
                return self.effect_names[s]
        return ''

    def get_pronoun_code(self, gender_id, form_id):
        """Return a pronoun code corresponding to ID.

        Third-person, singular number pronouns are chosen as per https://en.wikipedia.org/wiki/Pronoun
        and https://en.wikipedia.org/wiki/English_personal_pronouns
        Genders are Epicene, Feminine, Masculine
        Forms are Subject, Object, Dependent possessive, Independent possessive

        Arguments:
            gender_id (int): gender ID
            form_id (int): form ID

        Returns:
            string: pronoun code
        """
        code_id = gender_id * 10 + form_id

        pronoun_codes = {
            1: 'pronounThey',
            2: 'pronounThem',
            3: 'pronounTheir',
            4: 'pronounTheirs',
            11: 'pronounShe',
            12: 'pronounHer',
            13: 'pronounHer',
            14: 'pronounHers',
            21: 'pronounHe',
            22: 'pronounHim',
            23: 'pronounHis',
            24: 'pronounHis',
        }

        if code_id in pronoun_codes:
            return pronoun_codes[code_id]
        else:
            return ''

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
            # raise NameError('Missing Loc String ' + code + '!')
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

    def get_next_participant_id(self):
        """Return next free ID for a participant (normally in [1..8] range).

        Returns:
            int: next free ID
        """
        return len(self.participant_list) + 1

    def get_next_monster_id(self):
        """Return next free ID for a monster (normally in [101..] range).

        Returns:
            int: next free ID
        """
        return self.monster_id_offset + len(self.monster_list) + 1

    def get_actor_by_id(self, actor_id, search_alive_only=1):
        """Return an instance of SpellBook-specific inheritant of Actor class.

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

    def get_name_by_id(self, actor_id, search_hands=0):
        """Return a string with actor's name for correct actor IDs.

        Arguments:
            actor_id (int): actor ID, can be participant_id or monster_id.
            search_hands (bool): flag to include hands IDs to search.

        Returns:
            string: actor's name or 'nobody' in appropriate locale
        """
        name = ''
        search_alive_only = 0
        if actor_id in self.get_ids_participants(search_alive_only):
            target = self.get_participant_by_id(actor_id, search_alive_only)
            name = target.name
        elif search_hands == 1 and actor_id in self.get_ids_hands(search_alive_only):
            if actor_id % 2:
                name = (self.get_participant_by_id(actor_id // 10).name
                        + ' ' + self.get_text_strings_by_code('nameLH'))
            else:
                name = (self.get_participant_by_id(actor_id // 10).name
                        + ' ' + self.get_text_strings_by_code('nameRH'))
        elif actor_id in self.get_ids_monsters(search_alive_only):
            target = self.get_monster_by_id(actor_id, search_alive_only)
            if target.monster_type in [5, 6]:
                name_code = 0
                name_multiplier = 0
            elif target.monster_type in [1, 2, 3, 4]:
                count = 0
                for m in self.monster_list:
                    if m.id == target.id:
                        break
                    if m.monster_type == target.monster_type:
                        count += 1
                size = len(self.monster_name_codes[target.monster_type])
                name_code = count % size
                name_multiplier = count // size

            name = ((self.get_text_strings_by_code('nameMonsterExtra') + ' ') * name_multiplier
                    + self.monster_names[target.monster_type][name_code] + ' '
                    + self.monster_classes[target.monster_type])
        else:
            name = self.get_text_strings_by_code('nameNobody')

        return name

    def get_ids_targets(self, search_alive_only=1):
        """Return a list of all viable target IDs.

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
        plist = []
        for p in self.participant_list:
            if (not search_alive_only) or (search_alive_only and p.is_alive):
                plist.append(p.id)
        return plist

    def get_ids_opponents(self, participant_id, search_alive_only=1):
        """Return a list of all viable IDs of opponents.

        i.e. participants with different team number than submitted participant.

        Arguments:
            participant_id (int):  a participant that wants to know IDs of their opponents
            search_alive_only (bool, optional): flag to search only for alive actors or for all actors.

        Returns:
            list: a list of integer IDs.
        """
        p = self.get_participant_by_id(participant_id)
        team_id = p.team_id
        olist = []
        for p in self.participant_list:
            if p.team_id != team_id:
                if (not search_alive_only) or (search_alive_only and p.is_alive):
                    olist.append(p.id)
        return olist

    def get_random_actor_id(self):
        """Return an ID of a randomly-selected actor.

        Returns:
            integer: opponent's ID
        """
        return random.Random(self.match_id + self.current_turn + participant_id).choice(
            self.get_ids_participants(search_alive_only) + self.get_ids_monsters(search_alive_only))

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
        hlist = []
        for p in self.participant_list:
            if (not search_alive_only) or (search_alive_only and p.is_alive):
                hlist.append(p.lh_id)
                hlist.append(p.rh_id)
        return hlist

    def get_ids_monsters_by_type(self, type, search_alive_only=1):
        """Return a list of all viable IDs of monsters of specified type.

        This is mostly used to control the population of elementals (types 5 and 6).

        Arguments:
            type (int): requested monster type. For Warlocks it would be in range [1..6]
            search_alive_only (bool, optional): flag to search only for alive actors or for all actors.

        Returns:
            list: a list of integer IDs.
        """
        mlist = []
        for m in self.monster_list:
            if m.monster_type == type:
                if (not search_alive_only) or (search_alive_only and m.is_alive):
                    mlist.append(m.id)
        return mlist

    def get_ids_monsters(self, search_alive_only=1):
        """Return a list of all viable IDs of monsters.

        Arguments:
            search_alive_only (bool, optional): flag to search only for alive actors or for all actors.

        Returns:
            A list of integer IDs.
        """
        mlist = []
        for m in self.monster_list:
            if (not search_alive_only) or (search_alive_only and m.is_alive):
                mlist.append(m.id)
        return mlist

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
            if (m.summoner_hand_id == hand_id) and (m.turn_created == turn_num):
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

    def set_match_status_ongoing(self):
        """Update current match status to ongoing."""
        self.match_status = 1

    def set_match_status_finished(self):
        """Update current match status to finished."""
        self.match_status = 2

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
                m.turn_destroyed = self.current_turn
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
        """Save gestures made by participant_id on turn_num.

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
        """Set is_alive to 0 for monsters marked to be destroyed before attack phase."""
        for m in self.monster_list:
            if m.is_alive and (m.destroy_before_attack == 1):
                m.is_alive = 0
                m.turn_destroyed = self.current_turn
                self.add_log_entry(11, 'resultActorDies', actor_id=m.id)

    def kill_monsters_eot(self):
        """Set is_alive to 0 for monsters marked to be destroyed in the end of turn."""
        for m in self.monster_list:
            if m.is_alive and (m.hp <= 0 or m.destroy_eot == 1):
                m.is_alive = 0
                m.turn_destroyed = self.current_turn
                self.add_log_entry(11, 'resultActorDies', actor_id=m.id)

    def kill_participants_eot(self):
        """Set is_alive to 0 for participants marked to be destroyed in the end of turn."""
        for p in self.participant_list:
            if p.is_alive and (p.hp <= 0 or p.destroy_eot == 1):
                p.is_alive = 0
                p.turn_destroyed = self.current_turn
                self.add_log_entry(11, 'resultActorDies', actor_id=p.id)

    def check_match_end_eot(self):
        """End of Turn check for match end.

        Match end is triggered and match status is updated if all alive players belong to the same team.
        """
        # Make a list to flag teams still present in the match
        # max 8 teams, l[0] and l[9] not used
        tlist = [0] * self.hand_id_offset
        for p in self.participant_list:
            if p.is_alive:
                tlist[p.team_id] = 1

        # If more than one team left, do nothing.

        # If only one team left, get tead ID, then get participant names,
        # and log names of all participants (even dead) of the team.
        if sum(tlist) == 1:
            team_won = 0
            for i in range(len(tlist)):
                if tlist[i] == 1:
                    team_won = i
                    break
            if team_won:
                for p in self.participant_list:
                    if p.team_id == team_won:
                        self.add_log_entry(
                            12, 'resultActorVictorious', actor_id=p.id)
            self.set_match_status_finished()

        # If no teams left, declare a draw.
        elif sum(tlist) == 0:
            self.add_log_entry(12, 'resultDraw')
            self.set_match_status_finished()

    def give_single_attack_order(self, m, attack_id):
        """Process single attack order for a single monster.

        Arguments:
            m (object): an instance of SpellBook-specific Monster-inherited class
            attack_id (int): ID of attack target (from Orders)
        """
        target = None
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

    def get_log_entry_template(self):
        """Return a log entry dictionary template.

        Returns:
            dict: log entry dictionary template
        """
        log_entry = {'log_id': 0, 'match_id': 0,
                     'turn_num': 0, 'str_type': 0, 'str_code': '',
                     'actor_id': 0, 'pronoun_owner_id': 0,
                     'target_id': 0, 'spell_id': 0, 'attack_id': 0,
                     'damage_amount': 0, 'hand_type': 0, 'tmpstr': ''}
        return log_entry

    def add_log_entry(self, str_type, str_code, actor_id=0, pronoun_owner_id=0,
                      target_id=0, spell_id=0, attack_id=0, damage_amount=0, hand_type=0, tmpstr=''):
        """Log a game action.

        Arguments:
            str_type (int): type of action
            str_code (string): code to fetch unformatted string from localization files
            actor_id (int): ID of actor related to the action (i.e. caster of a spell)
            pronoun_owner_id (int, optional): pronoun owner ID
            target_id (int, optional): target ID
            spell_id (int, optional): spell ID
            attack_id (int, optional): ID of attack target
            damage_amount (int, optional): amount of damage dealt
            hand_type (int, optional): hand type {1: left, 2: right}
            tmpstr (str, optional): a string, for edge cases
        """
        log_entry = self.get_log_entry_template()
        log_entry['log_id'] = len(self.match_log)
        log_entry['match_id'] = self.match_id
        log_entry['turn_num'] = self.current_turn
        log_entry['str_type'] = str_type
        log_entry['str_code'] = str_code
        log_entry['actor_id'] = actor_id
        log_entry['pronoun_owner_id'] = pronoun_owner_id
        log_entry['target_id'] = target_id
        log_entry['spell_id'] = spell_id
        log_entry['attack_id'] = attack_id
        log_entry['damage_amount'] = damage_amount
        log_entry['hand_type'] = hand_type
        log_entry['tmpstr'] = tmpstr

        self.match_log.append(log_entry)

    # OUTPUT functions

    def init_text_vars(self, text_strings_loc, spell_names_loc,
                       effect_names_loc, monster_names_loc, monster_classes_loc):
        """Import localized text string patterns (for user's language).

        Patterns would later be formatted and used to display in-game messages.

        It shuffle imported localized monster names using match_id
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
            random.Random(self.match_id).shuffle(
                self.monster_name_codes[monster_type])

        for monster_type in monster_classes_loc:
            self.monster_classes[monster_type] = monster_classes_loc[monster_type]

    def match_init_output(self, spellbook_code, lang_code):
        """Process match_data and transform stuff.

        Transform match_log, gesture history and actors statuses,
        taking into account point-of-view visibility,
        user language locale and match spellbook,
        into text strings for output.

        Args:
            spellbook_code (str): selected spellbook code, f.e. "Warlocks"
            lang_code (str): code of the language to use for rendering (f.e. 'en')
        """
        # Init text strings
        core_name = 'ruleset_core.'
        lib_name = 'ruleset_' + spellbook_code.lower() + '.'

        """
        We load common text strings from respective lang file, f.e. loc_common_en.

        We load text strings from spellbook land file, f.e.:
        from loc_warlocks_en import warlocks_text_strings_en,
                                    warlocks_spell_names_en,
                                    warlocks_spell_effects_en,
                                    warlocks_monster_names_en,
                                    warlocks_monster_classes_en
        """

        common_text_strings = import_name(core_name + 'loc_common_' + lang_code.lower(),
                                          'common_text_strings_' + lang_code)
        spellbook_text_strings = import_name(lib_name + 'loc_' + spellbook_code.lower() + '_' + lang_code.lower(),
                                             spellbook_code.lower() + '_text_strings_' + lang_code)
        spellbook_spell_names = import_name(lib_name + 'loc_' + spellbook_code.lower() + '_' + lang_code.lower(),
                                            spellbook_code.lower() + '_spell_names_' + lang_code)
        spellbook_spell_effects = import_name(lib_name + 'loc_' + spellbook_code.lower() + '_' + lang_code.lower(),
                                              spellbook_code.lower() + '_spell_effects_' + lang_code)
        spellbook_monster_names = import_name(lib_name + 'loc_' + spellbook_code.lower() + '_' + lang_code.lower(),
                                              spellbook_code.lower() + '_monster_names_' + lang_code)
        spellbook_monster_classes = import_name(lib_name + 'loc_' + spellbook_code.lower() + '_' + lang_code.lower(),
                                                spellbook_code.lower() + '_monster_classes_' + lang_code)
        self.init_text_vars(spellbook_text_strings | common_text_strings, spellbook_spell_names,
                            spellbook_spell_effects, spellbook_monster_names, spellbook_monster_classes)

    def get_status_string_actor_by_id(self, actor_id, turn_num=0):
        """Return a string with actor status.

        Including name, HP, effects,
        controller and attack target (for monsters), etc.

        This is a placeholder that should be reworked for future front-end implementation.

        Arguments:
            actor_id (int): actor ID
            turn_num (int): turn number

        Returns:
            string: a string with actor's status
        """
        if turn_num == 0:
            turn_num = self.current_turn

        a = self.get_actor_by_id(actor_id, 0)

        slist = []
        s = self.get_text_strings_by_code('statusName').format(
            name=self.get_name_by_id(actor_id))
        if a.is_alive == 0:
            s += self.get_text_strings_by_code('statusDead')
        slist.append(s)
        s = self.get_text_strings_by_code('statusHP').format(damage=a.hp)
        slist.append(s)

        if a.type == 2 and a.controller_id:
            controller = self.get_participant_by_id(a.controller_id, 0)
            s = self.get_text_strings_by_code(
                'statusController').format(name=self.get_name_by_id(controller.id))
            slist.append(s)

            attack_target_name = self.get_name_by_id(a.attack_id)
            s = self.get_text_strings_by_code(
                'statusAttacking').format(attackname=attack_target_name)
            slist.append(s)

        # This is temporary safeguard for situations
        # when effects or states are not recorded for a specific turn
        # Which normally should not happen
        if turn_num in a.effects:
            for key in a.effects[turn_num]:
                if a.effects[turn_num][key] > 0:
                    s1 = self.get_effect_name(key)
                    # some effects, like AntiSpell, are not actually displayed in status bar
                    if s1:
                        if a.effects[turn_num][key] == self.permanent_duration:
                            s2 = self.get_text_strings_by_code('statusPermanent')
                        else:
                            s2 = str(a.effects[turn_num][key])
                        s = self.get_text_strings_by_code(
                            'statusEffectLength').format(spellname=s1, damage=s2)
                        slist.append(s)
            if a.type == 1 and a.get_delayed_spell(turn_num) is not None:
                s = self.get_text_strings_by_code('statusStored').format(
                    spellname=self.spell_names[a.get_delayed_spell(turn_num).id])
                slist.append(s)

        s = ', '.join(slist)
        return s

    def get_log_string_by_log_id(self, log_id, turn_num, pov_id):
        """Format and output a log entry.

        This is a placeholder that should be reworked for future front-end implementation.

        Arguments:
            log_id (int): log entry ID
            turn_num (int): turn number
            pov_id (int): ID of participant to output for

        Returns:
            string: formatted log string
        """
        log_entry = self.match_log[log_id]

        print_flag = 1
        # If POV is global or log is not about gestures or log belongs to POV, then print
        if (pov_id == -1
                or log_entry['str_type'] != 1
                or log_entry['actor_id'] == pov_id):
            print_flag = 1
        # If we use non-participant vision (limited to only things everyone sees)
        elif pov_id == 0:
            search_alive_only = 0
            log_actor = self.get_participant_by_id(
                log_entry['actor_id'], search_alive_only)
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
            search_alive_only = 0
            pov_actor = self.get_participant_by_id(pov_id, search_alive_only)
            log_actor = self.get_participant_by_id(
                log_entry['actor_id'], search_alive_only)
            if (pov_actor.affected_by_blindness(turn_num)
                    or log_actor.affected_by_invisibility(turn_num)
                    or log_actor.affected_by_timestop(turn_num)):
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
                if log_entry['pronoun_owner_id']:
                    actor_gender = self.get_actor_by_id(log_entry['pronoun_owner_id'], search_alive_only=0).gender
                    pronoun1form1_code = self.get_pronoun_code(actor_gender, 1)
                    pronoun1form1_text = self.get_text_strings_by_code(pronoun1form1_code)
                    pronoun1form2_code = self.get_pronoun_code(actor_gender, 2)
                    pronoun1form2_text = self.get_text_strings_by_code(pronoun1form2_code)
                    pronoun1form3_code = self.get_pronoun_code(actor_gender, 3)
                    pronoun1form3_text = self.get_text_strings_by_code(pronoun1form3_code)
                    pronoun1form4_code = self.get_pronoun_code(actor_gender, 4)
                    pronoun1form4_text = self.get_text_strings_by_code(pronoun1form4_code)
                else:
                    pronoun1form1_text = ''
                    pronoun1form2_text = ''
                    pronoun1form3_text = ''
                    pronoun1form4_text = ''

                strf = strt.format(name=actor_name,
                                   pronoun1form1=pronoun1form1_text,
                                   pronoun1form2=pronoun1form2_text,
                                   pronoun1form3=pronoun1form3_text,
                                   pronoun1form4=pronoun1form4_text,
                                   targetname=target_name,
                                   spellname=spell_name,
                                   attackname=attack_name,
                                   damage=log_entry['damage_amount'],
                                   handname=hand_name,
                                   tmpstr=log_entry['tmpstr'])
                return strf
        return ''

    def get_log_entries_by_turn(self, turn_num):
        """Filter match log for turn_num.

        Args:
            turn_num (int): turn number

        Returns:
            list: match log subset
        """
        elist = []
        for entry in self.match_log:
            if entry['turn_num'] == turn_num:
                elist.append(entry)

        return elist

    def print_match_log(self, pov_id):
        """Print match log.

        Args:
            pov_id (int): ID of participant to output for
        """
        if self.get_match_status_finished():
            last_turn = self.current_turn + 1
        else:
            last_turn = self.current_turn

        for turn_num in range(0, last_turn):
            print(self.get_text_strings_by_code(
                'turnNum').format(tmpstr=turn_num))
            turn_log = self.get_log_entries_by_turn(turn_num)
            for entry in turn_log:
                output_string = self.get_log_string_by_log_id(
                    entry['log_id'], turn_num, pov_id)
                if output_string:
                    print(output_string)
            print('')

    def print_actor_statuses(self, pov_id):
        """Print actor statuses.

        Args:
            pov_id (int): ID of participant to output for
        """
        tstr = ''
        for i in range(0, self.current_turn + 1):
            tstr += str(i % 10)
        spaced_gesture_history = 1
        for participant_id in self.get_ids_participants(0):
            print(self.get_status_string_actor_by_id(participant_id))
            print(self.get_text_strings_by_code('statusTurn') + tstr)
            print(self.get_text_strings_by_code('statusLH') + 'B' +
                  self.get_gesture_history(participant_id, 1, spaced_gesture_history, pov_id))
            print(self.get_text_strings_by_code('statusRH') + 'B' +
                  self.get_gesture_history(participant_id, 2, spaced_gesture_history, pov_id))
            print('')

        for monster_id in self.get_ids_monsters():
            print(self.get_status_string_actor_by_id(monster_id))
