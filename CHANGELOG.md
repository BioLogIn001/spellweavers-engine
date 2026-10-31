# Changelog

All notable changes to the spellweavers engine.
Versions follow CalVer `YYYY.M.N`: release year, release month, and a counter
within the month. Read the **Breaking** section before upgrading. **Rules** lists
changes to game outcomes: matches replayed on a newer version may give different results.

## [Unreleased]

## [2026.10.2] - 2026-10-31

### Breaking
- Damage types are `int` constants instead of strings: use `DefaultActor.DAMAGE_TYPE_PHYSICAL`,
  `DAMAGE_TYPE_FIRE`, `DAMAGE_TYPE_ICE` for `damage_type` in `monster_types` entries
  and actor constructors.
- Core declares the ruleset contract. `core.class_actor` has `Participant` and `Monster` base classes listing the
  attributes core relies on; a ruleset's participant and monster classes must subclass them. Methods core calls
  but a ruleset implements are `NotImplementedError` stubs in core `MatchData`, `Orders`, `SpellBook` and
  `DefaultActor` (e.g. `create_participant`, `get_name_by_id`, `check_gesture_visibility`, `parse_json_order`,
  `get_effects_template`).
- Core `get_log_string_by_log_id` no longer has its own copy of the visibility rules; it calls the ruleset's
  `check_gesture_visibility`.
- `Orders` is generic over its order class: subclass it as `Orders[YourOrder]`. `search_orders`, the `orders` list
  and the `ORDER_INVALID_*` constants now live in core.
- Spell tables are typed (`core.class_spellbook.SpellDefinition`) and need a `tags` list on every row; mindspell rows
  also need an `effect` key (the effect name, e.g. `'Paralysis'`). A spellbook provides its table by overriding
  `get_spell_definitions()` instead of assigning `spell_definitions` in `__init__`. `valid_spell_ids` is built from
  the table.
- A ruleset's `MatchData` must name its spellbook in `spellbook_class`: the mindspell effect names come from that
  spellbook's table (`MatchData.mindspell_effects`). Actors get them only through `create_participant` /
  `create_monster`; actor constructors are not part of any contract.
- `valid_gestures` is a read-only property built from the gesture dictionary; assigning it raises `AttributeError`.
- `gesture_dict_paraff` (default) and `gesture_dict_parafc` (Warlocks) are renamed `gesture_dict_paralysis`.
- `create_monster` raises `ValueError` for an unknown monster type instead of returning `None`.

### Rules
- A two-handed spell ordered by spell ID now uses both hands: it is cast once, and the other hand's order is ignored.
  Before, ordering it on both hands cast it twice, and ordering it on one hand let the other hand also
  cast a one-handed spell. If both hands order a two-handed spell, the LH order wins, as in automatic selection.
  Delay and Permanency accept either hand's ID, as they already did for automatically selected two-handed spells (#80).
- A spell whose last gesture uses both hands now always takes its target from the LH target field (orderTargetLH).
  Before, the target came from whichever hand made the rest of the pattern.
  A hypothetical two-handed summon gets the LH ID as its summoning hand (#44).

### Added
- Client contract: `docs/client-contract.md` lists what clients such as swweb may rely on, and
  `tests_core/tests_contract.py` checks it for every ruleset (#74).
- `SpellBook.valid_gestures_feared`: the gestures a participant under Fear can make, built from the Fear table.
  swweb's order form already reads this name.
- `spell_definitions` rows carry `tags` (`permanentable`, `summon`, `mindspell`, `storm`) and, for mindspells,
  `effect`. Helpers: `get_ids_spells_by_tag`, `get_effects_by_tag`, and `get_id_spell_by_code`, which raises
  `LookupError` for a code the spellbook doesn't have.
- `MatchData.require_actor` / `require_participant` / `require_monster`: lookups for actors that must exist; they
  raise `LookupError` instead of returning `None`.
- Ruleset switches as class attributes: `SPELL_TARGET_ALIVE_ONLY` (spellbook; `True` in Warlocks: spells can't
  target the dead) and `STAB_SELF_ALLOWED` (match data; `True` in Warlocks).

### Fixed
- Log entries for spells cast at nobody (`castTimeStopNobody`, `castProtectionNobody`,
  `castCureWoundsNobody`, `castLightningBoltNobody`) now carry the caster as `actor_id`,
  like all other `…Nobody` entries. Both rulesets.
- Spellbinder rules text: Confusion was listed as Maladroitness in mindspell, Permanency
  and Remove Enchantment descriptions; elemental max HP corrected to 3; elemental Fear note
  rewritten for Spellbinder.
- Spellbinder: Haste-countered log text had a stray quote (`{targetname}'s' shield`).
- Log text for a participant's POV now shows gestures of other players time-stopped
  on the same turn, matching the gesture grid (#79). Both rulesets.

### Changed
- `make_precast_target_checks` (Warlocks) accepts an optional `search_alive_only`
  argument (default `True`), as in Spellbinder.
- new `default/` package (a copy of Bartle's Spellbinder); Spellbinder classes are now thin subclasses.
- Spellbinder log text says "wizards" instead of "spellbinders" (`resultDraw`, `effectHaste`), following Bartle's wording.
- Warlocks classes are now thin subclasses of `default/`, overriding only where RavenBlack's rules differ.
- mypy now runs with no disabled error codes and no `# type: ignore` (#74).
- `get_ids_spells_permanentable`, `get_ids_summons` and the other `get_ids_spells_*` lists are derived from the
  spell table's tags and codes instead of being written out. Same lists as before in both rulesets.
- Warlocks overrides removed where the default now covers the difference through the switches above, the spell
  table, or `mindspell_effects`: `select_spells_for_stack`, `check_stabs`, `effect_paralysis`,
  `remove_enchantments`, `remove_mindspell_effects`, `affected_by_permanent_mindspell`,
  `update_effects_on_participants_eot`. Warlocks' spellbook `__init__` now goes through the default's.

## [2026.10.1] - 2026-10-27

First tagged release.

### Breaking
- Code moved to `src/spellweavers/`; old top-level packages are gone:
  `ruleset_core` → `spellweavers.core`, `ruleset_warlocks` → `spellweavers.warlocks`,
  `ruleset_spellbinder` → `spellweavers.spellbinder`,
  `common.tools_engine` → `spellweavers.tools_engine`.
- `match_process_json` moved from `tests_core.tests_engine_core` to `spellweavers.engine`.
- Engine code no longer prints (#69). `MatchData.print_match_log()` is now
  `log_match_history()` and `print_actor_statuses()` is now `log_actor_statuses()`;
  both drop the `stay_silent` argument and append lines to `MatchData.log` instead.
- `Spell.clone()` now requires the `pattern` argument (#72).

### Rules
- Mind-spell clashes now ignore spells that fizzled, e.g. because the caster
  was blinded (#73). Applies to both Warlocks and Spellbinder.

### Added
- Installable package: `pip install git+https://github.com/BioLogIn001/spellweavers-engine.git@v2026.10.1`.
- CI running pytest on Python 3.12–3.14 and mypy (#76).
- `spellweavers_rungame.py` takes command-line options
  (`-f`, `-s`, `-m`, `-p`, `-pov`, `-l`, `-silent`) (#77).

### Changed
- `tools_engine.import_name` keeps the original `ImportError` as the cause
  of the `ModuleNotFoundError` it raises (#70).
- Tests run with plain `pytest`; `spellweavers_testsuite.py` removed (#78).
- `mypy.ini` replaced by `pyproject.toml`; dev tools installable with
  `pip install --group dev` (#71).

[Unreleased]: https://github.com/BioLogIn001/spellweavers-engine/compare/v2026.10.1...HEAD
[2026.10.2]: https://github.com/BioLogIn001/spellweavers-engine/releases/tag/v2026.10.2
[2026.10.1]: https://github.com/BioLogIn001/spellweavers-engine/releases/tag/v2026.10.1
