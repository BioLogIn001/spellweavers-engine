import sys
import os
from spellweavers_main import tmp_parse_json_game


def run_test(match_json_filename, silent_run):

    print('Testing', match_json_filename)
    if silent_run == 1:
        sys.stdout = open(os.devnull, 'w')
    match_data = tmp_parse_json_game(match_id, available_spellbooks[match_spellbook],
                                     lang_code, match_players_init, match_json_filename)
    if silent_run == 1:
        sys.stdout = sys.__stdout__
    return match_data


def test_template(silent_run=1):

    match_json_filename = 'tests\\test_!template.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)

# Dispel Magic


def test_spell_01_dispelmagic_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_01_dispelmagic_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.is_alive == 0)


def test_spell_01_dispelmagic_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_01_dispelmagic_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 14)
    assert(p2.hp == 15)
    assert(m1.is_alive == 0)


def test_spell_01_dispelmagic_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_01_dispelmagic_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.is_alive == 0)


def test_spell_01_dispelmagic_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_01_dispelmagic_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 14)
    assert(p2.hp == 15)
    assert(m1.is_alive == 0)


def test_spell_01_dispelmagic_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_01_dispelmagic_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 14)
    assert(p2.hp == 15)
    assert(m1.is_alive == 0)


def test_spell_01_dispelmagic_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_01_dispelmagic_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 14)
    assert(p2.hp == 15)
    assert(m1.is_alive == 0)

# CounterSpell


def test_spell_02_counterspell_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_02_counterspell_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_02_counterspell_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_02_counterspell_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 13)
    assert(p2.hp == 15)


def test_spell_02_counterspell_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_02_counterspell_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_02_counterspell_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_02_counterspell_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_02_counterspell_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_02_counterspell_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.is_alive == 1)


def test_spell_02_counterspell_J_pattern(silent_run=1):

    match_json_filename = 'tests\\test_spell_02_counterspell_J_pattern.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)

# Magic Mirror


def test_spell_03_magicmirror_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_03_magicmirror_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 13)


def test_spell_03_magicmirror_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_03_magicmirror_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 13)
    assert(p2.hp == 15)


def test_spell_03_magicmirror_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_03_magicmirror_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 13)


def test_spell_03_magicmirror_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_03_magicmirror_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 13)
    assert(p2.hp == 15)


def test_spell_03_magicmirror_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_03_magicmirror_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 13)
    assert(m1.is_alive == 1)


def test_spell_03_magicmirror_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_03_magicmirror_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)

# Summon Goblin, Ogre, Troll, Giant


def test_spell_04_summongoblin_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_04_summongoblin_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 14)
    assert(m1.is_alive == 1)
    assert(m1.monster_type == 1)
    assert(m1.hp == 1)
    assert(m1.controller_id == 1)


def test_spell_04_summongoblin_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_04_summongoblin_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_04_summongoblin_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_04_summongoblin_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 14)
    assert(m1.is_alive == 1)
    assert(m1.monster_type == 1)
    assert(m1.hp == 1)
    assert(m1.controller_id == 1)


def test_spell_04_summongoblin_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_04_summongoblin_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 14)
    assert(p2.hp == 15)
    assert(m1.is_alive == 1)
    assert(m1.monster_type == 1)
    assert(m1.hp == 1)
    assert(m1.controller_id == 2)


def test_spell_04_summongoblin_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_04_summongoblin_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    m2 = match_data.get_monster_by_id(102, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 14)
    assert(m2.is_alive == 1)
    assert(m2.monster_type == 1)
    assert(m2.hp == 1)
    assert(m2.controller_id == 1)


def test_spell_04_summongoblin_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_04_summongoblin_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_04_summongoblin_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_04_summongoblin_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 14)
    assert(m1.is_alive == 1)
    assert(m1.monster_type == 1)
    assert(m1.hp == 1)
    assert(m1.controller_id == 1)


def test_spell_05_summonogre_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_05_summonogre_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 13)
    assert(m1.is_alive == 1)
    assert(m1.monster_type == 2)
    assert(m1.hp == 2)
    assert(m1.controller_id == 1)


def test_spell_06_summontroll_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_06_summontroll_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 12)
    assert(m1.is_alive == 1)
    assert(m1.monster_type == 3)
    assert(m1.hp == 3)
    assert(m1.controller_id == 1)


def test_spell_07_summongiant_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_07_summongiant_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 11)
    assert(m1.is_alive == 1)
    assert(m1.monster_type == 4)
    assert(m1.hp == 4)
    assert(m1.controller_id == 1)

# Summon Fire Elemental and Ice Elemental


def test_spell_08_fireelemental_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_08_fireelemental_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 12)
    assert(p2.hp == 12)
    assert(m1.is_alive == 1)
    assert(m1.monster_type == 5)
    assert(m1.hp == 3)


def test_spell_08_fireelemental_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_08_fireelemental_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 12)
    assert(p2.hp == 12)
    assert(m1.is_alive == 1)
    assert(m1.monster_type == 5)
    assert(m1.hp == 3)


def test_spell_08_fireelemental_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_08_fireelemental_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 12)
    assert(p2.hp == 12)
    assert(m1.is_alive == 1)
    assert(m1.monster_type == 5)
    assert(m1.hp == 3)


def test_spell_08_fireelemental_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_08_fireelemental_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 12)
    assert(p2.hp == 12)
    assert(m1.is_alive == 1)
    assert(m1.monster_type == 5)
    assert(m1.hp == 3)


def test_spell_08_fireelemental_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_08_fireelemental_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    m2 = match_data.get_monster_by_id(102, 0)
    assert(p1.hp == 12)
    assert(p2.hp == 12)
    assert(m1.is_alive == 0)
    assert(m1.hp == -2)
    assert(m2.is_alive == 1)
    assert(m2.monster_type == 5)
    assert(m2.hp == 3)


def test_spell_08_fireelemental_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_08_fireelemental_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 12)
    assert(p2.hp == 15)
    assert(m1.is_alive == 1)
    assert(m1.monster_type == 5)
    assert(m1.hp == 3)


def test_spell_08_fireelemental_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_08_fireelemental_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 12)
    assert(p2.hp == 12)
    assert(m1.is_alive == 1)
    assert(m1.monster_type == 5)
    assert(m1.hp == 3)


def test_spell_08_fireelemental_J_merge(silent_run=1):

    match_json_filename = 'tests\\test_spell_08_fireelemental_J_merge.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    m2 = match_data.get_monster_by_id(102, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.is_alive == 0)
    assert(m1.monster_type == 5)
    assert(m2.is_alive == 1)
    assert(m2.monster_type == 5)


def test_spell_09_iceelemental_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_09_iceelemental_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 12)
    assert(p2.hp == 12)
    assert(m1.is_alive == 1)
    assert(m1.monster_type == 6)
    assert(m1.hp == 3)


def test_spell_09_iceelemental_J_merge(silent_run=1):

    match_json_filename = 'tests\\test_spell_09_iceelemental_J_merge.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    m2 = match_data.get_monster_by_id(102, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.is_alive == 0)
    assert(m1.monster_type == 6)
    assert(m2.is_alive == 1)
    assert(m2.monster_type == 6)

# Haste


def test_spell_10_haste_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_10_haste_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 12)
    assert(p2.hp == 9)


def test_spell_10_haste_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_10_haste_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 9)
    assert(p2.hp == 9)


def test_spell_10_haste_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_10_haste_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 12)
    assert(p2.hp == 9)


def test_spell_10_haste_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_10_haste_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 9)
    assert(p2.hp == 12)


def test_spell_10_haste_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_10_haste_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 9)
    assert(p2.hp == 9)


def test_spell_10_haste_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_10_haste_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == -1)
    assert(p2.hp == 9)
    assert(p1.is_alive == 0)
    m1 = match_data.get_monster_by_id(101)
    assert(m1.is_alive == 1)


def test_spell_10_haste_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_10_haste_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 0)
    assert(p2.is_alive == 0)
    m1 = match_data.get_monster_by_id(101)
    assert(m1.is_alive == 1)


def test_spell_10_haste_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_10_haste_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 9)
    assert(p2.hp == 9)


def test_spell_10_haste_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_10_haste_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 12)
    assert(p2.hp == 9)


def test_spell_10_haste_J_mindspells(silent_run=1):

    match_json_filename = 'tests\\test_spell_10_haste_J_mindspells.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 14)
    assert(p2.hp == 12)

# Time Stop


def test_spell_11_timestop_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_11_timestop_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    assert(p1.affected_by_resist_heat() == 1)
    assert(p2.affected_by_resist_heat() == 1)


def test_spell_11_timestop_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_11_timestop_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_heat() == 1)
    assert(p2.affected_by_resist_heat() == 1)


def test_spell_11_timestop_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_11_timestop_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    assert(p1.affected_by_resist_heat() == 1)
    assert(p2.affected_by_resist_heat() == 1)


def test_spell_11_timestop_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_11_timestop_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    assert(p1.affected_by_resist_heat() == 1)
    assert(p2.affected_by_resist_heat() == 1)


def test_spell_11_timestop_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_11_timestop_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_heat() == 1)
    assert(p2.affected_by_resist_heat() == 1)


def test_spell_11_timestop_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_11_timestop_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 14)
    assert(p2.affected_by_pshield() > 0)


def test_spell_11_timestop_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_11_timestop_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 14)
    assert(p2.affected_by_pshield() > 0)


def test_spell_11_timestop_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_11_timestop_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_heat() == 1)
    assert(p2.affected_by_resist_heat() == 1)


def test_spell_11_timestop_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_11_timestop_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    assert(p1.affected_by_resist_heat() == 1)
    assert(p2.affected_by_resist_heat() == 1)


def test_spell_11_timestop_J_pattern(silent_run=1):

    match_json_filename = 'tests\\test_spell_11_timestop_J_pattern.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 14)
    assert(p2.affected_by_pshield() > 0)

# Protection


def test_spell_12_protection_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_12_protection_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_pshield() == 1)
    assert(p2.affected_by_pshield() == 0)


def test_spell_12_protection_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_12_protection_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 14)
    assert(p2.hp == 15)
    assert(p1.affected_by_pshield() == 0)
    assert(p2.affected_by_pshield() == 0)


def test_spell_12_protection_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_12_protection_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_pshield() == 1)
    assert(p2.affected_by_pshield() == 0)


def test_spell_12_protection_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_12_protection_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 14)
    assert(p2.hp == 15)
    assert(p1.affected_by_pshield() == 0)
    assert(p2.affected_by_pshield() == 1)


def test_spell_12_protection_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_12_protection_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 14)
    assert(p2.hp == 15)
    assert(p1.affected_by_pshield() == 0)
    assert(p2.affected_by_pshield() == 0)


def test_spell_12_protection_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_12_protection_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 14)
    assert(p2.hp == 15)
    assert(p1.affected_by_pshield() == 0)
    assert(p2.affected_by_pshield() == 0)
    assert(m1.affected_by_pshield() == 1)


def test_spell_12_protection_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_12_protection_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 14)
    assert(p2.hp == 15)
    assert(p1.affected_by_pshield() == 0)
    assert(p2.affected_by_pshield() == 0)
    assert(m1.affected_by_pshield() == 1)


def test_spell_12_protection_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_12_protection_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_pshield() == 0)
    assert(p2.affected_by_pshield() == 0)


def test_spell_12_protection_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_12_protection_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_pshield() == 1)
    assert(p2.affected_by_pshield() == 0)

# Resist Heat


def test_spell_13_resistheat_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_13_resistheat_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_heat() == 1)
    assert(p2.affected_by_resist_heat() == 0)


def test_spell_13_resistheat_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_13_resistheat_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_heat() == 0)
    assert(p2.affected_by_resist_heat() == 0)


def test_spell_13_resistheat_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_13_resistheat_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_heat() == 1)
    assert(p2.affected_by_resist_heat() == 0)


def test_spell_13_resistheat_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_13_resistheat_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_heat() == 0)
    assert(p2.affected_by_resist_heat() == 1)


def test_spell_13_resistheat_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_13_resistheat_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_heat() == 0)
    assert(p2.affected_by_resist_heat() == 0)


def test_spell_13_resistheat_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_13_resistheat_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_heat() == 0)
    assert(p2.affected_by_resist_heat() == 0)
    assert(m1.affected_by_resist_heat() == 1)


def test_spell_13_resistheat_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_13_resistheat_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_heat() == 0)
    assert(p2.affected_by_resist_heat() == 0)
    assert(m1.affected_by_resist_heat() == 1)


def test_spell_13_resistheat_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_13_resistheat_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_heat() == 0)
    assert(p2.affected_by_resist_heat() == 0)


def test_spell_13_resistheat_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_13_resistheat_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_heat() == 1)
    assert(p2.affected_by_resist_heat() == 0)


def test_spell_13_resistheat_J_fireelem(silent_run=1):

    match_json_filename = 'tests\\test_spell_13_resistheat_J_fireelem.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    m2 = match_data.get_monster_by_id(102, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_heat() == 0)
    assert(p2.affected_by_resist_heat() == 0)
    assert(m2.is_alive == 0)

# Resist Cold


def test_spell_14_resistcold_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_14_resistcold_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_cold() == 1)
    assert(p2.affected_by_resist_cold() == 0)


def test_spell_14_resistcold_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_14_resistcold_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_cold() == 0)
    assert(p2.affected_by_resist_cold() == 0)


def test_spell_14_resistcold_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_14_resistcold_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_cold() == 1)
    assert(p2.affected_by_resist_cold() == 0)


def test_spell_14_resistcold_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_14_resistcold_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_cold() == 0)
    assert(p2.affected_by_resist_cold() == 1)


def test_spell_14_resistcold_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_14_resistcold_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_cold() == 0)
    assert(p2.affected_by_resist_cold() == 0)


def test_spell_14_resistcold_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_14_resistcold_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_cold() == 0)
    assert(p2.affected_by_resist_cold() == 0)
    assert(m1.affected_by_resist_cold() == 1)


def test_spell_14_resistcold_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_14_resistcold_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_cold() == 0)
    assert(p2.affected_by_resist_cold() == 0)
    assert(m1.affected_by_resist_cold() == 1)


def test_spell_14_resistcold_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_14_resistcold_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_cold() == 0)
    assert(p2.affected_by_resist_cold() == 0)


def test_spell_14_resistcold_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_14_resistcold_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_cold() == 1)
    assert(p2.affected_by_resist_cold() == 0)


def test_spell_14_resistcold_J_iceelem(silent_run=1):

    match_json_filename = 'tests\\test_spell_14_resistcold_J_iceelem.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    m2 = match_data.get_monster_by_id(102, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(p1.affected_by_resist_cold() == 0)
    assert(p2.affected_by_resist_cold() == 0)
    assert(m2.is_alive == 0)

# Paralysis


def test_spell_15_paralysis_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_15_paralysis_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'F')
    assert(p1gRH == 'W')
    assert(p2gLH == 'P')
    assert(p2gRH == 'W')


def test_spell_15_paralysis_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_15_paralysis_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'F')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_15_paralysis_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_15_paralysis_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'F')
    assert(p1gRH == 'P')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_15_paralysis_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_15_paralysis_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'F')
    assert(p1gRH == 'W')
    assert(p2gLH == 'P')
    assert(p2gRH == 'W')


def test_spell_15_paralysis_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_15_paralysis_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'F')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_15_paralysis_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_15_paralysis_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'F')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_15_paralysis_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_15_paralysis_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'F')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_15_paralysis_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_15_paralysis_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'F')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_15_paralysis_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_15_paralysis_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'C')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')

# Amnesia


def test_spell_16_amnesia_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_16_amnesia_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'S')
    assert(p2gRH == 'S')


def test_spell_16_amnesia_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_16_amnesia_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'F')
    assert(p2gRH == 'F')


def test_spell_16_amnesia_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_16_amnesia_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'P')
    assert(p1gRH == 'S')
    assert(p2gLH == 'F')
    assert(p2gRH == 'F')


def test_spell_16_amnesia_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_16_amnesia_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'S')
    assert(p2gRH == 'S')


def test_spell_16_amnesia_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_16_amnesia_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'F')
    assert(p2gRH == 'F')


def test_spell_16_amnesia_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_16_amnesia_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'F')
    assert(p2gRH == 'F')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_16_amnesia_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_16_amnesia_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'F')
    assert(p2gRH == 'F')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_16_amnesia_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_16_amnesia_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'F')
    assert(p2gRH == 'F')


def test_spell_16_amnesia_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_16_amnesia_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'P')
    assert(p1gRH == 'S')
    assert(p2gLH == 'F')
    assert(p2gRH == 'F')

# Fear


def test_spell_17_fear_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_17_fear_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_17_fear_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_17_fear_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'F')
    assert(p2gRH == 'F')


def test_spell_17_fear_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_17_fear_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'W')
    assert(p1gRH == 'W')
    assert(p2gLH == 'F')
    assert(p2gRH == 'F')


def test_spell_17_fear_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_17_fear_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_17_fear_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_17_fear_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'F')
    assert(p2gRH == 'F')


def test_spell_17_fear_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_17_fear_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'F')
    assert(p2gRH == 'F')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_17_fear_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_17_fear_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'F')
    assert(p2gRH == 'F')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_17_fear_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_17_fear_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'F')
    assert(p2gRH == 'F')


def test_spell_17_fear_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_17_fear_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'W')
    assert(p1gRH == 'W')
    assert(p2gLH == 'F')
    assert(p2gRH == 'F')

# Maladroitness


def test_spell_18_maladroitness_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_18_maladroitness_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_18_maladroitness_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_18_maladroitness_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'S')
    assert(p2gRH == 'W')


def test_spell_18_maladroitness_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_18_maladroitness_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'F')
    assert(p1gRH == 'F')
    assert(p2gLH == 'S')
    assert(p2gRH == 'W')


def test_spell_18_maladroitness_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_18_maladroitness_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_18_maladroitness_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_18_maladroitness_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'S')
    assert(p2gRH == 'W')


def test_spell_18_maladroitness_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_18_maladroitness_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'S')
    assert(p2gRH == 'W')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_18_maladroitness_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_18_maladroitness_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'S')
    assert(p2gRH == 'W')
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_18_maladroitness_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_18_maladroitness_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'S')
    assert(p1gRH == 'F')
    assert(p2gLH == 'S')
    assert(p2gRH == 'W')


def test_spell_18_maladroitness_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_18_maladroitness_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'F')
    assert(p1gRH == 'F')
    assert(p2gLH == 'S')
    assert(p2gRH == 'W')

# Charm Monster


def test_spell_19_charmmonster_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_19_charmmonster_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)


def test_spell_19_charmmonster_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_19_charmmonster_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)


def test_spell_19_charmmonster_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_19_charmmonster_C_self.json'
    match_data = run_test(match_json_filename, silent_run)


def test_spell_19_charmmonster_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_19_charmmonster_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)


def test_spell_19_charmmonster_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_19_charmmonster_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)


def test_spell_19_charmmonster_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_19_charmmonster_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    m1 = match_data.get_monster_by_id(101)
    assert(m1.controller_id == 1)


def test_spell_19_charmmonster_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_19_charmmonster_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    m1 = match_data.get_monster_by_id(101)
    assert(m1.controller_id == 1)


def test_spell_19_charmmonster_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_19_charmmonster_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)


def test_spell_19_charmmonster_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_19_charmmonster_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)

# Charm Person


def test_spell_20_charmperson_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_20_charmperson_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'W')
    assert(p1gRH == 'W')
    assert(p2gLH == '-')
    assert(p2gRH == 'W')


def test_spell_20_charmperson_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_20_charmperson_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'W')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_20_charmperson_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_20_charmperson_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'F')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_20_charmperson_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_20_charmperson_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'W')
    assert(p1gRH == 'W')
    assert(p2gLH == '-')
    assert(p2gRH == 'W')


def test_spell_20_charmperson_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_20_charmperson_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'W')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_20_charmperson_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_20_charmperson_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'W')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_20_charmperson_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_20_charmperson_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'W')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_20_charmperson_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_20_charmperson_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'W')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_20_charmperson_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_20_charmperson_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == '-')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_20_charmperson_J_samegestures(silent_run=1):

    match_json_filename = 'tests\\test_spell_20_charmperson_J_samegestures.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'W')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')

# Disease


def test_spell_21_disease_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_21_disease_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 0)
    assert(p1.affected_by_disease() == 0)
    assert(p2.affected_by_disease() == 1)


def test_spell_21_disease_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_21_disease_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_disease() == 0)
    assert(p2.affected_by_disease() == 0)


def test_spell_21_disease_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_21_disease_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 0)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_disease() == 1)
    assert(p2.affected_by_disease() == 0)


def test_spell_21_disease_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_21_disease_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 0)
    assert(p1.affected_by_disease() == 0)
    assert(p2.affected_by_disease() == 1)


def test_spell_21_disease_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_21_disease_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_disease() == 0)
    assert(p2.affected_by_disease() == 0)


def test_spell_21_disease_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_21_disease_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_disease() == 0)
    assert(p2.affected_by_disease() == 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_21_disease_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_21_disease_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_disease() == 0)
    assert(p2.affected_by_disease() == 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_21_disease_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_21_disease_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_disease() == 0)
    assert(p2.affected_by_disease() == 0)


def test_spell_21_disease_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_21_disease_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 0)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_disease() == 1)
    assert(p2.affected_by_disease() == 0)


def test_spell_21_disease_J_cures(silent_run=1):

    match_json_filename = 'tests\\test_spell_21_disease_J_cures.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_disease() == 0)
    assert(p2.affected_by_disease() == 0)

# Poison


def test_spell_22_poison_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_22_poison_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 0)
    assert(p1.affected_by_poison() == 0)
    assert(p2.affected_by_poison() == 1)


def test_spell_22_poison_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_22_poison_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_poison() == 0)
    assert(p2.affected_by_poison() == 0)


def test_spell_22_poison_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_22_poison_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 0)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_poison() == 1)
    assert(p2.affected_by_poison() == 0)


def test_spell_22_poison_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_22_poison_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 0)
    assert(p1.affected_by_poison() == 0)
    assert(p2.affected_by_poison() == 1)


def test_spell_22_poison_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_22_poison_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_poison() == 0)
    assert(p2.affected_by_poison() == 0)


def test_spell_22_poison_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_22_poison_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_poison() == 0)
    assert(p2.affected_by_poison() == 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_22_poison_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_22_poison_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_poison() == 0)
    assert(p2.affected_by_poison() == 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_22_poison_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_22_poison_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_poison() == 0)
    assert(p2.affected_by_poison() == 0)


def test_spell_22_poison_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_22_poison_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 0)
    assert(p2.is_alive == 1)
    assert(p1.affected_by_poison() == 1)
    assert(p2.affected_by_poison() == 0)

# Cure Light Wounds


def test_spell_23_curelightwounds_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_23_curelightwounds_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 16)
    assert(p2.hp == 15)


def test_spell_23_curelightwounds_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_23_curelightwounds_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_23_curelightwounds_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_23_curelightwounds_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 16)
    assert(p2.hp == 15)


def test_spell_23_curelightwounds_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_23_curelightwounds_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 16)


def test_spell_23_curelightwounds_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_23_curelightwounds_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_23_curelightwounds_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_23_curelightwounds_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.hp == 2)


def test_spell_23_curelightwounds_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_23_curelightwounds_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.hp == 2)


def test_spell_23_curelightwounds_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_23_curelightwounds_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_23_curelightwounds_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_23_curelightwounds_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 16)
    assert(p2.hp == 15)


def test_spell_23_curelightwounds_J_overheal(silent_run=1):

    match_json_filename = 'tests\\test_spell_23_curelightwounds_J_overheal.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 16)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.hp == 2)

# Cure Heavy Wounds


def test_spell_24_cureheavywounds_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_24_cureheavywounds_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_24_cureheavywounds_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_24_cureheavywounds_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 13)
    assert(p2.hp == 15)


def test_spell_24_cureheavywounds_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_24_cureheavywounds_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_24_cureheavywounds_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_24_cureheavywounds_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_24_cureheavywounds_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_24_cureheavywounds_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 13)
    assert(p2.hp == 15)


def test_spell_24_cureheavywounds_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_24_cureheavywounds_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 13)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)
    assert(m1.hp == 0)


def test_spell_24_cureheavywounds_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_24_cureheavywounds_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 13)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)
    assert(m1.hp == 0)


def test_spell_24_cureheavywounds_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_24_cureheavywounds_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 13)
    assert(p2.hp == 15)


def test_spell_24_cureheavywounds_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_24_cureheavywounds_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_24_cureheavywounds_J_overheal(silent_run=1):

    match_json_filename = 'tests\\test_spell_24_cureheavywounds_J_overheal.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 16)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.hp == 2)

# Anti-Spell


def test_spell_25_antispell_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_25_antispell_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'P')
    assert(p1gRH == 'W')
    assert(p2gLH == '-')
    assert(p2gRH == '-')


def test_spell_25_antispell_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_25_antispell_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'P')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_25_antispell_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_25_antispell_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == '-')
    assert(p1gRH == '-')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_25_antispell_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_25_antispell_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'P')
    assert(p1gRH == 'W')
    assert(p2gLH == '-')
    assert(p2gRH == '-')


def test_spell_25_antispell_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_25_antispell_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'P')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_25_antispell_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_25_antispell_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'P')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_25_antispell_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_25_antispell_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'P')
    assert(p1gRH == 'W')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')


def test_spell_25_antispell_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_25_antispell_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == 'P')
    assert(p1gRH == 'W')
    assert(p2gLH == 'S')
    assert(p2gRH == 'W')


def test_spell_25_antispell_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_25_antispell_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1gLH = match_data.get_gesture_last(1, 1)
    p1gRH = match_data.get_gesture_last(1, 2)
    p2gLH = match_data.get_gesture_last(2, 1)
    p2gRH = match_data.get_gesture_last(2, 2)
    assert(p1gLH == '-')
    assert(p1gRH == '-')
    assert(p2gLH == 'W')
    assert(p2gRH == 'W')

# Blindness


def test_spell_26_blindness_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_26_blindness_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_26_blindness_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_26_blindness_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 13)
    assert(p2.hp == 15)


def test_spell_26_blindness_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_26_blindness_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 13)
    assert(p2.hp == 15)


def test_spell_26_blindness_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_26_blindness_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_26_blindness_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_26_blindness_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 13)
    assert(p2.hp == 15)


def test_spell_26_blindness_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_26_blindness_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 13)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_26_blindness_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_26_blindness_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 13)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_26_blindness_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_26_blindness_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 13)
    assert(p2.hp == 15)


def test_spell_26_blindness_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_26_blindness_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_26_blindness_J_pattern(silent_run=1):

    match_json_filename = 'tests\\test_spell_26_blindness_J_pattern.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)

# Invisibility


def test_spell_27_invisibility_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_27_invisibility_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_27_invisibility_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_27_invisibility_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 12)
    assert(p2.hp == 15)


def test_spell_27_invisibility_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_27_invisibility_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_27_invisibility_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_27_invisibility_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 12)
    assert(p2.hp == 15)


def test_spell_27_invisibility_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_27_invisibility_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 12)
    assert(p2.hp == 15)


def test_spell_27_invisibility_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_27_invisibility_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 13)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_27_invisibility_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_27_invisibility_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 12)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_27_invisibility_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_27_invisibility_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 13)
    assert(p2.hp == 15)


def test_spell_27_invisibility_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_27_invisibility_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 13)

# Permanency


def test_spell_28_permanency_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_28_permanency_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.affected_by_pshield_permanent() == 1)
    assert(p2.affected_by_pshield() == 0)


def test_spell_28_permanency_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_28_permanency_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.affected_by_pshield() == 1)
    assert(p2.affected_by_pshield() == 0)


def test_spell_28_permanency_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_28_permanency_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.affected_by_pshield_permanent() == 1)
    assert(p2.affected_by_pshield() == 0)


def test_spell_28_permanency_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_28_permanency_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.affected_by_pshield() == 1)
    assert(p2.affected_by_pshield_permanent() == 1)


def test_spell_28_permanency_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_28_permanency_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.affected_by_pshield() == 1)
    assert(p2.affected_by_pshield() == 0)


def test_spell_28_permanency_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_28_permanency_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.affected_by_pshield() == 1)
    assert(p2.affected_by_pshield() == 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.affected_by_pshield() == 0)


def test_spell_28_permanency_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_28_permanency_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.affected_by_pshield() == 1)
    assert(p2.affected_by_pshield() == 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.affected_by_pshield() == 0)


def test_spell_28_permanency_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_28_permanency_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.affected_by_pshield() == 1)
    assert(p2.affected_by_pshield() == 0)


def test_spell_28_permanency_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_28_permanency_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.affected_by_pshield_permanent() == 1)
    assert(p2.affected_by_pshield() == 0)


def test_spell_28_permanency_J_dualhand(silent_run=1):

    match_json_filename = 'tests\\test_spell_28_permanency_J_dualhand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.affected_by_haste_permanent() == 1)


# Delay Effect

def test_spell_29_delayeffect_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_29_delayeffect_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 13)


def test_spell_29_delayeffect_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_29_delayeffect_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_29_delayeffect_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_29_delayeffect_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 13)


def test_spell_29_delayeffect_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_29_delayeffect_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_29_delayeffect_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_29_delayeffect_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_29_delayeffect_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_29_delayeffect_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    #m1 = match_data.get_monster_by_id(101, 0)
    #assert(m1.affected_by_pshield() == 0)


def test_spell_29_delayeffect_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_29_delayeffect_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    #m1 = match_data.get_monster_by_id(101, 0)
    #assert(m1.affected_by_pshield() == 0)


def test_spell_29_delayeffect_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_29_delayeffect_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_29_delayeffect_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_29_delayeffect_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 13)


def test_spell_29_delayeffect_J_multisummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_29_delayeffect_J_multisummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 13)
    m1 = match_data.get_monster_by_id(101, 0)
    m2 = match_data.get_monster_by_id(102, 0)
    assert(m1.is_alive == 1)
    assert(m2.is_alive == 0)

def test_spell_29_delayeffect_K_dualhand(silent_run=1):

    match_json_filename = 'tests\\test_spell_29_delayeffect_K_dualhand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 14)

# Remove Enchantment

def test_spell_30_removeenchantment_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_30_removeenchantment_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.statuses['ResistHeat'] == 9999)
    assert(p2.statuses['ResistHeat'] == 0)


def test_spell_30_removeenchantment_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_30_removeenchantment_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.statuses['ResistHeat'] == 9999)
    assert(p2.statuses['ResistHeat'] == 9999)


def test_spell_30_removeenchantment_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_30_removeenchantment_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.statuses['ResistHeat'] == 0)
    assert(p2.statuses['ResistHeat'] == 9999)


def test_spell_30_removeenchantment_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_30_removeenchantment_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.statuses['ResistHeat'] == 9999)
    assert(p2.statuses['ResistHeat'] == 0)


def test_spell_30_removeenchantment_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_30_removeenchantment_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.statuses['ResistHeat'] == 9999)
    assert(p2.statuses['ResistHeat'] == 9999)


def test_spell_30_removeenchantment_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_30_removeenchantment_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.statuses['ResistHeat'] == 9999)
    assert(p2.statuses['ResistHeat'] == 9999)
    assert(p1.hp == 15)
    assert(p2.hp == 14)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_30_removeenchantment_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_30_removeenchantment_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.statuses['ResistHeat'] == 9999)
    assert(p2.statuses['ResistHeat'] == 9999)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_30_removeenchantment_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_30_removeenchantment_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.statuses['ResistHeat'] == 9999)
    assert(p2.statuses['ResistHeat'] == 9999)


def test_spell_30_removeenchantment_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_30_removeenchantment_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.statuses['ResistHeat'] == 0)
    assert(p2.statuses['ResistHeat'] == 9999)

# Shield


def test_spell_31_shield_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_31_shield_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_31_shield_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_31_shield_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 14)
    assert(p2.hp == 15)


def test_spell_31_shield_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_31_shield_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_31_shield_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_31_shield_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 14)
    assert(p2.hp == 15)


def test_spell_31_shield_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_31_shield_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 14)
    assert(p2.hp == 15)


def test_spell_31_shield_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_31_shield_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.hp == 1)
    assert(m1.is_alive == 1)


def test_spell_31_shield_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_31_shield_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.hp == 1)
    assert(m1.is_alive == 1)


def test_spell_31_shield_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_31_shield_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_31_shield_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_31_shield_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)

# Magic Missile


def test_spell_32_magicmissile_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_32_magicmissile_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 14)


def test_spell_32_magicmissile_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_32_magicmissile_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_32_magicmissile_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_32_magicmissile_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 14)
    assert(p2.hp == 15)


def test_spell_32_magicmissile_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_32_magicmissile_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 14)


def test_spell_32_magicmissile_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_32_magicmissile_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_32_magicmissile_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_32_magicmissile_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.hp == 0)
    assert(m1.is_alive == 0)


def test_spell_32_magicmissile_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_32_magicmissile_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.hp == 0)
    assert(m1.is_alive == 0)


def test_spell_32_magicmissile_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_32_magicmissile_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 14)
    assert(p2.hp == 15)


def test_spell_32_magicmissile_J_shielded(silent_run=1):

    match_json_filename = 'tests\\test_spell_32_magicmissile_J_shielded.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)

# Cause Light Wounds


def test_spell_33_causelightwounds_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_33_causelightwounds_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 13)


def test_spell_33_causelightwounds_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_33_causelightwounds_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_33_causelightwounds_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_33_causelightwounds_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 13)
    assert(p2.hp == 15)


def test_spell_33_causelightwounds_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_33_causelightwounds_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 13)


def test_spell_33_causelightwounds_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_33_causelightwounds_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_33_causelightwounds_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_33_causelightwounds_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.hp == -1)
    assert(m1.is_alive == 0)


def test_spell_33_causelightwounds_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_33_causelightwounds_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.hp == -1)
    assert(m1.is_alive == 0)


def test_spell_33_causelightwounds_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_33_causelightwounds_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_33_causelightwounds_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_33_causelightwounds_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 13)
    assert(p2.hp == 15)

# Cause Heavy Wounds


def test_spell_34_causeheavywounds_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_34_causeheavywounds_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 12)


def test_spell_34_causeheavywounds_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_34_causeheavywounds_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_34_causeheavywounds_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_34_causeheavywounds_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 12)
    assert(p2.hp == 15)


def test_spell_34_causeheavywounds_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_34_causeheavywounds_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 12)


def test_spell_34_causeheavywounds_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_34_causeheavywounds_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_34_causeheavywounds_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_34_causeheavywounds_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.hp == -2)
    assert(m1.is_alive == 0)


def test_spell_34_causeheavywounds_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_34_causeheavywounds_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.hp == -2)
    assert(m1.is_alive == 0)


def test_spell_34_causeheavywounds_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_34_causeheavywounds_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_34_causeheavywounds_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_34_causeheavywounds_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 12)
    assert(p2.hp == 15)

# Fireball


def test_spell_35_fireball_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_35_fireball_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 10)


def test_spell_35_fireball_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_35_fireball_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_35_fireball_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_35_fireball_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 10)
    assert(p2.hp == 15)


def test_spell_35_fireball_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_35_fireball_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 10)


def test_spell_35_fireball_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_35_fireball_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_35_fireball_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_35_fireball_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.hp == -4)
    assert(m1.is_alive == 0)


def test_spell_35_fireball_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_35_fireball_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.hp == -4)
    assert(m1.is_alive == 0)


def test_spell_35_fireball_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_35_fireball_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_35_fireball_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_35_fireball_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 10)
    assert(p2.hp == 15)


def test_spell_35_fireball_J_resistheat(silent_run=1):

    match_json_filename = 'tests\\test_spell_35_fireball_J_resistheat.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)

# Lightning Bolt


def test_spell_36_lightningbolt_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_36_lightningbolt_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 10)


def test_spell_36_lightningbolt_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_36_lightningbolt_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_36_lightningbolt_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_36_lightningbolt_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 10)
    assert(p2.hp == 15)


def test_spell_36_lightningbolt_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_36_lightningbolt_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 10)


def test_spell_36_lightningbolt_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_36_lightningbolt_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_36_lightningbolt_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_36_lightningbolt_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.hp == -4)
    assert(m1.is_alive == 0)


def test_spell_36_lightningbolt_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_36_lightningbolt_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.hp == -4)
    assert(m1.is_alive == 0)


def test_spell_36_lightningbolt_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_36_lightningbolt_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_36_lightningbolt_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_36_lightningbolt_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 10)
    assert(p2.hp == 15)

# Clap of Lightning


def test_spell_37_clapoflightning_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_37_clapoflightning_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 10)


def test_spell_37_clapoflightning_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_37_clapoflightning_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_37_clapoflightning_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_37_clapoflightning_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 10)
    assert(p2.hp == 15)


def test_spell_37_clapoflightning_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_37_clapoflightning_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 10)


def test_spell_37_clapoflightning_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_37_clapoflightning_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_37_clapoflightning_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_37_clapoflightning_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.hp == -4)
    assert(m1.is_alive == 0)


def test_spell_37_clapoflightning_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_37_clapoflightning_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    assert(m1.hp == -4)
    assert(m1.is_alive == 0)


def test_spell_37_clapoflightning_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_37_clapoflightning_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_spell_37_clapoflightning_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_37_clapoflightning_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 10)
    assert(p2.hp == 15)


def test_spell_37_clapoflightning_J_double(silent_run=1):

    match_json_filename = 'tests\\test_spell_37_clapoflightning_J_double.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 10)

# Finger of Death


def test_spell_38_fingerofdeath_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_38_fingerofdeath_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 0)


def test_spell_38_fingerofdeath_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_38_fingerofdeath_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)


def test_spell_38_fingerofdeath_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_38_fingerofdeath_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 0)
    assert(p2.is_alive == 1)


def test_spell_38_fingerofdeath_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_38_fingerofdeath_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 0)


def test_spell_38_fingerofdeath_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_38_fingerofdeath_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)


def test_spell_38_fingerofdeath_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_38_fingerofdeath_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)
    assert(m1.is_alive == 0)


def test_spell_38_fingerofdeath_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_38_fingerofdeath_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 1)
    assert(m1.is_alive == 0)


def test_spell_38_fingerofdeath_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_38_fingerofdeath_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 0)


def test_spell_38_fingerofdeath_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_38_fingerofdeath_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 0)
    assert(p2.is_alive == 1)

# Fire Storm


def test_spell_39_firestorm_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_39_firestorm_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_39_firestorm_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_39_firestorm_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_39_firestorm_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_39_firestorm_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_39_firestorm_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_39_firestorm_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_39_firestorm_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_39_firestorm_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_39_firestorm_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_39_firestorm_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_39_firestorm_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_39_firestorm_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_39_firestorm_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_39_firestorm_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_39_firestorm_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_39_firestorm_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_39_firestorm_J_resistheat(silent_run=1):

    match_json_filename = 'tests\\test_spell_39_firestorm_J_resistheat.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_39_firestorm_K_fireelem(silent_run=1):

    match_json_filename = 'tests\\test_spell_39_firestorm_K_fireelem.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_39_firestorm_L_iceelem(silent_run=1):

    match_json_filename = 'tests\\test_spell_39_firestorm_L_iceelem.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 1)


def test_spell_39_firestorm_M_icestorm(silent_run=1):

    match_json_filename = 'tests\\test_spell_39_firestorm_M_icestorm.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 1)

# Ice Storm


def test_spell_40_icestorm_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_spell_40_icestorm_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_40_icestorm_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_spell_40_icestorm_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_40_icestorm_C_self(silent_run=1):

    match_json_filename = 'tests\\test_spell_40_icestorm_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_40_icestorm_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_spell_40_icestorm_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_40_icestorm_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_spell_40_icestorm_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_40_icestorm_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_spell_40_icestorm_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_40_icestorm_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_spell_40_icestorm_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_40_icestorm_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_spell_40_icestorm_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_40_icestorm_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_spell_40_icestorm_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_40_icestorm_J_resistcold(silent_run=1):

    match_json_filename = 'tests\\test_spell_40_icestorm_J_resistcold.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_40_icestorm_K_iceelem(silent_run=1):

    match_json_filename = 'tests\\test_spell_40_icestorm_K_iceelem.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 10)
    assert(p2.hp == 10)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)


def test_spell_40_icestorm_L_fireelem(silent_run=1):

    match_json_filename = 'tests\\test_spell_40_icestorm_L_fireelem.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 1)

# Stab


def test_action_01_stab_A_deftarget(silent_run=1):

    match_json_filename = 'tests\\test_action_01_stab_A_deftarget.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 14)


def test_action_01_stab_B_nobody(silent_run=1):

    match_json_filename = 'tests\\test_action_01_stab_B_nobody.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_action_01_stab_C_self(silent_run=1):

    match_json_filename = 'tests\\test_action_01_stab_C_self.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 14)
    assert(p2.hp == 15)


def test_action_01_stab_D_oppo(silent_run=1):

    match_json_filename = 'tests\\test_action_01_stab_D_oppo.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 14)


def test_action_01_stab_E_hand(silent_run=1):

    match_json_filename = 'tests\\test_action_01_stab_E_hand.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_action_01_stab_F_newsummon(silent_run=1):

    match_json_filename = 'tests\\test_action_01_stab_F_newsummon.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)
    assert(m1.hp == 0)


def test_action_01_stab_G_monster(silent_run=1):

    match_json_filename = 'tests\\test_action_01_stab_G_monster.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101, 0)
    assert(m1.is_alive == 0)
    assert(m1.hp == 0)


def test_action_01_stab_H_countered(silent_run=1):

    match_json_filename = 'tests\\test_action_01_stab_H_countered.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)


def test_action_01_stab_I_mirrored(silent_run=1):

    match_json_filename = 'tests\\test_action_01_stab_I_mirrored.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 14)


def test_action_01_stab_J_shielded(silent_run=1):

    match_json_filename = 'tests\\test_action_01_stab_J_shielded.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.hp == 15)
    assert(p2.hp == 15)

# Surrender


def test_action_02_surrender(silent_run=1):

    match_json_filename = 'tests\\test_action_02_surrender.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 0)
    assert(p2.is_alive == 1)
    assert(p1.hp == 15)
    assert(p2.hp == 15)

# Suicide


def test_action_03_suicide(silent_run=1):

    match_json_filename = 'tests\\test_action_03_suicide.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1, 0)
    p2 = match_data.get_participant_by_id(2, 0)
    assert(p1.is_alive == 1)
    assert(p2.is_alive == 0)

def test_special_spell_selection(silent_run=1):

    match_json_filename = 'tests\\test_special_spell_selection.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    assert(p1.hp == 15)
    assert(p2.hp == 15)
    m1 = match_data.get_monster_by_id(101)
    assert(m1.monster_type == 2)

def test_special_seeded_random_targets(silent_run=1):

    match_json_filename = 'tests\\test_special_seeded_random_targets.json'
    match_data = run_test(match_json_filename, silent_run)
    p1 = match_data.get_participant_by_id(1)
    p2 = match_data.get_participant_by_id(2)
    p3 = match_data.get_participant_by_id(3)
    p4 = match_data.get_participant_by_id(4)
    assert(p1.hp == 15)
    assert(p2.hp == 14)
    assert(p3.hp == 15)
    assert(p4.hp == 14)


# MAIN

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

# Placeholder. Should be chosen from the settings of participant we render for.
lang_code = 'en'

# Random attack seed test, 4 players
"""
test_special_seeded_random_targets()
test_special_seeded_random_targets()
test_special_seeded_random_targets()
test_special_seeded_random_targets()
test_special_seeded_random_targets()
test_special_seeded_random_targets()
test_special_seeded_random_targets()
test_special_seeded_random_targets()
test_special_seeded_random_targets()
test_special_seeded_random_targets()
"""

# General test, 10 turns of _/_
test_template()

# Dispel Magic
test_spell_01_dispelmagic_A_deftarget()
test_spell_01_dispelmagic_B_nobody()
test_spell_01_dispelmagic_C_self()
test_spell_01_dispelmagic_D_oppo()
test_spell_01_dispelmagic_E_hand()
test_spell_01_dispelmagic_G_monster()

# CounterSpell
test_spell_02_counterspell_A_deftarget()
test_spell_02_counterspell_B_nobody()
test_spell_02_counterspell_C_self()
test_spell_02_counterspell_D_oppo()
test_spell_02_counterspell_G_monster()
test_spell_02_counterspell_J_pattern()

# Magic Mirror
test_spell_03_magicmirror_A_deftarget()
test_spell_03_magicmirror_B_nobody()
test_spell_03_magicmirror_C_self()
test_spell_03_magicmirror_D_oppo()
test_spell_03_magicmirror_G_monster()
test_spell_03_magicmirror_H_countered()

# Summon Goblin, Ogre, Troll, Giant
test_spell_04_summongoblin_A_deftarget()
test_spell_04_summongoblin_B_nobody()
test_spell_04_summongoblin_C_self()
test_spell_04_summongoblin_D_oppo()
test_spell_04_summongoblin_G_monster()
test_spell_04_summongoblin_H_countered()
test_spell_04_summongoblin_I_mirrored()
test_spell_05_summonogre_A_deftarget()
test_spell_06_summontroll_A_deftarget()
test_spell_07_summongiant_A_deftarget()

# Summon Fire Elemental, Ice Elemental
test_spell_08_fireelemental_A_deftarget()
test_spell_08_fireelemental_B_nobody()
test_spell_08_fireelemental_C_self()
test_spell_08_fireelemental_D_oppo()
test_spell_08_fireelemental_G_monster()
test_spell_08_fireelemental_H_countered()
test_spell_08_fireelemental_I_mirrored()
test_spell_08_fireelemental_J_merge()
test_spell_09_iceelemental_A_deftarget()
test_spell_09_iceelemental_J_merge()

# Haste
test_spell_10_haste_A_deftarget()
test_spell_10_haste_B_nobody()
test_spell_10_haste_C_self()
test_spell_10_haste_D_oppo()
test_spell_10_haste_E_hand()
test_spell_10_haste_F_newsummon()
test_spell_10_haste_G_monster()
test_spell_10_haste_H_countered()
test_spell_10_haste_I_mirrored()
test_spell_10_haste_J_mindspells()

# Time Stop
test_spell_11_timestop_A_deftarget()
test_spell_11_timestop_B_nobody()
test_spell_11_timestop_C_self()
test_spell_11_timestop_D_oppo()
test_spell_11_timestop_E_hand()
test_spell_11_timestop_F_newsummon()
test_spell_11_timestop_G_monster()
test_spell_11_timestop_H_countered()
test_spell_11_timestop_I_mirrored()
test_spell_11_timestop_J_pattern()

# Protection
test_spell_12_protection_A_deftarget()
test_spell_12_protection_B_nobody()
test_spell_12_protection_C_self()
test_spell_12_protection_D_oppo()
test_spell_12_protection_E_hand()
test_spell_12_protection_F_newsummon()
test_spell_12_protection_G_monster()
test_spell_12_protection_H_countered()
test_spell_12_protection_I_mirrored()

# Resist Heat
test_spell_13_resistheat_A_deftarget()
test_spell_13_resistheat_B_nobody()
test_spell_13_resistheat_C_self()
test_spell_13_resistheat_D_oppo()
test_spell_13_resistheat_E_hand()
test_spell_13_resistheat_F_newsummon()
test_spell_13_resistheat_G_monster()
test_spell_13_resistheat_H_countered()
test_spell_13_resistheat_I_mirrored()
test_spell_13_resistheat_J_fireelem()

# Resist Cold
test_spell_14_resistcold_A_deftarget()
test_spell_14_resistcold_B_nobody()
test_spell_14_resistcold_C_self()
test_spell_14_resistcold_D_oppo()
test_spell_14_resistcold_E_hand()
test_spell_14_resistcold_F_newsummon()
test_spell_14_resistcold_G_monster()
test_spell_14_resistcold_H_countered()
test_spell_14_resistcold_I_mirrored()
test_spell_14_resistcold_J_iceelem()

# Paralysis
test_spell_15_paralysis_A_deftarget()
test_spell_15_paralysis_B_nobody()
test_spell_15_paralysis_C_self()
test_spell_15_paralysis_D_oppo()
test_spell_15_paralysis_E_hand()
test_spell_15_paralysis_F_newsummon()
test_spell_15_paralysis_G_monster()
test_spell_15_paralysis_H_countered()
test_spell_15_paralysis_I_mirrored()

# Amnesia
test_spell_16_amnesia_A_deftarget()
test_spell_16_amnesia_B_nobody()
test_spell_16_amnesia_C_self()
test_spell_16_amnesia_D_oppo()
test_spell_16_amnesia_E_hand()
test_spell_16_amnesia_F_newsummon()
test_spell_16_amnesia_G_monster()
test_spell_16_amnesia_H_countered()
test_spell_16_amnesia_I_mirrored()

# Fear
test_spell_17_fear_A_deftarget()
test_spell_17_fear_B_nobody()
test_spell_17_fear_C_self()
test_spell_17_fear_D_oppo()
test_spell_17_fear_E_hand()
test_spell_17_fear_F_newsummon()
test_spell_17_fear_G_monster()
test_spell_17_fear_H_countered()
test_spell_17_fear_I_mirrored()

# Maladroitness
test_spell_18_maladroitness_A_deftarget()
test_spell_18_maladroitness_B_nobody()
test_spell_18_maladroitness_C_self()
test_spell_18_maladroitness_D_oppo()
test_spell_18_maladroitness_E_hand()
test_spell_18_maladroitness_F_newsummon()
test_spell_18_maladroitness_G_monster()
test_spell_18_maladroitness_H_countered()
test_spell_18_maladroitness_I_mirrored()

# Charm Monster
test_spell_19_charmmonster_A_deftarget()
test_spell_19_charmmonster_B_nobody()
test_spell_19_charmmonster_C_self()
test_spell_19_charmmonster_D_oppo()
test_spell_19_charmmonster_E_hand()
test_spell_19_charmmonster_F_newsummon()
test_spell_19_charmmonster_G_monster()
test_spell_19_charmmonster_H_countered()
test_spell_19_charmmonster_I_mirrored()

# Charm Person
test_spell_20_charmperson_A_deftarget()
test_spell_20_charmperson_B_nobody()
test_spell_20_charmperson_C_self()
test_spell_20_charmperson_D_oppo()
test_spell_20_charmperson_E_hand()
test_spell_20_charmperson_F_newsummon()
test_spell_20_charmperson_G_monster()
test_spell_20_charmperson_H_countered()
test_spell_20_charmperson_I_mirrored()
test_spell_20_charmperson_J_samegestures()

# Disease
test_spell_21_disease_A_deftarget()
test_spell_21_disease_B_nobody()
test_spell_21_disease_C_self()
test_spell_21_disease_D_oppo()
test_spell_21_disease_E_hand()
test_spell_21_disease_F_newsummon()
test_spell_21_disease_G_monster()
test_spell_21_disease_H_countered()
test_spell_21_disease_I_mirrored()
test_spell_21_disease_J_cures()

# Poison
test_spell_22_poison_A_deftarget()
test_spell_22_poison_B_nobody()
test_spell_22_poison_C_self()
test_spell_22_poison_D_oppo()
test_spell_22_poison_E_hand()
test_spell_22_poison_F_newsummon()
test_spell_22_poison_G_monster()
test_spell_22_poison_H_countered()
test_spell_22_poison_I_mirrored()

# Cure Light Wounds
test_spell_23_curelightwounds_A_deftarget()
test_spell_23_curelightwounds_B_nobody()
test_spell_23_curelightwounds_C_self()
test_spell_23_curelightwounds_D_oppo()
test_spell_23_curelightwounds_E_hand()
test_spell_23_curelightwounds_F_newsummon()
test_spell_23_curelightwounds_G_monster()
test_spell_23_curelightwounds_H_countered()
test_spell_23_curelightwounds_I_mirrored()
test_spell_23_curelightwounds_J_overheal()

# Cure Heavy Wounds
test_spell_24_cureheavywounds_A_deftarget()
test_spell_24_cureheavywounds_B_nobody()
test_spell_24_cureheavywounds_C_self()
test_spell_24_cureheavywounds_D_oppo()
test_spell_24_cureheavywounds_E_hand()
test_spell_24_cureheavywounds_F_newsummon()
test_spell_24_cureheavywounds_G_monster()
test_spell_24_cureheavywounds_H_countered()
test_spell_24_cureheavywounds_I_mirrored()
test_spell_24_cureheavywounds_J_overheal()

# Anti-Spell
test_spell_25_antispell_A_deftarget()
test_spell_25_antispell_B_nobody()
test_spell_25_antispell_C_self()
test_spell_25_antispell_D_oppo()
test_spell_25_antispell_E_hand()
test_spell_25_antispell_F_newsummon()
test_spell_25_antispell_G_monster()
test_spell_25_antispell_H_countered()
test_spell_25_antispell_I_mirrored()

# Blindness
test_spell_26_blindness_A_deftarget()
test_spell_26_blindness_B_nobody()
test_spell_26_blindness_C_self()
test_spell_26_blindness_D_oppo()
test_spell_26_blindness_E_hand()
test_spell_26_blindness_F_newsummon()
test_spell_26_blindness_G_monster()
test_spell_26_blindness_H_countered()
test_spell_26_blindness_I_mirrored()
test_spell_26_blindness_J_pattern()

# Invisibility
test_spell_27_invisibility_A_deftarget()
test_spell_27_invisibility_B_nobody()
test_spell_27_invisibility_C_self()
test_spell_27_invisibility_D_oppo()
test_spell_27_invisibility_E_hand()
test_spell_27_invisibility_F_newsummon()
test_spell_27_invisibility_G_monster()
test_spell_27_invisibility_H_countered()
test_spell_27_invisibility_I_mirrored()

# Permanency

test_spell_28_permanency_A_deftarget()
test_spell_28_permanency_B_nobody()
test_spell_28_permanency_C_self()
test_spell_28_permanency_D_oppo()
test_spell_28_permanency_E_hand()
test_spell_28_permanency_F_newsummon()
test_spell_28_permanency_G_monster()
test_spell_28_permanency_H_countered()
test_spell_28_permanency_I_mirrored()
test_spell_28_permanency_J_dualhand()

# Delay Effect
test_spell_29_delayeffect_A_deftarget()
test_spell_29_delayeffect_B_nobody()
test_spell_29_delayeffect_C_self()
test_spell_29_delayeffect_D_oppo()
test_spell_29_delayeffect_E_hand()
test_spell_29_delayeffect_F_newsummon()
test_spell_29_delayeffect_G_monster()
test_spell_29_delayeffect_H_countered()
test_spell_29_delayeffect_I_mirrored()
test_spell_29_delayeffect_J_multisummon()
test_spell_29_delayeffect_K_dualhand()

# Remove Enchantment
test_spell_30_removeenchantment_A_deftarget()
test_spell_30_removeenchantment_B_nobody()
test_spell_30_removeenchantment_C_self()
test_spell_30_removeenchantment_D_oppo()
test_spell_30_removeenchantment_E_hand()
test_spell_30_removeenchantment_F_newsummon()
test_spell_30_removeenchantment_G_monster()
test_spell_30_removeenchantment_H_countered()
test_spell_30_removeenchantment_I_mirrored()

# Shield
test_spell_31_shield_A_deftarget()
test_spell_31_shield_B_nobody()
test_spell_31_shield_C_self()
test_spell_31_shield_D_oppo()
test_spell_31_shield_E_hand()
test_spell_31_shield_F_newsummon()
test_spell_31_shield_G_monster()
test_spell_31_shield_H_countered()
test_spell_31_shield_I_mirrored()

# Magic Missle
test_spell_32_magicmissile_A_deftarget()
test_spell_32_magicmissile_B_nobody()
test_spell_32_magicmissile_C_self()
test_spell_32_magicmissile_D_oppo()
test_spell_32_magicmissile_E_hand()
test_spell_32_magicmissile_F_newsummon()
test_spell_32_magicmissile_G_monster()
test_spell_32_magicmissile_I_mirrored()
test_spell_32_magicmissile_J_shielded()

# Cause Light Wounds
test_spell_33_causelightwounds_A_deftarget()
test_spell_33_causelightwounds_B_nobody()
test_spell_33_causelightwounds_C_self()
test_spell_33_causelightwounds_D_oppo()
test_spell_33_causelightwounds_E_hand()
test_spell_33_causelightwounds_F_newsummon()
test_spell_33_causelightwounds_G_monster()
test_spell_33_causelightwounds_H_countered()
test_spell_33_causelightwounds_I_mirrored()

# Cause Heavy Wounds
test_spell_34_causeheavywounds_A_deftarget()
test_spell_34_causeheavywounds_B_nobody()
test_spell_34_causeheavywounds_C_self()
test_spell_34_causeheavywounds_D_oppo()
test_spell_34_causeheavywounds_E_hand()
test_spell_34_causeheavywounds_F_newsummon()
test_spell_34_causeheavywounds_G_monster()
test_spell_34_causeheavywounds_H_countered()
test_spell_34_causeheavywounds_I_mirrored()

# Fireball
test_spell_35_fireball_A_deftarget()
test_spell_35_fireball_B_nobody()
test_spell_35_fireball_C_self()
test_spell_35_fireball_D_oppo()
test_spell_35_fireball_E_hand()
test_spell_35_fireball_F_newsummon()
test_spell_35_fireball_G_monster()
test_spell_35_fireball_H_countered()
test_spell_35_fireball_I_mirrored()
test_spell_35_fireball_J_resistheat()

# Lightning Bolt
test_spell_36_lightningbolt_A_deftarget()
test_spell_36_lightningbolt_B_nobody()
test_spell_36_lightningbolt_C_self()
test_spell_36_lightningbolt_D_oppo()
test_spell_36_lightningbolt_E_hand()
test_spell_36_lightningbolt_F_newsummon()
test_spell_36_lightningbolt_G_monster()
test_spell_36_lightningbolt_H_countered()
test_spell_36_lightningbolt_I_mirrored()

# Clap of Lightning
test_spell_37_clapoflightning_A_deftarget()
test_spell_37_clapoflightning_B_nobody()
test_spell_37_clapoflightning_C_self()
test_spell_37_clapoflightning_D_oppo()
test_spell_37_clapoflightning_E_hand()
test_spell_37_clapoflightning_F_newsummon()
test_spell_37_clapoflightning_G_monster()
test_spell_37_clapoflightning_H_countered()
test_spell_37_clapoflightning_I_mirrored()
test_spell_37_clapoflightning_J_double()

# Finger of Death
test_spell_38_fingerofdeath_A_deftarget()
test_spell_38_fingerofdeath_B_nobody()
test_spell_38_fingerofdeath_C_self()
test_spell_38_fingerofdeath_D_oppo()
test_spell_38_fingerofdeath_E_hand()
test_spell_38_fingerofdeath_F_newsummon()
test_spell_38_fingerofdeath_G_monster()
test_spell_38_fingerofdeath_H_countered()
test_spell_38_fingerofdeath_I_mirrored()

# Fire Storm
test_spell_39_firestorm_A_deftarget()
test_spell_39_firestorm_B_nobody()
test_spell_39_firestorm_C_self()
test_spell_39_firestorm_D_oppo()
test_spell_39_firestorm_E_hand()
test_spell_39_firestorm_F_newsummon()
test_spell_39_firestorm_G_monster()
test_spell_39_firestorm_H_countered()
test_spell_39_firestorm_I_mirrored()
test_spell_39_firestorm_J_resistheat()
test_spell_39_firestorm_K_fireelem()
test_spell_39_firestorm_L_iceelem()
test_spell_39_firestorm_M_icestorm()

# Ice Storm
test_spell_40_icestorm_A_deftarget()
test_spell_40_icestorm_B_nobody()
test_spell_40_icestorm_C_self()
test_spell_40_icestorm_D_oppo()
test_spell_40_icestorm_E_hand()
test_spell_40_icestorm_F_newsummon()
test_spell_40_icestorm_G_monster()
test_spell_40_icestorm_H_countered()
test_spell_40_icestorm_I_mirrored()
test_spell_40_icestorm_J_resistcold()
test_spell_40_icestorm_K_iceelem()
test_spell_40_icestorm_L_fireelem()

# Stab
test_action_01_stab_A_deftarget()
test_action_01_stab_B_nobody()
test_action_01_stab_C_self()
test_action_01_stab_D_oppo()
test_action_01_stab_E_hand()
test_action_01_stab_F_newsummon()
test_action_01_stab_G_monster()
test_action_01_stab_H_countered()
test_action_01_stab_I_mirrored()
test_action_01_stab_J_shielded()

# Surrender

test_action_02_surrender()

# Suicide

test_action_03_suicide()

# Spell selection

test_special_spell_selection()
