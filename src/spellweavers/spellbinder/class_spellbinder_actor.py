from spellweavers.default.class_default_actor import DefaultActor, DefaultMonster, DefaultParticipant


class SpellbinderActor(DefaultActor):
    """Thin Spellbinder wrapper over Default Actor."""


class SpellbinderParticipant(SpellbinderActor, DefaultParticipant):
    """Thin Spellbinder wrapper over Default Participant."""


class SpellbinderMonster(SpellbinderActor, DefaultMonster):
    """Thin Spellbinder wrapper over Default Monster."""
