def import_name(modulename, name):
    """Import a named object from a module in the context of this function.
    Source: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch15s04.html
    """
    try:
        module = __import__(modulename, globals(), locals(), [name])
    except ImportError:
        return None
    return vars(module)[name]


def tmp_parse_json_game(match_id, spellbook_code, lang_code, match_players_init, match_json_fname, pov_id):
    """Initiate game variables and play a game using JSON file as a source of orders.
    
    Classes and variables are loaded dynamically from selected spellbook files. 
    For example, for Warlocks spellbook and for English language we load the following:
    from class_warlocks_match_data import WarlocksMatchData
    from class_warlocks_spellbook import WarlocksSpellBook
    from class_warlocks_orders import WarlocksOrders
    from loc_warlocks_en import warlocks_strings_en, warlocks_monster_names_en, 
        warlocks_monster_classes_en, warlocks_spell_names_en, warlocks_spell_effects_en
    
    In additional to files and classes and variables listed above, 
        the following methods are required from each MatchData implementation:
    .process_match_start()
    .process_turn_phase_startup()
    .process_turn_phase_cast()
    .process_turn_phase_attack()
    .process_turn_phase_cleanup()

    We also load common text strings from respective lang file, f.e. loc_common_en.
    """

    core_name = 'ruleset_core.'
    lib_name = 'ruleset_' + spellbook_code.lower() + '.'

    # Init match data
    match_data = import_name(lib_name + 'class_' + spellbook_code.lower() + '_matchdata',
                             spellbook_code + 'MatchData')(match_id)
    # Init text strings
    spellbook_text_strings = import_name(lib_name + 'loc_' + spellbook_code.lower() + '_' + lang_code.lower(),
                                         spellbook_code.lower() + '_text_strings_' + lang_code)
    common_text_strings = import_name(core_name + 'loc_common_' + lang_code.lower(),
                                      'common_text_strings_' + lang_code)
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
    # Init spellbook
    match_spellbook = import_name(lib_name + 'class_' + spellbook_code.lower() + '_spellbook',
                                  spellbook_code + 'SpellBook')(match_data.spell_names)
    # Init orders
    match_orders = import_name(lib_name + 'class_' + spellbook_code.lower() + '_orders',
                               spellbook_code + 'Orders')()
    match_orders.set_filename(match_json_fname)
    # Init participants and start the match
    match_data.init_actors_tmp(match_players_init)
    match_data.process_match_start()

    # Make turns while match is not over and turn orders are available
    while 1:

        # Turn startup and orders loading
        status = match_data.process_turn_phase_startup(match_orders, match_spellbook)
        if status != 1:
            break

        # Spellcasting
        status = match_data.process_turn_phase_cast(match_orders, match_spellbook, pov_id)
        if status != 1:
            break

        # Combat
        status = match_data.process_turn_phase_attack(match_orders)
        if status != 1:
            break

        # Clean-up
        status = match_data.process_turn_phase_cleanup(match_orders, pov_id)
        if status != 1:
            break

    match_data.output_match_actors_status(pov_id)

    return match_data


if __name__ == '__main__':

    available_spellbooks = {
        1: {'code': 'Warlocks', 'title': "RavenBlack's Warlocks - ParaFC Maladroit"},
        2: {'code': 'SpellBinder', 'title': "Bartle's Original Ruleset [not implemented]"},
        3: {'code': 'MortalSpell', 'title': "Naigsa's MortalSpell Ruleset [not implemented]"},
    }
    match_id = 123456
    match_spellbook = 1
    match_players_init = [
        {'player_id': 2, 'player_name': 'TestWarlock',
            'gender': 1, 'team_id': 1, 'lang': 'en'},
        {'player_id': 3, 'player_name': 'TestFoe',
            'gender': 0, 'team_id': 2, 'lang': 'en'},
        #{'player_id': 666, 'player_name': 'TestAlly',
        #    'gender': 2, 'team_id': 1, 'lang': 'en'},
        #{'player_id': 777, 'player_name': 'TestFoe2', 
        #    'gender': 2, 'team_id': 2, 'lang': 'en'},
    ]
    match_json_fname = 'tests_warlocks\\test_special_double_delay.json'

    # Placeholder. Should be chosen from the settings of participant we render for.
    lang_code = 'en'

    pov_id = 0

    match_data = tmp_parse_json_game(match_id, available_spellbooks[match_spellbook]['code'], 
                                     lang_code, match_players_init, match_json_fname, pov_id)

    match_data.print_output_strings()