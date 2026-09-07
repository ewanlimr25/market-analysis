"""G6 data-layer orchestration: `build_rows_for_week` on synthetic (already-loaded) frames,
plus a small integration check of the real I/O against the panel."""
from __future__ import annotations

import os
from datetime import date

import duckdb
import pandas as pd
import pytest

from engine import config
from engine.research.expiry_pinning import ExpiryWeek
from engine.research import expiry_pinning_data as D
from engine.research.expiry_pinning_data import ScreenerRow, build_rows_for_week

WEEK = ExpiryWeek(friday=date(2026, 3, 20), expiry=date(2026, 3, 20), is_monthly=True,
                  day_minus_1=date(2026, 3, 19), prior_friday=date(2026, 3, 13))


def _raw_oi(rows: list[tuple[str, str, float, int]]) -> pd.DataFrame:
    """rows of (underlying, option_symbol_suffix_type, strike, curr_oi); builds OCC symbols
    for the WEEK's expiry (260320)."""
    out = []
    for und, cp, strike, oi in rows:
        sym = f"{und}260320{cp}{int(strike * 1000):08d}"
        out.append({"option_symbol": sym, "underlying_symbol": und, "strike": strike, "curr_oi": oi})
    return pd.DataFrame(out)


@pytest.mark.unit
def test_build_rows_for_week_includes_only_qualifying_names():
    raw = _raw_oi([
        ("BIG", "C", 100.0, 4000), ("BIG", "P", 100.0, 2000),   # total 6000 >= floor
        ("SMALL", "C", 50.0, 1000), ("SMALL", "P", 50.0, 500),  # total 1500 < floor
    ])
    screener = {
        ("BIG", WEEK.day_minus_1): ScreenerRow("Common Stock", 3e9, 100.0),
        ("BIG", WEEK.expiry): ScreenerRow("Common Stock", 3e9, 100.2),
        ("BIG", WEEK.prior_friday): ScreenerRow("Common Stock", 3e9, 98.0),
        ("SMALL", WEEK.day_minus_1): ScreenerRow("Common Stock", 3e9, 50.0),
        ("SMALL", WEEK.expiry): ScreenerRow("Common Stock", 3e9, 50.1),
    }
    rows = build_rows_for_week(WEEK, raw, screener)
    assert [r["underlying"] for r in rows] == ["BIG"]


@pytest.mark.unit
def test_build_rows_for_week_excludes_below_mcap_floor():
    raw = _raw_oi([("X", "C", 100.0, 6000), ("X", "P", 100.0, 2000)])
    screener = {
        ("X", WEEK.day_minus_1): ScreenerRow("Common Stock", 1.5e9, 100.0),  # below $2B
        ("X", WEEK.expiry): ScreenerRow("Common Stock", 1.5e9, 100.1),
    }
    assert build_rows_for_week(WEEK, raw, screener) == []


@pytest.mark.unit
def test_build_rows_for_week_excludes_etf_issue_type():
    raw = _raw_oi([("SPY", "C", 700.0, 10000), ("SPY", "P", 700.0, 10000)])
    screener = {
        ("SPY", WEEK.day_minus_1): ScreenerRow("ETF", 5e11, 700.0),
        ("SPY", WEEK.expiry): ScreenerRow("ETF", 5e11, 701.0),
    }
    assert build_rows_for_week(WEEK, raw, screener) == []


@pytest.mark.unit
def test_build_rows_for_week_missing_expiry_close_drops_the_name():
    raw = _raw_oi([("X", "C", 100.0, 6000), ("X", "P", 100.0, 2000)])
    screener = {("X", WEEK.day_minus_1): ScreenerRow("Common Stock", 3e9, 100.0)}   # no expiry-day row
    assert build_rows_for_week(WEEK, raw, screener) == []


@pytest.mark.unit
def test_build_rows_for_week_missing_prior_friday_leaves_baseline_columns_nan():
    raw = _raw_oi([("X", "C", 100.0, 6000), ("X", "P", 100.0, 2000)])
    screener = {
        ("X", WEEK.day_minus_1): ScreenerRow("Common Stock", 3e9, 100.0),
        ("X", WEEK.expiry): ScreenerRow("Common Stock", 3e9, 100.4),
        # no prior_friday row
    }
    rows = build_rows_for_week(WEEK, raw, screener)
    assert len(rows) == 1
    row = rows[0]
    assert row["close_prior_friday"] is None
    assert pd.isna(row["dist_pin_prior_friday"])
    assert pd.isna(row["nearest_any_strike_dist_prior_friday"])
    assert not pd.isna(row["dist_pin_expiry"])


@pytest.mark.unit
def test_build_rows_for_week_computes_pin_and_distances():
    raw = _raw_oi([
        ("X", "C", 95.0, 100), ("X", "P", 95.0, 100),
        ("X", "C", 100.0, 3000), ("X", "P", 100.0, 3000),   # the pin: 6000 combined
        ("X", "C", 105.0, 200), ("X", "P", 105.0, 100),
    ])
    screener = {
        ("X", WEEK.day_minus_1): ScreenerRow("Common Stock", 3e9, 99.5),
        ("X", WEEK.expiry): ScreenerRow("Common Stock", 3e9, 100.3),
        ("X", WEEK.prior_friday): ScreenerRow("Common Stock", 3e9, 96.0),
    }
    rows = build_rows_for_week(WEEK, raw, screener)
    assert len(rows) == 1
    row = rows[0]
    assert row["pin_strike"] == 100.0
    assert row["dist_pin_expiry"] == pytest.approx(abs(100.3 - 100.0) / 100.3)
    assert row["dist_pin_prior_friday"] == pytest.approx(abs(96.0 - 100.0) / 96.0)
    assert row["placebo_second_strike"] == 105.0   # 300 combined beats 95's 200
    assert row["total_oi"] == 6500
    assert row["n_strikes"] == 3


# ----------------------------------------------------------------------------- integration

REAL_EXPIRY = date(2026, 9, 4)
REAL_OI_PATH = D.oi_snapshot_path(REAL_EXPIRY)
needs_panel = pytest.mark.skipif(not os.path.exists(REAL_OI_PATH), reason="UW panel not available")


@pytest.mark.integration
@needs_panel
def test_load_oi_snapshot_curr_oi_matches_daily_contract_open_interest():
    """Cross-check the module's docstring claim: curr_oi on the file dated D equals
    `daily_contract.open_interest` for the same date (both are OI effective at D's start)."""
    raw = D.load_oi_snapshot(REAL_EXPIRY)
    assert not raw.empty
    sample = raw[raw["underlying_symbol"] == "SPY"].iloc[0]
    dc_path = os.path.join(config.MART, "daily_contract", f"date={REAL_EXPIRY.isoformat()}", "part.parquet")
    if not os.path.exists(dc_path):
        pytest.skip("daily_contract mart partition not built for this date")
    dc_row = duckdb.connect().execute(
        f"SELECT open_interest FROM read_parquet('{dc_path}') "
        f"WHERE option_chain_id = '{sample['option_symbol']}'").fetchone()
    if dc_row is None:
        pytest.skip("sampled contract did not print on the expiry day; no daily_contract row")
    assert dc_row[0] == sample["curr_oi"]


@pytest.mark.integration
@needs_panel
def test_screener_panel_has_marketcap_and_issue_type_for_spy_window():
    panel = D.screener_panel(date(2026, 9, 1), REAL_EXPIRY)
    row = panel[(panel.ticker == "AAPL") & (panel.date == REAL_EXPIRY)]
    assert len(row) == 1
    assert row.iloc[0]["issue_type"] == "Common Stock"
    assert row.iloc[0]["marketcap"] > 0
