import sys
from pathlib import Path
from tests_core.tests_engine_core import match_process_json

def parse_args() -> dict:
    args: dict = {}
    for arg in sys.argv[1:]:
        (k, v) = arg.split("=", 1)
        if not k or not v:
            continue
        args |= {k: v}
    return args


if __name__ == '__main__':

    DEFAULT_MATCH_ID = 123456

    supported_locales = ['en']

    available_spellbooks = {
        1: {'code': 'Warlocks', 'title': "RavenBlack's Warlocks - ParaFC Maladroit"},
        2: {'code': 'Spellbinder', 'title': "Bartle's Spellbinder - Original Ruleset"},
        3: {'code': 'TBD', 'title': "TBD"},
    }

    match_players_init_template: dict[int, list[dict[str, str | int]]] = {
        2: [{'player_id': 2, 'player_name': 'TestWarlock',
                'gender': 1, 'team_id': 1, 'lang': 'en'},
                {'player_id': 3, 'player_name': 'TestFoe',
                'gender': 0, 'team_id': 2, 'lang': 'en'},],
        3: [{'player_id': 2, 'player_name': 'TestWarlock',
                'gender': 1, 'team_id': 1, 'lang': 'en'},
                {'player_id': 3, 'player_name': 'TestFoe1',
                'gender': 0, 'team_id': 2, 'lang': 'en'},
                {'player_id': 4, 'player_name': 'TestFoe2',
                'gender': 2, 'team_id': 1, 'lang': 'en'}],
        4: [{'player_id': 2, 'player_name': 'TestWarlock',
                'gender': 1, 'team_id': 1, 'lang': 'en'},
                {'player_id': 3, 'player_name': 'TestFoe',
                'gender': 0, 'team_id': 2, 'lang': 'en'},
                {'player_id': 4, 'player_name': 'TestAlly',
                'gender': 2, 'team_id': 1, 'lang': 'en'},
                {'player_id': 5, 'player_name': 'TestFoe2',
                'gender': 2, 'team_id': 2, 'lang': 'en'},]
    }

    args = parse_args()
    
    if '-f' in args:
        match_json_filename = args['-f']
    else:
        raise Exception('Filename not submitted')
    filepath = Path(match_json_filename)
    if not filepath.is_file():
        raise Exception('File does not exist')        

    if '-m' in args:
        match_id = int(args['-m'])
    else:
        match_id = DEFAULT_MATCH_ID
    
    if '-s' in args and int(args['-s']) in available_spellbooks:
        match_spellbook = int(args['-s'])
        spellbook_code = available_spellbooks[match_spellbook]['code']
    else:
        raise Exception('Spellbook not submitted')
    
    if '-l' in args and args['-l'] in supported_locales:
        lang_code = args['-l']
    else:
        lang_code = 'en'
    
    if  '-p' in args and int(args['-p']) in match_players_init_template:
        player_count = int(args['-p'])
    else:
        player_count = 2
    match_players_init = match_players_init_template[player_count]
    
    if '-pov' in args and int(args['-pov']) in range(-1, player_count + 1):
        pov_id = int(args['-pov'])
    else:
        pov_id = -1

    if '-silent' in args:
        stay_silent = bool(args['-silent'])
    else:
        stay_silent = False

    match_data = match_process_json(match_id,
                                    spellbook_code,
                                    match_players_init,
                                    match_json_filename)

    match_data.match_init_output(spellbook_code, lang_code)
    match_data.print_match_log(pov_id, stay_silent)
    match_data.print_actor_statuses(pov_id, stay_silent)
