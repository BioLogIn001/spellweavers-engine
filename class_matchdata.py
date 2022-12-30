import random
from functions_debug import *


class MatchData:
    '''Base class for various match data.
    Contains: 
    - match ID, match status & current turn number,
    - lists of actors (participants and monsters),
    - log of match gestures for all players
    - log of match actions for output
    - localized text strings for output
    - additional information - monster names and classes

    '''

    def __init__(self, match_id):
        self.match_id = match_id
        self.match_status = 0  # {0: ongoing, 1: finished}
        self.current_turn = 0

        self.participant_list = []
        self.monster_list = []
        self.match_gestures = {}
        self.match_log = []
        self.text_strings = {}
        self.spell_names = {}
        self.effect_names = {}
        self.monster_names = {}
        self.monster_classes = {}

    def init_text_vars(self, text_strings_loc, spell_names_loc,
                       effect_names_loc, monster_names_loc, monster_classes_loc):
        '''This function imports localized text string patterns (for user's language), 
        which would later be formatted and used to display in-game messages.

        It also imports localized monster names and then shuffle them using match_id
        as a seed, so that for each match order or names is different,
        but it is always the same if loading the same match data.

        Arguments:
        text_strings_loc -- dictionary with text strings
        spell_names_loc -- dictionary with spell names
        effect_names_loc -- dictionary with effect names
        monster_names_loc -- dictionary with list of names for each monster_type
        monster_classes_loc -- list of monster class names
        '''

        self.text_strings = text_strings_loc
        self.spell_names = spell_names_loc
        self.effect_names = effect_names_loc

        for monster_type in monster_names_loc:
            self.monster_names[monster_type] = monster_names_loc[monster_type]
            random.Random(self.match_id).shuffle(
                self.monster_names[monster_type])

        for monster_type in monster_classes_loc:
            self.monster_classes[monster_type] = monster_classes_loc[monster_type]

    def init_actors_tmp(self, participants):
        ''' Populate self.participant_list with match participants.

        Arguments:
        participants -- list of participants initial data
        '''

        for p in participants:
            # Create new Participant instance
            new_participant = self.create_participant(
                p['player_id'], p['player_name'], p['team_id'])
            # Set participant ID and hand IDs
            new_participant.set_actor_id(self.get_next_participant_id())
            new_participant.set_hands_ids(self.hand_id_offset)
            # Get and set pronouns
            pronouns = self.get_pronouns(p['gender'])
            new_participant.pronoun_a = pronouns[0]
            new_participant.pronoun_b = pronouns[1]
            new_participant.pronoun_c = pronouns[2]
            # Add participant to the match
            self.participant_list.append(new_participant)

    def add_gestures(self, participant_id, turn_num, gesture_lh, gesture_rh):
        '''Add gestures to the match history, i.e. to self.match_gestures.
        These gestures were taken from player_orders, validated in match_orders.validateOrders(), 
        and possibly changed by spell effects in SpellBook.determineGestures().

        Arguments: 
        participant_id -- integer [1..8], ID of the participant who made gestures
        turn_num -- integer, number of turn on which the gestures were made
        gesture_lh -- str(1), a Left Hand gesture from SpellBook.validGestures set
        gesture_rh -- str(1), a Right Hand gesture from SpellBook.validGestures set
        '''

        g = {
            'gLH': gesture_lh,
            'gRH': gesture_rh,
        }

        if participant_id not in self.match_gestures:
            self.match_gestures.update({participant_id: {}})
        self.match_gestures[participant_id].update({turn_num: g})

    # GET functions

    def get_match_status(self):
        ''' Return current match status: {0: ongoing, 1: finished}
        '''

        return self.match_status

    def get_effect_name(self, code):

        for s in self.effect_names:
            if s == code:
                return self.effect_names[s]
        return ''

    def get_pronouns(self, gender=-1, seed=0):
        ''' Return a tuple with localized pronouns according to gender vaiable.
        If gender is not set, assign random pronouns. These pronouns would later be used
        to format in-game messages where the participant would be mentioned.

        Arguments:
        gender -- integer, {-1: not set, 0: they, 1: she, 2: he}

        Return:
        A tuple with three forms of the selected pronoun
        '''

        if gender == -1:
            gender = random.Random(seed).choice([0, 1, 2])
        if gender == 0:
            pronoun_a = self.get_text_strings_by_code('pronounThey')
            pronoun_b = self.get_text_strings_by_code('pronounThem')
            pronoun_c = self.get_text_strings_by_code('pronounTheir')
        elif gender == 1:
            pronoun_a = self.get_text_strings_by_code('pronounShe')
            pronoun_b = self.get_text_strings_by_code('pronounHer')
            pronoun_c = self.get_text_strings_by_code('pronounHers')
        elif gender == 2:
            pronoun_a = self.get_text_strings_by_code('pronounHe')
            pronoun_b = self.get_text_strings_by_code('pronounHim')
            pronoun_c = self.get_text_strings_by_code('pronounHis')

        return (pronoun_a, pronoun_b, pronoun_c)

    def get_text_strings_by_code(self, code):
        ''' Return a string template for later formatting and output.

        Arguments:
        code -- string, test code name of a localized unformatted string

        Return:
        A localized unformatted string if the code is found, empty string otherwise
        '''

        if code in self.text_strings:
            return self.text_strings[code]
        else:
            # Debug
            #raise NameError('Missing Loc String '+code+'!')
            return ''

    def get_gesture_last(self, participant_id, hand):
        ''' Return the last gesture for this participand and hand.
        Note that on some turns a participant might not have made any gestures,
        so we have to go through all gestures and check turn_num each time.

        Arguments:
        participant ID -- integer [1..8], ID of the participant who made the gesture
        hand -- integer [1, 2], flag for left or right hand

        Return:
        A gesture str(1) that was shown by this participant with this hand if any, '' otherwise
        '''

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
        ''' Return the gesture for this participand and this turn and hand.

        Arguments:
        participant_id -- integer [1..8], ID of the participant who made the gesture
        turn_num -- integer, the number of the turn
        hand -- integer [1, 2], flag for left or right hand

        Return:
        A gesture str(1) that was shown by this participant on this turn with this hand if any, '' otherwise
        '''

        g = ''
        if ((participant_id in self.match_gestures)
                and (turn_num in self.match_gestures[participant_id])):
            if hand == 1:
                g = self.match_gestures[participant_id][turn_num]['gLH']
            elif hand == 2:
                g = self.match_gestures[participant_id][turn_num]['gRH']
        return g

    def get_gesture_history(self, participant_id, hand, spaced=0):
        ''' Return all gestures shown by this participand with this hand during this match.
        Note that on some turns a participant might not have made any gestures,
        and depending on 'spaced' flag we either ignore these turns (if this string is used to match spells)
        or add space (if this string is used for user output / turn log).

        Arguments:
        participant_id -- integer [1..8], ID of the participant who made the gesture
        hand -- integer [1, 2], flag for left or right hand
        spaced -- integer [0, 1], flag for using spaces instead of missing gestures

        Return:
        A gesture history string that was shown by this participant with this hand if any, '' otherwise
        '''

        g = ''
        if participant_id in self.match_gestures:
            for turn_num in range(1, self.current_turn + 1):
                if turn_num in self.match_gestures[participant_id]:
                    if hand == 1:
                        g += self.match_gestures[participant_id][turn_num]['gLH']
                    elif hand == 2:
                        g += self.match_gestures[participant_id][turn_num]['gRH']
                elif spaced == 1:
                    g += ' '
        return g

    def get_next_participant_id(self):
        ''' Return next free ID for a participant (normally in [1..8] range)
        '''

        return len(self.participant_list) + 1

    def get_next_monster_id(self):
        ''' Return next free ID for a monster (normally in [101..] range)
        '''

        return self.monster_id_offset + len(self.monster_list) + 1

    def get_actor_by_id(self, actor_id, search_alive_only=1):
        ''' Return a SpellBook-specific inheritant of an Actor object.

        Arguments:
        actor_id -- integer, which can be participant_id, hand_id or monsterID.
        search_alive_only -- boolean flag to search only for alive actors or for all actors.

        Return:
        An object of Participant or Monster classes - or their SpellBook-specific 
        inheritants like WarlocksParticipant and WarlocksMonster.
        '''

        target = None
        if actor_id in self.get_list_of_participants_ids(search_alive_only):
            target = self.get_participant_by_id(actor_id, search_alive_only)
        elif actor_id in self.get_list_of_monsters_ids(search_alive_only):
            target = self.get_monster_by_id(actor_id, search_alive_only)
        elif actor_id in self.get_list_of_participants_hands_ids(search_alive_only):
            target = self.get_monster_by_turn_and_hand(
                self.current_turn, actor_id, search_alive_only)
        return target

    def get_list_of_targets_ids(self, search_alive_only=1):
        ''' Return a list of all viable target IDs (participants, hands, monsters).

        Arguments:
        search_alive_only -- boolean flag to search only for alive actors or for all actors.

        Return:
        A list of integer IDs.
        '''

        return (self.get_list_of_participants_ids(search_alive_only)
                + self.get_list_of_participants_hands_ids(search_alive_only)
                + self.get_list_of_monsters_ids(search_alive_only))

    def get_list_of_participants_ids(self, search_alive_only=1):
        ''' Return a list of all viable IDs of participants.

        Arguments:
        search_alive_only -- boolean flag to search only for alive actors or for all actors.

        Return:
        A list of integer IDs.
        '''

        l = []
        for p in self.participant_list:
            if (not search_alive_only) or (search_alive_only and p.is_alive):
                l.append(p.id)
        return l

    def get_list_of_opponents_ids(self, participant_id, search_alive_only=1):
        ''' Return a list of all viable IDs of opponents (i.e. participants with a different team number)
        of a specific participant.

        Arguments:
        participant_id -- integer [1..8], a participant that wants to know IDs of their opponents
        search_alive_only -- boolean flag to search only for alive actors or for all actors.

        Return:
        A list of integer IDs.
        '''

        p = self.get_participant_by_id(participant_id)
        team_id = p.team_id
        l = []
        for p in self.participant_list:
            if p.team_id != team_id:
                if (not search_alive_only) or (search_alive_only and p.is_alive):
                    l.append(p.id)
        return l

    def get_random_opponent_id(self, participant_id):
        ''' Return an ID of a randomly-selected opponent.

        Arguments:
        participant_id -- integer [1..8], a participant that wants to know IDs of their opponents

        Return:
        Integer ID.
        '''

        return random.Random(self.match_id + self.current_turn + participant_id).choice(
            self.get_list_of_opponents_ids(participant_id))

    def get_list_of_participants_hands_ids(self, search_alive_only=1):
        ''' Return a list of all viable IDs of participants' hands.

        Arguments:
        search_alive_only -- boolean flag to search only for alive actors or for all actors.

        Return:
        A list of integer IDs.
        '''

        l = []
        for p in self.participant_list:
            if (not search_alive_only) or (search_alive_only and p.is_alive):
                l.append(p.lh_id)
                l.append(p.rh_id)
        return l

    def get_list_of_monster_ids_by_type(self, type, search_alive_only=1):
        ''' Return a list of all viable IDs of monsters of specified type.
        This is mostly used to control the population of elementals (types 5 and 6).

        Arguments:
        type -- integer, requested monster type. For Warlocks it would be in range [1..6]
        search_alive_only -- boolean flag to search only for alive actors or for all actors.

        Return:
        A list of integer IDs.
        '''

        l = []
        for m in self.monster_list:
            if m.monster_type == type:
                if (not search_alive_only) or (search_alive_only and m.is_alive):
                    l.append(m.id)
        return l

    def get_list_of_monsters_ids(self, search_alive_only=1):
        ''' Return a list of all viable IDs of monsters.

        Arguments:
        search_alive_only -- boolean flag to search only for alive actors or for all actors.

        Return:
        A list of integer IDs.
        '''

        l = []
        for m in self.monster_list:
            if (not search_alive_only) or (search_alive_only and m.is_alive):
                l.append(m.id)
        return l

    def get_participant_by_id(self, participant_id, search_alive_only=1):
        ''' Return a SpellBook-specific inheritant of Participant object.

        Arguments:
        ID -- integer, which is participant_id.
        search_alive_only -- boolean flag to search only for alive actors or for all actors.

        Return:
        An instance of a SpellBook-specific inheritant of Participant object.
        '''

        for p in self.participant_list:
            if p.id == participant_id:
                if (not search_alive_only) or (search_alive_only and p.is_alive):
                    return p
                else:
                    break

    def get_monster_by_id(self, monster_id, search_alive_only=1):
        ''' Return a SpellBook-specific inheritant of Monster object.

        Arguments:
        ID -- integer, which is monsterID.
        search_alive_only -- boolean flag to search only for alive actors or for all actors.

        Return:
        An instance of a SpellBook-specific inheritant of Monster object.
        '''

        for m in self.monster_list:
            if m.id == monster_id:
                if (not search_alive_only) or (search_alive_only and m.is_alive):
                    return m
                else:
                    break

    def get_monster_by_turn_and_hand(self, turn_num, hand_id, search_alive_only=1):
        ''' Return a SpellBook-specific inheritant of Monster object.
        This is used if the monster is summoned this turn, and it was originally targeted by hand ID.

        Arguments:
        turn_num -- integer, turn number.
        hand_id -- integer, ID of a hand that was used to summon a monster.
        search_alive_only -- boolean flag to search only for alive actors or for all actors.

        Return:
        An instance of a SpellBook-specific inheritant of Monster object.
        '''

        for m in self.monster_list:
            if (m.summoner_hand_id == hand_id) and (m.summon_turn == turn_num):
                if (not search_alive_only) or (search_alive_only and m.is_alive):
                    return m
                else:
                    break

    # SET functions

    def set_match_status(self, status):
        ''' Update current match status.

        Arguments:
        status -- boolean, {0: ongoing, 1: finished}
        '''

        self.match_status = status

    def set_current_turn(self, turn_num):
        ''' Update current turn number.

        Arguments:
        turn_num -- integer, turn number.
        '''

        self.current_turn = turn_num

    def set_destroy_monster_now_by_id(self, monster_id):
        ''' Mark monster as dead.

        Arguments:
        monster_id -- integer, monster ID
        '''

        for m in self.monster_list:
            if m.is_alive and (m.id == monster_id):
                m.is_alive = 0
                break

    def set_destroy_monster_before_attack_by_id(self, monster_id):
        ''' Flag monster to die this turn before attacks.
        We do not kill them right away as they still might be a target of another spell or interact somehow.

        Arguments:
        monster_id -- integer, monster ID
        '''

        if monster_id in self.get_list_of_monsters_ids():
            m = self.get_monster_by_id(monster_id)
            m.set_destroy_before_attack()
        elif monster_id in self.get_list_of_participants_hands_ids():
            m = self.get_monster_by_turn_and_hand(
                self.current_turn, monster_id)
            m.set_destroy_before_attack()

    def set_destroy_actor_eot_by_id(self, actor_id):
        ''' Flag actor to die in the end of the turn.
        They still get to attack or do something else.

        Arguments:
        actor_id -- integer, actor ID
        '''

        for participant_id in self.get_list_of_participants_ids():
            if participant_id == actor_id:
                p = self.get_participant_by_id(participant_id)
                p.set_destroy_eot()
                break

        for monster_id in self.get_list_of_monsters_ids():
            if monster_id == actor_id:
                m = self.get_monster_by_id(monster_id)
                m.set_destroy_eot()
                break

        for hand_id in self.get_list_of_participants_hands_ids():
            if hand_id == actor_id:
                m = self.get_monster_by_turn_and_hand(
                    self.current_turn, hand_id)
                m.set_destroy_eot()
                break

    def set_gestures(self, participant_id, turn_num, gesture_lh, gesture_rh):
        ''' Save gestures made by participant_id on turn_num

        Arguments:
        participant_id -- integer [1..8], a participant that wants to know IDs of their opponents
        turn_num -- integer, turn number.
        gesture_lh -- str(1), left hand gesture
        gesture_rh -- str(1), right hand gesture
        '''

        g = {
            'gLH': gesture_lh,
            'gRH': gesture_rh,
        }

        self.match_gestures[participant_id].update({turn_num: g})

    def kill_monsters_before_attack(self):
        ''' Set isAlive to 0 for monsters marked to be destroyed before attack phase.
        '''

        for m in self.monster_list:
            if m.is_alive and (m.destroy_before_attack == 1):
                m.is_alive = 0
                self.add_log_entry(m.id, 11, 'resultActorDies', name=m.name)

    def kill_monsters_eot(self):
        ''' Set isAlive to 0 for monsters marked to be destroyed in the end of turn.
        '''

        for m in self.monster_list:
            if m.is_alive and (m.hp <= 0 or m.destroy_eot == 1):
                m.is_alive = 0
                self.add_log_entry(m.id, 11, 'resultActorDies', name=m.name)

    def kill_participants_eot(self):
        ''' Set isAlive to 0 for participants marked to be destroyed in the end of turn.
        '''

        for p in self.participant_list:
            if p.is_alive and (p.hp <= 0 or p.destroy_eot == 1):
                p.is_alive = 0
                self.add_log_entry(p.id, 11, 'resultActorDies', name=p.name)

    def check_match_end_eot(self):
        ''' End of Turn check for match end. Match end is triggered 
        and match status is updated if all alive players belong to the same team.
        '''

        # Make a list to flag teams still present in the match
        # max 8 teams, l[0] and l[9] not used
        l = [0] * self.hand_id_offset
        for p in self.participant_list:
            if p.is_alive:
                l[p.team_id] = 1

        # If more than one team left, do nothing.

        # If only one team left, get tead ID, then get participant names,
        # and print names of all participants (even dead) of the team.
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
                self.add_log_entry(
                    p.id, 12, 'resultActorVictorious', name=namestr)
            else:
                namestr = ', '.join(names[0:-1:1]) + ' & ' + names[-1]
                self.add_log_entry(
                    p.id, 12, 'resultTeamVictorious', name=namestr)
            self.set_match_status(1)

        # If no teams left, declare a draw.
        elif sum(l) == 0:
            self.add_log_entry(p.id, 12, 'resultDraw')
            self.set_match_status(1)

    def give_single_attack_order(self, m, attack_id):
        ''' Process single attack order for a single monster.

        Arguments:
        m -- an instance of SpellBook-specific Monster-inherited object
        attack_id -- ID of attack target from player Orders.
        '''

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
            elif attack_id in self.get_list_of_monsters_ids(search_alive_only):
                target = self.get_monster_by_id(attack_id)
                order_counted = 1
            elif attack_id in self.get_list_of_participants_hands_ids(search_alive_only):
                target = self.get_monster_by_turn_and_hand(
                    self.current_turn, attack_id)
                attack_id = target.ID
                order_counted = 1
            elif attack_id in self.get_list_of_participants_ids(search_alive_only):
                target = self.get_participant_by_id(attack_id)
                order_counted = 1
            # If target not found, redirect to nobody
            else:
                attack_id = 0
        # save updated target
        m.attack_id = attack_id

        # print report if a valid order was given
        if order_counted:
            if target is None:
                targetname = self.get_text_strings_by_code('nameNobody')
            else:
                targetname = target.name
            controller = self.get_participant_by_id(m.controller_id)
            self.add_log_entry(controller.id, 6, 'attackOrder',
                               name=controller.name,
                               targetname=m.name,
                               attackname=targetname)

    def give_attack_orders(self, match_orders):
        ''' Process portion of turn Orders related to attacks.

        Arguments:
        match_orders -- a list of Order-objects
        '''

        search_alive_only = 1
        # checking all attack orders for participants acting this turn
        for participant_id in self.get_list_of_participants_ids_active_this_turn():
            player_orders = match_orders.search_orders(self.match_id,
                                                       self.current_turn, participant_id)
            if player_orders.attack_orders:
                for order_id in player_orders.attack_orders:
                    # trying to locate the object this order belongs to among monsters
                    if order_id in self.get_list_of_monsters_ids(search_alive_only):
                        m = self.get_monster_by_id(order_id)
                    # trying to locate the object this order belongs to among new summons
                    elif order_id in self.get_list_of_participants_hands_ids(search_alive_only):
                        m = self.get_monster_by_turn_and_hand(
                            self.current_turn, order_id)
                    # if object found, check check if order source is correct
                    # ignore orders that do not come from anyone other than monster controller
                    if m and (m.controller_id == participant_id):
                        attack_id = player_orders.attack_orders[order_id]
                        self.give_single_attack_order(m, attack_id)

    def add_log_entry(self, actor_id, str_type, str_code, name='', pronoun='',
                      targetname='', spellname='', attackname='',
                      damage='', handname=''):
        ''' Log a game action.

        Arguments:
        actor_id -- integer, ID of actor related to the action (i.e. caster of a spell)
        str_type -- integer, type of action, at the moment not well researched / follows RB colours
        str_code -- string, code to fetch unformatted string from localization files
        name, pronoun, targetname, spellname, attackname, damage, handname - strings that 
            are used to format string (fetched using str_code) later.
        '''

        new_log_id = len(self.match_log)
        log_entry = {'log_id': new_log_id, 'match_id': self.match_id,
                     'turn_num': self.current_turn, 'actor_id': actor_id,
                     'str_type': str_type, 'str_code': str_code,
                     'name': name, 'pronoun': pronoun, 'targetname': targetname,
                     'spellname': spellname, 'attackname': attackname,
                     'damage': damage, 'handname': handname
                     }
        self.match_log.append(log_entry)

    # OUTPUT functions

    def print_actor_status_by_id(self, actor_id):
        ''' Output actor status, including name, HP, statuses, controller and attack target (for monsters), etc.

        This is a placeholder that should be reworked for future front-end implementation.

        Arguments:
        actor_id -- integer, actor ID
        '''

        a = self.get_actor_by_id(actor_id, 0)

        slist = []
        s = self.get_text_strings_by_code('statusName').format(name=a.name)
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

        for key in a.statuses:
            if a.statuses[key] > 0:
                s1 = self.get_effect_name(key)
                if a.statuses[key] == self.permanent_duration:
                    s2 = self.get_text_strings_by_code('statusPermanent')
                else:
                    s2 = str(a.statuses[key])
                s = self.get_text_strings_by_code(
                    'statusEffectLength').format(spellname=s1, damage=s2)
                slist.append(s)
        if a.type == 1 and a.state_delayed_spell is not None:
            s = self.get_text_strings_by_code('statusStored').format(
                spellname=a.state_delayed_spell.name)
            slist.append(s)

        s = ', '.join(slist)
        print(s)

    def print_match_actors_status(self):
        ''' Output statuses for all actors and gesture history for all participants).

        This is a placeholder that should be reworked for future front-end implementation.
        '''

        for participant_id in self.get_list_of_participants_ids(0):
            self.print_actor_status_by_id(participant_id)
            tstr = ''
            for i in range(0, self.current_turn + 1):
                tstr += str(i % 10)
            print(self.get_text_strings_by_code('statusTurn') + tstr)
            print(self.get_text_strings_by_code('statusLH') + 'B' +
                  self.get_gesture_history(participant_id, 1, 1))
            print(self.get_text_strings_by_code('statusRH') + 'B' +
                  self.get_gesture_history(participant_id, 2, 1))
        for monster_id in self.get_list_of_monsters_ids():
            self.print_actor_status_by_id(monster_id)

    def print_log_entry(self, log_id):
        ''' Format and output a log entry.

        This is a placeholder that should be reworked for future front-end implementation.

        Arguments:
        log_id -- integer, ID of log entry
        '''

        log_entry = self.match_log[log_id]

        if self.get_text_strings_by_code(log_entry['str_code']):
            strf = self.get_text_strings_by_code(log_entry['str_code']).format(name=log_entry['name'],
                                                                               pronoun=log_entry['pronoun'],
                                                                               targetname=log_entry['targetname'],
                                                                               spellname=log_entry['spellname'],
                                                                               attackname=log_entry['attackname'],
                                                                               damage=log_entry['damage'],
                                                                               handname=log_entry['handname'])
            print(strf)
        else:
            # dprint(log_entry)
            pass

    def print_log_entries_by_turn(self, turn_num):
        ''' Select log entried related to a specific turn and print them.

        This is a placeholder that should be reworked for future front-end implementation.

        Arguments:
        turn_num -- integer, turn number.
        '''

        for l in self.match_log:
            if l['turn_num'] == turn_num:
                self.print_log_entry(l['log_id'])

        print(' ')
