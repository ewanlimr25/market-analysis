"""S-C R2 (DESIGN/90 §3, §4, §10): SS / IB legs, pricing through the marking engine, max and stress
loss, sizing, caps. Hand-computed cases; a tier-3 wing takes the 5% spread floor; expiry costs nothing."""
from __future__ import annotations

import json
import math
from dataclasses import replace
from datetime import date

import pandas as pd
import pytest

from engine import marking as M
from engine.config import SC_SIZING
from engine.strategies import sc_filters as F
from engine.strategies import sc_structures as S

pytestmark = pytest.mark.unit

ENTRY = date(2026, 7, 10)
EXP = date(2026, 8, 7)                                       # 28 calendar days
CLOSE, IV = 50.0, 0.45
SIGMA = F.sigma_hold(CLOSE, IV, 28)                          # 50 x 0.45 x sqrt(28/365) = 6.2318


def _contract(option_type: str, strike: float, vwap: float, spread: float = 0.05, size_late: int = 40) -> dict:
    return {"underlying_symbol": "ACME", "option_type": option_type, "strike": strike, "expiry": EXP,
            "size_late": size_late, "vwap_late": vwap, "late_rel_spread": spread, "late_last_bid": None,
            "late_last_ask": None, "last_nbbo_bid": None, "last_nbbo_ask": None}


def _rows() -> pd.DataFrame:
    """ATM 50 pair (call 3.00, put 2.80) on a $1 grid printed 45..55; the wings (62, 38) never printed."""
    recs = [_contract("call", 50.0, 3.00), _contract("put", 50.0, 2.80)]
    recs += [_contract(t, float(k), 1.0) for k in range(45, 56) if k != 50 for t in ("call", "put")]
    return pd.DataFrame(recs)


def _ev(**over) -> dict:
    rows = _rows()
    pair = F.select_atm_pair(rows, CLOSE)
    base = {"ticker": "ACME", "entry": ENTRY, "sector": "Healthcare", "expiry": EXP, "dte_cal": 28, "pair": pair,
            "sigma_hold": SIGMA, "mean_spread": pair.mean_spread, "close": CLOSE, "reason": None}
    return {**base, **over}


class FixedResolver:
    """Wing marks by option type, for hand-computed cases."""

    def __init__(self, marks: dict[str, M.Mark | None]):
        self.marks = marks

    def mark(self, contract: M.Contract, d: date, when: str) -> M.Mark | None:
        return self.marks.get(contract.option_type)


WINGS = FixedResolver({"call": M.Mark(0.30, 0.10, 2, M.SOURCE_PRINT_NBBO), "put": M.Mark(0.40, 0.05, 3, M.SOURCE_MODEL)})
BIG = replace(SC_SIZING, equity=1_000_000.0)


# ---- geometry ------------------------------------------------------------------------------------

def test_sigma_and_wings_round_to_the_grid_including_unprinted_strikes():
    assert SIGMA == pytest.approx(6.2318, abs=1e-4)
    grid = S.strike_grid(_rows())
    assert S.wing_strikes(CLOSE, SIGMA, grid) == (62.0, 38.0)       # 62.46 -> 62, 37.54 -> 38


# ---- SS ------------------------------------------------------------------------------------------

def test_ss_hand_computed_credit_stress_size_and_cost():
    out = S.build(_ev(), _rows(), WINGS, BIG)
    ss = out.structures["SS"]
    assert ss["credit_entry"] == pytest.approx(5.80)
    assert ss["stress_loss_usd"] == pytest.approx((3 * SIGMA - 5.80) * 100)       # 1289.54
    assert ss["contracts"] == 7                                                    # floor(10,000 / 1289.54)
    assert ss["entry_cost_usd"] == pytest.approx((8.15 + 7.65) * 7)                # half-spread x mark x 100 + 0.65
    assert ss["risk_usd"] == pytest.approx(ss["stress_loss_usd"] * 7)
    assert ss["entry_tier_max"] == 1 and not ss["model_entry"]


def test_ss_stress_is_the_worse_side_when_the_strike_is_off_spot():
    assert S.ss_stress_loss_usd(50.4, 50.0, SIGMA, 5.80) == pytest.approx((50.4 + 3 * SIGMA - 50.0 - 5.80) * 100)
    assert S.ss_stress_loss_usd(50.0, 50.0, 0.1, 5.80) == pytest.approx(1.0)      # floored at MIN_RISK_USD


def test_sizing_floors_at_one_contract():
    out = S.build(_ev(), _rows(), WINGS, SC_SIZING)                                # E = $100k
    assert out.structures["SS"]["contracts"] == 1 and out.structures["IB"]["contracts"] == 1


# ---- IB ------------------------------------------------------------------------------------------

def test_ib_hand_computed_credit_max_loss_size_and_cost():
    ib = S.build(_ev(), _rows(), WINGS, BIG).structures["IB"]
    assert (ib["k"], ib["k_up"], ib["k_dn"]) == (50.0, 62.0, 38.0)
    assert ib["credit_entry"] == pytest.approx(5.10)                               # 5.80 - 0.30 - 0.40
    assert ib["max_loss_usd"] == pytest.approx((12 - 5.10) * 100)                  # 690
    assert ib["contracts"] == 7                                                    # floor(5,000 / 690)
    assert ib["entry_cost_usd"] == pytest.approx((8.15 + 7.65 + 2.15 + 1.65) * 7)
    assert ib["entry_tier_max"] == 3 and ib["model_entry"]
    legs = json.loads(ib["legs_json"])
    assert [(l["name"], l["side"], l["strike"]) for l in legs] == [("call", -1, 50.0), ("put", -1, 50.0),
                                                                    ("wing_call", 1, 62.0), ("wing_put", 1, 38.0)]


def test_a_tier_3_wing_takes_the_five_percent_floor_through_the_real_resolver():
    resolver = M.MarkResolver({}, lambda c, d, w: M.ModelInputs(spot=CLOSE, iv=IV, rel_spread=0.01))
    ib = S.build(_ev(), _rows(), resolver, BIG).structures["IB"]
    legs = {l["name"]: l for l in json.loads(ib["legs_json"])}
    assert legs["wing_put"]["entry_tier"] == 3 and legs["wing_put"]["entry_spread"] == pytest.approx(M.MODEL_SPREAD_FLOOR)
    assert legs["wing_call"]["entry_tier"] == 3 and legs["wing_call"]["entry_spread"] == pytest.approx(M.MODEL_SPREAD_FLOOR)


def test_an_unmarkable_wing_drops_the_ib_and_keeps_the_ss():
    out = S.build(_ev(), _rows(), FixedResolver({"call": None, "put": M.Mark(0.4, 0.05, 3, M.SOURCE_MODEL)}), BIG)
    assert set(out.structures) == {"SS"} and out.dropped == [{"ticker": "ACME", "entry": ENTRY, "structure": "IB",
                                                               "reason": S.REASON_UNMARKABLE_WING}]


def test_degenerate_wings_drop_the_ib():
    out = S.build(_ev(sigma_hold=0.1), _rows(), WINGS, BIG)                        # wings round onto the ATM strike
    assert "IB" not in out.structures and out.dropped[0]["reason"] == S.REASON_DEGENERATE


def test_a_name_that_failed_a_filter_builds_nothing():
    with pytest.raises(ValueError):
        S.build(_ev(reason="F8", pair=None), _rows(), WINGS, BIG)


# ---- settlement: intrinsic at the expiry close, no cost ----------------------------------------------

def test_settle_ss_at_expiry_costs_nothing():
    ss = S.build(_ev(), _rows(), WINGS, SC_SIZING).structures["SS"]
    g = S.settle(ss, 55.0)
    assert g["debit_exit"] == pytest.approx(5.00) and g["exit_cost_usd"] == 0.0
    assert g["gross_usd"] == pytest.approx(80.0) and g["net_usd"] == pytest.approx(80.0 - 15.80)
    assert g["exit_tier_max"] == 4


def test_settle_ib_through_a_wing_loses_exactly_max_loss_plus_entry_cost():
    ib = S.build(_ev(), _rows(), WINGS, SC_SIZING).structures["IB"]
    g = S.settle(ib, 70.0)                                                         # call 20 - wing 8 = 12
    assert g["gross_usd"] == pytest.approx(-ib["max_loss_usd"])
    assert g["net_usd"] == pytest.approx(-690.0 - 19.60)


# ---- caps (§4) ---------------------------------------------------------------------------------

def _cand(i: int, sector: str = "Energy", risk: float = 500.0, structure: str = "IB", variant: str = "C1") -> dict:
    return {"ticker": f"T{i:02d}", "rank": i + 1, "sector": sector, "risk_usd": risk, "structure": structure,
            "variant": variant}


def test_caps_new_per_week_and_sector_in_rank_order():
    cands = [_cand(i, sector="Energy" if i < 5 else f"S{i}") for i in range(12)]
    out = S.apply_caps(cands, [], SC_SIZING, sb_open=False)
    assert [r["cap_pass"] for r in out] == [True] * 4 + [False] + [True] * 6 + [False]
    assert out[4]["cap_reason"] == S.CAP_SECTOR and out[11]["cap_reason"] == S.CAP_NEW_WEEK


def test_caps_count_the_open_book_per_sleeve():
    open_ = [_cand(90 + i, sector=f"O{i}") for i in range(19)] + [_cand(80, sector="Energy", structure="SS")]
    out = S.apply_caps([_cand(0), _cand(1, sector="Tech")], open_, SC_SIZING, sb_open=False)
    assert [r["cap_pass"] for r in out] == [True, False] and out[1]["cap_reason"] == S.CAP_OPEN
    sector_full = [_cand(70 + i, sector="Energy") for i in range(4)]
    assert S.apply_caps([_cand(0)], sector_full, SC_SIZING, sb_open=False)[0]["cap_reason"] == S.CAP_SECTOR


def test_the_book_budget_binds_only_while_sb_is_open():
    budget = S.book_budget_usd("IB", SC_SIZING)
    assert budget == pytest.approx(0.40 * 20 * 0.005 * 100_000)                    # $4,000
    cands = [_cand(i, sector=f"S{i}", risk=1_500.0) for i in range(3)]
    assert [r["cap_pass"] for r in S.apply_caps(cands, [], SC_SIZING, sb_open=True)] == [True, True, False]
    assert S.apply_caps(cands, [], SC_SIZING, sb_open=True)[2]["cap_reason"] == S.CAP_BUDGET
    assert all(r["cap_pass"] for r in S.apply_caps(cands, [], SC_SIZING, sb_open=False))
    assert not math.isnan(S.book_budget_usd("SS", SC_SIZING))
