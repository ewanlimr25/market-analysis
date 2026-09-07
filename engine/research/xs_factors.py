"""Pure factor-construction functions for G4 (IV spread, put skew) and G5 (O/S ratio)
(RESEARCH/47 §2 G4/G5; RESEARCH/30 §1: Bali-Hovakimian 2009, Cremers-Weinbaum 2010,
Xing-Zhang-Zhao 2010, Johnson-So 2012).

No I/O anywhere in this module -- every function takes plain pandas/numpy objects so the delta
matching, interpolation and O/S arithmetic can be tested on a synthetic chain
(`tests/test_cross_section.py`). `engine.research.cross_section` is the only caller that touches
the mart or the screener spine.

Delta convention (matches `engine.mart.daily_contract` and the CBOE chain loader): call delta in
(0, 1], put delta in [-1, 0). A contract whose delta violates that sign is treated as noise and
excluded by `clean_deltas` before any matching happens (RESEARCH/20 §4.2 notes a small tail of
implausible last-print deltas on thin contracts).

Targets, pre-registered (RESEARCH/47 §2 G4, this branch's task spec):
  ATM call / ATM put   -> nearest |delta| to 0.50 (`TARGET_CALL_DELTA` / `TARGET_PUT_DELTA_ATM`)
  25-delta put          -> nearest delta to -0.25 (`TARGET_PUT_DELTA_25D`)
  IV spread              = atm_call_iv - atm_put_iv                    (Bali-Hovakimian sign: + predicts +)
  put skew               = put_25d_iv - atm_call_iv                    (Xing-Zhang-Zhao: high skew predicts -)
  O/S ratio               = total option contract volume * 100 / stock share volume  (Johnson-So: high O/S predicts -)
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

NEAR_30D_TARGET_DAYS = 30
TARGET_CALL_DELTA = 0.50
TARGET_PUT_DELTA_ATM = -0.50
TARGET_PUT_DELTA_25D = -0.25
ELIGIBLE_CALL_DELTA_BAND = (0.20, 0.60)     # universe eligibility band (|delta|), RESEARCH/47 G4 task spec
ELIGIBLE_PUT_DELTA_BAND = (-0.60, -0.20)
CONTRACT_MULTIPLIER = 100                    # shares per option contract, Johnson-So O/S

METHOD_EXACT, METHOD_INTERP, METHOD_NEAREST = "exact", "interp", "nearest"


@dataclass(frozen=True)
class DeltaMatch:
    """One delta-matched IV read. `iv` is `None` when the contract pool is empty."""
    iv: float | None
    method: str | None            # "exact" | "interp" | "nearest" | None (empty pool)
    delta_used: float | None      # the single delta used (nearest) or None when interpolated
    delta_lo: float | None        # bracket low delta (interp only)
    delta_hi: float | None        # bracket high delta (interp only)
    n_points: int


def clean_deltas(contracts: pd.DataFrame, sign: int) -> pd.DataFrame:
    """Drop rows whose `delta` does not carry the expected sign (`sign` = +1 for calls, -1 for
    puts) or whose `iv` is not a finite positive number. Returns a copy; never mutates the input."""
    if contracts is None or contracts.empty:
        return pd.DataFrame(columns=["delta", "iv"])
    work = contracts.dropna(subset=["delta", "iv"]).copy()
    work["delta"] = pd.to_numeric(work["delta"], errors="coerce")
    work["iv"] = pd.to_numeric(work["iv"], errors="coerce")
    work = work.dropna(subset=["delta", "iv"])
    if sign > 0:
        work = work[(work["delta"] > 0) & (work["delta"] <= 1.0)]
    else:
        work = work[(work["delta"] < 0) & (work["delta"] >= -1.0)]
    work = work[np.isfinite(work["iv"]) & (work["iv"] > 0)]
    return work


def match_iv_at_delta(contracts: pd.DataFrame, target_delta: float) -> DeltaMatch:
    """The IV at `target_delta`, interpolated when two priced contracts bracket it, else the
    single nearest contract (flagged `"nearest"`). `contracts` must already be sign-cleaned
    (`clean_deltas`) and carry one option type. Empty pool -> `DeltaMatch(None, None, ...)`."""
    if contracts is None or contracts.empty:
        return DeltaMatch(None, None, None, None, None, 0)
    work = contracts.drop_duplicates(subset=["delta"]).sort_values("delta")
    deltas = work["delta"].to_numpy(dtype=float)
    ivs = work["iv"].to_numpy(dtype=float)
    n = len(deltas)
    exact = np.isclose(deltas, target_delta)
    if exact.any():
        idx = int(np.nonzero(exact)[0][0])
        return DeltaMatch(float(ivs[idx]), METHOD_EXACT, float(deltas[idx]), None, None, n)
    below = np.nonzero(deltas <= target_delta)[0]
    above = np.nonzero(deltas >= target_delta)[0]
    if len(below) and len(above):
        lo, hi = int(below[-1]), int(above[0])
        d_lo, d_hi = float(deltas[lo]), float(deltas[hi])
        iv_lo, iv_hi = float(ivs[lo]), float(ivs[hi])
        weight = (target_delta - d_lo) / (d_hi - d_lo)
        return DeltaMatch(iv_lo + weight * (iv_hi - iv_lo), METHOD_INTERP, None, d_lo, d_hi, n)
    nearest = int(np.argmin(np.abs(deltas - target_delta)))
    return DeltaMatch(float(ivs[nearest]), METHOD_NEAREST, float(deltas[nearest]), None, None, n)


def nearest_expiry(expiries_with_dte_cal: pd.DataFrame, target_days: int = NEAR_30D_TARGET_DAYS):
    """The expiry whose `dte_cal` is closest to `target_days`; ties broken by the smaller expiry
    (the nearer date). `expiries_with_dte_cal` needs distinct `expiry`/`dte_cal` columns."""
    if expiries_with_dte_cal is None or expiries_with_dte_cal.empty:
        return None
    work = expiries_with_dte_cal.drop_duplicates(subset=["expiry"]).copy()
    work["_dist"] = (work["dte_cal"] - target_days).abs()
    work = work.sort_values(["_dist", "expiry"])
    return work.iloc[0]["expiry"]


def has_delta_band(contracts: pd.DataFrame, band: tuple[float, float]) -> bool:
    """Whether any (sign-cleaned) contract's delta falls within `band` (inclusive)."""
    if contracts is None or contracts.empty:
        return False
    lo, hi = band
    return bool(((contracts["delta"] >= lo) & (contracts["delta"] <= hi)).any())


def iv_spread(atm_call: DeltaMatch, atm_put: DeltaMatch) -> float | None:
    """ATM call IV minus ATM put IV (Bali-Hovakimian / Cremers-Weinbaum sign)."""
    if atm_call.iv is None or atm_put.iv is None:
        return None
    return atm_call.iv - atm_put.iv


def put_skew(put_25d: DeltaMatch, atm_call: DeltaMatch) -> float | None:
    """25-delta put IV minus ATM (50-delta) call IV (Xing-Zhang-Zhao smirk)."""
    if put_25d.iv is None or atm_call.iv is None:
        return None
    return put_25d.iv - atm_call.iv


def os_ratio(call_volume: float | None, put_volume: float | None, total_volume: float | None,
             avg30_volume: float | None) -> tuple[float | None, str | None]:
    """Johnson-So O/S: total option contract volume * 100 / stock share volume that day, falling
    back to the 30-day average stock volume when the day's own volume is missing or non-positive
    (RESEARCH/20 §6, `total_volume` / `avg30_volume`). Returns `(ratio, source)`, `source` in
    `{"total_volume", "avg30_volume", None}`."""
    opt_vol = (call_volume or 0) + (put_volume or 0)
    if total_volume is not None and np.isfinite(total_volume) and total_volume > 0:
        return opt_vol * CONTRACT_MULTIPLIER / total_volume, "total_volume"
    if avg30_volume is not None and np.isfinite(avg30_volume) and avg30_volume > 0:
        return opt_vol * CONTRACT_MULTIPLIER / avg30_volume, "avg30_volume"
    return None, None
