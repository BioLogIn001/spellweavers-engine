# Changelog

All notable changes to the spellweavers engine.
Versions follow CalVer 'YYYY.M.N': release year, release month, and a counter
within the month. Read the **Breaking** section before upgrading.  **Rules** lists
changes to game outcomes: matches replayed on a newer version may give different results.

## [Unreleased]

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
[2026.10.1]: https://github.com/BioLogIn001/spellweavers-engine/releases/tag/v2026.10.1
