import random
from class_matchdata import MatchData
from class_warlocks_actor import WarlocksParticipant, WarlocksMonster


class WarlocksMatchData(MatchData):
    '''This class contains current match state, with some exceptions.
    - match_id and current_turn are obvious.
    - participantList and monster_list contain all match actors, alive and dead.
    - matchGestures contain history of gestures for all players all hands.
    - matchLog contain history of all events happened
    - textStings contains all warlocks text strings in the current loc
    '''

    def __init__(self, match_id):

        MatchData.__init__(self, match_id)

        self.current_turn_type = 1  # 1 - normal, 2 - hasted, 3 - timestopped
        self.prev_turn_type = 1

        self.current_turn_fire_storms = 0
        self.current_turn_ice_storms = 0
        self.current_turn_elementals_clash = 0

        self.hand_id_offset = 10
        self.monster_id_offset = 100

        self.permanent_duration = 9999

        self.monster_types = {
            1: {'start_hp': 1, 'max_hp': 2, 'attack_damage': 1, 'attack_type': 'Physical', 'attacks_all': 0, 'initial_statuses': {}},
            2: {'start_hp': 2, 'max_hp': 3, 'attack_damage': 2, 'attack_type': 'Physical', 'attacks_all': 0, 'initial_statuses': {}},
            3: {'start_hp': 3, 'max_hp': 4, 'attack_damage': 3, 'attack_type': 'Physical', 'attacks_all': 0, 'initial_statuses': {}},
            4: {'start_hp': 4, 'max_hp': 5, 'attack_damage': 4, 'attack_type': 'Physical', 'attacks_all': 0, 'initial_statuses': {}},
            5: {'start_hp': 3, 'max_hp': 4, 'attack_damage': 3, 'attack_type': 'Fire', 'attacks_all': 1, 'initial_statuses': {'ResistHeat': 9999}},
            6: {'start_hp': 3, 'max_hp': 4, 'attack_damage': 3, 'attack_type': 'Ice', 'attacks_all': 1, 'initial_statuses': {'ResistCold': 9999}}
        }

    # INIT and ADD functions

    def create_participant(self, player_id, player_name, team_id):
        ''' Creates an instance of Participant-inherited class.

        Arguments:
        player_id -- integer, a user ID to link game profile to in-match participant ID
        player_name -- string, player name to display
        team_id -- integer [1..8], selected at the start of the match.

        Returns:
        An instance of Participant-inherited class.
        '''

        new_participant = WarlocksParticipant(player_id, player_name, team_id)
        return new_participant

    def create_monster(self, controller_id, monster_type,
                       summoner_id, summoner_hand_id, summon_turn,
                       pronoun_a, pronoun_b, pronoun_c):
        ''' Creates an instance of Monster-inherited class.

        Arguments:
        controller_id -- integer [1..8], ID of the participant that controls the monster
        monster_type -- integer [1..6], monster type
        summoner_id -- integer [1..8], ID of the participant that summoned the monster
        summoner_hand_id -- integer, ID of the hand that was used to summon monster
        summon_turn -- integer, the numbre of turn when the monster was summoned
        pronoun_a, pronoun_b, pronoun_c -- strings, three forms of participant pronoun

        Returns:
        An instance of Monster-inherited class.
        '''

        new_monster = None
        if monster_type in self.monster_types:
            new_monster = WarlocksMonster(self.monster_types, controller_id, monster_type,
                                          summoner_id, summoner_hand_id, summon_turn,
                                          pronoun_a, pronoun_b, pronoun_c)
        return new_monster

    # GET functions

    def get_new_monster_name(self, monster_type):
        ''' Request a new name from name repository.
        For elemental the name is always the same (Fire Elemental and Ice Elemental respectively).
        For Goblins, Ogres, Trolls and Giants we cycle through previously shuffled list;
        if we have exhaused the list, we start over adding 'Very ' in front of name;
        this can be repeated indefinitely (i.e. at some moment there might be 'Very Very Green Goblin').

        Arguments:
        monster_type -- integer [1..6], monster type
        '''

        monster_name = ''
        if monster_type in [1, 2, 3, 4]:
            # Count all monsters of the monster_type, alive and dead
            count = self.get_count_named_monsters(monster_type)
            # Compare with the size of name list for this monster_type
            size = len(self.monster_names[monster_type])
            monster_name = (self.get_text_strings_by_code('nameMonsterExtra') * (count // size)
                            + self.monster_names[monster_type][count % size]
                            + ' ' + self.monster_classes[monster_type])
        elif monster_type in [5, 6]:
            monster_name = self.monster_names[monster_type][0]

        return monster_name

    def get_count_named_monsters(self, monster_type):
        ''' Counts the amount of already named (= already created) monsters of monster_type in this match.

        Arguments:
        monster_type -- integer [1..6], monster type

        Returns:
        Integer, monster count.
        '''

        c = 0
        for m in self.monster_list:
            if m.monster_type == monster_type and m.name > '':
                c += 1
        return c

    def get_gesture_log_entry(self, gesture_lh, gesture_rh):
        ''' Get codes for localized strings for LH and RH gestures to use in log.

        Arguments:
        gesture_lh, gesture_rh -- str(1), gestures for LH and RH

        Returns:
        tuple with codes of strings
        '''

        text_lh = ''
        text_rh = ''

        if gesture_lh == 'C' and gesture_rh == 'C':
            text_lh = 'gestureC'
            return (text_lh, text_rh)

        match gesture_lh:
            case '-':
                text_lh = 'gestureN'
            case 'C':
                text_lh = 'gestureC2'
            case 'D':
                text_lh = 'gestureD'
            case 'F':
                text_lh = 'gestureF'
            case 'P':
                text_lh = 'gestureP'
            case 'S':
                text_lh = 'gestureS'
            case 'W':
                text_lh = 'gestureW'
            case '>':
                text_lh = 'gestureT'

        match gesture_rh:
            case '-':
                text_rh = 'gestureN'
            case 'C':
                text_rh = 'gestureC2'
            case 'D':
                text_rh = 'gestureD'
            case 'F':
                text_rh = 'gestureF'
            case 'P':
                text_rh = 'gestureP'
            case 'S':
                text_rh = 'gestureS'
            case 'W':
                text_rh = 'gestureW'
            case '>':
                text_rh = 'gestureT'

        return (text_lh, text_rh)

    def get_list_of_participants_ids_hasted(self):
        ''' Get list of participants that are affected by Haste this turn.

        Returns:
        List with integer IDs
        '''

        l = []
        for participant_id in self.get_list_of_participants_ids():
            p = self.get_participant_by_id(participant_id)
            if p.affected_by_haste():
                l.append(participant_id)
        return l

    def get_list_of_participants_ids_timestopped(self):
        ''' Get list of participants that are affected by Timestop this turn.

        Returns:
        List with integer IDs
        '''

        l = []
        for participant_id in self.get_list_of_participants_ids():
            p = self.get_participant_by_id(participant_id)
            if p.affected_by_timestop():
                l.append(participant_id)
        return l

    def get_list_of_participants_ids_active_this_turn(self):
        ''' Get list of participants that are active this turn.

        Returns:
        List with integer IDs
        '''

        if self.is_current_turn_timestopped():
            return self.get_list_of_participants_ids_timestopped()
        if self.is_current_turn_hasted():
            return self.get_list_of_participants_ids_hasted()
        return self.get_list_of_participants_ids()

    def is_current_turn_hasted(self):
        ''' Check if the current turn is Hasted

        Returns:
        Boolean, 1 is turn is Hasted, 0 otherwise
        '''

        if self.current_turn_type == 2:
            return 1
        else:
            return 0

    def is_current_turn_timestopped(self):
        ''' Check if the current turn is Timestopped

        Returns:
        Boolean, 1 is turn is Timestopped, 0 otherwise
        '''

        if self.current_turn_type == 3:
            return 1
        else:
            return 0

    # TURN LOGIC functions

    def set_current_turn_type(self):
        ''' Determine current turn type.
        {1: Normal; 2: Hasted; 3: Timestopped}
        '''

        self.prev_turn_type = self.current_turn_type

        if self.get_list_of_participants_ids_timestopped():
            self.current_turn_type = 3  # timestopped
        elif self.get_list_of_participants_ids_hasted():
            if self.prev_turn_type == 2:
                self.current_turn_type = 1  # normal
            else:
                self.current_turn_type = 2  # hasted
        else:
            self.current_turn_type = 1  # normal

    def check_sickness_statuses(self):
        ''' Check participants affected by Disease or Poison. 
        Those who reached status 1, die EOT.
        '''

        for p in self.participant_list:
            if p.is_alive:
                if p.statuses['Disease'] == 1:
                    self.add_log_entry(
                        p.id, 9, 'effectDiseaseFatal', name=p.name)
                    p.destroy_eot = 1

                if p.statuses['Poison'] == 1:
                    self.add_log_entry(
                        p.id, 9, 'effectPoisonFatal', name=p.name)
                    p.destroy_eot = 1

    def check_antispell_statuses(self):
        ''' Check participants affected by Anti-Spell and update their last gestures with -/-
        We do this EOT, since we need to do stabs after spell casting, and other way around is even messy-er.
        '''

        for p in self.participant_list:
            if p.is_alive:
                if p.statuses['AntiSpell'] == 1:
                    self.set_gestures(p.id, self.current_turn, '-', '-')

    def kill_suicided_participants(self, match_orders):
        ''' Set is_alive to 0 for participants who were affectedd by perm mindspell and gave the suicide order.

        Arguments:
        match_orders -- an instance of spellbook-specific Orders class with orders for this turn.
        '''

        for participant_id in self.get_list_of_participants_ids():
            order = match_orders.search_orders(
                self.match_id, self.current_turn, participant_id)
            p = self.get_participant_by_id(participant_id)
            if (p.affected_by_permanent_mindspell()) and (order.commit_suicide == 1):
                p.is_alive = 0
                self.add_log_entry(
                    p.id, 11, 'resultActorSuicides', name=p.name)

    def kill_surrendered_participants(self, turn_num):
        ''' Set is_alive to 0 for participants who showed P/P

        Arguments:
        turn_num -- integer, turn number
        '''

        for p in self.participant_list:
            if (p.is_alive
                    and self.get_gesture(p.id, turn_num, 1) == 'P'
                    and self.get_gesture(p.id, turn_num, 2) == 'P'):
                p.is_alive = 0
                self.add_log_entry(
                    p.id, 11, 'resultActorSurrenders', name=p.name)

    def update_statuses_on_monsters_eot(self):
        ''' EOT tick down all statuses on monsters.
        Skipped for timestopped turns.
        '''

        for m in self.monster_list:
            if m.is_alive:
                for s in m.statuses:
                    if not self.is_current_turn_timestopped():
                        m.decrease_status(s)
                m.state_mindspells_this_turn = 0

    def update_statuses_on_participants_eot(self):
        ''' EOT tick down all statuses on participants.
        Skipped for turns that are followed by hasted or timestopped turns.
        '''

        # Tmp determine next turn type
        next_turn_type = 1
        next_turn_haste_counter = 0
        next_turn_timestop_counter = 0
        for p in self.participant_list:
            if p.is_alive:
                if p.statuses_next['TimeStop'] > 0:
                    next_turn_timestop_counter += 1
                if self.current_turn_type == 1 and (p.statuses['Haste'] > 0 or p.statuses_next['Haste'] > 0):
                    next_turn_haste_counter += 1
        if next_turn_timestop_counter:
            next_turn_type = 3
        elif next_turn_haste_counter:
            next_turn_type = 2

        for p in self.participant_list:
            if p.is_alive:
                for s in p.statuses:

                    # Log the end of Blindness / Invisibility
                    if s == 'Blindness' and p.statuses[s] == 1:
                        self.add_log_entry(
                            p.id, 8, 'effectBlindness2', name=p.name)
                    if s == 'Invisibility' and p.statuses[s] == 1:
                        self.add_log_entry(
                            p.id, 8, 'effectInvisibility2', name=p.name)

                    # Decrease non-mindspell statuses if next turn is normal.
                    # Decrease minspell-statuses if current turn is normal
                    if s in ['Fear', 'Maladroitness', 'Paralysis', 'Amnesia', 'CharmPerson']:
                        if self.current_turn_type == 1:
                            p.decrease_status(s)
                    else:
                        if next_turn_type == 1:
                            p.decrease_status(s)

                    # Push statuses_next into statuses if next turn is normal or hasted
                    # If next turn is timestopped, only push in Timestop status,
                    # and keep the rest for the next non-timestopped turn
                    if (next_turn_type in [1, 2]):
                        if s in p.statuses_next and (p.statuses_next[s] > p.statuses[s]):
                            p.statuses[s] = p.statuses_next[s]
                            p.statuses_next[s] = 0
                    elif (next_turn_type in [3]):
                        if s == 'TimeStop':
                            p.statuses[s] = p.statuses_next[s]
                            p.statuses_next[s] = 0

                    # Log the start of Blindness / Invisibility
                    if s == 'Blindness' and p.statuses[s] == 3:
                        self.add_log_entry(
                            p.id, 8, 'effectBlindness1', name=p.name)
                    if s == 'Invisibility' and p.statuses[s] == 3:
                        self.add_log_entry(
                            p.id, 8, 'effectInvisibility1', name=p.name)

                if (self.current_turn_type == 1):
                    # A lot of Paralyze housekeeping - we need to keep track
                    # who paralyzed partiicpant of turns before and after, and which hand
                    p.paralyzed_by_id_prev = p.paralyzed_by_id
                    p.paralyzed_by_id = p.paralyzed_by_id_next
                    p.paralyzed_by_id_next = 0
                    p.paralyzed_hand_id_prev = p.paralyzed_hand_id
                    p.paralyzed_hand_id = 0
                    # Charm Person housekeeping
                    p.charmed_by_id = p.charmed_by_id_next
                    p.charmed_by_id_next = 0
                    p.charmed_hand_id = 0
                    p.charm_same_gestures = 0
                # If the next turn is hasted or timesstopped, do not zero mindspell counter
                # top allow fast players to clash mindspells on the extra turn
                if (next_turn_type in [1]):
                    p.state_mindspells_this_turn = 0

    def attack_action(self, a, d, check_mindspells=1, check_visibility=1, check_shields=1):
        ''' Resolve a single attack action.

        a -- object, Monster or Participant
        d -- object, Monster or Participant
        check_mindspells -- boolean, flag to check minsdpell effects that prevent attack
        check_visibility -- boolean, flag to check visibility (Blindness, Invis)
        check_shields -- boolean, flag to chech shields (PShield, Protection, Resists)
        '''

        # If we check shields and other effects that prevent attacks,
        # we check for mindspells on attacker, but only for monsters
        if check_mindspells == 1 and a.type == 2 and a.affected_by_paralysis():
            self.add_log_entry(a.id, 8, 'effectParalysis2', targetname=a.name)
            return
        if check_mindspells == 1 and a.type == 2 and a.affected_by_amnesia():
            self.add_log_entry(a.id, 8, 'effectAmnesia2', targetname=a.name)
            return
        if check_mindspells == 1 and a.type == 2 and a.affected_by_fear():
            self.add_log_entry(a.id, 8, 'effectFear2', targetname=a.name)
            return
        if check_mindspells == 1 and a.type == 2 and a.affected_by_maladroitness():
            self.add_log_entry(
                a.id, 8, 'effectMaladroitness2', targetname=a.name)
            return

        # If we check visibility, we check visibility between attacker and defender
        if check_visibility == 1 and a.affected_by_blindness():
            self.add_log_entry(a.id, 10, 'attackMissesBlindness',
                               name=a.name,
                               attackname=d.name)
            return
        if check_visibility == 1 and d.affected_by_invisibility():
            self.add_log_entry(a.id, 10, 'attackMissesInvisibility',
                               name=a.name,
                               attackname=d.name)
            return

        # If we got here, we can actually attack.
        # a = Fire elem
        if a.attack_type == 'Fire':
            if check_shields == 1 and d.affected_by_resist_heat():
                self.add_log_entry(a.id, 7, 'effectResistHeat', name=d.name)
            elif check_shields == 1 and d.affected_by_pshield():
                self.add_log_entry(a.id, 10, 'effectShieldFromElemental',
                                   attackname=d.name, name=a.name)
            else:
                d.decrease_hp(a.attack_damage)
                self.add_log_entry(a.id, 9, 'damagedByFireElem',
                                   attackname=d.name, damage=a.attack_damage)
        # a = Ice elem
        elif a.attack_type == 'Ice':
            if check_shields == 1 and d.affected_by_resist_cold():
                self.add_log_entry(a.id, 7, 'effectResistCold', name=d.name)
            elif check_shields == 1 and d.affected_by_pshield():
                self.add_log_entry(a.id, 10, 'effectShieldFromElemental',
                                   attackname=d.name, name=a.name)
            else:
                d.decrease_hp(a.attack_damage)
                self.add_log_entry(a.id, 9, 'damagedByIceElem',
                                   attackname=d.name, damage=a.attack_damage)
        # a = monster or stabbing participant
        elif a.attack_type == 'Physical':
            # if a is a timestopped monster, then it deals damage anyways
            # if a is a timestopped participant, then we should check d.affected_by_pshield(1, 0) - shield but not protection
            # if a is a regular participant, then we should check d.affected_by_pshield(1, 1) or simply d.affected_by_pshield()
            if (check_shields == 0 and a.type == 2
                or check_shields == 0 and a.type == 1 and d.affected_by_pshield(1, 0) == 0
                    or d.affected_by_pshield() == 0):
                d.decrease_hp(a.attack_damage)
                self.add_log_entry(a.id, 9, 'damagedByMonster', name=a.name,
                                   attackname=d.name, damage=a.attack_damage)
            else:
                self.add_log_entry(a.id, 10, 'effectShieldFromMonster',
                                   name=a.name, attackname=d.name)

    def check_stabs(self, match_orders):
        ''' Check for stab orders and resolve them.

        Arguments:
        match_orders -- object, an instance of Spellbook-inherited Orders
        '''

        for p in self.participant_list:
            if p.is_alive:
                gesture_lh = self.get_gesture(p.id, self.current_turn, 1)
                gesture_rh = self.get_gesture(p.id, self.current_turn, 2)
                player_orders = match_orders.search_orders(self.match_id,
                                                           self.current_turn, p.id)
                # Get current turn gestures for all participants
                attack_id = 0
                stab_hand_name = ''
                # If RH or LH tried to stab, use that as an order.
                # If both stabbed, Lh is ignored, consider that dagger is in RH.
                if gesture_rh == '>':
                    attack_id = player_orders.order_target_rh
                    stab_hand_name = self.get_text_strings_by_code(
                        'nameRightHand')
                elif gesture_lh == '>':
                    attack_id = player_orders.order_target_lh
                    stab_hand_name = self.get_text_strings_by_code(
                        'nameLeftHand')
                else:
                    continue
                # Check if there was a target order. If not, get random opponent ID.
                if attack_id == -1:
                    attack_id = self.get_random_opponent_id(p.id)
                # Get target object
                if attack_id > 0:
                    target = self.get_participant_by_id(attack_id)
                    if target is None:
                        target = self.get_monster_by_id(attack_id)
                    if target is None:
                        target = self.get_monster_by_turn_and_hand(
                            self.current_turn, attack_id)
                    if target is None:
                        attack_id = 0
                # Adjust shield and visibility checks based on turn type.
                if stab_hand_name:
                    if self.is_current_turn_timestopped():
                        check_visibility = 0
                        check_shields = 0
                    else:
                        check_visibility = 1
                        check_shields = 1
                    # Commence stab
                    if attack_id > 0:
                        check_mindspells = 0
                        self.attack_action(
                            p, target, check_mindspells, check_visibility, check_shields)
                    else:
                        self.add_log_entry(p.id, 10, 'stabMissesNobody',
                                           name=p.name)

    def attack_phase(self, phase_type):
        ''' Process attack phase of a normal turn (and skip phase for hasted and timestopped turns).
        Note the difference. On timestopped or hasted turns (turns when there are 
        timestopped or hasted participants); on such turns there is no attack phase at all.
        But on normal turns there can be up to 3 attack phases, first for normal monsters, 
        second for hasted monsters and third for timestopped monsters.

        Arguments:
        phase_type -- integer; {1: Normal monsters; 2: Hasted monsters; 3: Timestopped monsters}
        '''

        # Skip attack phase entirely if turn is for timestopped or hasted participants
        # Note that a monster summoned during timestopped turn would not attack as well.
        if self.is_current_turn_hasted() or self.is_current_turn_timestopped():
            return

        # For all monsters alive and of status appropriate to phase_type
        for m in self.monster_list:
            if m.is_alive and (phase_type == 1
                               or (phase_type == 2 and m.affected_by_haste())
                               or (phase_type == 3 and m.affected_by_timestop())):
                # If monsters attacks everyone
                if m.attacks_all:

                    check_visibility = 0
                    if phase_type == 1:
                        if m.monster_type == 5:
                            self.add_log_entry(m.id, 9, 'attackFireElem')
                        elif m.monster_type == 6:
                            self.add_log_entry(m.id, 9, 'attackIceElem')
                        check_shields = 1
                    elif phase_type == 2:
                        if m.monster_type == 5:
                            self.add_log_entry(m.id, 9, 'attackFireElemHasted')
                        elif m.monster_type == 6:
                            self.add_log_entry(m.id, 9, 'attackIceElemHasted')
                        check_shields = 1
                    elif phase_type == 3:
                        if m.monster_type == 5:
                            self.add_log_entry(
                                m.id, 9, 'attackFireElemTimestopped')
                        elif m.monster_type == 6:
                            self.add_log_entry(
                                m.id, 9, 'attackIceElemTimestopped')
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
                        target = self.get_participant_by_id(m.attack_id)
                        if target is None:
                            target = self.get_monster_by_id(m.attack_id)
                        if target is None:
                            target = self.get_monster_by_turn_and_hand(
                                current_turn, m.attack_id)
                        if target is None:
                            m.attack_id = 0
                    # Determine if visibility and shields affect attacks in this phase
                    if phase_type == 1:
                        check_visibility = 1
                        check_shields = 1
                    elif phase_type == 2:
                        self.add_log_entry(m.id, 9, 'attackMonsterHasted',
                                           name=m.name)
                        check_visibility = 1
                        check_shields = 1
                    elif phase_type == 3:
                        self.add_log_entry(m.id, 9, 'attackMonsterTimestopped',
                                           name=m.name)
                        check_visibility = 0
                        check_shields = 0
                    check_mindspells = 1
                    if m.attack_id > 0:
                        self.attack_action(
                            m, target, check_mindspells, check_visibility, check_shields)
                    else:
                        self.add_log_entry(m.id, 10, 'attackMissesNobody',
                                           name=m.name)

    def process_match_start(self):
        ''' Start the match. Initiate turn counter and log match start actions for all participants.
        '''

        current_turn = 0
        self.set_current_turn(current_turn)
        valid_participant_ids = self.get_list_of_participants_ids_active_this_turn()

        self.add_log_entry(0, 1, 'turnNum', name=self.current_turn)
        for participant_id in valid_participant_ids:
            p = self.get_participant_by_id(participant_id)
            self.add_log_entry(0, 1, 'actorBows', name=p.name)
        self.print_log_entries_by_turn(self.current_turn)

    def process_turn_phase_0(self, match_orders, match_spellbook):
        ''' Process turn phase 0 - initiation.

        Arguments:
        match_orders -- object, an instance of Spellbook-inherited Orders
        match_spellbook -- object, an instance of Spellbook-inherited SpellBook
        '''

        # Check if the match is still going
        if self.get_match_status():
            return -1  # match finished

        # Increase the turn counter and determine the turn type (normal, hasted, timestoppes)
        self.set_current_turn(self.current_turn + 1)
        self.set_current_turn_type()

        # Request orders for all participants active during this turn
        match_orders.get_turn_orders(self, match_spellbook)
        # Check if some orders are missing and stop processing the turn if some are
        missing_orders = match_orders.check_missing_orders(self)
        if missing_orders:
            return 0  # not processed - missing orders

        # Log new turn start
        self.add_log_entry(0, 1, 'turnNum', name=self.current_turn)
        return 1

    def process_turn_phase_1(self, match_orders, match_spellbook):
        ''' Process turn phase 1 - spellcasting.

        Arguments:
        match_orders -- object, an instance of Spellbook-inherited Orders
        match_spellbook -- object, an instance of Spellbook-inherited SpellBook
        '''

        # Step 1.0 - clear stack
        match_spellbook.clear_stack()

        # Step 1.1 - determine gestures for the turn
        match_spellbook.determine_gestures(match_orders, self)

        # Step 1.2 - print effects and gestures for the turn
        match_spellbook.log_effects_sot(match_orders, self)
        match_spellbook.log_gesture_messages(self)

        # Step 1.3 - make a list of spells that match gestures for all participants
        match_spellbook.match_spell_pattern(self)

        # Step 1.4 - select spells to cast (and their targets) for all participants
        match_spellbook.select_spells_for_stack(match_orders, self)

        # Step 1.5 - cast delayed spells, if any and if ordered, for all participants
        match_spellbook.check_delayed_spell_cast(match_orders, self)

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

        return 1

    def process_turn_phase_2(self, match_orders):
        ''' Process turn phase 2 - combat.

        Arguments:
        match_orders -- object, an instance of Spellbook-inherited Orders
        '''

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

        return 1

    def process_turn_phase_3(self, match_orders):
        ''' Process turn phase 3 - clean-up.

        Arguments:
        match_orders -- object, an instance of Spellbook-inherited Orders
        '''

        # Step 3.1 - remove monsters killed in combat or by slow spells
        self.kill_monsters_eot()

        # Step 3.2 - check spell effects that occur EOT
        self.check_sickness_statuses()
        self.check_antispell_statuses()

        # Step 3.3 - remove players killed in combat or by spells
        self.kill_participants_eot()

        # Step 3.4 - check for game over
        self.check_match_end_eot()
        if self.get_match_status():
            return -1  # match finished

        # Step 3.2 - check surrender and suicide
        self.kill_surrendered_participants(self.current_turn)
        self.kill_suicided_participants(match_orders)

        # Step 3.3 - check for game over again, after surrenders
        self.check_match_end_eot()
        if self.get_match_status():
            return -1  # match finished

        # Step 3.4 - update effects on monsters
        self.update_statuses_on_monsters_eot()

        # Step 3.5 - update effects on participants
        self.update_statuses_on_participants_eot()

        self.print_log_entries_by_turn(self.current_turn)

        self.print_match_actors_status()

        return 1
