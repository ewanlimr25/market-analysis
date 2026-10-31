"""The fetch list behind the truth set and the FINRA loader (findings market-analysis D39, O14)."""
from __future__ import annotations

import json
import os
import sys
from datetime import date

import pandas as pd
import pytest

from engine import fetch_list as FL
from engine import ledger as L

pytestmark = pytest.mark.unit

E1, E2 = date(2026, 10, 2), date(2026, 10, 9)


def _rows(*specs) -> pd.DataFrame:
    """(ticker, E, role) -> ledger rows carrying every `L.KEY` column."""
    return pd.DataFrame([{"ticker": t, "E": e, "variant": "C1", "structure": "IB", "policy_id": "sc-1.0", "role": r}
                         for t, e, r in specs])


def _write_ledger(ledger_dir, signals: pd.DataFrame, graded: pd.DataFrame | None = None) -> str:
    os.makedirs(ledger_dir, exist_ok=True)
    signals.to_parquet(os.path.join(ledger_dir, L.SIGNALS_FILE), index=False)
    if graded is not None:
        graded.to_parquet(os.path.join(ledger_dir, L.LEDGER_FILE), index=False)
    return str(ledger_dir)


# ---- open_tickers (pure) ---------------------------------------------------------------------------

def test_a_signal_with_no_graded_row_is_open_whatever_its_role():
    signals = _rows(("WULF", E1, "champion"), ("SLDP", E1, "exploration"))
    assert FL.open_tickers(signals, pd.DataFrame()) == {"WULF", "SLDP"}


def test_a_graded_signal_is_not_open():
    signals = _rows(("WULF", E1, "champion"), ("MARA", E1, "champion"))
    graded = _rows(("WULF", E1, "champion"))
    assert FL.open_tickers(signals, graded) == {"MARA"}


def test_the_same_name_entered_again_is_open_until_that_entry_grades():
    signals = _rows(("WULF", E1, "champion"), ("WULF", E2, "champion"))
    graded = _rows(("WULF", E1, "champion"))
    assert FL.open_tickers(signals, graded) == {"WULF"}


def test_an_empty_ledger_holds_nothing():
    assert FL.open_tickers(pd.DataFrame(), pd.DataFrame()) == set()


# ---- combine (pure) --------------------------------------------------------------------------------

def test_the_list_is_the_sorted_union_of_the_universe_and_the_held_names():
    assert FL.combine(["MSFT", "AAPL"], ["SLDP", "AAPL"], indices=[]) == ["AAPL", "MSFT", "SLDP"]


def test_an_index_is_never_fetched_under_its_bare_symbol():
    assert FL.combine(["AAPL"], ["VIX", "SPX", "SLDP"], indices=["VIX", "SPX"]) == ["AAPL", "SLDP"]


def test_blank_and_missing_tickers_are_dropped():
    assert FL.combine(["AAPL"], ["", None, float("nan")], indices=[]) == ["AAPL"]


# ---- load (end to end, every source injected) -----------------------------------------------------

def test_load_unions_the_universe_file_the_open_rows_of_every_ledger_and_the_basket(tmp_path):
    universe = tmp_path / "universe.json"
    universe.write_text(json.dumps(["AAPL", "MSFT"]))
    sc = _write_ledger(tmp_path / "sc", _rows(("SLDP", E1, "exploration"), ("VIX", E1, "exploration"),
                                              ("WULF", E1, "champion")), _rows(("WULF", E1, "champion")))
    sa = _write_ledger(tmp_path / "sa", _rows(("TDOC", E2, "champion")))
    missing = str(tmp_path / "never-written")
    got = FL.load(str(universe), ledger_dirs=(sc, sa, missing),
                  basket_tickers=lambda: {"FLYW", "AAPL"}, index_tickers=lambda: {"VIX"})
    assert got == ["AAPL", "FLYW", "MSFT", "SLDP", "TDOC"]


def test_load_without_a_universe_file_still_returns_the_held_names(tmp_path):
    got = FL.load(str(tmp_path / "absent.json"), ledger_dirs=(),
                  basket_tickers=lambda: {"FLYW"}, index_tickers=lambda: set())
    assert got == ["FLYW"]


# ---- the two callers --------------------------------------------------------------------------------

def test_the_finra_loader_fetches_the_fetch_list_not_the_bare_universe(monkeypatch):
    from engine.mart import short_interest as SI
    seen = {}
    monkeypatch.setattr(FL, "load", lambda path: ["AAPL", "FLYW"])
    monkeypatch.setattr(SI, "refresh", lambda universe, **kw: seen.setdefault("u", list(universe)) and pd.DataFrame())
    monkeypatch.setattr(sys, "argv", ["short_interest", "--refresh"])
    assert SI.main() == 0
    assert seen["u"] == ["AAPL", "FLYW"]


def test_build_prices_fetches_the_fetch_list_plus_the_benchmarks(monkeypatch):
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts", "truthset"))
    import build_prices as BP
    monkeypatch.setattr(FL, "load", lambda path: ["SLDP", "AAPL"])
    assert BP.symbols() == ["AAPL", "IWM", "QQQ", "SLDP", "SPY"]
