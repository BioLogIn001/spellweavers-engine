from spellweavers.default.class_default_matchdata import DefaultMatchData
from spellweavers.spellbinder.class_spellbinder_actor import SpellbinderMonster, SpellbinderParticipant


class SpellbinderMatchData(DefaultMatchData):
    """Thin Spellbinder wrapper over Default MatchData."""

    participant_class = SpellbinderParticipant
    monster_class = SpellbinderMonster
