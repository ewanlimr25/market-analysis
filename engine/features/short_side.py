"""The short-side control join: `short_interest`, `days_to_cover`, `si_change_pct` (point-in-time,
`engine.mart.short_interest.load_short_interest`) and `borrow_fee` (daily snapshot,
`engine.mart.borrow.load_borrow`) attached to a screener-spine DataFrame of `(ticker, date)` rows.

This is the control column G4 (RESEARCH/47 §2) conditions its IV-spread cross-section on, and the
risk-veto input for any short leg. All four attached columns are nullable: a ticker absent from either
source on a given date gets NaN, not a dropped row -- the spine's row count and order are preserved.

Pure with respect to its loader arguments: `join_short_side` takes `load_short_interest` and
`load_borrow` as injectable callables (default: the real point-in-time / fail-soft loaders) so tests
never touch the mart on disk.
"""
from __future__ import annotations

from typing import Callable

import pandas as pd

from engine.mart import borrow as B
from engine.mart import short_interest as SI

SPINE_COLUMNS = ("ticker", "date")
ATTACHED_COLUMNS = ("short_interest", "days_to_cover", "si_change_pct", "borrow_fee")
BORROW_ASOF_COLUMN = "borrow_asof"     # the snapshot date each row's borrow_fee came from (None when null)

_SI_RENAME = {"current_short_position": "short_interest", "change_percent": "si_change_pct"}
_SI_KEEP = ["symbol", "current_short_position", "days_to_cover", "change_percent"]
_BORROW_KEEP = ["symbol", "fee_rate"]


def _si_for_date(load_short_interest: Callable, as_of) -> pd.DataFrame:
    si = load_short_interest(as_of)
    if si is None or si.empty:
        return pd.DataFrame(columns=["symbol", "short_interest", "days_to_cover", "si_change_pct"])
    return si[_SI_KEEP].rename(columns=_SI_RENAME)


def _borrow_for_date(load_borrow: Callable, d) -> tuple[pd.DataFrame, object]:
    """The borrow frame for `d` and the snapshot date it came from (`asof` when the loader reports
    one, else `d`; None when there is no data)."""
    result = load_borrow(d)
    data = result["data"] if isinstance(result, dict) else result
    if data is None or data.empty:
        return pd.DataFrame(columns=["symbol", "borrow_fee"]), None
    asof = result.get("asof", d) if isinstance(result, dict) else d
    return data[_BORROW_KEEP].rename(columns={"fee_rate": "borrow_fee"}), asof


def _empty_spine_with_columns(spine: pd.DataFrame) -> pd.DataFrame:
    out = spine.copy()
    for c in ATTACHED_COLUMNS:
        out[c] = pd.Series(dtype="float64")
    out[BORROW_ASOF_COLUMN] = pd.Series(dtype="object")
    return out


def join_short_side(spine: pd.DataFrame, load_short_interest: Callable = SI.load_short_interest,
                     load_borrow: Callable = B.load_borrow_asof) -> pd.DataFrame:
    """`spine` must have `ticker` and `date` columns (one row per name-day, as the screener spine does).
    Returns a new frame with the same row count and row order as `spine`, plus `short_interest`,
    `days_to_cover`, `si_change_pct` (point-in-time as of `date`, never later than what would have been
    known that day) and `borrow_fee` (that day's IBKR snapshot, else the latest one on or before the day
    within `borrow.BORROW_FALLBACK_MAX_DAYS`; nullable when none). `borrow_asof` names the snapshot date
    each row's fee came from, so a fallback night is visible in the output."""
    if spine is None or spine.empty:
        return _empty_spine_with_columns(spine if spine is not None else pd.DataFrame(columns=SPINE_COLUMNS))
    missing = [c for c in SPINE_COLUMNS if c not in spine.columns]
    if missing:
        raise ValueError(f"join_short_side: spine is missing columns {missing}")

    parts = []
    for d, group in spine.groupby("date", sort=False):
        si = _si_for_date(load_short_interest, d).drop_duplicates("symbol")
        borrow, asof = _borrow_for_date(load_borrow, d)
        borrow = borrow.drop_duplicates("symbol")
        # `how="left"` on a de-duplicated right side never fans out, so the merge keeps `group`'s row
        # count and order; only its index resets, which we restore from `group.index` (pandas `merge`
        # always returns a fresh RangeIndex, even when the left side carried a meaningful one).
        merged = group.merge(si, left_on="ticker", right_on="symbol", how="left")
        if "symbol" in merged.columns:
            merged = merged.drop(columns=["symbol"])
        merged = merged.merge(borrow, left_on="ticker", right_on="symbol", how="left")
        if "symbol" in merged.columns:
            merged = merged.drop(columns=["symbol"])
        merged[BORROW_ASOF_COLUMN] = [asof if pd.notna(v) else None for v in merged["borrow_fee"]]
        merged.index = group.index
        parts.append(merged)
    out = pd.concat(parts)          # each row keeps its original spine index
    for c in ATTACHED_COLUMNS:
        if c not in out.columns:
            out[c] = pd.Series(dtype="float64")
    if BORROW_ASOF_COLUMN not in out.columns:
        out[BORROW_ASOF_COLUMN] = None
    return out.loc[spine.index].reset_index(drop=True)   # restore the spine's exact row order
