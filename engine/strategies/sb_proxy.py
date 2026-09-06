"""The three-year S-B proxy (DESIGN/80 §5.1): Black-Scholes legs at the panel-measured smile
multipliers, entered on the last session of each week when the gate is ON, held to expiry and
settled at the close, costs from the panel-measured spreads. Pure functions over `ProxyInputs`.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Mapping

import pandas as pd

from engine import bs
from engine import config
from engine import marking as M
from engine.config import SB_PARAMS, SB_SIZING, SBParams, SBSizing
from engine.mart import index_vol as IV
from engine.strategies import sb_gate as G
from engine.strategies import sb_structures as SB
from engine.strategies import sa_structures as ST

SOURCE_PROXY = "proxy"
PROXY_TIER = 3
WINDOW_OFF = "off"


@dataclass
class ProxyInputs:
    index_vol: pd.DataFrame                       # date, vix, vix3m, vxn, vix9d
    closes: Mapping[tuple[str, date], float]      # (ticker, date) -> close
    sessions: list[date]                          # sorted SPY sessions


def load_inputs(index_vol_path: str | None = None, prices_path: str | None = None) -> ProxyInputs:
    iv = IV.load_index_vol(index_vol_path or config.INDEX_VOL_FILE, config.INDEX_VOL_FALLBACK)
    px = pd.read_parquet(prices_path or config.PROXY_PRICES_FALLBACK)
    px = px.assign(date=pd.to_datetime(px["date"]).dt.date)
    closes = {(r.ticker, r.date): float(r.close) for r in px.itertuples(index=False)}
    sessions = sorted(set(px.loc[px.ticker == "SPY", "date"]))
    return ProxyInputs(iv, closes, sessions)


def entry_sessions(sessions: list[date], start: date, end: date) -> list[date]:
    """The last session of each ISO week (from the full list), restricted to [start, end]."""
    last_of_week: dict[tuple[int, int], date] = {}
    for s in sessions:
        iso = s.isocalendar()
        last_of_week[(iso[0], iso[1])] = s
    return sorted(s for s in last_of_week.values() if start <= s <= end)


def window_of(entry: date) -> str:
    for name, (lo, hi) in config.SB_WINDOWS.items():
        if lo <= entry <= hi:
            return name
    return WINDOW_OFF


def proxy_leg_marks(underlying: str, spot: float, strikes: Mapping[str, float], dte_cal: int, x_t: float,
                    structure: str) -> dict[str, M.Mark]:
    t_years = dte_cal / SB.DAYS_PER_YEAR
    marks = {}
    for leg in SB.STRUCTURE_LEGS[structure]:
        iv = config.SB_PROXY_IV_MULT[(underlying, leg)] * x_t / 100.0
        price = float(bs.price(spot, strikes[leg], t_years, config.RISK_FREE_RATE, iv, SB.LEG_TYPE[leg]))
        marks[leg] = M.Mark(price, config.SB_PROXY_SPREAD[(underlying, leg)], PROXY_TIER, SOURCE_PROXY)
    return marks


def position_row(underlying: str, structure: str, entry: date, expiry: date, spot: float, x_t: float,
                 strikes: Mapping[str, float], legs: list[ST.Leg], sizing: SBSizing, cost_mult: float) -> dict:
    """Common row for a proxy or marked position from its legs (exits may be None)."""
    credit = ST.credit_per_share(legs, "entry")
    max_loss = SB.max_loss_per_contract(strikes, structure, credit)
    n = SB.size_position(max_loss, sizing)
    priced = ST.price_legs(legs, n, cost_mult)
    risk = max_loss * n
    dte_cal = (expiry - entry).days
    w = SB.width(strikes, structure)
    return {"underlying": underlying, "structure": structure, "entry": entry, "expiry": expiry, "dte_cal": dte_cal,
            "spot": spot, "x": x_t, "m": SB.sigma_unit(x_t, dte_cal),
            "k_p1": strikes.get(SB.LEG_P1), "k_p2": strikes.get(SB.LEG_P2),
            "k_c1": strikes.get(SB.LEG_C1) if structure == SB.STRUCTURE_IC else None,
            "k_c2": strikes.get(SB.LEG_C2) if structure == SB.STRUCTURE_IC else None,
            "width": w, **priced, "contracts": n, "max_loss_usd": max_loss, "risk_usd": risk,
            "ror": priced["net_usd"] / risk, "credit_over_width": credit / w if w else float("nan"),
            "cost_over_credit": priced["cost_usd"] / (credit * M.CONTRACT_MULTIPLIER * n) if credit > 0 else float("nan"),
            "window": window_of(entry), "entry_month": entry.strftime("%Y-%m"), "month": expiry.strftime("%Y-%m")}


def proxy_position(underlying: str, structure: str, entry: date, expiry: date, spot: float, x_t: float,
                   settle_close: float, params: SBParams, sizing: SBSizing, cost_mult: float = 1.0) -> dict | None:
    dte_cal = (expiry - entry).days
    m = SB.sigma_unit(x_t, dte_cal)
    strikes = {leg: SB.round_to_step(k, config.SB_PROXY_STRIKE_STEP)
               for leg, k in SB.target_strikes(spot, m, params).items() if leg in SB.STRUCTURE_LEGS[structure]}
    if not SB.strikes_ordered(strikes, spot, structure):
        return None
    entry_marks = proxy_leg_marks(underlying, spot, strikes, dte_cal, x_t, structure)
    exit_marks = SB.settle_marks(strikes, structure, settle_close)
    legs = SB.build_legs(underlying, expiry, strikes, entry_marks, exit_marks, structure)
    return {**position_row(underlying, structure, entry, expiry, spot, x_t, strikes, legs, sizing, cost_mult),
            "settle_close": settle_close}


def _gate_fields(state: G.GateState, mode: str) -> dict:
    return {"gate_reason": state.reason, "gate_asof": state.asof, "gate_vix": state.vix, "gate_vix3m": state.vix3m,
            "gate_x": state.x, "gate_x_median": state.x_median, "gate_mode": mode}


def _x_on(index_vol: pd.DataFrame, t: date, x_col: str) -> float | None:
    if index_vol is None or index_vol.empty or "date" not in index_vol.columns or x_col not in index_vol.columns:
        return None
    row = index_vol[index_vol["date"] == t]
    if row.empty:
        return None
    v = row[x_col].iloc[0]
    return None if pd.isna(v) else float(v)


def run_proxy(inputs: ProxyInputs, params: SBParams = SB_PARAMS, sizing: SBSizing = SB_SIZING,
              gate_mode: str = "both", cost_mult: float = 1.0, start: date | None = None, end: date | None = None,
              underlyings: tuple[str, ...] = config.SB_UNDERLYINGS,
              structures: tuple[str, ...] = config.SB_STRUCTURES) -> pd.DataFrame:
    """One row per (entry, underlying, structure) entered under `gate_mode`, capped per sleeve."""
    sessions = inputs.sessions
    if not sessions:
        return pd.DataFrame()
    entries = entry_sessions(sessions, start or sessions[0], end or sessions[-1])
    index = {d: i for i, d in enumerate(sessions)}
    session_set = set(sessions)
    index_vol = IV.on_sessions(inputs.index_vol, session_set.__contains__)
    rows = []
    for t in entries:
        i = index[t]
        if i == 0:
            continue
        expiry = SB.proxy_expiry(t, sessions, params)
        if expiry is None:
            continue
        for u in underlyings:
            x_col = config.SB_VOL_INDEX[u]
            state = G.gate(index_vol, t, sessions[i - 1], x_col, params)
            if not G.is_on(state, gate_mode):
                continue
            x_t = _x_on(index_vol, t, x_col)
            spot, settle = inputs.closes.get((u, t)), inputs.closes.get((u, expiry))
            if x_t is None or spot is None or settle is None:
                continue
            for s in structures:
                row = proxy_position(u, s, t, expiry, spot, x_t, settle, params, sizing, cost_mult)
                if row is not None:
                    rows.append({**row, **_gate_fields(state, gate_mode)})
    entered, _ = SB.cap_open_positions(rows, sizing.max_open_per_sleeve)
    if not entered:
        return pd.DataFrame()
    return pd.DataFrame(entered).sort_values(["entry", "underlying", "structure"], kind="mergesort").reset_index(drop=True)
