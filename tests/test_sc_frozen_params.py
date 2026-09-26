"""The S-C parameters were frozen on 2026-09-26 (findings DESIGN/90 §10 R6), after the D26 edit of
2026-09-25 and before any ledger row. This test pins every value, and re-pins the S-A and S-B sets so
that adding S-C provably changed nothing above it in config.py."""
from __future__ import annotations

from datetime import date

import pytest

from engine import config
from engine.strategies import sc, sc_structures
from test_sb_frozen_params import FROZEN_BAR as FROZEN_SB_BAR, FROZEN_SA, FROZEN_SB, FROZEN_SB_SIZING

pytestmark = pytest.mark.unit

FROZEN_SC = {"price_min": 10.0, "mcap_min": 1e9, "mcap_max": 20e9, "adv_min": 50e6, "iv30d_min": 0.30, "iv30d_max": 0.80,
             "dte_cal_min": 20, "dte_cal_max": 40, "target_dte_cal": 28, "atm_band": 0.025, "leg_size_min": 5,
             "spread_max": 0.08, "select_n": 10, "c2_excluded_sectors": ("Technology",), "wing_sigma": 2.0, "stress_sigma": 3.0}
FROZEN_SC_SIZING = {"equity": 100_000.0, "ib_max_loss_frac": 0.005, "ss_stress_frac": 0.010, "max_new_per_week": 10,
                    "max_open_per_variant": 20, "max_open_per_sector": 4, "book_budget_frac": 0.40}
FROZEN_SC_BAR = {"SC_NW_LAG": 4, "SC_DSR_TRIALS": 6, "SC_GO_T_MIN": 2.0, "SC_GO_MONTH_LOSS_MULT": 3.0,
                 "SC_READ_MIN_WEEKS": 40, "SC_SCALE_MIN_WEEKS": 80, "SC_PBO_BLOCKS": 8}


def test_sc_params_are_frozen():
    assert config.SC_PARAMS.__dict__ == FROZEN_SC
    assert config.SC_SIZING.__dict__ == FROZEN_SC_SIZING
    assert config.SC_FROZEN_ON == date(2026, 9, 26)
    assert config.SC_LEDGER_OPENS == date(2026, 10, 2)


def test_sc_identity_and_bar_are_frozen():
    assert config.SC_VARIANTS == ("C1", "C2") and config.SC_STRUCTURES == ("SS", "IB")
    assert config.SC_POLICY_ID == "sc-1.0" and config.SC_RV_TABLE == "intraday_rv"
    for name, value in FROZEN_SC_BAR.items():
        assert getattr(config, name) == value, name


def test_sc_build_constants_are_frozen():
    """The settlement split tolerance and the exploration sizing (R3, R5) move a grade, so they are pinned too."""
    assert sc.SPLIT_TOL == 0.05
    assert sc.EXPLORATION_SIZING.equity == 0.0
    assert (sc_structures.CAP_NEW_WEEK, sc_structures.CAP_OPEN, sc_structures.CAP_SECTOR, sc_structures.CAP_BUDGET) == \
        ("cap_new_week", "cap_open", "cap_sector", "cap_budget")


def test_sa_and_sb_sets_are_untouched_by_the_sc_addition():
    assert config.SA_PARAMS.__dict__ == FROZEN_SA
    assert config.SB_PARAMS.__dict__ == FROZEN_SB
    assert config.SB_SIZING.__dict__ == FROZEN_SB_SIZING
    for name, value in FROZEN_SB_BAR.items():
        assert getattr(config, name) == value, name
