from tests_core.tests_engine_core import run_common_tests
from tests_warlocks.tests_spellbook_warlocks import run_warlocks_tests, run_warlocks_attack_seed_test
from tests_spellbinder.tests_spellbook_spellbinder import run_spellbinder_tests, run_spellbinder_tests_melee

# MAIN
if __name__ == '__main__':

    match_id = 123456

    available_spellbooks = {
        1: {'code': 'Warlocks', 'title': "RavenBlack's Warlocks - ParaFC Maladroit"},
        2: {'code': 'Spellbinder', 'title': "Bartle's Spellbinder - Original Ruleset"},
        3: {'code': 'TBD', 'title': "TBD"},
    }

    lang_code = 'en'
    def_pov_id = -1

    silent_run = 1

    match_spellbook = 1

    match_players_init = [
        {'player_id': 2, 'player_name': 'TestWarlock',
            'gender': 1, 'team_id': 1, 'lang': 'en'},
        {'player_id': 3, 'player_name': 'TestFoe',
            'gender': 0, 'team_id': 2, 'lang': 'en'},
    ]

    run_common_tests(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    run_warlocks_tests(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    match_players_init = [
        {'player_id': 2, 'player_name': 'TestWarlock',
            'gender': 1, 'team_id': 1, 'lang': 'en'},
        {'player_id': 3, 'player_name': 'TestFoe',
            'gender': 0, 'team_id': 2, 'lang': 'en'},
        {'player_id': 4, 'player_name': 'TestAlly',
            'gender': 2, 'team_id': 1, 'lang': 'en'},
        {'player_id': 5, 'player_name': 'TestFoe2',
            'gender': 2, 'team_id': 2, 'lang': 'en'},
    ]

    run_warlocks_attack_seed_test(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    match_spellbook = 2

    match_players_init = [
        {'player_id': 2, 'player_name': 'TestWarlock',
            'gender': 1, 'team_id': 1, 'lang': 'en'},
        {'player_id': 3, 'player_name': 'TestFoe',
            'gender': 0, 'team_id': 2, 'lang': 'en'},
    ]
    run_spellbinder_tests(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    match_players_init = [
        {'player_id': 2, 'player_name': 'TestWarlock',
            'gender': 1, 'team_id': 1, 'lang': 'en'},
        {'player_id': 3, 'player_name': 'TestFoe',
            'gender': 0, 'team_id': 2, 'lang': 'en'},
        {'player_id': 4, 'player_name': 'TestFoe2',
            'gender': 2, 'team_id': 3, 'lang': 'en'},
    ]
    run_spellbinder_tests_melee(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
