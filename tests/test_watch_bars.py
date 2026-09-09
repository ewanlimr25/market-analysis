"""engine.watch.bars: cached daily OHLCV lookup (reusing the G7 earnings-history cache) and the
weekly resample used by the RSI conditions (DESIGN/110-watch-basket.md §1, §7)."""
from __future__ import annotations

import os
import sys
from datetime import date

import pandas as pd
import pytest

from engine import config
from engine.watch import bars as B

pytestmark = pytest.mark.unit


def _bars_df(dates, closes, highs=None, lows=None, opens=None, vols=None):
    n = len(dates)
    return pd.DataFrame({
        "date": dates,
        "open": opens or closes,
        "high": highs or closes,
        "low": lows or closes,
        "close": closes,
        "adj": closes,
        "volume": vols or [1_000] * n,
    })


class _FakeChart:
    """Stands in for `scripts/chart.py` at the network boundary: `bars` is the multi-day daily
    array, `session_bar` the single-day current-session read."""

    def __init__(self, daily=None, session=None, daily_error=None, session_error=None):
        self._daily, self._session = daily or [], session
        self._daily_error, self._session_error = daily_error, session_error
        self.daily_calls, self.session_calls = [], []

    def bars(self, ticker, rng):
        self.daily_calls.append((ticker, rng))
        if self._daily_error:
            raise self._daily_error
        rows = self._daily.get(rng, []) if isinstance(self._daily, dict) else self._daily
        return list(rows)

    def session_bar(self, ticker):
        self.session_calls.append(ticker)
        if self._session_error:
            raise self._session_error
        return self._session


class _NoFetch:
    """Any network call through this is a test failure."""

    def bars(self, ticker, rng):
        raise AssertionError(f"must not fetch daily bars for {ticker}")

    def session_bar(self, ticker):
        raise AssertionError(f"must not fetch a session bar for {ticker}")


def _row(day, close, volume=100):
    return {"date": day, "open": close, "high": close, "low": close,
            "close": close, "adj": close, "volume": volume}


def _mart(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    monkeypatch.setattr(B, "EARNINGS_HISTORY_BARS_DIR",
                        os.path.join(config.MART, "earnings_history", "bars"))
    monkeypatch.setattr(B, "WATCH_BARS_DIR", os.path.join(config.MART, "watch", "bars"))


def _seed(path, dates, closes):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    _bars_df(dates, closes).to_parquet(path, index=False)


def test_load_daily_bars_serves_the_earnings_history_cache_without_fetching(tmp_path, monkeypatch):
    _mart(tmp_path, monkeypatch)
    _seed(B.earnings_history_bars_path("AAPL"), [date(2026, 1, 2), date(2026, 1, 5)], [10.0, 11.0])

    monkeypatch.setitem(sys.modules, "chart", _NoFetch())
    out = B.load_daily_bars("AAPL")
    assert list(out["close"]) == [10.0, 11.0]
    assert not os.path.exists(B.watch_bars_path("AAPL"))


def test_load_daily_bars_falls_back_to_its_own_cache_then_a_fetch(tmp_path, monkeypatch):
    _mart(tmp_path, monkeypatch)
    chart = _FakeChart(daily=[_row("2026-01-02", 5.0)])
    monkeypatch.setitem(sys.modules, "chart", chart)
    out1 = B.load_daily_bars("ZZZZ")
    assert chart.daily_calls == [("ZZZZ", B.YAHOO_RANGE)]
    assert list(out1["close"]) == [5.0]
    # second call must hit the now-populated watch cache, not fetch again
    out2 = B.load_daily_bars("ZZZZ")
    assert chart.daily_calls == [("ZZZZ", B.YAHOO_RANGE)]
    assert list(out2["close"]) == [5.0]


def test_load_daily_bars_is_fail_soft_on_a_network_error(tmp_path, monkeypatch):
    _mart(tmp_path, monkeypatch)

    monkeypatch.setitem(sys.modules, "chart", _FakeChart(daily_error=RuntimeError("network down")))
    out = B.load_daily_bars("DEAD")
    assert out.empty
    assert list(out.columns) == list(B.BAR_COLUMNS)


def test_bars_as_of_truncates_and_never_looks_ahead():
    df = _bars_df([date(2026, 1, 2), date(2026, 1, 5), date(2026, 1, 6)], [1.0, 2.0, 3.0])
    out = B.bars_as_of(df, date(2026, 1, 5))
    assert list(out["date"]) == [date(2026, 1, 2), date(2026, 1, 5)]
    assert B.bars_as_of(df.iloc[0:0], date(2026, 1, 5)).empty


def test_weekly_bars_resamples_on_the_last_session_of_each_week():
    # Mon 1/5 .. Fri 1/9 is one week; Mon 1/12 .. Wed 1/14 (short week) is the next.
    dates = [date(2026, 1, 5), date(2026, 1, 6), date(2026, 1, 7), date(2026, 1, 8), date(2026, 1, 9),
             date(2026, 1, 12), date(2026, 1, 13), date(2026, 1, 14)]
    closes = [10, 11, 9, 12, 13, 14, 10, 15]
    highs = [c + 1 for c in closes]
    lows = [c - 1 for c in closes]
    vols = [100] * len(dates)
    df = _bars_df(dates, closes, highs=highs, lows=lows, vols=vols)
    wk = B.weekly_bars(df)
    assert len(wk) == 2
    assert wk.iloc[0]["close"] == 13          # last session of week 1 (Fri 1/9)
    assert wk.iloc[0]["high"] == max(highs[:5])
    assert wk.iloc[0]["low"] == min(lows[:5])
    assert wk.iloc[0]["volume"] == 500
    assert wk.iloc[1]["close"] == 15          # last session of the short second week (Wed 1/14)
    assert wk.iloc[1]["volume"] == 300


def test_weekly_bars_empty_input():
    out = B.weekly_bars(B._empty_bars())
    assert out.empty
    assert "week_end" in out.columns


# =============================================================================================
# Staleness: a cache that stops before the as-of session (2026-09-08)
# =============================================================================================
#
# `evaluate_bar_conditions` needs a bar EXACTLY on its as-of date and returns all-null otherwise,
# so a cache that stops one session short silences every bar-derived condition for every ticker.
# Both caches were written once, on 2026-09-07, and nothing ever refreshed them: the whole
# 2,041-name universe evaluated 11 of its 20 conditions as null on the first live nightly.

SEP4, SEP8 = date(2026, 9, 4), date(2026, 9, 8)


def test_load_daily_bars_refreshes_a_cache_that_stops_before_the_as_of_session(tmp_path, monkeypatch):
    # Arrange
    _mart(tmp_path, monkeypatch)
    _seed(B.earnings_history_bars_path("AAPL"), [date(2026, 9, 3), SEP4], [10.0, 11.0])
    chart = _FakeChart(daily=[_row("2026-09-04", 11.0), _row("2026-09-08", 12.0)])
    monkeypatch.setitem(sys.modules, "chart", chart)

    # Act
    out = B.load_daily_bars("AAPL", as_of=SEP8)

    # Assert
    assert list(out["date"]) == [date(2026, 9, 3), SEP4, SEP8]
    assert chart.daily_calls == [("AAPL", B.TAIL_RANGE)]       # incremental, not the full 10y
    assert chart.session_calls == []                            # daily array already had it
    assert list(B._read(B.watch_bars_path("AAPL"))["date"])[-1] == SEP8
    assert list(B._read(B.earnings_history_bars_path("AAPL"))["date"])[-1] == SEP4   # read-only


def test_load_daily_bars_recovers_the_as_of_session_the_daily_array_still_lacks(tmp_path, monkeypatch):
    # Arrange -- Yahoo's multi-day array lags its own single-day endpoint by hours
    _mart(tmp_path, monkeypatch)
    _seed(B.watch_bars_path("AI"), [date(2026, 9, 3), SEP4], [10.0, 11.0])
    chart = _FakeChart(daily=[_row("2026-09-04", 11.0)], session=_row("2026-09-08", 12.5, volume=999))
    monkeypatch.setitem(sys.modules, "chart", chart)
    monkeypatch.setattr(B, "_today", lambda: SEP8)

    # Act
    out = B.load_daily_bars("AI", as_of=SEP8)

    # Assert
    assert list(out["date"]) == [date(2026, 9, 3), SEP4, SEP8]
    assert out["close"].iloc[-1] == 12.5 and out["volume"].iloc[-1] == 999
    assert chart.session_calls == ["AI"]


def test_load_daily_bars_ignores_a_session_bar_for_a_different_date(tmp_path, monkeypatch):
    _mart(tmp_path, monkeypatch)
    _seed(B.watch_bars_path("AI"), [SEP4], [11.0])
    chart = _FakeChart(daily=[_row("2026-09-04", 11.0)], session=_row("2026-09-09", 13.0))
    monkeypatch.setitem(sys.modules, "chart", chart)
    monkeypatch.setattr(B, "_today", lambda: SEP8)

    out = B.load_daily_bars("AI", as_of=SEP8)

    assert list(out["date"]) == [SEP4]


def test_load_daily_bars_keeps_the_cached_history_when_the_refresh_fails(tmp_path, monkeypatch):
    # A network failure must never empty a cache we already hold -- every bar condition would
    # silently go null for that ticker.
    _mart(tmp_path, monkeypatch)
    _seed(B.watch_bars_path("AI"), [date(2026, 9, 3), SEP4], [10.0, 11.0])
    monkeypatch.setitem(sys.modules, "chart", _FakeChart(daily_error=RuntimeError("network down"),
                                                          session_error=RuntimeError("network down")))

    out = B.load_daily_bars("AI", as_of=SEP8)

    assert list(out["close"]) == [10.0, 11.0]


def test_load_daily_bars_prefers_the_freshest_of_the_two_caches(tmp_path, monkeypatch):
    # Once this module has refreshed a ticker, its own cache is ahead of the read-only G7 one.
    _mart(tmp_path, monkeypatch)
    _seed(B.earnings_history_bars_path("AAPL"), [date(2026, 9, 3), SEP4], [10.0, 11.0])
    _seed(B.watch_bars_path("AAPL"), [date(2026, 9, 3), SEP4, SEP8], [10.0, 11.0, 12.0])
    monkeypatch.setitem(sys.modules, "chart", _NoFetch())

    out = B.load_daily_bars("AAPL", as_of=SEP8)

    assert list(out["close"]) == [10.0, 11.0, 12.0]


def test_load_daily_bars_does_not_fetch_when_the_cache_covers_the_session(tmp_path, monkeypatch):
    _mart(tmp_path, monkeypatch)
    _seed(B.watch_bars_path("AI"), [SEP4, SEP8], [11.0, 12.0])
    monkeypatch.setitem(sys.modules, "chart", _NoFetch())

    assert list(B.load_daily_bars("AI", as_of=SEP8)["close"]) == [11.0, 12.0]


def test_a_refetched_session_overwrites_one_recovered_from_the_single_day_endpoint(tmp_path, monkeypatch):
    # The recovered bar is Yahoo's live single-day read; the next night's tail refresh carries its
    # official value for the same session and must win.
    _mart(tmp_path, monkeypatch)
    _seed(B.watch_bars_path("AI"), [SEP4, SEP8], [11.0, 12.5])
    chart = _FakeChart(daily=[_row("2026-09-04", 11.0), _row("2026-09-08", 12.4)],
                       session=_row("2026-09-09", 13.0))
    monkeypatch.setitem(sys.modules, "chart", chart)
    monkeypatch.setattr(B, "_today", lambda: date(2026, 9, 9))

    out = B.load_daily_bars("AI", as_of=date(2026, 9, 9))

    assert list(out["date"]) == [SEP4, SEP8, date(2026, 9, 9)]
    assert list(out["close"]) == [11.0, 12.4, 13.0]


def test_load_daily_bars_reads_only_one_cache_when_it_already_covers_the_session(tmp_path, monkeypatch):
    # Every universe ticker is looked up once a night, so a needless second parquet read of a
    # 2,500-row history costs ~12 s across a 2,000-name universe.
    _mart(tmp_path, monkeypatch)
    _seed(B.earnings_history_bars_path("AAPL"), [SEP4], [11.0])
    _seed(B.watch_bars_path("AAPL"), [SEP4, SEP8], [11.0, 12.0])
    monkeypatch.setitem(sys.modules, "chart", _NoFetch())
    reads = []
    real_read = B._read
    monkeypatch.setattr(B, "_read", lambda path: reads.append(path) or real_read(path))

    out = B.load_daily_bars("AAPL", as_of=SEP8)

    assert list(out["close"]) == [11.0, 12.0]
    assert reads == [B.watch_bars_path("AAPL")]


def test_load_daily_bars_still_takes_the_freshest_cache_when_no_session_is_named(tmp_path, monkeypatch):
    # With no `as_of` there is nothing to short-circuit on, so both caches are read and the
    # freshest wins -- order must not decide it.
    _mart(tmp_path, monkeypatch)
    _seed(B.earnings_history_bars_path("AAPL"), [SEP4, SEP8], [11.0, 12.0])
    _seed(B.watch_bars_path("AAPL"), [SEP4], [11.0])
    monkeypatch.setitem(sys.modules, "chart", _NoFetch())

    assert list(B.load_daily_bars("AAPL")["close"]) == [11.0, 12.0]


# =============================================================================================
# Adjustment basis: Yahoo back-adjusts the WHOLE raw OHLC history when a split executes
# =============================================================================================

def test_a_tail_on_a_new_split_basis_forces_a_full_refetch_instead_of_a_splice(tmp_path, monkeypatch):
    # Arrange -- the cache predates a 2:1 split, so its closes are twice the ones Yahoo serves now.
    # Merging the two would book a fake -50% overnight move that poisons ATR, RSI, the zigzag and
    # the 52-week extremes for the ~9 months the boundary stays inside the 252-session lookback.
    _mart(tmp_path, monkeypatch)
    _seed(B.watch_bars_path("MNST"), [date(2026, 9, 2), date(2026, 9, 3), SEP4], [90.0, 91.0, 92.0])
    chart = _FakeChart(daily={
        B.TAIL_RANGE: [_row("2026-09-03", 45.5), _row("2026-09-04", 46.0), _row("2026-09-08", 47.0)],
        B.YAHOO_RANGE: [_row("2026-09-02", 45.0), _row("2026-09-03", 45.5),
                        _row("2026-09-04", 46.0), _row("2026-09-08", 47.0)],
    })
    monkeypatch.setitem(sys.modules, "chart", chart)

    # Act
    out = B.load_daily_bars("MNST", as_of=SEP8)

    # Assert -- one basis only, and the stale rows are gone rather than merged under it
    assert [r for _, r in chart.daily_calls] == [B.TAIL_RANGE, B.YAHOO_RANGE]
    assert list(out["close"]) == [45.0, 45.5, 46.0, 47.0]


def test_a_tail_that_does_not_overlap_the_cache_forces_a_full_refetch(tmp_path, monkeypatch):
    # No shared session means the basis cannot be checked, so the merge is not safe to make.
    _mart(tmp_path, monkeypatch)
    _seed(B.watch_bars_path("MNST"), [date(2026, 1, 5)], [90.0])
    chart = _FakeChart(daily={
        B.TAIL_RANGE: [_row("2026-09-04", 46.0), _row("2026-09-08", 47.0)],
        B.YAHOO_RANGE: [_row("2026-01-05", 45.0), _row("2026-09-04", 46.0), _row("2026-09-08", 47.0)],
    })
    monkeypatch.setitem(sys.modules, "chart", chart)

    out = B.load_daily_bars("MNST", as_of=SEP8)

    assert [r for _, r in chart.daily_calls] == [B.TAIL_RANGE, B.YAHOO_RANGE]
    assert list(out["close"]) == [45.0, 46.0, 47.0]


def test_a_tail_on_the_same_basis_is_merged_without_a_second_fetch(tmp_path, monkeypatch):
    _mart(tmp_path, monkeypatch)
    _seed(B.watch_bars_path("AAPL"), [date(2026, 9, 3), SEP4], [45.5, 46.0])
    chart = _FakeChart(daily={B.TAIL_RANGE: [_row("2026-09-04", 46.0), _row("2026-09-08", 47.0)]})
    monkeypatch.setitem(sys.modules, "chart", chart)

    out = B.load_daily_bars("AAPL", as_of=SEP8)

    assert [r for _, r in chart.daily_calls] == [B.TAIL_RANGE]
    assert list(out["close"]) == [45.5, 46.0, 47.0]


# =============================================================================================
# The "never raises" contract -- one bad file must not blank the whole basket
# =============================================================================================

def test_an_unreadable_cache_is_treated_as_absent_and_refetched_in_full(tmp_path, monkeypatch):
    # `nightly.build_ticker_series_map` runs this under a thread pool whose exceptions re-raise in
    # the parent, where `nightly()` catches them at STEP level: one bad file would blank all 2,041
    # names instead of nulling one ticker.
    _mart(tmp_path, monkeypatch)
    path = B.watch_bars_path("AAPL")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(b"not a parquet file")
    chart = _FakeChart(daily={B.YAHOO_RANGE: [_row("2026-09-04", 46.0), _row("2026-09-08", 47.0)]})
    monkeypatch.setitem(sys.modules, "chart", chart)

    out = B.load_daily_bars("AAPL", as_of=SEP8)

    assert [r for _, r in chart.daily_calls] == [B.YAHOO_RANGE]
    assert list(out["close"]) == [46.0, 47.0]


def test_a_cache_missing_a_bar_column_is_treated_as_absent(tmp_path, monkeypatch):
    _mart(tmp_path, monkeypatch)
    path = B.watch_bars_path("AAPL")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    _bars_df([SEP4], [46.0]).drop(columns=["adj"]).to_parquet(path, index=False)
    chart = _FakeChart(daily={B.YAHOO_RANGE: [_row("2026-09-08", 47.0)]})
    monkeypatch.setitem(sys.modules, "chart", chart)

    assert list(B.load_daily_bars("AAPL", as_of=SEP8)["close"]) == [47.0]


def test_an_unchanged_cache_is_not_rewritten(tmp_path, monkeypatch):
    # A Yahoo outage must not rewrite ~206 MB of byte-identical parquet across the universe.
    _mart(tmp_path, monkeypatch)
    _seed(B.watch_bars_path("AI"), [SEP4], [11.0])
    monkeypatch.setitem(sys.modules, "chart", _FakeChart(daily_error=RuntimeError("network down"),
                                                          session_error=RuntimeError("network down")))
    writes = []
    monkeypatch.setattr(B, "_write", lambda t, df: writes.append(t))

    B.load_daily_bars("AI", as_of=SEP8)

    assert writes == []


def test_the_session_endpoint_is_not_called_for_a_date_that_is_not_today(tmp_path, monkeypatch):
    # `chart.session_bar` always answers about the CURRENT session, so a backfill or panel run
    # would pay a round-trip per ticker for a result discarded by construction.
    _mart(tmp_path, monkeypatch)
    _seed(B.watch_bars_path("AI"), [SEP4], [11.0])
    chart = _FakeChart(daily={B.TAIL_RANGE: [_row("2026-09-04", 11.0)]}, session=_row("2026-09-08", 12.0))
    monkeypatch.setitem(sys.modules, "chart", chart)
    monkeypatch.setattr(B, "_today", lambda: date(2026, 9, 30))

    B.load_daily_bars("AI", as_of=SEP8)

    assert chart.session_calls == []


def test_load_daily_bars_rejects_as_of_and_force_passed_positionally(tmp_path, monkeypatch):
    # `as_of` was inserted ahead of `force`; keyword-only keeps an old 3-positional call from
    # silently reading a bool as a date.
    _mart(tmp_path, monkeypatch)
    with pytest.raises(TypeError):
        B.load_daily_bars("AI", "10y", True)
