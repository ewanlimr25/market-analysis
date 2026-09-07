"""engine.research.intraday_flow_store: G2's own partition layout under data/backtest/g2_*, kept
separate from engine.mart.store because that module's table_dir points at the shared data/mart
symlink this worktree must never write into.
"""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine import config
from engine.research import intraday_flow_store as st

pytestmark = pytest.mark.unit

D1, D2 = date(2026, 7, 29), date(2026, 7, 30)


@pytest.fixture
def isolated_data_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "DATA", str(tmp_path / "data"))
    monkeypatch.setattr(st, "BACKTEST_DIR", str(tmp_path / "data" / "backtest"))
    return tmp_path


def test_write_then_read_partition_roundtrips(isolated_data_dir):
    df = pd.DataFrame({"a": [1, 2, 3]})
    path = st.write_partition(df, st.EVENTS_TABLE, D1)
    assert path == st.partition_path(st.EVENTS_TABLE, D1)
    assert st.has_partition(st.EVENTS_TABLE, D1)
    pd.testing.assert_frame_equal(st.read_partition(st.EVENTS_TABLE, D1), df)


def test_write_partition_does_not_clobber_other_dates_or_tables(isolated_data_dir):
    st.write_partition(pd.DataFrame({"a": [1]}), st.EVENTS_TABLE, D1)
    st.write_partition(pd.DataFrame({"a": [2]}), st.EVENTS_TABLE, D2)
    st.write_partition(pd.DataFrame({"b": [9]}), st.PATH_TABLE, D1)
    assert st.available_dates(st.EVENTS_TABLE) == [D1, D2]
    assert st.available_dates(st.PATH_TABLE) == [D1]
    assert st.read_partition(st.EVENTS_TABLE, D1)["a"].tolist() == [1]


def test_has_partition_false_when_absent(isolated_data_dir):
    assert not st.has_partition(st.EVENTS_TABLE, D1)
    assert st.available_dates(st.EVENTS_TABLE) == []


def test_read_table_concatenates_available_partitions_and_is_empty_when_none(isolated_data_dir):
    assert st.read_table(st.EVENTS_TABLE).empty
    st.write_partition(pd.DataFrame({"a": [1]}), st.EVENTS_TABLE, D1)
    st.write_partition(pd.DataFrame({"a": [2, 3]}), st.EVENTS_TABLE, D2)
    out = st.read_table(st.EVENTS_TABLE)
    assert sorted(out["a"].tolist()) == [1, 2, 3]
    only_d1 = st.read_table(st.EVENTS_TABLE, dates=[D1])
    assert only_d1["a"].tolist() == [1]
