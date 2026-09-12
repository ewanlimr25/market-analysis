"""Descriptive: the structures S-B does *not* trade, re-priced on the proxy's own entry rows
(DESIGN/80 §6.6 family; owner request 2026-09-12). Single legs, the naked short put and call, and
the call credit spread, each priced with the frozen proxy smile at entry (`sb_proxy.proxy_leg_marks`)
and at intrinsic on the settle close, with the frozen costs. Nothing here is a sleeve, a trial or a
verdict input: `go_no_go` never reads it, and the deflated-Sharpe trial count does not move.

Risk denominators (fixed here, mirrored in the challenger drafts under ledger/challengers/drafts/):
debit structures -- the premium paid; credit spreads -- width minus credit; naked shorts -- the
2-sigma stress loss, i.e. the matching credit spread's max loss at the same strikes (the
`sb-c-nakedput-margin` draft's rule), with the Reg-T proxy margin reported beside as `margin_usd`.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from engine import config
from engine.strategies import sb_proxy as P
from engine.strategies import sb_structures as SB
from engine.validation import stats as S

LONG, SHORT = 1, -1
MULT = config.CONTRACT_MULTIPLIER
COMMISSION = config.COMMISSION_PER_CONTRACT
REG_T_FRAC, REG_T_FLOOR_FRAC = 0.20, 0.10          # Reg-T proxy: max(20% spot - OTM, 10% spot) x 100 - premium

ALT_STRUCTURES: dict[str, tuple[tuple[str, int], ...]] = {
    "long_c1": (("c1", LONG),), "long_p1": (("p1", LONG),), "long_c2": (("c2", LONG),), "long_p2": (("p2", LONG),),
    "short_p1_naked": (("p1", SHORT),), "short_c1_naked": (("c1", SHORT),),
    "CS": (("c1", SHORT), ("c2", LONG)), "PS": (("p1", SHORT), ("p2", LONG)),
}
SETS = (("gate ON", "base"), ("every Friday", "gate_off"))
TABLE_COLS = ["set", "structure", "underlying", "n", "mean_ror", "nw_t", "hit", "mean_pnl_usd", "worst_ror",
              "mean_premium_usd", "mean_margin_usd", "total_pnl_usd"]


def intrinsic(leg: str, strike: float, close: float) -> float:
    return max(close - strike, 0.0) if leg.startswith("c") else max(strike - close, 0.0)


def _strikes(row) -> dict[str, float]:
    return {leg: float(getattr(row, f"k_{leg}")) for leg in ("p1", "p2", "c1", "c2")}


def _leg_pnl_per_contract(row, leg: str, side: int, marks) -> tuple[float, float]:
    """(net $ for one contract held to expiry, entry premium $ signed by side: +paid / -received)."""
    m = marks[leg]
    entry_cost = 0.5 * m.rel_spread * m.price * MULT + COMMISSION
    pnl = side * (intrinsic(leg, _strikes(row)[leg], row.settle_close) - m.price) * MULT - entry_cost - COMMISSION
    return pnl, side * m.price * MULT


def _risk(row, name: str, premium: float, marks) -> tuple[float, float]:
    """(risk_usd, margin_usd) per contract; margin is NaN except for naked shorts."""
    legs = ALT_STRUCTURES[name]
    k = _strikes(row)
    if premium > 0:                                             # debit: the premium is the risk
        return premium, np.nan
    if len(legs) == 2:                                          # credit spread: width - credit
        return abs(k[legs[0][0]] - k[legs[1][0]]) * MULT + premium, np.nan
    leg = legs[0][0]                                            # naked short: the 2-sigma stress loss = the
    wing = "p2" if leg == "p1" else "c2"                        # matching spread's max loss at the same strikes
    stress = (abs(k[leg] - k[wing]) - (marks[leg].price - marks[wing].price)) * MULT
    otm = abs(row.spot - k[leg])
    margin = max(REG_T_FRAC * row.spot - otm, REG_T_FLOOR_FRAC * row.spot) * MULT + premium
    return stress, margin


def structure_row(row, name: str) -> dict:
    """One structure on one proxy IC row (needs k_p1..k_c2, spot, x, dte_cal, settle_close)."""
    marks = P.proxy_leg_marks(row.underlying, row.spot, _strikes(row), int(row.dte_cal), row.x, SB.STRUCTURE_IC)
    pnl = premium = 0.0
    for leg, side in ALT_STRUCTURES[name]:
        p, prem = _leg_pnl_per_contract(row, leg, side, marks)
        pnl, premium = pnl + p, premium + prem
    risk, margin = _risk(row, name, premium, marks)
    return {"structure": name, "underlying": row.underlying, "entry": row.entry, "expiry": row.expiry,
            "premium_usd": premium, "pnl_usd": pnl, "risk_usd": risk, "margin_usd": margin, "ror": pnl / risk}


def structure_rows(ic_rows: pd.DataFrame, names: tuple[str, ...] = tuple(ALT_STRUCTURES)) -> pd.DataFrame:
    if ic_rows is None or ic_rows.empty:
        return pd.DataFrame(columns=["structure", "underlying", "entry", "expiry", "premium_usd", "pnl_usd",
                                     "risk_usd", "margin_usd", "ror"])
    return pd.DataFrame([structure_row(r, n) for r in ic_rows.itertuples(index=False) for n in names])


def summarize(rows: pd.DataFrame, label: str, lag: int = config.SB_NW_LAG) -> pd.DataFrame:
    out = []
    for (name, u), g in rows.groupby(["structure", "underlying"], sort=False):
        g = g.sort_values("entry", kind="mergesort")
        nw = S.nw_t(g["ror"], lag)
        out.append({"set": label, "structure": name, "underlying": u, "n": int(len(g)), "mean_ror": nw["mean"],
                    "nw_t": nw["t"], "hit": nw["hit"], "mean_pnl_usd": float(g["pnl_usd"].mean()),
                    "worst_ror": float(g["ror"].min()), "mean_premium_usd": float(g["premium_usd"].mean()),
                    "mean_margin_usd": float(g["margin_usd"].mean()), "total_pnl_usd": float(g["pnl_usd"].sum())})
    return pd.DataFrame(out, columns=TABLE_COLS)


def alt_structure_table(proxy_sens: pd.DataFrame) -> pd.DataFrame:
    """The report table: every alternative structure on the IC rows of the `base` (gate ON) and
    `gate_off` (every Friday) sensitivities, per underlying. Empty when the frame lacks them."""
    if proxy_sens is None or proxy_sens.empty or "sensitivity" not in proxy_sens.columns:
        return pd.DataFrame(columns=TABLE_COLS)
    ic = proxy_sens[proxy_sens["structure"] == SB.STRUCTURE_IC]
    parts = [summarize(structure_rows(ic[ic["sensitivity"] == key]), label) for label, key in SETS]
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame(columns=TABLE_COLS)
