def import_name(modulename, name):
    """Import a named object from a module in the context of this function.
    Source: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch15s04.html
    """
    try:
        module = __import__(modulename, globals(), locals(), [name])
    except ImportError:
        return None
    return vars(module)[name]


def match_process_json(match_id, spellbook_code, match_players_init, match_json_fname):
    """Initiate game variables and play a game using JSON file as a source of orders.
    
    Classes and variables are loaded dynamically from selected spellbook files. 
    For example, for Warlocks spellbook and for English language we load the following:
    from class_warlocks_match_data import WarlocksMatchData
    from class_warlocks_spellbook import WarlocksSpellBook
    from class_warlocks_orders import WarlocksOrders
    
    In additional to files and classes and variables listed above, 
        the following methods are required from each MatchData implementation:
    .process_match_start()
    .process_turn_phase_startup()
    .process_turn_phase_cast()
    .process_turn_phase_attack()
    .process_turn_phase_cleanup()
    
    Args:
        match_id (int): match number that should match match ID in orders / json
        spellbook_code (str): selected spellbook code, f.e. "Warlocks"
        match_players_init (dict): a dictionary with basic participant info (usernames, etc.)
        match_json_fname (str): name of the json file to parse orders from
    
    Returns:
        object: instance of spellbook-specific MatchData-inherited object
    """

    core_name = 'ruleset_core.'
    lib_name = 'ruleset_' + spellbook_code.lower() + '.'

    # Init match data
    match_data = import_name(lib_name + 'class_' + spellbook_code.lower() + '_matchdata',
                             spellbook_code + 'MatchData')(match_id)
    # Init spellbook
    match_spellbook = import_name(lib_name + 'class_' + spellbook_code.lower() + '_spellbook',
                                  spellbook_code + 'SpellBook')()
    # Init orders
    match_orders = import_name(lib_name + 'class_' + spellbook_code.lower() + '_orders',
                               spellbook_code + 'Orders')()

    match_orders.set_filename(match_json_fname)
    # Init participants and start the match
    match_data.init_actors_tmp(match_players_init)
    match_data.process_match_start()

    # Make turns while match is not over and turn orders are available
    while 1:

        # Check if the match is still going
        if match_data.get_match_status_finished():
            break  # match finished

        # Increase the turn counter
        match_data.set_current_turn(match_data.current_turn + 1)

        # Request orders for all participants active during this turn
        match_orders.get_turn_orders(match_data.match_id, 
                                        match_data.current_turn,
                                        match_data.hand_id_offset,
                                        match_data.get_ids_participants_active(),
                                        match_spellbook.valid_gestures,
                                        match_spellbook.valid_spell_ids)

        # Turn startup
        status = match_data.process_turn_phase_startup(match_orders, match_spellbook)
        if status != 1:
            break

        # Spellcasting
        status = match_data.process_turn_phase_cast(match_orders, match_spellbook)
        if status != 1:
            break

        # Combat
        status = match_data.process_turn_phase_attack(match_orders)
        if status != 1:
            break

        # Clean-up
        status = match_data.process_turn_phase_cleanup(match_orders)
        if status != 1:
            break

    return match_data

def match_init_output(spellbook_code, match_data, lang_code):
    """Process match_data and transform match_log, gesture history and actors statuses, 
    taking into account point-of-view visibility, user language locale and match spellbook, 
    into text strings for output.
    
    Args:
        spellbook_code (str): selected spellbook code, f.e. "Warlocks"
        match_data (object): instance of spellbook-specific MatchData-inherited object
        lang_code (str): code of the language to use for rendering (f.e. 'en')
    """

    # Init text strings
    core_name = 'ruleset_core.'
    lib_name = 'ruleset_' + spellbook_code.lower() + '.'

    """
    We load common text strings from respective lang file, f.e. loc_common_en.

    We load text strings from spellbook land file, f.e.:
    from loc_warlocks_en import warlocks_text_strings_en, warlocks_spell_names_en, 
        warlocks_spell_effects_en, warlocks_monster_names_en, warlocks_monster_classes_en
    """

    common_text_strings = import_name(core_name + 'loc_common_' + lang_code.lower(),
                                      'common_text_strings_' + lang_code)
    spellbook_text_strings = import_name(lib_name + 'loc_' + spellbook_code.lower() + '_' + lang_code.lower(),
                                         spellbook_code.lower() + '_text_strings_' + lang_code)
    spellbook_spell_names = import_name(lib_name + 'loc_' + spellbook_code.lower() + '_' + lang_code.lower(),
                                        spellbook_code.lower() + '_spell_names_' + lang_code)
    spellbook_spell_effects = import_name(lib_name + 'loc_' + spellbook_code.lower() + '_' + lang_code.lower(),
                                          spellbook_code.lower() + '_spell_effects_' + lang_code)
    spellbook_monster_names = import_name(lib_name + 'loc_' + spellbook_code.lower() + '_' + lang_code.lower(),
                                          spellbook_code.lower() + '_monster_names_' + lang_code)
    spellbook_monster_classes = import_name(lib_name + 'loc_' + spellbook_code.lower() + '_' + lang_code.lower(),
                                            spellbook_code.lower() + '_monster_classes_' + lang_code)
    match_data.init_text_vars(spellbook_text_strings | common_text_strings, spellbook_spell_names,
                              spellbook_spell_effects, spellbook_monster_names, spellbook_monster_classes)


if __name__ == '__main__':

    match_id = 123456

    available_spellbooks = {
        1: {'code': 'Warlocks', 'title': "RavenBlack's Warlocks - ParaFC Maladroit"},
        2: {'code': 'SpellBinder', 'title': "Bartle's Original Ruleset [not implemented]"},
        3: {'code': 'MortalSpell', 'title': "Naigsa's MortalSpell Ruleset [not implemented]"},
    }
    match_spellbook = 1
    spellbook_code = available_spellbooks[match_spellbook]['code']

    match_players_init = [
        {'player_id': 2, 'player_name': 'TestWarlock',
            'gender': 1, 'team_id': 1, 'lang': 'en'},
        {'player_id': 3, 'player_name': 'TestFoe',
            'gender': 0, 'team_id': 2, 'lang': 'en'},
        #{'player_id': 4, 'player_name': 'TestAlly',
        #    'gender': 2, 'team_id': 1, 'lang': 'en'},
        #{'player_id': 5, 'player_name': 'TestFoe2', 
        #    'gender': 2, 'team_id': 2, 'lang': 'en'},
    ]

    match_json_filename = 'tests_warlocks\\test_special_visibility.json'

    match_data = match_process_json(match_id, 
                                    spellbook_code, 
                                    match_players_init, 
                                    match_json_filename)

    lang_code = 'en'
    pov_id = 0

    match_init_output(spellbook_code, match_data, lang_code)
    match_data.print_match_log(pov_id)
    match_data.print_actor_statuses(pov_id)
