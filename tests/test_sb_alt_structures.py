"""engine.validation.sb_alt_structures: the descriptive re-pricing of structures S-B does not
trade, on the proxy's own IC rows. Hand-checked against `sb_proxy.proxy_position`."""
from __future__ import annotations

import math
from datetime import date

import numpy as np
import pandas as pd
import pytest

from engine.config import SB_PARAMS, SB_SIZING
from engine.strategies import sb_proxy as P
from engine.validation import sb_alt_structures as A

pytestmark = pytest.mark.unit


def _ic_row(close: float, x: float = 20.0, spot: float = 100.0) -> pd.Series:
    row = P.proxy_position("SPY", "IC", date(2026, 7, 10), date(2026, 7, 31), spot, x, close, SB_PARAMS, SB_SIZING)
    return pd.Series(row)


def _as_tuple(row: pd.Series):
    return next(pd.DataFrame([row]).itertuples(index=False))


def test_ps_recomputed_matches_the_proxy_row_own_ror():
    for close in (92.0, 80.0, 104.0):
        row = _ic_row(close)
        ps = P.proxy_position("SPY", "PS", date(2026, 7, 10), date(2026, 7, 31), 100.0, 20.0, close, SB_PARAMS, SB_SIZING)
        ours = A.structure_row(_as_tuple(row), "PS")
        assert ours["pnl_usd"] == pytest.approx(ps["net_usd"] / ps["contracts"])
        assert ours["risk_usd"] == pytest.approx(ps["max_loss_usd"])
        assert ours["ror"] == pytest.approx(ps["ror"])


def test_put_spread_plus_call_spread_is_the_iron_condor_per_contract():
    row = _ic_row(100.0)
    t = _as_tuple(row)
    ps, cs = A.structure_row(t, "PS"), A.structure_row(t, "CS")
    assert ps["pnl_usd"] + cs["pnl_usd"] == pytest.approx(row["net_usd"] / row["contracts"])


def test_long_leg_risk_is_the_premium_and_an_expiring_worthless_leg_loses_it_all_plus_costs():
    t = _as_tuple(_ic_row(100.0))               # settles at spot: every leg expires worthless
    for name in ("long_c1", "long_p1", "long_c2", "long_p2"):
        r = A.structure_row(t, name)
        assert r["risk_usd"] == pytest.approx(r["premium_usd"]) and r["premium_usd"] > 0
        assert r["pnl_usd"] < -r["premium_usd"]     # premium gone plus half-spread and two commissions
        assert r["ror"] < -1.0 and math.isnan(r["margin_usd"])


def test_naked_put_risk_is_the_two_sigma_stress_loss_and_margin_is_reported_beside():
    t = _as_tuple(_ic_row(92.0))
    naked, ps = A.structure_row(t, "short_p1_naked"), A.structure_row(t, "PS")
    assert naked["risk_usd"] == pytest.approx(ps["risk_usd"])          # the spread's max loss at the same strikes
    assert naked["pnl_usd"] > ps["pnl_usd"]                             # no wing to pay for, settle inside the wing
    assert naked["margin_usd"] > naked["risk_usd"]                      # Reg-T proxy: (20% x 100 - 5) x 100 - premium
    assert naked["margin_usd"] == pytest.approx((0.20 * 100.0 - 5.0) * 100 + naked["premium_usd"])


def test_beyond_the_wing_the_naked_put_loses_more_than_the_spread():
    t = _as_tuple(_ic_row(80.0))
    naked, ps = A.structure_row(t, "short_p1_naked"), A.structure_row(t, "PS")
    assert naked["pnl_usd"] < ps["pnl_usd"] and naked["ror"] < -1.0


def test_alt_structure_table_covers_both_sets_and_every_structure():
    rows = []
    for i, close in enumerate((92.0, 100.0, 104.0, 97.0)):
        r = _ic_row(close)
        r["entry"], r["expiry"] = date(2026, 7, 3) + pd.Timedelta(days=7 * i).to_pytimedelta(), date(2026, 7, 24) + pd.Timedelta(days=7 * i).to_pytimedelta()
        rows.append({**r.to_dict(), "sensitivity": "gate_off"})
        if i % 2 == 0:
            rows.append({**r.to_dict(), "sensitivity": "base"})
    sens = pd.DataFrame(rows)
    tab = A.alt_structure_table(sens)
    assert list(tab.columns) == A.TABLE_COLS
    assert set(tab["set"]) == {"gate ON", "every Friday"} and set(tab["structure"]) == set(A.ALT_STRUCTURES)
    assert tab[(tab.set == "every Friday") & (tab.structure == "PS")]["n"].iloc[0] == 4
    assert tab[(tab.set == "gate ON") & (tab.structure == "PS")]["n"].iloc[0] == 2
    assert tab["mean_margin_usd"].notna().sum() == 4                     # the two naked structures x two sets


def test_alt_structure_table_is_empty_without_sensitivities():
    assert A.alt_structure_table(pd.DataFrame()).empty
    assert A.alt_structure_table(pd.DataFrame({"structure": ["IC"]})).empty
    assert np.isnan(A.structure_row(_as_tuple(_ic_row(100.0)), "CS")["margin_usd"])
