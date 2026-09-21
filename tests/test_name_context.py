"""engine.name.context (R3, findings/stock-deep-dive DESIGN/70 §7 `context`, §8 line F, D3).

Hand-computed returns and 52-week position on synthetic bars, percentile edge cases (including a
one-row universe), and the three stored fixtures. No network, no panel.
"""
from __future__ import annotations

import json
import os
from datetime import date, timedelta

import pandas as pd
import pytest

import name_fixtures
from engine import config, schema
from engine.config import NAME_PARAMS
from engine.name import context as C

pytestmark = pytest.mark.unit

D = date(2026, 9, 18)
SCHEMA = json.load(open(os.path.join(config.REPO, "schemas", "ticker.schema.json"), encoding="utf-8"))


def assert_valid(section: dict, name: str = "context") -> None:
    assert schema.validate(section, {"$ref": f"#/$defs/{name}", "$defs": SCHEMA["$defs"]}) == []


def inputs(**kw):
    from engine.name.data import NameInputs
    return NameInputs(ticker=kw.pop("ticker", "X"), date=kw.pop("date", D), **kw)


def bars(closes: list[float], *, end: date = D, highs=None, lows=None) -> pd.DataFrame:
    n = len(closes)
    days = [end - timedelta(days=n - 1 - i) for i in range(n)]
    return pd.DataFrame({"date": days, "open": closes, "high": highs or closes,
                         "low": lows or closes, "close": closes, "adj": closes,
                         "volume": [1e6] * n})


def universe(rows: list[tuple]) -> pd.DataFrame:
    """`(ticker, bullish, bearish, total_volume, avg30_volume, issue_type, is_index)` rows."""
    return pd.DataFrame(rows, columns=["ticker", "bullish_premium", "bearish_premium",
                                       "total_volume", "avg30_volume", "issue_type", "is_index"])


def history(nets: list[float], *, volumes=None, end: date = D) -> pd.DataFrame:
    n = len(nets)
    days = [end - timedelta(days=n - 1 - i) for i in range(n)]
    volumes = volumes or [1e6] * n
    return pd.DataFrame({"date": days, "close": [100.0] * n, "iv30d": [0.3] * n,
                         "iv_rank": [50.0] * n, "bullish_premium": [max(x, 0.0) for x in nets],
                         "bearish_premium": [max(-x, 0.0) for x in nets], "total_volume": volumes,
                         "avg30_volume": [1e6] * n, "marketcap": [1e10] * n})


# ---- the percentile rule -------------------------------------------------------------------------

def test_percentile_rank_puts_a_value_at_the_middle_of_its_own_ties():
    assert C.percentile_rank([50.0, 75.0, 100.0, 150.0], 100.0) == pytest.approx(62.5)
    assert C.percentile_rank([100.0], 100.0) == pytest.approx(50.0)       # a one-row universe
    assert C.percentile_rank([1.0, 2.0, 3.0], 3.0) == pytest.approx(83.33333, rel=1e-4)
    assert C.percentile_rank([], 1.0) is None


# ---- returns and the 52-week position ------------------------------------------------------------

def test_ret_21_and_ret_63_are_close_over_close_from_the_last_bar():
    closes = [100.0 + i for i in range(64)]                # close 163 today, 142 21 back, 100 63 back
    out = C.evaluate(inputs(bars=bars(closes)), NAME_PARAMS)

    assert out["ret_21"] == pytest.approx(163 / 142 - 1)
    assert out["ret_63"] == pytest.approx(163 / 100 - 1)
    assert out["source"]["ret_21"].endswith(D.isoformat())


def test_returns_ignore_bars_after_the_sheet_date():
    closes = [100.0 + i for i in range(64)]
    frame = bars(closes)
    future = frame.iloc[[-1]].assign(date=[D + timedelta(days=3)], close=[1000.0])
    out = C.evaluate(inputs(bars=pd.concat([frame, future], ignore_index=True)), NAME_PARAMS)

    assert out["ret_21"] == pytest.approx(163 / 142 - 1)


def test_ret_63_is_null_with_too_few_bars_and_ret_21_still_prints():
    out = C.evaluate(inputs(bars=bars([100.0 + i for i in range(30)])), NAME_PARAMS)

    assert out["ret_21"] is not None and out["ret_63"] is None
    assert any(n["field"] == "ret_63" for n in out["nulls"])


def test_w52_pos_is_where_the_close_sits_in_the_trailing_year_range():
    closes = [100.0] * 252
    highs = [120.0] + [100.0] * 251
    lows = [80.0] + [100.0] * 251
    out = C.evaluate(inputs(bars=bars(closes, highs=highs, lows=lows)), NAME_PARAMS)

    assert out["w52_pos"] == pytest.approx(0.5)            # (100 - 80) / (120 - 80)
    assert out["source"]["w52_pos"].endswith(D.isoformat())


def test_w52_pos_is_null_under_two_hundred_bars():
    out = C.evaluate(inputs(bars=bars([100.0] * 199)), NAME_PARAMS)

    assert out["w52_pos"] is None
    assert any(n["field"] == "w52_pos" for n in out["nulls"])


# ---- the two flow percentiles (DESIGN/70 §1 last row, §8 line F) ----------------------------------

UNIVERSE = universe([
    ("X", 150.0, 50.0, 2_000_000, 1_000_000, "Common Stock", False),      # net +100, vol ratio 2.0
    ("A", 50.0, 0.0, 500_000, 1_000_000, "Common Stock", False),          # net  +50, ratio 0.5
    ("B", 150.0, 0.0, 4_000_000, 1_000_000, "ADR", False),                # net +150, ratio 4.0
    ("E", 75.0, 0.0, 1_000_000, 1_000_000, "ETF", False),                 # net  +75, ratio 1.0
    ("IDX", 9e9, 0.0, 9e9, 1.0, "Common Stock", True),                    # an index: excluded
    ("W", 9e9, 0.0, 9e9, 1.0, "Unit", False),                             # not a name issue type
])


def test_flow_pct_universe_ranks_the_name_among_names_only():
    out = C.evaluate(inputs(ticker="X", universe_today=UNIVERSE), NAME_PARAMS)

    assert out["net_premium"] == pytest.approx(100.0)
    assert out["flow_pct_universe"] == pytest.approx(62.5)   # below A, E; ties only with itself
    assert out["volume_ratio"] == pytest.approx(2.0)
    assert out["vol_pct_universe"] == pytest.approx(62.5)
    assert out["universe_n"] == 4                            # the index and the Unit are dropped
    assert out["source"]["flow_pct_universe"].endswith(D.isoformat())


def test_a_one_row_universe_puts_the_name_at_the_middle_of_its_own_tie():
    one = universe([("X", 150.0, 50.0, 2_000_000, 1_000_000, "Common Stock", False)])

    out = C.evaluate(inputs(ticker="X", universe_today=one), NAME_PARAMS)

    assert out["flow_pct_universe"] == pytest.approx(50.0) and out["universe_n"] == 1


def test_flow_pct_universe_is_null_when_the_name_is_not_in_the_universe():
    out = C.evaluate(inputs(ticker="ZZZZ", universe_today=UNIVERSE), NAME_PARAMS)

    assert out["flow_pct_universe"] is None and out["vol_pct_universe"] is None
    assert any(n["field"] == "flow_pct_universe" for n in out["nulls"])


def test_flow_pct_self_ranks_today_against_the_names_own_sixty_three_sessions():
    nets = [-100.0] * 62 + [0.0, 100.0]                      # today is the highest of 64 sessions
    out = C.evaluate(inputs(screener_history=history(nets)), NAME_PARAMS)

    assert out["flow_pct_self"] == pytest.approx(100 * (62 + 0.5) / 63)   # the 64th is dropped
    assert out["self_n"] == 63
    assert out["source"]["flow_pct_self"].endswith(D.isoformat())


def test_volume_percentiles_use_total_volume_over_avg30_volume():
    volumes = [1e6] * 62 + [5e6, 2e6]
    out = C.evaluate(inputs(screener_history=history([0.0] * 64, volumes=volumes)), NAME_PARAMS)

    assert out["volume_ratio"] == pytest.approx(2.0)          # today's 2e6 over avg30 1e6
    assert out["vol_pct_self"] == pytest.approx(100 * (61 + 0.5) / 63)


def test_the_screener_row_supplies_the_flow_when_the_universe_has_no_row_for_the_name():
    out = C.evaluate(inputs(ticker="X", screener={"bullish_premium": 300.0, "bearish_premium": 100.0,
                                                  "total_volume": 3e6, "avg30_volume": 1e6}),
                     NAME_PARAMS)

    assert out["net_premium"] == pytest.approx(200.0) and out["volume_ratio"] == pytest.approx(3.0)
    assert out["flow_pct_universe"] is None                   # nothing to rank it against


# ---- the fixed sentence (D3), the all-null sheet and the fixtures ---------------------------------

def test_section_f_is_the_frozen_sentence_and_nothing_else():
    assert C.SENTENCE == ("Direction: no input on this sheet has a measured directional edge at "
                          "1–4 weeks; the engine emits none.")
    assert C.evaluate(inputs(), NAME_PARAMS)["sentence"] == C.SENTENCE


def test_an_empty_name_inputs_yields_every_null_and_still_validates():
    out = C.evaluate(inputs(), NAME_PARAMS)

    assert out["ret_21"] is None and out["ret_63"] is None and out["w52_pos"] is None
    assert out["flow_pct_universe"] is None and out["flow_pct_self"] is None
    assert {n["field"] for n in out["nulls"]} >= {"ret_21", "ret_63", "w52_pos",
                                                  "flow_pct_universe", "flow_pct_self"}
    assert_valid(out)


@pytest.mark.parametrize("ticker", name_fixtures.FIXTURE_TICKERS)
def test_every_fixture_context_section_validates_and_names_its_sources(ticker):
    out = C.evaluate(name_fixtures.load_fixture(ticker), NAME_PARAMS)

    assert_valid(out)
    assert out["sentence"] == C.SENTENCE
    assert out["ret_21"] is not None and out["w52_pos"] is not None
    assert 0.0 <= out["flow_pct_universe"] <= 100.0 and 0.0 <= out["flow_pct_self"] <= 100.0
    assert json.loads(json.dumps(out)) == out


def test_nvda_flow_percentiles_come_from_the_stored_universe_and_history():
    out = C.evaluate(name_fixtures.load_fixture("NVDA"), NAME_PARAMS)

    assert out["universe_n"] == 5829                          # 6,310 screener rows minus non-names
    assert out["self_n"] == 63
    assert out["net_premium"] == pytest.approx(316_187_086.0 - 303_064_946.0)
    assert out["source"]["ret_21"].startswith("earnings_history/bars")
