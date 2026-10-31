"""Client contract: what swweb (and other clients) may rely on, per ruleset.

Each list is the documented surface (see docs/client-contract.md). A rename or removal that would
break a client fails here. Anything not listed is internal and may change without notice.
"""
import pytest

from spellweavers.tools_engine import import_name

MATCHDATA = [
    'DATA_HAND_ID_OFFSET', 'match_id', 'current_turn', 'match_status', 'participant_list', 'monster_list',
    'match_log', 'match_gestures', 'turns_info', 'spell_names',
    'create_participant', 'create_monster', 'process_match_start', 'process_match_turn', 'set_current_turn',
    'match_init_output', 'get_match_status_ongoing', 'get_match_status_finished',
    'get_ids_participants', 'get_ids_participants_active', 'get_ids_monsters', 'get_ids_targets',
    'get_participant_by_id', 'get_monster_by_id', 'get_name_by_id', 'get_participant_turn_active_status',
    'get_status_string_actor_by_id', 'get_text_strings_by_code', 'get_turn_info_template',
    'get_gesture', 'get_gesture_history', 'get_log_entry_template', 'get_log_entries_by_turn',
    'get_log_string_by_log_id',
]
ORDERS = ['orders', 'parse_json_order', 'validate_json_order', 'check_missing_orders']
ORDER = [
    'match_id', 'turn_num', 'participant_id', 'gesture_lh', 'gesture_rh', 'order_spell_lh', 'order_spell_rh',
    'order_target_lh', 'order_target_rh', 'delay_spell', 'cast_delayed_spell', 'make_spell_permanent',
    'commit_suicide', 'paralyze_orders', 'charm_orders', 'attack_orders',
]
SPELLBOOK = [
    'spellbook_code', 'valid_gestures', 'valid_gestures_feared', 'valid_spell_ids', 'spell_definitions',
    'get_new_spell_by_id', 'match_spell_pattern_monsters',
]
SPELL = ['id', 'caster_id', 'target_id', 'used_hand', 'used_pattern', 'cast_turn', 'resolve', 'flags']
ACTOR = ['id', 'hp', 'is_alive', 'effects', 'states', 'get_effects_template', 'get_states_template',
         'set_actor_id', 'turn_created', 'turn_destroyed']
PARTICIPANT = ACTOR + ['player_id', 'team_id', 'lh_id', 'rh_id', 'set_hands_ids', 'turn_surrendered']
MONSTER = ACTOR + ['monster_type', 'controller_id', 'attack_id', 'summoner_id', 'summoner_hand_id']
SPELL_DEFINITION = ['id', 'priority', 'patterns', 'default_target', 'duration', 'code', 'tags']


def load(spellbook_code: str, kind: str):
    lib_name = 'spellweavers.' + spellbook_code.lower() + '.'
    return import_name(lib_name + 'class_' + spellbook_code.lower() + '_' + kind,
                       spellbook_code + {'matchdata': 'MatchData', 'spellbook': 'SpellBook',
                                         'orders': 'Orders'}[kind])


def missing(obj, names: list[str]) -> list[str]:
    return [n for n in names if not hasattr(obj, n)]


@pytest.mark.parametrize('match_spellbook', [1, 2])
def test_client_contract(available_spellbooks, match_spellbook, match_id, lang_code):

    spellbook_code = available_spellbooks[match_spellbook]['code']
    match_data = load(spellbook_code, 'matchdata')(match_id)
    spellbook = load(spellbook_code, 'spellbook')()
    orders = load(spellbook_code, 'orders')()
    match_data.match_init_output(spellbook_code, lang_code)

    # Actors are created the way clients create them: through MatchData
    participant = match_data.create_participant(2, 1, 'TestWarlock', 1)
    participant.set_actor_id(1)
    participant.set_hands_ids(match_data.DATA_HAND_ID_OFFSET)
    monster = match_data.create_monster(participant.id, 1, participant.id, participant.lh_id, 1, 0)

    assert missing(match_data, MATCHDATA) == []
    assert missing(orders, ORDERS) == []
    assert missing(orders.order_class(), ORDER) == []
    assert missing(spellbook, SPELLBOOK) == []
    assert missing(spellbook.spells[0], SPELL) == []
    assert missing(participant, PARTICIPANT) == []
    assert missing(monster, MONSTER) == []
    assert all(set(SPELL_DEFINITION) <= d.keys() for d in spellbook.spell_definitions)
    assert 'delayed' in spellbook.spells[0].flags

    # Localisation tables clients load by name
    loc = 'spellweavers.' + spellbook_code.lower() + '.loc_' + spellbook_code.lower()
    assert import_name(loc + '_' + lang_code, spellbook_code.lower() + '_spell_names_' + lang_code)
    assert import_name(loc + '_rules_' + lang_code, spellbook_code.lower() + '_spell_descriptions_' + lang_code)
