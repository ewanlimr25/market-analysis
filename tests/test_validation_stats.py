"""P5 statistics: clustered t (Liang-Zeger), Benjamini-Hochberg, Sharpe deflation, PBO."""
from __future__ import annotations

import sys
import os

import numpy as np
import pandas as pd
import pytest

from engine.validation import stats as S

pytestmark = pytest.mark.unit

FINDINGS_VOL = os.path.expanduser("~/Development/findings/market-analysis/artifacts/vol")


def test_cluster_t_matches_the_research_implementation():
    sys.path.insert(0, FINDINGS_VOL)
    from vstats import cluster_t as ref  # the implementation behind RESEARCH/40
    rng = np.random.default_rng(7)
    x = rng.standard_t(4, size=800) * 0.03 + 0.005
    clusters = rng.integers(0, 60, size=800)
    a, b = S.cluster_t(x, clusters), ref(x, clusters)
    assert a["n"] == b["n"] and a["G"] == b["G"]
    assert a["mean"] == pytest.approx(b["mean"]) and a["se"] == pytest.approx(b["se"])
    assert a["t"] == pytest.approx(b["t"]) and a["p"] == pytest.approx(b["p"], abs=1e-6)


def test_cluster_t_with_one_observation_per_cluster_equals_plain_t():
    x = np.array([1.0, 2.0, 3.0, 4.0, 10.0])
    r = S.cluster_t(x, np.arange(5))
    plain_se = x.std(ddof=1) / np.sqrt(5)
    assert r["se"] == pytest.approx(plain_se) and r["G"] == 5


def test_cluster_t_handles_nan_and_empty():
    r = S.cluster_t(np.array([np.nan, np.nan]), np.array([1, 2]))
    assert r["n"] == 0 and np.isnan(r["t"])
    r = S.cluster_t(np.array([0.1, np.nan, 0.3]), np.array(["a", "a", "b"]))
    assert r["n"] == 2 and r["G"] == 2


def test_bh_known_example():
    # Benjamini & Hochberg (1995) worked example: 15 p-values, FDR 0.05 -> the first four reject
    p = [0.0001, 0.0004, 0.0019, 0.0095, 0.0201, 0.0278, 0.0298, 0.0344, 0.0459, 0.3240,
         0.4262, 0.5719, 0.6528, 0.7590, 1.000]
    rej = S.bh_reject(p, fdr=0.05)
    assert rej == [True] * 4 + [False] * 11
    # order-independent: shuffled input gives the same per-hypothesis decisions
    assert S.bh_reject(p[::-1], fdr=0.05) == ([False] * 11 + [True] * 4)
    assert S.bh_reject([0.5, 0.9], 0.10) == [False, False]
    assert S.bh_reject([], 0.10) == []


def test_sharpe_and_expected_max_sharpe():
    x = np.array([0.01, -0.005, 0.02, 0.0, 0.015])
    assert S.sharpe(x) == pytest.approx(x.mean() / x.std(ddof=1))
    # SR* grows with the trial count and with the trial variance; zero variance -> zero benchmark
    assert S.expected_max_sharpe(n_trials=6, var_sharpe=0.01) > S.expected_max_sharpe(n_trials=2, var_sharpe=0.01) > 0
    assert S.expected_max_sharpe(n_trials=6, var_sharpe=0.0) == 0.0
    assert S.expected_max_sharpe(n_trials=1, var_sharpe=0.01) == 0.0


def test_deflated_sharpe_report_fields_and_direction():
    rng = np.random.default_rng(1)
    good = rng.normal(0.02, 0.05, size=400)
    rep = S.deflated_sharpe(good, n_trials=6, var_sharpe=0.0025)
    for k in ("sr", "sr_star", "deflated_sr", "dsr_prob", "skew", "kurt", "n"):
        assert k in rep
    assert rep["deflated_sr"] == pytest.approx(rep["sr"] - rep["sr_star"])
    assert rep["dsr_prob"] > 0.5 and rep["deflated_sr"] > 0
    bad = rng.normal(0.0, 0.05, size=400)
    assert S.deflated_sharpe(bad, n_trials=6, var_sharpe=0.0025)["dsr_prob"] < 0.9


def test_pbo_is_high_for_noise_and_low_for_a_dominant_config():
    rng = np.random.default_rng(3)
    n_obs, n_cfg = 640, 4
    noise = pd.DataFrame(rng.normal(0, 1, size=(n_obs, n_cfg)))
    blocks = np.repeat(np.arange(16), n_obs // 16)
    pbo_noise = S.pbo(noise, blocks)
    assert 0.2 <= pbo_noise["pbo"] <= 0.8
    strong = noise.copy()
    strong[0] = strong[0] + 0.8
    assert S.pbo(strong, blocks)["pbo"] < 0.15
    assert S.pbo(strong, blocks)["n_combinations"] == 12870  # C(16, 8)


def test_pbo_requires_even_block_count_and_at_least_two_configs():
    with pytest.raises(ValueError):
        S.pbo(pd.DataFrame(np.zeros((10, 1))), np.zeros(10, dtype=int))
    with pytest.raises(ValueError):
        S.pbo(pd.DataFrame(np.zeros((9, 2))), np.repeat(np.arange(3), 3))


def test_deflated_sharpe_probability_agrees_with_purgedcv():
    from purgedcv import deflated_sharpe_ratio
    rng = np.random.default_rng(11)
    x = rng.normal(0.01, 0.05, size=300)
    ours = S.deflated_sharpe(x, n_trials=6, var_sharpe=0.002)["dsr_prob"]
    assert ours == pytest.approx(deflated_sharpe_ratio(x, 6, 0.002), abs=2e-2)
