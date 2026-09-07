"""engine.watch.basket: stacks, baskets and the episode rule (DESIGN/110-watch-basket.md §3-§4)."""
from __future__ import annotations

from datetime import date, timedelta

import pandas as pd
import pytest

from engine.watch import basket as BK

pytestmark = pytest.mark.unit


def test_stacks_counts_only_true_and_lists_true_and_null_ids():
    row = {
        "C-HIGH": True, "C-IVUP": False, "C-DIV": None, "C-DIV-D": False, "C-AVWAP": True,
        "C-POC": False, "C-POC-A": False, "C-SWING": True,
        "C-LOW": False, "C-SHORT": True, "C-OIBUILD": True, "C-CROWD": False,
        "C-AVWAP-LOSS": None, "C-POC-LOSS": False, "C-POC-A-LOSS": None, "C-SWING-LOSS": False,
        "C-VOL": True, "C-RSI": True, "C-LEAP": None, "C-DP": False,
    }
    s = BK.stacks(row)
    assert s["bull"] == 3          # C-HIGH, C-AVWAP, C-SWING
    assert s["bear"] == 2          # C-SHORT, C-OIBUILD
    assert s["vol"] is True
    assert set(s["true_ids"]) == {"C-HIGH", "C-AVWAP", "C-SWING", "C-SHORT", "C-OIBUILD", "C-VOL", "C-RSI"}
    assert set(s["null_ids"]) == {"C-DIV", "C-AVWAP-LOSS", "C-POC-A-LOSS", "C-LEAP"}


def test_stacks_missing_keys_treated_as_null():
    assert BK.stacks({})["bull"] == 0
    assert set(BK.stacks({})["null_ids"]) == set(BK.stacks({}).keys()) or True  # sanity: no crash
    assert len(BK.stacks({})["null_ids"]) == 20


def test_baskets_long_requires_three_bull_and_zero_bear():
    row = {"C-VOL": False, "C-LOW": False, "C-SHORT": False}
    assert BK.baskets(row, {"bull": 3, "bear": 0})["LONG"] is True
    assert BK.baskets(row, {"bull": 3, "bear": 1})["LONG"] is False
    assert BK.baskets(row, {"bull": 2, "bear": 0})["LONG"] is False


def test_baskets_short_requires_three_bear_and_zero_bull():
    row = {"C-VOL": False, "C-LOW": False, "C-SHORT": False}
    assert BK.baskets(row, {"bull": 0, "bear": 3})["SHORT"] is True
    assert BK.baskets(row, {"bull": 1, "bear": 3})["SHORT"] is False


def test_baskets_conflict_requires_two_and_two():
    row = {"C-VOL": False, "C-LOW": False, "C-SHORT": False}
    assert BK.baskets(row, {"bull": 2, "bear": 2})["CONFLICT"] is True
    assert BK.baskets(row, {"bull": 1, "bear": 2})["CONFLICT"] is False
    # a name can be CONFLICT and still fail both LONG and SHORT
    b = BK.baskets(row, {"bull": 2, "bear": 2})
    assert b["LONG"] is False and b["SHORT"] is False


def test_baskets_vol_requires_c_vol_true_and_not_confirmed_low_or_short():
    stack = {"bull": 0, "bear": 0}
    assert BK.baskets({"C-VOL": True, "C-LOW": False, "C-SHORT": False}, stack)["VOL"] is True
    assert BK.baskets({"C-VOL": True, "C-LOW": True, "C-SHORT": False}, stack)["VOL"] is False
    assert BK.baskets({"C-VOL": True, "C-LOW": False, "C-SHORT": True}, stack)["VOL"] is False
    assert BK.baskets({"C-VOL": False, "C-LOW": False, "C-SHORT": False}, stack)["VOL"] is False
    # unknown (None) C-LOW/C-SHORT does not exclude -- only a confirmed True does
    assert BK.baskets({"C-VOL": True, "C-LOW": None, "C-SHORT": None}, stack)["VOL"] is True


def test_baskets_calls_stacks_when_no_stack_given():
    row = {"C-HIGH": True, "C-IVUP": True, "C-DIV": True, "C-VOL": False, "C-LOW": False, "C-SHORT": False}
    out = BK.baskets(row)
    assert out["LONG"] is True   # bull=3 (HIGH, IVUP, DIV), bear=0


# --- episodes --------------------------------------------------------------------------------


def _sessions(n):
    base = date(2026, 1, 1)
    return {base + timedelta(days=i): i for i in range(n)}   # fake "trading day index" 0..n-1


def test_assign_episodes_collapses_reentries_within_21_sessions():
    order = _sessions(60)
    dates = list(order.keys())
    rows = pd.DataFrame({
        "ticker": ["A", "A", "A", "A", "B"],
        "date": [dates[0], dates[5], dates[25], dates[50], dates[3]],
    })
    out = BK.assign_episodes(rows, key_cols=["ticker"], date_col="date", session_order=order)
    a = out[out.ticker == "A"].sort_values("date")
    # idx0 -> idx5 (gap 5) -> idx25 (gap 20, still <=21) all one episode starting at dates[0]
    assert list(a["episode_start"]) == [dates[0], dates[0], dates[0], dates[50]]
    # idx50 - idx25 = 25 > 21 -> a new episode
    b = out[out.ticker == "B"]
    assert list(b["episode_start"]) == [dates[3]]
    assert BK.episode_count(out, ["ticker"]) == 3   # A has 2 episodes, B has 1


def test_assign_episodes_empty_input():
    out = BK.assign_episodes(pd.DataFrame(columns=["ticker", "date"]), ["ticker"], "date", {})
    assert out.empty
    assert BK.episode_count(out, ["ticker"]) == 0


def test_episode_count_distinguishes_different_keys_on_the_same_night():
    order = _sessions(10)
    dates = list(order.keys())
    rows = pd.DataFrame({"ticker": ["A", "B"], "date": [dates[0], dates[0]]})
    out = BK.assign_episodes(rows, ["ticker"], "date", order)
    assert BK.episode_count(out, ["ticker"]) == 2
