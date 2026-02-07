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
        self.orders = []

    def set_filename(self, filename: str) -> None:
        """Set filename to import orders from. Placeholder.

        Arguments:
            filename (string): name of a JSON file with Orders
        """
        self.filename = filename

    def load_orders_from_file(self) -> str:
        """Load orders from JSON file (for console engine implementation).

        Returns:
            JSON data: data loaded from file
        """
        data = None
        with open(self.filename, 'r') as f:
            data = json.load(f)
        return data
