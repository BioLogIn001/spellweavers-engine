from spellweavers.tools_engine import import_name


def match_process_json(match_id: int, spellbook_code: str, match_players_init: list[dict[str, str | int]], match_json_fname: str):
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

    Arguments:
        match_id (int): match number that should match match ID in orders / json
        spellbook_code (str): selected spellbook code, f.e. "Warlocks"
        match_players_init (list): a list with basic participant info (usernames, etc.)
        match_json_fname (str): name of the json file to parse orders from

    Returns:
        object: instance of spellbook-specific MatchData-inherited object
    """
    lib_name = 'spellweavers.' + spellbook_code.lower() + '.'

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
    while True:

        # Check if the match is still going
        if match_data.get_match_status_finished():
            break  # match finished

        # Request orders for all participants active during this turn
        match_orders.get_turn_orders(match_data.match_id,
                                     match_data.current_turn,
                                     match_data.DATA_HAND_ID_OFFSET,
                                     match_data.get_ids_participants_active(),
                                     match_spellbook.valid_gestures,
                                     match_spellbook.valid_spell_ids)

        # Check if some orders are missing and stop processing the turn if some are
        missing_orders = match_orders.check_missing_orders(match_data)
        if missing_orders:
            break  # not processed - missing orders

        match_data.process_match_turn(match_orders, match_spellbook)

        # Increase the turn counter
        if match_data.get_match_status_ongoing():
            match_data.set_current_turn(match_data.current_turn + 1)

    return match_data
