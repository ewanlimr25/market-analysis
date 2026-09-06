"""Q1: CBOE index-vol parsing, merge and the no-network loader (DESIGN/80 §1.1)."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine.mart import index_vol as IV

pytestmark = pytest.mark.unit

CSV_VIX = "DATE,OPEN,HIGH,LOW,CLOSE\n09/02/2026,15.5,15.9,15.0,15.20\n09/03/2026,15.1,15.4,14.2,14.32\n09/04/2026,14.15,14.58,13.8,14.53\n"
CSV_VIX3M = "DATE,OPEN,HIGH,LOW,CLOSE\n09/02/2026,17.9,18.0,17.6,17.73\n09/04/2026,17.34,17.67,17.21,17.61\n"


def test_parse_cboe_csv_gives_dates_and_the_named_close_column():
    df = IV.parse_cboe_csv(CSV_VIX, "VIX")
    assert list(df.columns) == ["date", "vix"]
    assert df.date.tolist() == [date(2026, 9, 2), date(2026, 9, 3), date(2026, 9, 4)]
    assert df.vix.tolist() == pytest.approx([15.20, 14.32, 14.53])


def test_merge_is_an_outer_join_on_date_with_every_column_present():
    merged = IV.merge_indices([IV.parse_cboe_csv(CSV_VIX, "VIX"), IV.parse_cboe_csv(CSV_VIX3M, "VIX3M")])
    assert list(merged.columns) == IV.COLUMNS
    assert len(merged) == 3
    row = merged[merged.date == date(2026, 9, 3)].iloc[0]
    assert row.vix == pytest.approx(14.32) and pd.isna(row.vix3m) and pd.isna(row.vxn)
    assert merged.date.is_monotonic_increasing


def test_parse_rejects_a_malformed_csv():
    with pytest.raises(ValueError):
        IV.parse_cboe_csv("nonsense,without,close\n1,2,3\n", "VIX")


def test_load_prefers_the_mart_file_then_the_fallback_then_empty(tmp_path):
    mart = tmp_path / "index_vol.parquet"
    fallback = tmp_path / "fallback.parquet"
    assert IV.load_index_vol(str(mart), str(fallback)).empty
    IV.normalize(pd.DataFrame({"date": ["2026-09-04"], "vix": [14.53], "vix3m": [17.61], "vxn": [20.04], "vix9d": [11.97]})).to_parquet(fallback, index=False)
    assert IV.latest_date(IV.load_index_vol(str(mart), str(fallback))) == date(2026, 9, 4)
    IV.write_index_vol(IV.normalize(pd.DataFrame({"date": ["2026-09-08"], "vix": [15.0], "vix3m": [17.0], "vxn": [21.0], "vix9d": [12.0]})), str(mart))
    assert IV.latest_date(IV.load_index_vol(str(mart), str(fallback))) == date(2026, 9, 8)


def test_refresh_uses_the_fetcher_and_writes_atomically(tmp_path):
    texts = {"VIX": CSV_VIX, "VIX3M": CSV_VIX3M, "VXN": CSV_VIX.replace("14.53", "20.04"), "VIX9D": CSV_VIX.replace("14.53", "11.97")}
    out = IV.refresh(str(tmp_path / "iv.parquet"), fetch_text=lambda index: texts[index])
    assert IV.latest_date(out) == date(2026, 9, 4) and out.iloc[-1].vxn == pytest.approx(20.04)
    assert (tmp_path / "iv.parquet").exists() and not (tmp_path / "iv.parquet.tmp").exists()


def test_on_sessions_drops_holiday_rows_that_carry_only_a_vix_print():
    df = IV.normalize(pd.DataFrame({"date": ["2026-09-04", "2026-09-07", "2026-09-08"], "vix": [14.5, 14.6, 15.0],
                                    "vix3m": [17.6, None, 17.7], "vxn": [20.0, None, 20.5], "vix9d": [12.0, None, 12.5]}))
    kept = IV.on_sessions(df, lambda d: d != date(2026, 9, 7))          # Labor Day 2026
    assert kept.date.tolist() == [date(2026, 9, 4), date(2026, 9, 8)] and not kept.vxn.isna().any()
    assert IV.on_sessions(pd.DataFrame(), lambda d: True).empty
