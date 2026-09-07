"""scripts/g7_rv_comparison.py: the S-C-universe RV-measure comparison (G7 task 2). Unit tests on
the pure transforms only (`summarize`, `apply_sc_universe`'s filters); no mart or network I/O.
"""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from scripts import g7_rv_comparison as cmp

pytestmark = pytest.mark.unit


def test_summarize_empty_input():
    out = cmp.summarize(pd.DataFrame())
    assert out == {"n": 0}


def test_summarize_computes_correlation_ratio_and_premium():
    df = pd.DataFrame({
        "ticker": ["A", "B", "C", "D"],
        "date": [date(2026, 5, 1)] * 4,
        "rv5_20d": [0.30, 0.40, 0.50, 0.20],
        "c2c_20d": [0.40, 0.50, 0.60, 0.30],
        "parkinson_20d": [0.25, 0.35, 0.45, 0.15],
        "iv30d": [0.45, 0.45, 0.45, 0.45],
    })
    out = cmp.summarize(df)
    assert out["n"] == 4
    assert out["n_tickers"] == 4
    assert out["mean_ratio_rv5_over_c2c"] == pytest.approx((0.75 + 0.8 + 0.8333 + 0.6667) / 4, rel=1e-3)
    # premium_c2c = iv30d - c2c_20d: [0.05, -0.05, -0.15, 0.15] -> 2 of 4 positive
    assert out["premium_c2c_share_positive"] == pytest.approx(0.5)
    assert out["premium_c2c_mean"] == pytest.approx((0.05 - 0.05 - 0.15 + 0.15) / 4)


def test_apply_sc_universe_filters_marketcap_and_iv_band():
    windows = pd.DataFrame({"ticker": ["A", "B", "C"], "date": [date(2026, 5, 1)] * 3,
                            "window_start": [date(2026, 4, 1)] * 3,
                            "rv5_20d": [0.3, 0.3, 0.3], "c2c_20d": [0.3, 0.3, 0.3],
                            "parkinson_20d": [0.3, 0.3, 0.3]})
    screener = pd.DataFrame({"ticker": ["A", "B", "C"], "date": [date(2026, 5, 1)] * 3,
                             "issue_type": ["Common Stock"] * 3,
                             "marketcap": [5e9, 30e9, 5e9],       # B fails F3 (too big)
                             "iv30d": [0.45, 0.45, 0.90]})        # C fails F6 (too high)
    out = cmp.apply_sc_universe(windows, screener)
    assert list(out.ticker) == ["A"]


def test_apply_sc_universe_earnings_free_excludes_a_window_with_a_print_inside_it():
    windows = pd.DataFrame({"ticker": ["A", "B"], "date": [date(2026, 5, 20)] * 2,
                            "window_start": [date(2026, 4, 21)] * 2,
                            "rv5_20d": [0.3, 0.3], "c2c_20d": [0.3, 0.3],
                            "parkinson_20d": [0.3, 0.3]})
    screener = pd.DataFrame({"ticker": ["A", "B"], "date": [date(2026, 5, 20)] * 2,
                             "issue_type": ["Common Stock"] * 2,
                             "marketcap": [5e9, 5e9], "iv30d": [0.45, 0.45]})
    earnings = pd.DataFrame({"ticker": ["A"], "E": [date(2026, 5, 5)]})  # inside A's window
    out = cmp.apply_sc_universe(windows, screener, earnings, earnings_free_only=True)
    assert list(out.ticker) == ["B"]


def test_apply_sc_universe_earnings_free_keeps_a_print_outside_the_window():
    windows = pd.DataFrame({"ticker": ["A"], "date": [date(2026, 5, 20)],
                            "window_start": [date(2026, 4, 21)],
                            "rv5_20d": [0.3], "c2c_20d": [0.3], "parkinson_20d": [0.3]})
    screener = pd.DataFrame({"ticker": ["A"], "date": [date(2026, 5, 20)],
                             "issue_type": ["Common Stock"], "marketcap": [5e9], "iv30d": [0.45]})
    earnings = pd.DataFrame({"ticker": ["A"], "E": [date(2026, 6, 1)]})  # after the window
    out = cmp.apply_sc_universe(windows, screener, earnings, earnings_free_only=True)
    assert list(out.ticker) == ["A"]
