"""G6: expiration-day pinning on single names (RESEARCH/47 §2 G6).

Ni, Pearson & Poteshman (2005), "Stock price clustering on option expiration dates" (JFE):
grade A on existence, confined to expiration itself (`findings/market-analysis/RESEARCH/30
§4`). `findings/uw-daily-analysis/RESEARCH/91` already killed the day-D OI-pin strike as a
NEXT-DAY *index* level (SPY/QQQ, 17 touches, −11.4 points vs random placement). This module
tests something different: does a single name's OWN expiration-day close sit near the
high-OI strike in ITS OWN expiring series, more often than that same name sits near that same
strike on an ordinary Friday? Single names, not indices; the expiration day itself, not D+1.

Pure functions only — no file I/O. `engine/research/expiry_pinning_data.py` loads the OI
snapshot and screener closes this module consumes; `scripts/expiry_pinning.py` wires them
together and writes `data/backtest/g6_pins.parquet`.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Iterable

import numpy as np
import pandas as pd
from scipy import stats as sps

from engine import calendar as cal
from engine.config import ISSUE_TYPES

MCAP_MIN = 2e9                     # universe floor, RESEARCH/47 §2 G6 pre-registration
MIN_OI_CONTRACTS = 5_000           # total call+put OI in the expiring series at day -1
TOLERANCES = (0.0025, 0.005, 0.01)  # pre-stated: 0.25%, 0.5% (primary), 1.0%
PRIMARY_TOLERANCE = 0.005
_OCC_SUFFIX_RE = r"^(\d{6})([CP])\d{8}$"   # date, call/put, strike*1000 (same tail scripts/oi_build.py parses)


# ----------------------------------------------------------------------------- expiry calendar


@dataclass(frozen=True)
class ExpiryWeek:
    friday: date            # the calendar Friday this expiry week belongs to
    expiry: date             # the trading-day expiry (== friday, or the Thursday before a holiday Friday)
    is_monthly: bool          # third Friday of the month
    day_minus_1: date         # the trading day immediately before `expiry`
    prior_friday: date        # the previous week's expiry-adjusted Friday (same-strike baseline)


def _friday_to_trading_day(friday: date) -> date:
    """A Friday expiry, or the trading day before it when Friday is an NYSE holiday."""
    return friday if cal.is_trading_day(friday) else cal.prev_session(friday, 1)


def _is_third_friday(friday: date) -> bool:
    return 15 <= friday.day <= 21


def build_expiry_calendar(start: date, end: date) -> list[ExpiryWeek]:
    """Every calendar Friday in [start, end], holiday-adjusted to its trading-day expiry."""
    weeks: list[ExpiryWeek] = []
    d = start + timedelta(days=(4 - start.weekday()) % 7)   # first Friday on/after start
    while d <= end:
        expiry = _friday_to_trading_day(d)
        prior_friday = _friday_to_trading_day(d - timedelta(days=7))
        weeks.append(ExpiryWeek(friday=d, expiry=expiry, is_monthly=_is_third_friday(d),
                                day_minus_1=cal.prev_session(expiry, 1), prior_friday=prior_friday))
        d += timedelta(days=7)
    return weeks


# ----------------------------------------------------------------------------- OI snapshot parsing


def parse_oi_snapshot(raw: pd.DataFrame) -> pd.DataFrame:
    """Add `option_type` ('call'/'put') and `expiry` (date), parsed from `option_symbol` by
    stripping the `underlying_symbol` prefix and reading the standard OCC date+type+strike
    tail (`YYMMDD[C|P]########`), the same convention `scripts/oi_build.py`'s `CP` regex
    uses for option_type alone. Rows whose symbol does not start with their own underlying,
    or whose tail does not match, are dropped (RESEARCH/20 §5 documents no such rows on the
    panel; kept here as a fail-closed guard, not a silent swallow)."""
    if raw.empty:
        return raw.assign(option_type=pd.Series(dtype=object), expiry=pd.Series(dtype=object))
    syms = raw["option_symbol"].astype(str)
    unds = raw["underlying_symbol"].astype(str)
    suffixes = pd.Series(
        [s[len(u):] if s.startswith(u) else "" for s, u in zip(syms, unds)], index=raw.index)
    extracted = suffixes.str.extract(_OCC_SUFFIX_RE)
    ok = extracted[0].notna()
    out = raw.loc[ok].copy()
    out["option_type"] = np.where(extracted.loc[ok, 1] == "C", "call", "put")
    out["expiry"] = pd.to_datetime(extracted.loc[ok, 0], format="%y%m%d").dt.date
    return out.reset_index(drop=True)


# ----------------------------------------------------------------------------- strike selection


def combined_oi_by_strike(oi_df: pd.DataFrame) -> pd.DataFrame:
    """One row per strike, `oi` = call + put open interest combined."""
    if oi_df.empty:
        return pd.DataFrame({"strike": pd.Series(dtype=float), "oi": pd.Series(dtype=float)})
    out = (oi_df.groupby("strike", as_index=False)["curr_oi"].sum()
                .rename(columns={"curr_oi": "oi"}).sort_values("strike"))
    return out.reset_index(drop=True)


def _nearest(candidates: Iterable[float], ref: float) -> float:
    return float(min(candidates, key=lambda k: abs(k - ref)))


def pin_strike(strike_oi: pd.DataFrame, ref_close: float) -> float | None:
    """The strike with the largest combined call+put OI; ties broken by distance to `ref_close`."""
    if strike_oi.empty:
        return None
    max_oi = strike_oi["oi"].max()
    candidates = strike_oi.loc[strike_oi["oi"] == max_oi, "strike"]
    return _nearest(candidates, ref_close)


def max_pain_strike(oi_df: pd.DataFrame, ref_close: float) -> float | None:
    """The strike minimizing total ITM dollar payout to holders at expiration (standard
    max-pain), evaluated only at strikes that actually list. Ties broken by distance to
    `ref_close`."""
    strikes = np.sort(oi_df["strike"].unique())
    if len(strikes) == 0:
        return None
    calls, puts = oi_df[oi_df["option_type"] == "call"], oi_df[oi_df["option_type"] == "put"]
    call_k, call_oi = calls["strike"].to_numpy(dtype=float), calls["curr_oi"].to_numpy(dtype=float)
    put_k, put_oi = puts["strike"].to_numpy(dtype=float), puts["curr_oi"].to_numpy(dtype=float)
    payouts = np.array([
        float(np.sum(call_oi * np.maximum(s - call_k, 0.0)) + np.sum(put_oi * np.maximum(put_k - s, 0.0)))
        for s in strikes
    ])
    min_payout = payouts.min()
    candidates = strikes[np.isclose(payouts, min_payout, rtol=1e-9, atol=1e-6)]
    return _nearest(candidates, ref_close)


def second_largest_oi_strike(strike_oi: pd.DataFrame, exclude_strike: float | None,
                             ref_close: float) -> float | None:
    """The placebo strike: largest combined OI among strikes other than `exclude_strike`."""
    remaining = strike_oi if exclude_strike is None else strike_oi[strike_oi["strike"] != exclude_strike]
    return pin_strike(remaining, ref_close)


def nearest_strike_to_close(strikes: Iterable[float], ref_close: float | None) -> float | None:
    """The placebo strike: the listed strike nearest `ref_close` (the null a pin test must beat)."""
    values = [float(k) for k in strikes if k is not None and not (isinstance(k, float) and np.isnan(k))]
    if not values or ref_close is None:
        return None
    return _nearest(values, ref_close)


def nearest_strike_distance(strikes: Iterable[float], close: float | None) -> float:
    """|close - nearest listed strike of any type| / close, for the NPP diagnostic."""
    if close is None or close == 0:
        return float("nan")
    nearest = nearest_strike_to_close(strikes, close)
    return float("nan") if nearest is None else abs(close - nearest) / close


# ----------------------------------------------------------------------------- outcome metrics


def distance_frac(close: float, strike: float) -> float:
    return abs(close - strike) / close


def within_tolerance(close: float, strike: float, tol: float) -> bool:
    return distance_frac(close, strike) <= tol


# ----------------------------------------------------------------------------- universe filter


def passes_universe(issue_type: str | None, marketcap: float | None, total_oi: float | None,
                    mcap_min: float = MCAP_MIN, min_oi: float = MIN_OI_CONTRACTS) -> bool:
    """Optionable single name (`config.ISSUE_TYPES`, excludes ETF/index per RESEARCH/20 §6.1),
    market cap >= `mcap_min`, total day-(-1) OI in the expiring series >= `min_oi`."""
    if issue_type not in ISSUE_TYPES:
        return False
    if marketcap is None or not (marketcap >= mcap_min):
        return False
    if total_oi is None or not (total_oi >= min_oi):
        return False
    return True


# ----------------------------------------------------------------------------- NPP diagnostic


def npp_diagnostic(expiry_dist: Iterable[float], prior_dist: Iterable[float]) -> dict:
    """Does the expiration-day close's distance to the nearest strike (any strike) differ from
    the prior Friday's? Paired t-test and Wilcoxon signed-rank on (expiry_dist - prior_dist),
    finite pairs only."""
    e = np.asarray(list(expiry_dist), dtype=float)
    p = np.asarray(list(prior_dist), dtype=float)
    ok = np.isfinite(e) & np.isfinite(p)
    e, p = e[ok], p[ok]
    n = len(e)
    if n < 2:
        return {"n": int(n), "mean_expiry": float(e.mean()) if n else float("nan"),
                "mean_prior": float(p.mean()) if n else float("nan"),
                "median_expiry": float(np.median(e)) if n else float("nan"),
                "median_prior": float(np.median(p)) if n else float("nan"),
                "ttest_p": float("nan"), "wilcoxon_p": float("nan")}
    diff = e - p
    ttest_p = float(sps.ttest_1samp(diff, 0.0).pvalue)
    wilcoxon_p = float(sps.wilcoxon(e, p).pvalue) if np.any(diff != 0) else float("nan")
    return {"n": int(n), "mean_expiry": float(e.mean()), "mean_prior": float(p.mean()),
           "median_expiry": float(np.median(e)), "median_prior": float(np.median(p)),
           "ttest_p": ttest_p, "wilcoxon_p": wilcoxon_p}
