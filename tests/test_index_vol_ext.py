"""G10: CBOE VVIX/SKEW parsing (a different CSV shape than index_vol.py's), the two ratio columns
read from the base index_vol table, merge, and the no-network loader (RESEARCH/47-edge-gaps §2)."""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd
import pytest

from engine.mart import index_vol as IV
from engine.mart import index_vol_ext as EXT

pytestmark = pytest.mark.unit

CSV_VVIX = "DATE,VVIX\n09/02/2026,86.25\n09/03/2026,83.80\n09/04/2026,84.42\n"
CSV_SKEW = "DATE,SKEW\n09/02/2026,144.12\n09/04/2026,151.58\n"

BASE = IV.normalize(pd.DataFrame({
    "date": ["2026-09-02", "2026-09-03", "2026-09-04"],
    "vix": [15.0, 14.5, 14.53],
    "vix3m": [17.5, 17.4, 17.61],
    "vxn": [20.0, 19.8, 20.04],
    "vix9d": [13.5, 12.9, 12.85],
}))


def test_parse_cboe_value_csv_reads_the_index_named_value_column():
    df = EXT.parse_cboe_value_csv(CSV_VVIX, "VVIX")
    assert list(df.columns) == ["date", "vvix"]
    assert df.date.tolist() == [date(2026, 9, 2), date(2026, 9, 3), date(2026, 9, 4)]
    assert df.vvix.tolist() == pytest.approx([86.25, 83.80, 84.42])


def test_parse_cboe_value_csv_rejects_unknown_index_or_missing_columns():
    with pytest.raises(ValueError):
        EXT.parse_cboe_value_csv(CSV_VVIX, "VIX")  # VIX is index_vol.py's shape, not this module's
    with pytest.raises(ValueError):
        EXT.parse_cboe_value_csv("DATE,CLOSE\n09/02/2026,86.25\n", "VVIX")


def test_add_ratios_divides_the_base_columns_and_is_nan_safe():
    ratios = EXT.add_ratios(BASE)
    row = ratios[ratios.date == date(2026, 9, 4)].iloc[0]
    assert row.vix9d_vix_ratio == pytest.approx(12.85 / 14.53)
    assert row.vix_vix3m_ratio == pytest.approx(14.53 / 17.61)
    zero_vix3m = IV.normalize(pd.DataFrame({"date": ["2026-09-05"], "vix": [15.0], "vix3m": [0.0],
                                            "vxn": [20.0], "vix9d": [13.0]}))
    out = EXT.add_ratios(zero_vix3m).iloc[0]
    assert np.isnan(out.vix_vix3m_ratio) and out.vix9d_vix_ratio == pytest.approx(13.0 / 15.0)
    assert EXT.add_ratios(pd.DataFrame()).empty


def test_merge_ext_is_an_outer_join_with_every_column_present():
    vvix = EXT.parse_cboe_value_csv(CSV_VVIX, "VVIX")
    skew = EXT.parse_cboe_value_csv(CSV_SKEW, "SKEW")
    merged = EXT.merge_ext(vvix, skew, EXT.add_ratios(BASE))
    assert list(merged.columns) == EXT.COLUMNS
    assert len(merged) == 3
    row = merged[merged.date == date(2026, 9, 3)].iloc[0]
    assert row.vvix == pytest.approx(83.80) and pd.isna(row["skew"])
    assert row.vix9d_vix_ratio == pytest.approx(12.9 / 14.5)
    assert merged.date.is_monotonic_increasing


def test_load_prefers_the_mart_file_then_the_fallback_then_empty(tmp_path):
    mart = tmp_path / "index_vol_ext.parquet"
    fallback = tmp_path / "fallback.parquet"
    assert EXT.load_index_vol_ext(str(mart), str(fallback)).empty
    EXT.normalize(pd.DataFrame({"date": ["2026-09-04"], "vvix": [84.42], "skew": [151.58],
                                "vix9d_vix_ratio": [0.884], "vix_vix3m_ratio": [0.825]})).to_parquet(fallback, index=False)
    assert EXT.latest_date(EXT.load_index_vol_ext(str(mart), str(fallback))) == date(2026, 9, 4)
    EXT.write_index_vol_ext(EXT.normalize(pd.DataFrame({"date": ["2026-09-08"], "vvix": [85.0], "skew": [150.0],
                                                        "vix9d_vix_ratio": [0.9], "vix_vix3m_ratio": [0.83]})), str(mart))
    assert EXT.latest_date(EXT.load_index_vol_ext(str(mart), str(fallback))) == date(2026, 9, 8)


def test_refresh_fetches_vvix_and_skew_and_computes_ratios_from_the_passed_base_without_network(tmp_path):
    texts = {"VVIX": CSV_VVIX, "SKEW": CSV_SKEW}
    out = EXT.refresh(str(tmp_path / "ext.parquet"), fetch_text=lambda index: texts[index], base_index_vol=BASE)
    assert EXT.latest_date(out) == date(2026, 9, 4)
    row = out[out.date == date(2026, 9, 4)].iloc[0]
    assert row["skew"] == pytest.approx(151.58) and row.vix_vix3m_ratio == pytest.approx(14.53 / 17.61)
    assert (tmp_path / "ext.parquet").exists() and not (tmp_path / "ext.parquet.tmp").exists()


def test_refresh_never_writes_to_the_base_index_vol_file(tmp_path):
    """G10 constraint: this module must never touch data/mart/index_vol/."""
    base_path = tmp_path / "index_vol" / "index_vol.parquet"
    IV.write_index_vol(BASE, str(base_path))
    before = base_path.read_bytes()
    EXT.refresh(str(tmp_path / "ext.parquet"), fetch_text=lambda index: {"VVIX": CSV_VVIX, "SKEW": CSV_SKEW}[index],
               base_index_vol=IV.load_index_vol(str(base_path)))
    assert base_path.read_bytes() == before
