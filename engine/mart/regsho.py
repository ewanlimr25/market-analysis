"""FINRA Reg SHO daily off-exchange short-volume file (RESEARCH/47 §2 G9).

**This is a control variable only, never a signal.** `RESEARCH/30-literature.md` §5: the file counts
the short leg of trades reported to the TRF, the bulk of which is market-maker/wholesaler *facilitation*
of ordinary customer buying (a retail buy internalized by a wholesaler generates a "short sale" print).
It is not short interest and not directional positioning. This loader stores it for liquidity/volume
control use (the same role dark-pool share plays, `RESEARCH/30-literature.md` §5) and logs a coverage
line; nothing here computes a rank, a z-score, or feeds a strategy filter. See G9's kill instruction:
"log-only; no signal use."

Source: `https://cdn.finra.org/equity/regsho/daily/CNMSshvol<YYYYMMDD>.txt`, free, no key, pipe-delimited,
one row per (date, symbol): `Date|Symbol|ShortVolume|ShortExemptVolume|TotalVolume|Market`.

Stored at `data/mart/regsho/date=<YYYY-MM-DD>/part.parquet`. `refresh(d)` is the only function that
touches the network. `load_regsho(d)` never does: fail-soft, `{"available": False, "reason": ...}` when
the day has no snapshot.

CLI: `python3 -m engine.mart.regsho --refresh --date 2026-09-04` (logs row count and short-volume share).
"""
from __future__ import annotations

import argparse
import io
import urllib.request
from datetime import date
from typing import Callable

import pandas as pd

from engine.mart import store

TABLE = "regsho"
REGSHO_URL = "https://cdn.finra.org/equity/regsho/daily/CNMSshvol{d}.txt"
USER_AGENT = {"User-Agent": "Mozilla/5.0 (research; market-analysis engine)"}
FETCH_TIMEOUT_S = 30

COLUMNS = ["date", "symbol", "short_volume", "short_exempt_volume", "total_volume", "market"]


def _empty() -> pd.DataFrame:
    dtypes = {"date": object, "symbol": object, "short_volume": "float64",
              "short_exempt_volume": "float64", "total_volume": "float64", "market": object}
    return pd.DataFrame({c: pd.Series([], dtype=dtypes[c]) for c in COLUMNS})


def fetch_regsho_text(d: date, opener: Callable = urllib.request.urlopen) -> str:
    """Network boundary: one GET for the day's file. Raises on any transport failure."""
    url = REGSHO_URL.format(d=d.strftime("%Y%m%d"))
    req = urllib.request.Request(url, headers=USER_AGENT)
    with opener(req, timeout=FETCH_TIMEOUT_S) as resp:
        return resp.read().decode("utf-8")


def parse_regsho_text(text: str) -> pd.DataFrame:
    """The pipe-delimited `CNMSshvol<date>.txt` body -> normalized columns, one row per symbol."""
    if not text or not text.strip():
        return _empty()
    try:
        raw = pd.read_csv(io.StringIO(text), sep="|")
    except Exception as exc:
        raise ValueError(f"unreadable Reg SHO csv: {exc}") from exc
    expected = {"Date", "Symbol", "ShortVolume", "ShortExemptVolume", "TotalVolume", "Market"}
    missing = expected - set(raw.columns)
    if missing:
        raise ValueError(f"Reg SHO csv missing columns: {sorted(missing)}")
    out = pd.DataFrame({
        "date": pd.to_datetime(raw["Date"], format="%Y%m%d", errors="coerce").dt.date,
        "symbol": raw["Symbol"],
        "short_volume": pd.to_numeric(raw["ShortVolume"], errors="coerce"),
        "short_exempt_volume": pd.to_numeric(raw["ShortExemptVolume"], errors="coerce"),
        "total_volume": pd.to_numeric(raw["TotalVolume"], errors="coerce"),
        "market": raw["Market"],
    })
    out = out.dropna(subset=["date", "symbol"])
    return out.drop_duplicates("symbol").sort_values("symbol").reset_index(drop=True)


def refresh(d: date, fetch_text: Callable[[date], str] = fetch_regsho_text) -> pd.DataFrame:
    """Fetch, parse and write-once one day's snapshot. Raises on failure -- no fallback is
    fabricated; the file is a free daily publication with no history API to fall back to."""
    df = parse_regsho_text(fetch_text(d))
    if not store.has_partition(TABLE, d):
        store.write_partition(df, TABLE, d)
    return df


def load_regsho(d: date) -> dict:
    """Fail-soft, no network: `{"available": True, "reason": None, "data": df}` when `d` has a
    snapshot, else `{"available": False, "reason": ..., "data": <empty frame>}`. Control-variable use
    only -- see module docstring; do not derive a signal from this."""
    if not store.has_partition(TABLE, d):
        return {"available": False, "reason": f"no Reg SHO snapshot for {d.isoformat()}", "data": _empty()}
    return {"available": True, "reason": None, "data": store.read_partition(TABLE, d)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--date", required=True)
    a = ap.parse_args()
    d = date.fromisoformat(a.date)
    if not a.refresh:
        result = load_regsho(d)
        print(f"regsho: available={result['available']} reason={result['reason']} rows={len(result['data'])}")
        return 0
    try:
        df = refresh(d)
    except Exception as exc:
        print(f"regsho: refresh failed for {d.isoformat()}: {exc}")
        return 1
    total_short = df["short_volume"].sum() if not df.empty else 0.0
    total_vol = df["total_volume"].sum() if not df.empty else 0.0
    share = (total_short / total_vol) if total_vol else float("nan")
    print(f"regsho: {len(df)} symbols, short-volume share {share:.4f} (facilitation, control only, "
          "no signal use -- RESEARCH/30 §5)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
