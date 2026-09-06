"""The S-B parameters were frozen on 2026-09-05 (DESIGN/80). This test pins every value, and
re-pins the S-A set so that adding S-B provably changed nothing above it in config.py."""
from __future__ import annotations

from datetime import date

import pytest

from engine import config

pytestmark = pytest.mark.unit

FROZEN_SB = {"target_dte_cal": 21, "dte_cal_min": 7, "dte_cal_max": 30, "short_sigma": 1.0, "wing_sigma": 2.0,
             "strike_band_sigma": 0.25, "leg_size_min": 5, "short_spread_max": 0.10, "median_window": 20,
             "take_profit_frac": 0.50}
FROZEN_SB_SIZING = {"equity": 100_000.0, "max_loss_frac": 0.03, "max_open_per_sleeve": 3}
FROZEN_SB_WINDOWS = {"P1": (date(2023, 9, 8), date(2024, 8, 30)), "P2": (date(2024, 9, 6), date(2025, 8, 29)),
                     "P3": (date(2025, 9, 5), date(2026, 11, 6))}
FROZEN_IV_MULT = {("SPY", "p1"): 1.07, ("SPY", "p2"): 1.35, ("SPY", "c1"): 0.65, ("SPY", "c2"): 0.74,
                  ("QQQ", "p1"): 1.08, ("QQQ", "p2"): 1.34, ("QQQ", "c1"): 0.76, ("QQQ", "c2"): 0.79}
FROZEN_SPREAD = {("SPY", "p1"): 0.0076, ("SPY", "p2"): 0.0132, ("SPY", "c1"): 0.0225, ("SPY", "c2"): 0.222,
                 ("QQQ", "p1"): 0.0086, ("QQQ", "p2"): 0.0132, ("QQQ", "c1"): 0.0121, ("QQQ", "c2"): 0.0314}
FROZEN_BAR = {"SB_PRIMARY_TESTS": 4, "SB_DSR_TRIALS": 6, "SB_NW_LAG": 2, "SB_GO_T_MIN": 2.0,
              "SB_GO_MONTH_LOSS_MULT": 3.0, "SB_SCALE_MIN_POSITIONS": 40, "SB_PBO_BLOCKS": 16,
              "SB_PROXY_STRIKE_STEP": 1.0}
FROZEN_SA = {"price_min": 10.0, "mcap_min": 2e9, "mcap_max": 50e9, "adv_min": 50e6, "atm_band": 0.025,
             "leg_size_min": 10, "spread_max": 0.10, "implied_min": 0.04, "implied_max": 0.15, "wing_mult": 2.0,
             "a2_excluded_sectors": ("Technology", "Communication Services")}


def test_sb_params_are_frozen():
    assert config.SB_PARAMS.__dict__ == FROZEN_SB
    assert config.SB_SIZING.__dict__ == FROZEN_SB_SIZING
    assert config.SB_FROZEN_ON == date(2026, 9, 5)
    assert config.SB_LEDGER_OPENS == date(2026, 9, 11)


def test_sb_windows_universe_and_proxy_constants_are_frozen():
    assert config.SB_WINDOWS == FROZEN_SB_WINDOWS
    assert config.SB_MARKED_WINDOW == (date(2026, 3, 13), date(2026, 11, 6))
    assert config.SB_UNDERLYINGS == ("SPY", "QQQ") and config.SB_STRUCTURES == ("PS", "IC")
    assert config.SB_VOL_INDEX == {"SPY": "vix", "QQQ": "vxn"}
    assert config.SB_PROXY_IV_MULT == FROZEN_IV_MULT
    assert config.SB_PROXY_SPREAD == FROZEN_SPREAD


def test_sb_bar_is_frozen():
    for name, value in FROZEN_BAR.items():
        assert getattr(config, name) == value, name


def test_sa_set_is_untouched_by_the_sb_addition():
    assert config.SA_PARAMS.__dict__ == FROZEN_SA
    assert config.SIZING.__dict__ == {"equity": 100_000.0, "ic_max_loss_frac": 0.005, "ss_stress_frac": 0.010,
                                      "ss_stress_move_mult": 3.0, "max_open_events": 8, "max_per_sector": 3,
                                      "night_budget_frac": 0.40}
