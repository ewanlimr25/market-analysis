"""CBOE index-vol daily closes for the S-B gate and proxy (DESIGN/80 §1.1, §2, §5.1).

Columns: `date, vix, vix3m, vxn, vix9d`. Stored whole in `data/mart/index_vol/index_vol.parquet`
(a few hundred KB) and refreshed from the CBOE public daily-history CSVs by `refresh`, which is the
only function here that touches the network. `load_index_vol` never does: it reads the mart file,
else the artifact frozen in the findings repo on 2026-09-05, else returns an empty frame.

CLI: `python3 -m engine.mart.index_vol --refresh`.
"""
from __future__ import annotations

import argparse
import io
import os
import urllib.request
from datetime import date
from typing import Callable, Iterable

import numpy as np
import pandas as pd

from engine import config

COLUMNS = ["date", "vix", "vix3m", "vxn", "vix9d"]
INDEX_COLUMN = {"VIX": "vix", "VIX3M": "vix3m", "VXN": "vxn", "VIX9D": "vix9d"}
USER_AGENT = {"User-Agent": "Mozilla/5.0"}
FETCH_TIMEOUT_S = 30


def _empty() -> pd.DataFrame:
    return pd.DataFrame({c: pd.Series([], dtype=(object if c == "date" else "float64")) for c in COLUMNS})


def normalize(df: pd.DataFrame | None) -> pd.DataFrame:
    """`date` as python dates, every index column float (NaN when absent), sorted, one row per date."""
    if df is None or df.empty:
        return _empty()
    out = pd.DataFrame({"date": pd.to_datetime(df["date"]).dt.date})
    for col in COLUMNS[1:]:
        out[col] = pd.to_numeric(df[col], errors="coerce").astype("float64") if col in df.columns else np.nan
    return out.drop_duplicates("date").sort_values("date").reset_index(drop=True)


def parse_cboe_csv(text: str, index: str) -> pd.DataFrame:
    """A CBOE `<INDEX>_History.csv` (DATE, OPEN, HIGH, LOW, CLOSE) -> DataFrame(date, <index>)."""
    if index not in INDEX_COLUMN:
        raise ValueError(f"unknown CBOE index {index!r}; expected one of {tuple(INDEX_COLUMN)}")
    try:
        raw = pd.read_csv(io.StringIO(text))
    except Exception as exc:  # pandas raises several parser types
        raise ValueError(f"unreadable CBOE csv for {index}: {exc}") from exc
    if "DATE" not in raw.columns or "CLOSE" not in raw.columns:
        raise ValueError(f"CBOE csv for {index} lacks DATE/CLOSE columns: {list(raw.columns)}")
    out = pd.DataFrame({"date": pd.to_datetime(raw["DATE"], errors="coerce").dt.date,
                        INDEX_COLUMN[index]: pd.to_numeric(raw["CLOSE"], errors="coerce")})
    out = out.dropna(subset=["date"])
    if out.empty:
        raise ValueError(f"CBOE csv for {index} has no dated rows")
    return out.drop_duplicates("date").sort_values("date").reset_index(drop=True)


def merge_indices(frames: Iterable[pd.DataFrame]) -> pd.DataFrame:
    merged = None
    for frame in frames:
        merged = frame if merged is None else merged.merge(frame, on="date", how="outer")
    return normalize(merged)


def fetch_cboe_text(index: str, opener: Callable = urllib.request.urlopen) -> str:
    url = config.CBOE_HISTORY_URL.format(index=index)
    req = urllib.request.Request(url, headers=USER_AGENT)
    with opener(req, timeout=FETCH_TIMEOUT_S) as resp:
        return resp.read().decode("utf-8")


def write_index_vol(df: pd.DataFrame, path: str = config.INDEX_VOL_FILE) -> str:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp = path + ".tmp"
    normalize(df).to_parquet(tmp, index=False)
    os.replace(tmp, path)
    return path


def refresh(path: str = config.INDEX_VOL_FILE, fetch_text: Callable[[str], str] = fetch_cboe_text,
            indices: Iterable[str] = config.CBOE_INDICES) -> pd.DataFrame:
    """Fetch every index, merge, write atomically and return the frame. Raises on any failure."""
    frames = [parse_cboe_csv(fetch_text(index), index) for index in indices]
    merged = merge_indices(frames)
    write_index_vol(merged, path)
    return merged


def _read(path: str) -> pd.DataFrame:
    return normalize(pd.read_parquet(path))


def load_index_vol(path: str = config.INDEX_VOL_FILE, fallback: str = config.INDEX_VOL_FALLBACK) -> pd.DataFrame:
    """No network: the mart file, else the frozen artifact, else empty."""
    if os.path.exists(path):
        return _read(path)
    if fallback and os.path.exists(fallback):
        return _read(fallback)
    return _empty()


def on_sessions(df: pd.DataFrame, is_session: Callable[[date], bool]) -> pd.DataFrame:
    """Rows on exchange sessions only. CBOE publishes a VIX close on some NYSE holidays (Labor
    Day, Thanksgiving, ...) with no VIX3M/VXN; those rows are not sessions and would otherwise
    void the gate's 20-session window (DESIGN/80 §2; DECISIONS D16)."""
    if df is None or df.empty:
        return _empty()
    keep = df["date"].map(is_session)
    return df[keep.astype(bool)].reset_index(drop=True)


def latest_date(df: pd.DataFrame) -> date | None:
    return None if df is None or df.empty else df["date"].iloc[-1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--path", default=config.INDEX_VOL_FILE)
    a = ap.parse_args()
    if a.refresh:
        df = refresh(a.path)
        print(f"index_vol: {len(df)} rows through {latest_date(df)} -> {a.path}")
        return 0
    df = load_index_vol(a.path)
    print(f"index_vol: {len(df)} rows through {latest_date(df)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
