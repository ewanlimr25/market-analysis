"""R1 of the ticker sheet: every DESIGN/70 §1 input for one name on one session, in one object.

`load_inputs(ticker, d)` returns a frozen `NameInputs`; `write_inputs` puts it on disk (frames to
parquet, everything else to two JSON files) and `read_inputs` is the exact inverse, so a sheet
re-derives offline from `analyses/ticker/<T>/<DATE>/inputs/` without a socket (DESIGN/70 §1, §10 R1).

This module is a *caller* of the engine's existing marts, never a second copy of one
(RESEARCH/20 §6): `engine.strategies.sc_data` for the screener row, the 20-day dollar ADV and the
session's `daily_contract` rows; `engine.mart.store` partitions for `intraday_rv`; `engine.watch.bars`
for the cached 10-year daily bars; `engine.mart.earnings_history` / `earnings_events` for the print
history; `engine.mart.cboe_chain` for the chain; `borrow`, `short_interest`, `finviz_short`,
`index_vol` for the flag row; `scripts/_regime` for the label. Only the two queries this module owns
are written here: the trailing screener history (one DuckDB scan of the screener glob filtered by
ticker -- 0.3 s over the 112-file export) and the trailing contract sessions (one scan of the 21
named `daily_contract` partition paths with `WHERE underlying_symbol = ?`; the 3.4 GB table is never
scanned whole). The per-session aggregation itself is `contract_sessions`, a pure function.

Two invariants (the brief's hard rules, DESIGN/70 §1):

  * **Nulls are values.** Every field that could not be filled is `None` (or an empty frame) *and*
    carries an entry in `nulls` -- `[{"field", "reason"}]`. Nothing here raises for missing data.
  * **Every number names its source.** `sources[field]` is the mart, chain or endpoint plus the
    date the value carries, so the sheet can print it beside the number.

`online=False` makes no network call at all: the Finnhub, yfinance, finviz, CBOE-fetch and Yahoo
bars-refresh paths are skipped and recorded as nulls with reason `"offline"`. The CBOE chain is
still read when a partition for `(ticker, d)` is already stored -- that is a mart read, not a fetch.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta

import duckdb
import pandas as pd

from engine import calendar as cal
from engine import config
from engine.config import NAME_PARAMS
from engine.name import data_marts as marts
from engine.name import data_sources as src
from engine.schema import clean
from engine.strategies import sc_data

CONTRACT_SESSION_COLUMNS = ("date", "n_contracts", "n_hot", "n_prints", "premium_total")
SCREENER_HISTORY_COLUMNS = ("date", "close", "iv30d", "iv_rank", "bullish_premium",
                            "bearish_premium", "total_volume", "avg30_volume", "marketcap")
UNIVERSE_COLUMNS = ("ticker", "bullish_premium", "bearish_premium", "total_volume",
                    "avg30_volume", "issue_type", "is_index")
BARS_YEARS = 10                          # DESIGN/70 §1 row 4: ten years of daily bars
BORROW_MAX_STALE_DAYS = 5                # DESIGN/70 §1: `borrow.load_borrow_asof(DATE, 5)`
FOMC_WINDOW_DAYS = 45                    # `events.macro`: decisions inside the next 45 calendar days
SPY = "SPY"                              # `beta_250` and the context block are measured against it

# The published FOMC decision dates (federalreserve.gov calendar, read 2026-09-20). Hard-coded
# because no free dated feed carries them and the sheet must be reproducible offline; extend the
# tuple when the Board publishes the next year, never compute it.
FOMC_DATES: tuple[date, ...] = (
    date(2026, 1, 28), date(2026, 3, 18), date(2026, 4, 29), date(2026, 6, 17),
    date(2026, 7, 29), date(2026, 9, 16), date(2026, 10, 28), date(2026, 12, 9),
    date(2027, 1, 27), date(2027, 3, 17), date(2027, 4, 28), date(2027, 6, 9),
    date(2027, 7, 28), date(2027, 9, 15), date(2027, 10, 27), date(2027, 12, 8),
)

FRAME_FIELDS = ("contracts_today", "contract_sessions", "rv", "bars", "spy_bars",
                "screener_history", "universe_today", "earnings_events", "earnings_history", "chain")
VALUE_FIELDS = ("screener", "adv_usd_20d", "earnings_dates", "chain_meta", "borrow",
                "short_interest", "analyst", "form4", "index_vol", "regime", "fomc")
VALUES_FILE = "values.json"
META_FILE = "meta.json"

# Columns rendered as DATE by DuckDB or parquet that every consumer keys on as `datetime.date`.
DATE_COLUMNS = ("date", "expiry", "E", "pre", "post", "settlement_date", "publication_date")


def _empty(columns) -> pd.DataFrame:
    return pd.DataFrame({c: pd.Series([], dtype="object") for c in columns})


def _as_dates(df: pd.DataFrame) -> pd.DataFrame:
    """A new frame with every `DATE_COLUMNS` entry as `datetime.date` (never a Timestamp)."""
    if df is None or df.empty:
        return df
    todo = {c: pd.to_datetime(df[c], errors="coerce").dt.date
            for c in DATE_COLUMNS if c in df.columns and not _is_date_like(df[c])}
    return df.assign(**todo) if todo else df


def _is_date_like(s: pd.Series) -> bool:
    return s.dtype == "object" and len(s) > 0 and isinstance(s.iloc[0], date) and not isinstance(s.iloc[0], datetime)


@dataclass(frozen=True)
class NameInputs:
    """Every DESIGN/70 §1 input for `(ticker, date)`. Frames are point-in-time slices; dicts and
    lists are JSON-able as they stand. A field that could not be filled is None/empty and named in
    `nulls`; `sources` names the mart or endpoint and the date behind every field."""

    ticker: str
    date: date
    screener: dict | None = None
    contracts_today: pd.DataFrame = field(default_factory=pd.DataFrame)
    contract_sessions: pd.DataFrame = field(default_factory=lambda: _empty(CONTRACT_SESSION_COLUMNS))
    rv: pd.DataFrame = field(default_factory=pd.DataFrame)
    bars: pd.DataFrame = field(default_factory=pd.DataFrame)
    spy_bars: pd.DataFrame = field(default_factory=pd.DataFrame)
    screener_history: pd.DataFrame = field(default_factory=lambda: _empty(SCREENER_HISTORY_COLUMNS))
    universe_today: pd.DataFrame = field(default_factory=lambda: _empty(UNIVERSE_COLUMNS))
    adv_usd_20d: float | None = None
    earnings_events: pd.DataFrame = field(default_factory=pd.DataFrame)
    earnings_history: pd.DataFrame = field(default_factory=pd.DataFrame)
    earnings_dates: dict = field(default_factory=dict)
    chain: pd.DataFrame | None = None
    chain_meta: dict = field(default_factory=dict)
    borrow: dict | None = None
    short_interest: dict | None = None
    analyst: list = field(default_factory=list)
    form4: list = field(default_factory=list)
    index_vol: dict | None = None
    regime: dict | None = None
    fomc: list = field(default_factory=list)
    nulls: list = field(default_factory=list)
    sources: dict = field(default_factory=dict)


# --- Pure helpers (no I/O; every one of these is a unit test) -------------------------------------

def contract_sessions(rows: pd.DataFrame) -> pd.DataFrame:
    """Per-session counts from `daily_contract` rows of one underlying: one row per session with
    `n_contracts`, `n_hot` (rows whose `hc_volume` is non-null and > 0 -- L4's hot-chain count),
    `n_prints` and `premium_total`. Pure: the input frame is never mutated."""
    if rows is None or rows.empty:
        return _empty(CONTRACT_SESSION_COLUMNS)
    hot = rows["hc_volume"].notna() & (pd.to_numeric(rows["hc_volume"], errors="coerce") > 0)
    df = rows.assign(_hot=hot.astype("int64"))
    out = (df.groupby("date", as_index=False)
             .agg(n_contracts=("_hot", "size"), n_hot=("_hot", "sum"),
                  n_prints=("n_prints", "sum"), premium_total=("premium_total", "sum"))
             .sort_values("date").reset_index(drop=True))
    return out[list(CONTRACT_SESSION_COLUMNS)]


def fomc_window(d: date, days: int = FOMC_WINDOW_DAYS) -> list[str]:
    """The published FOMC decision dates in `[d, d + days]`, ISO, ascending."""
    end = d + timedelta(days=days)
    return [x.isoformat() for x in FOMC_DATES if d <= x <= end]


def _source_entry(result: dict | None, name: str) -> tuple[str | None, str | None]:
    if result is None:
        return None, "not requested"
    value = result.get("value") or {}
    return (value.get("date"), None) if result.get("available") else (None, result.get("reason") or f"{name}: unavailable")


def earnings_dates(screener: dict | None, finnhub: dict | None, yfinance: dict | None,
                   d: date) -> dict:
    """The three opinions DESIGN/70 §1 says the sheet prints side by side, never reconciled here.

    Each entry is `{"date": iso|None, "hour": str|None, "source": str, "reason": str|None}`;
    R2's `events.confirmed` is the one that compares them.
    """
    fh_date, fh_reason = _source_entry(finnhub, src.FINNHUB_CALENDAR)
    yf_date, yf_reason = _source_entry(yfinance, src.YF_CALENDAR)
    scr_date = src.iso_date((screener or {}).get("next_earnings_date")) if screener else None
    scr_hour = (screener or {}).get("er_time") if screener else None
    return {
        "finnhub": {"date": fh_date, "hour": ((finnhub or {}).get("value") or {}).get("hour"),
                    "source": src.FINNHUB_CALENDAR, "reason": fh_reason},
        "screener": {"date": scr_date, "hour": scr_hour or None,
                     "source": f"screener {d.isoformat()}",
                     "reason": None if scr_date else ("no screener row" if not screener
                                                      else "screener next_earnings_date is null")},
        "yfinance": {"date": yf_date, "hour": None, "source": src.YF_CALENDAR, "reason": yf_reason},
    }


# --- The inputs directory: write once, re-derive offline (DESIGN/70 §1 last paragraph) -----------

def _frame_path(out_dir: str, name: str) -> str:
    return os.path.join(out_dir, f"{name}.parquet")


def write_inputs(inputs: NameInputs, out_dir: str) -> list[str]:
    """Write every field of `inputs` under `out_dir`; returns the paths written, ascending.

    One parquet per frame (`chain.parquet` is absent when there is no chain -- a null is a fact,
    not an empty file), `values.json` for the dicts, lists and scalars, and `meta.json` carrying
    the ticker, the date, `nulls` and `sources`. `engine.schema.clean` is applied to everything
    JSON so the files are strict JSON (no NaN, no numpy scalars, dates as ISO strings).
    """
    os.makedirs(out_dir, exist_ok=True)
    written = []
    for name in FRAME_FIELDS:
        frame = getattr(inputs, name)
        if frame is None:
            continue
        path = _frame_path(out_dir, name)
        frame.to_parquet(path, index=False)
        written.append(path)
    values_path = os.path.join(out_dir, VALUES_FILE)
    _write_json(values_path, {name: clean(getattr(inputs, name)) for name in VALUE_FIELDS})
    meta_path = os.path.join(out_dir, META_FILE)
    _write_json(meta_path, {"ticker": inputs.ticker, "date": inputs.date.isoformat(),
                            "nulls": clean(inputs.nulls), "sources": clean(inputs.sources)})
    return sorted(written + [values_path, meta_path])


def _write_json(path: str, payload) -> None:
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, sort_keys=True, allow_nan=False)
    os.replace(tmp, path)


def read_inputs(in_dir: str) -> NameInputs:
    """The exact inverse of `write_inputs`. Raises only when `meta.json` is missing -- an absent
    frame file is the same null the writer recorded, not an error."""
    meta = json.loads(open(os.path.join(in_dir, META_FILE), encoding="utf-8").read())
    values_path = os.path.join(in_dir, VALUES_FILE)
    values = json.loads(open(values_path, encoding="utf-8").read()) if os.path.exists(values_path) else {}
    kwargs: dict = {"ticker": meta["ticker"], "date": date.fromisoformat(meta["date"]),
                    "nulls": meta.get("nulls") or [], "sources": meta.get("sources") or {}}
    for name in VALUE_FIELDS:
        if name in values:
            kwargs[name] = values[name]
    for name in FRAME_FIELDS:
        path = _frame_path(in_dir, name)
        if os.path.exists(path):
            kwargs[name] = _as_dates(pd.read_parquet(path))
        elif name == "chain":
            kwargs[name] = None
    return NameInputs(**kwargs)


# --- The loader (DESIGN/70 §1; `online=False` makes no network call at all) ----------------------

def load_inputs(ticker: str, d: date, *, con=None, online: bool = True, params=NAME_PARAMS,
                stocks_dir: str = config.STOCKS, finnhub_key: str | None = None) -> NameInputs:
    """Every DESIGN/70 §1 input for `(ticker, d)`, with `nulls` and `sources` filled.

    Never raises for missing data: a source that is absent, stale or refusing produces `None` (or
    an empty frame) plus one `nulls` entry naming the field and the reason. `online=False` skips
    Finnhub, yfinance, finviz, the CBOE fetch and the Yahoo bars refresh, and records each skipped
    field with reason `"offline"`; stored marts (including a stored `cboe_chain` partition) are
    still read. `finnhub_key` defaults to `FINNHUB_API_KEY` in the environment, else the `.env` at
    `~/Development/stock-deep-dive/.env`, read by name -- it is never written to the inputs dir.
    """
    ticker = ticker.upper()
    con = con or duckdb.connect()
    nulls: list[dict] = []
    sources: dict[str, str] = {}

    def take(name: str, triple):
        value, source, reason = triple
        sources[name] = source
        if reason:
            nulls.append({"field": name, "reason": reason})
        return value

    key = finnhub_key if finnhub_key is not None else src.finnhub_key()
    net = src.collect(ticker, d, online=online, key=key,
                      analyst_since=cal.prev_session(d, src.ANALYST_SESSIONS))

    day, scr_source, scr_reason = marts.screener_day(con, d, stocks_dir)
    screener = take("screener", _pair(marts.screener_row(day, ticker), scr_source, scr_reason))
    universe = take("universe_today", _pair(marts.universe_today(day, UNIVERSE_COLUMNS),
                                            scr_source, scr_reason))
    contracts = take("contracts_today", marts.contracts_today(con, ticker, d))
    session_rows = take("contract_sessions",
                        marts.contract_session_rows(con, ticker, d, params.hot_chain_window))
    rv = take("rv", marts.rv_rows(con, ticker, d, params.rv_window))
    bars = take("bars", marts.daily_bars(ticker, d, BARS_YEARS, online=online))
    spy_bars = take("spy_bars", marts.daily_bars(SPY, d, BARS_YEARS, online=online))
    history = take("screener_history", marts.screener_history(con, ticker, d, params.iv_pct_window,
                                                              SCREENER_HISTORY_COLUMNS, stocks_dir))
    adv = take("adv_usd_20d", _adv(con, ticker, d))
    events = take("earnings_events", marts.earnings_event_rows(con, ticker))
    history_events = take("earnings_history", marts.earnings_history_rows(ticker))
    chain, chain_meta = marts.resolve_chain(ticker, d, online=online)
    sources["chain"] = f"{chain_meta['source'] or 'none'} {chain_meta['date'] or d.isoformat()}"
    if chain is None:
        nulls.append({"field": "chain", "reason": chain_meta["reason"]})
    borrow = take("borrow", marts.borrow_row(ticker, d, BORROW_MAX_STALE_DAYS))
    si = take("short_interest", marts.short_interest_row(ticker, d, net["short_float"]))
    if (si or {}).get("short_float") is None:          # X5 reads it; a null must say why
        nulls.append({"field": "short_interest.short_float", "reason": net["short_float"]["reason"]})
    ivol = take("index_vol", marts.index_vol_row(d))
    regime = take("regime", marts.regime_row(d, con))

    dates = earnings_dates(screener, net["finnhub_earnings"], net["yf_earnings"], d)
    sources["earnings_dates"] = " + ".join(v["source"] for v in dates.values())
    nulls.extend({"field": f"earnings_dates.{k}", "reason": v["reason"]}
                 for k, v in dates.items() if v["reason"])
    analyst = take("analyst", _from_net(net["analyst"], src.YF_UPGRADES, d))
    form4 = take("form4", _from_net(net["form4"], src.FINNHUB_INSIDER, d))
    sources["fomc"] = "FOMC published calendar (engine.name.data.FOMC_DATES)"

    return NameInputs(
        ticker=ticker, date=d, screener=_clean_row(screener), contracts_today=_as_dates(contracts),
        contract_sessions=contract_sessions(session_rows), rv=rv, bars=bars, spy_bars=spy_bars,
        screener_history=_as_dates(history), universe_today=universe, adv_usd_20d=adv,
        earnings_events=_as_dates(events), earnings_history=_as_dates(history_events),
        earnings_dates=dates, chain=chain, chain_meta=chain_meta, borrow=borrow,
        short_interest=si, analyst=analyst, form4=form4, index_vol=ivol, regime=clean(regime),
        fomc=fomc_window(d), nulls=nulls, sources=sources)


def _pair(pair, source: str, day_reason: str | None):
    """`(value, reason)` from a screener helper -> the `(value, source, reason)` `take` expects."""
    value, reason = pair
    return value, source, (day_reason or reason)


def _adv(con, ticker: str, d: date):
    source = f"prices.parquet 20 sessions to {d.isoformat()}"
    try:
        value = sc_data.adv_usd_20d(con, [ticker], d).get(ticker)
    except Exception as exc:
        return None, source, f"adv_usd_20d failed: {str(exc)[:160]}"
    return value, source, (None if value is not None else f"fewer than 10 priced sessions for {ticker}")


def _from_net(result: dict, endpoint: str, d: date):
    """A `data_sources` result -> `(value, source, reason)`; an unavailable call is an empty list."""
    source = f"{endpoint} <= {d.isoformat()}"
    if not result.get("available"):
        return [], source, result.get("reason")
    return clean(result["value"]), source, None


def _clean_row(row: dict | None) -> dict | None:
    """The screener row as strict JSON (Timestamps to ISO, numpy scalars to Python, NaN to null)."""
    return None if row is None else clean(row)
