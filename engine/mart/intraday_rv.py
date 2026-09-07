"""`intraday_rv`: one row per (underlying, day), a realized-vol bundle built from the 5-minute
underlying-price path reconstructed from All Options prints (G7, `findings/RESEARCH/47-edge-gaps.md`
§2 G7; `findings/RESEARCH/20-data-inventory.md` §7.3).

Why this exists: S-C's variance premium and S-A's conditioning both use close-to-close realized
vol (`RESEARCH/40 E2`'s RV21). The literature the repo leans on (Duarte, Jones & Wang 2024,
`RESEARCH/30 §2`) defines the premium on *intraday* realized variance, which close-to-close never
sees (a name that chops all day and closes flat looks like zero realized vol to a close-to-close
measure). This table is a measurement change only: it does not touch any frozen parameter and S-C
is not built, so nothing downstream consumes it without a spec edit (see the module's `results.md`
companion for the exact `DESIGN/90` lines that would change).

Per (underlying, day):
  - `n_obs`      : print count with a valid `underlying_price` inside the session window.
  - `n_buckets`  : populated 5-minute buckets (of at most 79, `09:30` to `16:01` ET exclusive).
  - `max_gap_minutes` : the largest gap between two consecutive POPULATED buckets; interior gaps
    only, same philosophy as `scripts/chart.py`'s `_interior_holes` (a name that simply stops
    printing for the rest of the day is a coverage fact, not a "gap" in the sampled path).
  - `rv5`        : realized variance from 5-minute log returns, sum((ln(C_i / C_{i-1}))^2) over
    consecutive populated buckets. Not annualized -- annualizing a single day alone is not
    meaningful; the 20-session comparison (`results.md` companion) sums `rv5` over the window and
    annualizes once.
  - `parkinson`  : the realized-range estimator, sum((ln(H_i / L_i))^2 / (4 ln 2)) over every
    populated bucket -- the Parkinson (1980) formula applied per sub-interval and summed, which is
    the standard way to turn an OHLC estimator into an intraday one (Martens & van Dijk 2007).
  - `gk`         : likewise for Garman-Klass (1980): sum(0.5*(ln(H_i/L_i))^2
    - (2 ln 2 - 1)*(ln(C_i/O_i))^2) per bucket. Every bucket built by `fetch_buckets` is
    self-consistent (O and C are prices drawn from the same bucket as its own L/H), which makes
    each term provably >= 0 (|ln(C/O)| <= ln(H/L), and 0.5 > 2 ln 2 - 1); the per-bucket floor at
    0 is defensive against malformed input only (`_gk_bucket`'s tests cover both).
  - `open_to_close_ret` : ln(close of the last populated bucket / open of the first), this day's
    own intraday reconstruction only -- no cross-day dependency, so days build independently.
  - `close_to_close_ret`: ln(official close[d] / official close[prev session]), both read from
    `data/prices.parquet` -- deliberately NOT the intraday reconstruction, so this column is
    directly comparable to `RESEARCH/40 E2`'s RV21 (built the same way) and so a day's build needs
    no partition from any other day.
  - `quality`    : `n_obs >= QUALITY_MIN_OBS` and `n_buckets >= 2` and
    `max_gap_minutes <= QUALITY_MAX_GAP_MINUTES`.

Determinism: the bucket query is grouped (order-independent) and fetched `ORDER BY
underlying_symbol, bucket`; every day-level statistic is then a sequential sum in that fixed,
total order (numpy, single-threaded), so a rebuild is bit-for-bit regardless of DuckDB's thread
count. No BIGINT scaling is applied (unlike `daily_contract`'s weighted sums): the sums here are
already computed from a materialized, deterministically-ordered pandas frame rather than inside a
parallel SQL aggregate, so the ambiguity that scaling defends against does not arise.

CLI: `python3 -m engine.mart.intraday_rv --date 2026-07-29 | --rebuild [--days N] [--force]`.
"""
from __future__ import annotations

import argparse
import glob
import math
import os
import sys
import time
from dataclasses import dataclass
from datetime import date

import duckdb
import numpy as np
import pandas as pd

from engine import calendar as cal
from engine import config
from engine.mart import store
from engine.mart.daily_contract import all_options_path, panel_dates

TABLE = "intraday_rv"
BUCKET_MINUTES = 5
QUALITY_MIN_OBS = 100
QUALITY_MAX_GAP_MINUTES = 30
LN2 = math.log(2.0)
PARKINSON_SCALE = 1.0 / (4.0 * LN2)
GK_DRIFT_TERM = 2.0 * LN2 - 1.0

COLUMNS: tuple[str, ...] = (
    "underlying_symbol", "date", "n_obs", "n_buckets", "max_gap_minutes",
    "open_px", "close_px", "high_px", "low_px",
    "rv5", "parkinson", "gk",
    "open_to_close_ret", "close_to_close_ret",
    "prices_close", "prices_close_prev", "quality",
)
FLOAT_COLUMNS = ("open_px", "close_px", "high_px", "low_px", "rv5", "parkinson", "gk",
                  "open_to_close_ret", "close_to_close_ret", "prices_close", "prices_close_prev")


def _quote(path: str) -> str:
    return "'" + path.replace("'", "''") + "'"


_BUCKET_SQL = """
WITH prints AS (
  SELECT underlying_symbol, underlying_price AS px,
         (executed_at AT TIME ZONE '{tz}')::TIMESTAMP AS et
  FROM read_parquet({all_options})
  WHERE NOT canceled AND size > 0 AND price > 0 AND underlying_price > 0
    AND (executed_at AT TIME ZONE '{tz}')::TIME >= TIME '{session_start}'
    AND (executed_at AT TIME ZONE '{tz}')::TIME <  TIME '{session_end}'
), bucketed AS (
  SELECT underlying_symbol, et, px,
         time_bucket(INTERVAL '{bucket_min} minutes', et,
                     TIMESTAMP '{d} {session_start}') AS bucket
  FROM prints
)
SELECT underlying_symbol, bucket,
       count(*)::BIGINT AS n, min(px) AS lo, max(px) AS hi,
       arg_min(px, et) AS o, arg_max(px, et) AS c
FROM bucketed
GROUP BY underlying_symbol, bucket
ORDER BY underlying_symbol, bucket
"""


def _bucket_sql(all_options_path_: str, d: date) -> str:
    return _BUCKET_SQL.format(
        tz=config.ET_TZ, all_options=_quote(all_options_path_), d=d.isoformat(),
        bucket_min=BUCKET_MINUTES, session_start=config.SESSION_START,
        session_end=config.SESSION_END_EXCL)


def fetch_buckets(con: duckdb.DuckDBPyConnection, all_options_path_: str, d: date) -> pd.DataFrame:
    """5-minute (underlying, bucket) OHLC rows for the session, ordered deterministically."""
    return con.execute(_bucket_sql(all_options_path_, d)).df()


# ----------------------------------------------------------------------------- pure day-level math


def _gk_bucket(o: float, h: float, l: float, c: float) -> float:
    """One bucket's Garman-Klass contribution, floored at 0 (see module docstring)."""
    if h <= 0 or l <= 0 or o <= 0 or c <= 0:
        return 0.0
    term = 0.5 * math.log(h / l) ** 2 - GK_DRIFT_TERM * math.log(c / o) ** 2
    return max(term, 0.0)


def _one_underlying(g: pd.DataFrame) -> dict:
    """Day-level stats for one underlying's populated buckets (already time-sorted)."""
    closes = g["c"].to_numpy(dtype="float64")
    opens = g["o"].to_numpy(dtype="float64")
    highs = g["hi"].to_numpy(dtype="float64")
    lows = g["lo"].to_numpy(dtype="float64")
    ns = g["n"].to_numpy(dtype="int64")
    buckets = g["bucket"].tolist()

    n_obs = int(ns.sum())
    n_buckets = len(g)
    if n_buckets >= 2:
        gaps_min = [(buckets[i + 1] - buckets[i]).total_seconds() / 60.0
                    for i in range(n_buckets - 1)]
        max_gap_minutes = float(max(gaps_min))
        rv5 = float(np.sum(np.log(closes[1:] / closes[:-1]) ** 2))
    else:
        max_gap_minutes = float("nan")
        rv5 = 0.0 if n_buckets == 1 else float("nan")

    parkinson = float(sum(PARKINSON_SCALE * math.log(h / l) ** 2
                          for h, l in zip(highs, lows) if h > 0 and l > 0))
    gk = float(sum(_gk_bucket(o, h, l, c) for o, h, l, c in zip(opens, highs, lows, closes)))

    open_px = float(opens[0]) if n_buckets else float("nan")
    close_px = float(closes[-1]) if n_buckets else float("nan")
    high_px = float(highs.max()) if n_buckets else float("nan")
    low_px = float(lows.min()) if n_buckets else float("nan")
    open_to_close_ret = (math.log(close_px / open_px)
                         if n_buckets and open_px > 0 and close_px > 0 else float("nan"))

    quality = bool(n_obs >= QUALITY_MIN_OBS and n_buckets >= 2
                   and max_gap_minutes <= QUALITY_MAX_GAP_MINUTES)

    return {"n_obs": n_obs, "n_buckets": n_buckets, "max_gap_minutes": max_gap_minutes,
            "open_px": open_px, "close_px": close_px, "high_px": high_px, "low_px": low_px,
            "rv5": rv5, "parkinson": parkinson, "gk": gk,
            "open_to_close_ret": open_to_close_ret, "quality": quality}


def day_level(buckets: pd.DataFrame) -> pd.DataFrame:
    """`fetch_buckets`'s output -> one row per underlying_symbol (pure, no I/O).

    `buckets` must already be sorted by (underlying_symbol, bucket); `fetch_buckets` guarantees
    this. Underlyings with zero populated buckets never appear (there is nothing to group).
    """
    _DAY_LEVEL_FIELDS = ("n_obs", "n_buckets", "max_gap_minutes", "open_px", "close_px",
                        "high_px", "low_px", "rv5", "parkinson", "gk", "open_to_close_ret",
                        "quality")
    if buckets.empty:
        return pd.DataFrame({"underlying_symbol": pd.Series([], dtype=object),
                             **{k: pd.Series([], dtype="float64") for k in _DAY_LEVEL_FIELDS}})
    rows = []
    for sym, g in buckets.groupby("underlying_symbol", sort=False):
        rows.append({"underlying_symbol": sym, **_one_underlying(g)})
    return pd.DataFrame(rows).sort_values("underlying_symbol").reset_index(drop=True)


# ----------------------------------------------------------------------------- close-to-close join


def _official_closes(con: duckdb.DuckDBPyConnection, prices_path: str, syms: set[str],
                     d: date, d_prev: date) -> dict[str, tuple[float | None, float | None]]:
    """{ticker: (close[d], close[d_prev])} from `prices.parquet`; missing rows -> None."""
    if not syms:
        return {}
    df = con.execute(
        f"SELECT ticker, date, close FROM read_parquet({_quote(prices_path)}) "
        f"WHERE date IN (DATE '{d.isoformat()}', DATE '{d_prev.isoformat()}')").df()
    if df.empty:
        return {}
    df = df.assign(date=pd.to_datetime(df["date"]).dt.date)
    out: dict[str, tuple[float | None, float | None]] = {}
    for tk, g in df[df.ticker.isin(syms)].groupby("ticker"):
        by_date = dict(zip(g["date"], g["close"]))
        out[tk] = (by_date.get(d), by_date.get(d_prev))
    return out


def with_close_to_close(df: pd.DataFrame, con: duckdb.DuckDBPyConnection, prices_path: str,
                        d: date) -> pd.DataFrame:
    """Add `prices_close`, `prices_close_prev`, `close_to_close_ret` from `data/prices.parquet`."""
    if df.empty:
        return df.assign(prices_close=pd.Series(dtype="float64"),
                         prices_close_prev=pd.Series(dtype="float64"),
                         close_to_close_ret=pd.Series(dtype="float64"))
    d_prev = cal.prev_session(d)
    closes = _official_closes(con, prices_path, set(df.underlying_symbol), d, d_prev)
    pc = df.underlying_symbol.map(lambda s: closes.get(s, (None, None))[0])
    pp = df.underlying_symbol.map(lambda s: closes.get(s, (None, None))[1])
    c2c = [math.log(a / b) if (a is not None and b is not None and a > 0 and b > 0) else float("nan")
           for a, b in zip(pc, pp)]
    return df.assign(prices_close=pd.to_numeric(pc, errors="coerce").astype("float64"),
                     prices_close_prev=pd.to_numeric(pp, errors="coerce").astype("float64"),
                     close_to_close_ret=pd.Series(c2c, index=df.index, dtype="float64"))


# ----------------------------------------------------------------------------- public API


def aggregate_day(con: duckdb.DuckDBPyConnection, all_options_path_: str, prices_path: str,
                  d: date | str) -> pd.DataFrame:
    """One row per underlying that printed in the session on `d`; pure w.r.t. the file system."""
    d = cal.parse_date(d)
    buckets = fetch_buckets(con, all_options_path_, d)
    out = day_level(buckets)
    out = with_close_to_close(out, con, prices_path, d)
    out = out.assign(date=d)
    out = out.astype({c: "float64" for c in FLOAT_COLUMNS})
    return out[list(COLUMNS)]


def build_day(d: date | str, con: duckdb.DuckDBPyConnection | None = None,
             force: bool = False) -> pd.DataFrame:
    d = cal.parse_date(d)
    if not force and store.has_partition(TABLE, d):
        return store.read_partition(TABLE, d)
    ao = all_options_path(d)
    if not os.path.exists(ao):
        raise FileNotFoundError(f"No All Options file for {d.isoformat()}: {ao}")
    df = aggregate_day(con or duckdb.connect(), ao, config.PRICES, d)
    store.write_partition(df, TABLE, d)
    return store.read_partition(TABLE, d)


@dataclass(frozen=True)
class DayResult:
    date: date
    rows: int | None
    quality_rows: int | None
    screener_names: int | None
    seconds: float
    error: str | None = None


def _screener_universe(con: duckdb.DuckDBPyConnection, d: date) -> int | None:
    """Count of common-stock/ADR tickers in that day's screener export, or None if absent."""
    pattern = os.path.join(config.STOCKS, config.SCREENER_FILE.format(d=d.isoformat()))
    if not os.path.exists(pattern):
        matches = glob.glob(os.path.join(config.STOCKS, config.SCREENER_GLOB))
        candidates = [m for m in matches if d.isoformat() in m]
        if not candidates:
            return None
        pattern = candidates[0]
    types = ", ".join(f"'{t}'" for t in config.ISSUE_TYPES)
    return int(con.execute(
        f"SELECT count(distinct ticker) FROM read_parquet({_quote(pattern)}) "
        f"WHERE issue_type IN ({types})").fetchone()[0])


def _build_timed(d: date, con: duckdb.DuckDBPyConnection, force: bool) -> DayResult:
    cached = not force and store.has_partition(TABLE, d)
    t0 = time.perf_counter()
    try:
        df = build_day(d, con=con, force=force)
        screener_n = _screener_universe(con, d)
    except Exception as exc:  # noqa: BLE001 - one bad day must not abort the panel rebuild
        result = DayResult(d, None, None, None, time.perf_counter() - t0, f"{type(exc).__name__}: {exc}")
        print(f"{d} FAILED {result.error}", flush=True)
        return result
    q = int(df["quality"].sum()) if "quality" in df else 0
    result = DayResult(d, len(df), q, screener_n, time.perf_counter() - t0)
    note = " (existing partition)" if cached else ""
    cov = f"{100 * q / screener_n:5.1f}%" if screener_n else "  n/a"
    print(f"{d} {len(df):>6,} rows  quality {q:>6,}  screener_cov {cov}  {result.seconds:6.1f}s{note}",
          flush=True)
    return result


def rebuild(force: bool = False, days: int | None = None) -> list[DayResult]:
    """Build every panel day (or the most recent `days`), one day at a time."""
    con = duckdb.connect()
    dates = panel_dates()
    if days is not None:
        dates = dates[-days:]
    results = [_build_timed(d, con, force) for d in dates]
    built = [r for r in results if r.error is None]
    failed = [r for r in results if r.error is not None]
    total = sum(r.rows or 0 for r in built)
    total_q = sum(r.quality_rows or 0 for r in built)
    print(f"{TABLE}: {len(built)} days, {total:,} rows, {total_q:,} quality rows, "
          f"{len(failed)} failed, {sum(r.seconds for r in results):.0f}s", flush=True)
    return results


# ----------------------------------------------------------------------------- CLI


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=f"build the {TABLE} mart table")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--date", help="build the partition for D (YYYY-MM-DD)")
    g.add_argument("--rebuild", action="store_true", help="build every panel day (or --days N of them)")
    ap.add_argument("--days", type=int, default=None,
                    help="with --rebuild, limit to the most recent N panel days")
    ap.add_argument("--force", action="store_true", help="overwrite existing partitions")
    args = ap.parse_args(argv)
    t0 = time.time()
    if args.rebuild:
        results = rebuild(force=args.force, days=args.days)
        return 1 if any(r.error for r in results) else 0
    try:
        df = build_day(cal.parse_date(args.date), force=args.force)
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    q = int(df["quality"].sum()) if len(df) else 0
    print(f"{args.date} {len(df):,} rows, {q:,} quality -> "
          f"{store.partition_path(TABLE, cal.parse_date(args.date))} ({time.time() - t0:.1f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
