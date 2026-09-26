"""S-C R3 (DESIGN/90 §3, §10): the weekly run over synthetic `daily_contract` rows -- F10 selection,
the suppressed table, structures and caps, settlement with `settle_source` and `corporate_action`
(split inside the window, a name that stopped trading), two runs identical, every leg a tier and a cost."""
from __future__ import annotations

import json
from datetime import date

import pandas as pd
import pytest

from engine.config import SC_SIZING
from engine.strategies import sc as SC
from sc_fixtures import Wings, chain as _chain, is_session as _is_session, screener as _screener, week as _week

pytestmark = pytest.mark.unit

T1, T2 = date(2026, 7, 10), date(2026, 7, 17)            # two entry Fridays
X1, X2 = date(2026, 8, 7), date(2026, 8, 14)             # 28 days after each


def test_entry_week_selects_builds_and_suppresses():
    wk = SC.entry_week(_week(T1, X1), SC_SIZING, is_session=_is_session)
    sel = {(r["variant"], r["ticker"], r["structure"]) for r in wk.candidates}
    assert sel == {("C1", "AAA", "SS"), ("C1", "AAA", "IB"), ("C1", "BBB", "SS"), ("C1", "BBB", "IB"),
                   ("C2", "AAA", "SS"), ("C2", "AAA", "IB")}                     # BBB is Technology
    ranks = {(r["variant"], r["ticker"]): r["rank"] for r in wk.candidates}
    assert ranks[("C1", "AAA")] == 1 and ranks[("C1", "BBB")] == 2               # lower spread first
    reasons = {(r["ticker"], r.get("variant")): r["reason"] for r in wk.suppressed}
    assert reasons[("CCC", None)] == "F3" and reasons[("DDD", None)] == "F8"
    assert reasons[("BBB", "C2")] == SC.REASON_C2
    assert all(r["policy_id"] == "sc-1.0" and r["role"] == "champion" for r in wk.candidates)


def test_every_leg_carries_a_tier_and_every_row_an_entry_cost():
    wk = SC.entry_week(_week(T1, X1), SC_SIZING, is_session=_is_session)
    for r in wk.candidates:
        legs = json.loads(r["legs_json"])
        assert all(l["entry_tier"] in (1, 2, 3) and l["entry_spread"] == l["entry_spread"] for l in legs)
        assert r["entry_cost_usd"] > 0


# ---- settlement ----------------------------------------------------------------------------------

def test_settlement_prefers_prices_then_prints_then_nothing():
    closes = {("AAA", T1): 50.0, ("AAA", X1): 55.0}
    s = SC.settlement_for("AAA", T1, X1, 50.0, closes, {}, prices_through=X1)
    assert (s.close, s.source, s.corporate_action, s.split_factor) == (55.0, "prices", None, 1.0)
    s = SC.settlement_for("AAA", T1, X1, 50.0, {("AAA", T1): 50.0}, {("AAA", X1): 54.0}, prices_through=T1)
    assert (s.close, s.source) == (54.0, "daily_contract")
    s = SC.settlement_for("AAA", T1, X1, 50.0, {("AAA", T1): 50.0}, {}, prices_through=T1)
    assert s.close is None and s.source is None                                  # not observable yet


def test_a_split_inside_the_window_settles_in_entry_share_terms():
    # 2:1 split between entry and expiry; Yahoo closes are split-adjusted, the screener close is not.
    closes = {("AAA", T1): 25.0, ("AAA", X1): 27.5}
    s = SC.settlement_for("AAA", T1, X1, 50.0, closes, {}, prices_through=X1)
    assert s.split_factor == pytest.approx(2.0) and s.close == pytest.approx(55.0)
    assert s.corporate_action == SC.CA_SPLIT and s.source == "prices"
    small = SC.settlement_for("AAA", T1, X1, 50.6, {("AAA", T1): 50.0, ("AAA", X1): 55.0}, {}, prices_through=X1)
    assert small.split_factor == 1.0 and small.corporate_action is None           # last print vs close: noise


def test_a_name_that_stopped_trading_settles_at_its_last_close_flagged():
    closes = {("AAA", T1): 50.0, ("AAA", date(2026, 7, 28)): 61.0, ("ZZZ", X1): 1.0}
    s = SC.settlement_for("AAA", T1, X1, 50.0, closes, {}, prices_through=X1)
    assert (s.close, s.source, s.corporate_action) == (61.0, "last_close", SC.CA_DELISTED)


# ---- the run -------------------------------------------------------------------------------------

def _closes() -> dict:
    out = {}
    for name in ("AAA", "BBB", "DDD"):
        out.update({(name, T1): 50.0, (name, T2): 50.0, (name, X1): 55.0, (name, X2): 50.0})
    return out


def test_run_grades_caps_and_is_identical_twice():
    weeks = [_week(T1, X1), _week(T2, X2)]
    a = SC.run(weeks, _closes(), {}, prices_through=X2, sb_open_on=lambda d: False, is_session=_is_session)
    b = SC.run(weeks, _closes(), {}, prices_through=X2, sb_open_on=lambda d: False, is_session=_is_session)
    pd.testing.assert_frame_equal(a.trades, b.trades)
    pd.testing.assert_frame_equal(a.suppressed, b.suppressed)
    t = a.trades
    assert len(t) == 12 and t["graded"].all() and t["cap_pass"].all()
    ss = t[(t.ticker == "AAA") & (t.entry == T1) & (t.variant == "C1") & (t.structure == "SS")].iloc[0]
    assert ss["settle_close"] == 55.0 and ss["gross_usd"] == pytest.approx(80.0 * ss["contracts"])
    assert ss["ror"] == pytest.approx(ss["net_usd"] / ss["risk_usd"]) and ss["exit_cost_usd"] == 0.0
    assert set(t["settle_source"]) == {"prices"} and t["corporate_action"].isna().all()


def test_run_counts_the_open_book_across_weeks():
    tight = SC_SIZING.__class__(**{**SC_SIZING.__dict__, "max_open_per_variant": 2})
    weeks = [_week(T1, X1), _week(T2, X2)]
    t = SC.run(weeks, _closes(), {}, prices_through=X2, sb_open_on=lambda d: False, sizing=tight,
               is_session=_is_session).trades
    c1_ib = t[(t.variant == "C1") & (t.structure == "IB")].sort_values(["entry", "rank"])
    assert list(c1_ib["cap_pass"]) == [True, True, False, False]                 # week 1 still open on T2
    assert list(c1_ib["cap_reason"].fillna("")) == ["", "", SC.CAP_OPEN, SC.CAP_OPEN]


def test_an_unsettled_position_stays_ungraded():
    t = SC.run([_week(T1, X1)], {("AAA", T1): 50.0, ("BBB", T1): 50.0}, {}, prices_through=T1,
               sb_open_on=lambda d: False, is_session=_is_session).trades
    assert not t["graded"].any() and t["net_usd"].isna().all()


def test_a_week_with_no_selection_after_an_open_book_is_fine():
    empty = SC.WeekInput(T2, pd.DataFrame([_screener("CCC", marketcap=40e9)]), pd.DataFrame(), lambda names: Wings())
    t = SC.run([_week(T1, X1), empty], _closes(), {}, prices_through=X2, sb_open_on=lambda d: False,
               is_session=_is_session).trades
    assert len(t) == 6 and set(t["entry"]) == {T1}


# ---- the exploration book (DESIGN/100 §6, D22; S-A's pattern) ------------------------------------

def test_exploration_takes_every_priceable_pair_whatever_the_filters_say():
    wk = _week(T1, X1)
    rows = SC.exploration_week(wk, is_session=_is_session)
    got = {(r["ticker"], r["structure"]): r["gate_verdict"] for r in rows}
    assert got == {("AAA", "SS"): "PASS", ("AAA", "IB"): "PASS", ("BBB", "SS"): "PASS", ("BBB", "IB"): "PASS",
                   ("CCC", "SS"): "F3", ("CCC", "IB"): "F3"}                      # CCC: $40B; DDD has no pair
    assert all(r["role"] == "exploration" and r["variant"] == "C1" and r["contracts"] == 1 for r in rows)
    assert all(r["policy_id"] == "sc-1.0" for r in rows)


def test_exploration_marks_the_f10_cut():
    names = {f"N{i:02d}": 0.02 + 0.001 * i for i in range(11)}
    universe = pd.DataFrame([_screener(n) for n in names])
    rows = []
    for n, sp in names.items():
        rows += _chain(n, X1, spread=sp)
    wk = SC.WeekInput(T1, universe, pd.DataFrame(rows), lambda names: Wings())
    verdicts = {r["ticker"]: r["gate_verdict"] for r in SC.exploration_week(wk, is_session=_is_session)}
    assert verdicts["N10"] == SC.REASON_F10 and verdicts["N00"] == "PASS"
