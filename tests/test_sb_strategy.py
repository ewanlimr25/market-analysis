"""Q5: the marked S-B layer (DESIGN/80 §3, §5.2) on synthetic daily_contract rows: entry
candidates, tiers, spread filter, missing wing, grading at expiry, the chronological run."""
from __future__ import annotations

import json
from datetime import date

import pandas as pd
import pytest

from engine import calendar as cal
from engine.config import SB_PARAMS, SB_SIZING, COMMISSION_PER_CONTRACT
from engine.strategies import sb, sb_gate as G, sb_structures as SB

pytestmark = pytest.mark.unit

ENTRY, EXP = date(2026, 7, 10), date(2026, 7, 31)          # Friday, Friday + 21
X = 20.0
M_UNIT = SB.sigma_unit(X, 21)                              # 0.04797 -> 1σ ~ 4.8 points on spot 100


def _row(typ, k, exp=EXP, size=10, spread=0.01, vwap=None, d=ENTRY):
    return {"option_chain_id": f"SPY{exp.strftime('%y%m%d')}{'C' if typ == 'call' else 'P'}{int(k * 1000):08d}",
            "underlying_symbol": "SPY", "option_type": typ, "strike": float(k), "expiry": exp, "date": d,
            "dte_cal": (exp - d).days, "vwap_late": vwap if vwap is not None else (2.5 if k in (95.0, 105.0) else 0.8),
            "size_late": size, "late_rel_spread": spread, "late_last_bid": None, "late_last_ask": None,
            "last_nbbo_bid": None, "last_nbbo_ask": None, "last_price": 1.0, "n_prints": 20, "last_ts": pd.Timestamp("2026-07-10 15:59:00"),
            "underlying_last": 100.0}


def _rows(include_c2=True, p1_spread=0.01):
    rows = [_row("put", 95, spread=p1_spread), _row("put", 90), _row("call", 105), _row("put", 94, size=2),
            _row("put", 96, exp=date(2026, 7, 24)), _row("put", 100, exp=date(2026, 8, 7)),
            _row("call", 100, exp=EXP, vwap=4.0)]
    if include_c2:
        rows.append(_row("call", 110, vwap=0.1, spread=0.2))
    return pd.DataFrame(rows)


def _on():
    return G.GateState(ENTRY, date(2026, 7, 9), 18.0, 20.0, 18.0, 16.0, True, True, True, True, "ON")


def test_entry_candidates_build_ps_and_ic_with_every_leg_at_tier_one():
    res = sb.entry_candidates("SPY", ENTRY, _rows(), _on(), X, SB_PARAMS, SB_SIZING, cal.is_trading_day)
    assert [t["structure"] for t in res.trades] == ["PS", "IC"] and res.skipped == []
    ps = res.trades[0]
    assert ps["expiry"] == EXP and ps["k_p1"] == 95.0 and ps["k_p2"] == 90.0
    assert ps["p1_entry_tier"] == 1 and ps["p2_entry_tier"] == 1 and ps["entry_tier_max"] == 1
    assert ps["credit_entry"] == pytest.approx(2.5 - 0.8)
    assert ps["max_loss_usd"] == pytest.approx((5.0 - 1.7) * 100)
    assert ps["n"] == max(1, int(SB_SIZING.max_loss_frac * SB_SIZING.equity // ps["max_loss_usd"]))
    assert ps["ticker"] == "SPY" and ps["variant"] == "B1" and ps["pre"] == ENTRY and ps["post"] == EXP
    assert ps["gate_reason"] == "ON" and ps["window"] == "P3" and ps["graded"] is False
    assert pd.isna(ps["net_usd"]) and pd.isna(ps["ror"])
    ic = res.trades[1]
    assert (ic["k_c1"], ic["k_c2"]) == (105.0, 110.0) and ic["c2_entry_spread"] == 0.2
    assert ic["credit_entry"] == pytest.approx(1.7 + 2.5 - 0.1)
    legs = json.loads(ic["legs_json"])
    assert [l["name"] for l in legs] == ["p1", "p2", "c1", "c2"] and all(l["entry_tier"] == 1 for l in legs)


def test_gate_off_or_unknown_skips_everything_with_the_reason():
    off = G.GateState(ENTRY, date(2026, 7, 9), 18.0, 17.0, 18.0, 16.0, False, True, False, True, "OFF:G1")
    res = sb.entry_candidates("SPY", ENTRY, _rows(), off, X, SB_PARAMS, SB_SIZING, cal.is_trading_day)
    assert res.trades == [] and {s["reason"] for s in res.skipped} == {"OFF:G1"} and len(res.skipped) == 2
    unk = G.GateState(ENTRY, None, None, None, None, None, None, None, False, False, "UNKNOWN:no row")
    res = sb.entry_candidates("SPY", ENTRY, _rows(), unk, X, SB_PARAMS, SB_SIZING, cal.is_trading_day)
    assert res.trades == [] and res.skipped[0]["reason"].startswith("UNKNOWN")


def test_missing_wing_drops_only_the_condor_and_a_wide_short_leg_drops_both():
    res = sb.entry_candidates("SPY", ENTRY, _rows(include_c2=False), _on(), X, SB_PARAMS, SB_SIZING, cal.is_trading_day)
    assert [t["structure"] for t in res.trades] == ["PS"]
    assert res.skipped[0]["structure"] == "IC" and res.skipped[0]["reason"] == "no_tier1_c2"
    res = sb.entry_candidates("SPY", ENTRY, _rows(p1_spread=0.11), _on(), X, SB_PARAMS, SB_SIZING, cal.is_trading_day)
    assert res.trades == [] and {s["reason"] for s in res.skipped} == {"spread_p1"}


def test_no_friday_expiry_in_range_skips_with_no_expiry():
    rows = _rows().assign(expiry=date(2026, 8, 14))                       # 35 days: outside [7, 30]
    res = sb.entry_candidates("SPY", ENTRY, rows, _on(), X, SB_PARAMS, SB_SIZING, cal.is_trading_day)
    assert res.trades == [] and {s["reason"] for s in res.skipped} == {"no_expiry"}


def test_grade_position_settles_at_intrinsic_and_prices_costs_by_hand():
    ps = sb.entry_candidates("SPY", ENTRY, _rows(), _on(), X, SB_PARAMS, SB_SIZING, cal.is_trading_day).trades[0]
    g = sb.grade_position(ps, settle_close=92.0, settle_source="prices")
    n = ps["n"]
    assert g["graded"] is True and g["debit_exit"] == pytest.approx(3.0) and g["exit_tier_max"] == 4
    entry_cost = n * ((0.5 * 0.01 * 2.5 * 100 + COMMISSION_PER_CONTRACT) + (0.5 * 0.01 * 0.8 * 100 + COMMISSION_PER_CONTRACT))
    net = (1.7 - 3.0) * 100 * n - entry_cost - 2 * n * COMMISSION_PER_CONTRACT
    assert g["net_usd"] == pytest.approx(net) and g["ror"] == pytest.approx(net / (ps["max_loss_usd"] * n))
    assert g["settle_close"] == 92.0 and g["settle_source"] == "prices" and g["p1_exit"] == 3.0 and g["p2_exit"] == 0.0
    beyond = sb.grade_position(ps, settle_close=80.0, settle_source="prices")
    assert beyond["ror"] == pytest.approx(-1.0 - beyond["cost_usd"] / (ps["max_loss_usd"] * n))


def _index_vol():
    days = cal.trading_days(date(2026, 5, 1), date(2026, 8, 31))
    vix = [19.0 + 0.02 * i for i in range(len(days))]          # ~20 by July: matches the strike fixtures
    return pd.DataFrame({"date": days, "vix": vix, "vix3m": [v + 2 for v in vix], "vxn": [v + 5 for v in vix], "vix9d": vix})


def test_run_marked_is_chronological_grades_what_has_settled_and_is_deterministic():
    sessions = cal.trading_days(date(2026, 6, 1), date(2026, 8, 7))
    entry_rows = {}
    for d in (date(2026, 7, 10), date(2026, 7, 17)):
        df = _rows()
        df = df.assign(date=d, expiry=df.expiry + (d - ENTRY), dte_cal=lambda f: (f.expiry - d).map(lambda x: x.days))
        df["option_chain_id"] = [f"SPY{e.strftime('%y%m%d')}{'C' if t == 'call' else 'P'}{int(k * 1000):08d}" for e, t, k in zip(df.expiry, df.option_type, df.strike)]
        entry_rows[d] = df
    closes = {("SPY", d): 100.0 for d in sessions if d <= date(2026, 7, 31)}   # 08-07 close unknown yet
    closes[("SPY", date(2026, 7, 31))] = 92.0                      # first cohort settles inside the wings
    trades, skipped = sb.run_marked(entry_rows, _index_vol(), closes, sessions, SB_PARAMS, SB_SIZING)
    again, _ = sb.run_marked(entry_rows, _index_vol(), closes, sessions, SB_PARAMS, SB_SIZING)
    pd.testing.assert_frame_equal(trades, again)
    assert len(trades) == 4 and set(trades.entry) == {date(2026, 7, 10), date(2026, 7, 17)}
    first = trades[trades.entry == date(2026, 7, 10)]
    assert first.graded.all() and (first.settle_close == 92.0).all()
    second = trades[trades.entry == date(2026, 7, 17)]
    assert (~second.graded).all() and second.net_usd.isna().all()        # expiry 08-07: no close yet -> open
    assert set(skipped.reason) <= {"no_prints", "OFF:G1", "OFF:G2", "OFF:G1,G2"} or skipped.empty
