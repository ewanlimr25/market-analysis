"""DESIGN/100 P1 (findings/market-analysis): every ledger row carries `policy_id`, `role` and
`gate_verdict`; the writer refuses rows without them; keys never pool across policies or roles;
the champion `policy_id` is pinned beside the frozen parameters."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine import config
from engine import ledger as L
from engine import policy as POL
from engine.strategies import sa, sb
from engine.config import SA_PARAMS, SB_PARAMS, SB_SIZING, SIZING
from test_ledger_daily import _signal, PRE, POST
from test_sa_strategy import _event, _pre_rows, _resolver
from test_sb_strategy import ENTRY, _on, _rows, X
from engine import calendar as cal

pytestmark = pytest.mark.unit


def test_champion_policy_ids_are_pinned_beside_the_frozen_parameters():
    assert config.SA_POLICY_ID == "sa-1.0" and config.SB_POLICY_ID == "sb-1.0"
    assert POL.ROLES == ("champion", "challenger", "exploration")
    assert POL.POLICY_COLUMNS == ("policy_id", "role", "gate_verdict")


def test_ledger_refuses_rows_without_the_policy_columns(tmp_path):
    bare = pd.DataFrame([{k: v for k, v in _signal().items() if k not in POL.POLICY_COLUMNS}])
    with pytest.raises(ValueError, match="policy_id"):
        L.emit(str(tmp_path), bare, PRE)
    with pytest.raises(ValueError, match="role"):
        L.grade(str(tmp_path), bare.assign(policy_id="sa-1.0", gate_verdict="PASS"), POST)
    assert L.read_signals(str(tmp_path)).empty


def test_ledger_refuses_an_unknown_role(tmp_path):
    with pytest.raises(ValueError, match="role"):
        L.emit(str(tmp_path), pd.DataFrame([_signal(role="shadow")]), PRE)


def test_same_trade_under_two_roles_or_policies_are_distinct_keys(tmp_path):
    rows = pd.DataFrame([_signal(), _signal(role="exploration", contracts=1), _signal(policy_id="sa-c1", role="challenger")])
    assert L.emit(str(tmp_path), rows, PRE) == (3, 0)
    assert L.emit(str(tmp_path), rows, PRE) == (0, 3)
    sig = L.read_signals(str(tmp_path))
    assert sorted(zip(sig.policy_id, sig.role)) == [("sa-1.0", "champion"), ("sa-1.0", "exploration"), ("sa-c1", "challenger")]
    pend = L.pending(str(tmp_path), POST)
    assert len(pend) == 3
    graded = pend[pend.role == "exploration"].assign(net_usd=1.0, net_pct=0.001)
    assert L.grade(str(tmp_path), graded, POST) == (1, 0)
    assert set(L.pending(str(tmp_path), POST).role) == {"champion", "challenger"}


def test_grouping_helper_never_pools_policies():
    led = pd.DataFrame([_signal(net_pct=0.01), _signal(net_pct=-0.02, role="exploration"), _signal(net_pct=0.05, policy_id="sa-c1", role="challenger")])
    groups = {k: len(g) for k, g in POL.by_policy(led)}
    assert groups == {("sa-1.0", "champion"): 1, ("sa-1.0", "exploration"): 1, ("sa-c1", "challenger"): 1}


def test_sa_builder_stamps_champion_rows():
    res = sa.evaluate_event(_event(), _pre_rows(), _resolver(), SA_PARAMS, SIZING, with_exit=False)
    assert res.trades, "fixture should produce trades"
    for row in res.trades:
        assert (row["policy_id"], row["role"], row["gate_verdict"]) == ("sa-1.0", "champion", POL.SA_GATE_PASS)


def test_sb_builder_stamps_champion_rows_with_the_gate_verdict():
    res = sb.entry_candidates("SPY", ENTRY, _rows(), _on(), X, SB_PARAMS, SB_SIZING, cal.is_trading_day)
    assert [t["structure"] for t in res.trades] == ["PS", "IC"]
    for row in res.trades:
        assert (row["policy_id"], row["role"], row["gate_verdict"]) == ("sb-1.0", "champion", "ON")
        assert row["gate_reason"] == "ON"
