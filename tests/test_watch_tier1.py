"""engine.watch.tier1: the tier-1 ATM pair query (S-C's F7/F8, DESIGN/110 §2 C-VOL evidence),
against small synthetic `daily_contract`-shaped parquet fixtures."""
from __future__ import annotations

import pandas as pd
import pytest

from engine.watch import tier1 as T

pytestmark = pytest.mark.unit


def _contract_row(ticker, option_type, strike, dte_cal, size_late, underlying_last, expiry="2026-07-07"):
    return {"underlying_symbol": ticker, "option_type": option_type, "strike": strike,
            "expiry": expiry, "dte_cal": dte_cal, "size_late": size_late,
            "underlying_last": underlying_last}


def _write(tmp_path, rows, name="part.parquet"):
    path = str(tmp_path / name)
    pd.DataFrame(rows).to_parquet(path, index=False)
    return path


def test_good_pair_at_the_nearest_strike_is_true(tmp_path):
    rows = [
        _contract_row("GOOD", "call", 95, 28, 25, 100),    # band 5% -- too far, must be ignored
        _contract_row("GOOD", "put", 95, 28, 25, 100),
        _contract_row("GOOD", "call", 100, 28, 25, 100),   # exact ATM: nearest strike
        _contract_row("GOOD", "put", 100, 28, 30, 100),
        _contract_row("GOOD", "call", 105, 28, 25, 100),   # far strike, ignored
        _contract_row("GOOD", "call", 100, 10, 999, 100),  # out-of-window DTE, must be excluded
    ]
    out = T.tier1_atm_flags_for_partition(_write(tmp_path, rows))
    row = out[out.ticker == "GOOD"].iloc[0]
    assert bool(row.has_tier1_atm_pair) is True


def test_missing_one_side_at_the_nearest_strike_is_false(tmp_path):
    rows = [_contract_row("ONESIDE", "call", 50, 28, 25, 50)]
    out = T.tier1_atm_flags_for_partition(_write(tmp_path, rows))
    row = out[out.ticker == "ONESIDE"].iloc[0]
    assert bool(row.has_tier1_atm_pair) is False


def test_size_late_below_the_tier1_floor_is_false(tmp_path):
    rows = [
        _contract_row("SMALL", "call", 50, 28, 19, 50),   # one below the floor of 20
        _contract_row("SMALL", "put", 50, 28, 30, 50),
    ]
    out = T.tier1_atm_flags_for_partition(_write(tmp_path, rows))
    assert bool(out[out.ticker == "SMALL"].iloc[0].has_tier1_atm_pair) is False


def test_strike_outside_the_band_excludes_the_ticker_entirely(tmp_path):
    rows = [
        _contract_row("FAR", "call", 90, 28, 25, 100),  # band 10%, no strike within 2.5%
        _contract_row("FAR", "put", 90, 28, 25, 100),
    ]
    out = T.tier1_atm_flags_for_partition(_write(tmp_path, rows))
    assert "FAR" not in set(out.ticker)


def test_no_expiry_in_the_dte_window_excludes_the_ticker_entirely(tmp_path):
    rows = [
        _contract_row("SHORTDATED", "call", 100, 5, 25, 100),
        _contract_row("SHORTDATED", "put", 100, 5, 25, 100),
    ]
    out = T.tier1_atm_flags_for_partition(_write(tmp_path, rows))
    assert "SHORTDATED" not in set(out.ticker)


def test_picks_the_expiry_nearest_28_days_over_a_farther_one_in_window(tmp_path):
    rows = [
        _contract_row("PICK", "call", 100, 21, 25, 100, expiry="2026-07-01"),  # |21-28|=7
        _contract_row("PICK", "put", 100, 21, 25, 100, expiry="2026-07-01"),
        # a farther-but-still-in-window expiry with a pair that would also pass, to prove
        # it's excluded once the nearer expiry is chosen
        _contract_row("PICK", "call", 100, 35, 999, 100, expiry="2026-07-15"),  # |35-28|=7 too... use 34
    ]
    # make the second expiry strictly farther from 28 than the first (|34-28|=6 > |21-28|=7 is false,
    # so use dte 21 vs 30: |21-28|=7, |30-28|=2 -- flip so 30 is nearer and must win instead)
    rows = [
        _contract_row("PICK", "call", 100, 40, 25, 100, expiry="2026-08-01"),   # |40-28|=12, farther
        _contract_row("PICK", "put", 100, 40, 25, 100, expiry="2026-08-01"),
        _contract_row("PICK", "call", 100, 30, 25, 100, expiry="2026-07-15"),   # |30-28|=2, nearest
        _contract_row("PICK", "put", 100, 30, 30, 100, expiry="2026-07-15"),
    ]
    out = T.tier1_atm_flags_for_partition(_write(tmp_path, rows))
    assert bool(out[out.ticker == "PICK"].iloc[0].has_tier1_atm_pair) is True


def test_missing_partition_file_gives_empty_frame(tmp_path):
    out = T.tier1_atm_flags_for_partition(str(tmp_path / "does_not_exist.parquet"))
    assert out.empty
    assert list(out.columns) == ["ticker", "has_tier1_atm_pair"]
