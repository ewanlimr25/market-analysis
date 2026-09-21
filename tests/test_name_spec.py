"""The `sheet` and `disc` improvement-process entries (findings/stock-deep-dive DESIGN/70 §6).

Both books live in one file, `ledger/name/forward_ledger.parquet`, under three policy ids
(`sheet-1.0`, `disc-1.0` and the seeded `sdd-llm-1.0`); the read must never pool them. The sheet's
unit is not a date — DESIGN/70 §6 makes overlapping same-name rows within 21 sessions one unit, which
the R6 writer stamps into `unit_id` — so the adjudicator has to group on an identifier column as well
as on a date column.

Both reads are count-triggered (40 units for the sheet, 70 for the discretionary book, and no
earlier than 2027-03-01) and read NOT_DUE before their trigger, which is what this file pins.
"""
from __future__ import annotations

import os
import subprocess
import sys
from datetime import date

import pandas as pd
import pytest

from engine import config
from engine import policy as POL
from engine.improve import adjudicate as A
from engine.improve.spec import SPECS, spec

pytestmark = pytest.mark.unit

TODAY = date(2026, 9, 20)
REPO = config.REPO


def ledger_row(policy_id: str, role: str, ticker: str, E: str, unit_id: str, ror: float, r_share: float) -> dict:
    return {"ticker": ticker, "E": E, "variant": "sheet", "structure": "IB", "policy_id": policy_id,
            "role": role, "gate_verdict": "PASS", "pre": E, "post": E, "unit_id": unit_id,
            "ror": ror, "r_share": r_share}


def ledger(rows: list[dict]) -> pd.DataFrame:
    return pd.DataFrame(rows)


# ---- the two specs ---------------------------------------------------------------------------------

def test_the_sheet_spec_reads_return_on_risk_per_named_unit():
    sp = spec("sheet")
    assert sp.champion_id == config.NAME_POLICY_ID == "sheet-1.0"
    assert sp.metric == "ror" and sp.unit == "unit_id" and not sp.unit_is_date
    assert sp.entry_col == "E" and sp.lag == 0 and sp.gate_on == "PASS"
    assert sp.go_t == 2.0 and sp.units_per_week == 5.0 and sp.backtest_file == ""
    assert sp.read_n_required == config.NAME_PARAMS.sheet_read_n == 40 and sp.read_not_before is None


def test_the_disc_spec_reads_r_on_the_share_leg_per_decision_date():
    sp = spec("disc")
    assert sp.champion_id == config.DISC_POLICY_ID == "disc-1.0"
    assert sp.metric == "r_share" and sp.unit == "E" and sp.unit_is_date
    assert sp.entry_col == "E" and sp.lag == 0 and sp.gate_on == "PASS"
    assert sp.go_t == 2.0 and sp.units_per_week == 2.0
    assert sp.read_n_required == config.NAME_PARAMS.disc_read_n == 70
    assert sp.read_not_before == config.NAME_PARAMS.disc_read_not_before == date(2027, 3, 1)


def test_both_books_live_in_ledger_name():
    assert spec("sheet").ledger_dir() == spec("disc").ledger_dir() == config.LEDGER_NAME_DIR


def test_the_existing_specs_did_not_move():
    assert SPECS["sb"].champion_id == "sb-1.0" and SPECS["sa"].champion_id == "sa-1.0"
    assert SPECS["sb"].unit == "post" and SPECS["sa"].unit == "pre"
    assert SPECS["sb"].unit_is_date and SPECS["sa"].unit_is_date
    assert SPECS["sb"].read_n_required is None and SPECS["sa"].read_not_before is None


# ---- grouping ---------------------------------------------------------------------------------------

def test_the_sheet_groups_overlapping_same_name_rows_into_one_unit():
    rows = ledger([ledger_row("sheet-1.0", POL.ROLE_CHAMPION, "NVDA", "2026-09-18", "NVDA:2026-10-16", 0.4, 0.0),
                   ledger_row("sheet-1.0", POL.ROLE_CHAMPION, "NVDA", "2026-09-22", "NVDA:2026-10-16", 0.2, 0.0),
                   ledger_row("sheet-1.0", POL.ROLE_CHAMPION, "BL", "2026-09-18", "BL:2026-10-16", -1.0, 0.0)])
    units = A.unit_means(rows, spec("sheet"))
    assert list(units.index) == ["BL:2026-10-16", "NVDA:2026-10-16"]
    assert units["NVDA:2026-10-16"] == pytest.approx(0.3)


def test_the_discretionary_book_groups_by_decision_date():
    rows = ledger([ledger_row("disc-1.0", POL.ROLE_EXPLORATION, "NVDA", "2026-09-18", "NVDA:x", 0.0, 1.0),
                   ledger_row("disc-1.0", POL.ROLE_EXPLORATION, "BL", "2026-09-18", "BL:x", 0.0, -1.0),
                   ledger_row("disc-1.0", POL.ROLE_EXPLORATION, "BL", "2026-09-21", "BL:y", 0.0, 2.0)])
    units = A.unit_means(rows, spec("disc"))
    assert list(units.index) == [date(2026, 9, 18), date(2026, 9, 21)]
    assert units[date(2026, 9, 18)] == pytest.approx(0.0)


def test_the_three_policies_in_one_file_are_never_pooled():
    rows = ledger([ledger_row("sheet-1.0", POL.ROLE_CHAMPION, "NVDA", "2026-09-18", "NVDA:a", 0.4, 0.0),
                   ledger_row("disc-1.0", POL.ROLE_CHAMPION, "NVDA", "2026-09-18", "NVDA:a", 9.9, 9.9),
                   ledger_row(config.SEED_POLICY_ID, POL.ROLE_CHAMPION, "NVDA", "2026-09-18", "NVDA:a", 9.9, 9.9)])
    champions = A.champion_rows(rows, spec("sheet").champion_id)
    assert len(champions) == 1 and champions.iloc[0]["ror"] == 0.4
    assert len(A.champion_rows(rows, spec("disc").champion_id)) == 1
    assert len(A.rows_for(rows, config.SEED_POLICY_ID, POL.ROLE_CHAMPION)) == 1


# ---- the reads are NOT_DUE until their trigger fires --------------------------------------------------

@pytest.mark.parametrize("strategy", ["sheet", "disc"])
def test_an_empty_ledger_reads_not_due(strategy):
    sp = spec(strategy)
    stats = A.series_stats(A.unit_means(ledger([]), sp), sp.lag)
    assert stats["n_units"] == 0
    verdict, reason = A.read_due(stats["n_units"], sp, TODAY)
    assert verdict == A.NOT_DUE and str(sp.read_n_required) in reason


@pytest.mark.parametrize("strategy,n", [("sheet", 39), ("disc", 69)])
def test_a_short_ledger_reads_not_due(strategy, n):
    assert A.read_due(n, spec(strategy), TODAY)[0] == A.NOT_DUE
    assert A.read_due(n, spec(strategy), date(2028, 1, 1))[0] == A.NOT_DUE


def test_the_disc_read_is_not_due_before_its_registered_date_however_many_rows():
    assert A.read_due(500, spec("disc"), TODAY)[0] == A.NOT_DUE
    assert "2027-03-01" in A.read_due(500, spec("disc"), TODAY)[1]
    assert A.read_due(500, spec("disc"), date(2027, 3, 1)) is None
    assert A.read_due(500, spec("sheet"), TODAY) is None


def test_the_existing_strategies_have_no_count_trigger_and_keep_their_verdicts():
    assert A.read_due(0, SPECS["sb"], TODAY) is None and A.read_due(0, SPECS["sa"], TODAY) is None
    stats = {"n_units": 0, "mean": float("nan"), "t": float("nan")}
    assert A.champion_verdict(stats, 26, SPECS["sb"].go_t)[0] == A.INSUFFICIENT


# ---- the CLI wiring --------------------------------------------------------------------------------

@pytest.mark.parametrize("command,strategy", [("champion", "sheet"), ("champion", "disc"),
                                              ("gate", "sheet"), ("gate", "disc")])
def test_the_cli_runs_both_strategies_and_writes_nothing_before_the_trigger(tmp_path, command, strategy):
    args = [sys.executable, os.path.join(REPO, "scripts", "adjudicate.py"), "--ledger-dir", str(tmp_path),
            command, "--strategy", strategy, "--n-required", "40", "--as-of", TODAY.isoformat()]
    if command == "gate":
        args += ["--min-effect", "0.01"]
    done = subprocess.run(args, capture_output=True, text=True, cwd=REPO)
    assert done.returncode == 0, done.stderr
    assert A.NOT_DUE in done.stdout
    assert not os.path.exists(os.path.join(str(tmp_path), A.ADJUDICATIONS_DIR))
