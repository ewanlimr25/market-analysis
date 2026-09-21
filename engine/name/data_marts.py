"""The mart boundary of the ticker sheet's R1 loader (DESIGN/70 §1): one function per §1 row.

Everything here is a read of an existing mart or export -- no network except the two places
DESIGN/70 §1 names one (the CBOE chain fetch and the Yahoo bars refresh), and both are behind an
`online` flag. Each function returns `(value, source, reason)`: `source` names the mart and the
date the value carries, `reason` is `None` on success and the null's explanation otherwise.
`engine.name.data` turns those triples into `NameInputs`, `sources` and `nulls`.

Point-in-time is the rule everywhere: a trailing window is `<= d`, never a window centred on it,
and nothing reads a partition dated after `d`. The panel's own lag is a fact the source string
carries, not something this module hides (`intraday_rv` stops at 2026-09-04 while `daily_contract`
runs to 09-18; the sheet prints both dates).
"""
from __future__ import annotations

import os
from datetime import date, datetime, timezone

import pandas as pd

from engine import config
from engine.mart import borrow as borrow_mart
from engine.mart import cboe_chain, earnings_history, index_vol, short_interest, store
from engine.name import data_sources as src
from engine.strategies import sc_data

CONTRACTS = "daily_contract"
RV_TABLE = "intraday_rv"
EARNINGS_EVENTS = "earnings_events"


def _partition_list(table: str, d: date, window: int) -> list[date]:
    """The `window` stored partitions of `table` dated on or before `d`, ascending."""
    return [x for x in store.available_dates(table) if x <= d][-window:]


def _read_paths(con, table: str, days: list[date], where: str, params: list) -> pd.DataFrame:
    """One DuckDB scan of the named partition files only -- never the whole table glob."""
    if not days:
        return pd.DataFrame()
    files = ", ".join("'" + store.partition_path(table, x).replace("'", "''") + "'" for x in days)
    return con.execute(f"SELECT * FROM read_parquet([{files}], union_by_name=true) WHERE {where}",
                       params).df()


# --- Screener (DESIGN/70 §1 rows 2 and 10) --------------------------------------------------------

def screener_day(con, d: date, stocks_dir: str = config.STOCKS) -> tuple[pd.DataFrame, str, str | None]:
    """Every screener row of session `d`, all 52 columns (the sheet's spine and its universe)."""
    path = sc_data.screener_path(d, stocks_dir)
    source = f"screener {d.isoformat()}"
    if not os.path.exists(path):
        return pd.DataFrame(), source, f"no screener export for {d.isoformat()}"
    df = con.execute(f"SELECT * FROM read_parquet('{path}')").df()
    return df, source, None


def screener_row(day: pd.DataFrame, ticker: str) -> tuple[dict | None, str | None]:
    if day.empty or "ticker" not in day.columns:
        return None, "no screener export"
    hit = day[day["ticker"] == ticker]
    if hit.empty:
        return None, f"no screener row for {ticker}"
    return hit.iloc[0].to_dict(), None


def universe_today(day: pd.DataFrame, columns) -> tuple[pd.DataFrame, str | None]:
    """The session's whole screener universe, the columns the context percentile needs."""
    if day.empty:
        return pd.DataFrame({c: pd.Series([], dtype="object") for c in columns}), "no screener export"
    missing = [c for c in columns if c not in day.columns]
    if missing:
        return pd.DataFrame(), f"screener export lacks {', '.join(missing)}"
    return day[list(columns)].reset_index(drop=True), None


def screener_history(con, ticker: str, d: date, sessions: int, columns,
                     stocks_dir: str = config.STOCKS) -> tuple[pd.DataFrame, str, str | None]:
    """The name's own trailing `sessions` screener rows on or before `d` (`iv_pct_own`, self flow).

    One DuckDB scan of the whole screener glob filtered by ticker: 0.27 s over the 112-file export
    on 2026-09-20, so the file list is left to the glob. Should the export grow past a few hundred
    files, restrict it to the named session paths the way `_read_paths` does.
    """
    glob = os.path.join(stocks_dir, config.SCREENER_GLOB)
    cols = ", ".join(columns)
    try:
        df = con.execute(
            f"SELECT {cols} FROM read_parquet('{glob}', union_by_name=true) "
            f"WHERE ticker = ? AND date <= DATE '{d.isoformat()}' ORDER BY date DESC LIMIT {sessions}",
            [ticker]).df()
    except Exception as exc:
        return pd.DataFrame(), f"screener glob <= {d.isoformat()}", f"screener history query failed: {str(exc)[:160]}"
    df = df.sort_values("date").reset_index(drop=True)
    if df.empty:
        return df, f"screener glob <= {d.isoformat()}", f"no screener history for {ticker}"
    first = pd.to_datetime(df["date"].iloc[0]).date().isoformat()
    return df, f"screener {first}..{d.isoformat()} ({len(df)} sessions)", None


# --- daily_contract (DESIGN/70 §1 row 1) ----------------------------------------------------------

def contracts_today(con, ticker: str, d: date) -> tuple[pd.DataFrame, str, str | None]:
    """`sc_data.load_contract_rows` for one underlying: every `daily_contract` row of `d`."""
    source = f"{CONTRACTS} {d.isoformat()}"
    if not store.has_partition(CONTRACTS, d):
        return pd.DataFrame(), source, f"no {CONTRACTS} partition for {d.isoformat()}"
    df = sc_data.load_contract_rows(con, [ticker], d)
    return df, source, (None if not df.empty else f"no {CONTRACTS} rows for {ticker} on {d.isoformat()}")


def contract_session_rows(con, ticker: str, d: date, window: int) -> tuple[pd.DataFrame, str, str | None]:
    """The columns `contract_sessions` aggregates, over the trailing `window` stored partitions.

    One query over the named partition paths with `WHERE underlying_symbol = ?`; the 3.4 GB table
    is never scanned whole (RESEARCH/20 §6.2).
    """
    days = _partition_list(CONTRACTS, d, window)
    if not days:
        return pd.DataFrame(), f"{CONTRACTS} <= {d.isoformat()}", f"no {CONTRACTS} partitions on or before {d.isoformat()}"
    files = ", ".join("'" + store.partition_path(CONTRACTS, x).replace("'", "''") + "'" for x in days)
    df = con.execute(
        f"SELECT date, hc_volume, n_prints, premium_total FROM read_parquet([{files}], union_by_name=true) "
        f"WHERE underlying_symbol = ?", [ticker]).df()
    if not df.empty:
        df = df.assign(date=pd.to_datetime(df["date"]).dt.date)
    source = f"{CONTRACTS} {days[0].isoformat()}..{days[-1].isoformat()} ({len(days)} sessions)"
    return df, source, (None if not df.empty else f"no {CONTRACTS} rows for {ticker} in the window")


def rv_rows(con, ticker: str, d: date, window: int) -> tuple[pd.DataFrame, str, str | None]:
    """`intraday_rv` rows for the name over the trailing `window` stored partitions on or before `d`.

    The table lags `daily_contract` (RESEARCH/20 §6.2: 09-04 against 09-18); the source string
    carries the dates it actually holds so the sheet can print the lag rather than hide it.
    """
    days = _partition_list(RV_TABLE, d, window)
    if not days:
        return pd.DataFrame(), f"{RV_TABLE} <= {d.isoformat()}", f"no {RV_TABLE} partitions on or before {d.isoformat()}"
    df = _read_paths(con, RV_TABLE, days, "underlying_symbol = ?", [ticker])
    if not df.empty:
        df = df.assign(date=pd.to_datetime(df["date"]).dt.date).sort_values("date").reset_index(drop=True)
    source = f"{RV_TABLE} {days[0].isoformat()}..{days[-1].isoformat()} ({len(days)} sessions)"
    return df, source, (None if not df.empty else f"no {RV_TABLE} rows for {ticker} in the window")


# --- Daily bars (DESIGN/70 §1 row 4) --------------------------------------------------------------

def _bars_cached(ticker: str) -> bool:
    return any(os.path.exists(p) for p in (watch_bars_path(ticker), eh_bars_path(ticker)))


def watch_bars_path(ticker: str) -> str:
    from engine.watch.bars import watch_bars_path as p
    return p(ticker)


def eh_bars_path(ticker: str) -> str:
    return earnings_history.bars_path(ticker)


def daily_bars(ticker: str, d: date, years: int, *, online: bool = True) -> tuple[pd.DataFrame, str, str | None]:
    """Ten years of daily OHLCV through the last session on or before `d`.

    `engine.watch.bars.load_daily_bars` owns the cache (`earnings_history/bars/<T>.parquet`
    read-only, its own `watch/bars/<T>.parquet` for refreshes) and the Yahoo hole-healing that
    `scripts/chart.py` does; passing `as_of` makes it refresh a cache that stops short, which is a
    network call and therefore only happens when `online`. Offline with no cache at all is a null.
    """
    from engine.watch import bars as watch_bars
    source = f"earnings_history/bars + watch/bars <= {d.isoformat()}"
    if not online and not _bars_cached(ticker):
        return pd.DataFrame(), source, f"offline and no cached bars for {ticker}"
    try:
        daily = watch_bars.load_daily_bars(ticker, as_of=d) if online else watch_bars.load_daily_bars(ticker)
    except Exception as exc:                       # load_daily_bars is fail-soft, but never trust it
        return pd.DataFrame(), source, f"bars load failed: {str(exc)[:160]}"
    sliced = watch_bars.bars_as_of(daily, d)
    if sliced.empty:
        return sliced, source, f"no bars for {ticker} on or before {d.isoformat()}"
    cut = date(d.year - years, d.month, d.day) if (d.month, d.day) != (2, 29) else date(d.year - years, 2, 28)
    sliced = sliced[sliced["date"] >= cut].reset_index(drop=True)
    tail = sliced["date"].iloc[-1]
    return sliced, f"earnings_history/bars + watch/bars {sliced['date'].iloc[0]}..{tail}", None


# --- Earnings history (DESIGN/70 §1 row 5) --------------------------------------------------------

def earnings_event_rows(con, ticker: str) -> tuple[pd.DataFrame, str, str | None]:
    """`earnings_events` (the panel-built prints) for one ticker."""
    source = EARNINGS_EVENTS
    if not os.path.isdir(store.table_dir(EARNINGS_EVENTS)):
        return pd.DataFrame(), source, f"{EARNINGS_EVENTS} has never been built"
    df = store.read_table(con, EARNINGS_EVENTS, where="ticker = " + _sql_str(ticker))
    if df.empty:
        return df, source, f"no {EARNINGS_EVENTS} rows for {ticker}"
    return df.sort_values("E").reset_index(drop=True), f"{EARNINGS_EVENTS} <= {_max_iso(df, 'E')}", None


def earnings_history_rows(ticker: str) -> tuple[pd.DataFrame, str, str | None]:
    """`earnings_history/events.parquet` (ten years of Yahoo-measured moves) for one ticker."""
    path = earnings_history.EVENTS_PATH
    source = "earnings_history/events.parquet"
    if not os.path.exists(path):
        return pd.DataFrame(), source, "earnings_history/events.parquet has never been built"
    df = pd.read_parquet(path)
    hit = df[df["ticker"] == ticker].sort_values("E").reset_index(drop=True) if "ticker" in df.columns else pd.DataFrame()
    if hit.empty:
        return hit, source, f"no earnings_history rows for {ticker}"
    return hit, f"{source} <= {_max_iso(hit, 'E')}", None


def _sql_str(value: str) -> str:
    return "'" + str(value).replace("'", "''") + "'"


def _max_iso(df: pd.DataFrame, column: str) -> str:
    return pd.to_datetime(df[column]).max().date().isoformat()


# --- The live chain (DESIGN/70 §1 row 6): stored partition, else a fetch, else yfinance ----------

def _meta(source: str | None, d: date | None, reason: str | None, rows: int) -> dict:
    return {"source": source, "date": None if d is None else d.isoformat(), "reason": reason, "rows": rows}


def resolve_chain(ticker: str, d: date, *, online: bool = True,
                  fetch=cboe_chain.fetch_chain, yf_chain=src.yf_option_chain,
                  now=lambda: datetime.now(timezone.utc)) -> tuple[pd.DataFrame | None, dict]:
    """The chain for `(ticker, d)` and the `chain_meta` that says where it came from.

    Order: the stored `cboe_chain` partition (a mart read, so it works offline); else, when online,
    one CBOE fetch, stored only when the payload's own as-of date IS `d` (a weekend snapshot of a
    later session must never be filed under `d`); else the yfinance fallback normalised onto the
    same columns with `source = "yfinance"`; else `None` with the reason.
    """
    if cboe_chain.has_chain(ticker, d):
        df = cboe_chain.load_chain(ticker, d)
        return df, _meta("cboe_chain", d, None, len(df))
    if not online:
        return None, _meta(None, None, f"offline and no stored cboe_chain partition for {ticker} {d.isoformat()}", 0)
    try:
        payload = fetch(ticker)
        asof = cboe_chain.chain_asof_date(payload)
        if asof == d:
            df = cboe_chain.parse_chain(payload, now())
            if not df.empty:
                cboe_chain.store_chain(df, ticker, d)
                return df, _meta("cboe_chain", d, None, len(df))
            cboe_reason = "cboe chain parsed empty"
        else:
            cboe_reason = f"cboe chain as-of {asof} is not {d.isoformat()}"
    except Exception as exc:
        cboe_reason = f"cboe fetch failed: {str(exc)[:160]}"
    fallback = yf_chain(ticker, d)
    if fallback["available"]:
        df = fallback["value"]
        note = f"{cboe_reason}; yfinance fallback (first {src.YF_FALLBACK_EXPIRIES} expiries)"
        return df, _meta("yfinance", d, note, len(df))
    return None, _meta(None, None, f"{cboe_reason}; {fallback['reason']}", 0)


# --- Flags (DESIGN/70 §1 rows 7 and 9) ------------------------------------------------------------

def borrow_row(ticker: str, d: date, max_stale_days: int) -> tuple[dict | None, str, str | None]:
    """IBKR borrow for the name with its fee decile over that snapshot's whole universe (X2)."""
    snap = borrow_mart.load_borrow_asof(d, max_stale_days)
    source = f"borrow (IBKR) {snap.get('asof') or 'none'}"
    if not snap.get("available"):
        return None, source, snap.get("reason") or "no borrow snapshot"
    data = snap["data"]
    hit = data[data["symbol"] == ticker]
    if hit.empty:
        return None, source, f"{ticker} absent from the IBKR borrow file of {snap['asof']}"
    row = hit.iloc[0]
    decile = data["fee_rate"].rank(pct=True).loc[hit.index[0]]
    return {"fee_rate": _num(row.get("fee_rate")), "rebate_rate": _num(row.get("rebate_rate")),
            "available_shares": _num(row.get("available_shares")),
            "asof": snap["asof"].isoformat(), "stale_days": int(snap["stale_days"]),
            "decile": _num(decile)}, source, None


def short_interest_row(ticker: str, d: date, short_float_res: dict) -> tuple[dict | None, str, str | None]:
    """FINRA short interest (point-in-time by publication date) plus the short float and its source."""
    si = short_interest.load_short_interest(d)
    hit = si[si["symbol"] == ticker] if not si.empty else si
    sf = (short_float_res or {}).get("value") or {}
    if hit.empty:
        source = f"short_interest (FINRA) <= {d.isoformat()}"
        if sf.get("short_float") is None:
            return None, source, f"no FINRA short-interest row visible for {ticker} by {d.isoformat()}"
        return ({"current_short_position": None, "days_to_cover": None, "settlement_date": None,
                 "publication_date": None, **sf},
                f"{sf.get('short_float_source')}", f"no FINRA row for {ticker}; short float only")
    row = hit.iloc[0]
    settlement = row["settlement_date"]
    return ({"current_short_position": _num(row.get("current_short_position")),
             "days_to_cover": _num(row.get("days_to_cover")),
             "settlement_date": settlement.isoformat(),
             "publication_date": short_interest.publication_date(settlement).isoformat(),
             "short_float": sf.get("short_float"), "short_float_source": sf.get("short_float_source")},
            f"short_interest (FINRA) settlement {settlement.isoformat()}", None)


def index_vol_row(d: date) -> tuple[dict | None, str, str | None]:
    """The last `index_vol` row on or before `d` (VIX, VIX3M, VXN, VIX9D)."""
    df = index_vol.load_index_vol()
    source = f"index_vol <= {d.isoformat()}"
    if df.empty:
        return None, source, "index_vol has never been built"
    rows = df[pd.to_datetime(df["date"]).dt.date <= d]
    if rows.empty:
        return None, source, f"no index_vol row on or before {d.isoformat()}"
    row = rows.sort_values("date").iloc[-1]
    asof = pd.to_datetime(row["date"]).date()
    return ({"date": asof.isoformat(), "vix": _num(row.get("vix")), "vix3m": _num(row.get("vix3m")),
             "vxn": _num(row.get("vxn")), "vix9d": _num(row.get("vix9d"))},
            f"index_vol {asof.isoformat()}", None)


def regime_row(d: date, con=None) -> tuple[dict | None, str, str | None]:
    """`scripts/_regime.classify_regime` -- the same label every other strategy is conditioned on."""
    source = f"_regime.classify_regime {d.isoformat()}"
    try:
        import sys
        if config.SCRIPTS not in sys.path:
            sys.path.insert(0, config.SCRIPTS)
        from _regime import classify_regime
        out = classify_regime(d.isoformat(), con)
    except Exception as exc:
        return None, source, f"regime unavailable: {str(exc)[:160]}"
    return out, f"_regime.classify_regime asof {out.get('asof')}", None


def _num(value) -> float | None:
    try:
        out = float(value)
    except (TypeError, ValueError):
        return None
    return None if pd.isna(out) else out
