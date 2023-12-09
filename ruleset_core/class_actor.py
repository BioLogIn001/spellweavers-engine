class Actor:
    """Base class for game actor (a participant or a monster).

    Contains data and functions common to
    both participants and monsters.
    """

    def __init__(self, actor_type, hp, max_hp):
        """Init Actor."""
        self.type = actor_type  # { 1: 'Player', 2: 'Monster' }
        self.hp = hp
        self.max_hp = max_hp
        self.is_alive = 1
        self.gender = -1

    def set_actor_id(self, actor_id):
        """Set actor ID.

        Arguments:
            actor_id (int): ID of actor
        """
        self.id = actor_id

    def decrease_hp(self, diff):
        """Decrease actor's HP by diff amount.

        Arguments:
            diff (int): amount of HP to be substracted.
        """
        self.hp -= diff

    def increase_hp(self, diff):
        """Increase actor's HP by diff amount, respecting max_hp.

        Arguments:
            diff (int): amount of HP to be added.
        """
        self.hp += diff
        if self.hp > self.max_hp:
            self.hp = self.max_hp
