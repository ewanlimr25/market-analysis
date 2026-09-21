"""The ticker sheet (`make ticker`), specified in
`~/Development/findings/stock-deep-dive/DESIGN/70-ticker-sheet-spec.md`.

One command reads the marts and a live chain for one name and writes
`analyses/ticker/<SYMBOL>/<DATE>/ticker.json` + `report.md` + the inputs it read. Every threshold
the sheet applies lives in `engine.config.NAME_PARAMS` (frozen 2026-09-20, DESIGN/70 §2 to §6);
nothing in this package tunes one.

Build order (DESIGN/70 §10): `data.py` (R1, the per-name slice of every §1 input) is here;
`liquidity/events/premium` (R2), `range/flags/context` (R3), `structures` (R4), `grade/seed` (R5)
and `sheet/report/narrate` (R6) follow. Each section module exposes
`evaluate(inputs, params, ...) -> dict` over the `NameInputs` this package's `data` module loads.

Two rules hold across every module here: a missing input is a `None` plus an entry in `nulls`,
never an exception (a sheet with every null still writes, DESIGN/70 §1); and every number carries
a `source` sibling naming the mart, chain or endpoint and the date it carries.
"""
