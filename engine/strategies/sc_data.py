"""Data access for S-C (DESIGN/90 §2, §5): the screener rows of an entry session with the 20-day
dollar ADV attached, and the `daily_contract` rows of a set of underlyings on that session.
Read-only over the mart and the panel export; every S-C layer goes through here."""
from __future__ import annotations

from datetime import date
from typing import Iterable

import pandas as pd

from engine.config import PRICES, SCREENER_FILE, STOCKS
from engine.mart import store
from engine.strategies.sa_data import as_dates

CONTRACTS = "daily_contract"
ADV_WINDOW_SESSIONS = 20          # F4: mean close x volume over the 20 sessions ending at t
ADV_MIN_SESSIONS = 10
SCREENER_COLUMNS = ("date", "ticker", "issue_type", "is_index", "close", "marketcap", "iv30d",
                    "next_earnings_date", "sector")


def screener_path(d: date, stocks_dir: str = STOCKS) -> str:
    return f"{stocks_dir}/{SCREENER_FILE.format(d=d.isoformat())}"


def load_screener_rows(con, d: date, stocks_dir: str = STOCKS) -> pd.DataFrame:
    """The screener export of session `d`, `SCREENER_COLUMNS` only; empty when the file is absent."""
    import os
    path = screener_path(d, stocks_dir)
    if not os.path.exists(path):
        return pd.DataFrame(columns=SCREENER_COLUMNS)
    df = con.execute(f"SELECT {', '.join(SCREENER_COLUMNS)} FROM read_parquet('{path}')").df()
    df["date"] = pd.to_datetime(df["date"]).dt.date
    df["next_earnings_date"] = pd.to_datetime(df["next_earnings_date"], errors="coerce").dt.date
    return df


def adv_usd_20d(con, tickers: Iterable[str], d: date, prices_path: str = PRICES) -> dict[str, float]:
    """F4 input: mean close x volume over the 20 sessions of `prices.parquet` ending at `d` (the
    last session on or before `d`); absent when fewer than ADV_MIN_SESSIONS sessions exist."""
    con.register("sc_adv_tk", pd.DataFrame({"ticker": sorted(set(tickers))}))
    try:
        rows = con.execute(f"""
            WITH p AS (SELECT p.ticker, p.date, p.close * p.volume AS dv
                       FROM read_parquet('{prices_path}') p JOIN sc_adv_tk USING (ticker)
                       WHERE p.date <= DATE '{d.isoformat()}' AND p.close IS NOT NULL AND p.volume IS NOT NULL),
                 r AS (SELECT ticker, dv, row_number() OVER (PARTITION BY ticker ORDER BY date DESC) rn FROM p)
            SELECT ticker, avg(dv), count(dv) FROM r WHERE rn <= {ADV_WINDOW_SESSIONS} GROUP BY ticker""").fetchall()
    finally:
        con.unregister("sc_adv_tk")
    return {t: float(a) for t, a, n in rows if n >= ADV_MIN_SESSIONS and a is not None}


def load_entry_universe(con, d: date, stocks_dir: str = STOCKS, prices_path: str = PRICES) -> pd.DataFrame:
    """Screener rows of `d` with `adv_usd_20d` attached (NaN when unknown, which fails F4)."""
    scr = load_screener_rows(con, d, stocks_dir)
    if scr.empty:
        return scr.assign(adv_usd_20d=pd.Series(dtype="float64"))
    adv = adv_usd_20d(con, scr["ticker"], d, prices_path)
    return scr.assign(adv_usd_20d=scr["ticker"].map(adv).astype("float64"))


def load_contract_rows(con, underlyings: Iterable[str], d: date) -> pd.DataFrame:
    """Every daily_contract row of the underlyings on session d (empty when the day is absent)."""
    if not store.has_partition(CONTRACTS, d):
        return pd.DataFrame()
    con.register("sc_want_u", pd.DataFrame({"underlying_symbol": sorted(set(underlyings))}))
    try:
        df = con.execute(f"""
            SELECT c.* FROM read_parquet('{store.partition_path(CONTRACTS, d)}') c
            JOIN sc_want_u USING (underlying_symbol)""").df()
    finally:
        con.unregister("sc_want_u")
    return as_dates(df, ("date", "expiry"))


def panel_sessions() -> list[date]:
    return store.available_dates(CONTRACTS)


# ---- R3: wing history and settlement (DESIGN/90 §3) -------------------------------------------------

def load_rows_for_underlyings(con, underlyings: Iterable[str], dates: Iterable[date]) -> pd.DataFrame:
    """Every daily_contract row of the underlyings on the given sessions (the wings' IV lookback)."""
    want = [d for d in sorted(set(dates)) if store.has_partition(CONTRACTS, d)]
    names = sorted(set(underlyings))
    if not want or not names:
        return pd.DataFrame()
    return pd.concat([load_contract_rows(con, names, d) for d in want], ignore_index=True)


def prices_through(con, prices_path: str = PRICES) -> date | None:
    row = con.execute(f"SELECT max(date) FROM read_parquet('{prices_path}')").fetchone()
    return pd.Timestamp(row[0]).date() if row and row[0] is not None else None


class PrintCloses:
    """`.get((ticker, d))` -> the last print's underlying price on session d, queried on demand and
    cached (the settlement fallback when Yahoo has no close; only a few rows ever need it)."""

    def __init__(self, con):
        self._con, self._cache = con, {}

    def get(self, key: tuple[str, date], default=None):
        if key not in self._cache:
            self._cache[key] = self._query(*key)
        value = self._cache[key]
        return default if value is None else value

    def _query(self, ticker: str, d: date) -> float | None:
        if not store.has_partition(CONTRACTS, d):
            return None
        row = self._con.execute(f"""
            SELECT arg_max(underlying_last, last_ts) FROM read_parquet('{store.partition_path(CONTRACTS, d)}')
            WHERE underlying_symbol = ? AND underlying_last IS NOT NULL""", [ticker]).fetchone()
        return float(row[0]) if row and row[0] is not None else None
