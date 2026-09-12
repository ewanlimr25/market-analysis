"""engine.watch.nightly: the R2 nightly step (DESIGN/110-watch-basket.md §7 R2). `evaluate_fn` is
injected everywhere (the same pattern `test_sb_daily.py` uses for its loaders) so these tests never
touch the mart, the raw UW exports, or the network -- only the row contract, the ledger and the
episode/grading logic are exercised, on synthetic condition frames."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine import calendar as cal
from engine import policy as POL
from engine.config import LEDGER_WB_OPEN
from engine.watch import basket as BK
from engine.watch import conditions as C
from engine.watch import live as LV
from engine.watch import nightly as N
from engine.watch.wb_ledger import read_ledger

pytestmark = pytest.mark.unit

D0 = date(2026, 6, 9)          # a trading day, well before LEDGER_WB_OPEN
assert D0 < LEDGER_WB_OPEN


def _cond_row(ticker: str, d: date, true_conditions: tuple[str, ...] = ()) -> dict:
    flags = {cid: (cid in true_conditions) for cid in C.ALL_CONDITIONS}
    stack = BK.stacks(flags)
    row = {"ticker": ticker, "date": d, **flags, "bull": stack["bull"], "bear": stack["bear"],
           "vol": stack["vol"], "true_ids": stack["true_ids"], "null_ids": stack["null_ids"]}
    row.update(BK.baskets(flags, stack))
    return row


LONG_IDS = ("C-HIGH", "C-AVWAP", "C-SWING")     # 3 bull, 0 bear -> LONG
SHORT_IDS = ("C-LOW", "C-SHORT", "C-OIBUILD")   # 0 bull, 3 bear -> SHORT
CONFLICT_IDS = ("C-HIGH", "C-AVWAP", "C-LOW", "C-SHORT")  # 2 bull, 2 bear -> CONFLICT only


def _evaluate_fn(rows: list[dict], universe_n: int = 100):
    df = pd.DataFrame(rows) if rows else pd.DataFrame(
        columns=["ticker", "date", *C.ALL_CONDITIONS, "bull", "bear", "vol", "true_ids", "null_ids",
                 *BK.BASKET_NAMES])

    def fn(d):
        return df, universe_n
    return fn


# ---- evaluate_conditions wiring (live path) ------------------------------------------------------

def test_evaluate_conditions_wires_poc_a_through_to_bar_derived_keys():
    d = date(2026, 6, 9)
    universe = pd.DataFrame([{
        "ticker": "X", "date": d, "pct_52w_range": 0.9, "days_to_cover": None,
        "borrow_fee_pct": None, "c_oibuild_raw": True, "c_crowd_raw": False,
        "ivrank_chg_5d": 15.0, "iv30d": 0.5, "marketcap": 5e9, "has_tier1_atm_pair": True,
        "next_earnings_date": None, "c_leap_raw": True, "c_dp_raw": True,
    }])
    # no bars for X -> every bar-derived condition, including the new anchored-POC pair, is None
    out = N.evaluate_conditions(universe, series_map={})
    row = out.to_dict("records")[0]
    assert row["C-POC-A"] is None
    assert row["C-POC-A-LOSS"] is None
    assert row["C-POC"] is None and row["C-POC-LOSS"] is None   # unchanged sibling behaviour


# ---- row contract -------------------------------------------------------------------------------

def test_run_emits_one_row_per_basket_with_policy_columns_and_gate_verdict(tmp_path):
    rows = [_cond_row("LONGCO", D0, LONG_IDS), _cond_row("SHORTCO", D0, SHORT_IDS)]
    state = N.run(None, D0, str(tmp_path), force_ledger=True, evaluate_fn=_evaluate_fn(rows))
    assert {k: state[k] for k in ("wb_emitted", "wb_skipped", "wb_graded", "ledger_open")} == {"wb_emitted": 2, "wb_skipped": 0, "wb_graded": 0, "ledger_open": True}
    led = read_ledger(str(tmp_path))
    assert len(led) == 2
    assert set(led.policy_id) == {"wb-1.0"} and set(led.role) == {POL.ROLE_EXPLORATION}
    POL.require_policy_columns(led)
    long_row = led[led.ticker == "LONGCO"].iloc[0]
    assert long_row.basket == "LONG" and long_row.bull == 3 and long_row.bear == 0
    assert long_row.gate_verdict.startswith("LONG:3/0:")
    assert set(long_row.gate_verdict.split(":")[2].split(",")) == set(LONG_IDS)
    assert bool(long_row.episode) is True and long_row.benchmark == "spy_excess"
    assert long_row.excess_h5 is None and long_row.excess_h10 is None and long_row.excess_h21 is None


def test_conflict_is_reported_but_never_written_to_the_ledger(tmp_path):
    rows = [_cond_row("CFLCO", D0, CONFLICT_IDS)]
    state = N.run(None, D0, str(tmp_path), force_ledger=True, evaluate_fn=_evaluate_fn(rows))
    assert state["wb_emitted"] == 0
    assert read_ledger(str(tmp_path)).empty
    assert [r["ticker"] for r in state["conflict"]] == ["CFLCO"]
    assert state["long"] == [] and state["short"] == []


def test_key_is_unique_and_a_second_run_is_idempotent(tmp_path):
    rows = [_cond_row("LONGCO", D0, LONG_IDS)]
    fn = _evaluate_fn(rows)
    first = N.run(None, D0, str(tmp_path), force_ledger=True, evaluate_fn=fn)
    second = N.run(None, D0, str(tmp_path), force_ledger=True, evaluate_fn=fn)
    assert first["wb_emitted"] == 1
    assert {k: second[k] for k in ("wb_emitted", "wb_skipped", "wb_graded", "ledger_open")} == {"wb_emitted": 0, "wb_skipped": 1, "wb_graded": 0, "ledger_open": True}
    assert len(read_ledger(str(tmp_path))) == 1


# ---- open-date gating -----------------------------------------------------------------------------

def test_nothing_written_before_the_open_date_unless_forced(tmp_path):
    rows = [_cond_row("LONGCO", D0, LONG_IDS)]
    state = N.run(None, D0, str(tmp_path), force_ledger=False, evaluate_fn=_evaluate_fn(rows))
    assert {k: state[k] for k in ("wb_emitted", "wb_skipped", "wb_graded", "ledger_open")} == {"wb_emitted": 0, "wb_skipped": 0, "wb_graded": 0, "ledger_open": False}
    assert read_ledger(str(tmp_path)).empty
    assert state["long"] and state["long"][0]["ticker"] == "LONGCO"      # state still reports it


def test_ledger_open_on_and_after_the_open_date_without_forcing(tmp_path):
    rows = [_cond_row("LONGCO", LEDGER_WB_OPEN, LONG_IDS)]
    state = N.run(None, LEDGER_WB_OPEN, str(tmp_path), force_ledger=False, evaluate_fn=_evaluate_fn(rows))
    assert state["ledger_open"] is True and state["wb_emitted"] == 1


# ---- ledger-dir honoured --------------------------------------------------------------------------

def test_ledger_dir_argument_is_honoured(tmp_path):
    a, b = tmp_path / "a", tmp_path / "b"
    rows = [_cond_row("LONGCO", D0, LONG_IDS)]
    N.run(None, D0, str(a), force_ledger=True, evaluate_fn=_evaluate_fn(rows))
    assert len(read_ledger(str(a))) == 1
    assert read_ledger(str(b)).empty


# ---- episode rule (DESIGN/110 §4) ------------------------------------------------------------------

def test_episode_flag_false_on_reentry_within_21_sessions_true_after(tmp_path):
    d1 = D0
    d2 = cal.next_session(d1, 5)          # within 21 sessions: continuation
    d3 = cal.next_session(d1, 30)         # more than 21 sessions later: a new episode
    rows1 = [_cond_row("LONGCO", d1, LONG_IDS)]
    N.run(None, d1, str(tmp_path), force_ledger=True, evaluate_fn=_evaluate_fn(rows1))
    rows2 = [_cond_row("LONGCO", d2, LONG_IDS)]
    N.run(None, d2, str(tmp_path), force_ledger=True, evaluate_fn=_evaluate_fn(rows2))
    rows3 = [_cond_row("LONGCO", d3, LONG_IDS)]
    N.run(None, d3, str(tmp_path), force_ledger=True, evaluate_fn=_evaluate_fn(rows3))
    led = read_ledger(str(tmp_path)).sort_values("date")
    assert led["episode"].tolist() == [True, False, True]


# ---- fail-soft --------------------------------------------------------------------------------------

def test_nightly_is_fail_soft_when_evaluation_raises(tmp_path):
    def boom(d):
        raise RuntimeError("synthetic failure")
    state = N.nightly(None, D0, force_ledger=True, ledger_dir=str(tmp_path), evaluate_fn=boom)
    assert state["available"] is False
    assert "synthetic failure" in state["reason"]
    assert state["long"] == [] and state["wb_emitted"] == 0
    assert "elapsed_s" in state
    assert read_ledger(str(tmp_path)).empty
    assert state["count_distribution"]["bull"] == {str(i): 0 for i in range(len(C.SIGN_PLUS) + 1)}
    assert state["count_distribution"]["bear"] == {str(i): 0 for i in range(len(C.SIGN_MINUS) + 1)}


def test_nightly_available_true_on_a_normal_run(tmp_path):
    rows = [_cond_row("LONGCO", D0, LONG_IDS)]
    state = N.nightly(None, D0, force_ledger=True, ledger_dir=str(tmp_path), evaluate_fn=_evaluate_fn(rows))
    assert state["available"] is True and state["reason"] is None
    assert "elapsed_s" in state


# ---- count distribution / top-n shapes --------------------------------------------------------------

def test_count_distribution_and_top_n_shapes(tmp_path):
    rows = [_cond_row("LONGCO", D0, LONG_IDS), _cond_row("SHORTCO", D0, SHORT_IDS)]
    state = N.run(None, D0, str(tmp_path), force_ledger=True, evaluate_fn=_evaluate_fn(rows))
    assert state["count_distribution"]["bull"] == {str(i): (1 if i == 3 else (1 if i == 0 else 0))
                                                    for i in range(len(C.SIGN_PLUS) + 1)}
    assert set(state["count_distribution"]["bull"]) == {str(i) for i in range(len(C.SIGN_PLUS) + 1)}
    assert set(state["count_distribution"]["bear"]) == {str(i) for i in range(len(C.SIGN_MINUS) + 1)}
    assert state["top_bull"][0]["ticker"] == "LONGCO" and state["top_bull"][0]["bull"] == 3
    assert state["top_bear"][0]["ticker"] == "SHORTCO" and state["top_bear"][0]["bear"] == 3


# ---- grading (h5/h10/h21 SPY excess from the screener spine) -----------------------------------------

def test_grade_open_rows_fills_excess_h5_once_the_target_session_has_closed(tmp_path, monkeypatch):
    d1 = D0
    rows1 = [_cond_row("GRADEME", d1, LONG_IDS)]
    N.run(None, d1, str(tmp_path), force_ledger=True, evaluate_fn=_evaluate_fn(rows1))
    d_h5 = cal.next_session(d1, 5)

    closes = {("GRADEME", d1): 100.0, ("GRADEME", d_h5): 110.0, ("SPY", d1): 500.0, ("SPY", d_h5): 505.0}
    monkeypatch.setattr(LV, "load_closes", lambda tickers, dates, stocks_dir=None: closes)

    n_graded = N.grade_open_rows(str(tmp_path), d_h5)
    assert n_graded == 1
    led = read_ledger(str(tmp_path))
    row = led[led.ticker == "GRADEME"].iloc[0]
    fwd_ret, spy_ret = 110.0 / 100.0 - 1, 505.0 / 500.0 - 1
    assert row.excess_h5 == pytest.approx(fwd_ret - spy_ret)
    assert row.excess_h10 is None and row.excess_h21 is None

    # a second call the same night (or later, before h10 closes) must not touch the filled cell
    monkeypatch.setattr(LV, "load_closes", lambda tickers, dates, stocks_dir=None: {})
    assert N.grade_open_rows(str(tmp_path), d_h5) == 0
    led2 = read_ledger(str(tmp_path))
    assert led2[led2.ticker == "GRADEME"].iloc[0].excess_h5 == pytest.approx(fwd_ret - spy_ret)


def test_grade_open_rows_never_writes_a_false_value_when_a_close_is_missing(tmp_path, monkeypatch):
    d1 = D0
    rows1 = [_cond_row("NOCLOSE", d1, LONG_IDS)]
    N.run(None, d1, str(tmp_path), force_ledger=True, evaluate_fn=_evaluate_fn(rows1))
    d_h5 = cal.next_session(d1, 5)
    monkeypatch.setattr(LV, "load_closes", lambda tickers, dates, stocks_dir=None: {})
    assert N.grade_open_rows(str(tmp_path), d_h5) == 0
    led = read_ledger(str(tmp_path))
    assert led.iloc[0].excess_h5 is None


def test_grade_open_rows_empty_ledger_is_a_noop(tmp_path):
    assert N.grade_open_rows(str(tmp_path), D0) == 0


def test_run_grades_via_the_public_entry_point(tmp_path, monkeypatch):
    d1 = D0
    N.run(None, d1, str(tmp_path), force_ledger=True, evaluate_fn=_evaluate_fn([_cond_row("GRADEME", d1, LONG_IDS)]))
    d_h5 = cal.next_session(d1, 5)
    closes = {("GRADEME", d1): 100.0, ("GRADEME", d_h5): 90.0, ("SPY", d1): 500.0, ("SPY", d_h5): 505.0}
    monkeypatch.setattr(LV, "load_closes", lambda tickers, dates, stocks_dir=None: closes)
    state = N.run(None, d_h5, str(tmp_path), force_ledger=True, evaluate_fn=_evaluate_fn([]))
    assert state["wb_graded"] == 1


def test_run_carries_borrow_provenance_from_the_evaluated_frame(tmp_path):
    """The state dict names the IBKR snapshot C-SHORT read (d1.5 `borrow`), taken from the
    evaluated frame's attrs so a fallback night is visible in signals.json and the report."""
    from datetime import date as _date
    rows = [_cond_row("LONGCO", D0, LONG_IDS)]
    base_fn = _evaluate_fn(rows)

    def evaluate_fn(d):
        cond_df, n = base_fn(d)
        cond_df.attrs["borrow"] = {"asof": _date(2026, 9, 10), "stale_days": 1, "names_with_fee": 1}
        return cond_df, n

    state = N.run(None, D0, str(tmp_path), force_ledger=True, evaluate_fn=evaluate_fn)
    assert state["borrow"] == {"asof": _date(2026, 9, 10), "stale_days": 1, "names_with_fee": 1}


def test_borrow_provenance_reads_the_join_output():
    from datetime import date as _date
    side = pd.DataFrame({"borrow_fee": [1.0, float("nan"), 2.0], "borrow_asof": [_date(2026, 9, 10), None, _date(2026, 9, 10)]})
    assert N._borrow_provenance(side, _date(2026, 9, 11)) == {"asof": _date(2026, 9, 10), "stale_days": 1, "names_with_fee": 2}
    empty = pd.DataFrame({"borrow_fee": [float("nan")], "borrow_asof": [None]})
    assert N._borrow_provenance(empty, _date(2026, 9, 11)) == {"asof": None, "stale_days": None, "names_with_fee": 0}
