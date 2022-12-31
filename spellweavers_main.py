from functions_debug import dprint


def import_name(modulename, name):
    """Import a named object from a module in the context of this function.
    Source: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch15s04.html
    """
    try:
        module = __import__(modulename, globals(), locals(), [name])
    except ImportError:
        return None
    return vars(module)[name]


def tmp_parse_json_game(match_id, spellbook_data, lang_code, match_players_init, match_json_fname):
    """Initiate game variables and play a game using JSON file as a source of orders.
    
    Classes and variables are loaded dynamically from selected spellbook files. 
    For example, for Warlocks spellbook and for English language we load the following:
    from class_warlocks_match_data import WarlocksMatchData
    from class_warlocks_spellbook import WarlocksSpellBook
    from class_warlocks_orders import WarlocksOrders
    from loc_warlocks_en import warlocks_strings_en, warlocks_monster_names_en, warlocks_monster_classes_en, warlocksSpellNamesEN, warlocks_spell_effects_en
    
    Aside from aforementioned files and classes, the following methods are required:
    match_data.process_match_start
    match_data.process_turn_phase_0
    match_data.process_turn_phase_1
    match_data.process_turn_phase_2
    match_data.process_turn_phase_3
    
    We also load common text string from respective lang file, f.e. loc_common_en.
    """

    # Init match data
    match_data = import_name('class_' + spellbook_data['code'].lower() + '_matchdata',
                             spellbook_data['code'] + 'MatchData')(match_id)
    # Init text strings
    spellbook_text_strings = import_name('loc_' + spellbook_data['code'].lower() + '_' + lang_code.lower(),
                                         spellbook_data['code'].lower() + '_text_strings_' + lang_code)
    common_text_strings = import_name('loc_common_' + lang_code.lower(),
                                      'common_text_strings_' + lang_code)
    spellbook_spell_names = import_name('loc_' + spellbook_data['code'].lower() + '_' + lang_code.lower(),
                                        spellbook_data['code'].lower() + '_spell_names_' + lang_code)
    spellbook_spell_effects = import_name('loc_' + spellbook_data['code'].lower() + '_' + lang_code.lower(),
                                          spellbook_data['code'].lower() + '_spell_effects_' + lang_code)
    spellbook_monster_names = import_name('loc_' + spellbook_data['code'].lower() + '_' + lang_code.lower(),
                                          spellbook_data['code'].lower() + '_monster_names_' + lang_code)
    spellbook_monster_classes = import_name('loc_' + spellbook_data['code'].lower() + '_' + lang_code.lower(),
                                            spellbook_data['code'].lower() + '_monster_classes_' + lang_code)
    match_data.init_text_vars(spellbook_text_strings | common_text_strings, spellbook_spell_names,
                              spellbook_spell_effects, spellbook_monster_names, spellbook_monster_classes)
    # Init spellbook
    match_spellbook = import_name('class_' + spellbook_data['code'].lower() + '_spellbook',
                                  spellbook_data['code'] + 'SpellBook')(match_data.spell_names)
    # Init orders
    match_orders = import_name('class_' + spellbook_data['code'].lower() + '_orders',
                               spellbook_data['code'] + 'Orders')()
    match_orders.set_filename(match_json_fname)
    # Init participants and start the match
    match_data.init_actors_tmp(match_players_init)
    match_data.process_match_start()

    # Make turns while match is not over and turn orders are available
    while 1:

        # Turn startup and orders loading
        status = match_data.process_turn_phase_0(match_orders, match_spellbook)
        if status != 1:
            break

        # Spellcasting
        status = match_data.process_turn_phase_1(match_orders, match_spellbook)
        if status != 1:
            break

        # Combat
        status = match_data.process_turn_phase_2(match_orders)
        if status != 1:
            break

        # Clean-up
        status = match_data.process_turn_phase_3(match_orders)
        if status != 1:
            break

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
        {'player_id': 123, 'player_name': 'BioLogIn',
            'gender': 1, 'team_id': 1, 'lang': 'en'},
        {'player_id': 445, 'player_name': 'TestFoe',
            'gender': 0, 'team_id': 2, 'lang': 'en'},
        #{'player_id': 666, 'player_name': 'TestAlly',
        #    'gender': 2, 'team_id': 1, 'lang': 'en'},
        #{'player_id': 777, 'player_name': 'TestFoe2', 
        #    'gender': 2, 'team_id': 2, 'lang': 'en'},
    ]
    match_json_fname = 'tests/test_special_spell_selection.json'

    # Placeholder. Should be chosen from the settings of participant we render for.
    lang_code = 'en'

    match_data = tmp_parse_json_game(match_id, available_spellbooks[match_spellbook], lang_code,
                                     match_players_init, match_json_fname)
