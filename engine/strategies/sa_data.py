"""Data access for the S-A backtest: pulls the mart slices the strategy needs and builds the
MarkResolver's model inputs (DESIGN/70 §2 tier 3: spot from the price panel, IV from the
screener's iv30d scaled by the contract's last smile ratio, spread from the name's recent
late spreads). All reads go through DuckDB over data/mart and data/prices.parquet.
"""
from __future__ import annotations

from datetime import date
from typing import Iterable

import duckdb
import pandas as pd

from engine import calendar as cal
from engine import marking as M
from engine.config import MODEL_IV_LOOKBACK, MODEL_SPREAD_LOOKBACK, PRICES, SCREENER_GLOB, STOCKS
from engine.mart.store import scan_sql

EVENTS, CONTRACTS = "earnings_events", "daily_contract"


EVENT_DATE_COLS = ("E", "pre", "post", "date")
CONTRACT_DATE_COLS = ("date", "expiry")


def _register(con, name: str, df: pd.DataFrame) -> None:
    con.register(name, df)


def as_dates(df: pd.DataFrame, cols: Iterable[str]) -> pd.DataFrame:
    """DuckDB renders DATE as datetime64; the strategy keys on python dates. Returns a new frame."""
    if df.empty:
        return df
    return df.assign(**{c: pd.to_datetime(df[c]).dt.date for c in cols if c in df.columns})


def load_events(con) -> pd.DataFrame:
    df = con.execute(f"SELECT * FROM {scan_sql(EVENTS)} ORDER BY pre, ticker, E").df()
    return as_dates(df, EVENT_DATE_COLS)


def load_pre_rows(con, events: pd.DataFrame, mcap_lo: float, mcap_hi: float) -> pd.DataFrame:
    """daily_contract rows on `pre` for every event inside the widest market-cap band used."""
    keys = events.loc[events.marketcap.between(mcap_lo, mcap_hi), ["ticker", "pre"]].drop_duplicates()
    _register(con, "ev_keys", keys)
    df = con.execute(f"""
        SELECT c.* FROM {scan_sql(CONTRACTS)} c
        JOIN ev_keys k ON k.ticker = c.underlying_symbol AND k.pre = c.date""").df()
    return as_dates(df, CONTRACT_DATE_COLS)


def load_rows_for_contracts(con, ids: Iterable[str], dates: Iterable[date]) -> pd.DataFrame:
    """daily_contract rows for the given contract ids on the given dates (exit legs, wing history)."""
    ids, dates = sorted(set(ids)), sorted(set(dates))
    if not ids or not dates:
        return pd.DataFrame()
    _register(con, "want_ids", pd.DataFrame({"option_chain_id": ids}))
    _register(con, "want_dates", pd.DataFrame({"date": dates}))
    df = con.execute(f"""
        SELECT c.* FROM {scan_sql(CONTRACTS)} c
        JOIN want_ids i USING (option_chain_id) JOIN want_dates d USING (date)""").df()
    return as_dates(df, CONTRACT_DATE_COLS)


def load_prices(con, tickers: Iterable[str], dates: Iterable[date]) -> dict[tuple[str, date], tuple[float, float]]:
    _register(con, "want_tk", pd.DataFrame({"ticker": sorted(set(tickers))}))
    _register(con, "want_px_dates", pd.DataFrame({"date": sorted(set(dates))}))
    rows = con.execute(f"""
        SELECT p.ticker, p.date, p.open, p.close FROM read_parquet('{PRICES}') p
        JOIN want_tk USING (ticker) JOIN want_px_dates USING (date)""").fetchall()
    return {(t, d): (o, c) for t, d, o, c in rows}


def load_iv30d(con, tickers: Iterable[str], dates: Iterable[date]) -> dict[tuple[str, date], float]:
    _register(con, "want_tk2", pd.DataFrame({"ticker": sorted(set(tickers))}))
    _register(con, "want_iv_dates", pd.DataFrame({"date": sorted(set(dates))}))
    rows = con.execute(f"""
        SELECT s.ticker, s.date, any_value(s.iv30d) FROM read_parquet('{STOCKS}/{SCREENER_GLOB}') s
        JOIN want_tk2 USING (ticker) JOIN want_iv_dates USING (date) GROUP BY 1, 2""").fetchall()
    return {(t, d): v for t, d, v in rows if v is not None}


def load_spread_history(con, events: pd.DataFrame) -> dict[tuple[str, date], float]:
    """Median late_rel_spread over the name's contracts in the 20 sessions before `pre`."""
    keys = events[["ticker", "pre"]].drop_duplicates().copy()
    keys["lo"] = keys.pre.map(lambda d: cal.prev_session(d, MODEL_SPREAD_LOOKBACK))
    _register(con, "spread_keys", keys)
    rows = con.execute(f"""
        SELECT k.ticker, k.pre, median(c.late_rel_spread)
        FROM spread_keys k JOIN {scan_sql(CONTRACTS)} c
          ON c.underlying_symbol = k.ticker AND c.date >= k.lo AND c.date < k.pre
        WHERE c.late_rel_spread IS NOT NULL GROUP BY 1, 2""").fetchall()
    return {(t, d): v for t, d, v in rows}


def history_dates(post_dates: Iterable[date]) -> set[date]:
    """Sessions in [post - MODEL_IV_LOOKBACK, post) for every post date (wing IV lookback)."""
    out: set[date] = set()
    for p in set(post_dates):
        lo = cal.prev_session(p, MODEL_IV_LOOKBACK)
        out.update(cal.trading_days(lo, cal.prev_session(p)))
    return out


def _latest_contract_iv(history: pd.DataFrame) -> dict[str, tuple[date, float]]:
    if history.empty:
        return {}
    h = history.dropna(subset=["iv_vwap"]).sort_values(["option_chain_id", "date"])
    last = h.groupby("option_chain_id").tail(1)
    return {r.option_chain_id: (r.date, float(r.iv_vwap)) for r in last.itertuples(index=False)}


def build_model_inputs(prices: dict, iv30d: dict, spreads: dict, history: pd.DataFrame,
                       spread_key_by_post: dict[tuple[str, date], tuple[str, date]]):
    """Closure for MarkResolver: (contract, date, when) -> ModelInputs or None."""
    last_iv = _latest_contract_iv(history)

    def inputs(contract: M.Contract, d: date, when: str) -> M.ModelInputs | None:
        px = prices.get((contract.underlying, d))
        if px is None:
            return None
        spot = px[0] if when == M.WHEN_EARLY else px[1]
        today = iv30d.get((contract.underlying, d))
        hist = last_iv.get(contract.option_chain_id)
        hist_iv30d = iv30d.get((contract.underlying, hist[0])) if hist and (d - hist[0]).days <= 10 and hist[0] < d else None
        iv = M.model_iv(today, hist[1] if hist_iv30d is not None else None, hist_iv30d)
        spread_key = spread_key_by_post.get((contract.underlying, d), (contract.underlying, d))
        return M.ModelInputs(spot=spot, iv=iv, rel_spread=spreads.get(spread_key))

    return inputs
