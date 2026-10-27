import os

from spellweavers.engine import match_process_json


def run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id):
    """Prepare test runs."""
    print('Testing', match_json_filename)

    spellbook_code = available_spellbooks[match_spellbook]['code']

    match_data = match_process_json(match_id,
                                    spellbook_code,
                                    match_players_init,
                                    match_json_filename)

    match_data.match_init_output(spellbook_code, lang_code)
    match_data.log_match_history(def_pov_id)
    match_data.log_actor_statuses(def_pov_id)

    if stay_silent is False: 
        for ss in match_data.log:
            print(ss)

    return match_data


def test_template(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_core', 'test_!template.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
