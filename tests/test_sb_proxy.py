"""Q4: the three-year proxy (DESIGN/80 §5.1): one position priced by hand, settlement inside /
at / beyond the wings, entry sessions, windows, and a deterministic synthetic run."""
from __future__ import annotations

import math
from datetime import date, timedelta

import pandas as pd
import pytest

from engine import bs
from engine.config import (RISK_FREE_RATE, SB_PARAMS, SB_PROXY_IV_MULT, SB_PROXY_SPREAD, SB_SIZING,
                           COMMISSION_PER_CONTRACT)
from engine.strategies import sb_proxy as P

pytestmark = pytest.mark.unit


def _sessions(start: date, n: int, holidays=()) -> list[date]:
    out, d = [], start
    while len(out) < n:
        if d.weekday() < 5 and d not in holidays:
            out.append(d)
        d += timedelta(days=1)
    return out


def test_entry_sessions_are_the_last_session_of_each_iso_week():
    sessions = _sessions(date(2026, 3, 30), 15, holidays=(date(2026, 4, 3),))     # Good Friday week
    ent = P.entry_sessions(sessions, date(2026, 3, 30), date(2026, 4, 17))
    assert ent == [date(2026, 4, 2), date(2026, 4, 10), date(2026, 4, 17)]


def test_window_of_entry():
    assert P.window_of(date(2023, 9, 8)) == "P1" and P.window_of(date(2024, 8, 30)) == "P1"
    assert P.window_of(date(2025, 4, 4)) == "P2" and P.window_of(date(2026, 8, 14)) == "P3"
    assert P.window_of(date(2023, 9, 1)) == "off" and P.window_of(date(2024, 9, 3)) == "off"


def _hand_position(structure: str, close: float):
    spot, x, dte = 100.0, 20.0, 21
    m = x / 100 * math.sqrt(dte / 365)
    return P.proxy_position("SPY", structure, date(2026, 7, 10), date(2026, 7, 31), spot, x, close, SB_PARAMS, SB_SIZING), m


def test_put_spread_priced_by_hand_and_settled_inside_the_wings():
    row, m = _hand_position("PS", close=92.0)
    T = 21 / 365
    k1, k2 = round(100 * (1 - m)), round(100 * (1 - 2 * m))
    assert (row["k_p1"], row["k_p2"]) == (k1, k2) == (95.0, 90.0)
    p1 = bs.price(100.0, k1, T, RISK_FREE_RATE, 0.20 * SB_PROXY_IV_MULT[("SPY", "p1")], "put")
    p2 = bs.price(100.0, k2, T, RISK_FREE_RATE, 0.20 * SB_PROXY_IV_MULT[("SPY", "p2")], "put")
    credit = p1 - p2
    assert row["credit_entry"] == pytest.approx(credit)
    max_loss = (k1 - k2 - credit) * 100
    assert row["max_loss_usd"] == pytest.approx(max_loss)
    n = max(1, math.floor(SB_SIZING.max_loss_frac * SB_SIZING.equity / max_loss))
    assert row["contracts"] == n
    entry_cost = n * ((0.5 * SB_PROXY_SPREAD[("SPY", "p1")] * p1 * 100 + COMMISSION_PER_CONTRACT)
                      + (0.5 * SB_PROXY_SPREAD[("SPY", "p2")] * p2 * 100 + COMMISSION_PER_CONTRACT))
    assert row["entry_cost_usd"] == pytest.approx(entry_cost)
    assert row["debit_exit"] == pytest.approx(3.0)                       # 95 put worth 3 at 92, 90 put worth 0
    gross = (credit - 3.0) * 100 * n
    net = gross - entry_cost - 2 * n * COMMISSION_PER_CONTRACT
    assert row["net_usd"] == pytest.approx(net) and row["ror"] == pytest.approx(net / (max_loss * n))
    assert row["x"] == 20.0 and row["m"] == pytest.approx(m) and row["dte_cal"] == 21


def test_settlement_beyond_the_wing_loses_the_full_width_and_above_keeps_the_credit():
    beyond, _ = _hand_position("PS", close=80.0)
    assert beyond["debit_exit"] == pytest.approx(5.0)
    assert beyond["ror"] == pytest.approx(-1.0 - beyond["cost_usd"] / beyond["risk_usd"])
    kept, _ = _hand_position("PS", close=104.0)
    assert kept["debit_exit"] == 0.0 and kept["gross_usd"] == pytest.approx(kept["credit_entry"] * 100 * kept["contracts"])


def test_iron_condor_adds_the_call_side_and_uses_the_larger_width():
    row, m = _hand_position("IC", close=100.0)
    assert (row["k_c1"], row["k_c2"]) == (105.0, 110.0)
    assert row["width"] == 5.0 and row["credit_entry"] > _hand_position("PS", 100.0)[0]["credit_entry"]
    assert row["max_loss_usd"] == pytest.approx((5.0 - row["credit_entry"]) * 100)


def _synthetic_inputs(n_sessions: int = 80):
    sessions = _sessions(date(2026, 1, 5), n_sessions)
    vix = [15.0 + 0.05 * i for i in range(n_sessions)]           # rising: G2 on after the window fills
    iv = pd.DataFrame({"date": sessions, "vix": vix, "vix3m": [v + 2 for v in vix], "vxn": [v + 5 for v in vix], "vix9d": vix})
    closes = {(u, d): 100.0 + (0.1 * i if u == "SPY" else -0.1 * i) for i, d in enumerate(sessions) for u in ("SPY", "QQQ")}
    return P.ProxyInputs(index_vol=iv, closes=closes, sessions=sessions)


def test_run_proxy_is_deterministic_gated_and_carries_the_gate_fields():
    inputs = _synthetic_inputs()
    on = P.run_proxy(inputs, gate_mode="both")
    again = P.run_proxy(inputs, gate_mode="both")
    pd.testing.assert_frame_equal(on, again)
    assert set(on.underlying) == {"SPY", "QQQ"} and set(on.structure) == {"PS", "IC"}
    assert (on.expiry <= max(inputs.sessions)).all() and (on.entry.map(lambda d: d.weekday()) == 4).all()
    assert on.gate_reason.eq("ON").all() and on.gate_asof.lt(on.entry).all()
    off = P.run_proxy(inputs, gate_mode="off")
    assert len(off) >= len(on) and set(off.gate_mode) == {"off"}
    # the first 21 sessions cannot be gated (window not filled): UNKNOWN fails closed in every mode
    assert on.entry.min() > inputs.sessions[21]
    for col in ("window", "ror", "net_usd", "max_loss_usd", "contracts", "credit_entry", "k_p1", "k_p2", "entry_cost_usd", "exit_cost_usd"):
        assert col in on.columns
