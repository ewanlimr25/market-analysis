"""VIX close series for `earnings_events.vix_pre` (DESIGN/70 §1.2).

Stored as a plain file, `data/mart/vix/vix.parquet` (columns `date`, `vix`), not as a date
partition: the series is tiny and is refreshed whole from Yahoo via `scripts/chart.py`.

`load_vix` never raises on a missing file or a network failure: it returns whatever source is
available, in this order, and prints a one-line warning when it has to fall back:
  1. the mart file, if present;
  2. a fresh Yahoo fetch (`fetch_vix`), which also writes the mart file;
  3. the recorded E4 artifact (`e4_index_vrp.parquet`, ends 2026-08-06);
  4. an empty frame.
"""
from __future__ import annotations

import os
import sys
from datetime import date

import duckdb
import pandas as pd

from engine import config

VIX_TICKER = "^VIX"
DEFAULT_RANGE = "1y"
E4_VRP_FALLBACK = os.path.expanduser(
    "~/Development/findings/market-analysis/artifacts/vol/out/e4_index_vrp.parquet")
COLUMNS = ["date", "vix"]


def vix_path() -> str:
    return os.path.join(config.MART, "vix", "vix.parquet")


def _empty() -> pd.DataFrame:
    return pd.DataFrame({"date": pd.Series([], dtype=object), "vix": pd.Series([], dtype="float64")})


def _normalize(df: pd.DataFrame) -> pd.DataFrame:
    """`date` as python dates, `vix` as float, sorted, one row per date."""
    if df.empty:
        return _empty()
    out = pd.DataFrame({"date": pd.to_datetime(df["date"]).dt.date,
                        "vix": pd.to_numeric(df["vix"], errors="coerce").astype("float64")})
    return out.dropna(subset=["vix"]).drop_duplicates("date").sort_values("date").reset_index(drop=True)


def _read(con: duckdb.DuckDBPyConnection, path: str) -> pd.DataFrame:
    return _normalize(con.execute(f"SELECT date, vix FROM read_parquet('{path}')").df())


def fetch_vix(rng: str = DEFAULT_RANGE) -> pd.DataFrame:
    """Fetch VIX daily closes from Yahoo through `scripts/chart.py` and write the mart file.

    Raises on network failure; `load_vix` is the caller that swallows that.
    """
    if config.SCRIPTS not in sys.path:
        sys.path.insert(0, config.SCRIPTS)
    from chart import bars  # noqa: E402  (scripts/chart.py, network)

    rows = bars(VIX_TICKER, rng)
    if not rows:
        raise ValueError(f"chart.bars({VIX_TICKER!r}, {rng!r}) returned no bars")
    df = _normalize(pd.DataFrame({"date": [date.fromisoformat(b["date"]) for b in rows],
                                  "vix": [b["close"] for b in rows]}))
    path = vix_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)
    return df


def load_vix(con: duckdb.DuckDBPyConnection | None = None) -> pd.DataFrame:
    """VIX closes as DataFrame(date, vix); see the module docstring for the source order."""
    con = con or duckdb.connect()
    path = vix_path()
    if os.path.exists(path):
        return _read(con, path)
    try:
        return fetch_vix()
    except Exception as exc:  # network / parse failure: fall through, never raise
        print(f"[vix] fetch failed ({exc}); falling back to {E4_VRP_FALLBACK}")
    if os.path.exists(E4_VRP_FALLBACK):
        return _read(con, E4_VRP_FALLBACK)
    print("[vix] no VIX source available; vix_pre will be null")
    return _empty()
