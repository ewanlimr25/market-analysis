"""Ledger rows for one sheet (findings/stock-deep-dive DESIGN/70 §6): the `sheet-1.0` row and, when
the owner passed `DIRECTION=`, the two `disc-1.0` rows. Pure: takes the section dicts and the
structure menu, returns frames for `engine.ledger.emit`; nothing here reads a file.

Roles (§6 table). `sheet-1.0` writes one IB row per `CAN_PRICE` sheet: `champion` when no S-C filter
and no X1 fired (`gate_verdict = PASS`), else `exploration` with `gate_verdict` = `X1` or the first
failing S-C filter. The exploration rows are the point: they grade S-C's own filters on every name
the owner looks at. `disc-1.0` writes the share line (entry = next open, stop X4, target = entry +
2 x stop distance) and the debit vertical, `role = exploration` always, `gate_verdict = PASS`, with
`context_read` stamped by the caller from file mtimes (`engine/name/context_tag.py`).

Row key (`engine.ledger.KEY`): `ticker, E, variant, structure, policy_id, role`; `variant` is
`sheet` for the sheet row and the direction for the owner's rows. `unit_id = "<ticker>:<post>"` is
the improvement process's unit for the sheet book (`engine/improve/spec.py`).
"""
from __future__ import annotations

import json
from datetime import date

import pandas as pd

from engine import calendar as cal
from engine import policy as POL
from engine.config import DISC_POLICY_ID, NAME_POLICY_ID
from engine.improve.spec import GATE_PASS

SHEET_VARIANT = "sheet"
SHEET_STRUCTURE = "IB"
SHARES, DEBIT_VERTICAL = "SHARES", "DEBIT_VERTICAL"
DISC_HORIZON_SESSIONS = 21          # §6: the share leg is graded at the 1-4 week horizon
LEG_SLOTS = 4


def _leg_columns(legs: list[dict]) -> dict:
    """`k1..k4`, `m1..m4`, `r1..r4`, `s1..s4` in strike order, padded with None; plus `legs_json`."""
    ordered = sorted(legs, key=lambda l: (l.get("strike") or 0.0, 0 if l.get("right") == "P" else 1))
    out: dict = {}
    for i in range(LEG_SLOTS):
        leg = ordered[i] if i < len(ordered) else {}
        out[f"k{i + 1}"] = leg.get("strike")
        out[f"m{i + 1}"] = leg.get("mark")
        out[f"r{i + 1}"] = leg.get("right")
        out[f"s{i + 1}"] = leg.get("side")
    out["legs_json"] = json.dumps(ordered, default=str)
    return out


def _find(structures: list[dict], family: str) -> dict | None:
    return next((s for s in structures if s.get("family") == family), None)


def sheet_gate(liquidity: dict, premium: dict) -> tuple[str, str] | None:
    """`(role, gate_verdict)` for the sheet row, or None when no row is written (CANNOT_PRICE)."""
    if not liquidity.get("can_price"):
        return None
    if premium.get("x1"):
        return POL.ROLE_EXPLORATION, "X1"
    sc = premium.get("sc") or {}
    if sc.get("pass"):
        return POL.ROLE_CHAMPION, GATE_PASS
    return POL.ROLE_EXPLORATION, str(sc.get("failing") or "SC")


def sheet_row(ticker: str, d: date, liquidity: dict, premium: dict, structures: list[dict]) -> dict | None:
    """The `sheet-1.0` IB row at one contract, or None (CANNOT_PRICE, or the IB is unpriced)."""
    gate = sheet_gate(liquidity, premium)
    ib = _find(structures, SHEET_STRUCTURE)
    if gate is None or ib is None or ib.get("mark") is None or not ib.get("expiry"):
        return None
    role, verdict = gate
    row = {"ticker": ticker, "E": d.isoformat(), "variant": SHEET_VARIANT, "structure": SHEET_STRUCTURE,
           "pre": d.isoformat(), "post": ib["expiry"], "expiry": ib["expiry"], "unit_id": f"{ticker}:{ib['expiry']}",
           "credit": ib.get("mark"), "max_loss": ib.get("max_loss"), "cost": ib.get("cost"), "n": 1,
           "mark_source": ib.get("mark_source"), "context_read": None, "direction": None,
           "entry": None, "stop": None, "target": None, **_leg_columns(ib.get("legs") or [])}
    return POL.stamp(row, NAME_POLICY_ID, role, verdict)


def disc_rows(ticker: str, d: date, direction: str, structures: list[dict], context_read: str) -> list[dict]:
    """The owner's two `disc-1.0` rows: the share line and the debit vertical (each only when priced)."""
    rows = []
    shares = _find(structures, SHARES)
    if shares is not None and shares.get("entry") is not None and shares.get("stop") is not None:
        post = cal.next_session(d, DISC_HORIZON_SESSIONS).isoformat()
        rows.append({"ticker": ticker, "E": d.isoformat(), "variant": direction, "structure": SHARES,
                     "pre": d.isoformat(), "post": post, "expiry": None, "unit_id": f"{ticker}:{d.isoformat()}",
                     "credit": None, "max_loss": shares.get("max_loss"), "cost": shares.get("cost"), "n": shares.get("n", 0),
                     "mark_source": shares.get("mark_source"), "context_read": context_read, "direction": direction,
                     "entry": shares["entry"], "stop": shares["stop"], "target": shares.get("target"),
                     **_leg_columns([])})
    vert = _find(structures, DEBIT_VERTICAL)
    if vert is not None and vert.get("mark") is not None and vert.get("expiry"):
        rows.append({"ticker": ticker, "E": d.isoformat(), "variant": direction, "structure": DEBIT_VERTICAL,
                     "pre": d.isoformat(), "post": vert["expiry"], "expiry": vert["expiry"],
                     "unit_id": f"{ticker}:{d.isoformat()}", "credit": vert.get("mark"), "max_loss": vert.get("max_loss"),
                     "cost": vert.get("cost"), "n": 1, "mark_source": vert.get("mark_source"),
                     "context_read": context_read, "direction": direction, "entry": None, "stop": None, "target": None,
                     **_leg_columns(vert.get("legs") or [])})
    return [POL.stamp(r, DISC_POLICY_ID, POL.ROLE_EXPLORATION, GATE_PASS) for r in rows]


def frame(rows: list[dict]) -> pd.DataFrame:
    return pd.DataFrame(rows) if rows else pd.DataFrame()


def already_present(existing: pd.DataFrame, row: dict) -> bool:
    """True when the ledger already holds this row's key (write-once: it will be skipped)."""
    from engine.ledger import KEY
    if existing.empty:
        return False
    key = tuple(str(row[k]) for k in KEY)
    return key in set(map(tuple, existing[KEY].astype(str).itertuples(index=False)))


def summary(rows: list[dict], present_before: list[bool]) -> list[dict]:
    """The `ledger_rows` entries of `ticker.json`: what was built and whether the ledger took it."""
    return [{"policy_id": r["policy_id"], "role": r["role"], "gate_verdict": r["gate_verdict"],
             "structure": r["structure"], "written": not was_there,
             "reason": "already in the ledger (write-once)" if was_there else None}
            for r, was_there in zip(rows, present_before)]
