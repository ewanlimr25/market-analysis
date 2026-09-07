"""The full option chain, nightly, from CBOE's free delayed-quotes API (RESEARCH/47 G8).

`fetch_chain(symbol)` does one HTTP GET of
`https://cdn.cboe.com/api/global/delayed_quotes/options/<SYMBOL>.json` (no key, 15-minute delayed)
and returns the raw JSON payload. For an equity or ETF, `symbol` is the ticker as-is (`SPY`,
`QQQ`, a single name). For a CBOE index product the API needs a leading underscore on the request
(`_SPX`, `_VIX`, `_NDX`, ...); the payload's `data.symbol` then comes back as `^SPX` / `^VIX` and
the contract codes use the bare root (`SPX260918C00200000`). Verified 2026-09-07 by fetching
`_SPX.json` and `_VIX.json` directly; this module does not special-case index symbols beyond that
documentation — pass the prefixed string in.

`parse_chain(payload, fetched_at)` turns the payload into one row per contract: strike, expiry and
right come from the OCC option code (`<ROOT><YYMMDD><C|P><STRIKE*1000, 8 digits>`); a code that does
not match is a malformed row, dropped and counted, never silent (a `logging.warning` line reports
`n_rejected / n_total`).

`store_chain` / `load_chain` follow the mart write-once convention (`engine/mart/store.py`), with a
two-level partition (`symbol=<SYM>/date=<YYYY-MM-DD>`) because a chain is looked up by (symbol, date).

`refresh_chains(symbols, d)` is the fail-soft nightly hook: fetch, parse, store one symbol at a
time, catching every exception so one bad symbol never stops the rest (`engine/mart/index_vol.py`'s
`refresh_index_vol` fail-soft pattern). It is wired to `make cboe-chain DATE=...`, not into
`make daily` — see the module docstring note in `engine/README.md` and
`findings/market-analysis/artifacts/edge-gaps/g8/results.md` for why.
"""
from __future__ import annotations

import argparse
import logging
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from typing import Callable, Iterable

import pandas as pd

from engine import config

log = logging.getLogger(__name__)

CBOE_CHAIN_URL = "https://cdn.cboe.com/api/global/delayed_quotes/options/{symbol}.json"
USER_AGENT = {"User-Agent": "market-analysis-research/1.0 (+edge-gaps G8; contact via repo)"}
FETCH_TIMEOUT_S = 20

CBOE_CHAIN_DIR = os.path.join(config.MART, "cboe_chain")
SOURCE = "cboe_delayed"

# OCC option code: root (1-6 letters), YYMMDD, C or P, strike * 1000 (8 digits, no decimal point).
OCC_RE = re.compile(r"^(?P<root>[A-Z]{1,6})(?P<yy>\d{2})(?P<mm>\d{2})(?P<dd>\d{2})(?P<right>[CP])(?P<strike>\d{8})$")

CONTRACT_COLUMNS = ["bid", "ask", "bid_size", "ask_size", "iv", "delta", "gamma", "theta", "vega", "rho",
                     "theo", "open_interest", "volume", "last_trade_price", "prev_day_close"]
CHAIN_COLUMNS = ["symbol", "expiry", "strike", "right", "option_code"] + CONTRACT_COLUMNS + \
    ["mid", "last_trade_time", "underlying_price", "fetched_at", "source"]


class CboeFetchError(RuntimeError):
    """Raised by `fetch_chain` on any network, HTTP or JSON-shape failure."""


def _normalize_symbol(symbol: str) -> str:
    """`_SPX` -> `SPX`, `spy` -> `SPY`: the partition / column value, not the request string."""
    return symbol.upper().lstrip("_").lstrip("^")


def parse_occ_code(code: str) -> tuple[date, str, float] | None:
    """`SPY260908C00500000` -> `(date(2026, 9, 8), "C", 500.0)`, or `None` if it does not parse."""
    m = OCC_RE.match(code)
    if not m:
        return None
    try:
        expiry = date(2000 + int(m["yy"]), int(m["mm"]), int(m["dd"]))
    except ValueError:
        return None
    return expiry, m["right"], int(m["strike"]) / 1000.0


def fetch_chain(symbol: str, opener: Callable = urllib.request.urlopen,
                 timeout: int = FETCH_TIMEOUT_S) -> dict:
    """One GET of the CBOE delayed chain for `symbol`. Raises `CboeFetchError` on any failure."""
    import json as _json
    url = CBOE_CHAIN_URL.format(symbol=symbol)
    req = urllib.request.Request(url, headers=USER_AGENT)
    try:
        with opener(req, timeout=timeout) as resp:
            body = resp.read()
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise CboeFetchError(f"cboe_chain fetch failed for {symbol!r}: {exc}") from exc
    try:
        payload = _json.loads(body)
    except ValueError as exc:
        raise CboeFetchError(f"cboe_chain: unparseable JSON for {symbol!r}: {exc}") from exc
    if not isinstance(payload, dict) or "data" not in payload:
        raise CboeFetchError(f"cboe_chain: payload for {symbol!r} lacks a 'data' key")
    return payload


def chain_asof_date(payload: dict) -> date | None:
    """The session the chain's greeks describe, taken from the underlying's `last_trade_time`
    (not the top-level `timestamp`, which is the request's wall-clock time and, on a day the
    market is closed, is stale by the CBOE snapshot the API keeps serving)."""
    lt = (payload.get("data") or {}).get("last_trade_time")
    if not lt:
        return None
    try:
        return datetime.fromisoformat(lt).date()
    except ValueError:
        return None


def _underlying_price(data: dict) -> float | None:
    for key in ("current_price", "close", "prev_day_close"):
        v = data.get(key)
        if v is not None:
            return float(v)
    return None


def _num(row: dict, key: str) -> float | None:
    v = row.get(key)
    return None if v is None else float(v)


def _row_from_option(o: dict, symbol: str, underlying_price: float | None, fetched_at: datetime) -> dict | None:
    code = o.get("option")
    if not isinstance(code, str):
        return None
    parsed = parse_occ_code(code)
    if parsed is None:
        return None
    expiry, right, strike = parsed
    bid, ask = _num(o, "bid"), _num(o, "ask")
    mid = None if bid is None or ask is None else (bid + ask) / 2.0
    return {"symbol": symbol, "expiry": expiry, "strike": strike, "right": right, "option_code": code,
            "bid": bid, "ask": ask, "bid_size": _num(o, "bid_size"), "ask_size": _num(o, "ask_size"),
            "iv": _num(o, "iv"), "delta": _num(o, "delta"), "gamma": _num(o, "gamma"), "theta": _num(o, "theta"),
            "vega": _num(o, "vega"), "rho": _num(o, "rho"), "theo": _num(o, "theo"),
            "open_interest": _num(o, "open_interest"), "volume": _num(o, "volume"),
            "last_trade_price": _num(o, "last_trade_price"), "prev_day_close": _num(o, "prev_day_close"),
            "mid": mid, "last_trade_time": o.get("last_trade_time"), "underlying_price": underlying_price,
            "fetched_at": fetched_at, "source": SOURCE}


def parse_chain(payload: dict, fetched_at: datetime) -> pd.DataFrame:
    """One row per contract (`CHAIN_COLUMNS`). Malformed rows (an unparseable OCC code, or a
    missing `option` key) are dropped and counted; the count is never silent — a
    `logging.warning` line names `n_rejected` out of the total when it is nonzero.

    `fetched_at` should be a UTC-aware `datetime`; it is stamped on every row as-is.
    """
    data = payload.get("data") or {}
    options = data.get("options") or []
    symbol = _normalize_symbol(str(data.get("symbol") or payload.get("symbol") or ""))
    underlying_price = _underlying_price(data)
    rows, rejected = [], 0
    for o in options:
        row = _row_from_option(o, symbol, underlying_price, fetched_at)
        if row is None:
            rejected += 1
        else:
            rows.append(row)
    if rejected:
        log.warning("cboe_chain: rejected %d/%d malformed option rows for %s", rejected, len(options), symbol)
    if not rows:
        return pd.DataFrame(columns=CHAIN_COLUMNS)
    return pd.DataFrame(rows, columns=CHAIN_COLUMNS)


def _partition_path(symbol: str, d: date | str) -> str:
    sym = _normalize_symbol(symbol)
    d = d if isinstance(d, str) else d.isoformat()
    return os.path.join(CBOE_CHAIN_DIR, f"symbol={sym}", f"date={d}", "part.parquet")


def store_chain(df: pd.DataFrame, symbol: str, d: date | str, force: bool = False) -> str:
    """Write `data/mart/cboe_chain/symbol=<SYM>/date=<YYYY-MM-DD>/part.parquet`.

    Write-once: refuses to overwrite an existing date unless `force=True`.
    """
    path = _partition_path(symbol, d)
    if os.path.exists(path) and not force:
        raise FileExistsError(f"cboe_chain partition already exists: {path} (pass force=True to overwrite)")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)
    return path


def load_chain(symbol: str, d: date | str) -> pd.DataFrame:
    """Read a stored partition. Raises `FileNotFoundError` if it was never fetched."""
    path = _partition_path(symbol, d)
    if not os.path.exists(path):
        raise FileNotFoundError(f"no cboe_chain partition for {symbol!r} on {d}: {path}")
    return pd.read_parquet(path)


def has_chain(symbol: str, d: date | str) -> bool:
    return os.path.exists(_partition_path(symbol, d))


def refresh_one(symbol: str, d: date | None = None, fetch: Callable[[str], dict] = fetch_chain,
                 now: Callable[[], datetime] = lambda: datetime.now(timezone.utc),
                 force: bool = False) -> dict:
    """Fetch, parse and store one symbol. Never raises: returns
    `{"available": bool, "rows": int, "reason": str|None, "fetched_at": iso, "asof_date": iso|None}`.

    `d` pins the storage partition; when omitted, the date is taken from `chain_asof_date` (the
    underlying's last trade date), which is what a holiday/weekend snapshot needs (RESEARCH/47 G8).
    """
    fetched_at = now()
    try:
        payload = fetch(symbol)
        asof = chain_asof_date(payload) or d
        if asof is None:
            return {"available": False, "rows": 0, "reason": "no asof date in payload and none given",
                    "fetched_at": fetched_at.isoformat(), "asof_date": None}
        df = parse_chain(payload, fetched_at)
        if df.empty:
            return {"available": False, "rows": 0, "reason": "parsed chain is empty",
                    "fetched_at": fetched_at.isoformat(), "asof_date": asof.isoformat()}
        store_chain(df, symbol, asof, force=force)
        return {"available": True, "rows": int(len(df)), "reason": None,
                "fetched_at": fetched_at.isoformat(), "asof_date": asof.isoformat()}
    except FileExistsError as exc:
        return {"available": True, "rows": 0, "reason": f"already stored: {exc}",
                "fetched_at": fetched_at.isoformat(), "asof_date": None}
    except Exception as exc:  # network, parse, disk: the nightly must never crash on one symbol
        return {"available": False, "rows": 0, "reason": str(exc)[:300],
                "fetched_at": fetched_at.isoformat(), "asof_date": None}


def refresh_chains(symbols: Iterable[str], d: date | None = None,
                    fetch: Callable[[str], dict] = fetch_chain,
                    now: Callable[[], datetime] = lambda: datetime.now(timezone.utc),
                    force: bool = False) -> dict[str, dict]:
    """Fail-soft per symbol; returns `{symbol: refresh_one(...)}`. `symbols` should already include
    SPY and QQQ if the caller wants them (`engine.config` does not pin a default symbol list)."""
    return {symbol: refresh_one(symbol, d, fetch, now, force) for symbol in symbols}


def main() -> int:
    ap = argparse.ArgumentParser(description="Fetch and store the CBOE delayed option chain for one or more symbols.")
    ap.add_argument("--symbols", nargs="+", required=True, help="e.g. --symbols SPY QQQ")
    ap.add_argument("--date", default=None, help="storage date override (default: the payload's own asof date)")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    d = date.fromisoformat(a.date) if a.date else None
    result = refresh_chains(a.symbols, d, force=a.force)
    for symbol, r in result.items():
        print(f"{symbol}: {r}")
    return 0 if all(r["available"] for r in result.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
