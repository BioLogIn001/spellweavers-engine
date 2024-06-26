from tests_core.tests_engine_core import match_process_json

if __name__ == '__main__':

    match_id = 123456

    available_spellbooks = {
        1: {'code': 'Warlocks', 'title': "RavenBlack's Warlocks - ParaFC Maladroit"},
        2: {'code': 'Spellbinder', 'title': "Bartle's Original Ruleset [not implemented]"},
        3: {'code': 'MortalSpell', 'title': "Naigsa's MortalSpell Ruleset [not implemented]"},
    }

    match_players_init = [
        {'player_id': 2, 'player_name': 'TestWarlock',
            'gender': 1, 'team_id': 1, 'lang': 'en'},
        {'player_id': 3, 'player_name': 'TestFoe',
            'gender': 0, 'team_id': 2, 'lang': 'en'},
        # {'player_id': 4, 'player_name': 'TestAlly',
        #    'gender': 2, 'team_id': 1, 'lang': 'en'},
        # {'player_id': 5, 'player_name': 'TestFoe2',
        #    'gender': 2, 'team_id': 2, 'lang': 'en'},
        # {'player_id': 5, 'player_name': 'TestFoe2',
           # 'gender': 2, 'team_id': 3, 'lang': 'en'},
    ]

    match_json_filename = 'tests_warlocks\\test_action_02_surrender.json'
    # match_json_filename = 'tests_spellbinder\\test_spell_41_raisedead_M_surrendered_participant.json'

    match_spellbook = 1
    spellbook_code = available_spellbooks[match_spellbook]['code']

    match_data = match_process_json(match_id,
                                    spellbook_code,
                                    match_players_init,
                                    match_json_filename)

    lang_code = 'en'
    pov_id = 0

    match_data.match_init_output(spellbook_code, lang_code)
    match_data.print_match_log(pov_id)
    match_data.print_actor_statuses(pov_id)
