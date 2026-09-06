"""Q2: the S-B gate (DESIGN/80 §2): G1 contango, G2 level above the 20-session median, both read
at the prior session's close; UNKNOWN fails closed."""
from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from engine.config import SB_PARAMS
from engine.strategies import sb_gate as G

pytestmark = pytest.mark.unit


def _sessions(n: int, start: date = date(2026, 6, 1)) -> list[date]:
    out, d = [], start
    while len(out) < n:
        if d.weekday() < 5:
            out.append(d)
        d += timedelta(days=1)
    return out


def _frame(vix, vix3m=None, vxn=None, n=None):
    n = n or len(vix)
    days = _sessions(n)
    vix3m = vix3m if vix3m is not None else [v + 2 for v in vix]
    vxn = vxn if vxn is not None else [v + 5 for v in vix]
    return pd.DataFrame({"date": days, "vix": vix, "vix3m": vix3m, "vxn": vxn, "vix9d": vix})


def test_on_when_contango_and_level_above_the_median_of_the_prior_twenty():
    vix = [15.0] * 20 + [16.0]            # rows 0..19 = window, row 20 = prev (t-1)
    df = _frame(vix)
    t, prev = date(2026, 7, 1), df.date.iloc[20]
    st = G.gate(df, t, prev, "vix", SB_PARAMS)
    assert st.known and st.on and st.reason == "ON"
    assert st.asof == prev and st.vix == 16.0 and st.x_median == 15.0 and st.contango and st.level_ok


def test_off_on_backwardation_or_flat_term_structure():
    df = _frame([15.0] * 20 + [16.0], vix3m=[17.0] * 20 + [16.0])       # equality is not contango
    st = G.gate(df, date(2026, 7, 1), df.date.iloc[20], "vix", SB_PARAMS)
    assert st.known and not st.on and st.reason == "OFF:G1" and st.level_ok is True


def test_off_when_level_is_at_or_below_the_median_strictly():
    df = _frame([15.0] * 20 + [15.0])
    st = G.gate(df, date(2026, 7, 1), df.date.iloc[20], "vix", SB_PARAMS)
    assert not st.on and st.reason == "OFF:G2"
    df = _frame([15.0] * 20 + [14.0], vix3m=[14.0] * 21)
    assert G.gate(df, date(2026, 7, 1), df.date.iloc[20], "vix", SB_PARAMS).reason == "OFF:G1,G2"


def test_window_excludes_prev_itself_and_anything_on_or_after_t():
    # 20 prior rows at 15, prev at 30, and a row on t at 100: median must be 15 (prev and t excluded)
    vix = [15.0] * 20 + [30.0, 100.0]
    df = _frame(vix)
    prev, t = df.date.iloc[20], df.date.iloc[21]
    st = G.gate(df, t, prev, "vix", SB_PARAMS)
    assert st.x_median == 15.0 and st.on
    # if the window wrongly included prev, the median of [15]*20+[30] would still be 15, so also
    # test a window whose median moves when prev is included: 10 rows at 10, 10 rows at 20, prev at 20
    df = _frame([10.0] * 10 + [20.0] * 10 + [20.0])
    st = G.gate(df, date(2026, 7, 1), df.date.iloc[20], "vix", SB_PARAMS)
    assert st.x_median == 15.0 and st.level_ok


def test_unknown_when_prev_row_is_missing_or_the_window_is_short_or_has_nulls():
    df = _frame([15.0] * 20 + [16.0])
    st = G.gate(df, date(2026, 7, 1), date(2026, 6, 30), "vix", SB_PARAMS)      # 06-30 is not the frame's prev row? it is; use a missing date
    missing = df[df.date != df.date.iloc[20]]
    st = G.gate(missing, date(2026, 7, 1), df.date.iloc[20], "vix", SB_PARAMS)
    assert not st.known and not st.on and st.reason.startswith("UNKNOWN")
    short = _frame([15.0] * 10 + [16.0])
    st = G.gate(short, date(2026, 7, 1), short.date.iloc[10], "vix", SB_PARAMS)
    assert not st.known and "window" in st.reason
    nulls = _frame([15.0] * 20 + [16.0])
    nulls.loc[3, "vix"] = np.nan
    assert not G.gate(nulls, date(2026, 7, 1), nulls.date.iloc[20], "vix", SB_PARAMS).known
    nulls = _frame([15.0] * 20 + [16.0])
    nulls.loc[20, "vix3m"] = np.nan
    assert not G.gate(nulls, date(2026, 7, 1), nulls.date.iloc[20], "vix", SB_PARAMS).known


def test_qqq_uses_vxn_for_the_level_and_vix_term_structure_for_contango():
    vix = [15.0] * 21                                           # VIX flat: G2 on VIX would be OFF
    vxn = [20.0] * 20 + [22.0]                                  # VXN rose: G2 on VXN is ON
    df = _frame(vix, vxn=vxn)
    st = G.gate(df, date(2026, 7, 1), df.date.iloc[20], "vxn", SB_PARAMS)
    assert st.on and st.x == 22.0 and st.x_median == 20.0 and st.vix == 15.0 and st.vix3m == 17.0
    assert not G.gate(df, date(2026, 7, 1), df.date.iloc[20], "vix", SB_PARAMS).on


def test_gate_mode_selects_which_conditions_count():
    df = _frame([15.0] * 20 + [16.0], vix3m=[14.0] * 21)        # G1 off, G2 on
    st = G.gate(df, date(2026, 7, 1), df.date.iloc[20], "vix", SB_PARAMS)
    assert G.is_on(st, "both") is False and G.is_on(st, "g1") is False and G.is_on(st, "g2") is True and G.is_on(st, "off") is True
    unknown = G.gate(df.iloc[:5], date(2026, 7, 1), df.date.iloc[20], "vix", SB_PARAMS)
    assert G.is_on(unknown, "off") is False                     # unknown fails closed in every mode
