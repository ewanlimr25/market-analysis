"""engine.watch.universe: the §1 universe filter (issue_type, marketcap, close, daily_contract
coverage). `filter_universe` is pure -- these tests never touch disk."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine.watch import universe as U

pytestmark = pytest.mark.unit

D = date(2026, 6, 9)


def _screener(rows):
    base = {"issue_type": "Common Stock", "is_index": False, "marketcap": 5e9, "close": 50.0,
            "week_52_high": 60.0, "week_52_low": 40.0, "iv30d": 0.4, "iv_rank": 50.0,
            "next_earnings_date": None, "sector": "Technology", "bullish_premium": 1e6,
            "bearish_premium": 1e6, "net_call_premium": 0.0, "net_put_premium": 0.0, "date": D}
    return pd.DataFrame([{**base, **r} for r in rows])


def test_filter_universe_keeps_common_stock_and_adr_only():
    df = _screener([
        {"ticker": "A", "issue_type": "Common Stock"},
        {"ticker": "B", "issue_type": "ADR"},
        {"ticker": "C", "issue_type": "ETF"},
        {"ticker": "D", "issue_type": None},
    ])
    coverage = pd.DataFrame({"ticker": ["A", "B", "C", "D"], "date": [D, D, D, D]})
    out = U.filter_universe(df, coverage)
    assert sorted(out["ticker"]) == ["A", "B"]


def test_filter_universe_marketcap_and_close_thresholds():
    df = _screener([
        {"ticker": "LOW_MCAP", "marketcap": 0.99e9},
        {"ticker": "OK_MCAP", "marketcap": 1e9},
        {"ticker": "LOW_CLOSE", "close": 9.99},
        {"ticker": "OK_CLOSE", "close": 10.0},
    ])
    coverage = pd.DataFrame({"ticker": df["ticker"], "date": D})
    out = U.filter_universe(df, coverage)
    assert sorted(out["ticker"]) == ["OK_CLOSE", "OK_MCAP"]


def test_filter_universe_requires_daily_contract_coverage():
    df = _screener([{"ticker": "COVERED"}, {"ticker": "UNCOVERED"}])
    coverage = pd.DataFrame({"ticker": ["COVERED"], "date": [D]})
    out = U.filter_universe(df, coverage)
    assert list(out["ticker"]) == ["COVERED"]


def test_filter_universe_empty_coverage_gives_empty_universe():
    df = _screener([{"ticker": "A"}])
    out = U.filter_universe(df, pd.DataFrame(columns=["ticker", "date"]))
    assert out.empty


def test_filter_universe_empty_screener_panel():
    out = U.filter_universe(pd.DataFrame(columns=list(U.SCREENER_COLUMNS)),
                             pd.DataFrame({"ticker": ["A"], "date": [D]}))
    assert out.empty
