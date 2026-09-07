"""Stacks, baskets and the episode rule (`DESIGN/110-watch-basket.md` §3-§4).

`stacks(row)` turns one name-night's 17 condition values (a mapping `condition_id -> True/False/
None`) into the `bull`/`bear`/`vol` counts and the true/null id lists. `baskets(stack, row)`
applies the fixed thresholds to get LONG/SHORT/VOL/CONFLICT membership for that name-night.
`assign_episodes` implements §4's rule generically -- an episode is the first night a name enters
some grouping (a basket, a single condition, a bull/bear count bucket); a re-entry within 21
sessions is not a new episode -- so the same function grades baskets, conditions and counts alike
(`retro.py` uses it for all three).
"""
from __future__ import annotations

from typing import Mapping

import pandas as pd

from engine.watch.conditions import ALL_CONDITIONS, SIGN_MINUS, SIGN_PLUS

LONG_MIN_BULL = 3          # DESIGN/110 §3: "LONG: bull >= 3 and bear = 0"
SHORT_MIN_BEAR = 3         # "SHORT: bear >= 3 and bull = 0"
CONFLICT_MIN = 2           # "CONFLICT (logged, not a basket): bull >= 2 and bear >= 2"
REENTRY_SESSIONS = 21      # DESIGN/110 §4: re-entries within 21 sessions are not new episodes

BASKET_NAMES = ("LONG", "SHORT", "VOL", "CONFLICT")


def stacks(row: Mapping[str, bool | None]) -> dict:
    """`row`: `{condition_id: True/False/None}` for every id in `ALL_CONDITIONS` (a missing key is
    treated the same as `None`). Returns `bull`, `bear`, `vol`, `true_ids`, `null_ids`."""
    true_ids = [cid for cid in ALL_CONDITIONS if row.get(cid) is True]
    null_ids = [cid for cid in ALL_CONDITIONS if row.get(cid) is None]
    bull = sum(1 for cid in SIGN_PLUS if row.get(cid) is True)
    bear = sum(1 for cid in SIGN_MINUS if row.get(cid) is True)
    vol = row.get("C-VOL") is True
    return {"bull": bull, "bear": bear, "vol": vol, "true_ids": true_ids, "null_ids": null_ids}


def baskets(row: Mapping[str, bool | None], stack: dict | None = None) -> dict:
    """LONG/SHORT/CONFLICT come straight from the `bull`/`bear` counts (already True-only, so they
    are always definite integers). VOL additionally requires `C-LOW` and `C-SHORT` not be
    confirmed `True` that night -- a `None` (unknown) on either does not exclude the name, only a
    confirmed `True` does, matching a screening basket's practical reading of "and not C-LOW and
    not C-SHORT" (a stricter three-valued NOT would make VOL membership `None` whenever either is
    unknown, which the nightly report cannot use as a basket flag)."""
    stack = stack or stacks(row)
    bull, bear = stack["bull"], stack["bear"]
    vol_ok = (row.get("C-VOL") is True) and (row.get("C-LOW") is not True) and (row.get("C-SHORT") is not True)
    return {
        "LONG": bool(bull >= LONG_MIN_BULL and bear == 0),
        "SHORT": bool(bear >= SHORT_MIN_BEAR and bull == 0),
        "VOL": bool(vol_ok),
        "CONFLICT": bool(bull >= CONFLICT_MIN and bear >= CONFLICT_MIN),
    }


def assign_episodes(true_rows: pd.DataFrame, key_cols: list[str], date_col: str,
                     session_order: Mapping, reentry_sessions: int = REENTRY_SESSIONS) -> pd.DataFrame:
    """`true_rows`: rows where some event is already known to be `True` (the caller pre-filters --
    this function does not interpret truthiness). `session_order`: `{date: int index}` over the
    panel's actual nights (ascending, gaps and all), so "sessions apart" is measured on the real
    calendar this book trades on, not calendar days. Adds an `episode_start` column: the date of
    the first night of the episode each row belongs to. The number of distinct
    `(key_cols..., episode_start)` combinations is the episode count (`episode_count`)."""
    cols = list(key_cols) + [date_col]
    if true_rows.empty:
        return true_rows.assign(episode_start=pd.Series(dtype="object"))
    df = true_rows.sort_values(cols).reset_index(drop=True)
    last_start: dict[tuple, object] = {}
    last_idx: dict[tuple, int] = {}
    starts = []
    for row in df.itertuples(index=False):
        key = tuple(getattr(row, c) for c in key_cols)
        idx = session_order[getattr(row, date_col)]
        if key not in last_idx or (idx - last_idx[key]) > reentry_sessions:
            last_start[key] = getattr(row, date_col)
        last_idx[key] = idx
        starts.append(last_start[key])
    return df.assign(episode_start=starts)


def episode_count(episoded: pd.DataFrame, key_cols: list[str]) -> int:
    """Number of distinct episodes in a frame already carrying `episode_start` (from
    `assign_episodes`)."""
    if episoded.empty:
        return 0
    return int(episoded.drop_duplicates(list(key_cols) + ["episode_start"]).shape[0])
