"""Live nightly replacements for the five conditions R1 computed from `features.parquet`
(`~/Development/findings/market-analysis/artifacts/edge-gaps/wb/results.md` §5, "What R2 must
replace"): `pct_52w_range` from the screener spine, the 5-day net call-OI build from the OI-changes
files, the crowding screen from the All Options tape, the 5-day IV-rank change from the screener,
and closes for grading (also from the screener spine). `flows.py` (C-LEAP, C-DP) and `tier1.py`
(C-VOL's ATM pair) are already live sources per R1 and are reused unchanged, not duplicated here.

Every function is null-safe (DESIGN/110 §1): a metric whose source file is missing for a given
night returns nothing for that night (the caller's merge leaves every ticker `NaN`/`None`), never
a computed `0`/`False`. `decile_flag` mirrors `retro.py`'s private `_decile_flag` (R1, frozen,
never imported from here) so a live night and a retrospective run of the same night agree on the
top-decile rule by construction, even though the underlying raw metric differs (documented in
`results.md`).
"""
from __future__ import annotations

import os
from datetime import date

import duckdb
import pandas as pd

from engine import calendar as cal
from engine.config import SCREENER_GLOB, STOCKS
from engine.watch import flows as F
from engine.watch.universe import load_screener_panel

OI_CHANGES_DIR = "OI changes"
OI_CHANGES_FILE = "chain-oi-changes-{d}.parquet"
OI_CHANGES_PREFIX, OI_CHANGES_SUFFIX = "chain-oi-changes-", ".parquet"
OI_WINDOW_SESSIONS = 5            # DESIGN/110 §2 C-OIBUILD: "5-day net call-OI build"
IVRANK_WINDOW_SESSIONS = 5        # C-IVUP's own lookback, "ivrank_chg_5d >= +10"
DECILE_THRESHOLD = 0.9            # top decile, DESIGN/110 §2 C-OIBUILD / C-CROWD

# C-CROWD's SQL half: the DESIGN/110 §2 literal reading, "top decile of `tot_prem / marketcap`" --
# UNSIGNED total premium (both sides, calls and puts), unlike R1's retrospective which used the
# task brief's named `netprem_mcap` (signed net premium). Same shape as `flows.py`'s `_DP_QUERY`
# (one DuckDB scan per session of the All Options tape), no floor -- every universe ticker's true
# total is wanted, not just the ones crossing a print-level threshold.
_TOTAL_PREMIUM_QUERY = """
SELECT underlying_symbol AS ticker, sum(premium) AS tot_prem
FROM read_parquet(?)
WHERE NOT canceled
GROUP BY 1
"""

# C-OIBUILD's SQL half: net call-OI build (`oi_diff_plain`, NOT the `oi_change` ratio -- see
# `scripts/oi_build.py`'s own module docstring for why that mistake is easy and silent) minus the
# matching put build, per ticker per day. Same option-symbol regex `scripts/oi_build.py` uses.
_OI_CP_REGEX = r"regexp_extract(option_symbol,'\d{6}([CP])',1)"
_OI_NET_QUERY = f"""
SELECT underlying_symbol AS ticker,
       sum(CASE WHEN {_OI_CP_REGEX}='C' THEN oi_diff_plain ELSE 0 END)
       - sum(CASE WHEN {_OI_CP_REGEX}='P' THEN oi_diff_plain ELSE 0 END) AS net
FROM read_parquet(?)
WHERE underlying_symbol IS NOT NULL
GROUP BY 1
"""


# =============================================================================================
# pct_52w_range (C-HIGH / C-LOW)
# =============================================================================================

def pct_52w_range(close, week_52_high, week_52_low) -> float | None:
    """`(close - week_52_low) / (week_52_high - week_52_low)` -- the same formula
    `scripts/chart.py`'s own `w52()` uses. `None` on any missing input or a degenerate
    (non-positive) range."""
    if close is None or week_52_high is None or week_52_low is None:
        return None
    try:
        c, hi, lo = float(close), float(week_52_high), float(week_52_low)
    except (TypeError, ValueError):
        return None
    if c != c or hi != hi or lo != lo or hi <= lo:      # NaN or degenerate
        return None
    return (c - lo) / (hi - lo)


def add_pct_52w_range(universe: pd.DataFrame) -> pd.DataFrame:
    out = universe.copy()
    out["pct_52w_range"] = [pct_52w_range(c, h, lo) for c, h, lo in
                             zip(out["close"], out["week_52_high"], out["week_52_low"])]
    return out


# =============================================================================================
# 5-day net call-OI build (C-OIBUILD's raw metric)
# =============================================================================================

def oi_changes_path(d: date, stocks_dir: str = STOCKS) -> str:
    return os.path.join(stocks_dir, OI_CHANGES_DIR, OI_CHANGES_FILE.format(d=d.isoformat()))


def available_oi_dates(stocks_dir: str = STOCKS) -> list[date]:
    directory = os.path.join(stocks_dir, OI_CHANGES_DIR)
    if not os.path.isdir(directory):
        return []
    out = []
    for name in os.listdir(directory):
        if name.startswith(OI_CHANGES_PREFIX) and name.endswith(OI_CHANGES_SUFFIX):
            try:
                out.append(date.fromisoformat(name[len(OI_CHANGES_PREFIX):-len(OI_CHANGES_SUFFIX)]))
            except ValueError:
                continue
    return sorted(out)


def oi_window_dates(d: date, stocks_dir: str = STOCKS, window: int = OI_WINDOW_SESSIONS) -> list[date]:
    """Up to `window` most recent OI-changes file dates on or before `d` (mirrors
    `scripts/oi_build.py:_panel_dates`; a file's own date is whatever calendar day the export
    landed on, so this is "up to `window` available files", not strictly five trading sessions)."""
    have = [x for x in available_oi_dates(stocks_dir) if x <= d]
    return have[-window:]


def oi_net_5d_for_day(d: date, stocks_dir: str = STOCKS,
                       con: duckdb.DuckDBPyConnection | None = None) -> pd.DataFrame:
    """`(ticker, oi_net_5d)`: the mean of the daily net call-minus-put OI build across the
    OI-changes files available on or before `d` (up to `OI_WINDOW_SESSIONS`). Empty when no file
    exists in the window at all -- the caller's merge then leaves every ticker `NaN` for `d`."""
    dates = oi_window_dates(d, stocks_dir)
    if not dates:
        return pd.DataFrame(columns=["ticker", "oi_net_5d"])
    con = con or duckdb.connect()
    frames = []
    for dd in dates:
        path = oi_changes_path(dd, stocks_dir)
        if os.path.exists(path):
            frames.append(con.execute(_OI_NET_QUERY, [path]).df())
    if not frames:
        return pd.DataFrame(columns=["ticker", "oi_net_5d"])
    allf = pd.concat(frames, ignore_index=True)
    return allf.groupby("ticker", as_index=False)["net"].mean().rename(columns={"net": "oi_net_5d"})


def build_oi_net_5d(dates: list[date], stocks_dir: str = STOCKS) -> pd.DataFrame:
    """`(ticker, date, oi_net_5d)` across every date in `dates`."""
    con = duckdb.connect()
    frames = [oi_net_5d_for_day(d, stocks_dir, con).assign(date=d) for d in dates]
    frames = [f for f in frames if not f.empty]
    if not frames:
        return pd.DataFrame(columns=["ticker", "date", "oi_net_5d"])
    return pd.concat(frames, ignore_index=True)


# =============================================================================================
# Unsigned total premium / marketcap (C-CROWD's raw metric)
# =============================================================================================

def all_options_file_exists(d: date, stocks_dir: str = STOCKS) -> bool:
    return os.path.exists(F.all_options_path(stocks_dir, d))


def dark_pool_file_exists(d: date, stocks_dir: str = STOCKS) -> bool:
    return os.path.exists(F.dark_pool_path(stocks_dir, d))


def total_premium_for_day(path: str, con: duckdb.DuckDBPyConnection | None = None) -> pd.DataFrame:
    """`(ticker, tot_prem)`: every ticker with at least one non-canceled print that day, unsigned
    total premium across both sides. Empty (not an error) when the day's file is absent."""
    if not path or not os.path.exists(path):
        return pd.DataFrame(columns=["ticker", "tot_prem"])
    con = con or duckdb.connect()
    return con.execute(_TOTAL_PREMIUM_QUERY, [path]).df()


def build_total_premium(dates: list[date], stocks_dir: str = STOCKS) -> pd.DataFrame:
    con = duckdb.connect()
    frames = []
    for d in dates:
        flags = total_premium_for_day(F.all_options_path(stocks_dir, d), con)
        if not flags.empty:
            frames.append(flags.assign(date=d))
    if not frames:
        return pd.DataFrame(columns=["ticker", "date", "tot_prem"])
    return pd.concat(frames, ignore_index=True)


# =============================================================================================
# 5-day IV-rank change (C-IVUP's raw metric)
# =============================================================================================

def build_ivrank_chg_5d(dates: list[date]) -> pd.DataFrame:
    """`(ticker, date, ivrank_chg_5d)`: today's screener `iv_rank` minus the same ticker's
    `iv_rank` `IVRANK_WINDOW_SESSIONS` trading sessions earlier. `None` (NaN) when either side's
    screener row, or `iv_rank` itself, is missing."""
    if not dates:
        return pd.DataFrame(columns=["ticker", "date", "ivrank_chg_5d"])
    prev_of = {d: cal.prev_session(d, IVRANK_WINDOW_SESSIONS) for d in dates}
    all_dates = sorted(set(dates) | set(prev_of.values()))
    panel = load_screener_panel(all_dates)[["ticker", "date", "iv_rank"]]
    today = panel[panel["date"].isin(dates)].rename(columns={"iv_rank": "iv_rank_today"})
    prev_frames = []
    for d, p in prev_of.items():
        sub = panel[panel["date"] == p][["ticker", "iv_rank"]].rename(columns={"iv_rank": "iv_rank_prev"})
        prev_frames.append(sub.assign(date=d))
    prev = (pd.concat(prev_frames, ignore_index=True) if prev_frames
            else pd.DataFrame(columns=["ticker", "iv_rank_prev", "date"]))
    merged = today.merge(prev, on=["ticker", "date"], how="outer")
    merged["ivrank_chg_5d"] = merged["iv_rank_today"] - merged["iv_rank_prev"]
    return merged[["ticker", "date", "ivrank_chg_5d"]]


# =============================================================================================
# Cross-sectional decile flag (shared by C-OIBUILD and C-CROWD)
# =============================================================================================

def decile_flag(series: pd.Series, threshold: float = DECILE_THRESHOLD) -> pd.Series:
    """Top-decile flag within one night's column of raw values: `rank(pct=True) >= threshold`
    among non-null values, `None` (object dtype throughout) where the raw value itself is null.
    Mirrors `retro.py`'s private `_decile_flag` (R1, unchanged) exactly, so the two rules agree by
    construction even where the raw metric they rank differs."""
    ranked = series.rank(pct=True, method="average")
    flag = (ranked >= threshold).astype(object)
    flag[series.isna()] = None
    return flag


# =============================================================================================
# Closes for grading (h5/h10/h21 SPY excess)
# =============================================================================================

def load_closes(tickers, dates, stocks_dir: str = STOCKS) -> dict[tuple[str, date], float]:
    """`{(ticker, date): close}` from the screener spine for exactly the (ticker, date) pairs
    asked for (not a cross product) -- a pair with no screener row is simply absent from the
    result, never a `0.0`."""
    tickers, dates = set(tickers), set(dates)
    if not tickers or not dates:
        return {}
    con = duckdb.connect()
    tick_list = ", ".join(f"'{t}'" for t in sorted(tickers))
    date_list = ", ".join(f"DATE '{d.isoformat()}'" for d in sorted(dates))
    q = (f"SELECT ticker, date, close FROM read_parquet('{stocks_dir}/{SCREENER_GLOB}') "
         f"WHERE ticker IN ({tick_list}) AND date IN ({date_list})")
    df = con.execute(q).df()
    if df.empty:
        return {}
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return {(r.ticker, r.date): float(r.close) for r in df.itertuples(index=False) if r.close == r.close}
