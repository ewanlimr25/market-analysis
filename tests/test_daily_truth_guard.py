"""The last nightly of the week refuses a truth set that does not reach it (findings market-analysis D40)."""
from __future__ import annotations

import os
from datetime import date

import pandas as pd
import pytest

from engine import daily

pytestmark = pytest.mark.unit

FRI, MON = date(2026, 11, 6), date(2026, 11, 2)
THU_BEFORE_HOLIDAY = date(2026, 7, 2)   # 2026-07-03 is an NYSE holiday


def _write_truth_set(data_dir, rows: list[tuple[str, date]], sets=("prices", "returns", "features")) -> str:
    frame = pd.DataFrame([{"ticker": t, "date": d, "close": 1.0} for t, d in rows])
    for name in sets:
        frame.to_parquet(os.path.join(data_dir, f"{name}.parquet"), index=False)
    return str(data_dir)


def _both(d: date) -> list[tuple[str, date]]:
    return [("SPY", d), ("QQQ", d)]


@pytest.mark.parametrize("d, expected", [
    (FRI, True),
    (THU_BEFORE_HOLIDAY, True),
    (MON, False),
    (date(2026, 11, 5), False),         # an ordinary Thursday
    (date(2026, 11, 25), False),        # the Wednesday before Thanksgiving: Friday still opens
])
def test_last_session_of_week(d, expected):
    assert daily.is_last_session_of_week(d) is expected


def test_nothing_behind_when_all_three_sets_reach_the_session(tmp_path):
    assert daily.truth_set_behind(FRI, _write_truth_set(tmp_path, _both(FRI))) == []


def test_a_set_ending_before_the_session_is_named(tmp_path):
    data = _write_truth_set(tmp_path, _both(date(2026, 10, 30)))
    assert daily.truth_set_behind(FRI, data) == [
        "prices.parquet: QQQ ends 2026-10-30", "prices.parquet: SPY ends 2026-10-30",
        "returns.parquet: QQQ ends 2026-10-30", "returns.parquet: SPY ends 2026-10-30",
        "features.parquet: QQQ ends 2026-10-30", "features.parquet: SPY ends 2026-10-30",
    ]


def test_other_names_reaching_the_session_do_not_clear_a_stale_spy(tmp_path):
    """The preflight's max(date) across all tickers cleared this exact state (2026-07: eight backfilled names)."""
    rows = [("SPY", date(2026, 11, 5)), ("QQQ", FRI), ("AAPL", FRI)]
    behind = daily.truth_set_behind(FRI, _write_truth_set(tmp_path, rows))
    assert behind == [f"{name}.parquet: SPY ends 2026-11-05" for name in ("prices", "returns", "features")]


def test_a_benchmark_with_no_rows_and_a_missing_file_are_both_behind(tmp_path):
    data = _write_truth_set(tmp_path, [("SPY", FRI)], sets=("prices", "returns"))
    assert daily.truth_set_behind(FRI, data) == [
        "prices.parquet: QQQ has no rows", "returns.parquet: QQQ has no rows", "features.parquet missing",
    ]


def test_a_truth_set_past_the_session_does_not_block_a_rerun(tmp_path):
    assert daily.truth_set_behind(FRI, _write_truth_set(tmp_path, _both(date(2026, 11, 13)))) == []


@pytest.fixture
def nightly(monkeypatch, tmp_path):
    """`main` with `run_daily` replaced: records whether the nightly started, and points the guard at tmp_path."""
    started: list[date] = []

    def fake_run_daily(d, *args, **kwargs):
        started.append(d)
        return {"candidates": [], "suppressed": [], "graded": [], "watch_basket": {}}

    monkeypatch.setattr(daily, "run_daily", fake_run_daily)
    monkeypatch.setattr(daily.SCH, "validate", lambda signals: [])
    monkeypatch.setattr(daily, "DATA", str(tmp_path))

    def invoke(*argv: str) -> int:
        monkeypatch.setattr("sys.argv", ["engine.daily", *argv])
        return daily.main()

    return started, invoke, tmp_path


def test_friday_on_a_stale_truth_set_stops_before_the_nightly_starts(nightly, capsys):
    started, invoke, data = nightly
    _write_truth_set(data, _both(date(2026, 10, 30)))
    assert invoke("--date", FRI.isoformat()) == 2
    assert started == []
    err = capsys.readouterr().err
    assert "prices.parquet: SPY ends 2026-10-30" in err
    assert "build_prices.py" in err and "--allow-stale-truth" in err


def test_friday_on_a_fresh_truth_set_runs(nightly):
    started, invoke, data = nightly
    _write_truth_set(data, _both(FRI))
    assert invoke("--date", FRI.isoformat()) == 0
    assert started == [FRI]


def test_the_override_runs_the_nightly_and_says_so(nightly, capsys):
    started, invoke, data = nightly
    _write_truth_set(data, _both(date(2026, 10, 30)))
    assert invoke("--date", FRI.isoformat(), "--allow-stale-truth") == 0
    assert started == [FRI]
    assert "last print" in capsys.readouterr().err


def test_monday_to_thursday_a_stale_truth_set_still_runs(nightly):
    started, invoke, data = nightly
    _write_truth_set(data, _both(date(2026, 10, 30)))
    assert invoke("--date", MON.isoformat()) == 0
    assert started == [MON]
