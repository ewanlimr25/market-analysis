"""C-LEAP and C-DP: daily flow aggregates from the raw All Options and Dark Pool exports
(`DESIGN/110-watch-basket.md` §2). Both are one DuckDB scan per session, column-pruned and
predicate-pushed on `premium` (the dominant filter -- most prints never come close to either
floor), grouped by ticker.
"""
from __future__ import annotations

import os
from datetime import date

import duckdb
import pandas as pd

from engine.config import ALL_OPTIONS_FILE, STOCKS

# Not in engine.config (only ALL_OPTIONS_FILE/HOT_CHAINS_FILE/SCREENER_FILE live there today);
# defined here since this is the only module in the engine that reads the raw Dark Pool export.
DARK_POOL_FILE = "Dark pool/dp-eod-report-{d}.parquet"

# RESEARCH/20 §2.2: the single-leg upstream_condition_detail codes (this book's own list, not the
# RESEARCH/20 "clean single-leg lane" set -- `mesl` and `tlet` are included per the task brief).
SINGLE_LEG_CODES = ("auto", "slan", "isoi", "slft", "tlet", "mesl")
C_LEAP_MIN_PREMIUM = 1_000_000.0
C_LEAP_MIN_DTE_CAL = 180
C_DP_MIN_PREMIUM = 5_000_000.0

_LEAP_QUERY = """
SELECT underlying_symbol AS ticker, sum(premium) AS call_ask_premium
FROM read_parquet(?)
WHERE NOT canceled AND side = 'ask' AND option_type = 'call'
  AND upstream_condition_detail IN ({codes})
  AND date_diff('day', CAST(? AS DATE), expiry) >= {min_dte}
GROUP BY 1
HAVING sum(premium) >= {min_prem}
"""

_DP_QUERY = """
SELECT ticker, sum(premium) AS dp_premium
FROM read_parquet(?)
WHERE NOT canceled
GROUP BY 1
HAVING sum(premium) >= {min_prem}
"""


def all_options_path(stocks_dir: str, d: date) -> str:
    return os.path.join(stocks_dir, ALL_OPTIONS_FILE.format(d=d.isoformat()))


def dark_pool_path(stocks_dir: str, d: date) -> str:
    return os.path.join(stocks_dir, DARK_POOL_FILE.format(d=d.isoformat()))


def leap_flags_for_day(path: str, d: date, con: duckdb.DuckDBPyConnection | None = None) -> pd.DataFrame:
    """`(ticker, call_ask_premium)` for tickers whose single-leg, ask-side, DTE>=180 call premium
    that day is >= `C_LEAP_MIN_PREMIUM`. Empty (not an error) when the day's file is absent."""
    if not path or not os.path.exists(path):
        return pd.DataFrame(columns=["ticker", "call_ask_premium"])
    con = con or duckdb.connect()
    codes = ", ".join(f"'{c}'" for c in SINGLE_LEG_CODES)
    q = _LEAP_QUERY.format(codes=codes, min_dte=C_LEAP_MIN_DTE_CAL, min_prem=C_LEAP_MIN_PREMIUM)
    return con.execute(q, [path, d.isoformat()]).df()


def dp_flags_for_day(path: str, con: duckdb.DuckDBPyConnection | None = None) -> pd.DataFrame:
    """`(ticker, dp_premium)` for tickers whose dark-pool premium that day is >= `C_DP_MIN_PREMIUM`.
    Empty (not an error) when the day's file is absent."""
    if not path or not os.path.exists(path):
        return pd.DataFrame(columns=["ticker", "dp_premium"])
    con = con or duckdb.connect()
    q = _DP_QUERY.format(min_prem=C_DP_MIN_PREMIUM)
    return con.execute(q, [path]).df()


def build_leap_flags(dates: list[date], stocks_dir: str = STOCKS) -> pd.DataFrame:
    con = duckdb.connect()
    frames = []
    for d in dates:
        flags = leap_flags_for_day(all_options_path(stocks_dir, d), d, con)
        if not flags.empty:
            frames.append(flags.assign(date=d))
    if not frames:
        return pd.DataFrame(columns=["ticker", "date", "call_ask_premium"])
    return pd.concat(frames, ignore_index=True)


def build_dp_flags(dates: list[date], stocks_dir: str = STOCKS) -> pd.DataFrame:
    con = duckdb.connect()
    frames = []
    for d in dates:
        flags = dp_flags_for_day(dark_pool_path(stocks_dir, d), con)
        if not flags.empty:
            frames.append(flags.assign(date=d))
    if not frames:
        return pd.DataFrame(columns=["ticker", "date", "dp_premium"])
    return pd.concat(frames, ignore_index=True)
