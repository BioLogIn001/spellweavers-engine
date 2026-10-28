from spellweavers.default.class_default_spellbook import DefaultSpellBook


class SpellbinderSpellBook(DefaultSpellBook):
    """Thin Spellbinder wrapper over Default SpellBook."""

    def __init__(self) -> None:
        """Init spellbook."""
        super().__init__()
        self.title = "Bartle's Spellbinder"
        self.spellbook_code = 'Spellbinder'
