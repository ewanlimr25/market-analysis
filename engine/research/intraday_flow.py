"""G2 — intraday flow event study (S-F). RESEARCH/47-edge-gaps.md §2 G2, DESIGN/60-redesign.md §4 S-F.

Pre-registered design (do not widen without a new registration):

  Events: single-leg prints, premium >= $250,000, DTE (calendar days) 0..30, executed 09:35..15:30
  ET, on underlyings with >= 100 distinct `underlying_price` observations that session
  (RESEARCH/20 §2.4, §7.3). Six single-leg condition codes only (RESEARCH/20 §2.2): a print tagged
  multi-leg, floor-multi-leg, two-leg, complex, cabinet or late does not get a `side`.

  Direction: call at ask or put at bid = bullish; put at ask or call at bid = bearish; mid /
  no_side excluded from the directional cells but counted (RESEARCH/47 §2 G2).

  Classification (primary): the D+1 OI join (RESEARCH/20 §7.2). OPENING if the contract's
  next-session `oi_diff_plain` is >= this print's own size, CLOSING if <= -size, MIXED otherwise
  (including no matching OI row, e.g. the panel's 19-session hole or the last panel day).

  Classification (secondary, reported not scored): the running-volume-crosses-open_interest proxy
  (RESEARCH/20 §2.4) -- whether this print's own cumulative `volume` has reached the session's
  starting `open_interest`.

This module builds the two per-day intermediates (`build_day`): the qualifying event prints,
labeled, and the 5-minute underlying-price path for every liquid underlying that session. Both are
pure with respect to the filesystem beyond the paths passed in. `scripts/intraday_flow.py` drives
the panel loop and persists the partitions under `data/backtest/g2_events/` and `data/backtest/g2_path/`.
"""
from __future__ import annotations

import math
import os
from dataclasses import dataclass
from datetime import date

import duckdb
import pandas as pd

from engine import calendar as cal
from engine import config

# ----------------------------------------------------------------------------------- parameters

EVENT_PREMIUM_MIN = 250_000.0
EVENT_DTE_CAL_MIN = 0
EVENT_DTE_CAL_MAX = 30
EVENT_TIME_START = "09:35:00"
EVENT_TIME_END = "15:30:00"                 # inclusive
PATH_BUCKET_MINUTES = 5
MIN_UNDERLYING_OBS = 100                     # RESEARCH/20 §7.3 / RESEARCH/47 §2 G2
HORIZONS_MIN: tuple[int, ...] = (30, 60, 120)
OUTCOME_TOLERANCE_MIN = 10                   # drop an outcome with no observation this close
SPY_SYMBOL = "SPY"
BH_FDR = 0.05                                # RESEARCH/47 §2 G2's pre-registered bar
# Cameron-Gelbach-Miller two-way clustering is unreliable when a dimension has few clusters, and
# degenerates (Var_a + Var_b - Var_(a,b) collapses onto the smaller dimension's tiny residual sum)
# when the two dimensions are near-collinear within a cell -- e.g. a cell where every underlying's
# prints fall on a single day. A cell needs at least this many clusters on BOTH dimensions to be
# scored; smaller cells are reported as untested, not silently given an inflated t.
MIN_CLUSTERS_PER_DIM = 5
CELL_DIMS: tuple[str, ...] = (
    "direction", "size_bucket", "dte_bucket", "tod_bucket", "classification_oi", "horizon")

# RESEARCH/20 §2.2 "clean single-leg lane": side carries unambiguous directional meaning only here.
SINGLE_LEG_CODES: tuple[str, ...] = ("auto", "isoi", "slan", "slai", "slft", "slcn")

SIZE_BUCKETS: tuple[tuple[str, float, float], ...] = (
    ("250k_1m", EVENT_PREMIUM_MIN, 1_000_000.0),   # [250k, 1M)
    ("gte_1m", 1_000_000.0, math.inf),              # [1M, inf)
)
DTE_BUCKETS: tuple[tuple[str, int, int], ...] = (
    ("0_7", 0, 7),
    ("8_30", 8, 30),
)
TOD_BUCKETS: tuple[tuple[str, str, str], ...] = (
    ("09:35-11:00", "09:35:00", "11:00:00"),   # [start, end)
    ("11:00-14:00", "11:00:00", "14:00:00"),   # [start, end)
    ("14:00-15:30", "14:00:00", "15:30:00"),   # [start, end] -- last bucket is closed both ends
)
CLASSIFICATIONS: tuple[str, ...] = ("OPENING", "CLOSING", "MIXED")

OI_CHANGES_FILE = "OI changes/chain-oi-changes-{d}.parquet"

RAW_COLUMNS = (
    "executed_at", "underlying_symbol", "option_chain_id", "option_type", "side", "expiry",
    "underlying_price", "price", "size", "premium", "volume", "open_interest",
    "upstream_condition_detail",
)

EVENT_COLUMNS = (
    "executed_at", "et", "underlying_symbol", "option_chain_id", "option_type", "side",
    "entry_underlying_price", "price", "size", "premium", "volume", "open_interest", "dte_cal",
)


# ----------------------------------------------------------------------------------- paths


def all_options_path(d: date) -> str:
    return os.path.join(config.STOCKS, config.ALL_OPTIONS_FILE.format(d=d.isoformat()))


def oi_changes_path(d: date) -> str | None:
    """The OI-changes file dated the next NYSE trading session after `d`, if it exists on disk.

    RESEARCH/20 §7.2: a print on day D joins to the OI-change row filed the morning of D+1. When
    the panel's 19-session hole (2026-03-30..04-24) or the last panel day sits between D and its
    would-be D+1, no file exists and the join is skipped (classification MIXED, counted separately).
    """
    nxt = cal.next_session(d)
    path = os.path.join(config.STOCKS, OI_CHANGES_FILE.format(d=nxt.isoformat()))
    return path if os.path.exists(path) else None


def _quote(path: str) -> str:
    return "'" + path.replace("'", "''") + "'"


# ----------------------------------------------------------------------------------- SQL builders


def raw_prints_sql(all_options_path_: str) -> str:
    """The one scan of the day's All Options file: session window, canceled/size/price filter,
    the columns both the event selection and the path bucketing need, ET-local timestamp added.
    """
    return f"""
    SELECT {", ".join(RAW_COLUMNS)},
           (executed_at AT TIME ZONE '{config.ET_TZ}')::TIMESTAMP AS et
    FROM read_parquet({_quote(all_options_path_)})
    WHERE NOT canceled AND size > 0 AND price > 0
      AND (executed_at AT TIME ZONE '{config.ET_TZ}')::TIME >= TIME '{config.SESSION_START}'
      AND (executed_at AT TIME ZONE '{config.ET_TZ}')::TIME <  TIME '{config.SESSION_END_EXCL}'
    """


def path_bucketing_sql(raw_relation: str = "raw") -> str:
    """5-minute underlying-price path per underlying with >= MIN_UNDERLYING_OBS distinct prices
    that session (RESEARCH/20 §7.3 pattern, at 5-minute rather than 30-minute resolution).
    """
    return f"""
    WITH elig AS (
      SELECT underlying_symbol
      FROM {raw_relation}
      WHERE underlying_price IS NOT NULL
      GROUP BY underlying_symbol
      HAVING count(DISTINCT underlying_price) >= {MIN_UNDERLYING_OBS}
    )
    SELECT r.underlying_symbol,
           time_bucket(INTERVAL '{PATH_BUCKET_MINUTES} minutes', r.et) AS bucket_ts,
           arg_max(r.underlying_price, r.et) AS last_price,
           max(r.et)                          AS last_ts,
           count(*)                           AS n_prints
    FROM {raw_relation} r JOIN elig e USING (underlying_symbol)
    WHERE r.underlying_price IS NOT NULL
    GROUP BY 1, 2
    ORDER BY 1, 2
    """


def event_selection_sql(raw_relation: str = "raw") -> str:
    """Qualifying single-leg prints: premium floor, the six single-leg condition codes, the
    09:35-15:30 window and DTE 0..30 calendar days (RESEARCH/47 §2 G2's pre-registered filter).
    Not yet restricted to liquid underlyings; caller intersects with `path_bucketing_sql`'s output.
    """
    codes = ", ".join(f"'{c}'" for c in SINGLE_LEG_CODES)
    return f"""
    SELECT executed_at, et, underlying_symbol, option_chain_id, option_type, side,
           underlying_price AS entry_underlying_price, price, size, premium, volume, open_interest,
           date_diff('day', et::DATE, expiry) AS dte_cal
    FROM {raw_relation}
    WHERE premium >= {EVENT_PREMIUM_MIN}
      AND upstream_condition_detail IN ({codes})
      AND et::TIME >= TIME '{EVENT_TIME_START}' AND et::TIME <= TIME '{EVENT_TIME_END}'
      AND date_diff('day', et::DATE, expiry) BETWEEN {EVENT_DTE_CAL_MIN} AND {EVENT_DTE_CAL_MAX}
    """


# ----------------------------------------------------------------------------------- labeling


def _bucket_of(value: float, buckets: tuple) -> str | None:
    """First bucket whose half-open [lo, hi) contains `value` (the last bucket's hi may be inf)."""
    for name, lo, hi in buckets:
        if lo <= value < hi:
            return name
    return None


def label_direction(option_type: pd.Series, side: pd.Series) -> pd.Series:
    bullish = ((option_type == "call") & (side == "ask")) | ((option_type == "put") & (side == "bid"))
    bearish = ((option_type == "put") & (side == "ask")) | ((option_type == "call") & (side == "bid"))
    return pd.Series(
        [_pick(b, r) for b, r in zip(bullish, bearish)], index=option_type.index, dtype="object")


def _pick(bullish: bool, bearish: bool) -> str:
    if bullish:
        return "bullish"
    if bearish:
        return "bearish"
    return "excluded"


def label_size_bucket(premium: pd.Series) -> pd.Series:
    return premium.map(lambda p: _bucket_of(p, SIZE_BUCKETS))


def label_dte_bucket(dte_cal: pd.Series) -> pd.Series:
    return dte_cal.map(lambda d: next((n for n, lo, hi in DTE_BUCKETS if lo <= d <= hi), None))


def label_tod_bucket(et: pd.Series) -> pd.Series:
    t = et.dt.time
    out = pd.Series(None, index=et.index, dtype="object")
    for name, lo, hi in TOD_BUCKETS:
        lo_t, hi_t = pd.Timestamp(lo).time(), pd.Timestamp(hi).time()
        inclusive_hi = hi == TOD_BUCKETS[-1][2]
        mask = (t >= lo_t) & ((t <= hi_t) if inclusive_hi else (t < hi_t))
        out = out.mask(mask & out.isna(), name)
    return out


def classify_oi_join(oi_diff_plain: pd.Series, size: pd.Series) -> pd.Series:
    """RESEARCH/47 §2 G2 (a): OPENING if next-session OI rose by >= this print's size, CLOSING if
    it fell by >= size, MIXED otherwise (NULL oi_diff_plain -- no matching row -- is MIXED too)."""
    opening = (oi_diff_plain >= size).fillna(False).astype(bool)
    closing = (oi_diff_plain <= -size).fillna(False).astype(bool)
    out = pd.Series("MIXED", index=oi_diff_plain.index, dtype="object")
    out = out.mask(opening, "OPENING")
    out = out.mask(closing, "CLOSING")
    return out


def label_opening_proxy(volume: pd.Series, open_interest: pd.Series) -> pd.Series:
    """RESEARCH/20 §2.4 secondary label: this print's own cumulative volume has reached the
    session's starting open interest. Reported, not used in the primary cell grid."""
    return volume >= open_interest


def label_events(df: pd.DataFrame, oi: pd.DataFrame | None) -> pd.DataFrame:
    """Add direction, the three cut buckets and both classification labels to selected events.

    `oi` is the next-session OI-changes frame (`option_symbol`, `oi_diff_plain`) or None when no
    file was available; a left join either way so `oi_row_found` records the coverage gap.
    """
    out = df.copy()
    out["direction"] = label_direction(out["option_type"], out["side"])
    out["size_bucket"] = label_size_bucket(out["premium"])
    out["dte_bucket"] = label_dte_bucket(out["dte_cal"])
    out["tod_bucket"] = label_tod_bucket(out["et"])
    if oi is not None and len(oi):
        out = out.merge(oi[["option_symbol", "oi_diff_plain"]], how="left",
                        left_on="option_chain_id", right_on="option_symbol")
        out = out.drop(columns=["option_symbol"])
    else:
        out["oi_diff_plain"] = pd.Series(pd.NA, index=out.index, dtype="Int64")
    out["oi_row_found"] = out["oi_diff_plain"].notna()
    out["classification_oi"] = classify_oi_join(out["oi_diff_plain"], out["size"])
    out["opening_proxy_volume"] = label_opening_proxy(out["volume"], out["open_interest"])
    return out


# ----------------------------------------------------------------------------------- orchestration


@dataclass(frozen=True)
class DayBuild:
    date: date
    events: pd.DataFrame
    path: pd.DataFrame
    seconds: float
    n_raw_prints: int


def build_day(con: duckdb.DuckDBPyConnection, d: date) -> DayBuild:
    """One pass over day `d`'s All Options file: qualifying events (labeled) and the 5-minute
    liquid-underlying path. Memory-bounded: the day's session-filtered prints live in one DuckDB
    temp table for the duration of this call and are dropped before returning.
    """
    import time
    t0 = time.perf_counter()
    ao = all_options_path(d)
    if not os.path.exists(ao):
        raise FileNotFoundError(f"No All Options file for {d.isoformat()}: {ao}")
    con.execute("DROP TABLE IF EXISTS raw_g2")
    con.execute(f"CREATE TEMP TABLE raw_g2 AS {raw_prints_sql(ao)}")
    n_raw = con.execute("SELECT count(*) FROM raw_g2").fetchone()[0]
    path_df = con.execute(path_bucketing_sql("raw_g2")).df()
    events_df = con.execute(event_selection_sql("raw_g2")).df()
    liquid = set(path_df["underlying_symbol"].unique())
    events_df = events_df[events_df["underlying_symbol"].isin(liquid)].reset_index(drop=True)
    oi_path = oi_changes_path(d)
    oi_df = None
    if oi_path is not None:
        oi_df = con.execute(
            f"SELECT option_symbol, oi_diff_plain FROM read_parquet({_quote(oi_path)})").df()
    events_df = label_events(events_df, oi_df)
    events_df.insert(0, "date", d)
    path_df.insert(0, "date", d)
    con.execute("DROP TABLE raw_g2")
    return DayBuild(d, events_df, path_df, time.perf_counter() - t0, int(n_raw))


def panel_dates() -> list[date]:
    """Every day with an All Options file, ascending (mirrors engine.mart.daily_contract)."""
    import glob
    import re
    pattern = os.path.join(config.STOCKS, config.ALL_OPTIONS_FILE.format(d="*"))
    date_re = re.compile(r"(\d{4}-\d{2}-\d{2})")
    matches = (date_re.search(os.path.basename(p)) for p in glob.glob(pattern))
    return sorted(date.fromisoformat(m.group(1)) for m in matches if m)
