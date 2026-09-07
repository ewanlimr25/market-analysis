"""Nightly universe and screener spine (`DESIGN/110-watch-basket.md` §1).

"Screener names with `issue_type` Common Stock or ADR, `marketcap >= $1B`, `close >= $10`, options
coverage in `daily_contract` that day." All reads go through DuckDB, column-pruned, over
`~/Documents/Stocks` (screener) and `data/mart/daily_contract` (coverage).
"""
from __future__ import annotations

from datetime import date

import duckdb
import pandas as pd

from engine.config import SCREENER_GLOB, STOCKS
from engine.mart import store

UNIVERSE_ISSUE_TYPES = ("Common Stock", "ADR")
UNIVERSE_MIN_MARKETCAP = 1e9
UNIVERSE_MIN_CLOSE = 10.0

SCREENER_COLUMNS = (
    "date", "ticker", "issue_type", "is_index", "marketcap", "close",
    "week_52_high", "week_52_low", "iv30d", "iv_rank", "next_earnings_date", "sector",
    "bullish_premium", "bearish_premium", "net_call_premium", "net_put_premium",
)


def load_screener_panel(dates: list[date], stocks_dir: str = STOCKS) -> pd.DataFrame:
    """One row per (ticker, date) for exactly `dates`, `SCREENER_COLUMNS` only."""
    if not dates:
        return pd.DataFrame({c: pd.Series(dtype=object) for c in SCREENER_COLUMNS})
    con = duckdb.connect()
    date_list = ", ".join(f"DATE '{d.isoformat()}'" for d in sorted(set(dates)))
    cols = ", ".join(SCREENER_COLUMNS)
    q = (f"SELECT {cols} FROM read_parquet('{stocks_dir}/{SCREENER_GLOB}') "
         f"WHERE date IN ({date_list})")
    df = con.execute(q).df()
    df["date"] = pd.to_datetime(df["date"]).dt.date
    df["next_earnings_date"] = pd.to_datetime(df["next_earnings_date"]).dt.date
    return df


def contract_coverage(dates: list[date]) -> pd.DataFrame:
    """One row per (ticker, date) with a `daily_contract` row on that date, restricted to `dates`."""
    if not dates:
        return pd.DataFrame(columns=["ticker", "date"])
    con = duckdb.connect()
    df = con.execute(
        f"SELECT DISTINCT underlying_symbol AS ticker, date "
        f"FROM {store.scan_sql('daily_contract')}").df()
    df["date"] = pd.to_datetime(df["date"]).dt.date
    wanted = set(dates)
    return df[df["date"].isin(wanted)].reset_index(drop=True)


def filter_universe(screener_panel: pd.DataFrame, coverage: pd.DataFrame) -> pd.DataFrame:
    """§1's filter, applied to an already-loaded screener panel and coverage frame (pure, no I/O
    -- tests exercise this directly on synthetic frames)."""
    if screener_panel.empty:
        return screener_panel
    df = screener_panel[
        screener_panel["issue_type"].isin(UNIVERSE_ISSUE_TYPES)
        & (screener_panel["marketcap"] >= UNIVERSE_MIN_MARKETCAP)
        & (screener_panel["close"] >= UNIVERSE_MIN_CLOSE)
    ]
    if coverage.empty:
        return df.iloc[0:0]
    covered = coverage.assign(_covered=True)
    out = df.merge(covered, on=["ticker", "date"], how="inner")
    return out.drop(columns=["_covered"]).reset_index(drop=True)


def build_universe(dates: list[date]) -> pd.DataFrame:
    """The full §1 pipeline: load the screener panel and `daily_contract` coverage for `dates`,
    then filter. This is the only function in this module that touches disk end-to-end."""
    screener = load_screener_panel(dates)
    coverage = contract_coverage(dates)
    return filter_universe(screener, coverage)
