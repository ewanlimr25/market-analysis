"""The five descriptive tables of `DESIGN/110-watch-basket.md` §5, built from the assembled
`wb_conditions`-shaped frame `retro.py` produces. Every mean/median/hit-rate/t is clustered by
ticker (`engine.validation.stats.cluster_t`, the same Liang-Zeger cluster-robust estimator the
rest of the engine's validation reports use); the independent-episode count (`basket.py`'s §4
rule) is reported beside every mean as its own column, never substituted for the cluster count.
"""
from __future__ import annotations

from datetime import date

import pandas as pd

from engine.validation import stats as VS
from engine.watch import basket as BK
from engine.watch import conditions as C

GRADE_HORIZONS = (5, 10, 21)


def session_index(dates: list[date]) -> dict[date, int]:
    ordered = sorted(set(dates))
    return {d: i for i, d in enumerate(ordered)}


def cluster_stats_for_rows(rows: pd.DataFrame, returns_df: pd.DataFrame, horizon: int) -> dict:
    sub = returns_df.loc[returns_df["horizon"] == horizon, ["ticker", "date", "excess"]]
    merged = rows[["ticker", "date"]].merge(sub, on=["ticker", "date"], how="left").dropna(subset=["excess"])
    if merged.empty:
        return {"n": 0, "G": 0, "mean": float("nan"), "median": float("nan"),
                "hit": float("nan"), "t": float("nan"), "p": float("nan"), "se": float("nan")}
    return VS.cluster_t(merged["excess"].to_numpy(), merged["ticker"].to_numpy())


def _episode_count(rows: pd.DataFrame, idx: dict[date, int]) -> int:
    if rows.empty:
        return 0
    episoded = BK.assign_episodes(rows[["ticker", "date"]], ["ticker"], "date", idx)
    return BK.episode_count(episoded, ["ticker"])


def _row_stats(label: str, rows: pd.DataFrame, returns_df: pd.DataFrame, idx: dict[date, int],
               base: dict[int, dict], n_total_nights: int) -> dict:
    out = {"key": label, "nights_true": int(len(rows)), "names": int(rows["ticker"].nunique()) if len(rows) else 0,
           "episodes": _episode_count(rows, idx)}
    for h in GRADE_HORIZONS:
        st = cluster_stats_for_rows(rows, returns_df, h)
        b = base[h]
        out[f"h{h}_n"] = st["n"]
        out[f"h{h}_names_clustered"] = st["G"]
        out[f"h{h}_mean_excess"] = st["mean"]
        out[f"h{h}_median_excess"] = st["median"]
        out[f"h{h}_hit_rate"] = st["hit"]
        out[f"h{h}_t_clustered"] = st["t"]
        out[f"h{h}_base_mean_excess"] = b["mean"]
        out[f"h{h}_base_hit_rate"] = b["hit"]
    return out


def base_stats(cond_df: pd.DataFrame, returns_df: pd.DataFrame) -> dict[int, dict]:
    """Unconditional universe-wide stats per horizon -- the "against the universe base" reference
    every table row carries alongside its own numbers."""
    return {h: cluster_stats_for_rows(cond_df[["ticker", "date"]], returns_df, h) for h in GRADE_HORIZONS}


def condition_table(cond_df: pd.DataFrame, returns_df: pd.DataFrame) -> pd.DataFrame:
    """Table (a): per condition -- nights true, names, episodes, h5/h10/h21 stats, null rate."""
    idx = session_index(list(cond_df["date"]))
    base = base_stats(cond_df, returns_df)
    n_total = len(cond_df)
    rows = []
    for cid in C.ALL_CONDITIONS:
        col = cond_df[cid]
        true_rows = cond_df.loc[col == True, ["ticker", "date"]]  # noqa: E712 -- explicit True, not truthy
        n_null = int(col.isna().sum())
        stat = _row_stats(cid, true_rows, returns_df, idx, base, n_total)
        stat["null_nights"] = n_null
        stat["null_rate"] = n_null / n_total if n_total else float("nan")
        stat["sign"] = ("+" if cid in C.SIGN_PLUS else "-" if cid in C.SIGN_MINUS
                        else "V" if cid in C.SIGN_VOL else "L")
        rows.append(stat)
    return pd.DataFrame(rows)


def count_table(cond_df: pd.DataFrame, returns_df: pd.DataFrame, count_col: str, max_count: int) -> pd.DataFrame:
    """Table (b): per exact `bull`/`bear` count 0..`max_count`."""
    idx = session_index(list(cond_df["date"]))
    base = base_stats(cond_df, returns_df)
    rows = []
    for k in range(max_count + 1):
        sub = cond_df.loc[cond_df[count_col] == k, ["ticker", "date"]]
        rows.append(_row_stats(f"{count_col}={k}", sub, returns_df, idx, base, len(cond_df)))
    return pd.DataFrame(rows)


def basket_table(cond_df: pd.DataFrame, returns_df: pd.DataFrame) -> pd.DataFrame:
    """Table (c): per basket (LONG, SHORT, VOL, CONFLICT)."""
    idx = session_index(list(cond_df["date"]))
    base = base_stats(cond_df, returns_df)
    rows = []
    for name in BK.BASKET_NAMES:
        sub = cond_df.loc[cond_df[name] == True, ["ticker", "date"]]  # noqa: E712
        rows.append(_row_stats(name, sub, returns_df, idx, base, len(cond_df)))
    return pd.DataFrame(rows)


def worked_examples(cond_df: pd.DataFrame, returns_df: pd.DataFrame, n: int = 6) -> dict:
    """Table (d): the `n` highest-`bull` and `n` highest-`bear` names-and-dates, each with its
    true condition ids and realized h21 excess. Ties broken by most-recent date, then ticker."""
    h21 = returns_df.loc[returns_df["horizon"] == 21, ["ticker", "date", "excess"]]
    merged = cond_df.merge(h21, on=["ticker", "date"], how="left")

    def _top(metric: str) -> list[dict]:
        ranked = merged.sort_values([metric, "date", "ticker"], ascending=[False, False, True])
        picked = ranked.drop_duplicates(["ticker", "date"]).head(n)
        out = []
        for _, r in picked.iterrows():
            true_ids = [cid for cid in C.ALL_CONDITIONS if r[cid] is True]
            out.append({
                "ticker": r["ticker"], "date": r["date"].isoformat(), metric: int(r[metric]),
                "true_ids": true_ids,
                "h21_excess": (None if pd.isna(r["excess"]) else float(r["excess"])),
            })
        return out

    return {"top_bull": _top("bull"), "top_bear": _top("bear")}


def nightly_basket_sizes(cond_df: pd.DataFrame) -> dict:
    """Table (e): nightly basket size distribution (min/median/max across the panel's nights)."""
    all_dates = pd.Index(sorted(cond_df["date"].unique()))
    out = {}
    for name in BK.BASKET_NAMES:
        counts = cond_df.loc[cond_df[name] == True].groupby("date").size()  # noqa: E712
        counts = counts.reindex(all_dates, fill_value=0)
        out[name] = {"min": int(counts.min()), "median": float(counts.median()), "max": int(counts.max())}
    return out
