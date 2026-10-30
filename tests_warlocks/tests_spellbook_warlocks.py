import os

from tests_core.tests_engine_core import run_test

# Summon Fire Elemental and Ice Elemental

def test_spell_08_fireelemental_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_A_deftarget.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 12)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 5)
    assert (m1.hp == 3)


def test_spell_08_fireelemental_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_B_nobody.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 12)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 5)
    assert (m1.hp == 3)


def test_spell_08_fireelemental_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_C_self.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 12)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 5)
    assert (m1.hp == 3)


def test_spell_08_fireelemental_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_D_oppo.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 12)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 5)
    assert (m1.hp == 3)


def test_spell_08_fireelemental_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_G_monster.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    m2 = match_data.get_monster_by_id(102, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 12)
    assert (m1.is_alive == 0)
    assert (m1.hp == -2)
    assert (m2.is_alive == 1)
    assert (m2.monster_type == 5)
    assert (m2.hp == 3)


def test_spell_08_fireelemental_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_H_countered.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 15)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 5)
    assert (m1.hp == 3)


def test_spell_08_fireelemental_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_I_mirrored.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 12)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 5)
    assert (m1.hp == 3)


def test_spell_08_fireelemental_J_merge(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_J_merge.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    m2 = match_data.get_monster_by_id(102, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.is_alive == 0)
    assert (m1.monster_type == 5)
    assert (m2.is_alive == 1)
    assert (m2.monster_type == 5)


def test_spell_09_iceelemental_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_09_iceelemental_A_deftarget.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 12)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 6)
    assert (m1.hp == 3)


def test_spell_09_iceelemental_J_merge(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_09_iceelemental_J_merge.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    m2 = match_data.get_monster_by_id(102, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.is_alive == 0)
    assert (m1.monster_type == 6)
    assert (m2.is_alive == 1)
    assert (m2.monster_type == 6)


# Time Stop

def test_spell_11_timestop_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_A_deftarget.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_11_timestop_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_B_nobody.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_11_timestop_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_C_self.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_11_timestop_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_D_oppo.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_11_timestop_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_E_hand.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_11_timestop_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_F_newsummon.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 14)
    assert (p2.affected_by_pshield(match_data.current_turn) > 0)


def test_spell_11_timestop_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_G_monster.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 14)
    assert (p2.affected_by_pshield(match_data.current_turn) > 0)


def test_spell_11_timestop_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_H_countered.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_11_timestop_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_I_mirrored.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_11_timestop_K_invis_end_antispell(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_K_invis_end_antispell.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    spaced_gesture_history = 1
    participant_id = 1
    pov_id = 2
    hand_id = 1
    lh_gestures = 'B' + match_data.get_gesture_history(participant_id, hand_id, spaced_gesture_history, pov_id)
    hand_id = 2
    rh_gestures = 'B' + match_data.get_gesture_history(participant_id, hand_id, spaced_gesture_history, pov_id)
    assert (lh_gestures[7] == '?')
    assert (rh_gestures[7] == '?')
    assert (lh_gestures[8] == '-')
    assert (rh_gestures[8] == '-')


def test_spell_11_timestop_L_counter_antispell(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_L_counter_antispell.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    spaced_gesture_history = 1
    participant_id = 1
    pov_id = 2
    hand_id = 1
    lh_gestures = 'B' + match_data.get_gesture_history(participant_id, hand_id, spaced_gesture_history, pov_id)
    hand_id = 2
    rh_gestures = 'B' + match_data.get_gesture_history(participant_id, hand_id, spaced_gesture_history, pov_id)
    assert (lh_gestures[8] == '-')
    assert (rh_gestures[8] == '-')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 14)
    assert (p2.hp == 15)


# Resist Heat

def test_spell_13_resistheat_J_fireelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_13_resistheat_J_fireelem.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    m2 = match_data.get_monster_by_id(102, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 0)
    assert (m2.is_alive == 0)


# Resist Cold

def test_spell_14_resistcold_J_iceelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_14_resistcold_J_iceelem.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    m2 = match_data.get_monster_by_id(102, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_cold_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_cold_permanent(match_data.current_turn) == 0)
    assert (m2.is_alive == 0)


# Paralysis

def test_spell_15_paralysis_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_15_paralysis_I_mirrored.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'C')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


# Amnesia

def test_spell_16_amnesia_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_16_amnesia_F_newsummon.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'F')
    assert (p2gRH == 'F')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_16_amnesia_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_16_amnesia_G_monster.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'F')
    assert (p2gRH == 'F')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


# Fear

def test_spell_17_fear_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_17_fear_F_newsummon.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'F')
    assert (p2gRH == 'F')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_17_fear_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_17_fear_G_monster.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'F')
    assert (p2gRH == 'F')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


# Maladroitness

def test_spell_18_maladroitness_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_A_deftarget.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_18_maladroitness_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_B_nobody.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'S')
    assert (p2gRH == 'W')


def test_spell_18_maladroitness_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_C_self.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'F')
    assert (p1gRH == 'F')
    assert (p2gLH == 'S')
    assert (p2gRH == 'W')


def test_spell_18_maladroitness_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_D_oppo.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_18_maladroitness_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_E_hand.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'S')
    assert (p2gRH == 'W')


def test_spell_18_maladroitness_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_F_newsummon.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'S')
    assert (p2gRH == 'W')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_18_maladroitness_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_G_monster.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'S')
    assert (p2gRH == 'W')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_18_maladroitness_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_H_countered.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'S')
    assert (p2gRH == 'W')


def test_spell_18_maladroitness_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_I_mirrored.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'F')
    assert (p1gRH == 'F')
    assert (p2gLH == 'S')
    assert (p2gRH == 'W')


# Cure Light Wounds

def test_spell_23_curelightwounds_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_A_deftarget.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 16)
    assert (p2.hp == 15)


def test_spell_23_curelightwounds_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_C_self.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 16)
    assert (p2.hp == 15)


def test_spell_23_curelightwounds_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_D_oppo.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 16)


def test_spell_23_curelightwounds_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_F_newsummon.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.hp == 2)


def test_spell_23_curelightwounds_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_G_monster.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.hp == 2)


def test_spell_23_curelightwounds_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_I_mirrored.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 16)
    assert (p2.hp == 15)


def test_spell_23_curelightwounds_J_overheal(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_J_overheal.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 16)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.hp == 2)


# Cure Heavy Wounds

def test_spell_24_cureheavywounds_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_24_cureheavywounds_F_newsummon.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)
    assert (m1.hp == 0)


def test_spell_24_cureheavywounds_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_24_cureheavywounds_G_monster.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)
    assert (m1.hp == 0)


def test_spell_24_cureheavywounds_J_overheal(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_24_cureheavywounds_J_overheal.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 16)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.hp == 2)


# Anti-Spell

def test_spell_25_antispell_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_A_deftarget.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == '-')
    assert (p2gRH == '-')


def test_spell_25_antispell_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_B_nobody.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_25_antispell_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_C_self.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == '-')
    assert (p1gRH == '-')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_25_antispell_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_D_oppo.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == '-')
    assert (p2gRH == '-')


def test_spell_25_antispell_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_E_hand.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_25_antispell_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_F_newsummon.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_25_antispell_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_G_monster.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_25_antispell_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_H_countered.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == 'S')
    assert (p2gRH == 'W')


def test_spell_25_antispell_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_I_mirrored.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == '-')
    assert (p1gRH == '-')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_25_antispell_J_surrender(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_J_surrender.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == '-')
    assert (p2gRH == '-')
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p2.is_alive == 0)


# Blindness

def test_spell_26_blindness_J_pattern(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_26_blindness_J_pattern.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


# Permanency

def test_spell_28_permanency_M_maladroitness(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_M_maladroitness.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p2.affected_by_maladroitness_permanent(match_data.current_turn) == 1)
    respect_antispell = True
    assert (match_data.get_gesture_filtered(p2.id, 8, 1, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 8, 2, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 9, 1, respect_antispell) == 'D')
    assert (match_data.get_gesture_filtered(p2.id, 9, 2, respect_antispell) == 'D')
    assert (match_data.get_gesture_filtered(p2.id, 10, 1, respect_antispell) == 'S')
    assert (match_data.get_gesture_filtered(p2.id, 10, 2, respect_antispell) == 'S')
    assert (match_data.get_gesture_filtered(p2.id, 11, 1, respect_antispell) == 'F')
    assert (match_data.get_gesture_filtered(p2.id, 11, 2, respect_antispell) == 'F')


def test_spell_28_permanency_N_charm_person(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_N_charmperson.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p2.affected_by_charm_person_permanent(match_data.current_turn) == 1)
    respect_antispell = True
    assert (match_data.get_gesture_filtered(p2.id, 8, 1, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 8, 2, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 9, 1, respect_antispell) == '-')
    assert (match_data.get_gesture_filtered(p2.id, 9, 2, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 10, 1, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 10, 2, respect_antispell) == '-')
    assert (match_data.get_gesture_filtered(p2.id, 11, 1, respect_antispell) == '-')
    assert (match_data.get_gesture_filtered(p2.id, 11, 2, respect_antispell) == 'W')


def test_spell_28_permanency_P_invis_blind(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_P_invis_blind.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    spaced_gesture_history = 1
    participant_id = 1
    pov_id = 2
    hand_id = 1
    lh_gestures = 'B' + match_data.get_gesture_history(participant_id, hand_id, spaced_gesture_history, pov_id)
    hand_id = 2
    rh_gestures = 'B' + match_data.get_gesture_history(participant_id, hand_id, spaced_gesture_history, pov_id)
    assert (lh_gestures[9] == '?')
    assert (rh_gestures[9] == '?')
    assert (lh_gestures[12] == '?')
    assert (rh_gestures[12] == '?')
    participant_id = 2
    pov_id = 1
    hand_id = 1
    lh_gestures = 'B' + match_data.get_gesture_history(participant_id, hand_id, spaced_gesture_history, pov_id)
    hand_id = 2
    rh_gestures = 'B' + match_data.get_gesture_history(participant_id, hand_id, spaced_gesture_history, pov_id)
    assert (lh_gestures[9] == '?')
    assert (rh_gestures[9] == '?')
    assert (lh_gestures[12] == '?')
    assert (rh_gestures[12] == '?')


# Remove Enchantment

def test_spell_30_removeenchantment_J_maladroitness(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_30_removeenchantment_J_maladroitness.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p2 = match_data.get_participant_by_id(2)
    respect_antispell = True
    # Permanent Maladroitness makes p2's LH copy the RH, so the turn 9 stab is lost
    assert (match_data.get_gesture_filtered(p2.id, 9, 1, respect_antispell) == '-')
    # Remove Enchantment on turn 12 clears Maladroitness (WarlocksActor.remove_enchantments), so the turn 13 stab goes through
    assert (p2.affected_by_maladroitness(match_data.current_turn) == 0)
    assert (match_data.get_gesture_filtered(p2.id, 13, 1, respect_antispell) == '>')


# Clap of Lightning

def test_spell_37_clapoflightning_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_A_deftarget.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 10)


def test_spell_37_clapoflightning_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_B_nobody.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_37_clapoflightning_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_C_self.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 15)


def test_spell_37_clapoflightning_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_D_oppo.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 10)


def test_spell_37_clapoflightning_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_E_hand.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_37_clapoflightning_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_F_newsummon.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == -4)
    assert (m1.is_alive == 0)


def test_spell_37_clapoflightning_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_G_monster.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == -4)
    assert (m1.is_alive == 0)


def test_spell_37_clapoflightning_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_H_countered.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_37_clapoflightning_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_I_mirrored.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 15)


def test_spell_37_clapoflightning_J_double(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_J_double.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 10)


# Fire Storm

def test_spell_39_firestorm_L_iceelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_39_firestorm_L_iceelem.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 1)


# Ice Storm

def test_spell_40_icestorm_K_iceelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_K_iceelem.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_40_icestorm_L_fireelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_L_fireelem.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 1)


# Stab

def test_action_01_stab_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_action_01_stab_C_self.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 14)
    assert (p2.hp == 15)


# Special cases

def test_special_mirror_para_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_special_mirror_para_monster.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101)
    assert (m1.monster_type == 1)
    respect_antispell = True
    assert (match_data.get_gesture_filtered(p2.id, 6, 1, respect_antispell) == 'C')


def test_special_double_delay(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_special_double_delay.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    respect_antispell = True
    assert (match_data.get_gesture_filtered(p2.id, 11, 1, respect_antispell) == '-')
    assert (match_data.get_gesture_filtered(p2.id, 11, 2, respect_antispell) == '-')
    assert (p1.states[match_data.current_turn]['delayed_spell'] is not None)


def test_special_delay_corruption(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_special_delay_corruption.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 13)
    assert (p2.hp == 15)
    respect_antispell = True
    assert (match_data.get_gesture_filtered(p2.id, 11, 1, respect_antispell) == '-')
    assert (match_data.get_gesture_filtered(p2.id, 11, 2, respect_antispell) == '-')


def test_special_delay_dispel_and_monsters(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, stay_silent):

    match_json_filename = os.path.join('tests_warlocks', 'test_special_delay_dispel_and_monsters.json')
    match_data = run_test(match_json_filename, stay_silent, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 14)
    assert (p2.hp == 13)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)
