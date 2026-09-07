"""G4/G5 exploration row generator (RESEARCH/47 §2 G4/G5; DESIGN/100 §2-3): paper rows for the top
and bottom decile of every cross-sectional factor, entered on every formation Friday the panel
computes a week for, ten names a side, equal-weighted, one-week hold. There is no gate to audit
here (`gate_verdict` records the factor:side instead, per DESIGN/100 §3's contract that every row
carries the verdict the engine printed that night) -- this strategy starts life entirely in the
exploration book, per RESEARCH/47's "enters as exploration rows" instruction, and only reaches a
champion role if an adjudicated challenger promotes it (DESIGN/100 §5).

Not wired into `make daily`; `scripts/xs_rows.py` is a dry run that prints rows and never writes to
`ledger/`. No I/O in this module -- `build_rows` takes one formation week's factor table (as
`engine.research.cross_section.build_week_factors` returns it) and returns rows in memory;
`grade_rows` takes an injectable outcome lookup so tests never touch the panel.

Trading direction bakes in the pre-registered hypothesis sign (RESEARCH/30 §1): a positive IV
spread (and its one-week change) predicts a positive return, so the top decile is long; a high put
skew or a high O/S ratio predicts a negative return (Xing-Zhang-Zhao, Johnson-So), so the top decile
is short there instead. `FACTOR_SIGN[factor]` is the return sign predicted for the *top* decile;
the bottom decile always takes the opposite side.
"""
from __future__ import annotations

from typing import Callable

import pandas as pd

from engine import policy as POL
from engine.research.cross_section import FACTOR_COLS

POLICY_ID = "xs-1.0"
N_PER_SIDE = 10
WEIGHT = 1.0 / N_PER_SIDE
SIDE_TOP, SIDE_BOTTOM = "top", "bottom"
SIDES = (SIDE_TOP, SIDE_BOTTOM)
DIRECTION_LONG, DIRECTION_SHORT = "long", "short"

# Predicted return sign of the TOP decile, one entry per pre-registered factor (RESEARCH/30 §1).
FACTOR_SIGN: dict[str, int] = {"iv_spread": +1, "d_iv_spread": +1, "put_skew": -1, "os_ratio": -1}

KEY = ["formation_date", "factor", "side", "ticker", "policy_id", "role"]
ROW_COLUMNS = ["formation_date", "factor", "side", "direction", "rank", "ticker", "factor_value",
               "weight", "policy_id", "role", "gate_verdict"]


def _direction(factor: str, side: str) -> str:
    sign = FACTOR_SIGN[factor] if side == SIDE_TOP else -FACTOR_SIGN[factor]
    return DIRECTION_LONG if sign > 0 else DIRECTION_SHORT


def _row(formation_date, factor: str, side: str, rank: int, ticker: str, factor_value: float) -> dict:
    base = {"formation_date": formation_date, "factor": factor, "side": side,
            "direction": _direction(factor, side), "rank": rank, "ticker": ticker,
            "factor_value": float(factor_value), "weight": WEIGHT}
    return POL.stamp(base, POLICY_ID, POL.ROLE_EXPLORATION, gate_verdict=f"{factor}:{side}")


def _decile_rows(week: pd.DataFrame, factor: str, formation_date) -> list[dict]:
    """Top and bottom `N_PER_SIDE` names by `factor` (highest first for top). When fewer than
    `2 * N_PER_SIDE` names have a non-null factor value that week, both sides shrink to
    `len(sub) // 2` so a name never appears on both sides."""
    if factor not in week.columns:
        return []
    sub = week[["ticker", factor]].dropna().rename(columns={factor: "factor_value"})
    sub = sub.sort_values("factor_value", ascending=False).reset_index(drop=True)
    n_side = min(N_PER_SIDE, len(sub) // 2)
    if n_side == 0:
        return []
    rows = [_row(formation_date, factor, SIDE_TOP, i + 1, r["ticker"], r["factor_value"])
            for i, (_, r) in enumerate(sub.head(n_side).iterrows())]
    bottom = sub.tail(n_side).sort_values("factor_value").reset_index(drop=True)
    rows += [_row(formation_date, factor, SIDE_BOTTOM, i + 1, r["ticker"], r["factor_value"])
             for i, (_, r) in enumerate(bottom.iterrows())]
    return rows


def build_rows(week: pd.DataFrame, formation_date=None,
                factors: tuple[str, ...] = tuple(FACTOR_COLS)) -> pd.DataFrame:
    """Exploration rows for one formation week across every factor in `factors`."""
    if formation_date is None:
        formation_date = week["formation_date"].iloc[0] if "formation_date" in week.columns and len(week) else None
    rows = [r for f in factors for r in _decile_rows(week, f, formation_date)]
    out = pd.DataFrame(rows, columns=ROW_COLUMNS)
    if len(out):
        POL.require_policy_columns(out)
    return out


def check_key_unique(rows: pd.DataFrame) -> bool:
    """Whether every row is unique on `KEY` -- the invariant `engine.ledger` relies on to never
    pool two policies' rows together (DESIGN/100 §3)."""
    if rows is None or rows.empty:
        return True
    return not rows.duplicated(subset=KEY).any()


def grade_rows(rows: pd.DataFrame, outcome_lookup: Callable[[str, object], float | None]) -> pd.DataFrame:
    """Attach `next_week_excess` (from `outcome_lookup(ticker, formation_date)`) and
    `realized_excess` (`next_week_excess` signed by `direction`: short rows flip the sign)."""
    if rows is None or rows.empty:
        return pd.DataFrame(columns=list(ROW_COLUMNS) + ["next_week_excess", "realized_excess"])
    excess = rows.apply(lambda r: outcome_lookup(r["ticker"], r["formation_date"]), axis=1).astype(float)
    trade_sign = rows["direction"].map({DIRECTION_LONG: 1.0, DIRECTION_SHORT: -1.0})
    return rows.assign(next_week_excess=excess, realized_excess=excess * trade_sign)
