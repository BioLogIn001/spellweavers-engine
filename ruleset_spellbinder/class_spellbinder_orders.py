from typing import Final
from ruleset_core.class_orders import Order, Orders


class SpellbinderOrder(Order):
    """Order class for Spellbinder.

    Contains all possible / accepted types of orders from a participant for a turn.
    """

    def __init__(self) -> None:
        """Init Spellbinder Orders."""
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


class SpellbinderOrders(Orders):
    """Orders class for Spellbinder.

    Contains a list of orders and methods that parse them.
    """

    ORDER_INVALID_MATCH_ID: Final[int] = 1
    ORDER_INVALID_TURN_NUM: Final[int] = 2
    ORDER_INVALID_PARTICIPANT_ID: Final[int] = 3

    def __init__(self) -> None:
        """Init SpellbinderOrders."""
        super().__init__()
        self.orders: list[SpellbinderOrder] = []

    def check_missing_orders(self, match_data: 'SpellbinderMatchData') -> list[int]:
        """Check for missing orders for the turn using submitted active participants list.

        Arguments:
            match_data (object): SpellbinderMatchData instance, match data

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

    def search_orders(self, match_id: int, turn_num: int, participant_id: int) -> SpellbinderOrder | None:
        """Search for Order for the specific match - turn - participant.

        Arguments:
            match_id (int): match ID
            turn_num (int): turn number
            participant_id (int): ID of participant

        Returns:
            Object: SpellbinderOrder instance if found, None otherwise
        """
        for order in self.orders:
            if ((order.match_id == match_id)
                    and (order.turn_num == turn_num)
                    and (order.participant_id == participant_id)):
                return order
        return None

    def parse_json_order(self, data: dict, hand_id_offset: int, valid_gestures: list[str], 
                            valid_spell_ids: list[int]) -> SpellbinderOrder:
        """Parse JSON order.

        Arguments:
            data (dict): JSON data
            hand_id_offset (int): offset to calculate hand IDs (set to 10 for Spellbinder)
            valid_gestures (list): gestures (str(1)) that are valid for selected SpellBook
            valid_spell_ids (list): spell IDs (integer) that are valid for selected SpellBook
        """
        default_gesture = '-'
        default_spell_id = -1
        default_target_id = -1
        strict_type_check = False

        # create order instance
        new_order = SpellbinderOrder()
        new_order.match_id = int(data['matchID'])
        new_order.turn_num = int(data['turnNum'])
        new_order.participant_id = int(data['participantID'])

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
        tmp = None
        if ('orderSpellLH' in data): 
            tmp = self.validate_int(data['orderSpellLH'], valid_spell_ids, strict=strict_type_check)
        if tmp is None:
            new_order.order_spell_lh = default_spell_id
        else:
            new_order.order_spell_lh = tmp
        tmp = None
        if ('orderSpellRH' in data): 
            tmp = self.validate_int(data['orderSpellRH'], valid_spell_ids, strict=strict_type_check)
        if tmp is None:
            new_order.order_spell_rh = default_spell_id
        else:
            new_order.order_spell_rh = tmp

        # Get and validate requested LH and RH targets
        tmp = None
        if ('orderTargetLH' in data): 
            tmp = self.validate_int(data['orderTargetLH'], strict=strict_type_check)
        if tmp is None:
            new_order.order_target_lh = default_target_id
        else:
            new_order.order_target_lh = tmp
        tmp = None
        if ('orderTargetRH' in data): 
            tmp = self.validate_int(data['orderTargetRH'], strict=strict_type_check)
        if tmp is None:
            new_order.order_target_rh = default_target_id
        else:
            new_order.order_target_rh = tmp

        # Get and validate special action - delay spell
        tmp = None
        if ('delaySpell' in data): 
            tmp = self.validate_int(data['delaySpell'], strict=strict_type_check)
        if tmp is None:
            new_order.delay_spell = 0
        else:
            new_order.delay_spell = tmp

        # Get and validate special action - fire delayed spell
        tmp = None
        if ('castDelayedSpell' in data): 
            tmp = self.validate_int(data['castDelayedSpell'], [1], strict=strict_type_check)
        if tmp is None:
            new_order.cast_delayed_spell = False
        else:
            new_order.cast_delayed_spell = True

        # Get and validate special action - make spell permanent
        tmp = None
        if ('makeSpellPermanent' in data): 
            tmp = self.validate_int(data['makeSpellPermanent'], strict=strict_type_check)
        if tmp is None:
            new_order.make_spell_permanent = 0
        else:
            new_order.make_spell_permanent = tmp

        # Get and validate special action - commit suicide (if under a permanent mindspell)
        tmp = None
        if ('commitSuicide' in data): 
            tmp = self.validate_int(data['commitSuicide'], [1], strict=strict_type_check)
        if tmp is None:
            new_order.commit_suicide = False
        else:
            new_order.commit_suicide = True

        # Get and validate orders for paralyze
        if ('paralyzeOrders' in data) and isinstance(data['paralyzeOrders'], dict):
            for i in data['paralyzeOrders']:
                if isinstance(i, str) and i.isdigit() and data['paralyzeOrders'][i] == 1:
                    new_order.paralyze_orders[int(i) // hand_id_offset] = int(i)

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
