import json


class WarlocksOrder:
    ''' Order class for Warlocks.
    Contains all possible / accepted types of orders from a participant for a turn.
    '''

    def __init__(self):

        # Order belongs to a specific match and a specific turn
        self.match_id = 0,
        self.turn_num = 0,
        # Order comes from a specific participant (to be improved in the web version)
        self.participant_id = 0,

        # Str(1) - gestures for LH and RH
        self.gesture_lh = '',
        self.gesture_rh = '',
        # Integer spell IDs for LH and RH
        # Used to select a spell cast for overlapping patterns like WPP and P
        self.order_spell_lh = -1,
        self.order_spell_rh = -1,
        # Integer target IDs for LH and RH
        self.order_target_lh = -1,
        self.order_target_rh = -1,

        # Hand ID(s) to be paralyzed
        self.paralyze_orders = {}
        # Hand ID(s) to be charmed, and respective gestures
        self.charm_orders = {}

        # Monster ID(s) and their respective targets
        self.attack_orders = {}

        # Special order - store spell
        self.delay_spell = 0,
        # Special order - fire stored spell
        self.cast_delayed_spell = 0,
        # Special order - make spell permanent
        self.make_spell_permanent = 0,
        # Special order - commit suicide (if affected by perm mindspell)
        self.commit_suicide = 0,


class WarlocksOrders:
    ''' Orders class for Warlocks.
    Contains a list of orders and methods that parse them.
    '''

    def __init__(self):

        self.orders = []

    def set_filename(self, filename):
        ''' Set filename to import orders from. Placeholder.

        Arguments:
        filename -- string, name of a JSON file with Orders
        '''

        self.filename = filename

    def load_orders_from_file(self):
        ''' Placeholder orders load from JSON file for console engine implementation
        '''

        data = None
        with open(self.filename, 'r') as f:
            data = json.load(f)
        return data

    def get_turn_orders(self, match_data, match_spellbook):
        ''' Get and validate orders for the turn

        Arguments:
        match_data -- object, MatchData-inherited
        match_spellbook -- object, SpellBook-inherited
        '''

        valid_participant_ids = match_data.get_ids_participants_active()

        data = self.load_orders_from_file()
        self.validate_orders(data, match_data.match_id, match_data.current_turn,
                             match_data.hand_id_offset, valid_participant_ids,
                             match_spellbook.valid_gestures, match_spellbook.valid_spell_ids)

    def check_missing_orders(self, match_data):
        ''' Check for missing orders for the turn using submitted active participants list.

        Arguments:
        match_data -- object, MatchData-inherited

        Returns:
        A list of IDs of participants that have not submitted their orders yet.
        '''

        valid_participant_ids = match_data.get_ids_participants_active()
        missing_orders = []
        for p in valid_participant_ids:
            order = self.search_orders(
                match_data.match_id, match_data.current_turn, p)
            if order is not None:
                pass
            else:
                missing_orders.append(p)
        return missing_orders

    def search_orders(self, match_id, turn_num, participant_id):
        ''' Search for Orders for the specific match - turn - participant.

        Arguments:
        match_id -- integer, match ID
        turn_num -- integer, turn number
        participant_id -- integer, ID of participant

        Returns:
        Order object if found, None otherwise
        '''

        for order in self.orders:
            if ((order.match_id == match_id)
                    and (order.turn_num == turn_num)
                    and (order.participant_id == participant_id)):
                return order
        return None

    def validate_orders(self, data, match_id, turn_num, hand_offset,
                        valid_participant_ids, valid_gestures, valid_spell_ids):
        ''' Validate incoming orders.

        data -- string, raw JSON data
        match_id -- integer, match ID
        turn_num -- integer, turn number
        hand_offset -- integer, offset to calculate hand IDs
        valid_participant_ids -- a list of integer IDs of participants that are expected to act this turn
        valid_gestures -- a list of gestures (str(1)) that are valid for selected SpellBook
        valid_spell_ids -- a list of spell IDs (integer) that are valid for selected SpellBook
        '''

        for o in data:

            # Determine match ID, turn number, and participant ID from Orders
            # and check them against current match - turn - participants.
            if ('matchID' not in data[o]):
                continue
            else:
                match_id_t = int(data[o]['matchID'])
            if ('turnNum' not in data[o]):
                continue
            else:
                turn_num_t = int(data[o]['turnNum'])
            if ('participantID' not in data[o]):
                continue
            else:
                participant_id_t = int(data[o]['participantID'])

            if ((match_id_t != match_id) or (turn_num_t != turn_num)
                    or (participant_id_t not in valid_participant_ids)):
                continue

            # If we expect an order from this participant on this turn of this match
            # create order instance
            new_order = WarlocksOrder()
            new_order.match_id = match_id_t
            new_order.turn_num = turn_num_t
            new_order.participant_id = participant_id_t

            # Get and validate LH and RH gestures
            if ('gestureLH' not in data[o]) or (data[o]['gestureLH'][0] not in valid_gestures):
                new_order.gesture_lh = '-'
            else:
                new_order.gesture_lh = data[o]['gestureLH'][0]
            if ('gestureRH' not in data[o]) or (data[o]['gestureRH'][0] not in valid_gestures):
                new_order.gesture_rh = '-'
            else:
                new_order.gesture_rh = data[o]['gestureRH'][0]

            # Get and validate requested LH and RH spell IDs
            if ('orderSpellLH' not in data[o]) or (int(data[o]['orderSpellLH']) not in valid_spell_ids):
                new_order.order_spell_lh = -1
            else:
                new_order.order_spell_lh = int(data[o]['orderSpellRH'])
            if ('orderSpellRH' not in data[o]) or (int(data[o]['orderSpellRH']) not in valid_spell_ids):
                new_order.order_spell_rh = -1
            else:
                new_order.order_spell_rh = int(data[o]['orderSpellRH'])

            # Get and validate requested LH and RH targets
            if ('orderTargetLH' not in data[o]):
                new_order.order_target_lh = -1
            else:
                new_order.order_target_lh = int(data[o]['orderTargetLH'])
            if ('orderTargetRH' not in data[o]):
                new_order.order_target_rh = -1
            else:
                new_order.order_target_rh = int(data[o]['orderTargetRH'])

            # Get and validate special action - delay spell
            if ('delaySpell' not in data[o]):
                new_order.delay_spell = 0
            else:
                new_order.delay_spell = int(data[o]['delaySpell'])

            # Get and validate special action - fire delayed spell
            if ('castDelayedSpell' not in data[o]) or (int(data[o]['castDelayedSpell']) not in [1]):
                new_order.cast_delayed_spell = 0
            else:
                new_order.cast_delayed_spell = int(data[o]['castDelayedSpell'])

            # Get and validate special action - make spell permanent
            if ('makeSpellPermanent' not in data[o]):
                new_order.make_spell_permanent = 0
            else:
                new_order.make_spell_permanent = int(
                    data[o]['makeSpellPermanent'])

            # Get and validate special action - commit suicide (if under a permanent mindspell)
            if ('commitSuicide' not in data[o]) or (int(data[o]['commitSuicide']) not in [1]):
                new_order.commit_suicide = 0
            else:
                new_order.commit_suicide = int(data[o]['commitSuicide'])

            # Get and validate orders for paralyze
            if ('paralyzeOrders' in data[o]):
                for i in data[o]['paralyzeOrders']:
                    if data[o]['paralyzeOrders'][i] is not None:
                        # int(data[o]['paralyzeOrders'][i])
                        new_order.paralyze_orders[int(
                            i) // hand_offset] = int(i)

            # Get and validate orders for charm person
            if ('charmOrders' in data[o]):
                for i in data[o]['charmOrders']:
                    if data[o]['charmOrders'][i] is not None:
                        new_order.charm_orders[int(
                            i) // hand_offset] = (int(i), data[o]['charmOrders'][i])

            # Get and validate attack orders
            if ('attackOrders' in data[o]):
                for i in data[o]['attackOrders']:
                    if data[o]['attackOrders'][i] is not None:
                        new_order.attack_orders[int(i)] = int(
                            data[o]['attackOrders'][i])

            self.orders.append(new_order)
