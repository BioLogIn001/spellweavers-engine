import json


class Order:
    """Base order class.

    Contains core info about orders from a participant for a turn.
    """

    def __init__(self):
        """Init Orders."""
        # Order belongs to a specific match and a specific turn
        self.match_id = 0
        self.turn_num = 0
        # Order comes from a specific participant (to be improved in the web version)
        self.participant_id = 0

        # Str(1) - gestures for LH and RH
        self.gesture_lh = ''
        self.gesture_rh = ''
        # Integer spell IDs for LH and RH
        # Used to select a spell cast for overlapping patterns like WPP and P
        self.order_spell_lh = -1
        self.order_spell_rh = -1
        # Integer target IDs for LH and RH
        self.order_target_lh = -1
        self.order_target_rh = -1

        # Monster ID(s) and their respective targets
        self.attack_orders = {}


class Orders:
    """Base orders class.

    Contains a list of orders.
    """

    def __init__(self):
        """Init base orders."""
        self.filename = ''

    def set_filename(self, filename: str) -> None:
        """Set filename to import orders from. Placeholder.

        Arguments:
            filename (string): name of a JSON file with Orders
        """
        self.filename = filename

    def load_orders_from_file(self) -> dict:
        """Load orders from JSON file (for console engine implementation).

        Returns:
            dict: data loaded from JSON file
        """
        with open(self.filename, 'r') as f:
            return dict(json.load(f))

    def get_turn_orders(self, match_id: int, current_turn: int, hand_id_offset: int,
                        valid_participant_ids: list[int], valid_gestures: list[str], 
                        valid_spell_ids: list[int]) -> None:
        """Get and validate orders for the turn.

        Arguments:
            match_id (int): match ID
            current_turn (int): turn number
            hand_id_offset (int): offset to calculate hand IDs (set to 10 for Spellbinder)
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

    def validate_int(self, var: str | int, vrange: list[int]=[], strict: bool=False) -> int | None:
        """Validate int.

        Arguments:
            var (str | int): var to check
            vrange (list, optional): list of ints to check against
            strict (bool): bool flag to enforce type check

        Returns:
            int | None: validated int or None
        """        
        if isinstance(var, int):
            if vrange:
                if var in vrange:
                    return var
                else:
                    return None
            else:
                return var
        elif not strict and isinstance(var, str) and var.isdigit():
            if vrange:
                if int(var) in vrange:
                    return int(var)
                else:
                    return None
            else:
                return int(var)
        else:
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

        if ('matchID' not in data) or not self.validate_int(data['matchID'], [match_id], strict=False):
            # missing or invalid matchID
            validation_error_codes.append(self.ORDER_INVALID_MATCH_ID)
        if ('turnNum' not in data) or not self.validate_int(data['turnNum'], [turn_num], strict=False):
            # missing or invalid turnNum
            validation_error_codes.append(self.ORDER_INVALID_TURN_NUM)
        if ('participantID' not in data) or not self.validate_int(data['participantID'], valid_participant_ids, strict=False):
            # missing or invalid participantID
            validation_error_codes.append(self.ORDER_INVALID_PARTICIPANT_ID)

        return validation_error_codes