from typing import Final
from ruleset_core.class_orders import Order, Orders


class WarlocksOrder(Order):
    """Order class for Warlocks.

    Contains all possible / accepted types of orders from a participant for a turn.
    """

    def __init__(self) -> None:
        """Init Warlocks Orders."""
        super().__init__()

        """Init Spellbook-specific Orders."""
        # Hand ID(s) to be paralyzed
        self.paralyze_orders: dict[int, int] = {}
        # Hand ID(s) to be charmed, and respective gestures
        self.charm_orders: dict[int, tuple[int, str]] = {}
        # Special order - store spell - hand ID
        self.delay_spell = 0
        # Special order - fire stored spell
        self.cast_delayed_spell = False
        # Special order - make spell permanent - hand ID
        self.make_spell_permanent = 0
        # Special order - commit suicide (if affected by perm mindspell)
        self.commit_suicide = False


class WarlocksOrders(Orders):
    """Orders class for Warlocks.

    Contains a list of orders and methods that parse them.
    """

    ORDER_INVALID_MATCH_ID: Final[int] = 1
    ORDER_INVALID_TURN_NUM: Final[int] = 2
    ORDER_INVALID_PARTICIPANT_ID: Final[int] = 3

    def __init__(self) -> None:
        """Init WarlocksOrders."""
        super().__init__()
        self.orders: list[WarlocksOrder] = []

    def get_turn_orders(self, match_id: int, current_turn: int, hand_id_offset: int,
                        valid_participant_ids: list[int], valid_gestures: list[str], 
                        valid_spell_ids: list[int]) -> None:
        """Get and validate orders for the turn.

        Arguments:
            match_id (int): match ID
            current_turn (int): turn number
            hand_id_offset (int): offset to calculate hand IDs (set to 10 for Warlocks)
            valid_participant_ids (list): list of participant IDs (int)
            valid_gestures (list): gestures (str(1)) that are valid for selected SpellBook
            valid_spell_ids (list): spell IDs (integer) that are valid for selected SpellBook
        """
        data = self.load_orders_from_file()
        for key in data:
            validation_error_codes = self.validate_json_order(data[key],
                                                              match_id,
                                                              current_turn,
                                                              valid_participant_ids)
            if not validation_error_codes:
                new_order = self.parse_json_order(data[key],
                                                  hand_id_offset,
                                                  valid_gestures,
                                                  valid_spell_ids)
                self.orders.append(new_order)

    def check_missing_orders(self, match_data: 'WarlocksMatchData') -> list[int]:
        """Check for missing orders for the turn using submitted active participants list.

        Arguments:
            match_data (object): WarlocksMatchData instance, match data

        Returns:
            List: IDs of participants that have not submitted their orders.
        """
        valid_participant_ids = match_data.get_ids_participants_active()
        missing_orders = []
        for p in valid_participant_ids:
            order = self.search_orders(
                match_data.match_id, match_data.current_turn, p)
            if order is None:
                missing_orders.append(p)
        return missing_orders

    def search_orders(self, match_id: int, turn_num: int, participant_id: int) -> WarlocksOrder | None:
        """Search for Order for the specific match - turn - participant.

        Arguments:
            match_id (int): match ID
            turn_num (int): turn number
            participant_id (int): ID of participant

        Returns:
            Object: WarlocksOrder instance if found, None otherwise
        """
        for order in self.orders:
            if ((order.match_id == match_id)
                    and (order.turn_num == turn_num)
                    and (order.participant_id == participant_id)):
                return order
        return None

    def validate_json_order(self, data: dict, match_id: int, turn_num: int, 
                            valid_participant_ids: list[int]) -> list[int]:
        """Validate incoming orders.

        Arguments:
            data (dict): JSON data
            match_id (int): match ID
            turn_num (int): turn number
            valid_participant_ids (list): IDs of participants that are expected to act this turn

        Returns:
            validation_error_codes: list of ints (error codes)
        """
        validation_error_codes = []

        if ('matchID' not in data) or (not isinstance(data['matchID'], int)) or (data['matchID'] != match_id):
            # missing or invalid matchID
            validation_error_codes.append(self.ORDER_INVALID_MATCH_ID)
        if ('turnNum' not in data) or (not isinstance(data['turnNum'], int)) or (data['turnNum'] != turn_num):
            # missing or invalid turnNum
            validation_error_codes.append(self.ORDER_INVALID_TURN_NUM)
        if ('participantID' not in data) or (not isinstance(data['participantID'], int)) or (data['participantID'] not in valid_participant_ids):
            # missing or invalid participantID
            validation_error_codes.append(self.ORDER_INVALID_PARTICIPANT_ID)

        return validation_error_codes

    def parse_json_order(self, data: dict, hand_id_offset: int, valid_gestures: list[str], 
                            valid_spell_ids: list[int]) -> WarlocksOrder:
        """Parse JSON order.

        Arguments:
            data (dict): JSON data
            hand_id_offset (int): offset to calculate hand IDs (set to 10 for Warlocks)
            valid_gestures (list): gestures (str(1)) that are valid for selected SpellBook
            valid_spell_ids (list): spell IDs (integer) that are valid for selected SpellBook

        Returns:
            new_order: an instance of WarlocksOrder
        """
        default_gesture = '-'
        default_spell_id = -1
        default_target_id = -1

        # create order instance
        new_order = WarlocksOrder()
        new_order.match_id = data['matchID']
        new_order.turn_num = data['turnNum']
        new_order.participant_id = data['participantID']

        # Get and validate LH and RH gestures
        if ('gestureLH' not in data) or (data['gestureLH'] == '') or (data['gestureLH'][0] not in valid_gestures):
            new_order.gesture_lh = default_gesture
        else:
            new_order.gesture_lh = data['gestureLH'][0]
        if ('gestureRH' not in data) or (data['gestureRH'] == '') or (data['gestureRH'][0] not in valid_gestures):
            new_order.gesture_rh = default_gesture
        else:
            new_order.gesture_rh = data['gestureRH'][0]

        # Get and validate requested LH and RH spell IDs
        if ('orderSpellLH' not in data) or (not isinstance(data['orderSpellLH'], int)) or (data['orderSpellLH'] not in valid_spell_ids):
            new_order.order_spell_lh = default_spell_id
        else:
            new_order.order_spell_lh = data['orderSpellLH']
        if ('orderSpellRH' not in data) or (not isinstance(data['orderSpellRH'], int)) or (data['orderSpellRH'] not in valid_spell_ids):
            new_order.order_spell_rh = default_spell_id
        else:
            new_order.order_spell_rh = data['orderSpellRH']

        # Get and validate requested LH and RH targets
        if ('orderTargetLH' not in data) or (not isinstance(data['orderTargetLH'], int)):
            new_order.order_target_lh = default_target_id
        else:
            new_order.order_target_lh = data['orderTargetLH']
        if ('orderTargetRH' not in data) or (not isinstance(data['orderTargetRH'], int)):
            new_order.order_target_rh = default_target_id
        else:
            new_order.order_target_rh = data['orderTargetRH']

        # Get and validate special action - delay spell
        if ('delaySpell' not in data) or (not isinstance(data['delaySpell'], int)):
            new_order.delay_spell = 0
        else:
            new_order.delay_spell = data['delaySpell']

        # Get and validate special action - fire delayed spell
        if ('castDelayedSpell' not in data) or (not isinstance(data['castDelayedSpell'], int)) or (data['castDelayedSpell'] not in [1]):
            new_order.cast_delayed_spell = False
        else:
            new_order.cast_delayed_spell = True

        # Get and validate special action - make spell permanent
        if ('makeSpellPermanent' not in data) or (not isinstance(data['makeSpellPermanent'], int)):
            new_order.make_spell_permanent = 0
        else:
            new_order.make_spell_permanent = data['makeSpellPermanent']

        # Get and validate special action - commit suicide (if under a permanent mindspell)
        if ('commitSuicide' not in data) or (not isinstance(data['commitSuicide'], int)) or (data['commitSuicide'] not in [1]):
            new_order.commit_suicide = False
        else:
            new_order.commit_suicide = True

        # Get and validate orders for paralyze
        if ('paralyzeOrders' in data) and isinstance(data['paralyzeOrders'], dict):
            for i in data['paralyzeOrders']:
                if isinstance(i, str) and i.isdigit() and data['paralyzeOrders'][i] == 1:
                    new_order.paralyze_orders[int(
                        i) // hand_id_offset] = int(i)

        # Get and validate orders for charm person
        if ('charmOrders' in data) and isinstance(data['charmOrders'], dict):
            for i in data['charmOrders']:
                if isinstance(i, str) and i.isdigit() and data['charmOrders'][i] in valid_gestures:
                    new_order.charm_orders[int(
                        i) // hand_id_offset] = (int(i), data['charmOrders'][i])

        # Get and validate attack orders
        if ('attackOrders' in data) and isinstance(data['attackOrders'], dict):
            for i in data['attackOrders']:
                if isinstance(i, str) and i.isdigit() and isinstance(data['attackOrders'][i], int):
                    new_order.attack_orders[int(i)] = data['attackOrders'][i]

        return new_order
