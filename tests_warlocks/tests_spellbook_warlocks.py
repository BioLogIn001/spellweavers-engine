import os
from tests_core.tests_engine_core import match_process_json, run_test

# Dispel Magic


def test_spell_01_dispelmagic_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_01_dispelmagic_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.is_alive == 0)


def test_spell_01_dispelmagic_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_01_dispelmagic_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 14)
    assert (p2.hp == 15)
    assert (m1.is_alive == 0)


def test_spell_01_dispelmagic_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_01_dispelmagic_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.is_alive == 0)


def test_spell_01_dispelmagic_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_01_dispelmagic_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 14)
    assert (p2.hp == 15)
    assert (m1.is_alive == 0)


def test_spell_01_dispelmagic_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_01_dispelmagic_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 14)
    assert (p2.hp == 15)
    assert (m1.is_alive == 0)


def test_spell_01_dispelmagic_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_01_dispelmagic_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 14)
    assert (p2.hp == 15)
    assert (m1.is_alive == 0)


def test_spell_01_dispelmagic_F_remove_bug(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_01_dispelmagic_F_remove_bug.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_01_dispelmagic_H_visibility(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_01_dispelmagic_H_visibility.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    spaced_gesture_history = 1
    participant_id = 1
    pov_id = 2
    hand_id = 1
    lh_gestures = 'B' + match_data.get_gesture_history(participant_id, hand_id, spaced_gesture_history, pov_id)
    hand_id = 2
    rh_gestures = 'B' + match_data.get_gesture_history(participant_id, hand_id, spaced_gesture_history, pov_id)
    assert (lh_gestures[6] == '?')
    assert (rh_gestures[6] == '?')
    assert (lh_gestures[7] == '?')
    assert (rh_gestures[7] == '?')
    assert (lh_gestures[8] == '?')
    assert (rh_gestures[8] == '?')
    assert (lh_gestures[10] == '?')
    assert (rh_gestures[10] == '?')
    assert (lh_gestures[11] != '?')
    assert (rh_gestures[11] != '?')
    participant_id = 2
    pov_id = 1
    hand_id = 1
    lh_gestures = 'B' + match_data.get_gesture_history(participant_id, hand_id, spaced_gesture_history, pov_id)
    hand_id = 2
    rh_gestures = 'B' + match_data.get_gesture_history(participant_id, hand_id, spaced_gesture_history, pov_id)
    assert (lh_gestures[6] == '?')
    assert (rh_gestures[6] == '?')
    assert (lh_gestures[7] == '?')
    assert (rh_gestures[7] == '?')
    assert (lh_gestures[8] == '?')
    assert (rh_gestures[8] == '?')
    assert (lh_gestures[9] != '?')
    assert (rh_gestures[9] != '?')

# CounterSpell


def test_spell_02_counterspell_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_02_counterspell_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_02_counterspell_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_02_counterspell_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 13)
    assert (p2.hp == 15)


def test_spell_02_counterspell_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_02_counterspell_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_02_counterspell_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_02_counterspell_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_02_counterspell_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_02_counterspell_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.is_alive == 1)


def test_spell_02_counterspell_J_pattern(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_02_counterspell_J_pattern.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)

# Magic Mirror


def test_spell_03_magicmirror_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_03_magicmirror_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 13)


def test_spell_03_magicmirror_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_03_magicmirror_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 13)
    assert (p2.hp == 15)


def test_spell_03_magicmirror_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_03_magicmirror_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 13)


def test_spell_03_magicmirror_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_03_magicmirror_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 13)
    assert (p2.hp == 15)


def test_spell_03_magicmirror_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_03_magicmirror_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 13)
    assert (m1.is_alive == 1)


def test_spell_03_magicmirror_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_03_magicmirror_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_03_magicmirror_I_double(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_03_magicmirror_I_double.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.effects[10]['MagicMirror'] == 1)
    assert (p2.effects[10]['MagicMirror'] == 0)

# Summon Goblin, Ogre, Troll, Giant


def test_spell_04_summongoblin_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_04_summongoblin_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 14)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 1)
    assert (m1.hp == 1)
    assert (m1.controller_id == 1)


def test_spell_04_summongoblin_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_04_summongoblin_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_04_summongoblin_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_04_summongoblin_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 14)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 1)
    assert (m1.hp == 1)
    assert (m1.controller_id == 1)


def test_spell_04_summongoblin_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_04_summongoblin_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 14)
    assert (p2.hp == 15)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 1)
    assert (m1.hp == 1)
    assert (m1.controller_id == 2)


def test_spell_04_summongoblin_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_04_summongoblin_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    m2 = match_data.get_monster_by_id(102, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 14)
    assert (m2.is_alive == 1)
    assert (m2.monster_type == 1)
    assert (m2.hp == 1)
    assert (m2.controller_id == 1)


def test_spell_04_summongoblin_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_04_summongoblin_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_04_summongoblin_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_04_summongoblin_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 14)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 1)
    assert (m1.hp == 1)
    assert (m1.controller_id == 1)


def test_spell_05_summonogre_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_05_summonogre_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 13)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 2)
    assert (m1.hp == 2)
    assert (m1.controller_id == 1)


def test_spell_06_summontroll_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_06_summontroll_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 12)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 3)
    assert (m1.hp == 3)
    assert (m1.controller_id == 1)


def test_spell_07_summongiant_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_07_summongiant_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 11)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 4)
    assert (m1.hp == 4)
    assert (m1.controller_id == 1)

# Summon Fire Elemental and Ice Elemental


def test_spell_08_fireelemental_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 12)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 5)
    assert (m1.hp == 3)


def test_spell_08_fireelemental_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 12)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 5)
    assert (m1.hp == 3)


def test_spell_08_fireelemental_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 12)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 5)
    assert (m1.hp == 3)


def test_spell_08_fireelemental_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 12)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 5)
    assert (m1.hp == 3)


def test_spell_08_fireelemental_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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


def test_spell_08_fireelemental_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 15)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 5)
    assert (m1.hp == 3)


def test_spell_08_fireelemental_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 12)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 5)
    assert (m1.hp == 3)


def test_spell_08_fireelemental_J_merge(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_08_fireelemental_J_merge.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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


def test_spell_09_iceelemental_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_09_iceelemental_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 12)
    assert (m1.is_alive == 1)
    assert (m1.monster_type == 6)
    assert (m1.hp == 3)


def test_spell_09_iceelemental_J_merge(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_09_iceelemental_J_merge.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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

# Haste


def test_spell_10_haste_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_10_haste_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 12)
    assert (p2.hp == 9)


def test_spell_10_haste_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_10_haste_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 9)
    assert (p2.hp == 9)


def test_spell_10_haste_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_10_haste_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 12)
    assert (p2.hp == 9)


def test_spell_10_haste_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_10_haste_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 9)
    assert (p2.hp == 12)


def test_spell_10_haste_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_10_haste_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 9)
    assert (p2.hp == 9)


def test_spell_10_haste_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_10_haste_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == -1)
    assert (p2.hp == 9)
    assert (p1.is_alive == 0)
    m1 = match_data.get_monster_by_id(101)
    assert (m1.is_alive == 1)


def test_spell_10_haste_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_10_haste_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 0)
    assert (p2.is_alive == 0)
    m1 = match_data.get_monster_by_id(101)
    assert (m1.is_alive == 1)


def test_spell_10_haste_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_10_haste_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 9)
    assert (p2.hp == 9)


def test_spell_10_haste_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_10_haste_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 12)
    assert (p2.hp == 9)


def test_spell_10_haste_J_mindspells(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_10_haste_J_mindspells.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 14)
    assert (p2.hp == 12)

# Time Stop


def test_spell_11_timestop_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_11_timestop_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_11_timestop_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_11_timestop_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_11_timestop_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_11_timestop_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 14)
    assert (p2.affected_by_pshield(match_data.current_turn) > 0)


def test_spell_11_timestop_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 14)
    assert (p2.affected_by_pshield(match_data.current_turn) > 0)


def test_spell_11_timestop_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_11_timestop_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_11_timestop_J_pattern(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_J_pattern.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 14)
    assert (p2.affected_by_pshield(match_data.current_turn) > 0)


def test_spell_11_timestop_K_invis_end_antispell(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_K_invis_end_antispell.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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


def test_spell_11_timestop_L_counter_antispell(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_11_timestop_L_counter_antispell.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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


# Protection


def test_spell_12_protection_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_12_protection_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_pshield(match_data.current_turn) == 1)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)


def test_spell_12_protection_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_12_protection_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 14)
    assert (p2.hp == 15)
    assert (p1.affected_by_pshield(match_data.current_turn) == 0)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)


def test_spell_12_protection_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_12_protection_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_pshield(match_data.current_turn) == 1)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)


def test_spell_12_protection_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_12_protection_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 14)
    assert (p2.hp == 15)
    assert (p1.affected_by_pshield(match_data.current_turn) == 0)
    assert (p2.affected_by_pshield(match_data.current_turn) == 1)


def test_spell_12_protection_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_12_protection_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 14)
    assert (p2.hp == 15)
    assert (p1.affected_by_pshield(match_data.current_turn) == 0)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)


def test_spell_12_protection_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_12_protection_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 14)
    assert (p2.hp == 15)
    assert (p1.affected_by_pshield(match_data.current_turn) == 0)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)
    assert (m1.affected_by_pshield(match_data.current_turn) == 1)


def test_spell_12_protection_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_12_protection_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 14)
    assert (p2.hp == 15)
    assert (p1.affected_by_pshield(match_data.current_turn) == 0)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)
    assert (m1.affected_by_pshield(match_data.current_turn) == 1)


def test_spell_12_protection_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_12_protection_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_pshield(match_data.current_turn) == 0)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)


def test_spell_12_protection_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_12_protection_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_pshield(match_data.current_turn) == 1)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)

# Resist Heat


def test_spell_13_resistheat_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_13_resistheat_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 0)


def test_spell_13_resistheat_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_13_resistheat_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 0)


def test_spell_13_resistheat_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_13_resistheat_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 0)


def test_spell_13_resistheat_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_13_resistheat_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_13_resistheat_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_13_resistheat_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 0)


def test_spell_13_resistheat_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_13_resistheat_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 0)
    assert (m1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_13_resistheat_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_13_resistheat_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 0)
    assert (m1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_13_resistheat_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_13_resistheat_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 0)


def test_spell_13_resistheat_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_13_resistheat_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 0)


def test_spell_13_resistheat_J_fireelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_13_resistheat_J_fireelem.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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


def test_spell_14_resistcold_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_14_resistcold_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_cold_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_cold_permanent(match_data.current_turn) == 0)


def test_spell_14_resistcold_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_14_resistcold_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_cold_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_cold_permanent(match_data.current_turn) == 0)


def test_spell_14_resistcold_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_14_resistcold_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_cold_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_cold_permanent(match_data.current_turn) == 0)


def test_spell_14_resistcold_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_14_resistcold_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_cold_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_cold_permanent(match_data.current_turn) == 1)


def test_spell_14_resistcold_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_14_resistcold_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_cold_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_cold_permanent(match_data.current_turn) == 0)


def test_spell_14_resistcold_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_14_resistcold_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_cold_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_cold_permanent(match_data.current_turn) == 0)
    assert (m1.affected_by_resist_cold_permanent(match_data.current_turn) == 1)


def test_spell_14_resistcold_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_14_resistcold_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_cold_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_cold_permanent(match_data.current_turn) == 0)
    assert (m1.affected_by_resist_cold_permanent(match_data.current_turn) == 1)


def test_spell_14_resistcold_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_14_resistcold_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_cold_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_cold_permanent(match_data.current_turn) == 0)


def test_spell_14_resistcold_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_14_resistcold_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (p1.affected_by_resist_cold_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_cold_permanent(match_data.current_turn) == 0)


def test_spell_14_resistcold_J_iceelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_14_resistcold_J_iceelem.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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


def test_spell_15_paralysis_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_15_paralysis_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'F')
    assert (p1gRH == 'W')
    assert (p2gLH == 'P')
    assert (p2gRH == 'W')


def test_spell_15_paralysis_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_15_paralysis_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'F')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_15_paralysis_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_15_paralysis_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'F')
    assert (p1gRH == 'P')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_15_paralysis_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_15_paralysis_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'F')
    assert (p1gRH == 'W')
    assert (p2gLH == 'P')
    assert (p2gRH == 'W')


def test_spell_15_paralysis_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_15_paralysis_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'F')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_15_paralysis_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_15_paralysis_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'F')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_15_paralysis_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_15_paralysis_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'F')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_15_paralysis_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_15_paralysis_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'F')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_15_paralysis_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_15_paralysis_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'C')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')

# Amnesia


def test_spell_16_amnesia_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_16_amnesia_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'S')
    assert (p2gRH == 'S')


def test_spell_16_amnesia_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_16_amnesia_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'F')
    assert (p2gRH == 'F')


def test_spell_16_amnesia_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_16_amnesia_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'S')
    assert (p2gLH == 'F')
    assert (p2gRH == 'F')


def test_spell_16_amnesia_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_16_amnesia_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'S')
    assert (p2gRH == 'S')


def test_spell_16_amnesia_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_16_amnesia_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'F')
    assert (p2gRH == 'F')


def test_spell_16_amnesia_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_16_amnesia_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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


def test_spell_16_amnesia_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_16_amnesia_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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


def test_spell_16_amnesia_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_16_amnesia_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'F')
    assert (p2gRH == 'F')


def test_spell_16_amnesia_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_16_amnesia_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'S')
    assert (p2gLH == 'F')
    assert (p2gRH == 'F')

# Fear


def test_spell_17_fear_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_17_fear_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_17_fear_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_17_fear_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'F')
    assert (p2gRH == 'F')


def test_spell_17_fear_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_17_fear_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'W')
    assert (p1gRH == 'W')
    assert (p2gLH == 'F')
    assert (p2gRH == 'F')


def test_spell_17_fear_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_17_fear_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_17_fear_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_17_fear_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'F')
    assert (p2gRH == 'F')


def test_spell_17_fear_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_17_fear_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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


def test_spell_17_fear_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_17_fear_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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


def test_spell_17_fear_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_17_fear_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'F')
    assert (p2gRH == 'F')


def test_spell_17_fear_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_17_fear_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'W')
    assert (p1gRH == 'W')
    assert (p2gLH == 'F')
    assert (p2gRH == 'F')

# Maladroitness


def test_spell_18_maladroitness_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_18_maladroitness_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'S')
    assert (p2gRH == 'W')


def test_spell_18_maladroitness_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'F')
    assert (p1gRH == 'F')
    assert (p2gLH == 'S')
    assert (p2gRH == 'W')


def test_spell_18_maladroitness_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_18_maladroitness_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'S')
    assert (p2gRH == 'W')


def test_spell_18_maladroitness_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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


def test_spell_18_maladroitness_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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


def test_spell_18_maladroitness_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'S')
    assert (p1gRH == 'F')
    assert (p2gLH == 'S')
    assert (p2gRH == 'W')


def test_spell_18_maladroitness_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_18_maladroitness_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'F')
    assert (p1gRH == 'F')
    assert (p2gLH == 'S')
    assert (p2gRH == 'W')

# Charm Monster


def test_spell_19_charmmonster_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_19_charmmonster_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)


def test_spell_19_charmmonster_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_19_charmmonster_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)


def test_spell_19_charmmonster_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_19_charmmonster_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)


def test_spell_19_charmmonster_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_19_charmmonster_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)


def test_spell_19_charmmonster_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_19_charmmonster_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)


def test_spell_19_charmmonster_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_19_charmmonster_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    m1 = match_data.get_monster_by_id(101)
    assert (m1.controller_id == 1)


def test_spell_19_charmmonster_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_19_charmmonster_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    m1 = match_data.get_monster_by_id(101)
    assert (m1.controller_id == 1)


def test_spell_19_charmmonster_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_19_charmmonster_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)


def test_spell_19_charmmonster_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_19_charmmonster_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)

# Charm Person


def test_spell_20_charmperson_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_20_charmperson_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'W')
    assert (p1gRH == 'W')
    assert (p2gLH == '-')
    assert (p2gRH == 'W')


def test_spell_20_charmperson_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_20_charmperson_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'W')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_20_charmperson_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_20_charmperson_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'F')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_20_charmperson_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_20_charmperson_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'W')
    assert (p1gRH == 'W')
    assert (p2gLH == '-')
    assert (p2gRH == 'W')


def test_spell_20_charmperson_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_20_charmperson_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'W')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_20_charmperson_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_20_charmperson_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'W')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_20_charmperson_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_20_charmperson_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'W')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_20_charmperson_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_20_charmperson_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'W')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_20_charmperson_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_20_charmperson_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == '-')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_20_charmperson_J_samegestures(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_20_charmperson_J_samegestures.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'W')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')

# Disease


def test_spell_21_disease_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_21_disease_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 0)
    assert (p1.affected_by_disease(match_data.current_turn) == 0)
    assert (p2.affected_by_disease(match_data.current_turn) == 1)


def test_spell_21_disease_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_21_disease_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_disease(match_data.current_turn) == 0)
    assert (p2.affected_by_disease(match_data.current_turn) == 0)


def test_spell_21_disease_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_21_disease_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 0)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_disease(match_data.current_turn) == 1)
    assert (p2.affected_by_disease(match_data.current_turn) == 0)


def test_spell_21_disease_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_21_disease_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 0)
    assert (p1.affected_by_disease(match_data.current_turn) == 0)
    assert (p2.affected_by_disease(match_data.current_turn) == 1)


def test_spell_21_disease_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_21_disease_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_disease(match_data.current_turn) == 0)
    assert (p2.affected_by_disease(match_data.current_turn) == 0)


def test_spell_21_disease_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_21_disease_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_disease(match_data.current_turn) == 0)
    assert (p2.affected_by_disease(match_data.current_turn) == 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_21_disease_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_21_disease_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_disease(match_data.current_turn) == 0)
    assert (p2.affected_by_disease(match_data.current_turn) == 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_21_disease_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_21_disease_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_disease(match_data.current_turn) == 0)
    assert (p2.affected_by_disease(match_data.current_turn) == 0)


def test_spell_21_disease_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_21_disease_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 0)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_disease(match_data.current_turn) == 1)
    assert (p2.affected_by_disease(match_data.current_turn) == 0)


def test_spell_21_disease_J_cures(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_21_disease_J_cures.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_disease(match_data.current_turn) == 0)
    assert (p2.affected_by_disease(match_data.current_turn) == 0)

# Poison


def test_spell_22_poison_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_22_poison_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 0)
    assert (p1.affected_by_poison(match_data.current_turn) == 0)
    assert (p2.affected_by_poison(match_data.current_turn) == 1)


def test_spell_22_poison_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_22_poison_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_poison(match_data.current_turn) == 0)
    assert (p2.affected_by_poison(match_data.current_turn) == 0)


def test_spell_22_poison_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_22_poison_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 0)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_poison(match_data.current_turn) == 1)
    assert (p2.affected_by_poison(match_data.current_turn) == 0)


def test_spell_22_poison_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_22_poison_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 0)
    assert (p1.affected_by_poison(match_data.current_turn) == 0)
    assert (p2.affected_by_poison(match_data.current_turn) == 1)


def test_spell_22_poison_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_22_poison_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_poison(match_data.current_turn) == 0)
    assert (p2.affected_by_poison(match_data.current_turn) == 0)


def test_spell_22_poison_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_22_poison_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_poison(match_data.current_turn) == 0)
    assert (p2.affected_by_poison(match_data.current_turn) == 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_22_poison_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_22_poison_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_poison(match_data.current_turn) == 0)
    assert (p2.affected_by_poison(match_data.current_turn) == 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_22_poison_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_22_poison_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_poison(match_data.current_turn) == 0)
    assert (p2.affected_by_poison(match_data.current_turn) == 0)


def test_spell_22_poison_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_22_poison_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 0)
    assert (p2.is_alive == 1)
    assert (p1.affected_by_poison(match_data.current_turn) == 1)
    assert (p2.affected_by_poison(match_data.current_turn) == 0)

# Cure Light Wounds


def test_spell_23_curelightwounds_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 16)
    assert (p2.hp == 15)


def test_spell_23_curelightwounds_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_23_curelightwounds_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 16)
    assert (p2.hp == 15)


def test_spell_23_curelightwounds_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 16)


def test_spell_23_curelightwounds_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_23_curelightwounds_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.hp == 2)


def test_spell_23_curelightwounds_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.hp == 2)


def test_spell_23_curelightwounds_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_23_curelightwounds_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 16)
    assert (p2.hp == 15)


def test_spell_23_curelightwounds_J_overheal(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_23_curelightwounds_J_overheal.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 16)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.hp == 2)

# Cure Heavy Wounds


def test_spell_24_cureheavywounds_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_24_cureheavywounds_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_24_cureheavywounds_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_24_cureheavywounds_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)


def test_spell_24_cureheavywounds_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_24_cureheavywounds_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_24_cureheavywounds_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_24_cureheavywounds_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_24_cureheavywounds_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_24_cureheavywounds_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)


def test_spell_24_cureheavywounds_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_24_cureheavywounds_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)
    assert (m1.hp == 0)


def test_spell_24_cureheavywounds_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_24_cureheavywounds_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)
    assert (m1.hp == 0)


def test_spell_24_cureheavywounds_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_24_cureheavywounds_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)


def test_spell_24_cureheavywounds_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_24_cureheavywounds_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_24_cureheavywounds_J_overheal(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_24_cureheavywounds_J_overheal.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 16)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.hp == 2)

# Anti-Spell


def test_spell_25_antispell_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == '-')
    assert (p2gRH == '-')


def test_spell_25_antispell_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_25_antispell_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == '-')
    assert (p1gRH == '-')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_25_antispell_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == '-')
    assert (p2gRH == '-')


def test_spell_25_antispell_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_25_antispell_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_25_antispell_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_25_antispell_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == 'P')
    assert (p1gRH == 'W')
    assert (p2gLH == 'S')
    assert (p2gRH == 'W')


def test_spell_25_antispell_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert (p1gLH == '-')
    assert (p1gRH == '-')
    assert (p2gLH == 'W')
    assert (p2gRH == 'W')


def test_spell_25_antispell_J_surrender(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_25_antispell_J_surrender.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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


def test_spell_26_blindness_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_26_blindness_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_26_blindness_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_26_blindness_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)


def test_spell_26_blindness_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_26_blindness_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)


def test_spell_26_blindness_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_26_blindness_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_26_blindness_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_26_blindness_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)


def test_spell_26_blindness_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_26_blindness_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_26_blindness_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_26_blindness_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_26_blindness_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_26_blindness_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)


def test_spell_26_blindness_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_26_blindness_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_26_blindness_J_pattern(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_26_blindness_J_pattern.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)

# Invisibility


def test_spell_27_invisibility_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_27_invisibility_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_27_invisibility_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_27_invisibility_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 15)


def test_spell_27_invisibility_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_27_invisibility_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_27_invisibility_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_27_invisibility_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 15)


def test_spell_27_invisibility_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_27_invisibility_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 15)


def test_spell_27_invisibility_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_27_invisibility_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_27_invisibility_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_27_invisibility_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 12)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_27_invisibility_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_27_invisibility_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 13)
    assert (p2.hp == 15)


def test_spell_27_invisibility_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_27_invisibility_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 13)

# Permanency


def test_spell_28_permanency_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.affected_by_pshield_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)


def test_spell_28_permanency_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.affected_by_pshield(match_data.current_turn) == 1)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)


def test_spell_28_permanency_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.affected_by_pshield_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)


def test_spell_28_permanency_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.affected_by_pshield(match_data.current_turn) == 1)
    assert (p2.affected_by_pshield_permanent(match_data.current_turn) == 1)


def test_spell_28_permanency_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.affected_by_pshield(match_data.current_turn) == 1)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)


def test_spell_28_permanency_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.affected_by_pshield(match_data.current_turn) == 1)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.affected_by_pshield(match_data.current_turn) == 0)


def test_spell_28_permanency_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.affected_by_pshield(match_data.current_turn) == 1)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.affected_by_pshield(match_data.current_turn) == 0)


def test_spell_28_permanency_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.affected_by_pshield(match_data.current_turn) == 1)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)


def test_spell_28_permanency_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.affected_by_pshield_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_pshield(match_data.current_turn) == 0)


def test_spell_28_permanency_J_dualhand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_J_dualhand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.affected_by_haste_permanent(match_data.current_turn) == 1)


def test_spell_28_permanency_K_amnesia(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_K_amnesia.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p2.affected_by_amnesia_permanent(match_data.current_turn) == 1)
    respect_antispell = 1
    assert (match_data.get_gesture_filtered(p2.id, 8, 1, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 8, 2, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 9, 1, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 9, 2, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 10, 1, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 10, 2, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 11, 1, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 11, 2, respect_antispell) == 'W')


def test_spell_28_permanency_L_fear(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_L_fear.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p2.affected_by_fear_permanent(match_data.current_turn) == 1)
    respect_antispell = 1
    assert (match_data.get_gesture_filtered(p2.id, 8, 1, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 8, 2, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 9, 1, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 9, 2, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 10, 1, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 10, 2, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 11, 1, respect_antispell) == '>')
    assert (match_data.get_gesture_filtered(p2.id, 11, 2, respect_antispell) == 'P')


def test_spell_28_permanency_M_maladroitness(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_M_maladroitness.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p2.affected_by_maladroitness_permanent(match_data.current_turn) == 1)
    respect_antispell = 1
    assert (match_data.get_gesture_filtered(p2.id, 8, 1, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 8, 2, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 9, 1, respect_antispell) == 'D')
    assert (match_data.get_gesture_filtered(p2.id, 9, 2, respect_antispell) == 'D')
    assert (match_data.get_gesture_filtered(p2.id, 10, 1, respect_antispell) == 'S')
    assert (match_data.get_gesture_filtered(p2.id, 10, 2, respect_antispell) == 'S')
    assert (match_data.get_gesture_filtered(p2.id, 11, 1, respect_antispell) == 'F')
    assert (match_data.get_gesture_filtered(p2.id, 11, 2, respect_antispell) == 'F')


def test_spell_28_permanency_N_charm_person(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_N_charmperson.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p2.affected_by_charm_person_permanent(match_data.current_turn) == 1)
    respect_antispell = 1
    assert (match_data.get_gesture_filtered(p2.id, 8, 1, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 8, 2, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 9, 1, respect_antispell) == '-')
    assert (match_data.get_gesture_filtered(p2.id, 9, 2, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 10, 1, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 10, 2, respect_antispell) == '-')
    assert (match_data.get_gesture_filtered(p2.id, 11, 1, respect_antispell) == '-')
    assert (match_data.get_gesture_filtered(p2.id, 11, 2, respect_antispell) == 'W')


def test_spell_28_permanency_O_paralysis(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_O_paralysis.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p2.affected_by_paralysis_permanent(match_data.current_turn) == 1)
    respect_antispell = 1
    assert (match_data.get_gesture_filtered(p2.id, 8, 1, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 8, 2, respect_antispell) == 'W')
    assert (match_data.get_gesture_filtered(p2.id, 9, 1, respect_antispell) == 'P')
    assert (match_data.get_gesture_filtered(p2.id, 9, 2, respect_antispell) == 'S')
    assert (match_data.get_gesture_filtered(p2.id, 10, 1, respect_antispell) == 'P')
    assert (match_data.get_gesture_filtered(p2.id, 10, 2, respect_antispell) == 'F')
    assert (match_data.get_gesture_filtered(p2.id, 11, 1, respect_antispell) == 'P')
    assert (match_data.get_gesture_filtered(p2.id, 11, 2, respect_antispell) == 'D')


def test_spell_28_permanency_P_invis_blind(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_28_permanency_P_invis_blind.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
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


# Delay Effect


def test_spell_29_delayeffect_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_29_delayeffect_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 13)


def test_spell_29_delayeffect_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_29_delayeffect_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_29_delayeffect_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_29_delayeffect_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_29_delayeffect_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_29_delayeffect_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_29_delayeffect_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_29_delayeffect_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_29_delayeffect_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_29_delayeffect_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_29_delayeffect_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_29_delayeffect_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_29_delayeffect_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_29_delayeffect_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_29_delayeffect_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_29_delayeffect_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 13)


def test_spell_29_delayeffect_J_multisummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_29_delayeffect_J_multisummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 13)
    m1 = match_data.get_monster_by_id(101, 0)
    m2 = match_data.get_monster_by_id(102, 0)
    assert (m1.is_alive == 1)
    assert (m2.is_alive == 0)


def test_spell_29_delayeffect_K_dualhand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_29_delayeffect_K_dualhand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 14)

# Remove Enchantment


def test_spell_30_removeenchantment_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_30_removeenchantment_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 0)


def test_spell_30_removeenchantment_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_30_removeenchantment_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_30_removeenchantment_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_30_removeenchantment_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_30_removeenchantment_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_30_removeenchantment_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 0)


def test_spell_30_removeenchantment_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_30_removeenchantment_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_30_removeenchantment_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_30_removeenchantment_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p1.hp == 15)
    assert (p2.hp == 14)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_30_removeenchantment_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_30_removeenchantment_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_30_removeenchantment_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_30_removeenchantment_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 1)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)


def test_spell_30_removeenchantment_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_30_removeenchantment_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.affected_by_resist_heat_permanent(match_data.current_turn) == 0)
    assert (p2.affected_by_resist_heat_permanent(match_data.current_turn) == 1)

# Shield


def test_spell_31_shield_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_31_shield_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_31_shield_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_31_shield_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 14)
    assert (p2.hp == 15)


def test_spell_31_shield_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_31_shield_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_31_shield_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_31_shield_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 14)
    assert (p2.hp == 15)


def test_spell_31_shield_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_31_shield_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 14)
    assert (p2.hp == 15)


def test_spell_31_shield_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_31_shield_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == 1)
    assert (m1.is_alive == 1)


def test_spell_31_shield_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_31_shield_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == 1)
    assert (m1.is_alive == 1)


def test_spell_31_shield_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_31_shield_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_31_shield_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_31_shield_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)

# Magic Missile


def test_spell_32_magicmissile_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_32_magicmissile_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 14)


def test_spell_32_magicmissile_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_32_magicmissile_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_32_magicmissile_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_32_magicmissile_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 14)
    assert (p2.hp == 15)


def test_spell_32_magicmissile_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_32_magicmissile_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 14)


def test_spell_32_magicmissile_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_32_magicmissile_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_32_magicmissile_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_32_magicmissile_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == 0)
    assert (m1.is_alive == 0)


def test_spell_32_magicmissile_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_32_magicmissile_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == 0)
    assert (m1.is_alive == 0)


def test_spell_32_magicmissile_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_32_magicmissile_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 14)
    assert (p2.hp == 15)


def test_spell_32_magicmissile_J_shielded(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_32_magicmissile_J_shielded.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)

# Cause Light Wounds


def test_spell_33_causelightwounds_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_33_causelightwounds_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 13)


def test_spell_33_causelightwounds_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_33_causelightwounds_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_33_causelightwounds_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_33_causelightwounds_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 13)
    assert (p2.hp == 15)


def test_spell_33_causelightwounds_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_33_causelightwounds_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 13)


def test_spell_33_causelightwounds_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_33_causelightwounds_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_33_causelightwounds_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_33_causelightwounds_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == -1)
    assert (m1.is_alive == 0)


def test_spell_33_causelightwounds_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_33_causelightwounds_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == -1)
    assert (m1.is_alive == 0)


def test_spell_33_causelightwounds_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_33_causelightwounds_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_33_causelightwounds_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_33_causelightwounds_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 13)
    assert (p2.hp == 15)

# Cause Heavy Wounds


def test_spell_34_causeheavywounds_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_34_causeheavywounds_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 12)


def test_spell_34_causeheavywounds_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_34_causeheavywounds_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_34_causeheavywounds_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_34_causeheavywounds_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 12)
    assert (p2.hp == 15)


def test_spell_34_causeheavywounds_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_34_causeheavywounds_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 12)


def test_spell_34_causeheavywounds_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_34_causeheavywounds_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_34_causeheavywounds_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_34_causeheavywounds_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == -2)
    assert (m1.is_alive == 0)


def test_spell_34_causeheavywounds_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_34_causeheavywounds_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == -2)
    assert (m1.is_alive == 0)


def test_spell_34_causeheavywounds_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_34_causeheavywounds_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_34_causeheavywounds_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_34_causeheavywounds_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 12)
    assert (p2.hp == 15)

# Fireball


def test_spell_35_fireball_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_35_fireball_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 10)


def test_spell_35_fireball_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_35_fireball_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_35_fireball_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_35_fireball_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 15)


def test_spell_35_fireball_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_35_fireball_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 10)


def test_spell_35_fireball_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_35_fireball_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_35_fireball_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_35_fireball_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == -4)
    assert (m1.is_alive == 0)


def test_spell_35_fireball_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_35_fireball_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == -4)
    assert (m1.is_alive == 0)


def test_spell_35_fireball_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_35_fireball_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_35_fireball_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_35_fireball_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 15)


def test_spell_35_fireball_J_resistheat(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_35_fireball_J_resistheat.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)

# Lightning Bolt


def test_spell_36_lightningbolt_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_36_lightningbolt_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 10)


def test_spell_36_lightningbolt_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_36_lightningbolt_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_36_lightningbolt_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_36_lightningbolt_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 15)


def test_spell_36_lightningbolt_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_36_lightningbolt_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 10)


def test_spell_36_lightningbolt_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_36_lightningbolt_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_36_lightningbolt_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_36_lightningbolt_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == -4)
    assert (m1.is_alive == 0)


def test_spell_36_lightningbolt_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_36_lightningbolt_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == -4)
    assert (m1.is_alive == 0)


def test_spell_36_lightningbolt_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_36_lightningbolt_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_36_lightningbolt_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_36_lightningbolt_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 15)

# Clap of Lightning


def test_spell_37_clapoflightning_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 10)


def test_spell_37_clapoflightning_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_37_clapoflightning_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 15)


def test_spell_37_clapoflightning_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 10)


def test_spell_37_clapoflightning_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_37_clapoflightning_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == -4)
    assert (m1.is_alive == 0)


def test_spell_37_clapoflightning_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    assert (m1.hp == -4)
    assert (m1.is_alive == 0)


def test_spell_37_clapoflightning_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_spell_37_clapoflightning_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 10)
    assert (p2.hp == 15)


def test_spell_37_clapoflightning_J_double(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_37_clapoflightning_J_double.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 10)

# Finger of Death


def test_spell_38_fingerofdeath_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_38_fingerofdeath_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 0)


def test_spell_38_fingerofdeath_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_38_fingerofdeath_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)


def test_spell_38_fingerofdeath_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_38_fingerofdeath_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 0)
    assert (p2.is_alive == 1)


def test_spell_38_fingerofdeath_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_38_fingerofdeath_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 0)


def test_spell_38_fingerofdeath_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_38_fingerofdeath_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)


def test_spell_38_fingerofdeath_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_38_fingerofdeath_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)
    assert (m1.is_alive == 0)


def test_spell_38_fingerofdeath_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_38_fingerofdeath_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 1)
    assert (m1.is_alive == 0)


def test_spell_38_fingerofdeath_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_38_fingerofdeath_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 0)


def test_spell_38_fingerofdeath_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_38_fingerofdeath_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 0)
    assert (p2.is_alive == 1)

# Fire Storm


def test_spell_39_firestorm_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_39_firestorm_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_39_firestorm_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_39_firestorm_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_39_firestorm_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_39_firestorm_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_39_firestorm_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_39_firestorm_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_39_firestorm_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_39_firestorm_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_39_firestorm_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_39_firestorm_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_39_firestorm_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_39_firestorm_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_39_firestorm_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_39_firestorm_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_39_firestorm_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_39_firestorm_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_39_firestorm_J_resistheat(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_39_firestorm_J_resistheat.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_39_firestorm_K_fireelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_39_firestorm_K_fireelem.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_39_firestorm_L_iceelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_39_firestorm_L_iceelem.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 1)


def test_spell_39_firestorm_M_icestorm(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_39_firestorm_M_icestorm.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 1)

# Ice Storm


def test_spell_40_icestorm_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_40_icestorm_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_40_icestorm_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_40_icestorm_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_40_icestorm_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_40_icestorm_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_40_icestorm_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_40_icestorm_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_40_icestorm_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_40_icestorm_J_resistcold(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_J_resistcold.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_40_icestorm_K_iceelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_K_iceelem.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 10)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_spell_40_icestorm_L_fireelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_L_fireelem.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 1)


def test_spell_40_icestorm_M_fireball(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_spell_40_icestorm_M_fireball.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 1)


# Stab


def test_action_01_stab_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_action_01_stab_A_deftarget.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 14)


def test_action_01_stab_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_action_01_stab_B_nobody.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_action_01_stab_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_action_01_stab_C_self.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 14)
    assert (p2.hp == 15)


def test_action_01_stab_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_action_01_stab_D_oppo.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 14)


def test_action_01_stab_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_action_01_stab_E_hand.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_action_01_stab_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_action_01_stab_F_newsummon.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)
    assert (m1.hp == 0)


def test_action_01_stab_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_action_01_stab_G_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)
    assert (m1.hp == 0)


def test_action_01_stab_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_action_01_stab_H_countered.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)


def test_action_01_stab_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_action_01_stab_I_mirrored.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 14)


def test_action_01_stab_J_shielded(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_action_01_stab_J_shielded.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.hp == 15)
    assert (p2.hp == 15)

# Surrender


def test_action_02_surrender(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_action_02_surrender.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 0)
    assert (p2.is_alive == 1)
    assert (p1.hp == 15)
    assert (p2.hp == 15)

# Suicide


def test_action_03_suicide(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_action_03_suicide.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert (p1.is_alive == 1)
    assert (p2.is_alive == 0)


def test_special_spell_selection(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_special_spell_selection.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101)
    assert (m1.monster_type == 2)


def test_special_mirror_para_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_special_mirror_para_monster.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    m1 = match_data.get_monster_by_id(101)
    assert (m1.monster_type == 1)
    respect_antispell = 1
    assert (match_data.get_gesture_filtered(p2.id, 6, 1, respect_antispell) == 'C')


def test_special_double_delay(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_special_double_delay.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 15)
    assert (p2.hp == 15)
    respect_antispell = 1
    assert (match_data.get_gesture_filtered(p2.id, 11, 1, respect_antispell) == '-')
    assert (match_data.get_gesture_filtered(p2.id, 11, 2, respect_antispell) == '-')
    assert (p1.states[match_data.current_turn]['delayed_spell'] is not None)


def test_special_delay_corruption(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_special_delay_corruption.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 13)
    assert (p2.hp == 15)
    respect_antispell = 1
    assert (match_data.get_gesture_filtered(p2.id, 11, 1, respect_antispell) == '-')
    assert (match_data.get_gesture_filtered(p2.id, 11, 2, respect_antispell) == '-')


def test_special_delay_dispel_and_monsters(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_special_delay_dispel_and_monsters.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert (p1.hp == 14)
    assert (p2.hp == 13)
    m1 = match_data.get_monster_by_id(101, 0)
    assert (m1.is_alive == 0)


def test_special_summongoblin_horde(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_special_summongoblin_horde.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    monster_names = []
    for m_id in match_data.get_ids_monsters():
        monster_names.append(match_data.get_name_by_id(m_id))
    assert (len(monster_names) == 16)
    assert (len(set(monster_names)) == 16)


def test_special_seeded_random_targets(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):

    match_json_filename = os.path.join('tests_warlocks', 'test_special_seeded_random_targets.json')
    match_data = run_test(match_json_filename, silent_run, available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    p3 = match_data.get_participant_by_id(3)
    p4 = match_data.get_participant_by_id(4)
    assert (p1.hp == 15)
    assert (p2.hp == 14)
    assert (p3.hp == 15)
    assert (p4.hp == 14)


def run_warlocks_attack_seed_test(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):
    """Test that random attack target is preserved by seed."""
    test_special_seeded_random_targets(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_special_seeded_random_targets(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_special_seeded_random_targets(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_special_seeded_random_targets(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_special_seeded_random_targets(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_special_seeded_random_targets(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_special_seeded_random_targets(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_special_seeded_random_targets(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_special_seeded_random_targets(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_special_seeded_random_targets(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_special_seeded_random_targets(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)


def run_warlocks_tests(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run):
    """Run all specific tests."""
    # Dispel Magic
    test_spell_01_dispelmagic_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_01_dispelmagic_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_01_dispelmagic_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_01_dispelmagic_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_01_dispelmagic_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_01_dispelmagic_F_remove_bug(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_01_dispelmagic_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_01_dispelmagic_H_visibility(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # CounterSpell
    test_spell_02_counterspell_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_02_counterspell_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_02_counterspell_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_02_counterspell_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_02_counterspell_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_02_counterspell_J_pattern(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Magic Mirror
    test_spell_03_magicmirror_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_03_magicmirror_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_03_magicmirror_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_03_magicmirror_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_03_magicmirror_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_03_magicmirror_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_03_magicmirror_I_double(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Summon Goblin, Ogre, Troll, Giant
    test_spell_04_summongoblin_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_04_summongoblin_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_04_summongoblin_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_04_summongoblin_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_04_summongoblin_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_04_summongoblin_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_04_summongoblin_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_05_summonogre_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_06_summontroll_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_07_summongiant_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Summon Fire Elemental, Ice Elemental
    test_spell_08_fireelemental_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_08_fireelemental_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_08_fireelemental_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_08_fireelemental_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_08_fireelemental_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_08_fireelemental_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_08_fireelemental_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_08_fireelemental_J_merge(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_09_iceelemental_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_09_iceelemental_J_merge(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Haste
    test_spell_10_haste_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_10_haste_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_10_haste_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_10_haste_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_10_haste_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_10_haste_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_10_haste_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_10_haste_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_10_haste_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_10_haste_J_mindspells(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Time Stop
    test_spell_11_timestop_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_11_timestop_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_11_timestop_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_11_timestop_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_11_timestop_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_11_timestop_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_11_timestop_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_11_timestop_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_11_timestop_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_11_timestop_J_pattern(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_11_timestop_K_invis_end_antispell(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_11_timestop_L_counter_antispell(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Protection
    test_spell_12_protection_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_12_protection_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_12_protection_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_12_protection_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_12_protection_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_12_protection_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_12_protection_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_12_protection_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_12_protection_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Resist Heat
    test_spell_13_resistheat_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_13_resistheat_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_13_resistheat_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_13_resistheat_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_13_resistheat_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_13_resistheat_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_13_resistheat_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_13_resistheat_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_13_resistheat_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_13_resistheat_J_fireelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Resist Cold
    test_spell_14_resistcold_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_14_resistcold_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_14_resistcold_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_14_resistcold_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_14_resistcold_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_14_resistcold_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_14_resistcold_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_14_resistcold_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_14_resistcold_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_14_resistcold_J_iceelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Paralysis
    test_spell_15_paralysis_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_15_paralysis_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_15_paralysis_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_15_paralysis_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_15_paralysis_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_15_paralysis_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_15_paralysis_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_15_paralysis_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_15_paralysis_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Amnesia
    test_spell_16_amnesia_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_16_amnesia_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_16_amnesia_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_16_amnesia_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_16_amnesia_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_16_amnesia_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_16_amnesia_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_16_amnesia_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_16_amnesia_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Fear
    test_spell_17_fear_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_17_fear_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_17_fear_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_17_fear_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_17_fear_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_17_fear_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_17_fear_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_17_fear_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_17_fear_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Maladroitness
    test_spell_18_maladroitness_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_18_maladroitness_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_18_maladroitness_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_18_maladroitness_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_18_maladroitness_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_18_maladroitness_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_18_maladroitness_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_18_maladroitness_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_18_maladroitness_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Charm Monster
    test_spell_19_charmmonster_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_19_charmmonster_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_19_charmmonster_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_19_charmmonster_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_19_charmmonster_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_19_charmmonster_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_19_charmmonster_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_19_charmmonster_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_19_charmmonster_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Charm Person
    test_spell_20_charmperson_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_20_charmperson_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_20_charmperson_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_20_charmperson_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_20_charmperson_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_20_charmperson_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_20_charmperson_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_20_charmperson_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_20_charmperson_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_20_charmperson_J_samegestures(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Disease
    test_spell_21_disease_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_21_disease_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_21_disease_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_21_disease_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_21_disease_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_21_disease_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_21_disease_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_21_disease_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_21_disease_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_21_disease_J_cures(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Poison
    test_spell_22_poison_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_22_poison_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_22_poison_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_22_poison_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_22_poison_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_22_poison_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_22_poison_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_22_poison_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_22_poison_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Cure Light Wounds
    test_spell_23_curelightwounds_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_23_curelightwounds_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_23_curelightwounds_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_23_curelightwounds_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_23_curelightwounds_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_23_curelightwounds_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_23_curelightwounds_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_23_curelightwounds_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_23_curelightwounds_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_23_curelightwounds_J_overheal(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Cure Heavy Wounds
    test_spell_24_cureheavywounds_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_24_cureheavywounds_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_24_cureheavywounds_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_24_cureheavywounds_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_24_cureheavywounds_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_24_cureheavywounds_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_24_cureheavywounds_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_24_cureheavywounds_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_24_cureheavywounds_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_24_cureheavywounds_J_overheal(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Anti-Spell
    test_spell_25_antispell_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_25_antispell_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_25_antispell_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_25_antispell_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_25_antispell_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_25_antispell_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_25_antispell_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_25_antispell_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_25_antispell_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_25_antispell_J_surrender(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Blindness
    test_spell_26_blindness_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_26_blindness_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_26_blindness_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_26_blindness_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_26_blindness_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_26_blindness_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_26_blindness_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_26_blindness_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_26_blindness_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_26_blindness_J_pattern(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Invisibility
    test_spell_27_invisibility_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_27_invisibility_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_27_invisibility_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_27_invisibility_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_27_invisibility_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_27_invisibility_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_27_invisibility_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_27_invisibility_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_27_invisibility_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Permanency
    test_spell_28_permanency_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_J_dualhand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_K_amnesia(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_L_fear(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_M_maladroitness(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_N_charm_person(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_O_paralysis(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_28_permanency_P_invis_blind(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Delay Effect
    test_spell_29_delayeffect_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_29_delayeffect_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_29_delayeffect_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_29_delayeffect_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_29_delayeffect_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_29_delayeffect_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_29_delayeffect_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_29_delayeffect_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_29_delayeffect_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_29_delayeffect_J_multisummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_29_delayeffect_K_dualhand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Remove Enchantment
    test_spell_30_removeenchantment_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_30_removeenchantment_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_30_removeenchantment_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_30_removeenchantment_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_30_removeenchantment_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_30_removeenchantment_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_30_removeenchantment_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_30_removeenchantment_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_30_removeenchantment_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Shield
    test_spell_31_shield_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_31_shield_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_31_shield_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_31_shield_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_31_shield_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_31_shield_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_31_shield_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_31_shield_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_31_shield_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Magic Missle
    test_spell_32_magicmissile_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_32_magicmissile_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_32_magicmissile_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_32_magicmissile_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_32_magicmissile_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_32_magicmissile_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_32_magicmissile_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_32_magicmissile_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_32_magicmissile_J_shielded(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Cause Light Wounds
    test_spell_33_causelightwounds_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_33_causelightwounds_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_33_causelightwounds_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_33_causelightwounds_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_33_causelightwounds_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_33_causelightwounds_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_33_causelightwounds_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_33_causelightwounds_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_33_causelightwounds_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Cause Heavy Wounds
    test_spell_34_causeheavywounds_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_34_causeheavywounds_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_34_causeheavywounds_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_34_causeheavywounds_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_34_causeheavywounds_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_34_causeheavywounds_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_34_causeheavywounds_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_34_causeheavywounds_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_34_causeheavywounds_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Fireball
    test_spell_35_fireball_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_35_fireball_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_35_fireball_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_35_fireball_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_35_fireball_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_35_fireball_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_35_fireball_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_35_fireball_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_35_fireball_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_35_fireball_J_resistheat(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Lightning Bolt
    test_spell_36_lightningbolt_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_36_lightningbolt_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_36_lightningbolt_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_36_lightningbolt_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_36_lightningbolt_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_36_lightningbolt_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_36_lightningbolt_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_36_lightningbolt_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_36_lightningbolt_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Clap of Lightning
    test_spell_37_clapoflightning_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_37_clapoflightning_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_37_clapoflightning_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_37_clapoflightning_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_37_clapoflightning_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_37_clapoflightning_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_37_clapoflightning_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_37_clapoflightning_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_37_clapoflightning_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_37_clapoflightning_J_double(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Finger of Death
    test_spell_38_fingerofdeath_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_38_fingerofdeath_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_38_fingerofdeath_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_38_fingerofdeath_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_38_fingerofdeath_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_38_fingerofdeath_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_38_fingerofdeath_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_38_fingerofdeath_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_38_fingerofdeath_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Fire Storm
    test_spell_39_firestorm_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_39_firestorm_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_39_firestorm_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_39_firestorm_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_39_firestorm_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_39_firestorm_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_39_firestorm_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_39_firestorm_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_39_firestorm_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_39_firestorm_J_resistheat(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_39_firestorm_K_fireelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_39_firestorm_L_iceelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_39_firestorm_M_icestorm(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Ice Storm
    test_spell_40_icestorm_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_40_icestorm_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_40_icestorm_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_40_icestorm_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_40_icestorm_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_40_icestorm_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_40_icestorm_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_40_icestorm_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_40_icestorm_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_40_icestorm_J_resistcold(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_40_icestorm_K_iceelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_40_icestorm_L_fireelem(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_spell_40_icestorm_M_fireball(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Stab
    test_action_01_stab_A_deftarget(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_action_01_stab_B_nobody(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_action_01_stab_C_self(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_action_01_stab_D_oppo(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_action_01_stab_E_hand(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_action_01_stab_F_newsummon(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_action_01_stab_G_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_action_01_stab_H_countered(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_action_01_stab_I_mirrored(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
    test_action_01_stab_J_shielded(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Surrender

    test_action_02_surrender(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Suicide

    test_action_03_suicide(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    # Spell selection

    test_special_spell_selection(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    test_special_mirror_para_monster(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    test_special_double_delay(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    test_special_delay_corruption(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    test_special_delay_dispel_and_monsters(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)

    test_special_summongoblin_horde(available_spellbooks, match_spellbook, match_id, match_players_init, lang_code, def_pov_id, silent_run)
