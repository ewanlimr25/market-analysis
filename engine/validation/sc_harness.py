"""Validation harness for S-C (DESIGN/90 §6): entry-week aggregation, Newey-West lag 4, BH across the
four (variant, structure) pairs, the six-trial deflated Sharpe, PBO, the month rule, the tail, the
descriptive strata, the count-trigger status and the go / no-go.

The unit is the **entry week**: a pair's weekly series is the mean net return on risk of the positions
entered that week (§6 "averaged within entry week and then across weeks"). Frames are position rows
(`backtest_sc` trades, or the forward ledger) with `variant, structure, entry, expiry, ror, net_usd,
risk_usd, entry_cost_usd`. In-sample is window M; forward rows are labelled by calendar quarter.
Every selected structure is read; `cap_pass` is never a filter here.
"""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

from engine.config import (BH_FDR, SC_DSR_TRIALS, SC_GO_MONTH_LOSS_MULT, SC_GO_T_MIN, SC_NW_LAG, SC_PBO_BLOCKS,
                           SC_READ_MIN_WEEKS, SC_SCALE_MIN_WEEKS, SC_PARAMS, SC_STRUCTURES, SC_VARIANTS)
from engine.validation import stats as S

PAIRS = [(v, s) for v in SC_VARIANTS for s in SC_STRUCTURES]
WINDOW_M, POOLED = "M", "pooled"
NOT_DUE, DUE = "NOT DUE", "DUE"
GO_MIN, GO_SCALE, NO_GO = "GO-MIN", "GO-SCALE", "NO-GO"
TAIL_PCT = 0.01
TERCILES = ("T1", "T2", "T3")
TERCILE_STRATA = {"cap_tercile": "marketcap", "iv_tercile": "iv30d"}
CORE = ("c1_forward", "c2_pooled", "c3_month", "c4_dsr_null")


def pair_name(v: str, s: str) -> str:
    return f"{v}-{s}"


def forward_window(entry: date) -> str:
    return f"F-{entry.year}Q{(entry.month - 1) // 3 + 1}"


def graded(df: pd.DataFrame | None) -> pd.DataFrame:
    if df is None or df.empty or "ror" not in df.columns:
        return pd.DataFrame(columns=["variant", "structure", "entry", "expiry", "ror", "net_usd", "risk_usd"])
    return df[df["ror"].notna()]


def _pair(df: pd.DataFrame, v: str, s: str) -> pd.DataFrame:
    g = graded(df)
    return g[(g["variant"] == v) & (g["structure"] == s)].sort_values(["entry", "ticker"] if "ticker" in g.columns else ["entry"], kind="mergesort")


def weekly(df: pd.DataFrame, v: str, s: str) -> pd.Series:
    """The pair's entry-week series: mean `ror` of the week's positions, in entry order."""
    sub = _pair(df, v, s)
    return sub.groupby("entry")["ror"].mean().sort_index() if len(sub) else pd.Series(dtype=float)


def _cost_ror(sub: pd.DataFrame) -> float:
    if sub.empty or "entry_cost_usd" not in sub.columns:
        return np.nan
    return float((sub["entry_cost_usd"] / sub["risk_usd"]).mean())


def pair_block(df: pd.DataFrame, v: str, s: str, window: str, lag: int = SC_NW_LAG) -> dict:
    sub, wk = _pair(df, v, s), weekly(df, v, s)
    nw = S.nw_t(wk.to_numpy(), lag)
    return {"variant": v, "structure": s, "pair": pair_name(v, s), "window": window, "n": int(len(sub)),
            "weeks": int(len(wk)), "mean_ror": nw["mean"], "median_ror": nw["median"], "hit": nw["hit"],
            "nw_t": nw["t"], "nw_p": nw["p"], "net_usd_total": float(sub["net_usd"].sum()) if len(sub) else 0.0,
            "mean_cost_ror": _cost_ror(sub)}


def pair_table(insample: pd.DataFrame, forward: pd.DataFrame | None = None) -> pd.DataFrame:
    """Per pair: M, each forward quarter, forward pooled (F) and M + F pooled."""
    fwd = graded(forward)
    frames = [(WINDOW_M, graded(insample))]
    if len(fwd):
        q = fwd.assign(window=fwd["entry"].map(forward_window))
        frames += [(w, g) for w, g in q.groupby("window", sort=True)] + [("F", fwd)]
    frames.append((POOLED, pooled(insample, forward)))
    return pd.DataFrame([pair_block(g, v, s, w) for w, g in frames for v, s in PAIRS if len(_pair(g, v, s))])


def pooled(insample: pd.DataFrame, forward: pd.DataFrame | None) -> pd.DataFrame:
    parts = [p for p in (graded(insample), graded(forward)) if len(p)]
    return pd.concat(parts, ignore_index=True) if parts else graded(None)


def bh_table(df: pd.DataFrame, window: str = POOLED, fdr: float = BH_FDR) -> pd.DataFrame:
    tab = pd.DataFrame([pair_block(df, v, s, window) for v, s in PAIRS])
    return tab.assign(bh_pass=S.bh_reject(tab["nw_p"].fillna(1.0).tolist(), fdr), fdr=fdr)


def dsr_table(df: pd.DataFrame, window: str = POOLED, n_trials: int = SC_DSR_TRIALS) -> pd.DataFrame:
    """On the weekly series. `sr_star` charges the empirical cross-pair Sharpe variance (as written);
    `sr_star_null` the null variance 1 / min(weeks) -- S-B's D16 companion, which governs when the
    two disagree (a hold-to-expiry return on risk is bimodal, as S-B's is)."""
    series = {(v, s): weekly(df, v, s).to_numpy() for v, s in PAIRS}
    srs = [S.sharpe(x) for x in series.values() if len(x) > 2]
    var_emp = float(np.nanvar(srs, ddof=1)) if len(srs) > 1 else 0.0
    n_min = min((len(x) for x in series.values() if len(x) > 3), default=0)
    var_null = 1.0 / n_min if n_min else 0.0
    rows = []
    for (v, s), x in series.items():
        base = {"variant": v, "structure": s, "pair": pair_name(v, s), "window": window, "n_trials": n_trials}
        if len(x) <= 3:
            rows.append({**base, "n": len(x), "deflated_sr": np.nan, "deflated_sr_null": np.nan})
            continue
        emp, null = S.deflated_sharpe(x, n_trials, var_emp), S.deflated_sharpe(x, n_trials, var_null)
        rows.append({**base, **{k: emp[k] for k in ("n", "sr", "sr_star", "deflated_sr", "dsr_prob", "skew", "kurt")},
                     "sr_star_null": null["sr_star"], "deflated_sr_null": null["deflated_sr"], "dsr_prob_null": null["dsr_prob"]})
    return pd.DataFrame(rows)


def pbo_report(df: pd.DataFrame, n_blocks: int = SC_PBO_BLOCKS) -> dict:
    """CSCV over entry-week blocks across the four pairs (descriptive; not a §6 criterion)."""
    mat = pd.DataFrame({pair_name(v, s): weekly(df, v, s) for v, s in PAIRS}).sort_index()
    mat = mat.dropna(how="all").fillna(0.0)
    if mat.shape[1] < 2 or len(mat) < n_blocks:
        return {"pbo": np.nan, "n_blocks": n_blocks, "n_weeks": int(len(mat)), "note": "too few entry weeks"}
    blocks = np.floor(np.arange(len(mat)) * n_blocks / len(mat)).astype(int)
    return {**S.pbo(mat, blocks), "n_weeks": int(len(mat))}


def month_table(df: pd.DataFrame, mult: float = SC_GO_MONTH_LOSS_MULT) -> pd.DataFrame:
    """Net $ by expiry calendar month per pair: the worst month must be >= -mult x the median month,
    and a non-positive median fails (§6 tail / criterion 3)."""
    rows = []
    for v, s in PAIRS:
        sub = _pair(df, v, s)
        base = {"variant": v, "structure": s, "pair": pair_name(v, s)}
        if sub.empty:
            rows.append({**base, "n_months": 0, "month_rule_pass": False})
            continue
        months = sub.groupby(sub["expiry"].map(lambda d: f"{d.year}-{d.month:02d}"))["net_usd"].sum().sort_values()
        median, worst = float(months.median()), float(months.iloc[0])
        rows.append({**base, "n_months": int(len(months)), "median_month_usd": median, "worst_month": str(months.index[0]),
                     "worst_month_usd": worst, "worst_over_median": float(-worst / median) if median > 0 else np.nan,
                     "months_negative": int((months < 0).sum()), "month_rule_pass": bool(median > 0 and worst >= -mult * median)})
    return pd.DataFrame(rows)


def tail_report(df: pd.DataFrame, v: str, s: str) -> dict:
    sub = _pair(df, v, s).sort_values("ror", kind="mergesort")
    if sub.empty:
        return {"pair": pair_name(v, s), "n": 0}
    x = sub["ror"].to_numpy()
    k = max(1, int(round(TAIL_PCT * len(x))))
    decile, losses = max(1, len(x) // 10), x[x < 0]
    worst_share = float(x[:decile][x[:decile] < 0].sum() / losses.sum()) if losses.sum() < 0 else 0.0
    moved = (sub["settle_close"] - sub["close"]).abs() if {"settle_close", "close"} <= set(sub.columns) else pd.Series(dtype=float)
    stress = int((moved >= SC_PARAMS.stress_sigma * sub["sigma_hold"]).sum()) if len(moved) else 0
    cols = [c for c in ("ticker", "entry", "expiry", "ror", "net_usd") if c in sub.columns]
    return {"pair": pair_name(v, s), "n": int(len(x)), "mean_ror": float(x.mean()), "worst_ror": float(x.min()),
            "best_ror": float(x.max()), "worst_decile_share_of_loss": worst_share, "realized_stress": stress,
            "mean_without_worst_1pct": float(x[k:].mean()), "skew": float(pd.Series(x).skew()) if len(x) > 2 else np.nan,
            "worst_10": sub.head(10)[cols]}


def _stratum(df: pd.DataFrame, name: str) -> pd.Series:
    if name in TERCILE_STRATA:
        col = TERCILE_STRATA[name]
        return pd.qcut(df[col].rank(method="first"), 3, labels=list(TERCILES)).astype(str)
    if name == "month":
        return df["entry"].map(lambda d: f"{d.year}-{d.month:02d}")
    return df[name].astype(str)


def strata_table(df: pd.DataFrame, name: str) -> pd.DataFrame:
    """Descriptive only (§6 windows): per pair and stratum, positions, weeks, mean ror. Cannot promote."""
    g = graded(df)
    if g.empty or (name not in g.columns and TERCILE_STRATA.get(name) not in g.columns and name != "month"):
        return pd.DataFrame(columns=["pair", "stratum", "n", "weeks", "mean_ror"])
    g = g.assign(stratum=_stratum(g, name))
    rows = [{"pair": pair_name(v, s), "stratum": st, "n": int(len(sub)), "weeks": int(sub["entry"].nunique()),
             "mean_ror": float(sub["ror"].mean())}
            for v, s in PAIRS for st, sub in g[(g["variant"] == v) & (g["structure"] == s)].groupby("stratum", sort=True)]
    return pd.DataFrame(rows)


def count_status(forward: pd.DataFrame | None) -> pd.DataFrame:
    rows = []
    for v, s in PAIRS:
        n = int(len(weekly(forward if forward is not None else graded(None), v, s)))
        rows.append({"variant": v, "structure": s, "pair": pair_name(v, s), "forward_weeks": n,
                     "required": SC_READ_MIN_WEEKS, "status": DUE if n >= SC_READ_MIN_WEEKS else NOT_DUE,
                     "scale_required": SC_SCALE_MIN_WEEKS})
    return pd.DataFrame(rows)


def _criteria(insample: pd.DataFrame, forward: pd.DataFrame, v: str, s: str, bh_fwd: pd.DataFrame,
              dsr: pd.DataFrame, months: pd.DataFrame) -> dict:
    f, m, p = pair_block(forward, v, s, "F"), pair_block(insample, v, s, WINDOW_M), pair_block(pooled(insample, forward), v, s, POOLED)
    pick = lambda tab: tab.set_index("pair").loc[pair_name(v, s)]  # noqa: E731
    d = pick(dsr)
    cost = p["mean_cost_ror"]
    return {"variant": v, "structure": s, "pair": pair_name(v, s), "forward_weeks": f["weeks"], "mean_f": f["mean_ror"],
            "nw_t_f": f["nw_t"], "mean_m": m["mean_ror"], "mean_pooled": p["mean_ror"], "cost_ror": cost,
            "worst_over_median": pick(months).get("worst_over_median", np.nan),
            "deflated_sr": d.get("deflated_sr", np.nan), "deflated_sr_null": d.get("deflated_sr_null", np.nan),
            "c1_forward": bool(f["weeks"] and f["mean_ror"] > 0 and f["nw_t"] >= SC_GO_T_MIN and pick(bh_fwd)["bh_pass"]),
            "c2_pooled": bool(p["mean_ror"] > 0 and np.isfinite(cost) and (m["mean_ror"] - f["mean_ror"]) <= cost),
            "c3_month": bool(pick(months)["month_rule_pass"]),
            "c4_dsr": bool(np.isfinite(d.get("deflated_sr", np.nan)) and d["deflated_sr"] > 0),
            "c4_dsr_null": bool(np.isfinite(d.get("deflated_sr_null", np.nan)) and d["deflated_sr_null"] > 0),
            "c5_scale": bool(f["weeks"] >= SC_SCALE_MIN_WEEKS and f["mean_ror"] > 0)}


def go_no_go(insample: pd.DataFrame, forward: pd.DataFrame | None) -> pd.DataFrame:
    """§6 per pair. NOT DUE until the forward ledger holds SC_READ_MIN_WEEKS graded entry-weeks; then
    GO-MIN (1-4 clear), GO-SCALE (also 5) or NO-GO. Criterion 4 is read on the null benchmark (D16)."""
    fwd = graded(forward)
    status = count_status(fwd).set_index("pair")
    if (status["status"] == NOT_DUE).all():
        return status.reset_index().assign(verdict=NOT_DUE, note=lambda t: t["forward_weeks"].map(
            lambda n: f"{n} of {SC_READ_MIN_WEEKS} graded forward entry-weeks"))
    pool = pooled(insample, fwd)
    bh_fwd, dsr, months = bh_table(fwd, "F"), dsr_table(pool), month_table(pool)
    rows = []
    for v, s in PAIRS:
        c = _criteria(insample, fwd, v, s, bh_fwd, dsr, months)
        if c["forward_weeks"] < SC_READ_MIN_WEEKS:
            verdict, note = NOT_DUE, f"{c['forward_weeks']} of {SC_READ_MIN_WEEKS} graded forward entry-weeks"
        elif all(c[k] for k in CORE):
            verdict = GO_SCALE if c["c5_scale"] else GO_MIN
            note = "clears 1-4 and the scale trigger" if c["c5_scale"] else f"clears 1-4; one contract until {SC_SCALE_MIN_WEEKS} forward weeks"
        else:
            verdict, note = NO_GO, "fails " + ", ".join(k for k in CORE if not c[k])
        rows.append({**c, "verdict": verdict, "note": note})
    return pd.DataFrame(rows)


def md(tab: pd.DataFrame, cols: list[str] | None = None, pct_cols: tuple[str, ...] = ()) -> str:
    from engine.validation.harness import md as _md
    return _md(tab, cols, pct_cols)
