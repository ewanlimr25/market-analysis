"""engine.watch.retro_tables: the five DESIGN/110-watch-basket.md §5 descriptive tables, on a
small hand-built `wb_conditions`-shaped frame so every number is checkable by hand."""
from __future__ import annotations

from datetime import date, timedelta

import pandas as pd
import pytest

from engine.watch import basket as BK
from engine.watch import conditions as C
from engine.watch import retro_tables as RT

pytestmark = pytest.mark.unit


def _dates(n):
    base = date(2026, 1, 5)
    return [base + timedelta(days=i) for i in range(n)]


def _row(ticker, d, **overrides):
    r = {cid: None for cid in C.ALL_CONDITIONS}
    r.update({"ticker": ticker, "date": d, "bull": 0, "bear": 0, "vol": False,
              "LONG": False, "SHORT": False, "VOL": False, "CONFLICT": False})
    r.update(overrides)
    return r


@pytest.fixture
def fixture():
    d = _dates(4)
    rows = [
        _row("A", d[0], **{"C-HIGH": True}, bull=3, LONG=True),
        _row("A", d[1], **{"C-HIGH": True}, bull=2),
        _row("A", d[2], **{"C-HIGH": False}, bear=3, SHORT=True),
        _row("B", d[2], **{"C-HIGH": True}, bull=1),
        _row("C", d[3], **{"C-HIGH": None}, bull=0, bear=0),
    ]
    cond_df = pd.DataFrame(rows)
    returns_df = pd.DataFrame([
        {"ticker": "A", "date": d[0], "horizon": 21, "excess": 0.05, "resolved": True},
        {"ticker": "A", "date": d[1], "horizon": 21, "excess": 0.03, "resolved": True},
        {"ticker": "B", "date": d[2], "horizon": 21, "excess": -0.02, "resolved": True},
        {"ticker": "A", "date": d[2], "horizon": 21, "excess": -0.10, "resolved": True},
    ])
    return d, cond_df, returns_df


def test_condition_table_c_high(fixture):
    d, cond_df, returns_df = fixture
    table = RT.condition_table(cond_df, returns_df)
    row = table[table.key == "C-HIGH"].iloc[0]
    assert row.nights_true == 3          # A/d0, A/d1, B/d2
    assert row.names == 2                # A, B
    assert row.episodes == 2             # A's d0->d1 (gap 1) one episode; B's d2 a second
    assert row.h21_n == 3
    assert row.h21_mean_excess == pytest.approx((0.05 + 0.03 - 0.02) / 3)
    assert row.null_nights == 1          # C's row is None
    assert row.null_rate == pytest.approx(1 / 5)
    assert row.sign == "+"


def test_condition_table_covers_all_20_conditions(fixture):
    _, cond_df, returns_df = fixture
    table = RT.condition_table(cond_df, returns_df)
    assert set(table["key"]) == set(C.ALL_CONDITIONS)
    other = table[table.key == "C-LOW"].iloc[0]
    assert other.nights_true == 0 and other.episodes == 0


def test_count_table_per_bull_value(fixture):
    _, cond_df, returns_df = fixture
    table = RT.count_table(cond_df, returns_df, "bull", max_count=3)
    row3 = table[table.key == "bull=3"].iloc[0]
    assert row3.nights_true == 1  # only A/d0
    assert row3.h21_mean_excess == pytest.approx(0.05)
    row0 = table[table.key == "bull=0"].iloc[0]
    assert row0.nights_true == 2  # A/d2 (bear row, bull defaults to 0) and C/d3


def test_basket_table(fixture):
    _, cond_df, returns_df = fixture
    table = RT.basket_table(cond_df, returns_df)
    long_row = table[table.key == "LONG"].iloc[0]
    assert long_row.nights_true == 1
    assert long_row.h21_mean_excess == pytest.approx(0.05)
    short_row = table[table.key == "SHORT"].iloc[0]
    assert short_row.nights_true == 1
    assert short_row.h21_mean_excess == pytest.approx(-0.10)


def test_worked_examples_top_bull_and_bear(fixture):
    _, cond_df, returns_df = fixture
    ex = RT.worked_examples(cond_df, returns_df, n=2)
    top_bull = ex["top_bull"]
    assert top_bull[0]["ticker"] == "A" and top_bull[0]["bull"] == 3
    assert top_bull[0]["h21_excess"] == pytest.approx(0.05)
    assert "C-HIGH" in top_bull[0]["true_ids"]
    top_bear = ex["top_bear"]
    assert top_bear[0]["ticker"] == "A" and top_bear[0]["bear"] == 3


def test_nightly_basket_sizes_includes_zero_nights(fixture):
    _, cond_df, returns_df = fixture
    sizes = RT.nightly_basket_sizes(cond_df)
    assert sizes["LONG"]["max"] == 1
    assert sizes["LONG"]["min"] == 0     # most of the 4 nights have zero LONG names
    assert sizes["CONFLICT"]["max"] == 0


def test_base_stats_is_unconditional_over_the_whole_universe(fixture):
    _, cond_df, returns_df = fixture
    base = RT.base_stats(cond_df, returns_df)
    assert base[21]["n"] == 4  # all 4 resolved h21 rows in returns_df
    assert base[5]["n"] == 0   # no h5 rows at all
