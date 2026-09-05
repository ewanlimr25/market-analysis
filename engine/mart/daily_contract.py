"""`daily_contract`: one row per (option_chain_id, date) for every contract that printed in the
session (DESIGN/70 §1.1). Built from the day's All Options file with a Hot Chains left join.

Determinism (DESIGN/70 §7.3, bit-for-bit across thread counts): every size-weighted sum is an
exact integer sum over scaled BIGINT prices (`config.PRICE_SCALE`, `config.IV_SCALE`, cents for
premium), divided once at the end, and "last print" is chosen by `arg_max` over a struct key that
totally orders prints (timestamp, then every payload field), so tied keys carry identical payloads.

Windows (ET, from `config`): the session is [SESSION_START, SESSION_END_EXCL); `late` is
>= LATE_START; `early` is <= EARLY_END. Prints kept: not canceled, size > 0, price > 0.
Spread statistics use only prints with `nbbo_bid > 0 AND nbbo_ask >= nbbo_bid`.

CLI: `python3 -m engine.mart.daily_contract --date 2026-07-29 | --rebuild [--force]`.
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys
import time
from dataclasses import dataclass
from datetime import date

import duckdb
import pandas as pd

from engine import calendar as cal
from engine import config
from engine.mart import store

TABLE = "daily_contract"
PREMIUM_SCALE = 100                     # dollars -> cents: premium sums are exact in cents
REL_SPREAD_SCALE = config.IV_SCALE      # dimensionless (ask-bid)/mid on the same 1e-6 grid as IV
VALID_NBBO = "nbbo_bid > 0 AND nbbo_ask >= nbbo_bid"
_DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")

COLUMNS: tuple[str, ...] = (
    "option_chain_id", "underlying_symbol", "option_type", "strike", "expiry", "date",
    "dte", "dte_cal", "n_prints", "size_total", "premium_total",
    "vwap_all", "vwap_late", "size_late", "vwap_early", "size_early",
    "last_price", "last_nbbo_bid", "last_nbbo_ask", "last_ts",
    "late_nbbo_mid", "late_rel_spread", "early_nbbo_mid", "early_rel_spread",
    "late_last_bid", "late_last_ask", "early_last_bid", "early_last_ask",
    "iv_vwap", "delta_last", "gamma_last", "vega_last",
    "open_interest", "underlying_last", "hc_close", "hc_iv", "hc_volume",
)


# ----------------------------------------------------------------------------- SQL assembly


def _quote(path: str) -> str:
    """Single-quote a file path for interpolation into SQL."""
    return "'" + path.replace("'", "''") + "'"


def _weighted(numerator: str, scale: int, where: str | None = None) -> str:
    """Size-weighted mean of a scaled-integer column as one exact integer ratio (null if empty)."""
    flt = f" FILTER (WHERE {where})" if where else ""
    return (f"(sum(({numerator}) * size){flt})::DOUBLE"
            f" / nullif({scale} * (sum(size){flt}), 0)::DOUBLE")


def _hot_chains_sql(hot_chains_path: str | None) -> str:
    """Hot Chains keyed by option_symbol (max() guards against a duplicated symbol), or empty."""
    if hot_chains_path is None:
        return ("SELECT NULL::VARCHAR AS option_symbol, NULL::DOUBLE AS close, "
                "NULL::DOUBLE AS iv, NULL::BIGINT AS volume WHERE false")
    return (f"SELECT option_symbol, max(close) AS close, max(iv) AS iv, max(volume) AS volume "
            f"FROM read_parquet({_quote(hot_chains_path)}) GROUP BY option_symbol")


_PRINTS_SQL = """
WITH prints AS (
  SELECT option_chain_id, underlying_symbol, option_type, strike, expiry, price, size,
         nbbo_bid, nbbo_ask, open_interest, underlying_price, gamma, vega,
         (executed_at AT TIME ZONE '{tz}')::TIMESTAMP           AS et,
         greatest(-1.0, least(1.0, delta))                     AS delta,
         round(price * {price_scale})::BIGINT                   AS price_s,
         round(nbbo_bid * {price_scale})::BIGINT                AS bid_s,
         round(nbbo_ask * {price_scale})::BIGINT                AS ask_s,
         round(premium * {premium_scale})::BIGINT               AS premium_c,
         CASE WHEN isfinite(implied_volatility)
              THEN round(implied_volatility * {iv_scale})::BIGINT END AS iv_s,
         ({valid_nbbo})                                        AS valid_nbbo
  FROM read_parquet({all_options})
  WHERE NOT canceled AND size > 0 AND price > 0
), session AS (
  SELECT *,
         et::TIME >= TIME '{late_start}'                       AS is_late,
         et::TIME <= TIME '{early_end}'                        AS is_early,
         CASE WHEN valid_nbbo
              THEN round(2.0 * (ask_s - bid_s) / (ask_s + bid_s) * {rel_scale})::BIGINT END AS rel_s,
         row(et, price, size, nbbo_bid, nbbo_ask, delta, gamma, vega, underlying_price) AS print_key
  FROM prints
  WHERE et::TIME >= TIME '{session_start}' AND et::TIME < TIME '{session_end}'
)"""

_AGGREGATE_SQL = """, agg AS (
  SELECT option_chain_id,
         max(underlying_symbol) AS underlying_symbol, max(option_type) AS option_type,
         max(strike) AS strike, max(expiry) AS expiry,
         count(*)                                              AS n_prints,
         sum(size)::BIGINT                                     AS size_total,
         sum(premium_c)::DOUBLE / {premium_scale}              AS premium_total,
         {vwap_all}                                            AS vwap_all,
         {vwap_late}                                           AS vwap_late,
         coalesce(sum(size) FILTER (WHERE is_late), 0)::BIGINT  AS size_late,
         {vwap_early}                                          AS vwap_early,
         coalesce(sum(size) FILTER (WHERE is_early), 0)::BIGINT AS size_early,
         arg_max(struct_pack(price := price, bid := nbbo_bid, ask := nbbo_ask, ts := et,
                             delta := delta, gamma := gamma, vega := vega,
                             underlying := underlying_price), print_key) AS last_print,
         {late_nbbo_mid}                                       AS late_nbbo_mid,
         {late_rel_spread}                                     AS late_rel_spread,
         {early_nbbo_mid}                                      AS early_nbbo_mid,
         {early_rel_spread}                                    AS early_rel_spread,
         arg_max(struct_pack(bid := nbbo_bid, ask := nbbo_ask), print_key)
             FILTER (WHERE is_late AND valid_nbbo)             AS late_last,
         arg_max(struct_pack(bid := nbbo_bid, ask := nbbo_ask), print_key)
             FILTER (WHERE is_early AND valid_nbbo)            AS early_last,
         {iv_vwap}                                             AS iv_vwap,
         max(open_interest)                                    AS open_interest
  FROM session GROUP BY option_chain_id
), hot AS ({hot_chains})
SELECT a.option_chain_id, a.underlying_symbol, a.option_type, a.strike, a.expiry,
       DATE '{d}' AS date,
       a.n_prints, a.size_total, a.premium_total,
       a.vwap_all, a.vwap_late, a.size_late, a.vwap_early, a.size_early,
       a.last_print.price AS last_price, a.last_print.bid AS last_nbbo_bid,
       a.last_print.ask AS last_nbbo_ask, a.last_print.ts AS last_ts,
       a.late_nbbo_mid, a.late_rel_spread, a.early_nbbo_mid, a.early_rel_spread,
       a.late_last.bid AS late_last_bid, a.late_last.ask AS late_last_ask,
       a.early_last.bid AS early_last_bid, a.early_last.ask AS early_last_ask,
       a.iv_vwap, a.last_print.delta AS delta_last, a.last_print.gamma AS gamma_last,
       a.last_print.vega AS vega_last, a.open_interest,
       a.last_print.underlying AS underlying_last,
       h.close AS hc_close, h.iv AS hc_iv, h.volume AS hc_volume
FROM agg a LEFT JOIN hot h ON h.option_symbol = a.option_chain_id
ORDER BY a.option_chain_id
"""


def _day_sql(all_options_path: str, hot_chains_path: str | None, d: date) -> str:
    late_valid, early_valid = "is_late AND valid_nbbo", "is_early AND valid_nbbo"
    return (_PRINTS_SQL + _AGGREGATE_SQL).format(
        tz=config.ET_TZ, all_options=_quote(all_options_path), d=d.isoformat(),
        price_scale=config.PRICE_SCALE, iv_scale=config.IV_SCALE,
        premium_scale=PREMIUM_SCALE, rel_scale=REL_SPREAD_SCALE, valid_nbbo=VALID_NBBO,
        session_start=config.SESSION_START, session_end=config.SESSION_END_EXCL,
        late_start=config.LATE_START, early_end=config.EARLY_END,
        vwap_all=_weighted("price_s", config.PRICE_SCALE),
        vwap_late=_weighted("price_s", config.PRICE_SCALE, "is_late"),
        vwap_early=_weighted("price_s", config.PRICE_SCALE, "is_early"),
        late_nbbo_mid=_weighted("bid_s + ask_s", 2 * config.PRICE_SCALE, late_valid),
        late_rel_spread=_weighted("rel_s", REL_SPREAD_SCALE, late_valid),
        early_nbbo_mid=_weighted("bid_s + ask_s", 2 * config.PRICE_SCALE, early_valid),
        early_rel_spread=_weighted("rel_s", REL_SPREAD_SCALE, early_valid),
        iv_vwap=_weighted("iv_s", config.IV_SCALE, "iv_s IS NOT NULL"),
        hot_chains=_hot_chains_sql(hot_chains_path),
    )


# ----------------------------------------------------------------------------- aggregation


def _with_dte(df: pd.DataFrame, d: date) -> pd.DataFrame:
    """Add `dte` (NYSE trading days, engine.calendar) and `dte_cal` per distinct expiry."""
    expiries = df["expiry"].drop_duplicates()
    if expiries.isna().any():
        n_null = int(df["expiry"].isna().sum())
        raise ValueError(f"{d}: {n_null} contract rows carry a null expiry; refusing to build")
    dte = {e: cal.trading_days_between(d, e.date()) for e in expiries}
    dte_cal = {e: cal.calendar_days_between(d, e.date()) for e in expiries}
    return df.assign(dte=df["expiry"].map(dte).astype("int32"),
                     dte_cal=df["expiry"].map(dte_cal).astype("int32"))


def aggregate_day(con: duckdb.DuckDBPyConnection, all_options_path: str,
                  hot_chains_path: str | None, d: date | str) -> pd.DataFrame:
    """Aggregate one day's All Options prints (plus optional Hot Chains) into `COLUMNS`.

    Pure with respect to the file system: reads the given paths, writes nothing. One row per
    option_chain_id that printed inside the session window, sorted by option_chain_id.
    """
    d = cal.parse_date(d)
    if not os.path.exists(all_options_path):
        raise FileNotFoundError(f"All Options file not found: {all_options_path}")
    if hot_chains_path is not None and not os.path.exists(hot_chains_path):
        raise FileNotFoundError(f"Hot Chains file not found: {hot_chains_path}")
    raw = con.execute(_day_sql(all_options_path, hot_chains_path, d)).df()
    return _with_dte(raw, d)[list(COLUMNS)]


# ----------------------------------------------------------------------------- partitions


def all_options_path(d: date) -> str:
    return os.path.join(config.STOCKS, config.ALL_OPTIONS_FILE.format(d=d.isoformat()))


def hot_chains_path(d: date) -> str | None:
    """The day's Hot Chains file, or None when the vendor did not deliver one."""
    path = os.path.join(config.STOCKS, config.HOT_CHAINS_FILE.format(d=d.isoformat()))
    return path if os.path.exists(path) else None


def build_day(d: date | str, con: duckdb.DuckDBPyConnection | None = None,
              force: bool = False) -> pd.DataFrame:
    """Build (or reuse) the `daily_contract` partition for d and return it as stored on disk."""
    d = cal.parse_date(d)
    if not force and store.has_partition(TABLE, d):
        return store.read_partition(TABLE, d)
    ao = all_options_path(d)
    if not os.path.exists(ao):
        raise FileNotFoundError(f"No All Options file for {d.isoformat()}: {ao}")
    df = aggregate_day(con or duckdb.connect(), ao, hot_chains_path(d), d)
    store.write_partition(df, TABLE, d)
    return store.read_partition(TABLE, d)


def panel_dates() -> list[date]:
    """Every day with an All Options file, ascending."""
    pattern = os.path.join(config.STOCKS, config.ALL_OPTIONS_FILE.format(d="*"))
    matches = (_DATE_RE.search(os.path.basename(p)) for p in glob.glob(pattern))
    return sorted(date.fromisoformat(m.group(1)) for m in matches if m)


@dataclass(frozen=True)
class DayResult:
    date: date
    rows: int | None
    seconds: float
    error: str | None = None


def _build_timed(d: date, con: duckdb.DuckDBPyConnection, force: bool) -> DayResult:
    cached = not force and store.has_partition(TABLE, d)
    t0 = time.perf_counter()
    try:
        rows = len(build_day(d, con=con, force=force))
    except Exception as exc:  # noqa: BLE001 - one bad day must not abort the panel rebuild
        result = DayResult(d, None, time.perf_counter() - t0, f"{type(exc).__name__}: {exc}")
        print(f"{d} FAILED {result.error}", flush=True)
        return result
    result = DayResult(d, rows, time.perf_counter() - t0)
    note = " (existing partition)" if cached else ""
    print(f"{d} {rows:>8,} rows {result.seconds:6.1f}s{note}", flush=True)
    return result


def rebuild(force: bool = False, dates: list[date] | None = None) -> list[DayResult]:
    """Build every panel day (or `dates`) with per-day timing; failures are collected, not raised."""
    con = duckdb.connect()
    days = panel_dates() if dates is None else list(dates)
    results = [_build_timed(d, con, force) for d in days]
    built = [r for r in results if r.error is None]
    failed = [r for r in results if r.error is not None]
    total = sum(r.rows or 0 for r in built)
    print(f"daily_contract: {len(built)} days, {total:,} rows, {len(failed)} failed, "
          f"{sum(r.seconds for r in results):.0f}s", flush=True)
    return results


# ----------------------------------------------------------------------------- CLI


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the daily_contract mart table.")
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--date", type=cal.parse_date, help="build one day (YYYY-MM-DD)")
    target.add_argument("--rebuild", action="store_true", help="build every panel day")
    parser.add_argument("--force", action="store_true", help="overwrite existing partitions")
    args = parser.parse_args(argv)
    if args.rebuild:
        results = rebuild(force=args.force)
        return 1 if any(r.error for r in results) else 0
    try:
        df = build_day(args.date, force=args.force)
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"{args.date} {len(df):,} rows -> {store.partition_path(TABLE, args.date)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
