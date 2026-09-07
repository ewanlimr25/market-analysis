"""S-G strategy (DESIGN/91 §2) on synthetic daily_contract / earnings_events rows."""
from __future__ import annotations

import math
from datetime import date

import pandas as pd
import pytest

from engine import marking as M
from engine.config import SG_PARAMS
from engine.strategies import sa_filters as F
from engine.strategies import sg, sg_filters as G, sg_structures as ST

pytestmark = pytest.mark.unit

E = date(2026, 8, 6)            # AMC release: pre == E, entry_day(3) counts back from E
ENTRY3 = date(2026, 8, 3)
PRE = E
POST = date(2026, 8, 7)
EXP = date(2026, 8, 21)


def _event(**kw):
    e = dict(ticker="XYZ", E=E, pre=PRE, post=POST, timing="postmarket", how="labelled",
             spot_pre=108.0, implied_move_perc=0.08, marketcap=5e9, adv_usd_20d=100e6,
             issue_type="Common Stock", sector="Industrials", iv30d_pre=0.5, iv30d_post=0.35,
             regime_pre="CHOP", vix_pre=17.0, month="2026-08", season="S2",
             realized_move=0.03, gap_signed=-0.03, close_post=105.0)
    e.update(kw)
    return e


def _cid(sym, exp, typ, k):
    return f"{sym}{exp.strftime('%y%m%d')}{'C' if typ == 'call' else 'P'}{int(round(k * 1000)):08d}"


def _row(sym, exp, typ, k, d, **kw):
    r = dict(option_chain_id=_cid(sym, exp, typ, k), underlying_symbol=sym, option_type=typ, strike=float(k),
             expiry=exp, date=d, vwap_late=None, size_late=0, late_rel_spread=None, late_last_bid=None,
             late_last_ask=None, last_price=1.0, last_nbbo_bid=0.9, last_nbbo_ask=1.1, n_prints=5,
             iv_vwap=0.45)
    r.update(kw)
    return r


def _entry_rows(illiquid_wings: bool = False):
    wing_size = 3 if illiquid_wings else 40
    return pd.DataFrame([
        _row("XYZ", EXP, "call", 100, ENTRY3, vwap_late=4.0, size_late=30, late_rel_spread=0.06, iv_vwap=0.45),
        _row("XYZ", EXP, "put", 100, ENTRY3, vwap_late=3.6, size_late=25, late_rel_spread=0.07, iv_vwap=0.45),
        _row("XYZ", EXP, "call", 105, ENTRY3, vwap_late=1.8, size_late=wing_size, late_rel_spread=0.05, iv_vwap=0.40),
        _row("XYZ", EXP, "put", 95, ENTRY3, vwap_late=1.5, size_late=wing_size, late_rel_spread=0.05, iv_vwap=0.40),
        _row("XYZ", POST, "call", 100, ENTRY3, vwap_late=2.0, size_late=100, late_rel_spread=0.03),  # must not be picked
    ])


def _exit_rows():
    return pd.DataFrame([
        _row("XYZ", EXP, "call", 100, PRE, vwap_late=9.0, size_late=50, late_rel_spread=0.04, iv_vwap=0.55),
        _row("XYZ", EXP, "put", 100, PRE, vwap_late=1.2, size_late=45, late_rel_spread=0.05, iv_vwap=0.55),
        _row("XYZ", EXP, "call", 105, PRE, vwap_late=5.0, size_late=40, late_rel_spread=0.05, iv_vwap=0.50),
        _row("XYZ", EXP, "put", 95, PRE, vwap_late=0.6, size_late=35, late_rel_spread=0.06, iv_vwap=0.50),
    ])


def _prices():
    return {("XYZ", ENTRY3): (99.5, 100.0), ("XYZ", PRE): (107.0, 108.0)}


def _rows_dict(*frames):
    out = {}
    for df in frames:
        for r in df.to_dict("records"):
            out[(r["option_chain_id"], r["date"])] = r
    return out


def _resolver(rows_dict, model_inputs_fn=None):
    return M.MarkResolver(rows_dict, model_inputs_fn or (lambda c, d, w: None))


# ---- day arithmetic already covered by test_sg_filters.py; here: strategy behaviour -----------

def test_select_legs_finds_atm_pair_at_entry_day_not_exit_day():
    sel, flags = sg.select_legs(_event(), _entry_rows(), spot_entry=100.0)
    assert sel is not None and sel.pair.strike == 100.0 and sel.expiry == EXP
    assert flags == {"F5": True, "F6": True}


def test_select_legs_fails_f5_when_no_spot_entry():
    sel, flags = sg.select_legs(_event(), _entry_rows(), spot_entry=None)
    assert sel is None and flags["F5"] is False


def test_evaluate_event_prices_ls_and_lg():
    rows_dict = _rows_dict(_entry_rows(), _exit_rows())
    resolver = _resolver(rows_dict)
    res = sg.evaluate_event(_event(), _entry_rows(), 3, ENTRY3, PRE, resolver, _prices(), SG_PARAMS,
                            1.0, rows_dict, lambda c, d, w: None)
    assert not res.suppressed and not res.dropped
    structures = {r["structure"] for r in res.trades}
    assert structures == {"LS", "LG"}
    ls = next(r for r in res.trades if r["structure"] == "LS")
    assert ls["k"] == 100.0 and ls["contracts"] >= 1
    assert ls["premium_paid_usd"] > 0
    assert ls["entry_tier_max"] == 1 and ls["exit_tier_max"] == 1
    lg = next(r for r in res.trades if r["structure"] == "LG")
    assert lg["k_up"] == 105.0 and lg["k_dn"] == 95.0


def test_long_straddle_pnl_is_exit_minus_entry_direction():
    rows_dict = _rows_dict(_entry_rows(), _exit_rows())
    resolver = _resolver(rows_dict)
    res = sg.evaluate_event(_event(), _entry_rows(), 3, ENTRY3, PRE, resolver, _prices(), SG_PARAMS,
                            1.0, rows_dict, lambda c, d, w: None)
    ls = next(r for r in res.trades if r["structure"] == "LS")
    # entry straddle 4.0+3.6=7.6, exit straddle 9.0+1.2=10.2: bought low, sold high -> gross positive
    assert ls["gross_usd"] > 0
    assert ls["net_usd"] < ls["gross_usd"]                # costs subtract from gross
    assert ls["net_pct_prem"] == pytest.approx(ls["net_usd"] / ls["premium_paid_usd"])


def test_decomposition_present_and_sums_consistently():
    rows_dict = _rows_dict(_entry_rows(), _exit_rows())
    resolver = _resolver(rows_dict)
    res = sg.evaluate_event(_event(), _entry_rows(), 3, ENTRY3, PRE, resolver, _prices(), SG_PARAMS,
                            1.0, rows_dict, lambda c, d, w: None)
    ls = next(r for r in res.trades if r["structure"] == "LS")
    for k in ("unhedged_pnl_pct", "delta_pnl_pct", "delta_hedged_pnl_pct", "vega_pnl_pct", "residual_pnl_pct"):
        assert math.isfinite(ls[k])
    assert ls["delta_pnl_pct"] + ls["delta_hedged_pnl_pct"] == pytest.approx(ls["unhedged_pnl_pct"])
    assert ls["vega_pnl_pct"] + ls["residual_pnl_pct"] == pytest.approx(ls["delta_hedged_pnl_pct"])


def test_lg_dropped_when_wings_illiquid_but_ls_still_trades():
    entry_rows = _entry_rows(illiquid_wings=True)
    rows_dict = _rows_dict(entry_rows, _exit_rows())
    resolver = _resolver(rows_dict)
    res = sg.evaluate_event(_event(), entry_rows, 3, ENTRY3, PRE, resolver, _prices(), SG_PARAMS,
                            1.0, rows_dict, lambda c, d, w: None)
    assert len(res.trades) == 1 and res.trades[0]["structure"] == "LS"
    assert len(res.dropped) == 1 and res.dropped[0]["structure"] == "LG"
    assert res.dropped[0]["reason"] == "illiquid_strangle_leg"


def test_suppressed_when_cheap_filter_fails():
    rows_dict = _rows_dict(_entry_rows(), _exit_rows())
    resolver = _resolver(rows_dict)
    res = sg.evaluate_event(_event(marketcap=1e9), _entry_rows(), 3, ENTRY3, PRE, resolver, _prices(),
                            SG_PARAMS, 1.0, rows_dict, lambda c, d, w: None)
    assert not res.trades and res.suppressed[0]["first_fail"] == "F3"


def test_suppressed_f5_when_no_atm_pair_at_entry_day():
    empty = _entry_rows().iloc[0:0]
    rows_dict = _rows_dict(_exit_rows())
    resolver = _resolver(rows_dict)
    res = sg.evaluate_event(_event(), empty, 3, ENTRY3, PRE, resolver, _prices(), SG_PARAMS, 1.0,
                            rows_dict, lambda c, d, w: None)
    assert not res.trades and res.suppressed[0]["first_fail"] == "F5"


def test_run_over_both_offsets_produces_g3_3_and_g3_5_variants():
    entry_rows_5 = _entry_rows().assign(date=date(2026, 7, 30))
    rows_dict = _rows_dict(_entry_rows(), entry_rows_5, _exit_rows())
    resolver = _resolver(rows_dict)
    events = pd.DataFrame([_event()])
    entry_rows_by_offset = {3: _entry_rows(), 5: entry_rows_5}
    res = sg.run(events, entry_rows_by_offset, resolver, _prices() | {("XYZ", date(2026, 7, 30)): (99.0, 99.5)},
                lambda c, d, w: None, (3, 5), SG_PARAMS, 1.0, rows_dict)
    assert set(res.trades.variant) == {"G3_3", "G3_5"}
    assert set(res.trades.structure) == {"LS", "LG"}
