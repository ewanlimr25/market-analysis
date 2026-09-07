"""FINRA consolidated short interest (RESEARCH/47 §2 G9; verified `artifacts/edge-gaps/endpoints.md`).

Source: FINRA's Query API, `POST https://api.finra.org/data/group/otcMarket/name/consolidatedShortInterest`
with a `compareFilters` body. An `EQUAL` filter on `symbolCode` (no `settlementDate` filter) returns that
one symbol's *entire* settlement history in a single call -- verified against AAPL (208 rows, 2017-12-29
through the latest settlement) and MSFT. `limit`/`offset` page a single-date pull (`record-total` /
`record-limit` / `record-offset` response headers); an `IN` filter on `symbolCode` was tried and rejected
("Unable to parse request body") -- the API takes one `EQUAL` value per filter, not a list, so one call
per ticker is the verified shape. The endpoint returns CSV-ish `text/plain`, not `text/csv` (an explicit
`Accept: text/csv` is rejected with a 400); the default `Accept` gets you the CSV body regardless.

Settlement is twice monthly (mid-month and month-end, sometimes shifted for a holiday). FINRA's own
short-interest dissemination schedule documents publication at roughly 9 business days after settlement,
so a row is not knowable to a point-in-time reader on `settlement_date` itself -- see `publication_date`.

Columns kept: `symbol, settlement_date, current_short_position, previous_short_position,
avg_daily_volume, days_to_cover, change_percent`. Stored write-once at
`data/mart/short_interest/settlement=<YYYY-MM-DD>/part.parquet`, one row per (symbol, settlement_date).
"Write-once" here means: run `refresh` with the full universe you want covered, in one pass -- a second
`refresh` call never rewrites a settlement date that already has a partition, so partial universes do not
merge across calls (RESEARCH/47 G9's brief; matches `mart/store.py`'s partition contract).

CLI: `python3 -m engine.mart.short_interest --refresh --universe data/universe.json [--workers 8]`.
"""
from __future__ import annotations

import argparse
import io
import json
import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from typing import Callable, Iterable

import pandas as pd

from engine import calendar as cal
from engine import config
from engine.mart import store

TABLE = "short_interest"
FINRA_SI_URL = "https://api.finra.org/data/group/otcMarket/name/consolidatedShortInterest"
USER_AGENT = {"User-Agent": "Mozilla/5.0 (research; market-analysis engine)"}
FETCH_TIMEOUT_S = 30
PAGE_LIMIT = 5000                # a single symbol's full history has always been well under this

# FINRA's short-interest dissemination calendar documents publication at about 9 business days after
# settlement. Encoded as a floor in *trading* days (not calendar days), which is the conservative
# direction: a shorter real lag only means the row is available sooner than this loader admits it,
# never the reverse, so `load_short_interest(as_of=...)` cannot look ahead.
PUBLICATION_LAG_BUSINESS_DAYS = 9

COLUMNS = ["symbol", "settlement_date", "current_short_position", "previous_short_position",
           "avg_daily_volume", "days_to_cover", "change_percent"]

_RAW_COLUMN_MAP = {
    "symbolCode": "symbol",
    "settlementDate": "settlement_date",
    "currentShortPositionQuantity": "current_short_position",
    "previousShortPositionQuantity": "previous_short_position",
    "averageDailyVolumeQuantity": "avg_daily_volume",
    "daysToCoverQuantity": "days_to_cover",
    "changePercent": "change_percent",
}


def _empty() -> pd.DataFrame:
    dtypes = {"symbol": object, "settlement_date": object, "current_short_position": "float64",
              "previous_short_position": "float64", "avg_daily_volume": "float64",
              "days_to_cover": "float64", "change_percent": "float64"}
    return pd.DataFrame({c: pd.Series([], dtype=dtypes[c]) for c in COLUMNS})


def parse_finra_csv(text: str) -> pd.DataFrame:
    """FINRA's `consolidatedShortInterest` text body -> normalized columns, one row per
    (symbol, settlement_date), deduplicated and sorted. Empty input -> empty frame (not an error);
    a body that parses but lacks the expected columns raises, since that means the API shape changed."""
    if not text or not text.strip():
        return _empty()
    try:
        raw = pd.read_csv(io.StringIO(text))
    except Exception as exc:  # pandas raises several parser types
        raise ValueError(f"unreadable FINRA short-interest csv: {exc}") from exc
    missing = [c for c in _RAW_COLUMN_MAP if c not in raw.columns]
    if missing:
        raise ValueError(f"FINRA short-interest csv missing columns: {missing}")
    out = raw.rename(columns=_RAW_COLUMN_MAP)[COLUMNS].copy()
    out["settlement_date"] = pd.to_datetime(out["settlement_date"], errors="coerce").dt.date
    for c in COLUMNS[2:]:
        out[c] = pd.to_numeric(out[c], errors="coerce")
    out = out.dropna(subset=["symbol", "settlement_date"])
    return (out.drop_duplicates(["symbol", "settlement_date"])
               .sort_values(["symbol", "settlement_date"]).reset_index(drop=True))


def fetch_symbol_text(symbol: str, opener: Callable = urllib.request.urlopen) -> str:
    """Network boundary: one POST, one symbol, its full settlement history. Raises on any transport
    failure; callers (`refresh`) decide fail-soft handling per symbol."""
    body = json.dumps({
        "limit": PAGE_LIMIT,
        "compareFilters": [{"compareType": "EQUAL", "fieldName": "symbolCode", "fieldValue": symbol}],
    }).encode("utf-8")
    req = urllib.request.Request(FINRA_SI_URL, data=body,
                                  headers={**USER_AGENT, "Content-Type": "application/json"}, method="POST")
    with opener(req, timeout=FETCH_TIMEOUT_S) as resp:
        return resp.read().decode("utf-8")


def publication_date(settlement_date: date) -> date:
    """The first `as_of` date on which a row settled on `settlement_date` may be used
    (RESEARCH/47 §2 G9: ~9 business days after settlement, encoded conservatively)."""
    return cal.next_session(settlement_date, PUBLICATION_LAG_BUSINESS_DAYS)


def write_settlement_partitions(df: pd.DataFrame) -> list[str]:
    """Write-once: one partition per settlement date; a date that already has a partition is left
    untouched (RESEARCH/47 G9's write-once brief)."""
    paths = []
    if df is None or df.empty:
        return paths
    for settlement_date, rows in df.groupby("settlement_date"):
        if store.has_partition(TABLE, settlement_date):
            continue
        paths.append(store.write_partition(rows.reset_index(drop=True), TABLE, settlement_date))
    return paths


def _fetch_all(universe: list[str], fetch_text: Callable[[str], str], max_workers: int,
               on_error: Callable[[str, Exception], None] | None) -> list[pd.DataFrame]:
    frames: list[pd.DataFrame] = []

    def one(symbol: str) -> pd.DataFrame | None:
        try:
            return parse_finra_csv(fetch_text(symbol))
        except Exception as exc:  # network / parse: fail-soft per symbol, not per refresh
            if on_error:
                on_error(symbol, exc)
            return None

    if max_workers <= 1:
        for symbol in universe:
            got = one(symbol)
            if got is not None:
                frames.append(got)
        return frames
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        for got in pool.map(one, universe):
            if got is not None:
                frames.append(got)
    return frames


def refresh(universe: Iterable[str], fetch_text: Callable[[str], str] = fetch_symbol_text,
            on_error: Callable[[str, Exception], None] | None = None,
            max_workers: int = 1) -> pd.DataFrame:
    """Fetch each symbol's full history, parse, combine and write new settlement partitions. A
    per-symbol failure is caught and reported to `on_error` (or silently dropped) rather than aborting
    the whole refresh. Returns the combined frame actually fetched this call (not the full mart)."""
    frames = _fetch_all(list(universe), fetch_text, max_workers, on_error)
    combined = pd.concat(frames, ignore_index=True) if frames else _empty()
    combined = (combined.drop_duplicates(["symbol", "settlement_date"])
                        .sort_values(["symbol", "settlement_date"]).reset_index(drop=True))
    write_settlement_partitions(combined)
    return combined


def load_short_interest(as_of: date) -> pd.DataFrame:
    """Per ticker, the latest settlement row whose `publication_date` is on or before `as_of`.
    Point-in-time safe by construction: a row settled 2026-08-14 (publication_date ~2026-08-27) is
    invisible to any `as_of` before that. No network; reads only partitions `refresh` already wrote.
    Empty frame (not an error) when the table does not exist yet, or nothing is visible by `as_of`."""
    if not os.path.isdir(store.table_dir(TABLE)):
        return _empty()
    df = store.read_table(None, TABLE)
    if df.empty:
        return _empty()
    df = df.copy()
    df["settlement_date"] = pd.to_datetime(df["settlement_date"]).dt.date
    df["publication_date"] = df["settlement_date"].map(publication_date)
    visible = df[df["publication_date"] <= as_of]
    if visible.empty:
        return _empty()
    latest_idx = visible.groupby("symbol")["settlement_date"].idxmax()
    out = visible.loc[latest_idx, COLUMNS].sort_values("symbol").reset_index(drop=True)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--universe", default=os.path.join(config.DATA, "universe.json"))
    ap.add_argument("--workers", type=int, default=8)
    a = ap.parse_args()
    if not a.refresh:
        print("short_interest: nothing to do without --refresh")
        return 0
    with open(a.universe) as f:
        universe = json.load(f)
    errors: list[tuple[str, str]] = []
    df = refresh(universe, on_error=lambda s, e: errors.append((s, str(e))), max_workers=a.workers)
    n_symbols = df.symbol.nunique() if not df.empty else 0
    print(f"short_interest: {len(df)} rows, {n_symbols}/{len(universe)} symbols, {len(errors)} errors")
    for symbol, err in errors[:20]:
        print(f"  {symbol}: {err}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
