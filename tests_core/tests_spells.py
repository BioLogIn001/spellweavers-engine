import pytest

from spellweavers.tools_engine import import_name


@pytest.mark.parametrize('match_spellbook', [1, 2])
def test_spell_clone(available_spellbooks, match_spellbook):

    spellbook_code = available_spellbooks[match_spellbook]['code']
    lib_name = 'spellweavers.' + spellbook_code.lower() + '.'

    # Init spellbook
    spellbook = import_name(lib_name + 'class_' + spellbook_code.lower() + '_spellbook',
                            spellbook_code + 'SpellBook')()
    src = spellbook.spells[0]
    clone = src.clone(src.patterns[0])

    # (a) Completeness: clone carries every attribute (catches a dropped field)
    assert vars(clone).keys() == vars(src).keys()

    # (b) No shared mutable: clone shares no top-level list/dict/set with its source
    #     (catches silent aliasing, incl. a future hand-written `clone.x = self.x` slip)
    for name, val in vars(clone).items():
        if isinstance(val, (list, dict, set)):
            assert val is not getattr(src, name), f"clone aliases mutable '{name}'"

    # (c) Concrete contamination check: Delay Effect sets flags['delayed'] on the
    # cast clone; it must not leak back to the roster spell
    clone.flags['delayed'] = True
    assert src.flags['delayed'] is False
