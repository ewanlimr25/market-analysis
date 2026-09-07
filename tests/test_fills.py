"""G1: fill-quality bucket assignment (`engine/improve/fills.py`)."""
from __future__ import annotations

import duckdb
import pandas as pd
import pytest

from engine.improve import fills as G

pytestmark = pytest.mark.unit


# ----------------------------------------------------------------------------- dte_bucket

@pytest.mark.parametrize("dte,expected", [
    (0, "0dte"), (1, "1-2d"), (2, "1-2d"), (3, "3-7d"), (7, "3-7d"),
    (8, "8-21d"), (21, "8-21d"), (22, "22-45d"), (45, "22-45d"), (46, "46d+"), (400, "46d+"),
])
def test_dte_bucket_edges(dte, expected):
    assert G.dte_bucket(dte) == expected


# ----------------------------------------------------------------------------- bucket30

def test_bucket30_index_first_and_later_buckets():
    assert G.bucket30_index(0) == 0
    assert G.bucket30_index(29) == 0
    assert G.bucket30_index(30) == 1
    assert G.bucket30_index(65) == 2


def test_bucket30_index_rejects_negative():
    with pytest.raises(ValueError):
        G.bucket30_index(-1)


def test_bucket30_label_anchored_at_session_start():
    assert G.bucket30_label(0) == "09:30-10:00"
    assert G.bucket30_label(1) == "10:00-10:30"


# ----------------------------------------------------------------------------- in_window

def test_in_window_early_and_late_boundaries():
    assert G.in_window("09:30:00", G.WINDOW_EARLY)
    assert G.in_window("10:30:00", G.WINDOW_EARLY)
    assert not G.in_window("10:30:01", G.WINDOW_EARLY)
    assert not G.in_window("14:59:59", G.WINDOW_LATE)
    assert G.in_window("15:00:00", G.WINDOW_LATE)
    assert G.in_window("16:00:00", G.WINDOW_LATE)


def test_in_window_b1_and_b2_boundaries():
    assert not G.in_window("10:30:00", G.WINDOW_B1)
    assert G.in_window("10:30:01", G.WINDOW_B1)
    assert G.in_window("11:30:00", G.WINDOW_B1)
    assert not G.in_window("11:30:01", G.WINDOW_B1)
    assert G.in_window("14:30:00", G.WINDOW_B2)
    assert G.in_window("15:30:00", G.WINDOW_B2)
    assert not G.in_window("14:29:59", G.WINDOW_B2)


def test_in_window_late_and_b2_overlap():
    assert G.in_window("15:15:00", G.WINDOW_LATE)
    assert G.in_window("15:15:00", G.WINDOW_B2)


# ----------------------------------------------------------------------------- tier_from_window_size

def test_tier_from_window_size():
    assert G.tier_from_window_size(5) == 1
    assert G.tier_from_window_size(4.9) == 2
    assert G.tier_from_window_size(0) == 2


# ----------------------------------------------------------------------------- classify_fill

def test_classify_ask_side_at_mid_is_best():
    assert G.classify_fill("ask", 1.00, 0.90, 1.10) == G.CLASS_AT_OR_BETTER_MID


def test_classify_ask_side_below_mid_is_still_best():
    assert G.classify_fill("ask", 0.92, 0.90, 1.10) == G.CLASS_AT_OR_BETTER_MID


def test_classify_ask_side_between_mid_and_touch():
    assert G.classify_fill("ask", 1.05, 0.90, 1.10) == G.CLASS_BETWEEN_MID_TOUCH


def test_classify_ask_side_at_touch():
    assert G.classify_fill("ask", 1.10, 0.90, 1.10) == G.CLASS_AT_TOUCH


def test_classify_ask_side_outside():
    assert G.classify_fill("ask", 1.20, 0.90, 1.10) == G.CLASS_OUTSIDE


def test_classify_bid_side_mirrors_ask():
    # symmetric prices around the same NBBO, bid aggressor
    assert G.classify_fill("bid", 1.00, 0.90, 1.10) == G.CLASS_AT_OR_BETTER_MID
    assert G.classify_fill("bid", 0.95, 0.90, 1.10) == G.CLASS_BETWEEN_MID_TOUCH
    assert G.classify_fill("bid", 0.90, 0.90, 1.10) == G.CLASS_AT_TOUCH
    assert G.classify_fill("bid", 0.80, 0.90, 1.10) == G.CLASS_OUTSIDE


def test_classify_mid_side_unsigned():
    assert G.classify_fill("mid", 1.00, 0.90, 1.10) == G.CLASS_AT_OR_BETTER_MID
    assert G.classify_fill("mid", 0.95, 0.90, 1.10) == G.CLASS_BETWEEN_MID_TOUCH
    assert G.classify_fill("mid", 1.05, 0.90, 1.10) == G.CLASS_BETWEEN_MID_TOUCH
    assert G.classify_fill("mid", 0.90, 0.90, 1.10) == G.CLASS_AT_TOUCH
    assert G.classify_fill("mid", 1.10, 0.90, 1.10) == G.CLASS_AT_TOUCH
    assert G.classify_fill("mid", 1.20, 0.90, 1.10) == G.CLASS_OUTSIDE


def test_classify_zero_width_quote_is_at_touch():
    assert G.classify_fill("ask", 1.00, 1.00, 1.00) == G.CLASS_AT_TOUCH


def test_classify_rejects_no_side():
    with pytest.raises(ValueError):
        G.classify_fill("no_side", 1.00, 0.90, 1.10)


def test_classify_rejects_invalid_nbbo():
    with pytest.raises(ValueError):
        G.classify_fill("ask", 1.00, 1.10, 0.90)  # crossed
    with pytest.raises(ValueError):
        G.classify_fill("ask", 1.00, 0.0, 1.10)   # non-positive bid


def test_classify_rejects_unknown_side():
    with pytest.raises(ValueError):
        G.classify_fill("cross", 1.00, 0.90, 1.10)


# ----------------------------------------------------------------------------- mid_or_better_share

def test_mid_or_better_share_basic():
    rows = [
        {"class": G.CLASS_AT_OR_BETTER_MID, "volume": 60.0, "premium": 600.0},
        {"class": G.CLASS_AT_TOUCH, "volume": 40.0, "premium": 400.0},
    ]
    r = G.mid_or_better_share(rows)
    assert r.volume == 100.0 and r.premium == 1000.0
    assert r.volume_share == pytest.approx(0.6)
    assert r.premium_share == pytest.approx(0.6)


def test_mid_or_better_share_empty_is_nan():
    r = G.mid_or_better_share([])
    assert r.volume == 0.0
    import math
    assert math.isnan(r.volume_share)


# ----------------------------------------------------------------------------- SQL / Python parity
# The driver classifies ~10M prints/day in SQL for speed; this asserts the SQL CASE expression
# (`classify_fill_sql`) makes exactly the same call as the tested Python function on the same rows.

def _synthetic_rows() -> pd.DataFrame:
    cases = [
        ("ask", 1.00, 0.90, 1.10), ("ask", 0.92, 0.90, 1.10), ("ask", 1.05, 0.90, 1.10),
        ("ask", 1.10, 0.90, 1.10), ("ask", 1.20, 0.90, 1.10), ("ask", 0.70, 0.90, 1.10),
        ("bid", 1.00, 0.90, 1.10), ("bid", 0.95, 0.90, 1.10), ("bid", 0.90, 0.90, 1.10),
        ("bid", 0.80, 0.90, 1.10), ("bid", 1.30, 0.90, 1.10),
        ("mid", 1.00, 0.90, 1.10), ("mid", 0.95, 0.90, 1.10), ("mid", 1.05, 0.90, 1.10),
        ("mid", 0.90, 0.90, 1.10), ("mid", 1.10, 0.90, 1.10), ("mid", 1.20, 0.90, 1.10),
        ("ask", 1.00, 1.00, 1.00),
    ]
    return pd.DataFrame(cases, columns=["side", "price", "bid", "ask"])


def test_sql_classification_matches_python():
    df = _synthetic_rows()
    con = duckdb.connect()
    con.register("rows", df)
    expr = G.classify_fill_sql("side", "price", "bid", "ask")
    out = con.execute(f"SELECT *, {expr} AS cls FROM rows").df()
    for _, row in out.iterrows():
        expected = G.classify_fill(row["side"], row["price"], row["bid"], row["ask"])
        assert row["cls"] == expected, row.to_dict()


def test_sql_dte_bucket_matches_python():
    con = duckdb.connect()
    df = pd.DataFrame({"dte": [0, 1, 2, 3, 7, 8, 21, 22, 45, 46, 400]})
    con.register("rows", df)
    out = con.execute(f"SELECT dte, {G.dte_bucket_sql('dte')} AS b FROM rows").df()
    for _, row in out.iterrows():
        assert row["b"] == G.dte_bucket(int(row["dte"]))


def test_sql_in_window_matches_python():
    con = duckdb.connect()
    times = ["09:30:00", "10:30:00", "10:30:01", "11:30:00", "11:30:01",
            "14:29:59", "14:30:00", "14:59:59", "15:00:00", "15:15:00", "15:30:00", "16:00:00"]
    df = pd.DataFrame({"t": times})
    con.register("rows", df)
    for window in G.CANDIDATE_WINDOWS:
        out = con.execute(f"SELECT t, {G.in_window_sql('t::TIME', window)} AS w FROM rows").df()
        for _, row in out.iterrows():
            assert bool(row["w"]) == G.in_window(row["t"], window), (window, row["t"])
