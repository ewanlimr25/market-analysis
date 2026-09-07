"""Policy identity on every ledger row (findings/market-analysis DESIGN/100 §2, §3; D22).

A row is produced by exactly one policy in one role. `policy_id` names the parameter set (the
champion's id is pinned beside the frozen parameters in `engine.config`; challengers are
registered under `ledger/challengers/`), `role` says whether the row belongs to the champion
book, a shadow challenger, or the exploration book that enters regardless of the gate, and
`gate_verdict` stores the gate code the engine printed that night so the gate itself can be
graded. Rows are never pooled across (policy_id, role): use `by_policy`.
"""
from __future__ import annotations

from typing import Iterator

import pandas as pd

ROLE_CHAMPION, ROLE_CHALLENGER, ROLE_EXPLORATION = "champion", "challenger", "exploration"
ROLES = (ROLE_CHAMPION, ROLE_CHALLENGER, ROLE_EXPLORATION)
POLICY_COLUMNS = ("policy_id", "role", "gate_verdict")
SA_GATE_PASS = "PASS"          # S-A has no vol gate: a champion row passed every filter F1..F8


def stamp(row: dict, policy_id: str, role: str, gate_verdict: str) -> dict:
    """A new row dict carrying the three policy columns."""
    if role not in ROLES:
        raise ValueError(f"role must be one of {ROLES}, got {role!r}")
    return {**row, "policy_id": policy_id, "role": role, "gate_verdict": gate_verdict}


def require_policy_columns(df: pd.DataFrame) -> None:
    """Raise ValueError unless every policy column is present and every role is known."""
    missing = [c for c in POLICY_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"ledger rows must carry {POLICY_COLUMNS}; missing {missing}")
    bad = sorted(set(df["role"].astype(str)) - set(ROLES))
    if bad:
        raise ValueError(f"unknown role {bad}; role must be one of {ROLES}")
    if df["policy_id"].isna().any() or (df["policy_id"].astype(str) == "").any():
        raise ValueError("policy_id must be non-empty on every ledger row")


def by_policy(df: pd.DataFrame) -> Iterator[tuple[tuple[str, str], pd.DataFrame]]:
    """Group by (policy_id, role); the only sanctioned way to aggregate ledger rows."""
    if df.empty:
        return iter(())
    return iter(df.groupby(["policy_id", "role"], sort=True))
