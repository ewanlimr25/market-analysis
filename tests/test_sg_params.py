"""S-G is a backtest-only research pre-registration (DESIGN/91), not a champion: there is no
frozen-params test analogous to `test_frozen_params.py` / `test_sb_frozen_params.py`, and this
file must not become one. It only pins the derived DSR trial count (`70`'s 6 trials + S-G's 4,
DESIGN/91 §4) so a future edit to either count is visible here rather than silently changing the
deflation charge.
"""
from __future__ import annotations

import pytest

from engine import config

pytestmark = pytest.mark.unit


def test_sg_dsr_trial_count_is_sa_trials_plus_four():
    assert config.SG_DSR_TRIALS == config.DSR_TRIALS + config.SG_PRIMARY_TESTS
    assert config.SG_PRIMARY_TESTS == 4


def test_sg_params_defaults():
    assert config.SG_PARAMS.entry_offsets == (3, 5)
    assert config.SG_PARAMS.leg_size_min == 10
    assert config.SG_PARAMS.risk_frac == pytest.approx(0.010)
