"""Per-week and across-formation statistics for the G4/G5 cross-section (RESEARCH/47 §2;
RESEARCH/30 §7 protocol: NW t at lag 1, BH across the 8 pre-registered tests, halves).

Pure functions over plain pandas objects; `engine.research.cross_section` supplies the panel.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats as sps

from engine.validation import stats as VS

NW_LAG = 1                 # formations are adjacent weeks; outcomes are non-overlapping (task spec)
MIN_WEEK_N = 5              # fewer names than this and a week's IC/decile is not trusted (NaN)
N_DECILES = 10


def residualize_week(df: pd.DataFrame, factor_col: str, control_cols: list[str]) -> pd.Series:
    """OLS residual of `factor_col` on `control_cols` (plus intercept) within one week's
    cross-section. Rows with a NaN in the factor or any control are excluded from the fit and get
    a NaN residual back (so the returned Series is aligned to `df.index`, same length as `df`)."""
    out = pd.Series(np.nan, index=df.index, dtype=float)
    cols = [factor_col] + control_cols
    complete = df[cols].apply(pd.to_numeric, errors="coerce").dropna()
    n_params = len(control_cols) + 1
    if len(complete) <= n_params:
        return out
    X = np.column_stack([np.ones(len(complete))] + [complete[c].to_numpy() for c in control_cols])
    y = complete[factor_col].to_numpy()
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ coef
    out.loc[complete.index] = resid
    return out


def rank_ic(df: pd.DataFrame, factor_col: str, outcome_col: str) -> tuple[float, int]:
    """Spearman rank-IC of one week's cross-section; `(nan, n)` when fewer than `MIN_WEEK_N` pairs."""
    sub = df[[factor_col, outcome_col]].apply(pd.to_numeric, errors="coerce").dropna()
    n = len(sub)
    if n < MIN_WEEK_N or sub[factor_col].nunique() < 2:
        return float("nan"), n
    rho, _ = sps.spearmanr(sub[factor_col], sub[outcome_col])
    return float(rho), n


def decile_spread(df: pd.DataFrame, factor_col: str, outcome_col: str, n_deciles: int = N_DECILES) -> tuple[float, int]:
    """Mean outcome of the top decile minus the bottom decile of `factor_col`, one week.
    `(nan, n)` when there are fewer than `2 * n_deciles` priced names (deciles would degenerate)."""
    sub = df[[factor_col, outcome_col]].apply(pd.to_numeric, errors="coerce").dropna()
    n = len(sub)
    if n < 2 * n_deciles:
        return float("nan"), n
    try:
        sub = sub.assign(_decile=pd.qcut(sub[factor_col], n_deciles, labels=False, duplicates="drop"))
    except ValueError:
        return float("nan"), n
    top, bottom = sub["_decile"].max(), sub["_decile"].min()
    if top == bottom:
        return float("nan"), n
    d_top = sub.loc[sub["_decile"] == top, outcome_col].mean()
    d_bottom = sub.loc[sub["_decile"] == bottom, outcome_col].mean()
    return float(d_top - d_bottom), n


def per_week_stats(df: pd.DataFrame, factor_col: str, outcome_col: str, week_col: str) -> pd.DataFrame:
    """One row per formation week: `ic`, `n_ic`, `decile_spread`, `n_decile`."""
    rows = []
    for wk, g in df.groupby(week_col, sort=True):
        ic, n_ic = rank_ic(g, factor_col, outcome_col)
        ds, n_ds = decile_spread(g, factor_col, outcome_col)
        rows.append({week_col: wk, "ic": ic, "n_ic": n_ic, "decile_spread": ds, "n_decile": n_ds})
    return pd.DataFrame(rows).sort_values(week_col).reset_index(drop=True)


def sign_consistency(ic_series: pd.Series) -> float:
    """Share of non-NaN, non-zero formation ICs agreeing in sign with the overall mean IC."""
    x = pd.Series(ic_series, dtype=float).dropna()
    x = x[x != 0]
    if x.empty:
        return float("nan")
    mean_sign = np.sign(x.mean())
    if mean_sign == 0:
        return float("nan")
    return float((np.sign(x) == mean_sign).mean())


def half_split(ic_series: pd.Series) -> dict:
    """Mean IC in the first and second chronological halves (`ic_series` must already be
    ordered by formation date); the split point is `len // 2`."""
    x = pd.Series(ic_series, dtype=float).reset_index(drop=True)
    mid = len(x) // 2
    first, second = x.iloc[:mid], x.iloc[mid:]
    return {
        "first_half_mean_ic": float(first.mean()) if len(first) else float("nan"),
        "second_half_mean_ic": float(second.mean()) if len(second) else float("nan"),
        "first_half_n": int(first.notna().sum()),
        "second_half_n": int(second.notna().sum()),
        "sign_stable_across_halves": bool(np.sign(first.mean()) == np.sign(second.mean()))
            if len(first) and len(second) and pd.notna(first.mean()) and pd.notna(second.mean()) else False,
    }


def summarize_ic(ic_series: pd.Series, lag: int = NW_LAG) -> dict:
    """Mean IC, NW t/p (lag `NW_LAG`, Bartlett kernel, `engine.validation.stats.nw_t`), sign
    consistency and the half-split, from one factor's per-formation IC series (ordered by week)."""
    x = pd.Series(ic_series, dtype=float)
    nw = VS.nw_t(x.dropna().to_numpy(), lag=lag)
    out = {"mean_ic": nw["mean"], "nw_t": nw["t"], "nw_p": nw["p"], "n_formations": nw["n"],
           "sign_consistency": sign_consistency(x)}
    out.update(half_split(x))
    return out


def bh_qvalues(pvals) -> list[float]:
    """Benjamini-Hochberg adjusted p-values (q-values): monotone step-up correction, same family
    as `engine.validation.stats.bh_reject` but returning the continuous adjusted p rather than a
    reject/accept boolean, for reporting a `BH q` column."""
    p = np.asarray(list(pvals), dtype=float)
    m = len(p)
    if m == 0:
        return []
    order = np.argsort(p)
    ranked = p[order]
    raw_q = ranked * m / (np.arange(1, m + 1))
    q = np.minimum.accumulate(raw_q[::-1])[::-1]     # enforce monotonicity from the largest rank down
    q = np.clip(q, 0.0, 1.0)
    out = np.empty(m, dtype=float)
    out[order] = q
    return out.tolist()
