"""engine.watch.flows: C-LEAP (single-leg ask-side call premium, DTE>=180, >=$1M) and C-DP
(dark-pool premium >= $5M) daily aggregates (DESIGN/110-watch-basket.md §2)."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine.watch import flows as F

pytestmark = pytest.mark.unit

D = date(2026, 6, 9)


def _opt_row(ticker, side, option_type, code, premium, expiry, canceled=False):
    return {"underlying_symbol": ticker, "side": side, "option_type": option_type,
            "upstream_condition_detail": code, "premium": premium, "expiry": expiry,
            "canceled": canceled}


def _write(tmp_path, rows, name="opts.parquet"):
    path = str(tmp_path / name)
    pd.DataFrame(rows).to_parquet(path, index=False)
    return path


def test_leap_flags_sums_qualifying_prints_and_applies_the_floor(tmp_path):
    rows = [
        _opt_row("BIGCALL", "ask", "call", "auto", 600_000.0, date(2027, 1, 15)),
        _opt_row("BIGCALL", "ask", "call", "slan", 500_000.0, date(2027, 1, 15)),  # sums to 1.1M >= floor
        _opt_row("SMALL", "ask", "call", "auto", 999_999.0, date(2027, 1, 15)),    # just under the floor
        _opt_row("SHORTDATE", "ask", "call", "auto", 5_000_000.0, date(2026, 8, 1)),  # DTE < 180
        _opt_row("BIDSIDE", "bid", "call", "auto", 5_000_000.0, date(2027, 1, 15)),    # wrong side
        _opt_row("PUTSIDE", "ask", "put", "auto", 5_000_000.0, date(2027, 1, 15)),     # wrong type
        _opt_row("MULTILEG", "ask", "call", "mlet", 5_000_000.0, date(2027, 1, 15)),   # not single-leg
        _opt_row("CANCELED", "ask", "call", "auto", 5_000_000.0, date(2027, 1, 15), canceled=True),
    ]
    out = F.leap_flags_for_day(_write(tmp_path, rows), D)
    tickers = dict(zip(out.ticker, out.call_ask_premium))
    assert tickers == {"BIGCALL": pytest.approx(1_100_000.0)}


def test_leap_flags_missing_file_is_empty(tmp_path):
    out = F.leap_flags_for_day(str(tmp_path / "missing.parquet"), D)
    assert out.empty
    assert list(out.columns) == ["ticker", "call_ask_premium"]


def _dp_row(ticker, premium, canceled=False):
    return {"ticker": ticker, "premium": premium, "canceled": canceled}


def test_dp_flags_sums_and_applies_the_floor(tmp_path):
    rows = [
        _dp_row("BIGDP", 3_000_000.0), _dp_row("BIGDP", 2_500_000.0),   # sums to 5.5M >= floor
        _dp_row("SMALLDP", 4_999_999.0),
        _dp_row("CANCELEDDP", 10_000_000.0, canceled=True),
    ]
    out = F.dp_flags_for_day(_write(tmp_path, rows, "dp.parquet"))
    tickers = dict(zip(out.ticker, out.dp_premium))
    assert tickers == {"BIGDP": pytest.approx(5_500_000.0)}


def test_dp_flags_missing_file_is_empty(tmp_path):
    out = F.dp_flags_for_day(str(tmp_path / "missing.parquet"))
    assert out.empty
