"""S-G validation harness (DESIGN/91 §4): season split, clustered t by entry day, BH across the
four primary tests, deflated Sharpe at the ten-trial charge, PBO, tail, spread halves, the gross
ramp decomposition summary, and the go/no-go bar. Reuses `engine.validation.harness`'s generic
`_block`/`primary_table`/`bh_table`/`dsr_table`/`pbo_report`/`tail_report`/`md` by import, passing
`pairs=SG_PAIRS` and `cluster_col="entry_day"` (the two hooks DESIGN/91 §6 added to `harness.py`
so S-A's code is not copied).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from engine.config import SG_BH_FDR, SG_DSR_TRIALS, SG_GO_T_MIN, SG_PBO_BLOCKS
from engine.validation import harness as H

SG_PAIRS = [(f"G3_{o}", s) for o in (3, 5) for s in ("LS", "LG")]
CLUSTER_COL = "entry_day"


def primary_table(trades: pd.DataFrame) -> pd.DataFrame:
    return H.primary_table(trades, seasons=("S1", "S2"), pairs=SG_PAIRS, cluster_col=CLUSTER_COL)


def bh_table(trades: pd.DataFrame, season: str) -> pd.DataFrame:
    return H.bh_table(trades, season, fdr=SG_BH_FDR, pairs=SG_PAIRS, cluster_col=CLUSTER_COL)


def dsr_table(trades: pd.DataFrame, season: str) -> pd.DataFrame:
    return H.dsr_table(trades, season, n_trials=SG_DSR_TRIALS, pairs=SG_PAIRS)


def pbo_report(trades: pd.DataFrame, season: str = H.POOLED) -> dict:
    return H.pbo_report(trades, season, n_blocks=SG_PBO_BLOCKS, cluster_col=CLUSTER_COL)


def tail_report(trades: pd.DataFrame, variant: str, structure: str, season: str) -> dict:
    return H.tail_report(trades, variant, structure, season)


def spread_median(ls_trades: pd.DataFrame) -> float:
    """Pooled median of `atm_spread_entry` over the G3a-LS population (DESIGN/91 §4)."""
    sub = ls_trades[(ls_trades.variant == "G3_3") & (ls_trades.structure == "LS")]
    return float(sub.atm_spread_entry.median()) if len(sub) else float("nan")


def spread_half_table(trades: pd.DataFrame, median: float) -> pd.DataFrame:
    """Season table split at the pooled G3a-LS spread median, per (variant, structure, half)."""
    rows = []
    for half, mask in (("low", trades.atm_spread_entry <= median), ("wide", trades.atm_spread_entry > median)):
        sub_all = trades[mask]
        for v, s in SG_PAIRS:
            sub = H._pair(sub_all, v, s, H.POOLED)
            rows.append({"half": half, **H._block(sub, v, s, H.POOLED, CLUSTER_COL)})
    return pd.DataFrame(rows)


def decomposition_summary(trades: pd.DataFrame, group_cols: tuple[str, ...] = ("season",)) -> pd.DataFrame:
    """Mean gross (unhedged), delta, delta-hedged (~vega+residual) and vega components, by the
    given grouping (season, spread half, ...), for the primary G3a-LS population."""
    ls = trades[(trades.variant == "G3_3") & (trades.structure == "LS")].copy()
    if ls.empty:
        return pd.DataFrame()
    cols = ["unhedged_pnl_pct", "delta_pnl_pct", "delta_hedged_pnl_pct", "vega_pnl_pct", "residual_pnl_pct",
           "net_pct", "net_pct_prem"]
    return ls.groupby(list(group_cols))[cols].mean().reset_index().assign(n=ls.groupby(list(group_cols)).size().values)


def go_no_go(trades: pd.DataFrame) -> pd.DataFrame:
    """DESIGN/91 §4's bar, read on the whole panel (no OOS season, no forward ledger)."""
    median = spread_median(trades)
    halves = spread_half_table(trades, median)
    rows = []
    for v, s in SG_PAIRS:
        s1 = H._block(H._pair(trades, v, s, "S1"), v, s, "S1", CLUSTER_COL)
        s2 = H._block(H._pair(trades, v, s, "S2"), v, s, "S2", CLUSTER_COL)
        pooled = H._block(H._pair(trades, v, s, H.POOLED), v, s, H.POOLED, CLUSTER_COL)
        low = halves[(halves.variant == v) & (halves.structure == s) & (halves.half == "low")]
        low_mean = float(low.mean_net_pct.iloc[0]) if len(low) else np.nan
        wide = halves[(halves.variant == v) & (halves.structure == s) & (halves.half == "wide")]
        wide_mean = float(wide.mean_net_pct.iloc[0]) if len(wide) else np.nan
        c1_sign = bool(s1["n"] and s2["n"] and s1["mean_net_pct"] > 0 and s2["mean_net_pct"] > 0)
        c2_t = bool(pooled["n"] and np.isfinite(pooled["t"]) and pooled["t"] >= SG_GO_T_MIN)
        c3_low_spread = bool(np.isfinite(low_mean) and low_mean > 0)
        kill_season = bool(s1["n"] and s1["mean_net_pct"] <= 0) or bool(s2["n"] and s2["mean_net_pct"] <= 0)
        kill_wide_only = bool(c1_sign and c2_t and not c3_low_spread and np.isfinite(wide_mean) and wide_mean > 0)
        if kill_season:
            verdict, note = "KILLED", "net <= 0 in Season 1 or Season 2 (DESIGN/91 §4 kill rule)"
        elif kill_wide_only:
            verdict, note = "KILLED", "positive only in the wide-spread half (DESIGN/91 §4 kill rule)"
        elif c1_sign and c2_t and c3_low_spread:
            verdict, note = "PASS", "clears sign consistency, pooled t, and the low-spread half"
        else:
            verdict, note = "NO-GO", "fails " + ", ".join(
                k for k, ok in (("c1_sign_s1_s2", c1_sign), ("c2_t_2.0", c2_t), ("c3_low_spread", c3_low_spread)) if not ok)
        rows.append({"variant": v, "structure": s, "n_s1": s1["n"], "n_s2": s2["n"], "mean_s1": s1["mean_net_pct"],
                    "mean_s2": s2["mean_net_pct"], "mean_pooled": pooled["mean_net_pct"], "t_pooled": pooled["t"],
                    "mean_low_spread": low_mean, "mean_wide_spread": wide_mean, "verdict": verdict, "note": note})
    return pd.DataFrame(rows)
