import random
from class_matchdata import MatchData
from class_warlocks_actor import WarlocksParticipant, WarlocksMonster


class WarlocksMatchData(MatchData):
    """This class contains current match state, with some exceptions.
    - match_id and current_turn are obvious.
    - participantList and monster_list contain all match actors, alive and dead.
    - matchGestures contain history of gestures for all players all hands.
    - matchLog contain history of all events happened
    - textStings contains all warlocks text strings in the current loc
    """

    def __init__(self, match_id):
        """Init match data.
        
        Args:
            match_id (int): match ID
        """
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
            1: {'start_hp': 1, 'max_hp': 2, 'attack_damage': 1, 'attack_type': 'Physical', 'attacks_all': 0, 'initial_effects': {}},
            2: {'start_hp': 2, 'max_hp': 3, 'attack_damage': 2, 'attack_type': 'Physical', 'attacks_all': 0, 'initial_effects': {}},
            3: {'start_hp': 3, 'max_hp': 4, 'attack_damage': 3, 'attack_type': 'Physical', 'attacks_all': 0, 'initial_effects': {}},
            4: {'start_hp': 4, 'max_hp': 5, 'attack_damage': 4, 'attack_type': 'Physical', 'attacks_all': 0, 'initial_effects': {}},
            5: {'start_hp': 3, 'max_hp': 4, 'attack_damage': 3, 'attack_type': 'Fire', 'attacks_all': 1, 'initial_effects': {'ResistHeat': 9999}},
            6: {'start_hp': 3, 'max_hp': 4, 'attack_damage': 3, 'attack_type': 'Ice', 'attacks_all': 1, 'initial_effects': {'ResistCold': 9999}}
        }

    # INIT and ADD functions

    def create_participant(self, player_id, player_name, team_id):
        """Creates an instance of Participant-inherited class.
        
        Arguments:
            player_id (int): a user ID to link game profile to in-match participant ID
            player_name (string): player name to display
            team_id (int): participant's team ID for the match
        
        Returns:
            An instance of WarlocksParticipant class.
        """

        start_turn = 1
        new_participant = WarlocksParticipant(player_id, player_name, team_id, start_turn)
        return new_participant

    def create_monster(self, controller_id, monster_type,
                       summoner_id, summoner_hand_id, summon_turn,
                       gender):
        """Creates an instance of Monster-inherited class.
        
        Arguments:
            controller_id (int): ID of the participant that controls the monster
            monster_type (int): monster type
            summoner_id (int): ID of the participant that summoned the monster
            summoner_hand_id (int): ID of the hand that was used to summon monster
            summon_turn (int): the number of turn when the monster was summoned
            gender (int): gender for pronouns {0: they/them/their, 1: she/her/hers, 2: he/him/his}
        
        Returns:
            An instance of WarlocksMonster class.
        """

        new_monster = None
        if monster_type in self.monster_types:
            new_monster = WarlocksMonster(self.monster_types, controller_id, monster_type,
                                          summoner_id, summoner_hand_id, summon_turn,
                                          gender, self.current_turn)
        return new_monster

    # GET functions

    def get_new_monster_name(self, monster_type):
        """Request a new name from name repository.
        For elemental the name is always the same (Fire Elemental and Ice Elemental respectively).
        For Goblins, Ogres, Trolls and Giants we cycle through previously shuffled list;
        if we have exhaused the list, we start over adding 'Very ' in front of name;
        this can be repeated indefinitely (i.e. at some moment there might be 'Very Very Green Goblin').
        
        Arguments:
            monster_type (int): monster type
        
        Returns:
            string: monster name
        """

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
        """Counts the amount of already named (= already created) monsters of monster_type in this match.
        
        Arguments:
            monster_type (int): monster type
        
        Returns:
            int: monster count.
        """

        c = 0
        for m in self.monster_list:
            if m.monster_type == monster_type and m.name > '':
                c += 1
        return c

    def get_gesture_log_entry(self, gesture_lh, gesture_rh):
        """Get codes for localized strings for LH and RH gestures to use in log.
        
        Arguments:
            gesture_lh (str): gesture for left hand
            gesture_rh (str): gesture for right hand
        
        Returns:
            tuple: codes of localization text strings associated with gestures
        """

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

    def get_ids_participants_hasted(self):
        """Get list of participants that are affected by Haste this turn.
        
        Returns:
            list: interget IDs of participants
        """

        l = []
        for participant_id in self.get_ids_participants():
            p = self.get_participant_by_id(participant_id)
            if p.affected_by_haste(self.current_turn):
                l.append(participant_id)
        return l

    def get_ids_participants_timestopped(self):
        """Get list of participants that are affected by Timestop this turn.
        
        Returns:
            list: interget IDs of participants
        """

        l = []
        for participant_id in self.get_ids_participants():
            p = self.get_participant_by_id(participant_id)
            if p.affected_by_timestop(self.current_turn):
                l.append(participant_id)
        return l

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
        """Check if the current turn is Hasted
        
        Returns:
            bool: 1 if turn is Hasted, 0 otherwise
        """

        if self.current_turn_type == 2:
            return 1
        else:
            return 0

    def is_current_turn_timestopped(self):
        """Check if the current turn is Timestopped
        
        Returns:
            bool: 1 if turn is Timestopped, 0 otherwise
        """

        if self.current_turn_type == 3:
            return 1
        else:
            return 0

    # TURN LOGIC functions

    def set_current_turn_type(self):
        """Determine current turn type.
        {1: Normal; 2: Hasted; 3: Timestopped}
        """

        self.prev_turn_type = self.current_turn_type

        if self.get_ids_participants_timestopped():
            self.current_turn_type = 3  # timestopped
        elif self.get_ids_participants_hasted():
            if self.prev_turn_type == 2:
                self.current_turn_type = 1  # normal
            else:
                self.current_turn_type = 2  # hasted
        else:
            self.current_turn_type = 1  # normal

    def check_sickness_effects(self):
        """Check participants affected by Disease or Poison. 
        Those who reached effect value 1, die EOT.
        """

        for p in self.participant_list:
            if p.is_alive:
                if p.effects[self.current_turn]['Disease'] == 1:
                    self.add_log_entry(9, 'effectDiseaseFatal', actor_id=p.id)
                    #self.add_log_entry(p.id, 9, 'effectDiseaseFatal', name=p.name)
                    p.destroy_eot = 1

                if p.effects[self.current_turn]['Poison'] == 1:
                    self.add_log_entry(9, 'effectPoisonFatal', actor_id=p.id)
                    #self.add_log_entry(p.id, 9, 'effectPoisonFatal', name=p.name)
                    p.destroy_eot = 1

    def check_antispell_effects(self):
        """Check participants affected by Anti-Spell and update their last gestures with -/-
        We do this EOT, since we need to do stabs after spell casting, and other way around is even messy-er.
        """

        for p in self.participant_list:
            if p.is_alive:
                if p.effects[self.current_turn]['AntiSpell'] == 1:
                    self.set_gestures(p.id, self.current_turn, '-', '-')

    def kill_suicided_participants(self, match_orders):
        """Set is_alive to 0 for participants who were affectedd by perm mindspell and gave the suicide order.
        
        Arguments:
            match_orders (object): WarlocksOrders instance, orders for this turn
        """

        for participant_id in self.get_ids_participants():
            order = match_orders.search_orders(
                self.match_id, self.current_turn, participant_id)
            p = self.get_participant_by_id(participant_id)
            if (p.affected_by_permanent_mindspell(self.current_turn) 
                    and (order.commit_suicide == 1)):
                p.is_alive = 0
                self.add_log_entry(11, 'resultActorSuicides', actor_id=p.id)
                #self.add_log_entry(p.id, 11, 'resultActorSuicides', name=p.name)

    def kill_surrendered_participants(self, turn_num):
        """Set is_alive to 0 for participants who showed P/P
        
        Arguments:
            turn_num (int): turn number
        """

        for p in self.participant_list:
            if (p.is_alive
                    and self.get_gesture(p.id, turn_num, 1) == 'P'
                    and self.get_gesture(p.id, turn_num, 2) == 'P'):
                p.is_alive = 0
                self.add_log_entry(11, 'resultActorSurrenders', actor_id=p.id)
                #self.add_log_entry(p.id, 11, 'resultActorSurrenders', name=p.name)

    def update_effects_on_monsters_eot(self):
        """EOT tick down all effects on monsters.
        Skipped for timestopped turns.
        """

        for m in self.monster_list:
            if m.is_alive:
                for s in m.effects[self.current_turn]:
                    if not self.is_current_turn_timestopped():
                        m.decrease_effect(s, self.current_turn)
                #m.state_mindspells_this_turn = 0

            for s in m.effects[self.current_turn]:
                if m.effects[self.current_turn][s] > m.effects[self.current_turn + 1][s]:
                    m.effects[self.current_turn + 1][s] = m.effects[self.current_turn][s]
            m.init_effects_and_states(self.current_turn + 2)

    def update_effects_on_participants_eot(self):
        """EOT tick down all effects on participants.
        Skipped for turns that are followed by hasted or timestopped turns.
        """

        # Tmp determine next turn type
        next_turn_type = 1
        next_turn_haste_counter = 0
        next_turn_timestop_counter = 0
        for p in self.participant_list:
            if p.is_alive:
                if p.effects[self.current_turn + 1]['TimeStop'] > 0:
                    next_turn_timestop_counter += 1
                if self.current_turn_type == 1 and (p.effects[self.current_turn]['Haste'] > 0 
                                                    or p.effects[self.current_turn + 1]['Haste'] > 0):
                    next_turn_haste_counter += 1
        if next_turn_timestop_counter:
            next_turn_type = 3
        elif next_turn_haste_counter:
            next_turn_type = 2

        for p in self.participant_list:
            if p.is_alive:

                # Log the end of Blindness / Invisibility
                if p.effects[self.current_turn]['Blindness'] == 1:
                    self.add_log_entry(8, 'effectBlindness2', actor_id=p.id)
                if p.effects[self.current_turn]['Invisibility'] == 1:
                    self.add_log_entry(8, 'effectInvisibility2',actor_id=p.id)

                # Log the start of Blindness / Invisibility
                if p.effects[self.current_turn + 1]['Blindness'] in [3, 9999]:
                    self.add_log_entry(8, 'effectBlindness1', actor_id=p.id)
                if p.effects[self.current_turn + 1]['Invisibility'] in [3, 9999]:
                    self.add_log_entry(8, 'effectInvisibility1', actor_id=p.id)

                for s in p.effects[self.current_turn]:

                    # Decrease non-mindspell effects if next turn is normal.
                    # Decrease mindspell-effects if current turn is normal
                    decrease_this_effect = 0
                    if s in ['Fear', 'Maladroitness', 'Paralysis', 'Amnesia', 'CharmPerson']:
                        if self.current_turn_type == 1 and p.effects[self.current_turn][s] < self.permanent_duration:
                            #p.decrease_effect(s, self.current_turn)
                            decrease_this_effect = 1
                    else:
                        if next_turn_type == 1 and p.effects[self.current_turn][s] < self.permanent_duration:
                            #p.decrease_effect(s, self.current_turn)
                            decrease_this_effect = 1

                    # Is there are effects remaining this turn, pass them to the next turn
                    if p.effects[self.current_turn][s] - decrease_this_effect > p.effects[self.current_turn + 1][s]:
                        p.effects[self.current_turn + 1][s] = p.effects[self.current_turn][s] - decrease_this_effect
                    
                    # Create effects template for the turn after the next
                    p.init_effects_and_states(self.current_turn + 2)

                # If current turn is hasted, pass info about paralyzer to next turn so that paralyze would work
                if self.current_turn_type == 2 and p.states[self.current_turn]['paralyzed_by_id']:
                    caster = self.get_participant_by_id(p.states[self.current_turn]['paralyzed_by_id'])
                    if caster.affected_by_haste(self.current_turn) == 0:
                        p.states[self.current_turn + 1]['paralyzed_by_id'] = p.states[self.current_turn]['paralyzed_by_id']
                # If current turn is hasted, pass info about charmer to next turn so that paralyze would work
                if self.current_turn_type == 2 and p.states[self.current_turn]['charmed_by_id']:
                    caster = self.get_participant_by_id(p.states[self.current_turn]['charmed_by_id'])
                    if caster.affected_by_haste(self.current_turn) == 0:
                        p.states[self.current_turn + 1]['charmed_by_id'] = p.states[self.current_turn]['charmed_by_id']

                # If current turn is timestopped, pass info about paralyzer to next turn so that paralyze would work
                if self.current_turn_type == 3 and p.states[self.current_turn]['paralyzed_by_id']:
                    caster = self.get_participant_by_id(p.states[self.current_turn]['paralyzed_by_id'])
                    if caster.affected_by_timestop(self.current_turn) == 0:
                        p.states[self.current_turn + 1]['paralyzed_by_id'] = p.states[self.current_turn]['paralyzed_by_id']
                # If current turn is timestopped, pass info about charmer to next turn so that paralyze would work
                if self.current_turn_type == 3 and p.states[self.current_turn]['charmed_by_id']:
                    caster = self.get_participant_by_id(p.states[self.current_turn]['charmed_by_id'])
                    if caster.affected_by_timestop(self.current_turn) == 0:
                        p.states[self.current_turn + 1]['charmed_by_id'] = p.states[self.current_turn]['charmed_by_id']

                # If next turn is hasted or timestopped, preserve mindspell counter to allow clashes
                if next_turn_type in [2,3]:
                    p.states[self.current_turn + 1]['mindspells_this_turn'] = p.states[self.current_turn]['mindspells_this_turn']

    def attack_action(self, a, d, check_mindspells=1, check_visibility=1, check_shields=1):
        """Resolve a single attack action.
        
        Args:
            a (object): WarlocksParticipant or WarlocksMonster instance, attacker
            d (object): WarlocksParticipant or WarlocksMonster instance, defender
            check_mindspells (bool, optional): flag to check minsdpell effects that prevent attack
            check_visibility (bool, optional): flag to check visibility (Blindness, Invis)
            check_shields (bool, optional): flag to chech shields (PShield, Protection, Resists)
        """

        # If we check shields and other effects that prevent attacks,
        # we check for mindspells on attacker, but only for monsters
        if check_mindspells == 1 and a.type == 2 and a.affected_by_paralysis(self.current_turn):
            self.add_log_entry(8, 'effectParalysis2', actor_id=a.id)
            return
        if check_mindspells == 1 and a.type == 2 and a.affected_by_amnesia(self.current_turn):
            self.add_log_entry(8, 'effectAmnesia2', actor_id=a.id)
            return
        if check_mindspells == 1 and a.type == 2 and a.affected_by_fear(self.current_turn):
            self.add_log_entry(8, 'effectFear2', actor_id=a.id)
            return
        if check_mindspells == 1 and a.type == 2 and a.affected_by_maladroitness(self.current_turn):
            self.add_log_entry(8, 'effectMaladroitness2', actor_id=a.id)
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
        if a.attack_type == 'Fire':
            if check_shields == 1 and d.affected_by_resist_heat_permanent(self.current_turn):
                self.add_log_entry(7, 'effectResistHeat', actor_id=a.id, attack_id=d.id)
            elif check_shields == 1 and d.affected_by_pshield(self.current_turn):
                self.add_log_entry(10, 'effectShieldFromElemental', actor_id=a.id, attack_id=d.id)
            else:
                d.decrease_hp(a.attack_damage)
                self.add_log_entry(9, 'damagedByFireElem', actor_id=a.id, attack_id=d.id, damage_amount=a.attack_damage)
        # a = Ice elem
        elif a.attack_type == 'Ice':
            if check_shields == 1 and d.affected_by_resist_cold_permanent(self.current_turn):
                self.add_log_entry(7, 'effectResistCold', actor_id=a.id, attack_id=d.id)
            elif check_shields == 1 and d.affected_by_pshield(self.current_turn):
                self.add_log_entry(10, 'effectShieldFromElemental', actor_id=a.id, attack_id=d.id)
            else:
                d.decrease_hp(a.attack_damage)
                self.add_log_entry(9, 'damagedByIceElem', actor_id=a.id, attack_id=d.id, damage_amount=a.attack_damage)
        # a = monster or stabbing participant
        elif a.attack_type == 'Physical':
            # if a is a timestopped monster, then it deals damage anyways
            # if a is a timestopped participant, then we should check d.affected_by_pshield(1, 0) - shield but not protection
            # if a is a regular participant, then we should check d.affected_by_pshield(1, 1) or simply d.affected_by_pshield()
            if (check_shields == 0 and a.type == 2
                or check_shields == 0 and a.type == 1 and d.affected_by_pshield(1, 0, self.current_turn) == 0
                    or d.affected_by_pshield(self.current_turn) == 0):
                d.decrease_hp(a.attack_damage)
                self.add_log_entry(9, 'damagedByMonster', actor_id=a.id, attack_id=d.id, damage_amount=a.attack_damage)
            else:
                self.add_log_entry(10, 'effectShieldFromMonster', actor_id=a.id, attack_id=d.id)

    def check_stabs(self, match_orders):
        """Check for stab orders and resolve them.
        
        Arguments:
            match_orders (object): WarlocksOrders instance, match orders
        """

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
                        self.add_log_entry(10, 'stabMissesNobody', actor_id=p.id)

    def attack_phase(self, phase_type):
        """Process attack phase of a normal turn (and skip phase for hasted and timestopped turns).
        Note the difference. On timestopped or hasted turns (turns when there are 
        timestopped or hasted participants); on such turns there is no attack phase at all.
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
                if m.attacks_all:

                    check_visibility = 0
                    if phase_type == 1:
                        if m.monster_type == 5:
                            self.add_log_entry(9, 'attackFireElem', actor_id=m.id)
                        elif m.monster_type == 6:
                            self.add_log_entry(9, 'attackIceElem', actor_id=m.id)
                        check_shields = 1
                    elif phase_type == 2:
                        if m.monster_type == 5:
                            self.add_log_entry(9, 'attackFireElemHasted', actor_id=m.id)
                        elif m.monster_type == 6:
                            self.add_log_entry(9, 'attackIceElemHasted', actor_id=m.id)
                        check_shields = 1
                    elif phase_type == 3:
                        if m.monster_type == 5:
                            self.add_log_entry(9, 'attackFireElemTimestopped', actor_id=m.id)
                        elif m.monster_type == 6:
                            self.add_log_entry(9, 'attackIceElemTimestopped', actor_id=m.id)
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
                        self.add_log_entry(9, 'attackMonsterHasted', actor_id=m.id)
                        check_visibility = 1
                        check_shields = 1
                    elif phase_type == 3:
                        self.add_log_entry(9, 'attackMonsterTimestopped', actor_id=m.id)
                        check_visibility = 0
                        check_shields = 0
                    check_mindspells = 1
                    if m.attack_id > 0:
                        self.attack_action(
                            m, target, check_mindspells, check_visibility, check_shields)
                    else:
                        self.add_log_entry(10, 'attackMissesNobody', actor_id=m.id)

    def process_match_start(self):
        """Start the match. Initiate turn counter and log match start actions for all participants.
        """

        current_turn = 0
        self.set_current_turn(current_turn)
        valid_participant_ids = self.get_ids_participants_active()

        self.add_log_entry(1, 'turnNum', tmpstr=self.current_turn)
        for participant_id in valid_participant_ids:
            p = self.get_participant_by_id(participant_id)
            self.add_log_entry(1, 'actorBows', actor_id=p.id)
        pov_id = 0
        self.print_log_entries_by_turn(self.current_turn, pov_id)

    def process_turn_phase_startup(self, match_orders, match_spellbook):
        """Process turn phase 0 - initiation.
        
        Arguments:
            match_orders (object): WarlocksOrders instance, match orders
            match_spellbook (object): WarlocksSpellBook instance, match spellbook
        
        Returns:
            int: phase completion status; 1: success, 0: not enough orders, -1: match already finished
        """

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
        self.add_log_entry(1, 'turnNum', tmpstr=self.current_turn)
        return 1

    def process_turn_phase_cast(self, match_orders, match_spellbook, pov_id):
        """Process turn phase 1 - spellcasting.
        
        Arguments:
            match_orders (object): WarlocksOrders instance, match orders
            match_spellbook (object): WarlocksSpellBook instance, match spellbook
            pov_id (int): ID of participant to output for
        
        Returns:
            int: phase completion status; 1: success
        """

        # Step 1.0 - clear stack
        match_spellbook.clear_stack()

        # Step 1.1 - determine gestures for the turn
        match_spellbook.determine_gestures(match_orders, self)

        # Step 1.2 - log effects and gestures for the turn
        match_spellbook.log_effects_bot(match_orders, self)
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

    def process_turn_phase_attack(self, match_orders):
        """Process turn phase 2 - combat.
        
        Arguments:
            match_orders (object): WarlocksOrders instance, match orders
        
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

        return 1

    def process_turn_phase_cleanup(self, match_orders, pov_id):
        """Process turn phase 3 - clean-up.
        
        Arguments:
            match_orders (object): WarlocksOrders instance, match orders
            pov_id (int): ID of participant to output for
        
        Returns:
            int: phase completion status; 1: success, -1: match already finished
        """

        # Step 3.1 - remove monsters killed in combat or by slow spells
        self.kill_monsters_eot()

        # Step 3.2 - check spell effects that occur EOT
        self.check_sickness_effects()
        self.check_antispell_effects()

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
        self.update_effects_on_monsters_eot()

        # Step 3.5 - update effects on participants
        self.update_effects_on_participants_eot()

        self.print_log_entries_by_turn(self.current_turn, pov_id)
        self.print_match_actors_status(pov_id)

        print('')

        return 1
