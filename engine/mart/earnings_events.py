"""`earnings_events` mart table (DESIGN/70 §1.2), promoted from `artifacts/vol/e1_earnings.py`.

One row per (ticker, print E), partitioned by the pre-print session `pre` (`date` == `pre`).
Event construction reproduces E1 exactly so the rebuilt table matches the recorded artifact
(`artifacts/vol/out/e1_events.parquet`: 3,260 events on 97 pre-dates):

  candidates : (ticker, E) where E appears as `next_earnings_date` on a screener row dated within
               14 calendar days up to E, on a name whose `issue_type` is in `config.ISSUE_TYPES`;
               `er_time` is the strict plurality of the non-null label over that window ('unknown'
               when never set or tied). E1 used DuckDB `mode()`, whose tie-break is not
               deterministic; the panel has two 5-5 ties between a label and the literal string
               'unknown' (THO 2026-06-03, AEHR 2026-07-14) and the recorded artifact resolved both
               as unlabelled, which is what the plurality rule reproduces. The screener spells
               "no label" three ways (NULL, 'unknown', 'unkown'); anything not in `LABELLED` is
               unlabelled, as in E1.
  timing     : postmarket -> pre = E, post = next session;  premarket -> pre = prev session, post = E;
               unlabelled -> inferred from WHERE the iv30d crush lands: a relative drop of
               >= 15% (`CRUSH = -0.15`) on E means premarket, on E+1 postmarket; otherwise
               `unresolved` with the 2-session window prev(E) -> next(E).
  filters    : E is a trading day with prev/next sessions in the calendar; the screener row at
               `pre` exists, still carries E as `next_earnings_date` and has a finite implied move;
               closes exist at `pre` and `post` and `close[pre] >= 5` (E1's floor; S-A's own $10
               floor F2 is applied by the strategy, not here).

Spec note: DESIGN/70 §1.2 paraphrases the crush as "iv30d falls >= 5 points"; E1 uses the
RELATIVE drop of >= 15% and §1.2's "unchanged from E1" clause governs, so that is what is built.
The inference is ported with E1's exact truthiness/NaN semantics (a null iv30d on E+1 blocks the
premarket branch, a zero iv30d disables the ratio) because the screener has null `iv30d` rows.

Calendar: E1 anchors on SPY's dates in `data/prices.parquet`; here the same span is taken from
`engine.calendar.trading_days` (verified identical by tests/test_engine_calendar.py) and extended
past the price edge so a nightly build can see `next_session(E)` before its bar exists.

Nightly builds (`build_day(d)` = events with `pre == d`): a row needs `close[post]`, and the
crush inference needs the screener's `iv30d` on E and E+1, so the partition for `pre == d` is
complete only once prices and the screener through `next_session(next_session(d))` are on disk.
Run `--date d` on that night (or later) or rerun it with `--force`; run early, unlabelled events
come out `unresolved` or are dropped and are re-resolved when the partition is rebuilt.
"""
from __future__ import annotations

import argparse
import shutil
import sys
import time
from dataclasses import dataclass
from datetime import date
from typing import Callable, NamedTuple

import duckdb
import numpy as np
import pandas as pd

from engine import calendar as cal
from engine import config
from engine.mart import store
from engine.mart.vix import load_vix

TABLE = "earnings_events"
CRUSH = -0.15                   # E1: relative iv30d drop that marks the post-print session
CANDIDATE_LOOKBACK_DAYS = 14    # E1: E seen as next_earnings_date within 14 calendar days up to E
RUNUP_LOOKBACK_SESSIONS = 5     # E1: imp_5d_ago / iv30d_5d_ago
PRICE_FLOOR = 5.0               # E1: close[pre] >= 5
ADV_WINDOW_SESSIONS = 20        # adv_usd_20d window, ending at and including pre
ADV_MIN_SESSIONS = 10           # fewer valid sessions than this -> fall back to adv_usd_30d
UNKNOWN_ER_TIME = "unknown"
LABELLED = ("postmarket", "premarket")
COLUMNS = ["ticker", "E", "er_time", "timing", "how", "pre", "post", "date",
           "spot_pre", "close_post", "realized_move", "gap_signed", "implied_move_perc", "proxy_pnl",
           "iv30d_pre", "iv30d_post", "iv_rank_pre", "imp_5d_ago", "iv30d_5d_ago",
           "marketcap", "sector", "issue_type", "adv_usd_30d", "adv_usd_20d",
           "regime_pre", "vix_pre", "month", "season"]
FLOAT_COLUMNS = ("spot_pre", "close_post", "realized_move", "gap_signed", "implied_move_perc", "proxy_pnl",
                 "iv30d_pre", "iv30d_post", "iv_rank_pre", "imp_5d_ago", "iv30d_5d_ago",
                 "marketcap", "adv_usd_30d", "adv_usd_20d", "vix_pre")
_SCR_TABLE, _CAL_VIEW, _KEYS_VIEW = "_ee_scr", "_ee_cal", "_ee_keys"

RegimeFn = Callable[[date], "str | None"]
VixFn = Callable[[date], "float | None"]


class ScrRow(NamedTuple):
    """One screener (ticker, date) row, E1's `scr` column names."""
    ned: object
    er_time: object
    imp: float
    iv30d: float
    iv_rank: float
    mcap: float
    sector: object
    px: float
    issue_type: object
    adv: float


@dataclass(frozen=True)
class _Ctx:
    cal: list[date]
    idx: dict[date, int]
    cands: pd.DataFrame                   # ticker, E, er_time
    scr: dict[tuple[str, date], ScrRow]
    px: dict[tuple[str, date], float]


# ---- inputs ---------------------------------------------------------------------------------------
def screener_glob() -> str:
    return f"{config.STOCKS}/{config.SCREENER_GLOB}"


def _dates(s: pd.Series) -> pd.Series:
    return pd.to_datetime(s).dt.date


def default_event_range(con: duckdb.DuckDBPyConnection, screener: str) -> tuple[date, date]:
    """(first screener session + 1 session, last screener session - 1 session)."""
    lo, hi = con.execute(f"SELECT min(date), max(date) FROM read_parquet('{screener}')").fetchone()
    if lo is None:
        raise ValueError(f"no screener files match {screener}")
    return cal.next_session(lo), cal.prev_session(hi)


def _calendar(con: duckdb.DuckDBPyConnection, prices_path: str, e_max: date) -> list[date]:
    lo, hi = con.execute(
        f"SELECT min(date), max(date) FROM read_parquet('{prices_path}') WHERE ticker = 'SPY'").fetchone()
    if lo is None:
        raise ValueError(f"{prices_path} has no SPY rows; the calendar is anchored on SPY")
    return cal.trading_days(lo, max(hi, cal.next_session(e_max)))


def _load_candidates(con: duckdb.DuckDBPyConnection, screener: str, e_min: date, e_max: date
                     ) -> tuple[pd.DataFrame, pd.DataFrame]:
    """E1's `scr` slice (one row per ticker-date) and its candidates (ticker, E, plurality er_time)."""
    types = ", ".join(f"'{t}'" for t in config.ISSUE_TYPES)
    con.execute(f"""
        CREATE OR REPLACE TEMP TABLE {_SCR_TABLE} AS
        SELECT date, ticker, any_value(next_earnings_date) ned, any_value(er_time) er_time,
               any_value(implied_move_perc) imp, any_value(iv30d) iv30d, any_value(iv_rank) iv_rank,
               any_value(marketcap) mcap, any_value(sector) sector, any_value(close) AS px,
               any_value(issue_type) issue_type, any_value(avg30_volume) adv
        FROM read_parquet('{screener}') GROUP BY date, ticker""")
    try:
        cands = con.execute(f"""
            WITH win AS (SELECT ticker, ned AS E, er_time FROM {_SCR_TABLE}
                         WHERE ned IS NOT NULL AND ned BETWEEN DATE '{e_min}' AND DATE '{e_max}'
                           AND date <= ned AND date >= ned - INTERVAL {CANDIDATE_LOOKBACK_DAYS} DAY
                           AND issue_type IN ({types})),
                 cnt AS (SELECT ticker, E, er_time, count(*) n FROM win WHERE er_time IS NOT NULL GROUP BY ALL),
                 top AS (SELECT *, max(n) OVER (PARTITION BY ticker, E) mx FROM cnt),
                 lab AS (SELECT ticker, E, CASE WHEN count(*) = 1 THEN min(er_time) END er_time
                         FROM top WHERE n = mx GROUP BY ticker, E)
            SELECT w.ticker, w.E, lab.er_time
            FROM (SELECT DISTINCT ticker, E FROM win) w LEFT JOIN lab USING (ticker, E)
            ORDER BY 1, 2""").df()
        scr = con.execute(f"SELECT * FROM {_SCR_TABLE}").df()
    finally:
        con.execute(f"DROP TABLE IF EXISTS {_SCR_TABLE}")
    return scr, cands.assign(E=_dates(cands.E))


def _screener_map(scr: pd.DataFrame, tickers: set[str]) -> dict[tuple[str, date], ScrRow]:
    sub = scr[scr.ticker.isin(tickers)]
    sub = sub.assign(date=_dates(sub.date), ned=_dates(sub.ned))
    values = sub[list(ScrRow._fields)].itertuples(index=False, name=None)
    return {key: ScrRow(*v) for key, v in zip(zip(sub.ticker, sub.date), values)}


def _price_map(con: duckdb.DuckDBPyConnection, prices_path: str, tickers: set[str]
               ) -> dict[tuple[str, date], float]:
    px = con.execute(f"SELECT ticker, date, close FROM read_parquet('{prices_path}')").df()
    px = px[px.ticker.isin(tickers)]
    return dict(zip(zip(px.ticker, _dates(px.date)), px.close))


def _context(con, screener: str, prices_path: str, e_min: date, e_max: date) -> _Ctx:
    days = _calendar(con, prices_path, e_max)
    scr, cands = _load_candidates(con, screener, e_min, e_max)
    tickers = set(cands.ticker)
    return _Ctx(cal=days, idx=cal.session_index(days), cands=cands,
                scr=_screener_map(scr, tickers), px=_price_map(con, prices_path, tickers))


# ---- E1's per-event logic -------------------------------------------------------------------------
def _rel(a, b):
    """E1's relative change, including its truthiness (None/0 disable) and NaN semantics."""
    return (b / a - 1) if a and b and a > 0 else None


def _infer_timing(iv_prev, iv_E, iv_next) -> tuple[str, str]:
    c_e, c_n = _rel(iv_prev, iv_E), _rel(iv_E, iv_next)
    if c_e is not None and c_e <= CRUSH and (c_n is None or c_e < c_n):
        return "premarket", "inferred"
    if c_n is not None and c_n <= CRUSH:
        return "postmarket", "inferred"
    return "unresolved", "2-session"


def _timing(er_time: str, tk: str, sessions: tuple[date, date, date], ctx: _Ctx) -> tuple[str, str]:
    if er_time in LABELLED:
        return er_time, "labelled"
    ivs = [(r.iv30d if (r := ctx.scr.get((tk, d))) is not None else None) for d in sessions]
    return _infer_timing(*ivs)


def _window(timing: str, e_prev: date, E: date, e_next: date) -> tuple[date, date]:
    if timing == "postmarket":
        return E, e_next
    if timing == "premarket":
        return e_prev, E
    return e_prev, e_next


def _event_row(tk: str, E: date, er_time: str, ctx: _Ctx) -> dict | None:
    i = ctx.idx.get(E)
    if i is None or i == 0 or i + 1 >= len(ctx.cal):
        return None
    e_prev, e_next = ctx.cal[i - 1], ctx.cal[i + 1]
    timing, how = _timing(er_time, tk, (e_prev, E, e_next), ctx)
    pre, post = _window(timing, e_prev, E, e_next)
    s = ctx.scr.get((tk, pre))
    if s is None or s.ned != E or s.imp is None or not np.isfinite(s.imp):
        return None
    c_pre, c_post = ctx.px.get((tk, pre)), ctx.px.get((tk, post))
    if c_pre is None or c_post is None or c_pre < PRICE_FLOOR:
        return None
    i5 = ctx.idx[pre] - RUNUP_LOOKBACK_SESSIONS
    s5 = ctx.scr.get((tk, ctx.cal[i5])) if i5 >= 0 else None
    s_post = ctx.scr.get((tk, post))
    return {"ticker": tk, "E": E, "er_time": er_time, "timing": timing, "how": how, "pre": pre, "post": post,
            "spot_pre": c_pre, "close_post": c_post, "realized_move": abs(c_post / c_pre - 1),
            "gap_signed": c_post / c_pre - 1, "implied_move_perc": float(s.imp),
            "iv30d_pre": s.iv30d, "iv30d_post": (s_post.iv30d if s_post is not None else None),
            "iv_rank_pre": s.iv_rank, "imp_5d_ago": (s5.imp if s5 is not None else None),
            "iv30d_5d_ago": (s5.iv30d if s5 is not None else None),
            "marketcap": s.mcap, "sector": s.sector, "issue_type": s.issue_type,
            "adv_usd_30d": (s.adv or 0) * c_pre}


def _build_rows(ctx: _Ctx) -> pd.DataFrame:
    rows = [_event_row(c.ticker, c.E, c.er_time if isinstance(c.er_time, str) else UNKNOWN_ER_TIME, ctx)
            for c in ctx.cands.itertuples(index=False)]
    kept = [r for r in rows if r is not None]
    return pd.DataFrame(kept) if kept else _empty_events()


# ---- enrichment -----------------------------------------------------------------------------------
def _empty_events() -> pd.DataFrame:
    return pd.DataFrame({c: pd.Series(dtype="float64" if c in FLOAT_COLUMNS else object) for c in COLUMNS})


def season_of(d: date) -> str:
    for label, (lo, hi) in config.SEASONS.items():
        if lo <= d <= hi:
            return label
    return "off"


def _adv_usd_20d(con: duckdb.DuckDBPyConnection, prices_path: str, days: list[date],
                 keys: pd.DataFrame) -> dict[tuple[str, date], float]:
    """Mean close*volume over the 20 sessions ending at pre, keyed (ticker, pre); NaN when < 10 sessions."""
    con.register(_CAL_VIEW, pd.DataFrame({"date": pd.to_datetime(days), "si": range(len(days))}))
    con.register(_KEYS_VIEW, pd.DataFrame({"ticker": keys.ticker.values, "pre": pd.to_datetime(keys.pre)}))
    win = f"PARTITION BY ticker ORDER BY si RANGE BETWEEN {ADV_WINDOW_SESSIONS - 1} PRECEDING AND CURRENT ROW"
    try:
        out = con.execute(f"""
            WITH c AS (SELECT CAST(date AS DATE) AS date, si FROM {_CAL_VIEW}),
                 p AS (SELECT p.ticker, c.si, p.close * p.volume AS dv
                       FROM read_parquet('{prices_path}') p JOIN c ON p.date = c.date),
                 w AS (SELECT ticker, si, avg(dv) OVER ({win}) adv, count(dv) OVER ({win}) n FROM p)
            SELECT k.ticker, CAST(k.pre AS DATE) AS pre, CASE WHEN w.n >= {ADV_MIN_SESSIONS} THEN w.adv END AS adv
            FROM {_KEYS_VIEW} k
            LEFT JOIN c ON c.date = CAST(k.pre AS DATE)
            LEFT JOIN w ON w.ticker = k.ticker AND w.si = c.si""").df()
    finally:
        con.unregister(_CAL_VIEW)
        con.unregister(_KEYS_VIEW)
    return dict(zip(zip(out.ticker, _dates(out.pre)), out.adv.astype("float64")))


def _enrich(raw: pd.DataFrame, con, prices_path: str, days: list[date],
            regime_fn: RegimeFn, vix_fn: VixFn) -> pd.DataFrame:
    if raw.empty:
        return _empty_events()
    keys = raw[["ticker", "pre"]].drop_duplicates().reset_index(drop=True)
    adv20 = _adv_usd_20d(con, prices_path, days, keys)
    adv20_rows = np.array([adv20.get(k, np.nan) for k in zip(raw.ticker, raw.pre)], dtype="float64")
    pres = sorted(raw.pre.unique())
    regime = {d: regime_fn(d) for d in pres}
    vix = {d: vix_fn(d) for d in pres}
    out = raw.assign(
        date=raw.pre, proxy_pnl=raw.implied_move_perc - raw.realized_move,
        adv_usd_20d=np.where(np.isnan(adv20_rows), raw.adv_usd_30d, adv20_rows),
        regime_pre=raw.pre.map(regime), vix_pre=raw.pre.map(vix).astype("float64"),
        month=raw.pre.map(cal.month_of), season=raw.pre.map(season_of))
    out = out.astype({c: "float64" for c in FLOAT_COLUMNS})
    return out[COLUMNS].sort_values(["pre", "ticker", "E"]).reset_index(drop=True)


def default_regime_fn(con: duckdb.DuckDBPyConnection) -> RegimeFn:
    """`scripts/_regime.classify_regime` label before '/', as E1 stored it. Reads the real panel."""
    if config.SCRIPTS not in sys.path:
        sys.path.insert(0, config.SCRIPTS)
    from _regime import classify_regime  # noqa: E402

    return lambda d: classify_regime(d.isoformat(), con)["label"].split("/")[0]


def default_vix_fn(con: duckdb.DuckDBPyConnection) -> VixFn:
    series = load_vix(con)
    table = dict(zip(series.date, series.vix))
    return table.get


# ---- public API -----------------------------------------------------------------------------------
def build_events(con: duckdb.DuckDBPyConnection, screener: str, prices_path: str, e_min: date, e_max: date,
                 pre_only: date | None = None, regime_fn: RegimeFn | None = None,
                 vix_fn: VixFn | None = None) -> pd.DataFrame:
    """The event table for prints E in [e_min, e_max], pure over the given paths (see module doc)."""
    if e_max < e_min:
        raise ValueError(f"e_max {e_max} precedes e_min {e_min}")
    ctx = _context(con, screener, prices_path, e_min, e_max)
    raw = _build_rows(ctx)
    if pre_only is not None:
        raw = raw[raw.pre == pre_only]
    return _enrich(raw, con, prices_path, ctx.cal,
                   regime_fn or default_regime_fn(con), vix_fn or default_vix_fn(con))


def build_day(d: date, con: duckdb.DuckDBPyConnection | None = None, force: bool = False,
              regime_fn: RegimeFn | None = None, vix_fn: VixFn | None = None) -> pd.DataFrame:
    """Events with `pre == d`, written as one partition; see the module doc for when it is final.

    An existing partition is returned as-is unless `force`.
    """
    if not cal.is_trading_day(d):
        raise ValueError(f"{d} is not a trading day")
    if store.has_partition(TABLE, d) and not force:
        return store.read_partition(TABLE, d)
    con = con or duckdb.connect()
    df = build_events(con, screener_glob(), config.PRICES, d, cal.next_session(d), pre_only=d,
                      regime_fn=regime_fn, vix_fn=vix_fn)
    store.write_partition(df, TABLE, d)
    return df


def rebuild(force: bool = False, con: duckdb.DuckDBPyConnection | None = None) -> pd.DataFrame:
    """Build the whole table in one pass and write one partition per distinct `pre`."""
    existing = store.available_dates(TABLE)
    if existing and not force:
        raise FileExistsError(f"{TABLE} already has {len(existing)} partitions; pass --force to overwrite")
    con = con or duckdb.connect()
    e_min, e_max = default_event_range(con, screener_glob())
    df = build_events(con, screener_glob(), config.PRICES, e_min, e_max)
    if existing:
        shutil.rmtree(store.table_dir(TABLE), ignore_errors=True)
    for d, part in df.groupby("pre", sort=True):
        store.write_partition(part.reset_index(drop=True), TABLE, d)
    return df


def _summary(df: pd.DataFrame, secs: float) -> str:
    lines = [f"rows {len(df)} · partitions {df.pre.nunique()} · {secs:.1f}s",
             f"timing {df.timing.value_counts().to_dict()}",
             f"how {df.how.value_counts().to_dict()}",
             f"season {df.season.value_counts().to_dict()}",
             f"vix_pre null {int(df.vix_pre.isna().sum())} · regime_pre null {int(df.regime_pre.isna().sum())}"]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=f"build the {TABLE} mart table")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--date", help="build the partition for pre == D (YYYY-MM-DD)")
    g.add_argument("--rebuild", action="store_true", help="rebuild every partition in one pass")
    ap.add_argument("--force", action="store_true", help="overwrite existing partitions")
    args = ap.parse_args(argv)
    t0 = time.time()
    try:
        df = rebuild(force=args.force) if args.rebuild else build_day(cal.parse_date(args.date), force=args.force)
    except (FileExistsError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(_summary(df, time.time() - t0) if len(df) else f"no events · {time.time() - t0:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
