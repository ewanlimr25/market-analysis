"""engine/book.py: `make book` -- the paper book on one page, each trade counted once."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine import book as B
from engine import ledger as L

pytestmark = pytest.mark.unit
ASOF = date(2026, 10, 5)


def _row(ticker, structure, variant="A1", role="champion", E="2026-10-01", risk=500.0, net=None, **kw):
    r = {"ticker": ticker, "E": E, "variant": variant, "structure": structure, "policy_id": "p-1.0", "role": role,
         "gate_verdict": "PASS", "expiry": "2026-10-09", "contracts": 1, "credit_entry": 3.0, "risk_usd": risk,
         "k": 35.0, "k_up": 41.0, "k_dn": 29.5, "post": "2026-10-02"}
    if net is not None:
        r["net_usd"] = net
    return {**r, **kw}


def _ledger(tmp_path, name, signals, graded=()):
    d = str(tmp_path / name)
    L.emit(d, pd.DataFrame(signals), ASOF)
    if graded:
        L.grade(d, pd.DataFrame(list(graded)), ASOF)
    return d


def test_variants_that_took_the_same_trade_count_once(tmp_path):
    sig = [_row("NKE", "SS", "A1"), _row("NKE", "SS", "A2"), _row("NKE", "IC", "A1"), _row("NKE", "IC", "A2")]
    graded = [_row("NKE", "SS", "A1", net=100.0), _row("NKE", "SS", "A2", net=100.0),
              _row("NKE", "IC", "A1", net=67.0, risk=292.0), _row("NKE", "IC", "A2", net=67.0, risk=292.0)]
    book = B.load(B.Strategy("S-A", _ledger(tmp_path, "sa", sig, graded), B.SA_STRIKES))
    assert len(book.closed) == 2 and book.open.empty
    assert set(book.closed.variants) == {"A1+A2"}
    s = B.summary(book).set_index("structure")
    assert s.loc["SS", "net_usd"] == 100.0 and s.loc["IC", "net_usd"] == 67.0
    assert s.loc["IC", "mean_ror"] == pytest.approx(67.0 / 292.0)


def test_exploration_rows_stay_out_of_the_book_but_are_counted(tmp_path):
    sig = [_row("SPY", "PS", "base"), _row("SPY", "PS", "base", role="exploration"),
           _row("QQQ", "PS", "base", role="exploration")]
    book = B.load(B.Strategy("S-B", _ledger(tmp_path, "sb", sig), B.SB_STRIKES))
    assert list(book.open.ticker) == ["SPY"] and book.exploration_open == 2


def test_open_means_emitted_and_not_yet_graded(tmp_path):
    sig = [_row("WULF", "IB", "C1", E="2026-10-02"), _row("MARA", "IB", "C1", E="2026-10-02")]
    graded = [_row("WULF", "IB", "C1", E="2026-10-02", net=-40.0)]
    book = B.load(B.Strategy("S-C", _ledger(tmp_path, "sc", sig, graded), B.SC_STRIKES))
    assert list(book.open.ticker) == ["MARA"] and list(book.closed.ticker) == ["WULF"]
    s = B.summary(book).set_index("structure").loc["IB"]
    assert (s.open_n, s.open_risk_usd, s.closed_n, s.wins, s.net_usd) == (1, 500.0, 1, 0, -40.0)


def test_a_missing_ledger_is_an_empty_book(tmp_path):
    book = B.load(B.Strategy("S-C", str(tmp_path / "none"), B.SC_STRIKES))
    assert book.open.empty and book.closed.empty and B.summary(book).empty


def test_render_lists_open_positions_with_strikes_and_closed_totals(tmp_path):
    sb = [_row("SPY", "PS", "base", k_p1=741.0, k_p2=715.0, expiry="2026-10-23", risk=2479.13)]
    sa = [_row("NKE", "SS")]
    sa_graded = [_row("NKE", "SS", net=100.79)]
    books = [B.load(B.Strategy("S-A", _ledger(tmp_path, "sa", sa, sa_graded), B.SA_STRIKES)),
             B.load(B.Strategy("S-B", _ledger(tmp_path, "sb", sb), B.SB_STRIKES))]
    md = B.render(books, ASOF)
    assert "715/741" in md and "2026-10-23" in md and "2,479.13" in md
    assert "+100.79" in md and "paper" in md.lower()
