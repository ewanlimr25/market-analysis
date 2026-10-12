"""VIX close series for `earnings_events.vix_pre` (DESIGN/70 §1.2).

Stored as a plain file, `data/mart/vix/vix.parquet` (columns `date`, `vix`), not as a date
partition: the series is tiny and is refreshed from Yahoo via `scripts/chart.py`.

`load_vix` never raises on a missing file or a network failure: it returns whatever source is
available, in this order, and prints a one-line warning when it has to fall back:
  1. the mart file, if present -- refreshed first (`fetch_vix`) when the caller names an `as_of`
     session the file does not reach; a failed refresh keeps the file as it was;
  2. a fresh Yahoo fetch (`fetch_vix`), which also writes the mart file;
  3. the recorded E4 artifact (`e4_index_vrp.parquet`, ends 2026-08-06);
  4. an empty frame.

**A cache is only as good as its tail.** Until 2026-10-12 nothing refreshed the file once it existed:
it was written on 2026-09-05, so every event after 2026-09-04 was built with `vix_pre` null (findings
market-analysis D36). `fetch_vix` merges into the file (a re-fetched session wins; sessions the range
no longer returns are kept) and never files today from Yahoo's multi-day array, which serves the live
value while the session trades and a null close for hours after it (`chart.session_bar`); today's close
comes from the single-day endpoint, once Yahoo itself reports the session closed and the New York clock
agrees (`cboe_chain.session_closed`: from 16:15, VIX's own close).
"""
from __future__ import annotations

import os
import sys
from datetime import date, datetime
from zoneinfo import ZoneInfo

import duckdb
import pandas as pd

from engine import config
from engine.mart.cboe_chain import session_closed

VIX_TICKER = "^VIX"
DEFAULT_RANGE = "1y"
E4_VRP_FALLBACK = os.path.expanduser(
    "~/Development/findings/market-analysis/artifacts/vol/out/e4_index_vrp.parquet")
COLUMNS = ["date", "vix"]
NEW_YORK = ZoneInfo("America/New_York")


def vix_path() -> str:
    return os.path.join(config.MART, "vix", "vix.parquet")


def _empty() -> pd.DataFrame:
    return pd.DataFrame({"date": pd.Series([], dtype=object), "vix": pd.Series([], dtype="float64")})


def _normalize(df: pd.DataFrame) -> pd.DataFrame:
    """`date` as python dates, `vix` as float, sorted, one row per date (the first one given)."""
    if df.empty:
        return _empty()
    out = pd.DataFrame({"date": pd.to_datetime(df["date"]).dt.date,
                        "vix": pd.to_numeric(df["vix"], errors="coerce").astype("float64")})
    return out.dropna(subset=["vix"]).drop_duplicates("date").sort_values("date").reset_index(drop=True)


def _read(con: duckdb.DuckDBPyConnection, path: str) -> pd.DataFrame:
    return _normalize(con.execute(f"SELECT date, vix FROM read_parquet('{path}')").df())


def _stored(con: duckdb.DuckDBPyConnection, path: str) -> pd.DataFrame | None:
    """The mart file, or None when it is missing or cannot be read (then it is fetched anew)."""
    if not os.path.exists(path):
        return None
    try:
        return _read(con, path)
    except Exception as exc:  # noqa: BLE001 -- a broken cache is refetched, never raised
        print(f"[vix] unreadable {path} ({exc}); fetching it anew")
        return None


def _frame(bars: list[dict]) -> pd.DataFrame:
    """Bar dicts from `scripts/chart.py` -> (date, vix)."""
    if not bars:
        return _empty()
    return _normalize(pd.DataFrame({"date": [b["date"] for b in bars], "vix": [b["close"] for b in bars]}))


def _merge(base: pd.DataFrame, add: pd.DataFrame) -> pd.DataFrame:
    """`base` extended by `add`; on a date both carry, `add` (the newer read) wins."""
    frames = [f for f in (add, base) if not f.empty]
    return _normalize(pd.concat(frames, ignore_index=True)) if frames else _empty()


def _covers(series: pd.DataFrame, as_of: date) -> bool:
    return not series.empty and series.date.iloc[-1] >= as_of


def _chart():
    """`scripts/chart.py`, the repo's single Yahoo boundary (network)."""
    if config.SCRIPTS not in sys.path:
        sys.path.insert(0, config.SCRIPTS)
    import chart  # noqa: E402

    return chart


def _now() -> datetime:
    """Now in New York; indirected so a test can pin it."""
    return datetime.now(NEW_YORK)


def _session_bars(chart, now: datetime) -> list[dict]:
    """Today's completed bar from the single-day endpoint, or nothing: still trading, not published,
    dated past what the clock can vouch for, or the request failed (the multi-day refresh still lands;
    today waits for the next one)."""
    try:
        bar = chart.session_bar(VIX_TICKER)
    except Exception as exc:  # noqa: BLE001 -- fail soft, like every reader of this file
        print(f"[vix] session fetch failed ({exc}); today's close waits for the next refresh")
        return []
    return [bar] if bar and session_closed(date.fromisoformat(bar["date"]), now) else []


def fetch_vix(rng: str = DEFAULT_RANGE) -> pd.DataFrame:
    """Fetch VIX daily closes from Yahoo through `scripts/chart.py`, merge them into the mart file and
    write it; today's close only from the single-day endpoint (module doc).

    Raises on network failure; `load_vix` is the caller that swallows that.
    """
    chart, now = _chart(), _now()
    closed = [b for b in chart.bars(VIX_TICKER, rng) if date.fromisoformat(b["date"]) < now.date()]
    if not closed:
        raise ValueError(f"chart.bars({VIX_TICKER!r}, {rng!r}) returned no closed session")
    fresh = _merge(_frame(_session_bars(chart, now)), _frame(closed))  # an official bar beats a recovered one
    path = vix_path()
    stored = _stored(duckdb.connect(), path)
    df = _merge(stored, fresh) if stored is not None else fresh
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = f"{path}.{os.getpid()}.tmp"           # the nightly and a hand-run refresh may write at once
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)
    return df


def load_vix(con: duckdb.DuckDBPyConnection | None = None, as_of: date | None = None) -> pd.DataFrame:
    """VIX closes as DataFrame(date, vix); see the module docstring for the source order. With `as_of`,
    a stored series that ends before it is refreshed first (Yahoo may not have `as_of` yet)."""
    con = con or duckdb.connect()
    path = vix_path()
    stored = _stored(con, path)
    if stored is not None:
        if as_of is None or _covers(stored, as_of):
            return stored
        try:
            return fetch_vix()
        except Exception as exc:  # network / parse failure: keep the stored series, never raise
            last = stored.date.iloc[-1] if len(stored) else "nothing"
            print(f"[vix] refresh failed ({exc}); using the stored series, which ends {last}")
            return stored
    try:
        return fetch_vix()
    except Exception as exc:  # network / parse failure: fall through, never raise
        print(f"[vix] fetch failed ({exc}); falling back to {E4_VRP_FALLBACK}")
    if os.path.exists(E4_VRP_FALLBACK):
        return _read(con, E4_VRP_FALLBACK)
    print("[vix] no VIX source available; vix_pre will be null")
    return _empty()
