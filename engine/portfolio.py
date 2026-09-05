"""Book caps (DESIGN/70 §3.3): per print night and per (variant, structure), take candidates in
order of implied premium after cost until the count, sector or night-risk-budget cap binds.

The event-level statistics in the validation harness run on every filter-passing event; the
capped subset is the portfolio view (what the account would have carried).
"""
from __future__ import annotations

import pandas as pd

from engine.config import SizingParams
from engine.strategies.sa_structures import STRUCTURE_IC

SORT_KEYS = ["variant", "structure", "pre", "credit_net_pct", "ticker"]


def night_budget_usd(structure: str, sizing: SizingParams) -> float:
    per_trade = sizing.ic_max_loss_frac if structure == STRUCTURE_IC else sizing.ss_stress_frac
    return sizing.night_budget_frac * sizing.max_open_events * per_trade * sizing.equity


def _cap_one_night(night: pd.DataFrame, sizing: SizingParams) -> list[dict]:
    budget = night_budget_usd(night["structure"].iloc[0], sizing)
    taken, sector_counts, risk_used = 0, {}, 0.0
    out = []
    for rank, row in enumerate(night.to_dict("records"), start=1):
        sector = row.get("sector")
        fits = (taken < sizing.max_open_events
                and sector_counts.get(sector, 0) < sizing.max_per_sector
                and risk_used + float(row["risk_usd"]) <= budget)
        if fits:
            taken += 1
            sector_counts[sector] = sector_counts.get(sector, 0) + 1
            risk_used += float(row["risk_usd"])
        out.append({**row, "cap_pass": bool(fits), "cap_rank": rank})
    return out


def apply_caps(trades: pd.DataFrame, sizing: SizingParams) -> pd.DataFrame:
    """Returns a new frame with `cap_pass` and `cap_rank` per (variant, structure, pre)."""
    if trades.empty:
        return trades.assign(cap_pass=pd.Series(dtype=bool), cap_rank=pd.Series(dtype=int))
    ordered = trades.sort_values(SORT_KEYS, ascending=[True, True, True, False, True], kind="mergesort")
    rows = []
    for _, night in ordered.groupby(["variant", "structure", "pre"], sort=False):
        rows.extend(_cap_one_night(night, sizing))
    return pd.DataFrame(rows)
