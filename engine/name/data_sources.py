"""The network boundary of the ticker sheet's R1 loader (DESIGN/70 §1).

Every function here is one endpoint, fail-soft, with an injectable getter so the unit tests reach
it without a socket. They all return `{"available": bool, "reason": str|None, "value": <payload>}`,
so `engine.name.data` turns a failure into a `None` field plus one `nulls` entry without knowing
which endpoint produced it. Nothing here raises; nothing here logs a key.

Endpoints (RESEARCH/20 §4, §5), one function each: Finnhub `/calendar/earnings` through the repo's
cached wrapper (the primary earnings date) and `/stock/insider-transactions` (Form 4, 30 calendar
days); yfinance `calendar` (the third earnings opinion), `upgrades_downgrades` (analyst changes,
10 sessions), `info.shortPercentOfFloat`, and `option_chain` (the chain fallback; CBOE is primary).
`short_float` tries `engine.mart.finviz_short` first and names whichever tool answered.

`normalize_yf_chain` maps yfinance's chain columns onto `engine.mart.cboe_chain.CHAIN_COLUMNS`
with `source = "yfinance"`, so a fallback chain is the same frame to every consumer; the greeks
yfinance does not carry are null, never zero (RESEARCH/20 §4.1).

The Finnhub key is read by name (`FINNHUB_API_KEY` from the environment, else the `.env` at
`~/Development/stock-deep-dive/.env`); it is never printed and never written to any file.
"""
from __future__ import annotations

import os
from datetime import date, datetime, timedelta, timezone
from typing import Callable

import pandas as pd

from engine.mart import cboe_chain

OFFLINE = "offline"
FINNHUB_CALENDAR = "finnhub /calendar/earnings"
FINNHUB_INSIDER = "finnhub /stock/insider-transactions"
YF_CALENDAR = "yfinance calendar"
YF_UPGRADES = "yfinance upgrades_downgrades"
YF_INFO = "yfinance info shortPercentOfFloat"
YF_CHAIN = "yfinance option_chain"
FINVIZ = "finviz fz quote"

NETWORK_FIELDS = ("finnhub_earnings", "yf_earnings", "analyst", "form4", "short_float")

FINNHUB_ENV_VAR = "FINNHUB_API_KEY"
DEFAULT_ENV_PATH = os.path.expanduser("~/Development/stock-deep-dive/.env")
FINNHUB_BASE_URL = "https://finnhub.io/api/v1"
FINNHUB_CALENDAR_FORWARD_DAYS = 180      # one `/calendar/earnings` window; the next print is inside it
FORM4_LOOKBACK_DAYS = 30                 # DESIGN/70 §1: Form 4 rows in the last 30 calendar days
YF_FALLBACK_EXPIRIES = 8                 # the fallback chain is bounded: one HTTP call per expiry
ANALYST_SESSIONS = 10                    # DESIGN/70 §1: analyst changes over the last 10 sessions


def skipped(reason: str = OFFLINE) -> dict:
    """The fail-soft dict for a call that was not made (offline) or that failed."""
    return {"available": False, "reason": reason, "value": None}


def _ok(value) -> dict:
    return {"available": True, "reason": None, "value": value}


def finnhub_key(env: dict | None = None, env_path: str = DEFAULT_ENV_PATH) -> str | None:
    """`FINNHUB_API_KEY` from the environment, else from `env_path` read by name only.

    The value is returned to the caller that makes the request and is never logged, printed or
    written to disk by this package.
    """
    env = os.environ if env is None else env
    key = env.get(FINNHUB_ENV_VAR)
    if key:
        return key
    try:
        with open(env_path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line.startswith("#") or "=" not in line:
                    continue
                name, _, value = line.partition("=")
                if name.strip() == FINNHUB_ENV_VAR:
                    return value.strip().strip("'\"") or None
    except OSError:
        return None
    return None


def iso_date(value) -> str | None:
    """Anything date-like -> an ISO date string, or None when it cannot be read as one."""
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    try:
        ts = pd.to_datetime(value, errors="coerce")
    except (TypeError, ValueError):
        return None
    return None if ts is None or pd.isna(ts) else ts.date().isoformat()


def _scrub(text: str, key: str | None) -> str:
    """A reason string can only ever quote an exception; a wrapper that embeds the request URL in
    its message would carry the token into `meta.json`. Redact it before it leaves this module."""
    return text if not key else text.replace(key, "<FINNHUB_KEY>")


def _float(value) -> float | None:
    try:
        out = float(value)
    except (TypeError, ValueError):
        return None
    return None if pd.isna(out) else out


# --- Finnhub -------------------------------------------------------------------------------------

def _http_get_json(url: str):
    """Network boundary for the endpoints without a repo wrapper. Raises on any failure."""
    import json
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": "market-analysis-name-sheet/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def _default_calendar_fetch(**kwargs) -> dict:
    from engine.mart.earnings_history import fetch_finnhub_calendar_cached
    return fetch_finnhub_calendar_cached(**kwargs)


def finnhub_earnings_date(ticker: str, d: date, key: str | None, *,
                          fetch: Callable[..., dict] = _default_calendar_fetch,
                          forward_days: int = FINNHUB_CALENDAR_FORWARD_DAYS) -> dict:
    """The next scheduled print on or after `d` from Finnhub's earnings calendar.

    Goes through `engine.mart.earnings_history.fetch_finnhub_calendar_cached`, which caches one
    payload per ticker under `data/mart/earnings_history/finnhub/` and never raises on its own.
    `value` is `{"date": iso|None, "hour": str|None}`.
    """
    if not key:
        return skipped(f"{FINNHUB_ENV_VAR} not set")
    try:
        payload = fetch(ticker=ticker, frm=d.isoformat(),
                        to=(d + timedelta(days=forward_days)).isoformat(), key=key)
    except Exception as exc:                       # the sheet writes with a null, never a traceback
        return skipped(_scrub(f"{FINNHUB_CALENDAR}: {str(exc)[:200]}", key))
    if not payload.get("available"):
        return skipped(_scrub(str(payload.get("skip_reason") or f"{FINNHUB_CALENDAR}: unavailable"), key))
    rows = [r for r in (payload.get("rows") or []) if iso_date(r.get("date"))]
    future = sorted((r for r in rows if iso_date(r["date"]) >= d.isoformat()), key=lambda r: iso_date(r["date"]))
    if not future:
        return skipped(f"{FINNHUB_CALENDAR}: no print scheduled on or after {d.isoformat()}")
    return _ok({"date": iso_date(future[0]["date"]), "hour": future[0].get("hour") or None})


def _form4_row(row: dict) -> dict:
    return {"date": iso_date(row.get("transactionDate")), "name": row.get("name"),
            "code": row.get("transactionCode"), "shares": _float(row.get("change")),
            "price": _float(row.get("transactionPrice"))}


def finnhub_insider_transactions(ticker: str, d: date, key: str | None, *,
                                 getter: Callable[[str], object] = _http_get_json,
                                 days: int = FORM4_LOOKBACK_DAYS) -> dict:
    """Form 4 rows with a transaction date in `(d - days, d]` (DESIGN/70 §1 "Analyst changes, Form 4")."""
    if not key:
        return skipped(f"{FINNHUB_ENV_VAR} not set")
    frm = (d - timedelta(days=days)).isoformat()
    url = (f"{FINNHUB_BASE_URL}/stock/insider-transactions"
           f"?symbol={ticker}&from={frm}&to={d.isoformat()}&token={key}")
    try:
        payload = getter(url)
    except Exception as exc:
        return skipped(_scrub(f"{FINNHUB_INSIDER}: {str(exc)[:200]}", key))
    rows = payload.get("data") if isinstance(payload, dict) else None
    if not isinstance(rows, list):
        return skipped(f"{FINNHUB_INSIDER}: payload has no 'data' list")
    out = [_form4_row(r) for r in rows if isinstance(r, dict)]
    return _ok([r for r in out if r["date"] and frm < r["date"] <= d.isoformat()])


# --- yfinance ------------------------------------------------------------------------------------

def _yf_ticker(ticker: str):
    """Network boundary for every yfinance read. Raises when the package is absent or Yahoo is."""
    import yfinance
    return yfinance.Ticker(ticker)


def _calendar_earnings_date(calendar) -> str | None:
    """`Ticker.calendar` is a dict whose `Earnings Date` is a list of dates (RESEARCH/20 §4.1)."""
    if not isinstance(calendar, dict):
        return None
    value = calendar.get("Earnings Date")
    if isinstance(value, (list, tuple)):
        value = value[0] if value else None
    return iso_date(value)


def yf_earnings_date(ticker: str, *, yf_ticker: Callable = _yf_ticker) -> dict:
    """yfinance's own next-earnings opinion. `value` is `{"date": iso|None, "hour": None}` --
    the calendar block carries no session, so `hour` is always null here."""
    try:
        iso = _calendar_earnings_date(yf_ticker(ticker).calendar)
    except Exception as exc:
        return skipped(f"{YF_CALENDAR}: {str(exc)[:200]}")
    if iso is None:
        return skipped(f"{YF_CALENDAR}: no Earnings Date in the calendar block")
    return _ok({"date": iso, "hour": None})


def _grade_rows(frame: pd.DataFrame, since: date, through: date) -> list[dict]:
    """`upgrades_downgrades` is indexed by `GradeDate`; keep `(since, through]` only."""
    if frame is None or len(frame) == 0:
        return []
    df = frame.reset_index()
    date_col = "GradeDate" if "GradeDate" in df.columns else df.columns[0]
    out = []
    for _, row in df.iterrows():
        iso = iso_date(row.get(date_col))
        if iso is None or not (since.isoformat() < iso <= through.isoformat()):
            continue
        out.append({"date": iso, "firm": row.get("Firm"), "from": row.get("FromGrade"),
                    "to": row.get("ToGrade"), "action": row.get("Action")})
    return sorted(out, key=lambda r: r["date"])


def yf_upgrades_downgrades(ticker: str, since: date, through: date, *,
                           yf_ticker: Callable = _yf_ticker) -> dict:
    """Analyst changes with `GradeDate` in `(since, through]` (DESIGN/70 §1: the last 10 sessions)."""
    try:
        frame = yf_ticker(ticker).upgrades_downgrades
    except Exception as exc:
        return skipped(f"{YF_UPGRADES}: {str(exc)[:200]}")
    try:
        return _ok(_grade_rows(frame, since, through))
    except Exception as exc:                      # an unexpected frame shape is a null, not a crash
        return skipped(f"{YF_UPGRADES}: unreadable frame ({str(exc)[:120]})")


def yf_short_percent_of_float(ticker: str, *, yf_ticker: Callable = _yf_ticker) -> dict:
    """`info.shortPercentOfFloat` as a fraction of float (RESEARCH/20 §4.1: NVDA 0.0129)."""
    try:
        info = yf_ticker(ticker).info
    except Exception as exc:
        return skipped(f"{YF_INFO}: {str(exc)[:200]}")
    value = _float((info or {}).get("shortPercentOfFloat"))
    if value is None:
        return skipped(f"{YF_INFO}: shortPercentOfFloat absent")
    return _ok({"short_float": value, "short_float_source": YF_INFO})


def _pct(raw) -> float | None:
    """`"1.29%"` -> 0.0129; a bare number is already a fraction and is returned as one."""
    if isinstance(raw, str):
        text = raw.strip()
        if text.endswith("%"):
            value = _float(text[:-1])
            return None if value is None else value / 100.0
        return _float(text)
    return _float(raw)


def _default_finviz(ticker: str) -> dict:
    from engine.mart.finviz_short import short_float as fz_short_float
    return fz_short_float(ticker)


def short_float(ticker: str, *, finviz: Callable[[str], dict] = _default_finviz,
                yf_ticker: Callable = _yf_ticker) -> dict:
    """Short float with its source named: `fz quote` first, yfinance `info` second, else a null.

    `engine.mart.finviz_short` documents a live `fz` regression that blanks the field; this is the
    fallback that regression asks for, and the answer always says which tool produced it.
    """
    try:
        fz = finviz(ticker)
    except Exception as exc:
        fz = {"available": False, "reason": f"{FINVIZ}: {str(exc)[:160]}"}
    if fz.get("available"):
        value = _pct(fz.get("short_float"))
        if value is not None:
            return _ok({"short_float": value, "short_float_source": FINVIZ})
    fallback = yf_short_percent_of_float(ticker, yf_ticker=yf_ticker)
    if fallback["available"]:
        return fallback
    return skipped(f"{fz.get('reason') or FINVIZ}; {fallback['reason']}")


# --- The yfinance chain fallback, normalised onto the cboe_chain column set ----------------------

_YF_CHAIN_MAP = {"bid": "bid", "ask": "ask", "iv": "impliedVolatility", "volume": "volume",
                 "open_interest": "openInterest", "last_trade_price": "lastPrice",
                 "strike": "strike", "option_code": "contractSymbol"}
_YF_CHAIN_NULL = ("bid_size", "ask_size", "delta", "gamma", "theta", "vega", "rho", "theo",
                  "prev_day_close")


def _yf_side(frame: pd.DataFrame, right: str, symbol: str, expiry: date,
             underlying_price: float | None, fetched_at: datetime) -> list[dict]:
    if frame is None or len(frame) == 0:
        return []
    rows = []
    for _, r in frame.iterrows():
        row = {"symbol": symbol, "expiry": expiry, "right": right}
        for target, source in _YF_CHAIN_MAP.items():
            row[target] = r.get(source) if target == "option_code" else _float(r.get(source))
        for col in _YF_CHAIN_NULL:
            row[col] = None
        bid, ask = row["bid"], row["ask"]
        row["mid"] = None if bid is None or ask is None else (bid + ask) / 2.0
        row["last_trade_time"] = _iso_datetime(r.get("lastTradeDate"))
        row["underlying_price"] = underlying_price
        row["fetched_at"] = fetched_at
        row["source"] = "yfinance"
        rows.append(row)
    return rows


def _iso_datetime(value) -> str | None:
    if value is None:
        return None
    try:
        ts = pd.to_datetime(value, errors="coerce")
    except (TypeError, ValueError):
        return None
    return None if ts is None or pd.isna(ts) else ts.isoformat()


def normalize_yf_chain(calls: pd.DataFrame, puts: pd.DataFrame, *, symbol: str, expiry: date,
                       underlying_price: float | None, fetched_at: datetime) -> pd.DataFrame:
    """One yfinance expiry -> `cboe_chain.CHAIN_COLUMNS` with `source = "yfinance"`.

    yfinance carries no greeks and no quote sizes, so those columns are null (RESEARCH/20 §4.1);
    a consumer that needs them must check `chain_meta["source"]` rather than read a zero.
    """
    rows = (_yf_side(calls, "C", symbol, expiry, underlying_price, fetched_at)
            + _yf_side(puts, "P", symbol, expiry, underlying_price, fetched_at))
    if not rows:
        return pd.DataFrame(columns=cboe_chain.CHAIN_COLUMNS)
    return pd.DataFrame(rows, columns=cboe_chain.CHAIN_COLUMNS)


def yf_option_chain(ticker: str, d: date, *, yf_ticker: Callable = _yf_ticker,
                    max_expiries: int = YF_FALLBACK_EXPIRIES) -> dict:
    """The marked chain fallback of DESIGN/70 §1: the nearest `max_expiries` listed expiries on or
    after `d`, each one HTTP call, concatenated into the cboe_chain column set.

    Bounded on purpose -- a name with 23 expiries would otherwise be 23 requests for a fallback
    that is only reached when CBOE is unavailable. `value` is the frame; the caller records the
    bound in `chain_meta`.
    """
    fetched_at = datetime.now(timezone.utc)
    try:
        handle = yf_ticker(ticker)
        expiries = [e for e in (handle.options or []) if iso_date(e) and iso_date(e) >= d.isoformat()]
    except Exception as exc:
        return skipped(f"{YF_CHAIN}: {str(exc)[:200]}")
    if not expiries:
        return skipped(f"{YF_CHAIN}: no listed expiry on or after {d.isoformat()}")
    frames, failed = [], []
    for raw in sorted(expiries)[:max_expiries]:
        try:
            chain = handle.option_chain(raw)
            spot = _float(getattr(chain, "underlying", {}).get("regularMarketPrice")
                          if isinstance(getattr(chain, "underlying", None), dict) else None)
            frames.append(normalize_yf_chain(chain.calls, chain.puts, symbol=ticker.upper(),
                                             expiry=date.fromisoformat(iso_date(raw)),
                                             underlying_price=spot, fetched_at=fetched_at))
        except Exception as exc:
            failed.append(f"{raw}: {str(exc)[:80]}")
    if not frames:
        return skipped(f"{YF_CHAIN}: every expiry failed ({'; '.join(failed)[:200]})")
    out = pd.concat(frames, ignore_index=True)[list(cboe_chain.CHAIN_COLUMNS)]
    return {"available": True, "value": out,
            "reason": f"{len(failed)} expiries failed: {'; '.join(failed)[:160]}" if failed else None}


# --- One call per sheet: every network field at once, or every one skipped -----------------------

def collect(ticker: str, d: date, *, online: bool = True, key: str | None = None,
            analyst_since: date | None = None, yf_ticker: Callable = _yf_ticker,
            finnhub_getter: Callable = _http_get_json, finviz_runner: Callable = _default_finviz,
            calendar_fetch: Callable = _default_calendar_fetch) -> dict:
    """`NETWORK_FIELDS` -> the fail-soft dict each endpoint returned.

    `online=False` makes no call at all -- every field is `skipped("offline")`, which is what the
    loader turns into a `nulls` entry. The chain is deliberately not here: it is resolved lazily
    (CBOE first, this module's `yf_option_chain` only if that fails) by `engine.name.data`.
    """
    if not online:
        return {field: skipped(OFFLINE) for field in NETWORK_FIELDS}
    from engine import calendar as cal
    since = analyst_since or cal.prev_session(d, ANALYST_SESSIONS)
    return {
        "finnhub_earnings": finnhub_earnings_date(ticker, d, key, fetch=calendar_fetch),
        "yf_earnings": yf_earnings_date(ticker, yf_ticker=yf_ticker),
        "analyst": yf_upgrades_downgrades(ticker, since, d, yf_ticker=yf_ticker),
        "form4": finnhub_insider_transactions(ticker, d, key, getter=finnhub_getter),
        "short_float": short_float(ticker, finviz=finviz_runner, yf_ticker=yf_ticker),
    }
