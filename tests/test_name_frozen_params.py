"""The ticker-sheet parameters were frozen on 2026-09-20 (findings/stock-deep-dive DESIGN/70 §2 to §6,
DECISIONS D14). This test pins every value.

If it fails, a pre-registered threshold was edited before its read. Do not update the expected
values here; register the change in DESIGN/70 §11 and wait for the read after the one it is
proposed at.
"""
from __future__ import annotations

from datetime import date

import pytest

from engine import config

pytestmark = pytest.mark.unit

FROZEN_NAME = {
    # §2 liquidity floor
    "price_min": 10.0, "contracts_min": 300, "hot_chain_min_contracts": 10, "hot_chain_min_days": 15,
    "hot_chain_window": 21, "adv_min": 50e6, "atm_band": 0.025, "atm_tier_max": 2, "atm_spread_max": 0.08,
    "atm_leg_size_min": 5,
    # §3 premium
    "iv_pct_window": 126, "iv_pct_min_sessions": 63, "rv_window": 21, "rv_min_sessions": 15,
    "rich_spread_rv5": 10.0, "rich_spread_c2c": 2.0, "cheap_spread_rv5": 2.0, "cheap_spread_c2c": -5.0,
    "slope_min_dte_cal": 7, "earnings_history_n": 8, "sa_window_days": 30,
    # §4 exclusions
    "x1_unknown_earnings_days": 45, "x2_borrow_decile": 0.9, "x2_available_min": 100_000, "x4_atr_mult": 2.0,
    "x5_short_float_min": 0.25, "x6_wing_sigma": 2.0, "x6_condor_sigma": 1.0,
    # §5 structures and cost model
    "dir_target_dte_cal": 28, "cost_spread_mult": 0.584, "commission_per_contract": 0.65, "share_cost_bp": 5.0,
    "sigma_c2c_window": 63, "risk_frac": 0.005, "undefined_risk_frac": 0.010, "stress_sigma": 3.0,
    "disc_target_mult": 2.0,
    # §6 reads and kill rules
    "sheet_read_n": 40, "disc_read_n": 70, "disc_read_not_before": date(2027, 3, 1), "context_stratum_min": 35,
    "sheet_retire_min_sessions": 20,
}
FROZEN_SIZING = {"equity": 100_000.0, "allow_undefined": False}


def test_name_params_are_frozen():
    assert config.NAME_PARAMS.__dict__ == FROZEN_NAME
    assert config.NAME_FROZEN_ON == date(2026, 9, 20)


def test_name_sizing_defaults_are_frozen():
    assert config.NAME_SIZING.__dict__ == FROZEN_SIZING


def test_policy_ids_schema_and_context_values_are_frozen():
    assert config.NAME_POLICY_ID == "sheet-1.0"
    assert config.DISC_POLICY_ID == "disc-1.0"
    assert config.SEED_POLICY_ID == "sdd-llm-1.0"
    assert config.NAME_SCHEMA_VERSION == "n1.0"
    assert config.CONTEXT_READ_VALUES == ("none", "sheet_only", "narrate")
    assert config.NAME_ISSUE_TYPES == ("Common Stock", "ADR", "ETF")


def test_the_sheet_imports_sc_and_sa_parameters_unchanged():
    """The sheet reports S-C / S-A filter distance; it never carries its own copy of their thresholds."""
    assert config.SC_PARAMS.mcap_max == 20e9 and config.SC_PARAMS.iv30d_min == 0.30
    assert config.NAME_PARAMS.price_min == config.SC_PARAMS.price_min
    assert config.NAME_PARAMS.adv_min == config.SC_PARAMS.adv_min
    assert config.NAME_PARAMS.atm_band == config.SC_PARAMS.atm_band
    assert config.NAME_PARAMS.atm_spread_max == config.SC_PARAMS.spread_max
