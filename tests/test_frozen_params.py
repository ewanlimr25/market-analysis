"""The S-A parameters were frozen on 2026-09-05 (DESIGN/70 §0, §3). This test pins every value.

If it fails, a pre-registered filter was edited before the Season 3 read. Do not update the
expected values here; add the idea to the pre-registration ledger for the season after.
"""
from __future__ import annotations

from datetime import date

import pytest

from engine import config

pytestmark = pytest.mark.unit

FROZEN_SA = {"price_min": 10.0, "mcap_min": 2e9, "mcap_max": 50e9, "adv_min": 50e6, "atm_band": 0.025,
             "leg_size_min": 10, "spread_max": 0.10, "implied_min": 0.04, "implied_max": 0.15, "wing_mult": 2.0,
             "a2_excluded_sectors": ("Technology", "Communication Services")}
FROZEN_SIZING = {"equity": 100_000.0, "ic_max_loss_frac": 0.005, "ss_stress_frac": 0.010, "ss_stress_move_mult": 3.0,
                 "max_open_events": 8, "max_per_sector": 3, "night_budget_frac": 0.40}
FROZEN_MARKING = {"TIER1_MIN_SIZE": 5, "MODEL_SPREAD_FLOOR": 0.05, "MODEL_IV_LOOKBACK": 5, "MODEL_SPREAD_LOOKBACK": 20,
                  "COMMISSION_PER_CONTRACT": 0.65, "CONTRACT_MULTIPLIER": 100, "LATE_START": "15:00:00",
                  "EARLY_END": "10:30:00", "SESSION_START": "09:30:00", "SESSION_END_EXCL": "16:01:00"}
FROZEN_SEASONS = {"S1": (date(2026, 4, 1), date(2026, 6, 15)), "S2": (date(2026, 7, 1), date(2026, 9, 4)),
                  "S3": (date(2026, 10, 1), date(2026, 11, 30))}
FROZEN_BAR = {"PRIMARY_TESTS": 4, "DSR_TRIALS": 6, "BH_FDR": 0.10, "GO_T_MIN": 2.5, "GO_MIN_EVENTS": 60,
              "GO_WORST_TO_MEAN_WIN_MAX": 4.0}


def test_sa_filters_are_frozen():
    assert config.SA_PARAMS.__dict__ == FROZEN_SA
    assert config.SA_FROZEN_ON == date(2026, 9, 5)


def test_sizing_is_frozen():
    assert config.SIZING.__dict__ == FROZEN_SIZING


def test_marking_constants_are_frozen():
    for name, value in FROZEN_MARKING.items():
        assert getattr(config, name) == value, name


def test_seasons_and_bar_are_frozen():
    assert config.SEASONS == FROZEN_SEASONS
    for name, value in FROZEN_BAR.items():
        assert getattr(config, name) == value, name
