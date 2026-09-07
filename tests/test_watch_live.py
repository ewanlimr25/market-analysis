"""engine.watch.live: the R2 nightly's live replacements for the five conditions R1 computed from
`features.parquet` (results.md §5) -- pct_52w_range, the 5-day net call-OI build, unsigned
total-premium/marketcap crowding, the 5-day IV-rank change, and screener-spine closes for grading.
Every source is exercised on synthetic files under `tmp_path`; nothing here touches the real mart
or `~/Documents/Stocks`."""
from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from engine.watch import live as LV

pytestmark = pytest.mark.unit

D = date(2026, 6, 9)


# ---- pct_52w_range ----------------------------------------------------------------------------

def test_pct_52w_range_matches_chart_pys_formula():
    assert LV.pct_52w_range(75.0, 100.0, 50.0) == pytest.approx(0.5)
    assert LV.pct_52w_range(100.0, 100.0, 50.0) == pytest.approx(1.0)
    assert LV.pct_52w_range(50.0, 100.0, 50.0) == pytest.approx(0.0)


def test_pct_52w_range_none_on_missing_or_degenerate_inputs():
    assert LV.pct_52w_range(None, 100.0, 50.0) is None
    assert LV.pct_52w_range(75.0, None, 50.0) is None
    assert LV.pct_52w_range(75.0, 100.0, None) is None
    assert LV.pct_52w_range(75.0, float("nan"), 50.0) is None
    assert LV.pct_52w_range(75.0, 50.0, 50.0) is None       # high <= low
    assert LV.pct_52w_range(75.0, 40.0, 50.0) is None       # high < low


def test_add_pct_52w_range_adds_a_column_row_by_row():
    df = pd.DataFrame({"close": [75.0, None], "week_52_high": [100.0, 100.0], "week_52_low": [50.0, 50.0]})
    out = LV.add_pct_52w_range(df)
    vals = out["pct_52w_range"].tolist()
    assert vals[0] == pytest.approx(0.5)
    assert pd.isna(vals[1])            # missing close -> null (NaN once assigned into a float column)


# ---- 5-day net call-OI build -------------------------------------------------------------------

def _oi_row(ticker, call_symbol_dte="261120C00020000", oi_diff=100):
    return {"underlying_symbol": ticker, "option_symbol": f"{ticker}{call_symbol_dte}", "oi_diff_plain": oi_diff}


def _write_oi_file(directory, d, rows):
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"chain-oi-changes-{d.isoformat()}.parquet"
    pd.DataFrame(rows).to_parquet(path, index=False)
    return path


def test_oi_net_5d_nets_call_minus_put_across_the_trailing_window(tmp_path):
    oi_dir = tmp_path / "OI changes"
    for i, d in enumerate([date(2026, 6, 3), date(2026, 6, 4), date(2026, 6, 5), date(2026, 6, 8), D]):
        rows = [
            {"underlying_symbol": "ABC", "option_symbol": "ABC261120C00020000", "oi_diff_plain": 100 + i},
            {"underlying_symbol": "ABC", "option_symbol": "ABC261120P00020000", "oi_diff_plain": 10},
        ]
        _write_oi_file(oi_dir, d, rows)
    out = LV.oi_net_5d_for_day(D, str(tmp_path))
    # daily net = call - put = (100+i) - 10 for i in 0..4 -> mean = 100+2-10 = 92
    assert out.set_index("ticker").loc["ABC", "oi_net_5d"] == pytest.approx(92.0)


def test_oi_net_5d_empty_when_no_file_in_the_window(tmp_path):
    out = LV.oi_net_5d_for_day(D, str(tmp_path))
    assert out.empty
    assert list(out.columns) == ["ticker", "oi_net_5d"]


def test_available_oi_dates_parses_filenames_and_ignores_junk(tmp_path):
    oi_dir = tmp_path / "OI changes"
    oi_dir.mkdir()
    (oi_dir / "chain-oi-changes-2026-06-01.parquet").write_bytes(b"")
    (oi_dir / "chain-oi-changes-2026-06-02.parquet").write_bytes(b"")
    (oi_dir / "not-a-panel-file.parquet").write_bytes(b"")
    assert LV.available_oi_dates(str(tmp_path)) == [date(2026, 6, 1), date(2026, 6, 2)]


def test_oi_window_dates_caps_at_five_and_respects_the_asof_date(tmp_path):
    oi_dir = tmp_path / "OI changes"
    oi_dir.mkdir()
    days = [date(2026, 6, d) for d in range(1, 9)]
    for d in days:
        (oi_dir / f"chain-oi-changes-{d.isoformat()}.parquet").write_bytes(b"")
    window = LV.oi_window_dates(date(2026, 6, 6), str(tmp_path))
    assert window == [date(2026, 6, 2), date(2026, 6, 3), date(2026, 6, 4), date(2026, 6, 5), date(2026, 6, 6)]


# ---- unsigned total premium / marketcap --------------------------------------------------------

def _prem_row(ticker, premium, canceled=False):
    return {"underlying_symbol": ticker, "premium": premium, "canceled": canceled}


def test_total_premium_sums_unsigned_both_sides(tmp_path):
    path = tmp_path / "opts.parquet"
    rows = [_prem_row("ABC", 1_000_000.0), _prem_row("ABC", 500_000.0), _prem_row("ABC", 2_000_000.0, canceled=True),
            _prem_row("XYZ", 250.0)]
    pd.DataFrame(rows).to_parquet(path, index=False)
    out = LV.total_premium_for_day(str(path))
    got = dict(zip(out.ticker, out.tot_prem))
    assert got == {"ABC": pytest.approx(1_500_000.0), "XYZ": pytest.approx(250.0)}


def test_total_premium_missing_file_is_empty(tmp_path):
    out = LV.total_premium_for_day(str(tmp_path / "missing.parquet"))
    assert out.empty and list(out.columns) == ["ticker", "tot_prem"]


# ---- decile_flag --------------------------------------------------------------------------------

def test_decile_flag_flags_top_decile_and_nulls_missing_values():
    s = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, None])
    flag = LV.decile_flag(s)
    assert flag.iloc[9] is None
    assert flag.iloc[8] is True             # the single largest non-null value
    assert all(v is False for v in flag.iloc[:8])


# ---- 5-day IV-rank change ------------------------------------------------------------------------

def test_ivrank_chg_5d_is_none_without_a_prior_screener_row(monkeypatch):
    def fake_panel(dates, stocks_dir=None):
        rows = [{"ticker": "ABC", "date": D, "iv_rank": 60.0}]
        return pd.DataFrame(rows)
    monkeypatch.setattr(LV, "load_screener_panel", fake_panel)
    out = LV.build_ivrank_chg_5d([D])
    row = out[out.ticker == "ABC"].iloc[0]
    assert pd.isna(row["ivrank_chg_5d"])


def test_ivrank_chg_5d_computes_the_delta_against_five_sessions_earlier(monkeypatch):
    from engine import calendar as cal
    prev = cal.prev_session(D, 5)

    def fake_panel(dates, stocks_dir=None):
        rows = [{"ticker": "ABC", "date": D, "iv_rank": 60.0},
                {"ticker": "ABC", "date": prev, "iv_rank": 45.0}]
        return pd.DataFrame(rows)
    monkeypatch.setattr(LV, "load_screener_panel", fake_panel)
    out = LV.build_ivrank_chg_5d([D])
    row = out[out.ticker == "ABC"].iloc[0]
    assert row["ivrank_chg_5d"] == pytest.approx(15.0)


# ---- closes for grading -------------------------------------------------------------------------

def test_load_closes_reads_exactly_the_asked_for_pairs(monkeypatch):
    import duckdb

    class _FakeCon:
        def execute(self, q, *a):
            self._q = q
            return self

        def df(self):
            return pd.DataFrame({"ticker": ["ABC", "SPY"], "date": [D, D], "close": [12.5, 500.0]})

    monkeypatch.setattr(duckdb, "connect", lambda: _FakeCon())
    out = LV.load_closes(["ABC", "SPY"], [D])
    assert out == {("ABC", D): 12.5, ("SPY", D): 500.0}


def test_load_closes_empty_inputs_short_circuit():
    assert LV.load_closes([], [D]) == {}
    assert LV.load_closes(["ABC"], []) == {}
