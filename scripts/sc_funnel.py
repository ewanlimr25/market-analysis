"""S-C R1 funnel on real entry sessions (DESIGN/90 §10 acceptance c): F1..F10 counts per date,
beside an E2-style count (an ATM pair within 3% with >= 10 lots on each leg, any expiry 20 to 40
DTE) so the numbers can be read against `RESEARCH/40 E2`'s coverage table.

    python3 scripts/sc_funnel.py 2026-05-08 2026-06-30 2026-08-26
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import sys
from datetime import date

import duckdb
import pandas as pd

from engine import calendar as cal
from engine.strategies import sc_data as D
from engine.strategies import sc_filters as F

E2_BAND, E2_MIN_LOTS, E2_DTE = 0.03, 10, (20, 40)


def e2_style_pairs(contracts: pd.DataFrame, closes: dict[str, float]) -> int:
    n = 0
    for u, g in contracts.groupby("underlying_symbol"):
        s = closes.get(u)
        if not s:
            continue
        g = g[(g["dte_cal"] >= E2_DTE[0]) & (g["dte_cal"] <= E2_DTE[1]) & (g["size_late"].fillna(0) >= E2_MIN_LOTS)]
        g = g[(g["strike"] / s - 1).abs() <= E2_BAND]
        if g.groupby(["expiry", "strike"])["option_type"].nunique().eq(2).any():
            n += 1
    return n


def _pair_count(rows: pd.DataFrame, close: float, band: float, min_size: int, size_col: str) -> bool:
    g = rows[(rows["size_late" if size_col == "late" else "size_total"].fillna(0) >= min_size)]
    g = g[(g["strike"] / close - 1).abs() <= band]
    return bool(g.groupby(["expiry", "strike"])["option_type"].nunique().eq(2).any())


def f8_diagnostics(survivors: list[dict], by_u: dict, d: date) -> dict:
    """Among names that passed F1..F6 (F7 ignored): which of F7 / F8's three clauses binds. Each
    column counts names with an ATM pair under one relaxation, the others at the spec value."""
    p = F.SC_PARAMS
    keys = {"F7 expiry exists": 0, "F7 expiry + spec F8": 0, "any 20-40 DTE expiry, spec F8": 0,
            "F7 expiry, size_late>=10": 0, "F7 expiry, size_total>=20 (all day)": 0, "F7 expiry, band 3%": 0}
    for row in survivors:
        rows = by_u.get(row["ticker"], pd.DataFrame())
        if rows.empty:
            continue
        close = float(row["close"])
        exp = F.select_expiry(rows["expiry"].dropna().unique(), d, cal.is_trading_day)
        any_exp = rows[(rows["dte_cal"] >= 20) & (rows["dte_cal"] <= 40)]
        if len(any_exp) and _pair_count(any_exp, close, p.atm_band, p.leg_size_min, "late"):
            keys["any 20-40 DTE expiry, spec F8"] += 1
        if exp is None:
            continue
        keys["F7 expiry exists"] += 1
        in_exp = rows[rows["expiry"].map(F.to_date) == exp]
        keys["F7 expiry + spec F8"] += _pair_count(in_exp, close, p.atm_band, p.leg_size_min, "late")
        keys["F7 expiry, size_late>=10"] += _pair_count(in_exp, close, p.atm_band, 10, "late")
        keys["F7 expiry, size_total>=20 (all day)"] += _pair_count(in_exp, close, p.atm_band, p.leg_size_min, "total")
        keys["F7 expiry, band 3%"] += _pair_count(in_exp, close, 0.03, p.leg_size_min, "late")
    return keys


def funnel_for(con, d: date) -> dict:
    universe = D.load_entry_universe(con, d)
    contracts = D.load_contract_rows(con, universe["ticker"], d)
    by_u = {u: g for u, g in contracts.groupby("underlying_symbol")} if len(contracts) else {}
    evs = [F.evaluate_name(row, by_u.get(row["ticker"], pd.DataFrame()), d, cal.is_trading_day)
           for row in universe.to_dict("records")]
    counts = F.funnel_counts(evs)
    closes = dict(zip(universe["ticker"], universe["close"]))
    scr_ok = {t for t, e in zip(universe["ticker"], evs) if all(e[f] for f in ("F1", "F2", "F3", "F4", "F6"))}
    survivors = [r for r in universe.to_dict("records") if r["ticker"] in scr_ok]
    return {"date": d.isoformat(), **counts, "e2_style_pairs": e2_style_pairs(contracts, closes) if len(contracts) else 0,
            "c1_names": [e["ticker"] for e in F.select_top(evs, "C1")], "f1_f6": len(survivors),
            "diag": f8_diagnostics(survivors, by_u, d)}


def main(argv: list[str]) -> int:
    dates = [date.fromisoformat(a) for a in argv] or [D.panel_sessions()[-1]]
    con = duckdb.connect()
    rows = [funnel_for(con, d) for d in dates]
    cols = ["date", "names", "F1", "F2", "F3", "F4", "F7", "F5", "F6", "F8", "F9", "C1", "C2", "e2_style_pairs"]
    print("| " + " | ".join(cols) + " |")
    print("|" + "---|" * len(cols))
    for r in rows:
        print("| " + " | ".join(str(r[c]) for c in cols) + " |")
    for r in rows:
        print(f"\nC1 on {r['date']}: {', '.join(r['c1_names']) or '(none)'}")
    diag_keys = list(rows[0]["diag"]) if rows else []
    print("\nF7 / F8 diagnostics among F1..F6 survivors (one clause relaxed at a time; descriptive):\n")
    print("| date | F1..F6 | " + " | ".join(diag_keys) + " |")
    print("|---|---|" + "---|" * len(diag_keys))
    for r in rows:
        print(f"| {r['date']} | {r['f1_f6']} | " + " | ".join(str(r["diag"][k]) for k in diag_keys) + " |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
