"""Data access for the marked S-B layer and the nightly step (DESIGN/80 §5.2, §7): SPY/QQQ
`daily_contract` rows on an entry session, closes for settlement, the panel's session list.
"""
from __future__ import annotations

from datetime import date
from typing import Iterable

import pandas as pd

from engine.config import PRICES
from engine.mart import store
from engine.mart.store import scan_sql
from engine.strategies.sa_data import as_dates

CONTRACTS = "daily_contract"
SETTLE_PRICES, SETTLE_PRINTS = "prices", "daily_contract"


def load_entry_rows(con, underlyings: Iterable[str], d: date) -> pd.DataFrame:
    """Every daily_contract row of the underlyings on session d (empty when the day is absent)."""
    if not store.has_partition(CONTRACTS, d):
        return pd.DataFrame()
    con.register("sb_want_u", pd.DataFrame({"underlying_symbol": sorted(set(underlyings))}))
    df = con.execute(f"""
        SELECT c.* FROM read_parquet('{store.partition_path(CONTRACTS, d)}') c
        JOIN sb_want_u USING (underlying_symbol)""").df()
    return as_dates(df, ("date", "expiry"))


def load_closes(con, tickers: Iterable[str], start: date | None = None, end: date | None = None) -> dict[tuple[str, date], float]:
    con.register("sb_want_tk", pd.DataFrame({"ticker": sorted(set(tickers))}))
    where = []
    if start is not None:
        where.append(f"p.date >= DATE '{start.isoformat()}'")
    if end is not None:
        where.append(f"p.date <= DATE '{end.isoformat()}'")
    clause = (" WHERE " + " AND ".join(where)) if where else ""
    rows = con.execute(f"SELECT p.ticker, p.date, p.close FROM read_parquet('{PRICES}') p JOIN sb_want_tk USING (ticker){clause}").fetchall()
    return {(t, pd.Timestamp(d).date()): float(c) for t, d, c in rows if c is not None}


def settle_close(con, ticker: str, d: date) -> tuple[float | None, str | None]:
    """The underlying's close on d: prices.parquet first, else the last print's underlying price."""
    px = load_closes(con, [ticker], d, d).get((ticker, d))
    if px is not None:
        return px, SETTLE_PRICES
    if not store.has_partition(CONTRACTS, d):
        return None, None
    row = con.execute(f"""
        SELECT arg_max(underlying_last, last_ts) FROM read_parquet('{store.partition_path(CONTRACTS, d)}')
        WHERE underlying_symbol = ? AND underlying_last IS NOT NULL""", [ticker]).fetchone()
    if row and row[0] is not None:
        return float(row[0]), SETTLE_PRINTS
    return None, None


def panel_sessions() -> list[date]:
    return store.available_dates(CONTRACTS)
