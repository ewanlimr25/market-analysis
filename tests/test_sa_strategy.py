"""P4: S-A strategy (DESIGN/70 §3) on synthetic daily_contract / earnings_events rows."""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd
import pytest

from engine import marking as M
from engine.config import SA_PARAMS, SIZING, COMMISSION_PER_CONTRACT
from engine.strategies import sa, sa_filters as F, sa_structures as ST
from engine import portfolio

pytestmark = pytest.mark.unit

PRE, POST = date(2026, 7, 29), date(2026, 7, 30)
EXP_W, EXP_M = date(2026, 7, 31), date(2026, 8, 21)


def _event(**kw):
    e = dict(ticker="XYZ", E=POST, pre=PRE, post=POST, timing="postmarket", how="labelled",
             spot_pre=100.0, implied_move_perc=0.08, marketcap=5e9, adv_usd_20d=100e6,
             issue_type="Common Stock", sector="Industrials", iv30d_pre=0.6, iv30d_post=0.4,
             regime_pre="CHOP", vix_pre=17.0, month="2026-07", season="S2",
             realized_move=0.03, gap_signed=-0.03, close_post=97.0)
    e.update(kw)
    return e


def _cid(sym, exp, typ, k):
    return f"{sym}{exp.strftime('%y%m%d')}{'C' if typ == 'call' else 'P'}{int(round(k * 1000)):08d}"


def _row(sym, exp, typ, k, d, **kw):
    r = dict(option_chain_id=_cid(sym, exp, typ, k), underlying_symbol=sym, option_type=typ, strike=float(k),
             expiry=exp, date=d, vwap_late=None, size_late=0, late_rel_spread=None, late_last_bid=None,
             late_last_ask=None, vwap_early=None, size_early=0, early_rel_spread=None, early_last_bid=None,
             early_last_ask=None, last_price=1.0, last_nbbo_bid=0.9, last_nbbo_ask=1.1, n_prints=5,
             size_total=10, iv_vwap=0.6, underlying_last=100.0, dte=2, dte_cal=2)
    r.update(kw)
    return r


def _pre_rows():
    rows = [
        _row("XYZ", EXP_W, "call", 100, PRE, vwap_late=4.0, size_late=30, late_rel_spread=0.06),
        _row("XYZ", EXP_W, "put", 100, PRE, vwap_late=3.6, size_late=25, late_rel_spread=0.07),
        _row("XYZ", EXP_W, "call", 105, PRE, vwap_late=1.8, size_late=40, late_rel_spread=0.05),
        _row("XYZ", EXP_W, "put", 95, PRE, vwap_late=1.5, size_late=40, late_rel_spread=0.05),
        _row("XYZ", EXP_W, "call", 115, PRE, vwap_late=0.5, size_late=12, late_rel_spread=0.20),
        _row("XYZ", EXP_W, "call", 110, PRE, vwap_late=0.9, size_late=3, late_rel_spread=0.10),
        _row("XYZ", EXP_W, "put", 90, PRE, vwap_late=0.8, size_late=50, late_rel_spread=0.10),
        _row("XYZ", EXP_M, "call", 100, PRE, vwap_late=6.0, size_late=100, late_rel_spread=0.03),
        _row("XYZ", EXP_M, "put", 100, PRE, vwap_late=5.5, size_late=100, late_rel_spread=0.03),
        # a same-day expiry (== pre) and one == post must never be selected
        _row("XYZ", PRE, "call", 100, PRE, vwap_late=2.0, size_late=100, late_rel_spread=0.03),
        _row("XYZ", POST, "call", 100, PRE, vwap_late=2.5, size_late=100, late_rel_spread=0.03),
    ]
    return pd.DataFrame(rows)


def _post_rows():
    return pd.DataFrame([
        _row("XYZ", EXP_W, "call", 100, POST, vwap_early=1.2, size_early=20, early_rel_spread=0.05),
        _row("XYZ", EXP_W, "put", 100, POST, vwap_early=1.0, size_early=15, early_rel_spread=0.05),
        _row("XYZ", EXP_W, "put", 85, POST, vwap_early=0.10, size_early=6, early_rel_spread=0.5),
    ])


def _model_inputs(contract, d, when):
    spot = 100.0 if d == PRE else 97.0
    iv = 0.6 if d == PRE else 0.4
    return M.ModelInputs(spot=spot, iv=iv, rel_spread=0.02)


def _resolver(pre=None, post=None):
    rows = {}
    for df in (pre if pre is not None else _pre_rows(), post if post is not None else _post_rows()):
        for r in df.to_dict("records"):
            rows[(r["option_chain_id"], r["date"])] = r
    return M.MarkResolver(rows, _model_inputs)


# ---- filters -------------------------------------------------------------------------------------

def test_cheap_filters_pass_on_the_base_event():
    flags = F.cheap_filters(_event(), SA_PARAMS)
    assert all(flags[f] for f in ("F1", "F2", "F3", "F4", "F7", "F8"))


@pytest.mark.parametrize("field,value,filt", [
    ("issue_type", "ETF", "F1"), ("spot_pre", 9.99, "F2"), ("marketcap", 1.9e9, "F3"),
    ("marketcap", 50.1e9, "F3"), ("adv_usd_20d", 49e6, "F4"), ("implied_move_perc", 0.039, "F7"),
    ("implied_move_perc", 0.151, "F7"), ("timing", "unresolved", "F8"), ("how", "2-session", "F8"),
])
def test_each_cheap_filter_fails_on_its_own_field(field, value, filt):
    flags = F.cheap_filters(_event(**{field: value}), SA_PARAMS)
    assert flags[filt] is False


def test_boundaries_are_inclusive():
    flags = F.cheap_filters(_event(spot_pre=10.0, marketcap=2e9, adv_usd_20d=50e6, implied_move_perc=0.04), SA_PARAMS)
    assert all(flags[f] for f in ("F2", "F3", "F4", "F7"))
    assert F.cheap_filters(_event(marketcap=50e9, implied_move_perc=0.15), SA_PARAMS)["F3"]


def test_a2_sector_exclusion():
    assert F.a2_sector_ok(_event(sector="Technology"), SA_PARAMS) is False
    assert F.a2_sector_ok(_event(sector="Communication Services"), SA_PARAMS) is False
    assert F.a2_sector_ok(_event(sector="Real Estate"), SA_PARAMS) is True


# ---- contract selection ----------------------------------------------------------------------------

def test_select_expiry_is_nearest_strictly_after_post():
    assert F.select_expiry(_pre_rows(), POST) == EXP_W
    assert F.select_expiry(_pre_rows()[_pre_rows().expiry != EXP_W], POST) == EXP_M
    assert F.select_expiry(_pre_rows()[_pre_rows().expiry <= POST], POST) is None


def test_atm_pair_nearest_strike_with_both_legs_qualifying():
    pair = F.select_atm_pair(_pre_rows()[_pre_rows().expiry == EXP_W], spot=100.0, params=SA_PARAMS)
    assert pair is not None and pair.strike == 100.0
    assert pair.call["option_type"] == "call" and pair.put["option_type"] == "put"


def test_atm_pair_skips_a_thin_leg_and_respects_the_band():
    rows = _pre_rows()
    rows = rows[rows.expiry == EXP_W]
    thin = rows.copy()
    thin.loc[thin.strike == 100.0, "size_late"] = SA_PARAMS.leg_size_min - 1
    assert F.select_atm_pair(thin, spot=100.0, params=SA_PARAMS) is None        # 105/95 have no partner leg
    # spot 102.4 -> 100 is inside 2.5% (2.35%); spot 103 -> 100 is 2.9% away: outside
    assert F.select_atm_pair(rows, spot=102.4, params=SA_PARAMS).strike == 100.0
    assert F.select_atm_pair(rows, spot=103.0, params=SA_PARAMS) is None


def test_spread_filter_applies_to_both_legs():
    pair = F.select_atm_pair(_pre_rows()[_pre_rows().expiry == EXP_W], spot=100.0, params=SA_PARAMS)
    assert F.spreads_ok(pair, SA_PARAMS)
    wide = dict(pair.put, late_rel_spread=0.11)
    assert not F.spreads_ok(F.AtmPair(pair.strike, pair.call, wide), SA_PARAMS)
    nan = dict(pair.put, late_rel_spread=None)
    assert not F.spreads_ok(F.AtmPair(pair.strike, pair.call, nan), SA_PARAMS)


def test_strike_grid_and_rounding():
    grid = F.strike_grid(_pre_rows()[_pre_rows().expiry == EXP_W])
    assert grid.increment == 5.0
    assert F.round_to_strike(116.0, grid) == 115.0
    assert F.round_to_strike(84.0, grid) == 85.0          # synthesized on the increment (not printed)
    assert F.round_to_strike(117.6, grid) == 120.0


def test_wing_strikes_at_two_times_implied():
    grid = F.strike_grid(_pre_rows()[_pre_rows().expiry == EXP_W])
    k_up, k_dn = F.wing_strikes(spot=100.0, implied=0.08, grid=grid, params=SA_PARAMS)
    assert (k_up, k_dn) == (115.0, 85.0)


# ---- structures, pricing, sizing ------------------------------------------------------------------

def test_short_straddle_pnl_and_costs_by_hand():
    res = sa.evaluate_event(_event(), _pre_rows(), _resolver(), SA_PARAMS, SIZING)
    ss = [t for t in res.trades if t["structure"] == "SS" and t["variant"] == "A1"][0]
    assert ss["n"] == 1                                            # stress 1640 > 1% of equity -> min 1
    assert ss["credit_entry"] == pytest.approx(7.6)
    assert ss["debit_exit"] == pytest.approx(2.2)
    assert ss["gross_usd"] == pytest.approx(540.0)
    expected_cost = (0.5 * 0.06 * 4.0 * 100 + 0.65) + (0.5 * 0.07 * 3.6 * 100 + 0.65) \
        + (0.5 * 0.05 * 1.2 * 100 + 0.65) + (0.5 * 0.05 * 1.0 * 100 + 0.65)
    assert ss["cost_usd"] == pytest.approx(expected_cost)
    assert ss["net_usd"] == pytest.approx(540.0 - expected_cost)
    assert ss["net_pct"] == pytest.approx((540.0 - expected_cost) / 10_000)
    assert ss["stress_loss_usd"] == pytest.approx((3 * 0.08 * 100 - 7.6) * 100)
    assert ss["model_exit"] is False and ss["exit_tier_max"] == 1
    assert ss["straddle_over_implied"] == pytest.approx(0.076 / 0.08)


def test_iron_condor_wings_and_max_loss():
    res = sa.evaluate_event(_event(), _pre_rows(), _resolver(), SA_PARAMS, SIZING)
    ic = [t for t in res.trades if t["structure"] == "IC" and t["variant"] == "A1"][0]
    assert (ic["k_up"], ic["k_dn"]) == (115.0, 85.0)
    assert ic["wing_call_entry_tier"] == 1 and ic["wing_put_entry_tier"] == 3   # 85P never printed on pre
    assert ic["wing_call_exit_tier"] == 3 and ic["wing_put_exit_tier"] == 1    # 115C did not print early on post
    assert ic["model_exit"] is True
    width = 15.0
    assert ic["max_loss_usd"] == pytest.approx((width - ic["credit_entry"]) * 100)
    assert ic["n"] == max(1, int(SIZING.ic_max_loss_frac * SIZING.equity // ic["max_loss_usd"]))
    assert ic["credit_entry"] < 7.6                                # wings cost premium
    assert ic["n_touches"] == 8


def test_variant_a2_drops_excluded_sectors_only():
    res = sa.evaluate_event(_event(sector="Technology"), _pre_rows(), _resolver(), SA_PARAMS, SIZING)
    assert {t["variant"] for t in res.trades} == {"A1"}
    assert [s for s in res.suppressed if s["variant"] == "A2"][0]["first_fail"] == "A2_sector"


def test_first_failing_filter_is_reported_in_order():
    res = sa.evaluate_event(_event(spot_pre=9.0, marketcap=1e9), _pre_rows(), _resolver(), SA_PARAMS, SIZING)
    assert res.trades == []
    assert all(s["first_fail"] == "F2" for s in res.suppressed)
    thin = _pre_rows().copy()
    thin.loc[thin.strike == 100.0, "size_late"] = 1
    res = sa.evaluate_event(_event(), thin, _resolver(pre=thin), SA_PARAMS, SIZING)
    assert res.suppressed[0]["first_fail"] == "F5"
    wide = _pre_rows().copy()
    wide.loc[(wide.strike == 100.0) & (wide.option_type == "put") & (wide.expiry == EXP_W), "late_rel_spread"] = 0.2
    res = sa.evaluate_event(_event(), wide, _resolver(pre=wide), SA_PARAMS, SIZING)
    assert res.suppressed[0]["first_fail"] == "F6"


def test_unmarkable_exit_drops_the_trade_with_a_reason():
    resolver = M.MarkResolver({(r["option_chain_id"], r["date"]): r for r in _pre_rows().to_dict("records")},
                              lambda *a: None)
    res = sa.evaluate_event(_event(), _pre_rows(), resolver, SA_PARAMS, SIZING)
    assert res.trades == [] and res.dropped and res.dropped[0]["reason"] == "unmarkable_exit"


def test_run_returns_frames_with_strata_and_is_deterministic():
    events = pd.DataFrame([_event(), _event(ticker="ABC", sector="Technology")])
    pre_rows = pd.concat([_pre_rows(), _pre_rows().assign(underlying_symbol="ABC",
                          option_chain_id=lambda d: d.option_chain_id.str.replace("XYZ", "ABC"))])
    post_rows = pd.concat([_post_rows(), _post_rows().assign(underlying_symbol="ABC",
                           option_chain_id=lambda d: d.option_chain_id.str.replace("XYZ", "ABC"))])
    resolver = _resolver(pre_rows, post_rows)
    out1 = sa.run(events, pre_rows, resolver, SA_PARAMS, SIZING)
    out2 = sa.run(events, pre_rows, resolver, SA_PARAMS, SIZING)
    pd.testing.assert_frame_equal(out1.trades, out2.trades)
    assert len(out1.trades) == 2 * 2 + 1 * 2                      # XYZ: A1+A2 x SS+IC; ABC: A1 x SS+IC
    for col in ("sector", "mcap_bucket", "timing", "regime_pre", "vix_pre", "month", "season", "pre"):
        assert col in out1.trades.columns
    assert set(out1.suppressed.first_fail) == {"A2_sector"}


# ---- book caps -------------------------------------------------------------------------------------

def test_book_caps_limit_count_sector_and_night_budget():
    n = 12
    trades = pd.DataFrame({
        "variant": ["A1"] * n, "structure": ["IC"] * n, "pre": [PRE] * n, "ticker": [f"T{i}" for i in range(n)],
        "sector": ["Energy"] * 5 + ["Industrials"] * 7,
        "credit_net_pct": np.linspace(0.05, 0.01, n),
        "risk_usd": [400.0] * n,
    })
    capped = portfolio.apply_caps(trades, SIZING)
    taken = capped[capped.cap_pass]
    assert (taken.groupby("sector").size() <= SIZING.max_per_sector).all()
    assert len(taken) <= SIZING.max_open_events
    budget = SIZING.night_budget_frac * SIZING.max_open_events * SIZING.ic_max_loss_frac * SIZING.equity
    assert taken.risk_usd.sum() <= budget
    # richest first: T0..T2 (Energy, then the sector cap binds), T5 (Industrials), then the $1,600
    # night budget (0.40 x 8 x 0.5% x $100k) binds at four $400 trades
    assert list(taken.ticker) == ["T0", "T1", "T2", "T5"]
    assert budget == 1600.0
    assert capped.cap_rank.notna().all() and list(capped.cap_rank) == list(range(1, n + 1))
