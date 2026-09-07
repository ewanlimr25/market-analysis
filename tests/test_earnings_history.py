"""engine.mart.earnings_history: per-name realized earnings-move history and its point-in-time
trailing summary (G7, findings/RESEARCH/47-edge-gaps.md §2 G7).

Unit tests exercise the pure transforms (`build_events`, `point_in_time_summary`,
`validate_against_panel`) on synthetic frames, and the cache/fail-soft wrappers
(`fetch_bars_cached`, `fetch_finnhub_calendar_cached`) with monkeypatched network calls -- no
real HTTP anywhere in this file.
"""
from __future__ import annotations

import json
import math
import os
from datetime import date

import pandas as pd
import pytest

from engine.mart import earnings_history as eh

pytestmark = pytest.mark.unit


def events_row(ticker: str, e: date, pre: date, post: date, timing: str = "postmarket",
              realized_move: float = 0.05, er_time: str = "postmarket", how: str = "labelled") -> dict:
    return {"ticker": ticker, "E": e, "er_time": er_time, "timing": timing, "how": how,
            "pre": pre, "post": post, "realized_move": realized_move}


def bars_df(rows: list[tuple[date, float]]) -> pd.DataFrame:
    return pd.DataFrame({"date": [d for d, _ in rows], "close": [c for _, c in rows],
                         "adj": [c for _, c in rows], "open": [c for _, c in rows],
                         "high": [c for _, c in rows], "low": [c for _, c in rows],
                         "volume": [1_000_000] * len(rows)})


# ----------------------------------------------------------------------------- build_events


def test_build_events_computes_move_from_yahoo_pre_post_closes():
    events = pd.DataFrame([events_row("AAA", date(2026, 5, 5), date(2026, 5, 5), date(2026, 5, 6),
                                      realized_move=0.10)])
    bars = {"AAA": bars_df([(date(2026, 5, 5), 100.0), (date(2026, 5, 6), 110.0)])}
    out = eh.build_events(events, bars)
    assert len(out) == 1
    row = out.iloc[0]
    assert row.yahoo_close_pre == pytest.approx(100.0)
    assert row.yahoo_close_post == pytest.approx(110.0)
    assert row.realized_move_yahoo == pytest.approx(0.10)
    assert row.abs_move_yahoo == pytest.approx(0.10)
    assert row.available
    assert row.matches_panel  # panel says 0.10 too, exact match


def test_build_events_flags_unavailable_when_a_close_is_missing():
    events = pd.DataFrame([events_row("AAA", date(2026, 5, 5), date(2026, 5, 5), date(2026, 5, 6))])
    bars = {"AAA": bars_df([(date(2026, 5, 5), 100.0)])}  # post-session close missing (vendor gap)
    out = eh.build_events(events, bars)
    row = out.iloc[0]
    assert not row.available
    assert math.isnan(row.realized_move_yahoo)
    assert not row.matches_panel


def test_build_events_flags_unavailable_for_a_ticker_with_no_bars_at_all():
    events = pd.DataFrame([events_row("ZZZ", date(2026, 5, 5), date(2026, 5, 5), date(2026, 5, 6))])
    out = eh.build_events(events, {})  # no bars fetched for ZZZ
    assert not out.iloc[0].available


def test_build_events_marks_unresolved_timing_as_unknown():
    events = pd.DataFrame([events_row("AAA", date(2026, 5, 5), date(2026, 5, 4), date(2026, 5, 6),
                                      timing="unresolved", er_time="unknown", how="2-session")])
    bars = {"AAA": bars_df([(date(2026, 5, 4), 100.0), (date(2026, 5, 6), 105.0)])}
    out = eh.build_events(events, bars)
    assert out.iloc[0].timing_unknown


def test_build_events_uses_amc_alignment_close_e_to_close_e_plus_1():
    # postmarket (AMC): pre == E, post == next session -- earnings_events already encodes this.
    e = date(2026, 6, 10)
    events = pd.DataFrame([events_row("AAA", e, pre=e, post=date(2026, 6, 11), timing="postmarket")])
    bars = {"AAA": bars_df([(e, 50.0), (date(2026, 6, 11), 55.0)])}
    out = eh.build_events(events, bars)
    assert out.iloc[0].realized_move_yahoo == pytest.approx(0.10)


def test_build_events_uses_bmo_alignment_close_e_minus_1_to_close_e():
    # premarket (BMO): pre == prev session, post == E.
    e = date(2026, 6, 10)
    events = pd.DataFrame([events_row("AAA", e, pre=date(2026, 6, 9), post=e, timing="premarket")])
    bars = {"AAA": bars_df([(date(2026, 6, 9), 50.0), (e, 45.0)])}
    out = eh.build_events(events, bars)
    assert out.iloc[0].realized_move_yahoo == pytest.approx(-0.10)


def test_build_events_empty_input_has_the_declared_columns():
    out = eh.build_events(pd.DataFrame(), {})
    assert list(out.columns) == list(eh.EVENTS_COLUMNS)
    assert out.empty


def test_matches_panel_within_tolerance_but_not_outside_it():
    e = date(2026, 5, 5)
    events = pd.DataFrame([events_row("AAA", e, e, date(2026, 5, 6), realized_move=0.10)])
    # Yahoo move 0.101 vs panel 0.10: within tol (max(0.005, 0.03*0.10)=0.005 -> diff 0.001 OK)
    bars = {"AAA": bars_df([(e, 100.0), (date(2026, 5, 6), 110.1)])}
    close_row = eh.build_events(events, bars).iloc[0]
    assert close_row.matches_panel

    events2 = pd.DataFrame([events_row("BBB", e, e, date(2026, 5, 6), realized_move=0.10)])
    # Yahoo move 0.20 vs panel 0.10: far outside tolerance.
    bars2 = {"BBB": bars_df([(e, 100.0), (date(2026, 5, 6), 120.0)])}
    far_row = eh.build_events(events2, bars2).iloc[0]
    assert not far_row.matches_panel


# ----------------------------------------------------------------------------- point_in_time_summary


def _events_with_moves(ticker: str, rows: list[tuple[date, float, bool]]) -> pd.DataFrame:
    """rows: (E, abs_move_yahoo, available)."""
    return pd.DataFrame({"ticker": [ticker] * len(rows), "E": [r[0] for r in rows],
                         "abs_move_yahoo": [r[1] for r in rows], "available": [r[2] for r in rows]})


def test_point_in_time_summary_first_event_has_zero_prior():
    df = _events_with_moves("AAA", [(date(2026, 3, 1), 0.05, True)])
    out = eh.point_in_time_summary(df)
    assert out.iloc[0].n_prior == 0
    assert math.isnan(out.iloc[0].median_abs_move_prior)


def test_point_in_time_summary_never_includes_the_current_or_later_event():
    df = _events_with_moves("AAA", [(date(2026, 3, 1), 0.05, True),
                                    (date(2026, 6, 1), 0.20, True),
                                    (date(2026, 9, 1), 0.01, True)])
    out = eh.point_in_time_summary(df).set_index("E")
    assert out.loc[date(2026, 3, 1), "n_prior"] == 0
    row2 = out.loc[date(2026, 6, 1)]
    assert row2.n_prior == 1
    assert row2.median_abs_move_prior == pytest.approx(0.05)  # only the March event, not June/Sept
    row3 = out.loc[date(2026, 9, 1)]
    assert row3.n_prior == 2
    assert row3.mean_abs_move_prior == pytest.approx((0.05 + 0.20) / 2)
    assert row3.max_abs_move_prior == pytest.approx(0.20)


def test_point_in_time_summary_skips_unavailable_events_from_the_trailing_window():
    df = _events_with_moves("AAA", [(date(2026, 3, 1), 0.30, False),   # unavailable: excluded
                                    (date(2026, 6, 1), 0.05, True),
                                    (date(2026, 9, 1), 0.01, True)])
    out = eh.point_in_time_summary(df).set_index("E")
    assert out.loc[date(2026, 6, 1), "n_prior"] == 0       # the March row doesn't count
    assert out.loc[date(2026, 9, 1), "n_prior"] == 1
    assert out.loc[date(2026, 9, 1), "median_abs_move_prior"] == pytest.approx(0.05)


def test_point_in_time_summary_share_thresholds():
    moves = [0.01, 0.06, 0.11, 0.02]
    rows = [(date(2026, 1, 1 + i), m, True) for i, m in enumerate(moves)]
    rows.append((date(2026, 2, 1), 0.0, True))  # a 5th event to read the trailing stats off
    df = _events_with_moves("AAA", rows)
    out = eh.point_in_time_summary(df).set_index("E").loc[date(2026, 2, 1)]
    assert out.n_prior == 4
    assert out.share_gt5_prior == pytest.approx(2 / 4)   # 0.06 and 0.11 exceed 5%
    assert out.share_gt10_prior == pytest.approx(1 / 4)  # only 0.11 exceeds 10%


def test_point_in_time_summary_keeps_tickers_independent():
    df = pd.concat([_events_with_moves("AAA", [(date(2026, 1, 1), 0.50, True)]),
                    _events_with_moves("BBB", [(date(2026, 1, 1), 0.01, True)]),
                    _events_with_moves("AAA", [(date(2026, 4, 1), 0.02, True)])], ignore_index=True)
    out = eh.point_in_time_summary(df)
    aaa_second = out[(out.ticker == "AAA") & (out.E == date(2026, 4, 1))].iloc[0]
    assert aaa_second.n_prior == 1
    assert aaa_second.median_abs_move_prior == pytest.approx(0.50)  # not contaminated by BBB


def test_point_in_time_summary_empty_input():
    out = eh.point_in_time_summary(pd.DataFrame())
    assert list(out.columns) == list(eh.SUMMARY_COLUMNS)
    assert out.empty


# ----------------------------------------------------------------------------- validate_against_panel


def test_validate_against_panel_reports_match_rate_and_coverage():
    e = date(2026, 5, 5)
    events = pd.DataFrame([
        events_row("AAA", e, e, date(2026, 5, 6), realized_move=0.10),
        events_row("BBB", e, e, date(2026, 5, 6), realized_move=0.03),
        events_row("CCC", e, e, date(2026, 5, 6), realized_move=0.03),
    ])
    bars = {"AAA": bars_df([(e, 100.0), (date(2026, 5, 6), 110.0)]),   # matches (0.10 vs 0.10)
           "BBB": bars_df([(e, 100.0), (date(2026, 5, 6), 130.0)]),    # 0.30 vs 0.03: mismatch
           }  # CCC has no bars: unavailable
    out = eh.build_events(events, bars)
    v = eh.validate_against_panel(out)
    assert v.n_total == 3
    assert v.n_available == 2
    assert v.coverage_rate == pytest.approx(2 / 3)
    assert v.n_matches == 1
    assert v.match_rate == pytest.approx(1 / 2)
    assert len(v.worst) <= 10


def test_validate_against_panel_empty_input():
    out = eh.build_events(pd.DataFrame(), {})
    v = eh.validate_against_panel(out)
    assert v.n_total == 0
    assert math.isnan(v.match_rate)
    assert math.isnan(v.coverage_rate)


# ----------------------------------------------------------------------------- fetch_bars_cached


def test_fetch_bars_cached_writes_and_reuses_the_cache(tmp_path, monkeypatch):
    monkeypatch.setattr(eh, "BARS_DIR", str(tmp_path / "bars"))
    calls = {"n": 0}

    def fake_bars(ticker, rng):
        calls["n"] += 1
        return [{"date": "2026-05-05", "open": 1, "high": 2, "low": 0.5, "close": 1.5,
                 "adj": 1.5, "volume": 100}]

    import sys
    import types
    fake_chart = types.ModuleType("chart")
    fake_chart.bars = fake_bars
    monkeypatch.setitem(sys.modules, "chart", fake_chart)

    df1 = eh.fetch_bars_cached("AAA")
    assert calls["n"] == 1
    assert len(df1) == 1
    assert os.path.exists(eh.bars_path("AAA"))

    df2 = eh.fetch_bars_cached("AAA")  # cache hit: no second network call
    assert calls["n"] == 1
    pd.testing.assert_frame_equal(df1.reset_index(drop=True), df2.reset_index(drop=True))


def test_fetch_bars_cached_is_fail_soft_and_does_not_cache_a_network_error(tmp_path, monkeypatch):
    monkeypatch.setattr(eh, "BARS_DIR", str(tmp_path / "bars"))

    def raising_bars(ticker, rng):
        raise ConnectionError("boom")

    import sys
    import types
    fake_chart = types.ModuleType("chart")
    fake_chart.bars = raising_bars
    monkeypatch.setitem(sys.modules, "chart", fake_chart)

    df = eh.fetch_bars_cached("AAA")
    assert df.empty
    assert not os.path.exists(eh.bars_path("AAA"))  # not cached: a later run can retry


# ----------------------------------------------------------------------------- Finnhub calendar cache


def test_fetch_finnhub_calendar_cached_available_false_when_key_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(eh, "FINNHUB_DIR", str(tmp_path / "finnhub"))
    out = eh.fetch_finnhub_calendar_cached("AAA", "2026-01-01", "2026-06-01", key="")
    assert out["available"] is False
    assert "FINNHUB_API_KEY" in out["skip_reason"]
    cached = json.loads(open(eh.finnhub_calendar_path("AAA")).read())
    assert cached == out


def test_fetch_finnhub_calendar_cached_parses_rows_and_caches(tmp_path):
    def fake_getter(url):
        return {"earningsCalendar": [{"symbol": "AAA", "date": "2026-09-10", "hour": "amc"}]}

    eh_dir = tmp_path / "finnhub"
    import unittest.mock as mock
    with mock.patch.object(eh, "FINNHUB_DIR", str(eh_dir)):
        out = eh.fetch_finnhub_calendar_cached("AAA", "2026-01-01", "2026-12-31", key="k",
                                               getter=fake_getter)
        assert out["available"] is True
        assert out["rows"][0]["hour"] == "amc"
        # second call hits the cache, not the getter
        out2 = eh.fetch_finnhub_calendar_cached("AAA", "2026-01-01", "2026-12-31", key="k",
                                                getter=lambda u: (_ for _ in ()).throw(AssertionError("should not call")))
        assert out2 == out


def test_fetch_finnhub_calendar_cached_available_false_on_request_error(tmp_path):
    def failing_getter(url):
        raise eh.FinnhubError("HTTP 429")

    import unittest.mock as mock
    with mock.patch.object(eh, "FINNHUB_DIR", str(tmp_path / "finnhub")):
        out = eh.fetch_finnhub_calendar_cached("AAA", "2026-01-01", "2026-12-31", key="k",
                                               getter=failing_getter)
        assert out["available"] is False
        assert "429" in out["skip_reason"]
