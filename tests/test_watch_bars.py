"""engine.watch.bars: cached daily OHLCV lookup (reusing the G7 earnings-history cache) and the
weekly resample used by the RSI conditions (DESIGN/110-watch-basket.md §1, §7)."""
from __future__ import annotations

import os
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


def test_load_daily_bars_prefers_the_earnings_history_cache(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    monkeypatch.setattr(B, "EARNINGS_HISTORY_BARS_DIR", os.path.join(config.MART, "earnings_history", "bars"))
    monkeypatch.setattr(B, "WATCH_BARS_DIR", os.path.join(config.MART, "watch", "bars"))
    eh_path = B.earnings_history_bars_path("AAPL")
    os.makedirs(os.path.dirname(eh_path), exist_ok=True)
    _bars_df([date(2026, 1, 2), date(2026, 1, 5)], [10.0, 11.0]).to_parquet(eh_path, index=False)

    def boom(*a, **k):
        raise AssertionError("must not fetch when the earnings_history cache already has this ticker")

    monkeypatch.setattr(B, "_fetch_and_cache", boom)
    out = B.load_daily_bars("AAPL")
    assert list(out["close"]) == [10.0, 11.0]
    assert not os.path.exists(B.watch_bars_path("AAPL"))


def test_load_daily_bars_falls_back_to_its_own_cache_then_a_fetch(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    monkeypatch.setattr(B, "EARNINGS_HISTORY_BARS_DIR", os.path.join(config.MART, "earnings_history", "bars"))
    monkeypatch.setattr(B, "WATCH_BARS_DIR", os.path.join(config.MART, "watch", "bars"))
    calls = []

    def fake_fetch(ticker, rng):
        calls.append(ticker)
        df = _bars_df([date(2026, 1, 2)], [5.0])
        path = B.watch_bars_path(ticker)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        df.to_parquet(path, index=False)
        return df

    monkeypatch.setattr(B, "_fetch_and_cache", fake_fetch)
    out1 = B.load_daily_bars("ZZZZ")
    assert calls == ["ZZZZ"]
    assert list(out1["close"]) == [5.0]
    # second call must hit the now-populated watch cache, not fetch again
    out2 = B.load_daily_bars("ZZZZ")
    assert calls == ["ZZZZ"]
    assert list(out2["close"]) == [5.0]


def test_load_daily_bars_is_fail_soft_on_a_network_error(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    monkeypatch.setattr(B, "EARNINGS_HISTORY_BARS_DIR", os.path.join(config.MART, "earnings_history", "bars"))
    monkeypatch.setattr(B, "WATCH_BARS_DIR", os.path.join(config.MART, "watch", "bars"))

    class FakeChart:
        @staticmethod
        def bars(ticker, rng):
            raise RuntimeError("network down")

    import sys
    monkeypatch.setitem(sys.modules, "chart", FakeChart)
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
