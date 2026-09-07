"""G1 step 2 (RESEARCH/47 §2 G1): re-mark the frozen 612 S-A trade rows under two pre-registered
treatments, without touching `data/backtest/trades.parquet` or the marking engine's frozen
behavior. Reuses `engine.strategies.sa_structures.price_legs` / `engine.marking.leg_cost` so the
dollar arithmetic is exactly the champion's, not a re-implementation.

  Treatment (a) mid fills: on any leg touch whose (tier, window) cell shows an observed
  at-or-better-than-mid volume share > 50% (`fills.py` step 1's crosswalk), assume the limit
  filled at the mark price with no spread cost — commission only. Tier-3 (model) touches always
  keep the original half-spread cost: there is no observed NBBO to condition on.

  Treatment (b) later exit: re-mark the exit legs only (entry is untouched) using prints in a
  later window on `post` (`b1` = 10:30-11:30, `b2` = 14:30-15:30) instead of the original
  09:30-10:30 `early` window. Building the new marks needs real panel access, so that part lives
  in `scripts/g1_remark.py`; this module takes the resulting `Mark` objects and reuses the
  champion's own pricer.

  Treatment (a+b) composes both: new exit marks from (b), then (a)'s cost override evaluated
  against the (tier, window) cell of whichever window produced each leg's mark (entry stays
  `late`, exit becomes `b1`/`b2`).
"""
from __future__ import annotations

from typing import Mapping

import pandas as pd

from engine import marking as M
from engine.config import CONTRACT_MULTIPLIER, MODEL_SPREAD_FLOOR
from engine.improve import fills as G
from engine.strategies import sa_structures as ST

ATM_LEGS = ("call", "put")
WING_LEGS = ("wing_call", "wing_put")
ALL_LEGS = ATM_LEGS + WING_LEGS
LEG_SIDE = {"call": ST.SHORT, "put": ST.SHORT, "wing_call": ST.LONG, "wing_put": ST.LONG}
LEG_OPTION_TYPE = {"call": "call", "put": "put", "wing_call": "call", "wing_put": "put"}
ENTRY_WINDOW = G.WINDOW_LATE   # every S-A entry leg is marked at `late` on `pre` (sa.py)


def present_legs(row: Mapping) -> list[str]:
    """Which of the four legs this trade row carries (SS: 2, IC: 4)."""
    return [leg for leg in ALL_LEGS if row.get(f"{leg}_id") is not None and pd.notna(row.get(f"{leg}_id"))]


def leg_strike(row: Mapping, leg: str) -> float:
    return row["k"] if leg in ATM_LEGS else (row["k_up"] if leg == "wing_call" else row["k_dn"])


def contract_for_leg(row: Mapping, leg: str) -> M.Contract:
    return M.Contract(row[f"{leg}_id"], row["ticker"], LEG_OPTION_TYPE[leg], float(leg_strike(row, leg)), row["expiry"])


def entry_mark_from_row(row: Mapping, leg: str) -> M.Mark:
    """The leg's original entry mark, unchanged by either treatment."""
    return M.Mark(float(row[f"{leg}_entry"]), float(row[f"{leg}_entry_spread"]), int(row[f"{leg}_entry_tier"]),
                 "orig_entry")


def exit_mark_from_row(row: Mapping, leg: str) -> M.Mark:
    """The leg's original exit mark (tier, spread as-frozen), for the treatment-a-only path."""
    return M.Mark(float(row[f"{leg}_exit"]), float(row[f"{leg}_exit_spread"]), int(row[f"{leg}_exit_tier"]),
                 "orig_exit")


def build_legs(row: Mapping, exit_marks: Mapping[str, M.Mark] | None = None) -> list[ST.Leg]:
    """One `ST.Leg` per present leg. `exit_marks` (leg name -> Mark) overrides the exit side for
    treatment (b); omitted legs (or a None entry) fall back to the row's original exit mark."""
    legs = []
    for leg in present_legs(row):
        exit_mark = None
        if exit_marks is not None and leg in exit_marks and exit_marks[leg] is not None:
            exit_mark = exit_marks[leg]
        elif exit_marks is None:
            exit_mark = exit_mark_from_row(row, leg)
        if exit_mark is None:
            continue    # unmarkable in the new window: this leg (and so this row) is excluded
        legs.append(ST.Leg(leg, contract_for_leg(row, leg), LEG_SIDE[leg], entry_mark_from_row(row, leg), exit_mark))
    return legs


# ----------------------------------------------------------------------------- treatment (a): mid-fill cost


def build_mid_share_lookup(fills_window: pd.DataFrame) -> dict[tuple[int, str], float]:
    """(tier, window) -> observed at-or-better-than-mid volume share, from `g1_fills.parquet`'s
    `cut == 'window'` rows (`scripts/fills.py`)."""
    out: dict[tuple[int, str], float] = {}
    for (tier, window), g in fills_window.groupby(["tier", "dim2"]):
        out[(int(tier), window)] = G.mid_or_better_share(g.to_dict("records")).volume_share
    return out


def qualifies_for_mid_fill(tier: int, window: str, lookup: Mapping[tuple[int, str], float]) -> bool:
    """Tier 3 (model, no observed print) never qualifies; tier 1/2 qualify when the observed
    mid-or-better share for that (tier, window) cell exceeds 50%."""
    if tier not in (1, 2):
        return False
    share = lookup.get((tier, window))
    return share is not None and share > 0.5


def leg_touch_cost(price: float, spread: float, tier: int, window: str, n: int,
                   lookup: Mapping[tuple[int, str], float], cost_mult: float = 1.0) -> float:
    """`marking.leg_cost`, with the half-spread zeroed when the (tier, window) cell qualifies for
    a mid fill (treatment a); commission is still paid either way."""
    from engine.config import COMMISSION_PER_CONTRACT
    if qualifies_for_mid_fill(tier, window, lookup):
        return cost_mult * COMMISSION_PER_CONTRACT * n
    eff_spread = spread if spread == spread else MODEL_SPREAD_FLOOR   # spread == spread: not NaN
    half_spread_dollars = 0.5 * eff_spread * price * CONTRACT_MULTIPLIER
    return cost_mult * (half_spread_dollars + COMMISSION_PER_CONTRACT) * n


def price_with_treatment_a(row: Mapping, lookup: Mapping[tuple[int, str], float],
                           exit_window: str = "early", exit_marks: Mapping[str, M.Mark] | None = None) -> dict:
    """Gross unchanged; cost recomputed leg-by-leg under treatment (a). `exit_window` names the
    (tier, window) cell each leg's *original* exit tier is checked against — `early` for
    treatment-a-only, `b1`/`b2` when composed with treatment (b) (`exit_marks` then also carries
    the new marks so gross reflects the moved window)."""
    legs = build_legs(row, exit_marks)
    if len(legs) != len(present_legs(row)):
        return {"net_usd": float("nan"), "gross_usd": float("nan"), "cost_usd": float("nan"), "n_legs": len(legs)}
    n = int(row["contracts"])
    priced = ST.price_legs(legs, n)
    cost = 0.0
    for leg in legs:
        cost += leg_touch_cost(leg.entry.price, leg.entry.rel_spread, leg.entry.tier, ENTRY_WINDOW, n, lookup)
        cost += leg_touch_cost(leg.exit.price, leg.exit.rel_spread, leg.exit.tier, exit_window, n, lookup)
    net_usd = priced["gross_usd"] - cost
    return {"net_usd": net_usd, "gross_usd": priced["gross_usd"], "cost_usd": cost, "n_legs": len(legs)}


def apply_treatment(trades: pd.DataFrame, suffix: str, lookup: Mapping[tuple[int, str], float] | None,
                    exit_window: str, exit_marks_by_row: Mapping[int, Mapping[str, M.Mark]] | None = None,
                    apply_a: bool = True) -> pd.DataFrame:
    """New frame (never mutates `trades`) with `net_usd_<suffix>`, `net_pct_<suffix>`,
    `cost_usd_<suffix>`, `gross_usd_<suffix>`, `n_legs_<suffix>` columns. `lookup=None` disables
    treatment (a)'s cost override (pure re-marking under (b) alone: original half-spread cost)."""
    out_net_usd, out_gross_usd, out_cost_usd, out_n_legs = [], [], [], []
    for idx, row in trades.iterrows():
        exit_marks = exit_marks_by_row.get(idx) if exit_marks_by_row is not None else None
        if apply_a:
            r = price_with_treatment_a(row, lookup or {}, exit_window, exit_marks)
        else:
            legs = build_legs(row, exit_marks)
            if len(legs) != len(present_legs(row)):
                r = {"net_usd": float("nan"), "gross_usd": float("nan"), "cost_usd": float("nan"), "n_legs": len(legs)}
            else:
                priced = ST.price_legs(legs, int(row["contracts"]))
                r = {"net_usd": priced["net_usd"], "gross_usd": priced["gross_usd"],
                    "cost_usd": priced["cost_usd"], "n_legs": len(legs)}
        out_net_usd.append(r["net_usd"])
        out_gross_usd.append(r["gross_usd"])
        out_cost_usd.append(r["cost_usd"])
        out_n_legs.append(r["n_legs"])
    notional = trades["notional_usd"].to_numpy()
    return trades.assign(**{
        f"gross_usd_{suffix}": out_gross_usd, f"cost_usd_{suffix}": out_cost_usd,
        f"net_usd_{suffix}": out_net_usd, f"n_legs_{suffix}": out_n_legs,
        f"net_pct_{suffix}": pd.Series(out_net_usd, index=trades.index) / notional,
        f"cost_pct_{suffix}": pd.Series(out_cost_usd, index=trades.index) / notional,
    })
