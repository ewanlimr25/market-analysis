"""G2 outcome join and cell statistics (RESEARCH/47-edge-gaps.md §2 G2).

`join_outcomes` turns one day's labeled events plus its 5-minute path into a long frame (one row
per event per horizon) carrying the SPY-excess signed return. `cell_stats` aggregates the long
frame over the pre-registered grid -- side x size bucket x DTE bucket x time-of-day x
classification x horizon -- with a t clustered by (underlying, day). `add_bh_and_stability` applies
Benjamini-Hochberg and the sign-stability kill rule, gating on `MIN_CLUSTERS_PER_DIM` because
Cameron-Gelbach-Miller two-way clustering can manufacture an enormous spurious t when a cell's
underlying and day dimensions are near-collinear (every print of a given underlying falling on one
day) and one dimension has few clusters -- observed directly on a 2-day smoke test (a cell read
t = -780 from 5 underlyings that happened to split cleanly across only 2 days). `descriptive_oi_share`
is the standalone OPENING/CLOSING/MIXED-by-time-of-day-and-side table RESEARCH/47 §2 G2 asks for.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from engine.research.intraday_flow import (
    BH_FDR, CELL_DIMS, HORIZONS_MIN, MIN_CLUSTERS_PER_DIM, OUTCOME_TOLERANCE_MIN, SPY_SYMBOL,
)
from engine.validation import stats

DIRECTIONAL = ("bullish", "bearish")

OUTCOME_COLUMNS = (
    "date", "underlying_symbol", "option_chain_id", "direction", "size_bucket", "dte_bucket",
    "tod_bucket", "classification_oi", "opening_proxy_volume", "horizon", "raw_ret", "spy_ret",
    "excess", "outcome_dropped",
)


def _asof_lookup(times: pd.Series, path: pd.DataFrame, tolerance_min: int,
                  by: pd.Series | None = None) -> np.ndarray:
    """`last_price` of the nearest `path` row at or before each `times[i]` (matched within `by[i]`
    when given), requiring that row's `last_ts` within `tolerance_min` minutes; else NaN. Result is
    aligned to `times`'s original order regardless of how the internal sort reorders rows."""
    n = len(times)
    if n == 0 or path.empty:
        return np.full(n, np.nan)
    left = pd.DataFrame({"_t": pd.to_datetime(np.asarray(times)), "_pos": np.arange(n)})
    right = path[["last_ts", "last_price"]].copy()
    if by is not None:
        left["_by"] = np.asarray(by)
        right["_by"] = path["underlying_symbol"].to_numpy()
        left = left.sort_values("_t")
        right = right.sort_values("last_ts")
        merged = pd.merge_asof(left, right, left_on="_t", right_on="last_ts", by="_by",
                               direction="backward", tolerance=pd.Timedelta(minutes=tolerance_min))
    else:
        left = left.sort_values("_t")
        right = right.sort_values("last_ts")
        merged = pd.merge_asof(left, right, left_on="_t", right_on="last_ts",
                               direction="backward", tolerance=pd.Timedelta(minutes=tolerance_min))
    return merged.sort_values("_pos")["last_price"].to_numpy()


def _direction_sign(direction: pd.Series) -> np.ndarray:
    return np.where(direction == "bullish", 1.0, np.where(direction == "bearish", -1.0, np.nan))


def join_outcomes(events: pd.DataFrame, path: pd.DataFrame, horizons=HORIZONS_MIN,
                  tolerance_min: int = OUTCOME_TOLERANCE_MIN, spy_symbol: str = SPY_SYMBOL
                  ) -> pd.DataFrame:
    """One day's events x horizons, long format, with the SPY-excess signed return.

    `events` and `path` must be a single day's `build_day` output (asof matching never crosses
    days). `excess` is NaN, `outcome_dropped` True, whenever the underlying or SPY has no path
    observation within `tolerance_min` minutes of the target horizon, or `direction` is excluded.
    """
    if events.empty:
        return pd.DataFrame(columns=list(OUTCOME_COLUMNS))
    spy_path = path[path["underlying_symbol"] == spy_symbol]
    spy_entry = _asof_lookup(events["et"], spy_path, tolerance_min)
    sign = _direction_sign(events["direction"])
    entry_price = events["entry_underlying_price"].to_numpy(dtype=float)
    frames = []
    for h in horizons:
        target = events["et"] + pd.Timedelta(minutes=h)
        exit_u = _asof_lookup(target, path, tolerance_min, by=events["underlying_symbol"])
        exit_spy = _asof_lookup(target, spy_path, tolerance_min)
        with np.errstate(invalid="ignore", divide="ignore"):
            raw_ret = np.log(exit_u / entry_price)
            spy_ret = np.log(exit_spy / spy_entry)
        excess = sign * (raw_ret - spy_ret)
        frame = events[["date", "underlying_symbol", "option_chain_id", "direction", "size_bucket",
                        "dte_bucket", "tod_bucket", "classification_oi",
                        "opening_proxy_volume"]].copy()
        frame["horizon"] = h
        frame["raw_ret"] = raw_ret
        frame["spy_ret"] = spy_ret
        frame["excess"] = excess
        frame["outcome_dropped"] = ~np.isfinite(excess)
        frames.append(frame)
    return pd.concat(frames, ignore_index=True)[list(OUTCOME_COLUMNS)]


def cell_stats(long_df: pd.DataFrame) -> pd.DataFrame:
    """Per pre-registered cell: n, mean, median, hit rate, and the (underlying, day)-clustered t."""
    df = long_df[long_df["direction"].isin(DIRECTIONAL) & long_df["excess"].notna()]
    cols = [*CELL_DIMS, "n", "mean", "median", "hit", "t", "p", "Ga", "Gb"]
    if df.empty:
        return pd.DataFrame(columns=cols)
    rows = []
    for keys, g in df.groupby(list(CELL_DIMS), observed=True):
        stat = stats.two_way_cluster_t(g["excess"].to_numpy(), g["underlying_symbol"].to_numpy(),
                                       g["date"].to_numpy())
        rows.append({**dict(zip(CELL_DIMS, keys)), **stat})
    out = pd.DataFrame(rows)[cols]
    return out.sort_values("p", na_position="last").reset_index(drop=True)


def _half_split_signs(long_df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Mean excess per cell in each date-ordered half of the panel present in `long_df`."""
    df = long_df[long_df["direction"].isin(DIRECTIONAL) & long_df["excess"].notna()]
    dates = np.sort(df["date"].unique())
    if len(dates) < 2:
        empty = pd.Series(dtype=float)
        return empty, empty
    mid = dates[len(dates) // 2]
    g1 = df[df["date"] < mid].groupby(list(CELL_DIMS), observed=True)["excess"].mean()
    g2 = df[df["date"] >= mid].groupby(list(CELL_DIMS), observed=True)["excess"].mean()
    return g1, g2


def add_bh_and_stability(cell_df: pd.DataFrame, long_df: pd.DataFrame, fdr: float = BH_FDR
                         ) -> pd.DataFrame:
    """Add `bh_reject`, `sign_stable` (RESEARCH/47's kill rule: BH-significant pooled AND the same
    sign in both halves of the panel) and `survivor` = both. A cell is `tested` only when its p is
    defined AND both cluster dimensions clear `MIN_CLUSTERS_PER_DIM` -- otherwise two-way
    clustering can degenerate to a near-zero variance and manufacture an enormous, spurious t
    (see the module docstring / RESEARCH write-up)."""
    out = cell_df.copy()
    out["tested"] = (out["p"].notna() & (out["Ga"] >= MIN_CLUSTERS_PER_DIM)
                     & (out["Gb"] >= MIN_CLUSTERS_PER_DIM))
    pvals = out.loc[out["tested"], "p"]
    reject = pd.Series(False, index=out.index)
    if len(pvals):
        reject.loc[pvals.index] = stats.bh_reject(pvals, fdr)
    out["bh_reject"] = reject
    half1, half2 = _half_split_signs(long_df)

    def stable(row) -> bool:
        key = tuple(row[c] for c in CELL_DIMS)
        s1, s2 = half1.get(key, np.nan), half2.get(key, np.nan)
        pooled = np.sign(row["mean"])
        return bool(pooled != 0 and pd.notna(s1) and pd.notna(s2)
                   and np.sign(s1) == pooled and np.sign(s2) == pooled)

    out["sign_stable"] = out.apply(stable, axis=1) if len(out) else pd.Series(dtype=bool)
    out["survivor"] = out["bh_reject"] & out["sign_stable"]
    return out


def descriptive_oi_share(events_df: pd.DataFrame) -> pd.DataFrame:
    """Share of qualifying >= $250k single-leg premium that is OPENING / CLOSING / MIXED, by
    time-of-day and by side (direction incl. `excluded`) -- informs S-A/S-C entry timing regardless
    of the direction result (RESEARCH/47 §2 G2)."""
    if events_df.empty:
        return pd.DataFrame(columns=["tod_bucket", "direction", "classification_oi",
                                     "n", "premium", "premium_share"])
    grouped = (events_df.groupby(["tod_bucket", "direction", "classification_oi"], observed=True)
              .agg(n=("premium", "size"), premium=("premium", "sum")).reset_index())
    total = grouped.groupby(["tod_bucket", "direction"])["premium"].transform("sum")
    grouped["premium_share"] = grouped["premium"] / total
    return grouped.sort_values(["tod_bucket", "direction", "classification_oi"]).reset_index(drop=True)
