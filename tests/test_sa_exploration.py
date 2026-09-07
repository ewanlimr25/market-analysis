"""DESIGN/100 §6, §9: the S-A exploration book. Every event the engine can price (a markable ATM pair,
F5) gets both structures at one contract under `role = exploration`, with the first failing champion
filter (or PASS) as `gate_verdict`, so the filter chain is graded at the season read."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine import daily as D
from engine import policy as POL
from engine import report as R
from engine import schema as SCH
from engine.config import SA_PARAMS, SIZING
from engine.strategies import sa
from test_sa_strategy import _event, _pre_rows, _resolver, PRE, POST

pytestmark = pytest.mark.unit


def test_exploration_prices_a_gate_failing_event_at_one_contract():
    ev = _event(marketcap=90e9)                                       # F3 fails: outside 2B..50B
    champion = sa.evaluate_event(ev, _pre_rows(), _resolver(), SA_PARAMS, SIZING, with_exit=False)
    assert champion.trades == [] and {s["first_fail"] for s in champion.suppressed} == {"F3"}
    res = sa.exploration_event(ev, _pre_rows(), _resolver(), SA_PARAMS, with_exit=False)
    assert [t["structure"] for t in res.trades] == ["SS", "IC"] and res.dropped == []
    for t in res.trades:
        assert (t["policy_id"], t["role"], t["gate_verdict"], t["variant"]) == ("sa-1.0", "exploration", "F3", "A1")
        assert t["contracts"] == 1 and t["cap_pass"] is True and t["cap_rank"] == 0
        assert t["risk_usd"] == pytest.approx(t["stress_loss_usd" if t["structure"] == "SS" else "max_loss_usd"])


def test_exploration_marks_a_passing_event_pass_and_ignores_caps():
    res = sa.exploration_event(_event(), _pre_rows(), _resolver(), SA_PARAMS, with_exit=False)
    assert [t["gate_verdict"] for t in res.trades] == [POL.SA_GATE_PASS, POL.SA_GATE_PASS]
    assert all(t["contracts"] == 1 for t in res.trades)


def test_exploration_needs_a_markable_atm_pair():
    res = sa.exploration_event(_event(), _pre_rows().iloc[0:0], _resolver(), SA_PARAMS, with_exit=False)
    assert res.trades == [] and res.dropped[0]["reason"] == "no_atm_pair"


def test_exploration_run_covers_every_event_in_the_load_band():
    events = pd.DataFrame([_event(), _event(ticker="ABC", marketcap=90e9), _event(ticker="TINY", marketcap=5e8)])
    rows = pd.concat([_pre_rows(), _pre_rows().assign(underlying_symbol="ABC")])
    rows["option_chain_id"] = rows["underlying_symbol"] + rows["option_chain_id"].str[3:]
    out = sa.exploration_run(events, rows, _resolver(), SA_PARAMS, with_exit=False)
    assert sorted(set(out.trades.ticker)) == ["ABC", "XYZ"] and len(out.trades) == 4
    assert out.dropped.ticker.tolist() == ["TINY"] and out.dropped.reason.tolist() == ["no_atm_pair"]
    assert set(out.trades.gate_verdict) == {"PASS", "F3"}


def test_season_running_never_pools_roles():
    led = pd.DataFrame([{"variant": "A1", "structure": "SS", "season": "S3", "pre": PRE, "net_pct": 0.02, "net_usd": 200.0,
                         "policy_id": "sa-1.0", "role": "champion"},
                        {"variant": "A1", "structure": "SS", "season": "S3", "pre": PRE, "net_pct": -0.05, "net_usd": -50.0,
                         "policy_id": "sa-1.0", "role": "exploration"}])
    run = D.season_running(led, "S3")
    assert {(r["role"], r["n"]) for r in run} == {("champion", 1), ("exploration", 1)}
    assert all(r["policy_id"] == "sa-1.0" for r in run)


def test_assembled_document_with_exploration_validates_and_renders():
    ex = sa.exploration_run(pd.DataFrame([_event(marketcap=90e9)]), _pre_rows(), _resolver(), SA_PARAMS, with_exit=False)
    run = sa.RunResult(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), ex.trades, ex.dropped)
    doc = D.assemble(PRE, {"ok": True, "warnings": []}, {"daily_contract_rows": 1, "earnings_events_rows": 1}, run,
                     pd.DataFrame(), pd.DataFrame(), [], {"emitted": 0, "skipped": 0, "graded": 0, "ledger_open": True,
                                                          "exploration_emitted": 2, "exploration_skipped": 0},
                     {"date": PRE.isoformat(), "gate": {}, "candidates": [], "graded": [], "refresh": {"ok": True, "through": PRE.isoformat()}})
    assert SCH.validate(doc) == [] and len(doc["exploration"]) == 2 and doc["exploration"][0]["gate_verdict"] == "F3"
    text = R.render(doc)
    assert "exploration" in text.lower() and "F3" in text and "XYZ" in text
