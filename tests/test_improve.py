"""DESIGN/100 P3, P4: power arithmetic, challenger registration, and one-shot adjudication of a
challenger, a champion and a gate from synthetic ledger rows."""
from __future__ import annotations

import json
import os
from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from engine.improve import adjudicate as A
from engine.improve import power as PW
from engine.improve.spec import SPECS, spec

pytestmark = pytest.mark.unit


# ---- power ---------------------------------------------------------------------------------------

def test_n_required_matches_the_closed_form():
    assert PW.n_required(0.01, 0.05) == 155                      # ((1.645 + 0.842) * 5)^2 = 154.6
    assert PW.n_required(0.01, 0.05, inflation=2.0) == 310
    assert PW.n_required(0.02, 0.05) == 39
    with pytest.raises(ValueError):
        PW.n_required(0.0, 0.05)
    with pytest.raises(ValueError):
        PW.n_required(0.01, 0.0)


def test_autocorr_inflation_is_one_for_noise_and_above_one_for_a_persistent_series():
    rng = np.random.default_rng(0)
    assert PW.autocorr_inflation(rng.normal(size=400), 2) == pytest.approx(1.0, abs=0.25)
    persistent = np.repeat(rng.normal(size=50), 4)
    assert PW.autocorr_inflation(persistent, 2) > 1.5
    assert PW.autocorr_inflation([1.0, 2.0], 2) == 1.0


def test_plan_reports_its_inputs_and_a_projected_date():
    out = PW.plan(0.01, [0.05, -0.02, 0.03, 0.0, 0.04, -0.01, 0.02, 0.01, -0.03, 0.02, 0.0, 0.03], 0, date(2026, 12, 5), 1.0)
    assert out["sd"] == pytest.approx(PW.realised_sd([0.05, -0.02, 0.03, 0.0, 0.04, -0.01, 0.02, 0.01, -0.03, 0.02, 0.0, 0.03]))
    assert out["inflation"] == 1.0 and out["n_required"] == PW.n_required(0.01, out["sd"])
    assert date.fromisoformat(out["adjudicate_on"]) == date(2026, 12, 5) + timedelta(days=7 * out["n_required"])
    explicit = PW.plan(0.01, None, 2, date(2026, 12, 5), 2.0, sd=0.05)
    assert explicit["sd_source"] == "explicit" and explicit["n_required"] == 155


# ---- registration --------------------------------------------------------------------------------

def _reg(policy_id="sb-c1", strategy="sb", **kw):
    reg = {"policy_id": policy_id, "strategy": strategy, "champion": "sb-1.0", "idea": "VIX floor 15", "params_diff": {"vix_floor": 15.0},
           "registered": "2026-12-05", "n_required": 10, "unit": "post", "adjudicate_on": "2027-03-05", "test": "paired t",
           "min_effect": 0.01, "kill": "early stop", "script_sha256": A.script_sha256()}
    reg.update(kw)
    return reg


def test_register_writes_once_and_allows_one_open_challenger_per_strategy(tmp_path):
    root = str(tmp_path)
    path = A.register(root, _reg())
    assert json.load(open(path))["policy_id"] == "sb-c1" and A.open_challengers(root, "sb") == ["sb-c1"]
    with pytest.raises(FileExistsError):
        A.register(root, _reg())
    with pytest.raises(ValueError, match="open challenger"):
        A.register(root, _reg(policy_id="sb-c2"))
    A.register(root, _reg(policy_id="sa-c1", strategy="sa", champion="sa-1.0", unit="pre"))    # another strategy is fine
    with pytest.raises(ValueError, match="exactly one parameter"):
        A.validate_registration(_reg(params_diff={"a": 1, "b": 2}))
    with pytest.raises(ValueError, match="missing"):
        A.validate_registration({k: v for k, v in _reg().items() if k != "kill"})


# ---- adjudication --------------------------------------------------------------------------------

def _rows(policy_id, role, diffs, start=date(2026, 12, 11), structure="PS"):
    """One S-B row per weekly expiry; `diffs` is the ror per unit."""
    out = []
    for i, r in enumerate(diffs):
        entry = start + timedelta(days=7 * i)
        out.append({"ticker": "SPY", "E": entry, "entry": entry, "post": entry + timedelta(days=21), "structure": structure,
                    "policy_id": policy_id, "role": role, "gate_verdict": "ON", "ror": r})
    return pd.DataFrame(out)


def test_paired_units_match_on_ticker_entry_structure_and_ignore_rows_before_registration():
    sp = spec("sb")
    champ = _rows("sb-1.0", "champion", [0.01, 0.02, 0.03, 0.04])
    chall = _rows("sb-c1", "challenger", [0.02, 0.02, 0.05, 0.03])
    units = A.paired_units(champ, chall, sp, date(2026, 12, 5))
    assert units.tolist() == pytest.approx([0.01, 0.0, 0.02, -0.01])
    later = A.paired_units(champ, chall, sp, date(2026, 12, 18))          # entries 12-11 and 12-18 are not after 12-18
    assert len(later) == 2
    assert A.paired_units(champ, chall.assign(structure="IC"), sp, date(2026, 12, 5)).empty


def test_challenger_verdicts_cover_not_due_insufficient_promote_fail_and_early_stop():
    sp = spec("sb")
    reg = _reg(n_required=10)
    good = A.series_stats(pd.Series([0.02, 0.03, 0.025, 0.02, 0.03, 0.02, 0.025, 0.03, 0.02, 0.03]), sp.lag)
    assert A.challenger_verdict(good, reg, date(2027, 3, 5))[0] == A.PROMOTE
    flat = A.series_stats(pd.Series([0.01, -0.01, 0.005, -0.005, 0.01, -0.01, 0.005, -0.005, 0.0, 0.0]), sp.lag)
    assert A.challenger_verdict(flat, reg, date(2027, 3, 5))[0] == A.FAIL
    few = A.series_stats(pd.Series([0.02, 0.03, 0.02]), sp.lag)
    assert A.challenger_verdict(few, reg, date(2027, 1, 1))[0] == A.NOT_DUE
    assert A.challenger_verdict(few, reg, date(2027, 3, 5))[0] == A.INSUFFICIENT
    bad = A.series_stats(pd.Series([-0.03, -0.02, -0.04, -0.03, -0.02]), sp.lag)
    verdict, reason = A.challenger_verdict(bad, reg, date(2027, 1, 1))
    assert verdict == A.FAIL and "early stop" in reason


def test_champion_and_gate_verdicts(tmp_path):
    sp = spec("sb")
    champ = _rows("sb-1.0", "champion", [0.04, 0.05, 0.03, 0.06, 0.04, 0.05, 0.03, 0.05, 0.04, 0.06])
    stats = A.series_stats(A.unit_means(champ, sp), sp.lag)
    assert A.champion_verdict(stats, 10, sp.go_t)[0] == A.PASS and A.champion_verdict(stats, 26, sp.go_t)[0] == A.INSUFFICIENT
    on = _rows("sb-1.0", "exploration", [0.05, 0.04, 0.06, 0.05, 0.04, 0.05])
    off = _rows("sb-1.0", "exploration", [-0.02, -0.01, -0.03, 0.0, -0.02, -0.01], start=date(2027, 3, 5)).assign(gate_verdict="OFF:G2")
    gs = A.gate_stats(pd.concat([on, off]), sp)
    assert gs["n_on"] == 6 and gs["n_off"] == 6 and gs["diff"] > 0.05
    assert A.gate_verdict(gs, 0.01, 6)[0] == "KEEP" and A.gate_verdict(gs, 0.01, 20)[0] == A.INSUFFICIENT
    same = A.gate_stats(pd.concat([on, on.assign(gate_verdict="OFF:G2", post=on.post + pd.Timedelta(days=1))]), sp)
    assert A.gate_verdict(same, 0.01, 6)[0] == "CANDIDATE_FOR_REMOVAL"
    path = A.write_adjudication(str(tmp_path), "gate-sb-2026-12-01", {"as_of": "2026-12-01", "verdict": "KEEP", "reason": "test"})
    assert os.path.exists(path) and "KEEP" in open(os.path.join(tmp_path, "adjudications", "LOG.md")).read()
    with pytest.raises(FileExistsError):
        A.write_adjudication(str(tmp_path), "gate-sb-2026-12-01", {})


def test_script_hash_changes_when_the_script_changes(tmp_path):
    a = tmp_path / "a.py"; a.write_text("x = 1\n")
    h1 = A.script_sha256((str(a),))
    a.write_text("x = 2\n")
    assert A.script_sha256((str(a),)) != h1


def test_specs_point_at_the_pinned_champions():
    assert SPECS["sb"].champion_id == "sb-1.0" and SPECS["sa"].champion_id == "sa-1.0"
    assert SPECS["sb"].metric == "ror" and SPECS["sa"].metric == "net_pct"
    with pytest.raises(ValueError):
        spec("sc")
