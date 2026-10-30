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
        self.id = actor_id

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


class Participant(Actor):
    """Contract for participants: what core MatchData relies on.

    Declares attributes and methods only.
    A ruleset's participant class sets the attributes in its own __init__
    (or, for hand IDs, in set_hands_ids) and implements the methods.
    """

    # User ID
    player_id: int
    # Username
    name: str
    # Team ID for the match
    team_id: int
    # Hand IDs, set by set_hands_ids()
    lh_id: int
    rh_id: int
    # Turn the participant was destroyed on, -1 while alive
    turn_destroyed: int
    # Flag to destroy the participant at the end of this turn
    destroy_eot: bool

    def set_hands_ids(self, offset: int) -> None:
        """Set IDs for participant's hands.

        Arguments:
            offset (int): offset for hand IDs (MatchData.DATA_HAND_ID_OFFSET, 10)
        """
        raise NotImplementedError

    def set_destroy_eot(self) -> None:
        """Set flag to destroy participant at the end of this turn."""
        raise NotImplementedError

class Monster(Actor):
    """Contract for monsters: what core MatchData relies on.

    Declares attributes and methods only.
    A ruleset's participant class sets the attributes in its own __init__
    (or, for hand IDs, in set_hands_ids) and implements the methods.
    """

    # Monster type
    monster_type: int
    # Controller (Player) ID
    controller_id: int
    # Attack target ID
    attack_id: int
    # ID of hand from which the monster was summoned
    summoner_hand_id: int
    # Turn num on which the monster was created
    turn_created: int
    # Turn num on which the monster was destroyed
    turn_destroyed: int
    # Flag to destroy the monster at the end of this turn
    destroy_eot: bool
    # Flag to destroy the monster before the attack
    destroy_before_attack: bool

    def set_destroy_eot(self) -> None:
        """Set flag to destroy monster at the end of this turn."""
        raise NotImplementedError

    def set_destroy_before_attack(self) -> None:
        """Set flag to destroy monster before attack."""
        raise NotImplementedError
