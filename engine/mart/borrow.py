"""IBKR stock-loan availability (`usa.txt`) -- free, ~daily-refreshed borrow-fee and share-availability
feed (RESEARCH/47 §2 G9).

**Host correction from the research note.** RESEARCH/47 and `artifacts/edge-gaps/endpoints.md` name
`ftp://ftp3.interactivebrokers.com/usa.txt` with an anonymous login, and record it unreachable (port 21
connection timeout). Re-probed from this environment: `ftp3.interactivebrokers.com:21` still times out
(TCP connect never completes -- `python3 -m ftplib` and `curl` agree), but `ftp2.interactivebrokers.com`
*is* reachable, and the file requires the named login `shortstock` with a **blank** password, not
anonymous. This is not a guess: every open-source parser found by `gh search code` uses this host/login
pair (OpenBB's `stocks/dark_pool_shorts/ibkr_model.py`, `joemccann/radon`'s docs, `guanquann/Stocksera`,
`tangentstorm/gme-data`) -- `ftp2` and `ftp3` are documented as interchangeable mirrors of the same file
in IBKR's own FTP instructions, and only `ftp2` answered from here. Verified live 2026-09-07: connect,
login, `RETR usa.txt` returned 19,950 lines / ~1.8MB, spot-checked against AAPL/MSFT/TSLA/GME.

**File layout** (pipe-delimited, undocumented by IBKR beyond the FTP instructions page, reverse-derived
from the fetched file and cross-checked against the OpenBB/radon parsers above):
```
#BOF|<yyyy.mm.dd>|<hh:mm:ss>
#SYM|CUR|NAME|CON|ISIN|REBATERATE|FEERATE|AVAILABLE|FIGI|
<SYM>|<CUR>|<NAME>|<CONID>|<ISIN>|<REBATERATE>|<FEERATE>|<AVAILABLE>|<FIGI>|
...
#EOF|<row count>
```
`REBATERATE` / `FEERATE` are annualized percentages (`FEERATE` is the borrow cost). `AVAILABLE` is a
bucketed share count and is sometimes a `>` lower bound (e.g. `>10000000`) rather than an exact number --
`parse_available` keeps the bound as a float and flags it with `shares_uncapped`.

Stored daily at `data/mart/borrow/date=<YYYY-MM-DD>/part.parquet`. `refresh(d)` is the only function
that touches the network and raises on failure -- callers (the CLI, `make short-interest`) catch it and
report the blocker rather than fabricating a snapshot. `load_borrow(d)` never touches the network:
fail-soft, `{"available": False, "reason": ...}` when the day has no snapshot.

CLI: `python3 -m engine.mart.borrow --refresh --date 2026-09-07`.
"""
from __future__ import annotations

import argparse
import ftplib
import io
from datetime import date
from typing import Callable

import pandas as pd

from engine.mart import store

TABLE = "borrow"
IBKR_FTP_HOST = "ftp2.interactivebrokers.com"
IBKR_FTP_USER = "shortstock"
IBKR_FTP_PASSWORD = ""
IBKR_FTP_FILE = "usa.txt"
FETCH_TIMEOUT_S = 30

COLUMNS = ["symbol", "currency", "name", "conid", "isin", "rebate_rate", "fee_rate",
           "available_shares", "shares_uncapped", "figi"]


def _empty() -> pd.DataFrame:
    dtypes = {"symbol": object, "currency": object, "name": object, "conid": object, "isin": object,
              "rebate_rate": "float64", "fee_rate": "float64", "available_shares": "float64",
              "shares_uncapped": "bool", "figi": object}
    return pd.DataFrame({c: pd.Series([], dtype=dtypes[c]) for c in COLUMNS})


def fetch_usa_txt(timeout: int = FETCH_TIMEOUT_S) -> str:
    """Network boundary: connect to `ftp2.interactivebrokers.com`, log in as `shortstock` (blank
    password), RETR `usa.txt`. Raises on any transport failure -- no fallback is fabricated here."""
    ftp = ftplib.FTP(timeout=timeout)
    ftp.connect(IBKR_FTP_HOST, 21, timeout=timeout)
    try:
        ftp.login(IBKR_FTP_USER, IBKR_FTP_PASSWORD)
        buf = io.BytesIO()
        ftp.retrbinary(f"RETR {IBKR_FTP_FILE}", buf.write)
        return buf.getvalue().decode("utf-8", errors="replace")
    finally:
        try:
            ftp.quit()
        except Exception:
            ftp.close()


def _to_float(s: str) -> float:
    try:
        return float(s)
    except (TypeError, ValueError):
        return float("nan")


def parse_available(raw: str) -> tuple[float, bool]:
    """`'7600000'` -> `(7600000.0, False)`; `'>10000000'` -> `(10000000.0, True)` -- a floor, not a
    count. Unparseable input -> `(nan, False)`."""
    raw = (raw or "").strip()
    uncapped = raw.startswith(">")
    return _to_float(raw.lstrip(">")), uncapped


def parse_usa_txt(text: str) -> pd.DataFrame:
    """The pipe-delimited `usa.txt` body -> one row per symbol. `#`-prefixed marker lines
    (`#BOF...`, the `#SYM|...` header, `#EOF...`) and short/blank lines are dropped."""
    if not text or not text.strip():
        return _empty()
    rows = []
    for line in text.splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("|")
        if len(parts) < 8:
            continue
        symbol, currency, name, conid, isin, rebate_rate, fee_rate, available = parts[:8]
        figi = parts[8] if len(parts) > 8 else ""
        available_shares, uncapped = parse_available(available)
        rows.append({"symbol": symbol, "currency": currency, "name": name, "conid": conid, "isin": isin,
                     "rebate_rate": _to_float(rebate_rate), "fee_rate": _to_float(fee_rate),
                     "available_shares": available_shares, "shares_uncapped": uncapped, "figi": figi})
    if not rows:
        return _empty()
    out = pd.DataFrame(rows, columns=COLUMNS)
    return out[out["symbol"] != ""].drop_duplicates("symbol").sort_values("symbol").reset_index(drop=True)


def refresh(d: date, fetch_text: Callable[[], str] = fetch_usa_txt) -> pd.DataFrame:
    """Fetch, parse and write-once one day's snapshot. Raises on any failure -- see module docstring."""
    df = parse_usa_txt(fetch_text())
    if not store.has_partition(TABLE, d):
        store.write_partition(df, TABLE, d)
    return df


def load_borrow(d: date) -> dict:
    """Fail-soft, no network: `{"available": True, "reason": None, "data": df}` when `d` has a
    snapshot, else `{"available": False, "reason": ..., "data": <empty frame>}`."""
    if not store.has_partition(TABLE, d):
        return {"available": False, "reason": f"no borrow snapshot for {d.isoformat()}", "data": _empty()}
    return {"available": True, "reason": None, "data": store.read_partition(TABLE, d)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--date", required=True)
    a = ap.parse_args()
    d = date.fromisoformat(a.date)
    if not a.refresh:
        result = load_borrow(d)
        print(f"borrow: available={result['available']} reason={result['reason']} "
              f"rows={len(result['data'])}")
        return 0
    try:
        df = refresh(d)
    except Exception as exc:
        print(f"borrow: refresh failed for {d.isoformat()}: {exc}")
        return 1
    print(f"borrow: {len(df)} symbols -> data/mart/borrow/date={d.isoformat()}/part.parquet")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
