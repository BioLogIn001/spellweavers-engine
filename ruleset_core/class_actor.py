from typing import Final


class Actor:
    """Base class for game actor (a participant or a monster).

    Contains data and functions common to
    both participants and monsters.
    """


    ACTOR_TYPE_PLAYER: Final[int] = 1
    ACTOR_TYPE_MONSTER: Final[int] = 2
    PLAYER_NO_HAND_ID: Final[int] = 0
    PLAYER_LEFT_HAND_ID: Final[int] = 1
    PLAYER_RIGHT_HAND_ID: Final[int] = 2

    def __init__(self, actor_type: int, hp: int, max_hp: int) -> None:
        """Init Actor."""
        self.id: int = -1
        self.type: int = actor_type  # { 1: 'Player', 2: 'Monster' }
        self.hp: int = hp
        self.max_hp: int = max_hp
        self.is_alive: bool = True
        self.gender: int = -1

    def set_actor_id(self, actor_id: int) -> None:
        """Set actor ID.

        Arguments:
            actor_id (int): ID of actor
        """
        self.id: int = actor_id

    def decrease_hp(self, diff: int) -> None:
        """Decrease actor's HP by diff amount.

        Arguments:
            diff (int): amount of HP to be subtracted.
        """
        self.hp -= diff

    def increase_hp(self, diff: int) -> None:
        """Increase actor's HP by diff amount, respecting max_hp.

        Arguments:
            diff (int): amount of HP to be added.
        """
        self.hp = min(self.hp + diff, self.max_hp)
