"""DESIGN/70 §8: `report.md` renders from `ticker.json` alone and survives every null."""
from __future__ import annotations

import pytest

from engine.name import report as R

pytestmark = pytest.mark.unit


def _base():
    return {"source": {}, "nulls": []}


def all_null_sheet() -> dict:
    return {
        "schema": "n1.0", "policy_id": "sheet-1.0", "ticker": "BL", "date": "2026-09-18", "generated": "x", "E": 100000.0,
        "direction": None,
        "liquidity": {**_base(), "can_price": False, "failing": "L3", "contracts": 15, "hot_chain_days": 3, "adv_usd": None,
                      "atm_spread": None, "tier": None},
        "events": {**_base(), "earnings": {"date": None, "session": None, "sources": [{"name": "finnhub", "date": None},
                                                                                     {"name": "screener", "date": None},
                                                                                     {"name": "yfinance", "date": None}],
                                           "confirmed": False, "days_to": None}, "ex_div": None, "expiries": [], "macro": []},
        "premium": {**_base(), "iv30d": None, "iv_pct_own": None, "rv5_21": None, "rv_c2c_21": None, "spread_rv5": None,
                    "spread_c2c": None, "slope": None, "earnings_history": [], "median_ratio_8": None,
                    "sc": {"pass": False, "failing": None}, "sa": None, "verdict": "CANNOT_MEASURE", "x1": True},
        "range": {**_base(), "straddle_front": None, "box_1s_front": None, "box_1s_21": None, "atr14": None, "gex_sign": None,
                  "zero_gamma": None},
        "flags": {**_base(), "borrow": None, "si": None, "beta_250": None, "analyst": [], "form4": None, "vix": None,
                  "regime": None, "x2": False, "x5": False},
        "context": {**_base(), "ret_21": None, "ret_63": None, "w52_pos": None, "flow_pct_universe": None, "flow_pct_self": None,
                    "sentence": "Direction: no input on this sheet has a measured directional edge at 1–4 weeks; the engine emits none."},
        "structures": [], "ledger_rows": [], "context_read": "none", "inputs_dir": "x",
        "nulls": [{"field": "premium.rv5_21", "reason": "fewer than 15 quality sessions"}],
    }


def test_all_null_sheet_renders_every_section():
    md = R.render(all_null_sheet())
    for tag in ("A  CANNOT_PRICE (L3)", "B  Earnings", "C  Premium CANNOT_MEASURE", "D  Range", "E  Flags", "F  Direction",
                "G  Structures: none", "H  Ledger: no row", "nulls: premium.rv5_21"):
        assert tag in md, tag


def test_structures_and_ledger_rows_render():
    t = all_null_sheet()
    t["liquidity"].update(can_price=True, failing=None, contracts=2051, hot_chain_days=21, adv_usd=1.84e10, atm_spread=0.018, tier=1)
    t["structures"] = [{"family": "IB", "legs": [{"right": "P", "strike": 208.0, "side": 1}, {"right": "C", "strike": 237.0, "side": 1}],
                        "expiry": "2026-10-16", "mark": 7.4, "mark_source": "cboe_chain 2026-09-18", "max_loss": 710.0,
                        "credit_debit": "credit", "breakevens": [215.1, 229.9], "p_inside": 0.42, "cost": 31.0, "n": 7,
                        "usd_at_risk": 4970.0, "excluded_by": None, "note": None},
                       {"family": "SHARES", "legs": [], "expiry": None, "mark": None, "mark_source": "s", "max_loss": 10.4,
                        "credit_debit": None, "breakevens": [], "p_touch": 0.3, "cost": 0.2, "n": 48, "usd_at_risk": 499.0,
                        "excluded_by": "X2", "note": None, "entry": 222.27, "stop": 211.9, "target": 243.0}]
    t["ledger_rows"] = [{"policy_id": "sheet-1.0", "role": "exploration", "gate_verdict": "F3", "structure": "IB", "written": True, "reason": None}]
    t["direction"] = "short"
    md = R.render(t)
    assert "G  Structures (expiry 2026-10-16)" in md and "IB " in md and "[X2]" in md and "n=7" in md
    assert "H  Ledger: sheet-1.0 exploration IB [F3] written · context_read none" in md
    assert "DIRECTION short" in md and "A  CAN_PRICE   contracts 2,051" in md
