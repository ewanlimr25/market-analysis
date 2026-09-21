"""R5 grader (findings/stock-deep-dive DESIGN/70 §6, §9, §10 R5).

The share walk is the port of `artifacts/outcomes/15_trade_plans.py::mtm` and `11_path_r.py::walk`
(the corrected `mark_to_market.py`: a bar that touches both levels is LOSS, and the `limit` fill
requires the entry to trade). The reproduction test is the acceptance criterion in DESIGN/70 §10 R5:
every row of `results/G_plans_stock.csv` at review 2026-09-18 on the nine old trade plans.

`grade_vertical` is cross-checked against the 119 expired rows of `results/CD_structure_rows.csv`,
which were priced by `artifacts/outcomes/lib.py::payoff_at` with an independent max-loss formula.
"""
from __future__ import annotations

import math
import os
from datetime import date

import pandas as pd
import pytest

from engine.name import grade as G

pytestmark = pytest.mark.unit

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures", "name")
PLAN_BARS = os.path.join(FIXTURES, "plans_bars.parquet")
SEED_REAL = os.path.join(FIXTURES, "seed", "real")
REVIEW = date(2026, 9, 18)
COLS = ["date", "open", "high", "low", "close"]


def bars(*rows) -> pd.DataFrame:
    """rows: (day-of-month in 2026-06, open, high, low, close)."""
    return pd.DataFrame([(date(2026, 6, d), o, h, lo, c) for d, o, h, lo, c in rows], columns=COLS)


def walk(b: pd.DataFrame, **kw) -> dict:
    args = dict(entry_after=date(2026, 6, 1), direction="long", entry=100.0, stop=90.0, target=120.0,
                horizon_sessions=10, fill="limit")
    args.update(kw)
    return G.walk_shares(b, **args)


# ---- the branches of the walk --------------------------------------------------------------------

def test_win_pays_the_plans_own_reward_not_one_r():
    b = bars((2, 100, 101, 99, 100), (3, 100, 121, 99, 120))
    out = walk(b)
    assert out["outcome"] == "WIN" and out["r"] == pytest.approx(2.0)
    assert out["event_date"] == date(2026, 6, 3) and out["fill_date"] == date(2026, 6, 2)


def test_loss_is_minus_one_r_on_the_stop():
    b = bars((2, 100, 101, 99, 100), (3, 100, 101, 89, 90))
    out = walk(b)
    assert out["outcome"] == "LOSS" and out["r"] == -1.0 and out["event_date"] == date(2026, 6, 3)


def test_a_bar_touching_both_stop_and_target_is_scored_loss():
    b = bars((2, 100, 121, 89, 100))
    out = walk(b)
    assert out["outcome"] == "LOSS" and out["r"] == -1.0


def test_limit_fill_requires_the_entry_to_trade():
    b = bars((2, 105, 108, 104, 107), (3, 107, 130, 106, 129))
    assert walk(b)["outcome"] == "NO_FILL"
    assert walk(b)["r"] is None and walk(b)["fill_date"] is None
    assert walk(b)["last_close"] == pytest.approx(129.0)


def test_instant_fill_opens_on_the_first_session_whatever_traded():
    b = bars((2, 105, 108, 104, 107), (3, 107, 130, 106, 129))
    out = walk(b, fill="instant")
    assert out["outcome"] == "WIN" and out["fill_date"] == date(2026, 6, 2)


def test_open_carries_the_signed_close_and_no_event_date():
    b = bars((2, 100, 101, 99, 100), (3, 100, 105, 99, 105))
    out = walk(b)
    assert out["outcome"] == "OPEN" and out["r"] == pytest.approx(0.5) and out["event_date"] is None
    assert out["mfe_r"] == pytest.approx(0.5) and out["mae_r"] == pytest.approx(0.1)


def test_no_data_when_no_session_follows_the_decision():
    assert walk(bars((2, 100, 101, 99, 100)), entry_after=date(2026, 6, 2))["outcome"] == "NO_DATA"
    assert walk(pd.DataFrame(columns=COLS))["outcome"] == "NO_DATA"


def test_next_open_resets_the_entry_and_shifts_stop_and_target_by_the_same_amount():
    b = bars((2, 110, 112, 108, 111), (3, 111, 131, 110, 130))
    out = walk(b, fill="next_open")
    # entry 110 (the open), stop 100, target 130: the same 10-point risk, hit on the second bar
    assert out["outcome"] == "WIN" and out["r"] == pytest.approx(2.0) and out["fill_date"] == date(2026, 6, 2)


def test_short_direction_mirrors_the_levels():
    b = bars((2, 100, 101, 99, 100), (3, 100, 101, 79, 80))
    out = walk(b, direction="short", stop=110.0, target=80.0)
    assert out["outcome"] == "WIN" and out["r"] == pytest.approx(2.0)
    out = walk(bars((2, 100, 111, 99, 110)), direction="short", stop=110.0, target=80.0)
    assert out["outcome"] == "LOSS"


def test_horizon_and_through_both_bound_the_window():
    b = bars((2, 100, 101, 99, 100), (3, 100, 101, 99, 100), (4, 100, 121, 99, 120))
    assert walk(b, horizon_sessions=2)["outcome"] == "OPEN"
    assert walk(b, through=date(2026, 6, 3))["outcome"] == "OPEN"
    assert walk(b, through=date(2026, 6, 4))["outcome"] == "WIN"
    assert walk(b)["sessions"] == 3


def test_bad_inputs_fail_fast():
    b = bars((2, 100, 101, 99, 100))
    with pytest.raises(ValueError):
        walk(b, direction="up")
    with pytest.raises(ValueError):
        walk(b, fill="market")
    with pytest.raises(ValueError):
        walk(b, stop=100.0)


def test_the_walk_does_not_mutate_the_bars_it_is_given():
    b = bars((2, 100, 101, 99, 100), (3, 100, 121, 99, 120))
    before = b.copy()
    walk(b, fill="next_open")
    pd.testing.assert_frame_equal(b, before)


# ---- the nine trade plans (DESIGN/70 §9, §10 R5; RESEARCH/15 §G) ---------------------------------

def plan_bars(ticker: str) -> pd.DataFrame:
    b = pd.read_parquet(PLAN_BARS)
    return b[b["ticker"] == ticker][COLS].reset_index(drop=True)


def expected_plans() -> pd.DataFrame:
    g = pd.read_csv(os.path.join(SEED_REAL, "G_plans_stock.csv"))
    return g[g["review"] == "2026-09-18"].reset_index(drop=True)


def same_number(got, want, tol: float = 1e-6) -> bool:
    if want is None or (isinstance(want, float) and math.isnan(want)):
        return got is None
    return got is not None and abs(got - want) <= tol


def same_date(got, want) -> bool:
    if not isinstance(want, str):
        return got is None
    return got == pd.Timestamp(want).date()


@pytest.mark.parametrize("i", range(18))
def test_the_nine_trade_plans_reproduce_the_2026_09_18_review(i):
    row = expected_plans().iloc[i]
    out = G.walk_shares(plan_bars(row.ticker), entry_after=pd.Timestamp(row.plan_date).date(),
                        direction=row.direction, entry=float(row.entry), stop=float(row.stop),
                        target=float(row.t1), horizon_sessions=G.NO_HORIZON, fill=row.fill, through=REVIEW)
    assert out["outcome"] == row.outcome
    assert same_number(out["r"], row.r), (row.ticker, row.fill, out["r"], row.r)
    assert same_number(out["mfe_r"], row.mfe_R) and same_number(out["mae_r"], row.mae_R)
    assert same_date(out["fill_date"], row.fill_date) and same_date(out["event_date"], row.event_date)
    assert out["sessions"] == int(row.sessions)


def test_the_two_plans_named_in_the_spec():
    """DESIGN/70 §9: ELF is a no-fill on limit and a WIN under the fill the old skill assumed."""
    elf = dict(entry_after=date(2026, 6, 30), direction="long", entry=70.0, stop=66.0, target=75.0,
               horizon_sessions=G.NO_HORIZON, through=REVIEW)
    assert G.walk_shares(plan_bars("ELF"), fill="limit", **elf)["outcome"] == "NO_FILL"
    instant = G.walk_shares(plan_bars("ELF"), fill="instant", **elf)
    assert instant["outcome"] == "WIN" and instant["r"] == pytest.approx(1.25)
    path = dict(entry_after=date(2026, 6, 21), direction="short", entry=9.95, stop=10.65, target=9.2,
                horizon_sessions=G.NO_HORIZON, through=REVIEW)
    lim = G.walk_shares(plan_bars("PATH"), fill="limit", **path)
    ins = G.walk_shares(plan_bars("PATH"), fill="instant", **path)
    assert lim["outcome"] == "LOSS" and lim["fill_date"] == date(2026, 6, 25)
    assert ins["outcome"] == "LOSS" and ins["fill_date"] == date(2026, 6, 22)
    assert lim["event_date"] == ins["event_date"] == date(2026, 6, 29)


# ---- defined-risk intrinsic at expiry -------------------------------------------------------------

def leg(right: str, strike: float, side: int, mark: float = 0.0) -> dict:
    return {"right": right, "strike": strike, "side": side, "mark": mark}


def test_debit_vertical_at_max_gain_and_at_max_loss():
    legs = [leg("C", 100, +1, 4.0), leg("C", 110, -1, 1.5)]
    g = G.grade_vertical(legs, 120.0)
    assert g["max_loss_per_share"] == pytest.approx(2.5) and g["payoff_per_share"] == pytest.approx(7.5)
    assert g["ror"] == pytest.approx(3.0) and not g["full_credit"] and not g["at_max_loss"]
    g = G.grade_vertical(legs, 90.0)
    assert g["payoff_per_share"] == pytest.approx(-2.5) and g["ror"] == pytest.approx(-1.0) and g["at_max_loss"]


def test_credit_vertical_expiring_worthless_is_full_credit():
    legs = [leg("P", 95, -1, 2.0), leg("P", 90, +1, 0.8)]
    g = G.grade_vertical(legs, 100.0)
    assert g["payoff_per_share"] == pytest.approx(1.2) and g["full_credit"]
    assert g["max_loss_per_share"] == pytest.approx(3.8) and g["ror"] == pytest.approx(1.2 / 3.8)
    assert G.grade_vertical(legs, 80.0)["at_max_loss"]


def test_iron_butterfly_grades_through_the_same_arithmetic():
    legs = [leg("P", 90, +1, 1.0), leg("P", 100, -1, 4.0), leg("C", 100, -1, 4.0), leg("C", 110, +1, 1.0)]
    g = G.grade_vertical(legs, 100.0)
    assert g["payoff_per_share"] == pytest.approx(6.0) and g["full_credit"]
    assert g["max_loss_per_share"] == pytest.approx(4.0)
    assert G.grade_vertical(legs, 80.0)["payoff_per_share"] == pytest.approx(-4.0)


def test_a_structure_that_cannot_lose_has_no_return_on_risk():
    legs = [leg("C", 100, -1, 5.0), leg("C", 100, +1, 1.0)]   # short the same strike for more than it cost
    g = G.grade_vertical(legs, 130.0)
    assert g["max_loss_per_share"] == pytest.approx(0.0) and g["ror"] is None


def test_grade_vertical_rejects_leg_counts_and_sides_it_cannot_price():
    with pytest.raises(ValueError):
        G.grade_vertical([leg("C", 100, +1, 1.0)], 100.0)
    with pytest.raises(ValueError):
        G.grade_vertical([leg("X", 100, +1, 1.0), leg("C", 110, -1, 0.5)], 100.0)
    with pytest.raises(ValueError):
        G.grade_vertical([leg("C", 100, +2, 1.0), leg("C", 110, -1, 0.5)], 100.0)


def cd_legs(row) -> list[dict]:
    """The old book's legs; only the net of the marks enters the payoff, so the whole premium is
    carried by one leg on the side that paid or received it."""
    legs = [leg(right, float(row[col]), side) for col, right, side in
            (("cl", "C", +1), ("cs", "C", -1), ("pl", "P", +1), ("ps", "P", -1)) if pd.notna(row[col])]
    want = -1 if row["is_credit"] else +1
    for lg in legs:
        if lg["side"] == want:
            lg["mark"] = float(row["premium"])
            break
    return legs


def test_grade_vertical_reproduces_the_old_books_expired_structures():
    cd = pd.read_csv(os.path.join(SEED_REAL, "CD_structure_rows.csv"))
    cd = cd[cd["ok"] & (cd["status"] == "EXPIRED")]
    checked = 0
    for _, row in cd.iterrows():
        legs = cd_legs(row)
        if len(legs) not in (2, 4):
            continue                      # two long single-leg rows: outside the defined-risk contract
        g = G.grade_vertical(legs, float(row["S"]))
        assert g["payoff_per_share"] == pytest.approx(float(row["pnl"]), abs=1e-6), (row["ticker"], row["date"])
        assert g["max_loss_per_share"] == pytest.approx(float(row["max_loss"]), abs=1e-6)
        assert g["ror"] == pytest.approx(float(row["ror"]), abs=1e-6)
        checked += 1
    assert checked == 117
