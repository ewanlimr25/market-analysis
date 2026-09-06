"""Validation harness for S-B (DESIGN/80 §6): sleeve tables with Newey-West and expiry-clustered
t, BH across the four sleeves, deflated Sharpe at the six-trial charge, PBO, the month rule, the
tail report, the marked-vs-proxy overlap check and the go/no-go verdict.

Every function takes position frames (one row per (entry, underlying, structure)) and returns a
DataFrame or dict. A sleeve is one (underlying, structure).
"""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

from engine.config import (SB_DSR_TRIALS, SB_GO_MONTH_LOSS_MULT, SB_GO_T_MIN, SB_NW_LAG, SB_PBO_BLOCKS,
                           SB_SCALE_MIN_POSITIONS, SB_STRUCTURES, SB_UNDERLYINGS, SB_WINDOWS, BH_FDR)
from engine.validation import stats as S

SLEEVES = [(u, s) for u in SB_UNDERLYINGS for s in SB_STRUCTURES]
POOLED = "pooled"
PROXY_WINDOWS = tuple(SB_WINDOWS)
TAIL_PCT = 0.01
FULL_WIDTH_TOL = 0.98


def sleeve_name(u: str, s: str) -> str:
    return f"{u}-{s}"


def _graded(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty or "ror" not in df.columns:
        return pd.DataFrame(columns=["underlying", "structure", "entry", "expiry", "ror", "net_usd", "risk_usd", "window", "month"])
    return df[df["ror"].notna()]


def _pair(df: pd.DataFrame, u: str, s: str, window: str | None = None) -> pd.DataFrame:
    sub = _graded(df)
    sub = sub[(sub["underlying"] == u) & (sub["structure"] == s)]
    if window and window != POOLED and "window" in sub.columns:
        sub = sub[sub["window"] == window]
    return sub.sort_values("entry", kind="mergesort")


def _mean(sub: pd.DataFrame, col: str) -> float:
    return float(sub[col].mean()) if len(sub) and col in sub.columns else np.nan


def sleeve_block(sub: pd.DataFrame, u: str, s: str, window: str, lag: int = SB_NW_LAG) -> dict:
    nw = S.nw_t(sub["ror"], lag)
    cl = S.cluster_t(sub["ror"], sub["expiry"].astype(str)) if len(sub) else S.cluster_t([], [])
    return {"underlying": u, "structure": s, "sleeve": sleeve_name(u, s), "window": window, "n": nw["n"],
            "expiries": cl["G"], "mean_ror": nw["mean"], "median_ror": nw["median"], "hit": nw["hit"],
            "nw_t": nw["t"], "nw_p": nw["p"], "cl_t": cl["t"], "cl_p": cl["p"],
            "net_usd_total": float(sub["net_usd"].sum()) if len(sub) else 0.0,
            "mean_credit_over_width": _mean(sub, "credit_over_width"), "mean_cost_over_credit": _mean(sub, "cost_over_credit"),
            "mean_x": _mean(sub, "x"), "mean_risk_usd": _mean(sub, "risk_usd")}


def sleeve_table(df: pd.DataFrame, windows: tuple[str, ...] = PROXY_WINDOWS) -> pd.DataFrame:
    g = _graded(df)
    present = [w for w in windows if "window" in g.columns and (g["window"] == w).any()] + [POOLED]
    active = [(u, s) for u, s in SLEEVES if len(_pair(g, u, s))]
    rows = [sleeve_block(_pair(g, u, s, w), u, s, w) for w in present for u, s in active]
    return pd.DataFrame(rows)


def bh_table(df: pd.DataFrame, window: str = POOLED, fdr: float = BH_FDR) -> pd.DataFrame:
    tab = pd.DataFrame([sleeve_block(_pair(df, u, s, window), u, s, window) for u, s in SLEEVES])
    return tab.assign(bh_pass=S.bh_reject(tab["nw_p"].fillna(1.0).tolist(), fdr), fdr=fdr)


def dsr_table(df: pd.DataFrame, window: str = POOLED, n_trials: int = SB_DSR_TRIALS) -> pd.DataFrame:
    """Two benchmarks per sleeve. `sr_star` charges the empirical cross-sleeve variance of the
    Sharpe (the pre-registered reading, DESIGN/80 §6.3); `sr_star_null` charges the null sampling
    variance 1 / min(n) of a per-position Sharpe, reported beside it (DECISIONS D16): a
    hold-to-expiry spread's return on risk is bimodal, and a sleeve with no loss in its sample has
    a near-zero variance whose Sharpe says nothing about a null trial's dispersion; when the two
    disagree the read records both and the null benchmark governs."""
    series = {(u, s): _pair(df, u, s, window)["ror"].to_numpy() for u, s in SLEEVES}
    srs = [S.sharpe(x) for x in series.values() if len(x) > 2]
    var_sharpe = float(np.nanvar(srs, ddof=1)) if len(srs) > 1 else 0.0
    n_min = min((len(x) for x in series.values() if len(x) > 3), default=0)
    var_null = 1.0 / n_min if n_min else 0.0
    rows = []
    for (u, s), x in series.items():
        if len(x) <= 3:
            rows.append({"underlying": u, "structure": s, "sleeve": sleeve_name(u, s), "window": window, "n": len(x),
                         "deflated_sr": np.nan, "deflated_sr_null": np.nan})
            continue
        rep = S.deflated_sharpe(x, n_trials, var_sharpe)
        null = S.deflated_sharpe(x, n_trials, var_null)
        rows.append({"underlying": u, "structure": s, "sleeve": sleeve_name(u, s), "window": window, **rep,
                     "sr_star_null": null["sr_star"], "deflated_sr_null": null["deflated_sr"], "dsr_prob_null": null["dsr_prob"],
                     "var_null": var_null})
    return pd.DataFrame(rows)


def pbo_report(df: pd.DataFrame, n_blocks: int = SB_PBO_BLOCKS) -> dict:
    g = _graded(df)
    if g.empty:
        return {"pbo": np.nan, "note": "no positions"}
    mat = g.pivot_table(index="entry", columns=["underlying", "structure"], values="ror", aggfunc="mean")
    mat.columns = [sleeve_name(u, s) for u, s in mat.columns]
    mat = mat.fillna(0.0).sort_index()
    if mat.shape[1] < 2 or len(mat) < n_blocks:
        return {"pbo": np.nan, "n_configs": int(mat.shape[1]), "n_entries": int(len(mat)), "note": "too few entries"}
    blocks = np.floor(np.arange(len(mat)) * n_blocks / len(mat)).astype(int)
    return {**S.pbo(mat, blocks), "n_entries": int(len(mat))}


def monthly_table(df: pd.DataFrame, mult: float = SB_GO_MONTH_LOSS_MULT) -> pd.DataFrame:
    """Per sleeve: net $ by expiry month at the frozen sizing, the worst month against the median
    month, and the §6.7(3) rule (median must be positive; worst >= -mult x median)."""
    rows = []
    for u, s in SLEEVES:
        sub = _pair(df, u, s)
        if sub.empty:
            rows.append({"underlying": u, "structure": s, "sleeve": sleeve_name(u, s), "n_months": 0, "month_rule_pass": False})
            continue
        months = sub.groupby("month")["net_usd"].sum().sort_values()
        median = float(months.median())
        worst_month, worst = str(months.index[0]), float(months.iloc[0])
        ok = bool(median > 0 and worst >= -mult * median)
        rows.append({"underlying": u, "structure": s, "sleeve": sleeve_name(u, s), "n_months": int(len(months)),
                     "median_month_usd": median, "worst_month": worst_month, "worst_month_usd": worst,
                     "worst_over_median": float(-worst / median) if median > 0 else np.nan,
                     "months_negative": int((months < 0).sum()), "month_rule_pass": ok})
    return pd.DataFrame(rows)


def tail_report(df: pd.DataFrame, u: str, s: str, window: str = POOLED) -> dict:
    sub = _pair(df, u, s, window).sort_values("ror", kind="mergesort")
    if sub.empty:
        return {"underlying": u, "structure": s, "sleeve": sleeve_name(u, s), "n": 0}
    x = sub["ror"].to_numpy()
    k = max(1, int(round(TAIL_PCT * len(x))))
    losses = x[x < 0]
    decile = max(1, len(x) // 10)
    worst_share = float(x[:decile][x[:decile] < 0].sum() / losses.sum()) if losses.sum() < 0 else 0.0
    wins = x[x > 0]
    return {"underlying": u, "structure": s, "sleeve": sleeve_name(u, s), "n": len(x), "mean_ror": float(x.mean()),
            "worst_ror": float(x.min()), "worst_entry": str(sub["entry"].iloc[0]), "best_ror": float(x.max()),
            "mean_win_ror": float(wins.mean()) if len(wins) else np.nan,
            "worst_decile_share_of_loss": worst_share, "full_width_losses": int((x <= -FULL_WIDTH_TOL).sum()),
            "mean_without_worst_1pct": float(x[k:].mean()), "mean_without_best_1pct": float(x[:-k].mean()),
            "skew": float(pd.Series(x).skew()) if len(x) > 2 else np.nan, "kurt": float(pd.Series(x).kurt()) if len(x) > 3 else np.nan,
            "worst_10": sub.head(10)[["entry", "expiry", "x", "ror", "net_usd"]] if "x" in sub.columns else sub.head(10)}


def overlap_table(marked: pd.DataFrame, proxy: pd.DataFrame) -> pd.DataFrame:
    """§6.7(2): on the (entry, sleeve) positions both layers hold, the proxy's mean ROR may exceed
    the marked mean by at most the marked mean round-trip cost (as a fraction of risk)."""
    key = ["underlying", "structure", "entry"]
    m, p = _graded(marked), _graded(proxy)
    rows = []
    for u, s in SLEEVES:
        mm, pp = m[(m.underlying == u) & (m.structure == s)], p[(p.underlying == u) & (p.structure == s)]
        both = mm.merge(pp[key + ["ror"]], on=key, how="inner", suffixes=("", "_proxy")) if len(mm) and len(pp) else pd.DataFrame()
        n = int(len(both))
        if n == 0:
            rows.append({"underlying": u, "structure": s, "sleeve": sleeve_name(u, s), "n_marked": int(len(mm)), "n_overlap": 0,
                         "marked_mean_ror": _mean(mm, "ror"), "proxy_mean_ror": np.nan, "gap_ror": np.nan,
                         "marked_cost_ror": np.nan, "overlap_pass": False})
            continue
        marked_mean, proxy_mean = float(both["ror"].mean()), float(both["ror_proxy"].mean())
        cost = float((both["cost_usd"] / both["risk_usd"]).mean()) if "cost_usd" in both.columns else np.nan
        gap = proxy_mean - marked_mean
        rows.append({"underlying": u, "structure": s, "sleeve": sleeve_name(u, s), "n_marked": int(len(mm)), "n_overlap": n,
                     "marked_mean_ror": marked_mean, "proxy_mean_ror": proxy_mean, "gap_ror": gap, "marked_cost_ror": cost,
                     "overlap_pass": bool(marked_mean > 0 and np.isfinite(cost) and gap <= cost)})
    return pd.DataFrame(rows)


def gate_table(sens: pd.DataFrame, lag: int = SB_NW_LAG) -> pd.DataFrame:
    """Descriptive: each gate mode / sensitivity beside the base, per sleeve (pooled)."""
    rows = []
    col = "sensitivity" if "sensitivity" in sens.columns else "gate_mode"
    for name, g in sens.groupby(col, sort=False):
        for u, s in SLEEVES:
            rows.append({"sensitivity": name, **sleeve_block(_pair(g, u, s), u, s, POOLED, lag)})
    return pd.DataFrame(rows)


def _criteria(proxy: pd.DataFrame, marked: pd.DataFrame, forward: pd.DataFrame, u: str, s: str,
              bh: pd.DataFrame, dsr: pd.DataFrame, months: pd.DataFrame, overlap: pd.DataFrame) -> dict:
    pooled = sleeve_block(_pair(proxy, u, s), u, s, POOLED)
    per_window = {w: sleeve_block(_pair(proxy, u, s, w), u, s, w) for w in PROXY_WINDOWS}
    pick = lambda tab: tab[(tab.underlying == u) & (tab.structure == s)].iloc[0]  # noqa: E731
    bh_pass = bool(pick(bh)["bh_pass"])
    signs_ok = all(per_window[w]["n"] > 0 and per_window[w]["mean_ror"] > 0 for w in PROXY_WINDOWS)
    c1 = bool(pooled["n"] and pooled["mean_ror"] > 0 and pooled["nw_t"] >= SB_GO_T_MIN and bh_pass and signs_ok)
    ov = pick(overlap)
    marked_all = _pair(marked, u, s)
    c2 = bool(len(marked_all) and marked_all["ror"].mean() > 0 and ov["overlap_pass"])
    c3 = bool(pick(months)["month_rule_pass"])
    d = pick(dsr)
    c4 = bool(np.isfinite(d.get("deflated_sr", np.nan)) and d["deflated_sr"] > 0)              # the pre-registered estimator
    c4_null = bool(np.isfinite(d.get("deflated_sr_null", np.nan)) and d["deflated_sr_null"] > 0)  # companion (D16)
    fwd = _pair(forward, u, s)
    c5 = bool(len(fwd) >= SB_SCALE_MIN_POSITIONS and fwd["ror"].mean() > 0)
    return {"underlying": u, "structure": s, "sleeve": sleeve_name(u, s), "n_proxy": pooled["n"], "mean_proxy": pooled["mean_ror"],
            "nw_t_proxy": pooled["nw_t"], "bh_pass": bh_pass,
            **{f"mean_{w.lower()}": per_window[w]["mean_ror"] for w in PROXY_WINDOWS},
            "n_marked": int(len(marked_all)), "mean_marked": float(marked_all["ror"].mean()) if len(marked_all) else np.nan,
            "gap_ror": ov["gap_ror"], "worst_over_median": pick(months).get("worst_over_median", np.nan),
            "deflated_sr": d.get("deflated_sr", np.nan), "deflated_sr_null": d.get("deflated_sr_null", np.nan), "forward_n": int(len(fwd)),
            "c1_proxy": c1, "c2_marked": c2, "c3_month": c3, "c4_dsr": c4, "c4_dsr_null": c4_null, "c5_scale": c5}


def go_no_go(proxy: pd.DataFrame, marked: pd.DataFrame, forward: pd.DataFrame | None = None) -> pd.DataFrame:
    """The §6.7 bar per sleeve. GO-MIN: criteria 1-4 clear (launch at one contract); GO-SCALE:
    also 5; NO-GO otherwise; NOT YET when the proxy holds no positions for the sleeve."""
    forward = forward if forward is not None else pd.DataFrame()
    bh, dsr, months, overlap = bh_table(proxy), dsr_table(proxy), monthly_table(proxy), overlap_table(marked, proxy)
    rows = []
    for u, s in SLEEVES:
        c = _criteria(proxy, marked, forward, u, s, bh, dsr, months, overlap)
        core = c["c1_proxy"] and c["c2_marked"] and c["c3_month"] and c["c4_dsr"]
        if c["n_proxy"] == 0:
            verdict, note = "NOT YET", "no proxy positions for the sleeve"
        elif core and c["c5_scale"]:
            verdict, note = "GO-SCALE", "clears 1-4 and the forward count trigger"
        elif core:
            verdict, note = "GO-MIN", f"clears 1-4; one contract until the forward ledger holds >= {SB_SCALE_MIN_POSITIONS} graded positions (now {c['forward_n']})"
        else:
            verdict, note = "NO-GO", "fails " + ", ".join(k for k in ("c1_proxy", "c2_marked", "c3_month", "c4_dsr") if not c[k])
        rows.append({**c, "verdict": verdict, "note": note})
    return pd.DataFrame(rows)


def md(tab: pd.DataFrame, cols: list[str] | None = None, pct_cols: tuple[str, ...] = ()) -> str:
    from engine.validation.harness import md as _md
    return _md(tab, cols, pct_cols)
