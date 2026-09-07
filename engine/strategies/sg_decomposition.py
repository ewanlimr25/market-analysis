"""The gross ramp decomposition (DESIGN/91 §4): delta (underlying-move) vs vega (IV-change)
components of the straddle's mark change from entry to exit, by finite-difference Greeks off
`engine.bs.price` (imported, not edited — `engine/bs.py` gains no new function).
"""
from __future__ import annotations

import math
from dataclasses import dataclass

from engine import bs

DS_FRAC = 1e-3     # relative underlying bump for the finite-difference delta
DV_ABS = 1e-4      # absolute vol-point bump for the finite-difference vega
MIN_T_YEARS = 1e-6


@dataclass(frozen=True)
class LegGreekInputs:
    spot: float
    strike: float
    t_years: float
    iv: float
    option_type: str


def numeric_delta(g: LegGreekInputs, r: float, ds_frac: float = DS_FRAC) -> float:
    if g.spot <= 0 or g.iv is None or g.iv <= 0 or g.t_years <= MIN_T_YEARS:
        return 0.0
    ds = max(g.spot * ds_frac, 1e-6)
    up = bs.price(g.spot + ds, g.strike, g.t_years, r, g.iv, g.option_type)
    dn = bs.price(g.spot - ds, g.strike, g.t_years, r, g.iv, g.option_type)
    return float((up - dn) / (2 * ds))


def numeric_vega(g: LegGreekInputs, r: float, dv_abs: float = DV_ABS) -> float:
    if g.spot <= 0 or g.iv is None or g.iv <= 0 or g.t_years <= MIN_T_YEARS:
        return 0.0
    up = bs.price(g.spot, g.strike, g.t_years, r, g.iv + dv_abs, g.option_type)
    dn = bs.price(g.spot, g.strike, g.t_years, r, max(g.iv - dv_abs, 1e-8), g.option_type)
    return float((up - dn) / (2 * dv_abs))


@dataclass(frozen=True)
class Decomposition:
    unhedged_pnl_pct: float
    delta_pnl_pct: float
    delta_hedged_pnl_pct: float
    vega_pnl_pct: float
    residual_pnl_pct: float
    net_delta: float
    net_vega: float
    iv_entry_mean: float | None
    iv_exit_mean: float | None


def decompose(entry_price_sum: float, exit_price_sum: float, spot_entry: float, spot_exit: float,
             net_delta: float, net_vega: float, iv_entry_mean: float | None,
             iv_exit_mean: float | None) -> Decomposition:
    """DESIGN/91 §4's five-line decomposition. `entry_price_sum`/`exit_price_sum` are the summed
    per-share call+put prices (a long straddle/strangle's mark), so their difference is the
    unhedged, no-cost P&L per share."""
    unhedged = (exit_price_sum - entry_price_sum) / spot_entry
    delta_pnl = net_delta * (spot_exit - spot_entry) / spot_entry
    delta_hedged = unhedged - delta_pnl
    iv_change = (iv_exit_mean - iv_entry_mean) if (iv_entry_mean is not None and iv_exit_mean is not None) else None
    vega_pnl = net_vega * iv_change / spot_entry if iv_change is not None else float("nan")
    residual = delta_hedged - vega_pnl if math.isfinite(vega_pnl) else float("nan")
    return Decomposition(unhedged, delta_pnl, delta_hedged, vega_pnl, residual, net_delta, net_vega,
                         iv_entry_mean, iv_exit_mean)
