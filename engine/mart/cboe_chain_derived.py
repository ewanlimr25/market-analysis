"""Derived analytics over a stored CBOE chain (RESEARCH/47 §2 G8; artifacts/edge-gaps/g8).

Pure functions over the DataFrame `engine.mart.cboe_chain.parse_chain` / `load_chain` returns
(columns: `symbol, expiry, strike, right, ..., bid, ask, mid, iv, delta, gamma, ..., open_interest,
volume, underlying_price, ...`). No I/O; every function takes and returns plain pandas objects so
they can be tested on a synthetic chain (`tests/test_cboe_chain_derived.py`) or run over
`load_chain(...)` output.

GEX convention: per contract, `gex = gamma * open_interest * CONTRACT_MULTIPLIER * underlying_price`,
sign +1 for calls and -1 for puts — dealers are assumed net long gamma from calls and net short
gamma from puts (the public is net long calls and net long puts against them). This is the same
formula `unusual-whales-mcp/shared/analysis_gex.py:compute_gex_per_strike` uses, chosen so the CBOE
chain's total GEX is directly comparable to `uw options-structure gex` (RESEARCH/47 G8 item 4),
not because it is the only defensible convention — GEX sign conventions vary across the industry
and this one is not a fitted or frozen parameter.
"""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

CONTRACT_MULTIPLIER = 100  # shares per option contract
TARGET_PUT_DELTA = -0.25
TARGET_CALL_DELTA = 0.25
NEAR_30D_TARGET_DAYS = 30


def _numeric(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    out = df.copy()
    for c in cols:
        if c in out.columns:
            out[c] = pd.to_numeric(out[c], errors="coerce")
    return out


def gex_per_strike(df: pd.DataFrame) -> pd.DataFrame:
    """`DataFrame(strike, gex)`, one row per strike, summed across expiries and both rights.

    Rows with non-positive gamma or open interest are dropped (no dealer gamma exposure to
    attribute), matching `unusual-whales-mcp`'s filter.
    """
    schema = ["strike", "gex"]
    if df is None or df.empty:
        return pd.DataFrame(columns=schema)
    work = _numeric(df, ["gamma", "open_interest", "underlying_price", "strike"])
    work = work.dropna(subset=["gamma", "open_interest", "underlying_price", "strike"])
    work = work[(work["gamma"] > 0) & (work["open_interest"] > 0)]
    if work.empty:
        return pd.DataFrame(columns=schema)
    sign = np.where(work["right"] == "C", 1.0, -1.0)
    work = work.assign(gex=work["gamma"] * work["open_interest"] * CONTRACT_MULTIPLIER * work["underlying_price"] * sign)
    return work.groupby("strike", as_index=False)["gex"].sum().sort_values("strike").reset_index(drop=True)


def total_gex(df: pd.DataFrame) -> float:
    """Sum of `gex_per_strike`; 0.0 on an empty or all-filtered chain."""
    per_strike = gex_per_strike(df)
    return float(per_strike["gex"].sum()) if len(per_strike) else 0.0


def _iv_at_delta(sub: pd.DataFrame, right: str, target_delta: float) -> float | None:
    """Linear interpolation of `iv` on `delta` for one `right`, at `target_delta`. `None` if
    fewer than two priced points exist for that right. Flat-extrapolates outside the observed
    delta range (`numpy.interp` default), since a chain rarely straddles +-0.25 delta exactly."""
    rows = sub[sub["right"] == right].dropna(subset=["delta", "iv"])
    rows = rows[rows["iv"] > 0]
    if len(rows) < 2:
        return None
    rows = rows.sort_values("delta")
    return float(np.interp(target_delta, rows["delta"].to_numpy(), rows["iv"].to_numpy()))


def skew_25d(df: pd.DataFrame, expiry: date) -> dict:
    """25-delta put IV minus 25-delta call IV for one expiry, both interpolated on delta.

    Returns `{"expiry", "put_iv_25d", "call_iv_25d", "skew_25d"}`; the IV fields and `skew_25d`
    are `None` when either side cannot be interpolated (fewer than two priced contracts).
    """
    sub = df[df["expiry"] == expiry] if len(df) else df
    put_iv = _iv_at_delta(sub, "P", TARGET_PUT_DELTA) if len(sub) else None
    call_iv = _iv_at_delta(sub, "C", TARGET_CALL_DELTA) if len(sub) else None
    skew = None if put_iv is None or call_iv is None else put_iv - call_iv
    return {"expiry": expiry, "put_iv_25d": put_iv, "call_iv_25d": call_iv, "skew_25d": skew}


def skew_by_expiry(df: pd.DataFrame) -> pd.DataFrame:
    """`skew_25d` for every expiry present, sorted by expiry."""
    if df is None or df.empty:
        return pd.DataFrame(columns=["expiry", "put_iv_25d", "call_iv_25d", "skew_25d"])
    expiries = sorted(df["expiry"].dropna().unique())
    return pd.DataFrame([skew_25d(df, e) for e in expiries])


def atm_iv(df: pd.DataFrame, expiry: date) -> float | None:
    """Mean of the call and put IV at the strike nearest `underlying_price` for one expiry.
    `None` if the expiry has no priced contracts."""
    sub = df[(df["expiry"] == expiry)].dropna(subset=["strike", "underlying_price"]) if len(df) else df
    if sub is None or sub.empty:
        return None
    spot = float(sub["underlying_price"].iloc[0])
    atm_strike = float(sub.iloc[(sub["strike"] - spot).abs().argsort().iloc[0]]["strike"])
    at_strike = sub[sub["strike"] == atm_strike].dropna(subset=["iv"])
    at_strike = at_strike[at_strike["iv"] > 0]
    if at_strike.empty:
        return None
    return float(at_strike["iv"].mean())


def front_expiry(df: pd.DataFrame) -> date | None:
    """The nearest (smallest) expiry present in the chain."""
    if df is None or df.empty:
        return None
    return min(df["expiry"].dropna())


def nearest_expiry_to(df: pd.DataFrame, asof: date, target_days: int = NEAR_30D_TARGET_DAYS) -> date | None:
    """The expiry whose `(expiry - asof).days` is closest to `target_days`."""
    if df is None or df.empty:
        return None
    expiries = sorted(df["expiry"].dropna().unique())
    if not expiries:
        return None
    return min(expiries, key=lambda e: abs((e - asof).days - target_days))


def atm_iv_summary(df: pd.DataFrame, asof: date) -> dict:
    """The front-expiry ATM IV and the ATM IV of the expiry nearest 30 calendar days out.

    Returns `{"front_expiry", "front_atm_iv", "near_30d_expiry", "near_30d_atm_iv"}`. When the
    front expiry is itself the nearest-to-30d one, both entries name the same expiry (that is
    correct, not a bug: a chain with only one usable expiry has no second point).
    """
    front = front_expiry(df)
    near = nearest_expiry_to(df, asof)
    return {"front_expiry": front, "front_atm_iv": atm_iv(df, front) if front else None,
            "near_30d_expiry": near, "near_30d_atm_iv": atm_iv(df, near) if near else None}


def put_call_oi_ratio(df: pd.DataFrame) -> float | None:
    """Sum(put open_interest) / Sum(call open_interest) over the whole chain. `None` if call OI
    is zero or the chain is empty (avoids a divide-by-zero, not a claim that the ratio is 0 or inf)."""
    if df is None or df.empty:
        return None
    work = _numeric(df, ["open_interest"]).dropna(subset=["open_interest"])
    call_oi = float(work.loc[work["right"] == "C", "open_interest"].sum())
    put_oi = float(work.loc[work["right"] == "P", "open_interest"].sum())
    if call_oi == 0:
        return None
    return put_oi / call_oi
