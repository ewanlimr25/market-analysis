"""Daily OHLCV for the watch basket (`DESIGN/110-watch-basket.md` §1, R1 build in §7).

Reuses the G7 earnings-history bars cache (`data/mart/earnings_history/bars/<TICKER>.parquet`,
1,755 names, `engine/mart/earnings_history.py:fetch_bars_cached`) read-only -- this module never
writes there. A ticker missing from that cache is fetched (fail-soft, via `scripts/chart.py`, the
same wrapper G7 uses) and cached under this module's own directory,
`data/mart/watch/bars/<TICKER>.parquet`, so a second call never re-fetches it and the two caches
are never merged into one file.

Every loader in this package fails soft (`DESIGN/110` §1: "a condition whose input is missing is
null, never false"): a fetch failure returns an empty frame, never an exception.
"""
from __future__ import annotations

import os
import sys
from datetime import date

import pandas as pd

from engine import config

EARNINGS_HISTORY_BARS_DIR = os.path.join(config.MART, "earnings_history", "bars")
WATCH_DIR = os.path.join(config.MART, "watch")
WATCH_BARS_DIR = os.path.join(WATCH_DIR, "bars")
YAHOO_RANGE = "10y"
BAR_COLUMNS = ("date", "open", "high", "low", "close", "adj", "volume")


def _empty_bars() -> pd.DataFrame:
    return pd.DataFrame({c: pd.Series([], dtype=("object" if c == "date" else "float64"))
                          for c in BAR_COLUMNS})


def earnings_history_bars_path(ticker: str) -> str:
    return os.path.join(EARNINGS_HISTORY_BARS_DIR, f"{ticker}.parquet")


def watch_bars_path(ticker: str) -> str:
    return os.path.join(WATCH_BARS_DIR, f"{ticker}.parquet")


def _read(path: str) -> pd.DataFrame:
    df = pd.read_parquet(path)
    if df.empty:
        return _empty_bars()
    df = df.assign(date=pd.to_datetime(df["date"]).dt.date).sort_values("date").reset_index(drop=True)
    return df


def _fetch_and_cache(ticker: str, rng: str) -> pd.DataFrame:
    """Network boundary: `scripts/chart.py:bars`, fail-soft (never raises), cached to
    `watch_bars_path`. A genuine failure is NOT cached (retried on the next call); a clean
    zero-row response IS cached (a real "no data" answer, e.g. a dead ticker)."""
    if config.SCRIPTS not in sys.path:
        sys.path.insert(0, config.SCRIPTS)
    try:
        from chart import bars  # noqa: E402 -- scripts/chart.py, network

        rows = bars(ticker, rng)
    except Exception as exc:  # noqa: BLE001 -- one bad ticker must not abort a nightly/panel run
        print(f"[watch.bars] Yahoo fetch failed for {ticker}: {exc}")
        return _empty_bars()
    df = pd.DataFrame(rows) if rows else _empty_bars()
    if not df.empty:
        df = df.assign(date=pd.to_datetime(df["date"]).dt.date).sort_values("date").reset_index(drop=True)
    path = watch_bars_path(ticker)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)
    return df


def load_daily_bars(ticker: str, rng: str = YAHOO_RANGE, force: bool = False) -> pd.DataFrame:
    """Daily OHLCV for `ticker`, oldest first, columns `BAR_COLUMNS`.

    Lookup order: (1) the G7 earnings-history cache, read-only; (2) this module's own cache;
    (3) a fresh fetch, cached here. Never raises -- an unresolvable ticker returns an empty frame
    (`_empty_bars()`), which every condition in `conditions.py` treats as `None`, never `False`.
    """
    if not force and os.path.exists(earnings_history_bars_path(ticker)):
        return _read(earnings_history_bars_path(ticker))
    if not force and os.path.exists(watch_bars_path(ticker)):
        return _read(watch_bars_path(ticker))
    return _fetch_and_cache(ticker, rng)


def bars_as_of(daily: pd.DataFrame, as_of: date) -> pd.DataFrame:
    """`daily` truncated to rows with `date <= as_of` -- the point-in-time slice every indicator
    and condition in this package must use (no lookahead)."""
    if daily.empty:
        return daily
    return daily[daily["date"] <= as_of].reset_index(drop=True)


def weekly_bars(daily: pd.DataFrame) -> pd.DataFrame:
    """Resample daily bars to one row per ISO week (anchored Friday): `open` = the week's first
    session's open, `high`/`low` = the week's extremes, `close` = the week's LAST session's close
    (not necessarily a Friday -- a holiday-shortened week still closes on its last trading day),
    `volume` = the week's summed volume. Weeks with no trading session are dropped."""
    if daily.empty:
        return pd.DataFrame({c: pd.Series([], dtype=("object" if c == "week_end" else "float64"))
                              for c in ("week_end", "open", "high", "low", "close", "volume")})
    d = daily.copy()
    d["date"] = pd.to_datetime(d["date"])
    d = d.set_index("date").sort_index()
    wk = d.resample("W-FRI").agg({"open": "first", "high": "max", "low": "min",
                                   "close": "last", "volume": "sum"})
    wk = wk.dropna(subset=["close"]).reset_index().rename(columns={"date": "week_end"})
    wk["week_end"] = wk["week_end"].dt.date
    return wk
