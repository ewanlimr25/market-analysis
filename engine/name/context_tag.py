"""`context_read` for a discretionary (`disc-1.0`) row (findings/stock-deep-dive DESIGN/70 §6, D13).

What the owner had read when `DIRECTION=` was passed, decided from file modification times in the
sheet directory `analyses/ticker/<SYMBOL>/<DATE>/`, never from a flag the owner sets:

    none        no `ticker.json` existed for (ticker, date) before this call
    sheet_only  `ticker.json` existed, no `narrate.md`
    narrate     `narrate.md` existed (the one surviving home of the old skill's research layer)

The discretionary read compares mean R by this stratum (`DESIGN/70 §6`); it is the one test of
whether the research layer helps the owner decide, so it must not be editable after the fact.
"""
from __future__ import annotations

import os

from engine.config import CONTEXT_READ_VALUES

NONE, SHEET_ONLY, NARRATE = CONTEXT_READ_VALUES
SHEET_FILE = "ticker.json"
NARRATE_FILE = "narrate.md"


def _existed_before(path: str, call_time: float) -> bool:
    return os.path.exists(path) and os.path.getmtime(path) <= call_time


def context_read(sheet_dir: str, call_time: float) -> str:
    """The stratum for a call made at `call_time` (epoch seconds) against `sheet_dir`."""
    if _existed_before(os.path.join(sheet_dir, NARRATE_FILE), call_time):
        return NARRATE
    if _existed_before(os.path.join(sheet_dir, SHEET_FILE), call_time):
        return SHEET_ONLY
    return NONE
