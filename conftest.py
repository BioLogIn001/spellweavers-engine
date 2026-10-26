import pytest
from tests_core.players_init import PLAYERS_2

@pytest.fixture
def available_spellbooks():
    return {
        1: {'code': 'Warlocks', 'title': "RavenBlack's Warlocks - ParaFC Maladroit"},
        2: {'code': 'Spellbinder', 'title': "Bartle's Spellbinder - Original Ruleset"},
        3: {'code': 'TBD', 'title': "TBD"},
    }

@pytest.fixture
def match_players_init():
    return PLAYERS_2

@pytest.fixture
def match_spellbook():
    '''We are returning 1 here intentionally, since we use Warlocks a default spellbook for now.'''
    return 1

@pytest.fixture
def match_id():
    return 123456

@pytest.fixture
def lang_code():
    return 'en'

@pytest.fixture
def def_pov_id():
    return -1

@pytest.fixture
def stay_silent():
    return True
