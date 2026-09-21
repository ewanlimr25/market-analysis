"""engine.name.structures (R4, findings/stock-deep-dive DESIGN/70 §4 X1..X6, §5, §7 `structures[]`).

Every test runs offline: a synthetic `NameInputs` whose every number is hand-checkable, plus the
stored `tests/fixtures/name/` slices. No network, no panel, no mart.

The synthetic name is a $100 stock on 2026-09-18 with `iv30d = 0.40`, one listed expiry 28 calendar
days out (2026-10-16, a Friday) and a 5-point strike grid, so every strike and every number below
is arithmetic a reader can redo:

    sigma_hold = 100 x 0.40 x sqrt(28/365)            = 11.0788
    IB   short straddle 100, wings round(100 +/- 2s)  = 80 / 100 / 120
    IC   shorts round(100 +/- 1s) = 90 / 110, longs round(100 +/- 2s) = 80 / 120
    quotes  100C 100P 8.90/9.10 (mid 9.00) · 90P 110C 2.90/3.10 (3.00) · 80P 120C 0.90/1.10 (1.00)
    IB credit 9 + 9 - 1 - 1 = 16.00, width 20  -> max loss $400, BE 84 / 116, n = 500/400 = 1
    IC credit 3 + 3 - 1 - 1 =  4.00, width 10  -> max loss $600, BE 86 / 114, n = 0
    SS credit 9 + 9         = 18.00            -> stress 3s = (33.2364 - 18) x 100 = $1,523.64
    cost per leg = 0.584 x 0.10 x 100 + 0.65 = 6.49; 4 legs entry-only = $25.96
"""
from __future__ import annotations

import json
import math
import os
from datetime import date, timedelta

import jsonschema
import numpy as np
import pandas as pd
import pytest
from scipy.stats import norm

import name_fixtures
from engine.config import NAME_PARAMS, NAME_SIZING, NameSizing
from engine.name import structures as S
from engine.name.data import NameInputs
from engine.name.grade import grade_vertical
from engine.strategies.sa_filters import round_to_strike, strike_grid

pytestmark = pytest.mark.unit

DATE = date(2026, 9, 18)                       # a Friday; the fixture session
EXPIRY = DATE + timedelta(days=28)             # 2026-10-16, a Friday: S-C's [21, 35] band
CLOSE = 100.0
IV30D = 0.40
SIGMA_HOLD = CLOSE * IV30D * math.sqrt(28 / 365)       # 11.0788
ATR14 = 2.5
EQUITY_1M = 1_000_000.0
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "schemas", "ticker.schema.json")

# (strike, right) -> (bid, ask); every other contract on the grid is a cheap 0.40/0.60 wing.
QUOTES = {(100.0, "C"): (8.90, 9.10), (100.0, "P"): (8.90, 9.10),
          (110.0, "C"): (2.90, 3.10), (90.0, "P"): (2.90, 3.10),
          (120.0, "C"): (0.90, 1.10), (80.0, "P"): (0.90, 1.10)}
DEFAULT_QUOTE = (0.40, 0.60)
STRIKES = [float(k) for k in range(50, 155, 5)]
LOG_RETURN_CYCLE = (0.01, -0.02, 0.01)         # 63 trailing returns = 21 whole cycles, mean 0
SIGMA_63 = 0.22630268055373634                 # sqrt(0.0126/62) x sqrt(252), recomputed in the test


# --------------------------------------------------------------------------------------------
# the synthetic name
# --------------------------------------------------------------------------------------------

def _chain(expiry: date = EXPIRY, drop: set | None = None) -> pd.DataFrame:
    rows = []
    for strike in STRIKES:
        for right in ("C", "P"):
            if drop and (strike, right) in drop:
                continue
            bid, ask = QUOTES.get((strike, right), DEFAULT_QUOTE)
            rows.append({"symbol": "SYN", "expiry": expiry, "strike": strike, "right": right,
                         "bid": bid, "ask": ask, "mid": (bid + ask) / 2, "iv": IV30D,
                         "underlying_price": CLOSE, "source": "cboe_chain"})
    return pd.DataFrame(rows)


def _contracts(expiry: date = EXPIRY, drop: set | None = None) -> pd.DataFrame:
    """`daily_contract` rows for the same grid: the tier-1/2 fallback when the chain cannot price."""
    rows = []
    for strike in STRIKES:
        for right, option_type in (("C", "call"), ("P", "put")):
            if drop and (strike, right) in drop:
                continue
            bid, ask = QUOTES.get((strike, right), DEFAULT_QUOTE)
            mid = (bid + ask) / 2
            rows.append({"option_chain_id": f"SYN{expiry:%y%m%d}{right}{strike:g}",
                         "underlying_symbol": "SYN", "option_type": option_type, "strike": strike,
                         "expiry": expiry, "date": DATE, "n_prints": 40, "size_late": 50.0,
                         "vwap_late": mid, "late_rel_spread": (ask - bid) / mid,
                         "late_last_bid": bid, "late_last_ask": ask,
                         "last_nbbo_bid": bid, "last_nbbo_ask": ask, "last_price": mid})
    return pd.DataFrame(rows)


def _bars(n: int = 70) -> pd.DataFrame:
    closes = [CLOSE]
    for i in range(n - 1):
        closes.append(closes[-1] * math.exp(LOG_RETURN_CYCLE[i % 3]))
    days = [DATE - timedelta(days=n - 1 - i) for i in range(n)]
    return pd.DataFrame({"date": days, "open": closes, "high": closes, "low": closes,
                         "close": closes, "adj": closes, "volume": [1e6] * n})


def _inputs(*, chain: pd.DataFrame | None = None, contracts: pd.DataFrame | None = None,
            bars: pd.DataFrame | None = None, chain_live: bool = True) -> NameInputs:
    meta = {"source": "cboe_chain" if chain_live else None,
            "date": DATE.isoformat() if chain_live else None, "reason": None, "rows": 0}
    return NameInputs(ticker="SYN", date=DATE,
                      screener={"ticker": "SYN", "close": CLOSE, "iv30d": IV30D},
                      contracts_today=_contracts() if contracts is None else contracts,
                      bars=_bars() if bars is None else bars,
                      chain=_chain() if chain is None else chain, chain_meta=meta)


# --------------------------------------------------------------------------------------------
# the R2 / R3 sections, hand-built (those modules are being written in parallel)
# --------------------------------------------------------------------------------------------

def _sections(*, can_price: bool = True, x1: bool = False, x2: bool = False, x5: bool = False,
              sc_expiry: date | None = EXPIRY, earnings: str | None = None,
              x1_window_end: str | None = None, atr14: float | None = ATR14) -> dict:
    sc = {"pass": True, "failing": None, "expiry": sc_expiry.isoformat() if sc_expiry else None,
          "dte_cal": (sc_expiry - DATE).days if sc_expiry else None,
          "sigma_hold": SIGMA_HOLD if sc_expiry else None}
    events = {"earnings": {"date": earnings, "session": "post" if earnings else None,
                           "sources": [], "confirmed": bool(earnings)},
              "ex_div": None, "expiries": [], "macro": []}
    if x1_window_end is not None:
        events["x1_window_end"] = x1_window_end
    return {"liquidity": {"can_price": can_price, "failing": None if can_price else "L3",
                          "atm_expiry": EXPIRY.isoformat()},
            "events": events,
            "premium": {"iv30d": IV30D, "x1": x1, "sc": sc, "verdict": "FAIR"},
            "range_": {"atr14": atr14},
            "flags": {"x2": x2, "x5": x5}}


def _build(direction: str | None = None, *, inputs: NameInputs | None = None,
           sizing=NAME_SIZING, **over) -> list[dict]:
    return S.build(inputs if inputs is not None else _inputs(), NAME_PARAMS, sizing,
                   direction=direction, **_sections(**over))


def _by_family(lines: list[dict]) -> dict:
    return {line["family"]: line for line in lines}


def _legs(line: dict) -> dict:
    """`(strike, right) -> side` for one line, so a strike assertion reads like the menu."""
    return {(leg["strike"], leg["right"]): leg["side"] for leg in line["legs"]}


def _validate(structure: dict) -> None:
    schema = json.loads(open(SCHEMA_PATH, encoding="utf-8").read())
    jsonschema.validate(structure, {"$ref": "#/$defs/structure", "$defs": schema["$defs"]})


# --------------------------------------------------------------------------------------------
# §2: a CANNOT_PRICE sheet writes no structure
# --------------------------------------------------------------------------------------------

def test_returns_no_structure_when_the_liquidity_floor_fails():
    assert _build(can_price=False) == []
    assert _build("long", can_price=False) == []


def test_unknown_direction_raises():
    with pytest.raises(ValueError, match="direction"):
        _build("sideways")


# --------------------------------------------------------------------------------------------
# §5 premium menu: the iron butterfly, the 1s condor, the measurement straddle
# --------------------------------------------------------------------------------------------

def test_iron_butterfly_strikes_credit_max_loss_breakevens_and_size():
    ib = _by_family(_build())["IB"]
    assert _legs(ib) == {(80.0, "P"): 1, (100.0, "P"): -1, (100.0, "C"): -1, (120.0, "C"): 1}
    assert ib["expiry"] == EXPIRY.isoformat() and ib["dte_cal"] == 28
    assert ib["mark"] == pytest.approx(16.0)                 # 9 + 9 - 1 - 1, credit > 0
    assert ib["credit_debit"] == "credit"
    assert ib["max_loss"] == pytest.approx(400.0)            # (20 - 16) x 100
    assert ib["breakevens"] == pytest.approx([84.0, 116.0])
    assert ib["n"] == 1                                      # floor(0.005 x 100,000 / 400)
    assert ib["usd_at_risk"] == pytest.approx(400.0)
    assert ib["excluded_by"] is None and ib["note"] is None
    assert ib["mark_source"] == "cboe_chain 2026-09-18"
    assert all(leg["half_spread"] == pytest.approx(0.10) for leg in ib["legs"])


def test_iron_condor_is_one_sigma_wide_and_reports_the_zero_size_note():
    ic = _by_family(_build())["IC"]
    assert _legs(ic) == {(80.0, "P"): 1, (90.0, "P"): -1, (110.0, "C"): -1, (120.0, "C"): 1}
    assert ic["mark"] == pytest.approx(4.0)
    assert ic["max_loss"] == pytest.approx(600.0)            # (10 - 4) x 100
    assert ic["breakevens"] == pytest.approx([86.0, 114.0])
    assert ic["n"] == 0 and ic["usd_at_risk"] == pytest.approx(0.0)
    assert ic["note"] == "max loss exceeds 0.5% of E at one contract"


def test_short_straddle_is_measurement_only_while_undefined_risk_is_off():
    ss = _by_family(_build())["SS"]
    assert _legs(ss) == {(100.0, "P"): -1, (100.0, "C"): -1}
    assert ss["mark"] == pytest.approx(18.0) and ss["max_loss"] is None
    assert ss["breakevens"] == pytest.approx([82.0, 118.0])
    assert ss["stress_loss_3s"] == pytest.approx((3 * SIGMA_HOLD - 18.0) * 100)   # $1,523.64
    assert ss["n"] == 0
    assert ss["note"] == "ALLOW_UNDEFINED=0: measurement only"


def test_short_straddle_is_sized_off_the_three_sigma_stress_when_undefined_risk_is_allowed():
    sizing = NameSizing(equity=EQUITY_1M, allow_undefined=True)
    ss = _by_family(_build(sizing=sizing))["SS"]
    assert ss["n"] == 6                              # floor(0.010 x 1,000,000 / 1,523.64)
    assert ss["usd_at_risk"] == pytest.approx(6 * (3 * SIGMA_HOLD - 18.0) * 100)
    assert ss["note"] is None


def test_cost_is_the_effective_half_spread_plus_commission_per_leg():
    lines = _by_family(_build("long"))
    per_leg = NAME_PARAMS.cost_spread_mult * 0.10 * 100 + NAME_PARAMS.commission_per_contract
    assert lines["IB"]["cost"] == pytest.approx(4 * per_leg)          # entry only: $25.96
    assert lines["SS"]["cost"] == pytest.approx(2 * per_leg)
    assert lines["DEBIT_VERTICAL"]["cost"] == pytest.approx(2 * 2 * per_leg)   # entry and exit
    assert lines["SHARES"]["cost"] == pytest.approx(NAME_PARAMS.share_cost_bp * 1e-4 * CLOSE * 2)


# --------------------------------------------------------------------------------------------
# §5 probabilities: driftless lognormal at the trailing 63-session close-to-close sigma
# --------------------------------------------------------------------------------------------

def _sigma_63(bars: pd.DataFrame) -> float:
    """The same quantity, written independently of the module under test."""
    returns = np.diff(np.log(bars["close"].to_numpy(dtype=float)))[-NAME_PARAMS.sigma_c2c_window:]
    return float(np.std(returns, ddof=1) * math.sqrt(252))


def _d(strike: float, sigma: float, t: float) -> float:
    return (math.log(strike / CLOSE) + 0.5 * sigma ** 2 * t) / (sigma * math.sqrt(t))


def test_probabilities_are_the_driftless_lognormal_at_the_trailing_63_session_sigma():
    sigma, t = _sigma_63(_bars()), 28 / 365
    assert sigma == pytest.approx(SIGMA_63)
    lines = _by_family(_build("long"))
    inside = float(norm.cdf(_d(116.0, sigma, t)) - norm.cdf(_d(84.0, sigma, t)))
    assert lines["IB"]["p_inside"] == pytest.approx(inside)
    assert lines["IB"]["p_touch"] is None
    assert lines["IC"]["p_inside"] == pytest.approx(
        float(norm.cdf(_d(114.0, sigma, t)) - norm.cdf(_d(86.0, sigma, t))))
    # a debit call vertical is touched when the short 110 strike is beaten: 2 x P(beyond)
    assert lines["DEBIT_VERTICAL"]["p_touch"] == pytest.approx(
        min(1.0, 2 * float(1 - norm.cdf(_d(110.0, sigma, t)))))
    assert lines["SHARES"]["p_touch"] == pytest.approx(   # the X4 stop at 100 - 2 x ATR14 = 95
        min(1.0, 2 * float(norm.cdf(_d(95.0, sigma, t)))))


def test_probabilities_are_null_when_the_bar_history_is_short():
    lines = _by_family(_build("long", inputs=_inputs(bars=_bars(20))))
    assert lines["IB"]["p_inside"] is None and lines["SHARES"]["p_touch"] is None
    assert lines["IB"]["n"] == 1                 # a null probability never changes a size


# --------------------------------------------------------------------------------------------
# marks: the live chain, the daily_contract fallback, and the unpriced leg
# --------------------------------------------------------------------------------------------

def test_a_leg_without_a_quote_makes_the_structure_unpriced_and_unsized():
    inputs = _inputs(chain=_chain(drop={(120.0, "C")}), contracts=_contracts(drop={(120.0, "C")}))
    lines = _by_family(_build(inputs=inputs))
    assert lines["IB"]["mark"] is None and lines["IB"]["n"] == 0
    assert lines["IB"]["note"] == "unpriced: 2026-10-16 120C"
    assert lines["IB"]["max_loss"] is None and lines["IB"]["breakevens"] == []
    assert lines["IC"]["mark"] is None                        # the condor's long call is the same leg
    assert lines["SS"]["mark"] == pytest.approx(18.0)         # the straddle never touches 120C


def test_a_stale_chain_falls_back_to_the_daily_contract_tier_mark():
    lines = _by_family(_build(inputs=_inputs(chain_live=False)))
    assert lines["IB"]["mark"] == pytest.approx(16.0)
    assert lines["IB"]["mark_source"] == "daily_contract tier 1"
    for leg in lines["IB"]["legs"]:                            # half_spread = rel_spread x mark / 2
        assert leg["half_spread"] == pytest.approx(0.10)


def test_nothing_listed_in_the_window_leaves_the_premium_lines_unpriced():
    near = DATE + timedelta(days=7)
    inputs = _inputs(chain=_chain(expiry=near), contracts=_contracts().iloc[0:0])
    lines = _by_family(_build("long", inputs=inputs, sc_expiry=None))
    for family in ("IB", "IC", "SS"):
        assert lines[family]["mark"] is None and lines[family]["expiry"] is None
        assert "no listed" in lines[family]["note"]
    assert lines["DEBIT_VERTICAL"]["mark"] is None            # nothing listed on/after t + 28 either
    assert lines["SHARES"]["n"] == 100                        # the share line needs no expiry


def test_listed_expiries_are_the_union_of_the_chain_and_the_printed_contracts():
    near = DATE + timedelta(days=7)
    inputs = _inputs(chain=_chain(expiry=near))            # chain lists only t+7; prints list t+28
    lines = _by_family(_build("long", inputs=inputs, sc_expiry=None))
    assert lines["IB"]["expiry"] == EXPIRY.isoformat()      # found through the prints ..
    assert all("daily_contract" in l["mark_source"] for l in lines["IB"]["legs"])   # .. and priced by print


# --------------------------------------------------------------------------------------------
# §4 exclusions X1, X2, X5
# --------------------------------------------------------------------------------------------

def test_x1_excludes_every_premium_line_and_leaves_the_directional_menu_alone():
    lines = _by_family(_build("long", x1=True))
    for family in ("IB", "IC", "SS"):
        assert lines[family]["excluded_by"] == "X1"
        assert lines[family]["n"] == 0 and lines[family]["usd_at_risk"] == pytest.approx(0.0)
        assert lines[family]["mark"] is not None            # the price is still printed
    assert lines["SHARES"]["excluded_by"] is None and lines["DEBIT_VERTICAL"]["excluded_by"] is None


def test_x1_fires_when_the_premium_expiry_reaches_the_earnings_session():
    assert _by_family(_build(earnings="2026-10-09"))["IB"]["excluded_by"] == "X1"
    assert _by_family(_build(earnings="2026-10-16"))["IB"]["excluded_by"] == "X1"   # on the session
    assert _by_family(_build(earnings="2026-11-20"))["IB"]["excluded_by"] is None


def test_the_x1_window_end_overrides_the_earnings_date_when_the_events_section_carries_one():
    assert _by_family(_build(earnings="2026-11-20", x1_window_end="2026-10-16"))["IB"]["excluded_by"] == "X1"
    assert _by_family(_build(earnings="2026-10-09", x1_window_end="2026-10-30"))["IB"]["excluded_by"] is None


def test_x2_excludes_the_short_share_line_and_points_at_the_put_vertical():
    lines = _by_family(_build("short", x2=True))
    assert lines["SHARES"]["excluded_by"] == "X2" and lines["SHARES"]["n"] == 0
    assert "debit put vertical" in lines["SHARES"]["note"]
    assert lines["DEBIT_VERTICAL"]["excluded_by"] is None    # the priced alternative
    assert _by_family(_build("long", x2=True))["SHARES"]["excluded_by"] is None


def test_x5_marks_the_share_line_and_ranks_the_verticals_first():
    plain = _by_family(_build("long"))
    assert plain["SHARES"]["rank"] < plain["DEBIT_VERTICAL"]["rank"]
    assert plain["SHARES"]["note"] is None
    flagged = _by_family(_build("long", x5=True))
    assert flagged["DEBIT_VERTICAL"]["rank"] < flagged["SHARES"]["rank"]
    assert flagged["CREDIT_VERTICAL"]["rank"] < flagged["SHARES"]["rank"]
    assert flagged["SHARES"]["note"] == "defined-risk preferred"
    assert [line["rank"] for line in _build("long", x5=True)] == [1, 2, 3, 4, 5, 6]


# --------------------------------------------------------------------------------------------
# §5 directional menu
# --------------------------------------------------------------------------------------------

def test_no_directional_line_without_a_direction():
    assert [line["family"] for line in _build()] == ["IB", "IC", "SS"]


def test_long_menu_verticals_and_the_x4_share_stop():
    lines = _by_family(_build("long"))
    debit = lines["DEBIT_VERTICAL"]
    assert _legs(debit) == {(100.0, "C"): 1, (110.0, "C"): -1}     # long ATM, short at +1 sigma
    assert debit["mark"] == pytest.approx(-6.0) and debit["credit_debit"] == "debit"
    assert debit["max_loss"] == pytest.approx(600.0) and debit["breakevens"] == pytest.approx([106.0])
    credit = lines["CREDIT_VERTICAL"]
    assert _legs(credit) == {(90.0, "P"): -1, (80.0, "P"): 1}      # short -1 sigma, long -2 sigma
    assert credit["mark"] == pytest.approx(2.0) and credit["credit_debit"] == "credit"
    assert credit["max_loss"] == pytest.approx(800.0) and credit["breakevens"] == pytest.approx([88.0])
    shares = lines["SHARES"]
    assert shares["entry"] == pytest.approx(100.0) and shares["stop"] == pytest.approx(95.0)
    assert shares["target"] == pytest.approx(110.0)                # entry + 2 x |entry - stop|
    assert shares["legs"][0] == {"right": "S", "strike": None, "side": 1, "mark": pytest.approx(100.0),
                                 "half_spread": None, "mark_source": "screener 2026-09-18",
                                 "expiry": None}
    assert shares["max_loss"] == pytest.approx(5.0) and shares["n"] == 100
    assert shares["usd_at_risk"] == pytest.approx(500.0)
    assert shares["unit"] == "share" and lines["IB"]["unit"] == "contract"


def test_short_menu_mirrors_the_long_menu():
    lines = _by_family(_build("short"))
    assert _legs(lines["DEBIT_VERTICAL"]) == {(100.0, "P"): 1, (90.0, "P"): -1}
    assert lines["DEBIT_VERTICAL"]["breakevens"] == pytest.approx([94.0])
    assert _legs(lines["CREDIT_VERTICAL"]) == {(110.0, "C"): -1, (120.0, "C"): 1}
    assert lines["CREDIT_VERTICAL"]["breakevens"] == pytest.approx([112.0])
    shares = lines["SHARES"]
    assert shares["legs"][0]["side"] == -1
    assert shares["stop"] == pytest.approx(105.0) and shares["target"] == pytest.approx(90.0)


def test_a_null_atr_leaves_the_share_line_unsized_rather_than_raising():
    shares = _by_family(_build("long", atr14=None))["SHARES"]
    assert shares["stop"] is None and shares["n"] == 0 and shares["max_loss"] is None
    assert "ATR(14)" in shares["note"]


# --------------------------------------------------------------------------------------------
# §7 schema, and the R5 grader's leg shape
# --------------------------------------------------------------------------------------------

def test_every_structure_validates_against_the_ticker_schema():
    unpriced = _build(inputs=_inputs(chain=_chain(drop={(120.0, "C")}),
                                     contracts=_contracts(drop={(120.0, "C")})))
    for line in _build("long", x5=True) + _build("short", x2=True, x1=True) + unpriced:
        _validate(line)


def test_a_wing_never_lands_on_a_strike_the_expiry_does_not_list():
    """A name quoted every 0.5 near the money and every 1.0 in the wings: `round_to_strike` puts
    the wing on the inferred 0.5 increment, which nothing can mark or trade."""
    grid = strike_grid(pd.DataFrame({"strike": [25.0, 25.5, 26.0, 48.0, 49.0, 50.0]}))
    assert round_to_strike(48.374, grid) == pytest.approx(48.5)      # not a listed strike
    assert S.round_to_listed_strike(48.374, grid) == pytest.approx(48.0)
    assert S.round_to_listed_strike(25.6, grid) == pytest.approx(25.5)


def test_grade_vertical_accepts_every_option_line_and_agrees_on_the_max_loss():
    lines = _by_family(_build("long"))
    for family in ("IB", "IC", "DEBIT_VERTICAL", "CREDIT_VERTICAL"):
        line = lines[family]
        graded = grade_vertical(line["legs"], CLOSE)
        assert graded["max_loss_per_share"] * 100 == pytest.approx(line["max_loss"])


# --------------------------------------------------------------------------------------------
# the stored fixtures (R2 / R3 are being written in parallel, so their sections are hand-built)
# --------------------------------------------------------------------------------------------

def _fixture_sections(inputs, *, can_price: bool, expiry: date | None, atr14: float | None) -> dict:
    """The minimum of R2 / R3 this module reads, taken from the fixture's own screener row."""
    iv30d = (inputs.screener or {}).get("iv30d")
    sc = {"pass": False, "failing": "F3", "expiry": expiry.isoformat() if expiry else None,
          "dte_cal": (expiry - inputs.date).days if expiry else None, "sigma_hold": None}
    return {"liquidity": {"can_price": can_price, "failing": None if can_price else "L3",
                          "atm_expiry": expiry.isoformat() if expiry else None},
            "events": {"earnings": {"date": "2026-11-19", "session": "post", "sources": [],
                                    "confirmed": True}, "ex_div": None, "expiries": [], "macro": []},
            "premium": {"iv30d": iv30d, "x1": False, "sc": sc, "verdict": "FAIR"},
            "range_": {"atr14": atr14}, "flags": {"x2": False, "x5": False}}


def test_nvda_prices_the_premium_menu_from_the_stored_live_chain():
    inputs = name_fixtures.load_fixture("NVDA")
    # the fixture chain is trimmed to the six nearest expiries, so S-C's own expiry is supplied
    # here the way R2 supplies it on a full chain (DESIGN/70 §5, "premium: S-C's expiry").
    lines = S.build(inputs, NAME_PARAMS, NAME_SIZING, direction=None,
                    **_fixture_sections(inputs, can_price=True, expiry=date(2026, 10, 2), atr14=5.2))
    by_family = _by_family(lines)
    assert [line["family"] for line in lines] == ["IB", "IC", "SS"]
    for family in ("IB", "IC", "SS"):
        line = by_family[family]
        _validate(line)
        assert line["mark_source"] == "cboe_chain 2026-09-18"
        assert line["mark"] is not None and line["p_inside"] is not None
        assert all(leg["half_spread"] > 0 for leg in line["legs"])
    assert by_family["IB"]["max_loss"] > 0 and by_family["IC"]["max_loss"] > 0
    assert by_family["SS"]["max_loss"] is None and by_family["SS"]["stress_loss_3s"] > 0


def test_nvda_is_too_large_for_a_100k_account_and_sizes_at_a_million():
    inputs = name_fixtures.load_fixture("NVDA")
    sections = _fixture_sections(inputs, can_price=True, expiry=date(2026, 10, 2), atr14=5.2)
    small = _by_family(S.build(inputs, NAME_PARAMS, NAME_SIZING, direction=None, **sections))
    assert small["IB"]["n"] == 0                     # max loss > 0.5% of $100,000 at one contract
    assert small["IB"]["note"] == "max loss exceeds 0.5% of E at one contract"
    big = _by_family(S.build(inputs, NAME_PARAMS, NameSizing(equity=EQUITY_1M),
                             direction=None, **sections))
    assert any(big[family]["n"] >= 1 for family in ("IB", "IC"))


def test_bl_cannot_price_writes_no_structure():
    inputs = name_fixtures.load_fixture("BL")
    sections = _fixture_sections(inputs, can_price=False, expiry=None, atr14=1.0)
    assert S.build(inputs, NAME_PARAMS, NAME_SIZING, direction="long", **sections) == []


def test_oklo_directional_menu_is_priced_and_graded():
    inputs = name_fixtures.load_fixture("OKLO")
    sections = _fixture_sections(inputs, can_price=True, expiry=date(2026, 10, 2), atr14=3.0)
    lines = _by_family(S.build(inputs, NAME_PARAMS, NAME_SIZING, direction="long", **sections))
    shares = lines["SHARES"]
    assert shares["entry"] == pytest.approx(inputs.screener["close"])
    assert shares["stop"] == pytest.approx(inputs.screener["close"] - 2 * 3.0)
    assert shares["n"] >= 1 and shares["usd_at_risk"] > 0
    for family in ("IB", "IC"):
        graded = grade_vertical(lines[family]["legs"], inputs.screener["close"])
        assert graded["max_loss_per_share"] * 100 == pytest.approx(lines[family]["max_loss"])
