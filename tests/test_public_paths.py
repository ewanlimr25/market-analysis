"""findings D32: nothing the engine commits under `analyses/` or `data/` names the machine it ran on.
`config.public_path` turns a path under the repo into a repo-relative one; the committed outputs are checked."""
from __future__ import annotations

import glob
import os

import pandas as pd
import pytest

from engine import backtest_sc as B
from engine import config

pytestmark = pytest.mark.unit

COMMITTED_OUTPUTS = ("analyses/ticker/*/*/ticker.json", "analyses/daily/*/*.json", "analyses/daily/*/*.md", "data/backtest/*.md")


def test_public_path_is_repo_relative_inside_the_repo_and_unchanged_outside():
    inside = os.path.join(config.REPO, "analyses", "ticker", "AAPL", "2026-09-18", "inputs")
    assert config.public_path(inside) == "analyses/ticker/AAPL/2026-09-18/inputs"
    assert config.public_path("/elsewhere/analyses/x") == "/elsewhere/analyses/x"
    assert config.public_path("analyses/x") == "analyses/x"


def test_the_sb_open_note_names_the_marked_file_relative_to_the_repo(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "REPO", str(tmp_path))
    out = tmp_path / "data" / "backtest"
    out.mkdir(parents=True)
    pd.DataFrame({"entry": ["2026-09-11"], "expiry": ["2026-10-02"]}).to_parquet(out / B.SB_MARKED_FILE)
    _, note = B.sb_open_fn(str(out))
    assert note == f"data/backtest/{B.SB_MARKED_FILE} (1 positions)"


@pytest.mark.parametrize("pattern", COMMITTED_OUTPUTS)
def test_committed_outputs_carry_no_machine_local_path(pattern):
    paths = glob.glob(os.path.join(config.REPO, pattern))
    assert paths, f"nothing matches {pattern}"
    leaking = [p for p in paths if "/Users/" in open(p, encoding="utf-8").read()]
    assert leaking == [], [os.path.relpath(p, config.REPO) for p in leaking]
