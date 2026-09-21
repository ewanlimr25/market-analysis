"""The `sdd-llm-1.0` seed (findings/stock-deep-dive DECISIONS D8, DESIGN/70 §10 R5).

Two fixture sets under `tests/fixtures/name/seed/`: five small synthetic CSVs that exercise every
branch (a directional decision, a RANGE decision with no walk, a no-fill, two structures of the same
family on one decision, an open structure), and `real/`, a copy of the five graded CSVs the corpus
actually ships, so the acceptance criterion — 62 decisions, 125 structures and 9 plans load as
graded history — is a unit test with no dependency on `~/Development/findings` being present.
"""
from __future__ import annotations

import math
import os

import pandas as pd
import pytest

from engine import ledger as L
from engine import policy as POL
from engine.config import SEED_POLICY_ID
from engine.name import seed as S

pytestmark = pytest.mark.unit

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures", "name", "seed")
REAL = os.path.join(FIXTURES, "real")
BIASES = {"LONG", "SHORT", "NEUTRAL", "RANGE"}


def row_of(rows: pd.DataFrame, ticker: str, structure: str, variant: str = S.DECISION) -> pd.Series:
    hit = rows[(rows["ticker"] == ticker) & (rows["structure"] == structure) & (rows["variant"] == variant)]
    assert len(hit) == 1, f"expected one {variant}/{structure} row for {ticker}, got {len(hit)}"
    return hit.iloc[0]


def is_null(value) -> bool:
    return value is None or (isinstance(value, float) and math.isnan(value))


# ---- the family classifier is a port, so it is checked against the source's own labels ------------

def test_family_of_reproduces_the_labels_the_old_book_recorded():
    cd = pd.read_csv(os.path.join(REAL, "CD_structure_rows.csv"))
    mismatched = [(t, f, S.family_of(t)) for t, f in zip(cd["type"], cd["family"]) if S.family_of(t) != f]
    assert mismatched == []


def test_family_of_classifies_the_plans_option_legs():
    kinds = [S.family_of(t) for t in pd.read_csv(os.path.join(REAL, "G_plans_options.csv"))["type"]]
    assert kinds.count("debit_vertical") == 10 and kinds.count("credit_vertical") == 6
    assert kinds.count("IC") == 1 and kinds.count("long_strangle") == 1 and "unknown" not in kinds


# ---- the synthetic corpus: one assertion per branch ----------------------------------------------

@pytest.fixture(scope="module")
def synthetic() -> pd.DataFrame:
    return S.build_rows(FIXTURES)


def test_the_synthetic_corpus_has_one_row_per_source_row(synthetic):
    assert S.counts(synthetic) == {"decisions": 5, "structures": 5, "plans": 2, "plan_options": 4, "total": 16}


def test_every_row_carries_the_seed_policy_and_the_narrate_context_tag(synthetic):
    POL.require_policy_columns(synthetic)
    assert set(synthetic["policy_id"]) == {SEED_POLICY_ID} and set(synthetic["role"]) == {POL.ROLE_CHAMPION}
    assert set(synthetic["context_read"]) == {"narrate"} and set(synthetic["n"]) == {1}
    assert set(synthetic["gate_verdict"]) <= BIASES
    assert synthetic["source"].str.startswith("findings/stock-deep-dive artifacts/outcomes results/").all()


def test_a_directional_decision_carries_the_walk_and_its_plus_one_r_target(synthetic):
    r = row_of(synthetic, "AAA", S.SHARES)
    assert r["direction"] == "long" and r["entry"] == 100.0 and r["stop"] == 90.0 and r["target"] == 110.0
    assert r["r_share"] == 1.0 and r["outcome"] == "WIN" and r["gate_verdict"] == "LONG"
    assert r["pre"] == "2026-06-01" and r["post"] == "2026-06-08"
    assert r["conviction"] == 0.65 and r["conf"] == 70.0


def test_a_range_decision_has_no_direction_and_no_share_outcome(synthetic):
    r = row_of(synthetic, "CCC", S.SHARES)
    assert is_null(r["direction"]) and is_null(r["r_share"]) and is_null(r["target"]) and is_null(r["outcome"])
    assert r["post"] == S.SEED_REVIEW.isoformat(), "a row that never resolved is stamped at the review date"


def test_a_no_fill_decision_is_seeded_with_a_null_r(synthetic):
    r = row_of(synthetic, "EEE", S.SHARES)
    assert r["outcome"] == "NO_FILL" and is_null(r["r_share"]) and r["post"] == S.SEED_REVIEW.isoformat()


def test_two_structures_of_one_family_on_one_decision_keep_distinct_keys(synthetic):
    first, second = row_of(synthetic, "AAA", "debit_vertical#0"), row_of(synthetic, "AAA", "debit_vertical#1")
    assert first["family"] == second["family"] == "debit_vertical"
    assert first["ror"] == 4.0 and second["ror"] == -1.0
    assert first["outcome"] == "WIN" and second["outcome"] == "LOSS"
    assert first["post"] == "2026-06-19" and is_null(first["direction"])


def test_an_open_structure_is_seeded_with_a_null_return_on_risk(synthetic):
    r = row_of(synthetic, "DDD", "IC#0")
    assert r["outcome"] == "OPEN" and is_null(r["ror"]) and r["post"] == "2026-10-16"


def test_only_the_limit_fill_rows_of_the_review_date_become_plan_rows(synthetic):
    plans = synthetic[synthetic["variant"] == S.PLAN]
    shares = plans[plans["structure"] == S.SHARES]
    assert sorted(shares["ticker"]) == ["AAA", "EEE"]
    assert row_of(synthetic, "AAA", S.SHARES, S.PLAN)["r_share"] == 2.0
    eee = row_of(synthetic, "EEE", S.SHARES, S.PLAN)
    assert eee["outcome"] == "NO_FILL" and is_null(eee["r_share"]) and eee["post"] == S.SEED_REVIEW.isoformat()


def test_a_plan_option_leg_borrows_the_plans_bias_and_confidence(synthetic):
    r = row_of(synthetic, "EEE", "debit_vertical#1", S.PLAN)
    assert r["gate_verdict"] == "LONG" and r["conf"] == 55.0 and r["ror"] == -1.0 and r["outcome"] == "LOSS"
    assert is_null(row_of(synthetic, "EEE", "IC#0", S.PLAN)["ror"])


# ---- the real corpus (DESIGN/70 §10 R5: the 62 old decisions load as graded history) --------------

@pytest.fixture(scope="module")
def corpus() -> pd.DataFrame:
    return S.build_rows(REAL)


def test_the_corpus_loads_62_decisions_125_structures_and_9_plans(corpus):
    assert S.counts(corpus) == {"decisions": 62, "structures": 125, "plans": 9, "plan_options": 18, "total": 214}


def test_the_corpus_keys_are_unique_so_the_write_once_ledger_drops_nothing(corpus):
    assert not corpus.duplicated(subset=L.KEY).any()
    assert set(corpus["variant"]) == {S.DECISION, S.PLAN} and set(corpus["gate_verdict"]) == BIASES


def test_the_resolved_share_of_each_book_is_what_the_outcomes_run_measured(corpus):
    decisions = corpus[(corpus["variant"] == S.DECISION) & (corpus["structure"] == S.SHARES)]
    assert decisions["outcome"].value_counts().to_dict() == {"LOSS": 9, "WIN": 9, "NO_FILL": 4}   # RESEARCH/15 §B
    assert decisions["r_share"].notna().sum() == 18 and decisions["outcome"].isna().sum() == 40
    structures = corpus[(corpus["variant"] == S.DECISION) & (corpus["structure"] != S.SHARES)]
    assert structures["outcome"].value_counts().to_dict() == {"WIN": 60, "LOSS": 59, "OPEN": 6}
    assert structures["ror"].notna().sum() == 119 and structures["r_share"].isna().all()
    plans = corpus[(corpus["variant"] == S.PLAN) & (corpus["structure"] == S.SHARES)]
    assert plans["outcome"].value_counts().to_dict() == {"LOSS": 5, "WIN": 2, "NO_FILL": 2}       # RESEARCH/15 §G
    assert corpus[(corpus["variant"] == S.PLAN) & (corpus["structure"] != S.SHARES)]["ror"].notna().sum() == 16


def test_the_two_plans_named_in_the_spec_seed_as_graded(corpus):
    elf = row_of(corpus, "ELF", S.SHARES, S.PLAN)
    assert elf["outcome"] == "NO_FILL" and is_null(elf["r_share"]) and elf["entry"] == 70.0
    path = corpus[(corpus["ticker"] == "PATH") & (corpus["variant"] == S.PLAN) & (corpus["structure"] == S.SHARES)]
    assert sorted(path["E"]) == ["2026-06-21", "2026-07-13"] and set(path["outcome"]) == {"LOSS"}
    assert path[path["E"] == "2026-06-21"].iloc[0]["post"] == "2026-06-29"


# ---- writing it once ------------------------------------------------------------------------------

def test_the_seed_writes_both_ledger_files_and_refuses_to_run_twice(tmp_path):
    out = str(tmp_path / "name")
    rows = S.build_rows(REAL)
    first = S.write(rows, out)
    assert first == {"emitted": 214, "emit_skipped": 0, "graded": 214, "graded_skipped": 0}
    second = S.write(rows, out)
    assert second == {"emitted": 0, "emit_skipped": 214, "graded": 0, "graded_skipped": 214}
    ledger = L.read_ledger(out)
    assert len(ledger) == 214 and set(ledger["graded_at"]) == {S.SEED_REVIEW.isoformat()}
    assert len(L.read_signals(out)) == 214
    assert L.pending(out, S.SEED_REVIEW).empty, "a graded row is never pending"


def test_the_seed_never_pools_with_another_policy(tmp_path):
    out = str(tmp_path / "name")
    S.write(S.build_rows(REAL), out)
    from engine.improve import adjudicate as A
    ledger = L.read_ledger(out)
    assert len(A.champion_rows(ledger, SEED_POLICY_ID)) == 214
    assert len(A.champion_rows(ledger, "sheet-1.0")) == 0 and len(A.champion_rows(ledger, "disc-1.0")) == 0


def test_the_cli_dry_run_writes_nothing(tmp_path, capsys):
    out = str(tmp_path / "name")
    assert S.main(["--ledger-dir", out, "--results-dir", REAL, "--dry-run"]) == 0
    assert "decisions 62" in capsys.readouterr().out
    assert not os.path.exists(out)


def test_the_cli_writes_then_reports_the_skipped_count(tmp_path, capsys):
    out = str(tmp_path / "name")
    assert S.main(["--ledger-dir", out, "--results-dir", REAL]) == 0
    assert "graded 214" in capsys.readouterr().out
    assert S.main(["--ledger-dir", out, "--results-dir", REAL]) == 0
    printed = capsys.readouterr().out
    assert "skipped 214" in printed and "already run" in printed


def test_a_missing_results_directory_is_named_not_swallowed(tmp_path):
    with pytest.raises(FileNotFoundError, match="E_calibration_rows.csv"):
        S.build_rows(str(tmp_path))
