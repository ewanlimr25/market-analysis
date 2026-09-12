"""engine.research.sc_rv5: forward RV5 windows, the earnings flag and the strata table on synthetic frames."""
from __future__ import annotations

import math
from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from engine.research import sc_rv5 as R

pytestmark = pytest.mark.unit

SESSIONS = [date(2026, 3, 2) + timedelta(days=i) for i in range(60) if (date(2026, 3, 2) + timedelta(days=i)).weekday() < 5]


def _rv(ticker: str, dates, rv5=1e-4, c2c=0.01) -> pd.DataFrame:
    return pd.DataFrame({"ticker": ticker, "date": list(dates), "rv5": rv5, "close_to_close_ret": c2c})


def test_forward_windows_need_consecutive_quality_sessions_and_annualise_like_g7():
    rv = pd.concat([_rv("AAA", SESSIONS), _rv("BBB", [d for d in SESSIONS if d != SESSIONS[5]])])
    w = R.forward_windows(rv, window=4)
    aaa = w[w.ticker == "AAA"]
    assert len(aaa) == len(SESSIONS) - 4 and aaa["T"].iloc[0] == SESSIONS[0]
    assert aaa["rv5_fwd"].iloc[0] == pytest.approx(math.sqrt(4 * 1e-4 * 252 / 4))
    assert aaa["c2c_fwd"].iloc[0] == pytest.approx(0.0)                                   # constant returns
    bbb = w[w.ticker == "BBB"]
    assert SESSIONS[1] not in set(bbb["T"]) and SESSIONS[2] not in set(bbb["T"])            # the gap at index 5 breaks these
    assert SESSIONS[6] in set(bbb["T"])
    assert R.forward_windows(pd.DataFrame()).empty


def test_assemble_flags_earnings_inside_the_window_and_keeps_common_and_adr_only():
    w = R.forward_windows(_rv("AAA", SESSIONS, rv5=2e-4, c2c=0.02), window=5)
    scr = pd.DataFrame({"date": w["T"], "ticker": "AAA", "iv30d": 0.5, "marketcap": 5e9, "sector": "Energy", "issue_type": "Common Stock"})
    scr.loc[scr.index[0], "issue_type"] = "ETF"
    earnings = pd.DataFrame({"ticker": ["AAA"], "E": [SESSIONS[10]]})
    df = R.assemble(w, scr, earnings, SESSIONS, window=5)
    assert len(df) == len(w) - 1
    flagged = set(df[df.earnings_in_window]["T"])
    assert flagged == set(SESSIONS[5:10])                                                 # T in [E-5, E-1]
    assert df["vrp_rv5"].iloc[0] == pytest.approx((0.5 - math.sqrt(2e-4 * 252)) * 100)
    assert df["month"].iloc[0] == "2026-03"


def test_strata_table_reports_bands_and_the_joint_sc_band():
    rng = np.random.default_rng(1)
    n = 400
    df = pd.DataFrame({"ticker": [f"T{i%40}" for i in range(n)], "T": [SESSIONS[i % 40] for i in range(n)],
                       "rv5_fwd": rng.uniform(0.2, 0.6, n), "c2c_fwd": rng.uniform(0.3, 0.7, n),
                       "iv30d": rng.uniform(0.1, 1.0, n), "marketcap": rng.choice([5e8, 5e9, 5e10], n),
                       "sector": "X", "earnings_in_window": rng.random(n) < 0.2})
    df["vrp_rv5"] = (df.iv30d - df.rv5_fwd) * 100
    df["vrp_c2c"] = (df.iv30d - df.c2c_fwd) * 100
    df["month"] = [f"{d.year}-{d.month:02d}" for d in df["T"]]
    tab = R.strata_table(df)
    assert list(tab.columns) == R.TABLE_COLS
    names = list(tab["stratum"])
    assert names[:2] == ["all windows", "earnings-free"] and "earnings-free, F3 and F6 (the S-C band)" in names
    assert any("mcap $1B to $20B (F3)" in s for s in names) and any("iv30d 30% to 80% (F6)" in s for s in names)
    free = tab[tab.stratum == "earnings-free"].iloc[0]
    assert free["n"] == int((~df.earnings_in_window).sum()) and 0 <= free["iv_gt_rv5"] <= 1
    assert R.strata_table(pd.DataFrame()).empty
