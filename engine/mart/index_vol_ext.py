"""CBOE VVIX and SKEW daily closes, plus two vol-index ratios read from the existing (untouched)
`data/mart/index_vol/` table (G10, findings/market-analysis RESEARCH/47-edge-gaps.md §2).

The VVIX and SKEW CSVs are *not* the same shape as `index_vol.py`'s VIX/VIX3M/VXN/VIX9D histories:
those are `DATE,OPEN,HIGH,LOW,CLOSE`; VVIX and SKEW are single-value `DATE,VVIX` / `DATE,SKEW`
(verified 2026-09-07 against `endpoints.md`, which called them "same format" meaning same host and
reachability, not the same columns). `parse_cboe_value_csv` below reads the value column named
after the index rather than `CLOSE`.

This module never writes to `data/mart/index_vol/`: it reads that table (via
`engine.mart.index_vol.load_index_vol`, no network) only to compute `vix9d_vix_ratio` and
`vix_vix3m_ratio`, and writes its own table at `data/mart/index_vol_ext/index_vol_ext.parquet`.
Columns: `date, vvix, skew, vix9d_vix_ratio, vix_vix3m_ratio`. `refresh` is the only function that
touches the network; `load_index_vol_ext` reads the mart file, else the frozen artifact, else empty
(the same fail-soft / cached / artifact-fallback convention as `index_vol.py`).

CLI: `python3 -m engine.mart.index_vol_ext --refresh`.
"""
from __future__ import annotations

import argparse
import io
import os
import urllib.request
from datetime import date
from typing import Callable

import numpy as np
import pandas as pd

from engine import config
from engine.mart import index_vol as IV

COLUMNS = ["date", "vvix", "skew", "vix9d_vix_ratio", "vix_vix3m_ratio"]
RATIO_COLUMNS = ["vix9d_vix_ratio", "vix_vix3m_ratio"]
USER_AGENT = IV.USER_AGENT
FETCH_TIMEOUT_S = IV.FETCH_TIMEOUT_S


def _empty() -> pd.DataFrame:
    return pd.DataFrame({c: pd.Series([], dtype=(object if c == "date" else "float64")) for c in COLUMNS})


def normalize(df: pd.DataFrame | None) -> pd.DataFrame:
    """`date` as python dates, every value column float (NaN when absent), sorted, one row per date."""
    if df is None or df.empty:
        return _empty()
    out = pd.DataFrame({"date": pd.to_datetime(df["date"]).dt.date})
    for col in COLUMNS[1:]:
        out[col] = pd.to_numeric(df[col], errors="coerce").astype("float64") if col in df.columns else np.nan
    return out.drop_duplicates("date").sort_values("date").reset_index(drop=True)


def parse_cboe_value_csv(text: str, index: str) -> pd.DataFrame:
    """A CBOE `<INDEX>_History.csv` shaped `DATE,<INDEX>` -> DataFrame(date, <lower(index)>)."""
    if index not in config.CBOE_EXT_INDICES:
        raise ValueError(f"unknown CBOE ext index {index!r}; expected one of {config.CBOE_EXT_INDICES}")
    try:
        raw = pd.read_csv(io.StringIO(text))
    except Exception as exc:  # pandas raises several parser types
        raise ValueError(f"unreadable CBOE csv for {index}: {exc}") from exc
    value_col = config.CBOE_EXT_VALUE_COLUMN[index]
    out_col = config.CBOE_EXT_INDEX_COLUMN[index]
    if "DATE" not in raw.columns or value_col not in raw.columns:
        raise ValueError(f"CBOE csv for {index} lacks DATE/{value_col} columns: {list(raw.columns)}")
    out = pd.DataFrame({"date": pd.to_datetime(raw["DATE"], errors="coerce").dt.date,
                        out_col: pd.to_numeric(raw[value_col], errors="coerce")})
    out = out.dropna(subset=["date"])
    if out.empty:
        raise ValueError(f"CBOE csv for {index} has no dated rows")
    return out.drop_duplicates("date").sort_values("date").reset_index(drop=True)


def fetch_cboe_ext_text(index: str, opener: Callable = urllib.request.urlopen) -> str:
    url = config.CBOE_HISTORY_URL.format(index=index)
    req = urllib.request.Request(url, headers=USER_AGENT)
    with opener(req, timeout=FETCH_TIMEOUT_S) as resp:
        return resp.read().decode("utf-8")


def add_ratios(base: pd.DataFrame) -> pd.DataFrame:
    """`vix9d_vix_ratio = vix9d / vix`, `vix_vix3m_ratio = vix / vix3m`, from the base index_vol
    table (`engine.mart.index_vol`), NaN where any input is missing or zero."""
    if base is None or base.empty:
        return pd.DataFrame({"date": pd.Series([], dtype=object), "vix9d_vix_ratio": pd.Series([], dtype="float64"),
                             "vix_vix3m_ratio": pd.Series([], dtype="float64")})
    vix = pd.to_numeric(base["vix"], errors="coerce")
    vix3m = pd.to_numeric(base["vix3m"], errors="coerce")
    vix9d = pd.to_numeric(base["vix9d"], errors="coerce")
    return pd.DataFrame({"date": base["date"],
                         "vix9d_vix_ratio": np.where(vix > 0, vix9d / vix, np.nan),
                         "vix_vix3m_ratio": np.where(vix3m > 0, vix / vix3m, np.nan)})


def merge_ext(vvix: pd.DataFrame, skew: pd.DataFrame, ratios: pd.DataFrame) -> pd.DataFrame:
    merged = vvix.merge(skew, on="date", how="outer").merge(ratios, on="date", how="outer")
    return normalize(merged)


def write_index_vol_ext(df: pd.DataFrame, path: str = config.INDEX_VOL_EXT_FILE) -> str:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp = path + ".tmp"
    normalize(df).to_parquet(tmp, index=False)
    os.replace(tmp, path)
    return path


def refresh(path: str = config.INDEX_VOL_EXT_FILE, fetch_text: Callable[[str], str] = fetch_cboe_ext_text,
            base_index_vol: pd.DataFrame | None = None) -> pd.DataFrame:
    """Fetch VVIX and SKEW, merge with ratios read from the base index_vol table (no network for
    that read), write atomically and return the frame. Raises on any failure (fail-soft is the
    caller's job, matching `index_vol.refresh`)."""
    vvix = parse_cboe_value_csv(fetch_text("VVIX"), "VVIX")
    skew = parse_cboe_value_csv(fetch_text("SKEW"), "SKEW")
    base = base_index_vol if base_index_vol is not None else IV.load_index_vol()
    merged = merge_ext(vvix, skew, add_ratios(base))
    write_index_vol_ext(merged, path)
    return merged


def _read(path: str) -> pd.DataFrame:
    return normalize(pd.read_parquet(path))


def load_index_vol_ext(path: str = config.INDEX_VOL_EXT_FILE,
                       fallback: str = config.INDEX_VOL_EXT_FALLBACK) -> pd.DataFrame:
    """No network: the mart file, else the frozen artifact, else empty."""
    if os.path.exists(path):
        return _read(path)
    if fallback and os.path.exists(fallback):
        return _read(fallback)
    return _empty()


def latest_date(df: pd.DataFrame) -> date | None:
    return None if df is None or df.empty else df["date"].iloc[-1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--path", default=config.INDEX_VOL_EXT_FILE)
    a = ap.parse_args()
    if a.refresh:
        try:
            df = refresh(a.path)
        except Exception as exc:  # fail-soft at the CLI: report and keep the file on disk
            print(f"index_vol_ext: refresh failed ({exc}); mart file on disk is unchanged")
            return 1
        print(f"index_vol_ext: {len(df)} rows through {latest_date(df)} -> {a.path}")
        return 0
    df = load_index_vol_ext(a.path)
    print(f"index_vol_ext: {len(df)} rows through {latest_date(df)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
