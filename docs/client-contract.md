# Client contract

What a client (such as swweb) may rely on. Everything listed here is checked for every ruleset by
`tests_core/tests_contract.py`; a change that breaks it is a **Breaking** changelog entry. Anything not
listed is internal and may change in any release.

The list starts from what swweb uses today. It grows when a client needs more, not before.

## Loading a ruleset

Clients load classes by name from the ruleset code (`Warlocks`, `Spellbinder`, …):

| What | Module | Name |
|---|---|---|
| Match data | `spellweavers.<code>.class_<code>_matchdata` | `<Code>MatchData` |
| Spellbook | `spellweavers.<code>.class_<code>_spellbook` | `<Code>SpellBook` |
| Orders | `spellweavers.<code>.class_<code>_orders` | `<Code>Orders` |
| Spell names | `spellweavers.<code>.loc_<code>_<lang>` | `<code>_spell_names_<lang>` |
| Spell descriptions | `spellweavers.<code>.loc_<code>_rules_<lang>` | `<code>_spell_descriptions_<lang>` |

`<code>` is the lower-case code (`warlocks`); `<Code>` keeps its capital (`Warlocks`).
`spellweavers.tools_engine.import_name(module, name)` does the import.

## Running a match

1. `match_data = <Code>MatchData(match_id)`, `spellbook = <Code>SpellBook()`, `orders = <Code>Orders()`.
2. `match_data.match_init_output(code, lang)` loads the text tables.
3. Create actors **only** through `match_data.create_participant(...)` / `create_monster(...)`, then append them to
   `participant_list` / `monster_list`. These methods give actors what the ruleset needs (e.g. `mindspell_effects`);
   constructing actor classes directly is not supported.
4. `match_data.process_match_start()`.
5. Each turn: parse and validate orders (`orders.validate_json_order`, `orders.parse_json_order`, appending to
   `orders.orders`), check `orders.check_missing_orders(match_data)`, then
   `match_data.process_match_turn(orders, spellbook)`.
6. Read results: `match_log`, `get_log_entries_by_turn`, `get_log_string_by_log_id`, `get_status_string_actor_by_id`,
   `turns_info`, `match_gestures`.

## Objects

**MatchData:** `DATA_HAND_ID_OFFSET`, `match_id`, `current_turn`, `match_status`, `participant_list`,
`monster_list`, `match_log`, `match_gestures`, `turns_info`, `spell_names`; `create_participant`, `create_monster`,
`process_match_start`, `process_match_turn`, `set_current_turn`, `match_init_output`, `get_match_status_ongoing`,
`get_match_status_finished`, `get_ids_participants`, `get_ids_participants_active`, `get_ids_monsters`,
`get_ids_targets`, `get_participant_by_id`, `get_monster_by_id`, `get_name_by_id`,
`get_participant_turn_active_status`, `get_status_string_actor_by_id`, `get_text_strings_by_code`,
`get_turn_info_template`, `get_gesture`, `get_gesture_history`, `get_log_entry_template`, `get_log_entries_by_turn`,
`get_log_string_by_log_id`.

**SpellBook:** `spellbook_code`, `valid_gestures`, `valid_gestures_feared`, `valid_spell_ids`, `spell_definitions`,
`get_new_spell_by_id`, `match_spell_pattern_monsters`.

**Orders:** `orders`, `parse_json_order`, `validate_json_order`, `check_missing_orders`.
**Order** fields: `match_id`, `turn_num`, `participant_id`, `gesture_lh`, `gesture_rh`, `order_spell_lh`,
`order_spell_rh`, `order_target_lh`, `order_target_rh`, `delay_spell`, `cast_delayed_spell`, `make_spell_permanent`,
`commit_suicide`, `paralyze_orders`, `charm_orders`, `attack_orders`.

**Participant:** `id`, `player_id`, `team_id`, `hp`, `is_alive`, `lh_id`, `rh_id`, `effects`, `states`,
`turn_created`, `turn_destroyed`, `turn_surrendered`, `get_effects_template`, `get_states_template`, `set_actor_id`,
`set_hands_ids`.
**Monster:** `id`, `monster_type`, `controller_id`, `attack_id`, `summoner_id`, `summoner_hand_id`, `hp`, `is_alive`,
`effects`, `states`, `turn_created`, `turn_destroyed`, `get_effects_template`, `get_states_template`, `set_actor_id`.

**Spell:** `id`, `caster_id`, `target_id`, `used_hand`, `used_pattern`, `cast_turn`, `resolve`, `flags`
(`flags['delayed']` marks a spell held by Delay Effect).

## Data formats

- **Spell definitions** (`spell_definitions`): dicts with `id`, `priority`, `patterns`, `default_target`,
  `duration`, `code`, `tags`; mindspells also have `effect`. Spell IDs are stable keys (loc tables, orders).
- **Effects and states:** per turn, `actor.effects[turn]` / `actor.states[turn]` hold exactly the keys of
  `get_effects_template()` / `get_states_template()`. The keys differ between rulesets; store and restore them by key.
- **Log entries:** dicts with the keys of `get_log_entry_template()`.
- **Orders JSON:** the keys `parse_json_order` reads (`matchID`, `turnNum`, `participantID`, `gestureLH`, …).

## Not in the contract

Everything else, including actor constructors, `require_*` lookups, `get_ids_spells_*`, and core's
`NotImplementedError` stubs (those are the contract for *ruleset* authors, a separate audience).
