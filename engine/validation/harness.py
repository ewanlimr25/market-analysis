"""Validation harness for S-A (DESIGN/70 §4): season split, clustered t by print date, BH across
the four primary tests, deflated Sharpe at the six-trial charge, PBO, tail and robustness
reports, the go/no-go verdict, and the §4.3 reproduction of E1's proxy.

Every function takes the trades frame (one row per event x variant x structure) and returns a
DataFrame or dict; `md` renders a frame as a markdown table for the write-up.
"""
from __future__ import annotations

from datetime import date
from typing import Callable

import numpy as np
import pandas as pd

from engine.config import (BH_FDR, DSR_TRIALS, GO_MIN_EVENTS, GO_T_MIN, GO_WORST_TO_MEAN_WIN_MAX,
                           SA_PARAMS, SEASONS, SAParams)
from engine.validation import stats as S

PAIRS = [(v, s) for v in ("A1", "A2") for s in ("SS", "IC")]
POOLED = "pooled"
TAIL_PCT = 0.01
PRIMARY_SEASONS = ("S1", "S2", "S3")
RerunFn = Callable[[SAParams, float], pd.DataFrame]


def season_of(pre: date) -> str:
    for name, (lo, hi) in SEASONS.items():
        if lo <= pre <= hi:
            return name
    return "off"


def _pair(trades: pd.DataFrame, variant: str, structure: str, season: str | None) -> pd.DataFrame:
    sub = trades[(trades.variant == variant) & (trades.structure == structure)]
    if season and season != POOLED:
        sub = sub[sub.season == season]
    return sub


def _block(sub: pd.DataFrame, variant: str, structure: str, season: str) -> dict:
    ct = S.cluster_t(sub.net_pct, sub.pre)
    return {"variant": variant, "structure": structure, "season": season, "n": ct["n"], "dates": ct["G"],
            "mean_net_pct": ct["mean"], "median_net_pct": ct["median"], "hit": ct["hit"], "se": ct["se"],
            "t": ct["t"], "p": ct["p"],
            "mean_gross_pct": float(sub.gross_pct.mean()) if len(sub) else np.nan,
            "mean_cost_pct": float(sub.cost_pct.mean()) if len(sub) else np.nan,
            "straddle_over_implied": float(sub.straddle_over_implied.mean()) if len(sub) else np.nan,
            "net_usd_total": float(sub.net_usd.sum()) if len(sub) else 0.0}


def primary_table(trades: pd.DataFrame, seasons: tuple[str, ...] = PRIMARY_SEASONS) -> pd.DataFrame:
    present = [s for s in seasons if (trades.season == s).any()] + [POOLED]
    rows = [_block(_pair(trades, v, s, sea), v, s, sea) for sea in present for v, s in PAIRS]
    return pd.DataFrame(rows)


def bh_table(trades: pd.DataFrame, season: str, fdr: float = BH_FDR) -> pd.DataFrame:
    rows = [_block(_pair(trades, v, s, season), v, s, season) for v, s in PAIRS]
    tab = pd.DataFrame(rows)
    pvals = tab.p.fillna(1.0).tolist()
    return tab.assign(bh_pass=S.bh_reject(pvals, fdr), fdr=fdr)


def dsr_table(trades: pd.DataFrame, season: str, n_trials: int = DSR_TRIALS) -> pd.DataFrame:
    series = {(v, s): _pair(trades, v, s, season).net_pct.to_numpy() for v, s in PAIRS}
    srs = [S.sharpe(x) for x in series.values() if len(x) > 2]
    var_sharpe = float(np.nanvar(srs, ddof=1)) if len(srs) > 1 else 0.0
    rows = []
    for (v, s), x in series.items():
        rep = S.deflated_sharpe(x, n_trials, var_sharpe) if len(x) > 3 else {"n": len(x)}
        rows.append({"variant": v, "structure": s, "season": season, **rep})
    return pd.DataFrame(rows)


def _daily_config_pnl(trades: pd.DataFrame, season: str) -> pd.DataFrame:
    sub = trades[trades.season == season] if season != POOLED else trades
    daily = sub.groupby(["pre", "variant", "structure"]).net_pct.mean().unstack(["variant", "structure"])
    daily.columns = [f"{v}-{s}" for v, s in daily.columns]
    return daily.fillna(0.0).sort_index()


def pbo_report(trades: pd.DataFrame, season: str, n_blocks: int = 16) -> dict:
    daily = _daily_config_pnl(trades, season)
    if daily.shape[1] < 2 or len(daily) < n_blocks:
        return {"pbo": np.nan, "n_configs": int(daily.shape[1]), "n_dates": int(len(daily)), "note": "too few dates"}
    blocks = np.floor(np.arange(len(daily)) * n_blocks / len(daily)).astype(int)
    return {**S.pbo(daily, blocks), "n_dates": int(len(daily))}


def tail_report(trades: pd.DataFrame, variant: str, structure: str, season: str) -> dict:
    sub = _pair(trades, variant, structure, season).sort_values("net_pct")
    if sub.empty:
        return {"variant": variant, "structure": structure, "season": season, "n": 0}
    x = sub.net_pct.to_numpy()
    k = max(1, int(round(TAIL_PCT * len(x))))
    losses = x[x < 0]
    decile = max(1, len(x) // 10)
    worst_share = float(x[:decile][x[:decile] < 0].sum() / losses.sum()) if losses.sum() < 0 else 0.0
    wins = x[x > 0]
    risk_col = "stress_loss_usd" if structure == "SS" else "max_loss_usd"
    breaches = int((sub.net_usd <= -sub[risk_col] * sub.contracts).sum()) if risk_col in sub else 0
    return {"variant": variant, "structure": structure, "season": season, "n": len(x),
            "mean_net_pct": float(x.mean()), "worst_event_pct": float(x.min()), "best_event_pct": float(x.max()),
            "mean_win_pct": float(wins.mean()) if len(wins) else np.nan,
            "worst_to_mean_win": float(-x.min() / wins.mean()) if len(wins) and x.min() < 0 else np.nan,
            "worst_decile_share_of_loss": worst_share,
            "mean_without_worst_1pct": float(x[k:].mean()), "mean_without_best_1pct": float(x[:-k].mean()),
            "skew": float(pd.Series(x).skew()), "kurt": float(pd.Series(x).kurt()),
            "stress_breaches": breaches,
            "worst_10": sub.head(10)[["ticker", "E", "pre", "implied", "realized_move", "net_pct", "net_usd"]
                                     if "realized_move" in sub else ["ticker", "E", "pre", "net_pct"]]}


def _with_costs(trades: pd.DataFrame, mult: float) -> pd.DataFrame:
    net_usd = trades.gross_usd - mult * trades.cost_usd
    return trades.assign(net_usd=net_usd, net_pct=net_usd / trades.notional_usd, cost_pct=mult * trades.cost_pct)


def robustness_table(trades: pd.DataFrame, season: str, rerun: RerunFn | None,
                     base_params: SAParams = SA_PARAMS) -> pd.DataFrame:
    """Sensitivities (descriptive, never promotional): model exits removed, costs doubled, and,
    when a `rerun(params, cost_mult)` callable is given, the spread filter at 7.5% / 12.5% and
    F3 widened to $1B–$100B."""
    variants = {"base": trades, "no_model_exit": trades[~trades.model_exit.astype(bool)],
                "costs_x2": _with_costs(trades, 2.0)}
    if rerun is not None:
        p = base_params.__dict__
        variants["spread_7.5pct"] = rerun(SAParams(**{**p, "spread_max": 0.075}), 1.0)
        variants["spread_12.5pct"] = rerun(SAParams(**{**p, "spread_max": 0.125}), 1.0)
        variants["mcap_1B_100B"] = rerun(SAParams(**{**p, "mcap_min": 1e9, "mcap_max": 100e9}), 1.0)
    rows = []
    for name, t in variants.items():
        for v, s in PAIRS:
            rows.append({"sensitivity": name, **_block(_pair(t, v, s, season), v, s, season)})
    return pd.DataFrame(rows)


def _criteria(trades: pd.DataFrame, variant: str, structure: str, bh_pass: bool, dsr_row: pd.Series | None) -> dict:
    s3 = _block(_pair(trades, variant, structure, "S3"), variant, structure, "S3")
    s1 = _block(_pair(trades, variant, structure, "S1"), variant, structure, "S1")
    s2 = _block(_pair(trades, variant, structure, "S2"), variant, structure, "S2")
    tail = tail_report(trades, variant, structure, "S3")
    c1 = bool(s3["n"] and s3["mean_net_pct"] > 0 and s3["t"] >= GO_T_MIN and bh_pass)
    c2 = bool(s1["n"] and s2["n"] and s1["mean_net_pct"] > 0 and s2["mean_net_pct"] > 0)
    c3 = bool(dsr_row is not None and np.isfinite(dsr_row.get("deflated_sr", np.nan)) and dsr_row["deflated_sr"] > 0)
    c4 = bool(s3["n"] and np.isfinite(tail.get("worst_to_mean_win", np.nan)) and tail["worst_to_mean_win"] <= GO_WORST_TO_MEAN_WIN_MAX)
    c5 = bool(s3["n"] >= GO_MIN_EVENTS)
    return {"variant": variant, "structure": structure, "n_s3": s3["n"], "mean_s3": s3["mean_net_pct"], "t_s3": s3["t"],
            "c1_t_and_bh": c1, "c2_sign_s1_s2": c2, "c3_dsr_positive": c3, "c4_tail": c4, "c5_n60": c5,
            "mean_s1": s1["mean_net_pct"], "mean_s2": s2["mean_net_pct"]}


def go_no_go(trades: pd.DataFrame) -> pd.DataFrame:
    """The §4.2 bar, applied to Season 3 alone. Verdict per (variant, structure)."""
    has_s3 = (trades.season == "S3").any()
    bh = bh_table(trades, "S3") if has_s3 else None
    dsr = dsr_table(trades, "S3") if has_s3 else None
    rows = []
    for v, s in PAIRS:
        bh_pass = bool(bh[(bh.variant == v) & (bh.structure == s)].bh_pass.iloc[0]) if has_s3 else False
        dsr_row = dsr[(dsr.variant == v) & (dsr.structure == s)].iloc[0] if has_s3 else None
        c = _criteria(trades, v, s, bh_pass, dsr_row)
        core = c["c1_t_and_bh"] and c["c2_sign_s1_s2"] and c["c3_dsr_positive"] and c["c4_tail"]
        if not has_s3 or c["n_s3"] == 0:
            verdict, note = "NOT YET", "Season 3 has no traded events yet; the bar is read on 2026-12-01"
        elif core and c["c5_n60"]:
            verdict, note = "GO", "clears all five criteria on Season 3"
        elif core:
            verdict, note = "PROVISIONAL", f"clears 1-4; re-evaluate at the first cycle at which N >= {GO_MIN_EVENTS} (now {c['n_s3']})"
        else:
            verdict, note = "NO-GO", "fails " + ", ".join(k for k in ("c1_t_and_bh", "c2_sign_s1_s2", "c3_dsr_positive", "c4_tail") if not c[k])
        rows.append({**c, "verdict": verdict, "note": note})
    return pd.DataFrame(rows)


def reproduce_e1(events: pd.DataFrame, reference: dict, tol_mean: float = 5e-6, tol_t: float = 0.02) -> dict:
    """§4.3: recompute E1's headline (N, mean implied-minus-realized, t clustered by pre)."""
    ct = S.cluster_t(events.proxy_pnl, events.pre)
    return {"n": ct["n"], "dates": ct["G"], "mean": ct["mean"], "t": ct["t"],
            "ref_n": reference["n"], "ref_mean": reference["mean"], "ref_t": reference["t"],
            "n_match": ct["n"] == reference["n"], "mean_match": abs(ct["mean"] - reference["mean"]) <= tol_mean,
            "t_match": abs(ct["t"] - reference["t"]) <= tol_t}


def _fmt(v) -> str:
    if isinstance(v, (bool, np.bool_)):
        return "yes" if v else "no"
    if isinstance(v, (float, np.floating)):
        if not np.isfinite(v):
            return "—"
        return f"{v:.4f}" if abs(v) < 1 else (f"{v:,.0f}" if abs(v) >= 1000 else f"{v:.2f}")
    return str(v)


def md(tab: pd.DataFrame, cols: list[str] | None = None, pct_cols: tuple[str, ...] = ()) -> str:
    cols = cols or [c for c in tab.columns if not isinstance(tab[c].iloc[0] if len(tab) else None, pd.DataFrame)]
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for r in tab[cols].itertuples(index=False):
        cells = [f"{100 * v:+.2f}%" if c in pct_cols and isinstance(v, (float, np.floating)) and np.isfinite(v) else _fmt(v)
                 for c, v in zip(cols, r)]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)
