"""The S-C nightly step (DESIGN/90 §7, steps 11 to 13; R5 of §10), called by `make daily` after S-B.

`run(...)` is pure given its loaders. On the last session of an ISO week it selects C1 and C2 (§2),
prices both structures, applies the §4 caps against the open book (every selection is written with
`cap_pass`; the harness reads all of them) and writes the exploration book (DESIGN/100 §6: one contract
for every priceable pair, `gate_verdict` = the first failing filter). Every night it grades each row
whose expiry is on or before tonight and which has no ledger row yet (a row whose close was missing on
its expiry night is picked up the next night). Everything lands in `signals.json["sc_state"]`, compact;
the full rows are in `ledger/sc/`.
"""
from __future__ import annotations

from datetime import date
from typing import Any, Callable

import pandas as pd

from engine import calendar as cal
from engine import ledger as L
from engine import policy as POL
from engine import sb_daily as SBD
from engine.config import LEDGER_SB_DIR, LEDGER_SC_DIR, SC_LEDGER_OPENS, SC_PARAMS, SC_SIZING, SCParams, SCSizing
from engine.strategies import sb_data, sc
from engine.strategies import sc_data as D
from engine.strategies import sc_structures as S
from engine.strategies.sa_data import as_dates
from engine.validation import sc_harness as H

WeekLoader = Callable[[Any, date], "sc.WeekInput | None"]
SettleLoader = Callable[[Any, list[str], date, date], tuple[dict, Any, "date | None"]]
DATE_COLS = ("E", "entry", "expiry", "post")
CANDIDATE_FIELDS = ("ticker", "variant", "structure", "rank", "sector", "close", "iv30d", "expiry", "dte_cal", "k", "k_up",
                    "k_dn", "credit_entry", "entry_cost_usd", "max_loss_usd", "stress_loss_usd", "contracts", "risk_usd",
                    "sigma_hold", "entry_tier_max", "cap_pass", "cap_reason", "policy_id", "role", "gate_verdict")
GRADED_FIELDS = ("ticker", "E", "variant", "structure", "expiry", "contracts", "settle_close", "settle_source",
                 "corporate_action", "net_usd", "ror", "policy_id", "role", "gate_verdict")
REASON_NO_CLOSE = "no_settlement_close"


def ledger_open(d: date) -> bool:
    return d >= SC_LEDGER_OPENS


def _signals(ledger_dir: str) -> pd.DataFrame:
    sig = L.read_signals(ledger_dir)
    return as_dates(sig, DATE_COLS) if len(sig) else sig


def open_book(ledger_dir: str, d: date) -> list[dict]:
    """Champion rows inside the caps whose expiry is after d: what §4 counts tonight."""
    sig = _signals(ledger_dir)
    if sig.empty:
        return []
    keep = (sig["role"] == POL.ROLE_CHAMPION) & (sig["cap_pass"].astype(bool)) & (sig["expiry"] > d)
    return sig[keep].to_dict("records")


def sb_open_on(sb_ledger_dir: str, d: date) -> bool:
    """§4's "when S-B positions are also open": an S-B champion signal entered on or before d, expiring after it."""
    sig = L.read_signals(sb_ledger_dir)
    if sig.empty:
        return False
    sig = as_dates(sig, ("E", "post"))
    return bool(((sig["role"] == POL.ROLE_CHAMPION) & (sig["E"] <= d) & (sig["post"] > d)).any())


def due(ledger_dir: str, d: date) -> pd.DataFrame:
    """Rows whose expiry is on or before d and which have no ledger row yet (catch-up included)."""
    sig = _signals(ledger_dir)
    if sig.empty:
        return sig
    return L._new_rows(L.read_ledger(ledger_dir), sig[sig["expiry"] <= d])


def default_week_loader(con, d: date) -> sc.WeekInput | None:
    from engine.backtest_sc import wing_resolver
    universe = D.load_entry_universe(con, d)
    if universe.empty:
        return None
    contracts = D.load_contract_rows(con, universe["ticker"], d)
    return sc.WeekInput(d, universe, contracts, wing_resolver(con, d, universe, contracts))


def default_settle_loader(con, tickers: list[str], start: date, d: date):
    return sb_data.load_closes(con, tickers, start, d), D.PrintCloses(con), D.prices_through(con)


def grade_due(con, d: date, ledger_dir: str, settle_loader: SettleLoader) -> tuple[list[dict], list[dict]]:
    rows = due(ledger_dir, d)
    if rows.empty:
        return [], []
    closes, prints, through = settle_loader(con, sorted(set(rows["ticker"])), min(rows["entry"]), d)
    graded, unsettled = [], []
    for row in rows.to_dict("records"):
        s = sc.settlement_for(row["ticker"], row["entry"], row["expiry"], row["close"], closes, prints, prices_through=through)
        if s.close is None:
            unsettled.append({k: row[k] for k in L.KEY} | {"expiry": row["expiry"], "reason": REASON_NO_CLOSE})
        else:
            graded.append(sc.grade(row, s))
    return graded, unsettled


def funnel(suppressed: list[dict], candidates: list[dict]) -> dict[str, int]:
    """Names stopped at each filter tonight, then the selected count per variant."""
    counts: dict[str, int] = {}
    for r in suppressed:
        key = r["reason"] if r.get("variant") is None else f"{r['variant']}:{r['reason']}"
        counts[key] = counts.get(key, 0) + 1
    for r in candidates:
        key = f"{r['variant']}:selected"
        counts[key] = counts.get(key, 0) + (1 if r["structure"] == S.STRUCTURE_SS else 0)
    return counts


def sleeves(book: list[dict], sizing: SCSizing, sb_open: bool) -> list[dict]:
    out = []
    for v, s in H.PAIRS:
        rows = [r for r in book if r["variant"] == v and r["structure"] == s]
        sectors: dict[str, int] = {}
        for r in rows:
            sectors[str(r.get("sector"))] = sectors.get(str(r.get("sector")), 0) + 1
        out.append({"pair": H.pair_name(v, s), "positions": len(rows), "open_risk_usd": float(sum(r["risk_usd"] for r in rows)),
                    "budget_usd": S.book_budget_usd(s, sizing) if sb_open else None,
                    "max_sector_positions": max(sectors.values(), default=0)})
    return out


def running(ledger_dir: str) -> tuple[list[dict], list[dict]]:
    """Per (policy, role, pair) on the entry-week series, and the champion's progress to the read."""
    led = L.read_ledger(ledger_dir)
    if led.empty:
        return [], H.count_status(None)[["pair", "forward_weeks", "required"]].to_dict("records")
    led = as_dates(led, DATE_COLS)
    out = []
    for (pid, role), sub in POL.by_policy(led):
        for v, s in H.PAIRS:
            b = H.pair_block(sub, v, s, "F")
            if b["n"]:
                out.append({"policy_id": pid, "role": role, "pair": b["pair"], "n": b["n"], "weeks": b["weeks"],
                            "mean_ror": b["mean_ror"], "nw_t": b["nw_t"], "net_usd_total": b["net_usd_total"]})
    champ = led[led["role"] == POL.ROLE_CHAMPION]
    return out, H.count_status(champ)[["pair", "forward_weeks", "required"]].to_dict("records")


def _compact(rows: list[dict], fields: tuple[str, ...]) -> list[dict]:
    return [{k: r.get(k) for k in fields} for r in rows]


def _entries(con, d: date, ledger_dir: str, sb_ledger_dir: str, week_loader: WeekLoader, sizing: SCSizing,
             params: SCParams) -> dict:
    week = week_loader(con, d)
    if week is None:
        return {"candidates": [], "suppressed": [], "exploration": [], "sb_open": sb_open_on(sb_ledger_dir, d), "note": "no screener"}
    wk = sc.entry_week(week, sizing, params)
    sb_open = sb_open_on(sb_ledger_dir, d)
    capped = S.apply_caps(wk.candidates, open_book(ledger_dir, d), sizing, sb_open=sb_open)
    explore = sc.exploration_week(week, params)
    return {"candidates": [{**r, "post": r["expiry"]} for r in capped], "suppressed": wk.suppressed,
            "exploration": [{**r, "post": r["expiry"]} for r in explore], "sb_open": sb_open, "dropped": wk.dropped}


def run(con, d: date, ledger_dir: str = LEDGER_SC_DIR, sb_ledger_dir: str = LEDGER_SB_DIR,
        week_loader: WeekLoader = default_week_loader, settle_loader: SettleLoader = default_settle_loader,
        force_ledger: bool = False, sizing: SCSizing = SC_SIZING, params: SCParams = SC_PARAMS) -> dict:
    entry_day = SBD.is_entry_day(d)
    is_open = ledger_open(d) or force_ledger
    ent = _entries(con, d, ledger_dir, sb_ledger_dir, week_loader, sizing, params) if entry_day else \
        {"candidates": [], "suppressed": [], "exploration": [], "sb_open": sb_open_on(sb_ledger_dir, d)}
    emitted = L.emit(ledger_dir, pd.DataFrame(ent["candidates"]), d) if is_open and ent["candidates"] else (0, 0)
    explored = L.emit(ledger_dir, pd.DataFrame(ent["exploration"]), d) if is_open and ent["exploration"] else (0, 0)
    graded, unsettled = grade_due(con, d, ledger_dir, settle_loader) if is_open else ([], [])
    n_graded = L.grade(ledger_dir, pd.DataFrame(graded), d)[0] if graded else 0
    runs, progress = running(ledger_dir)
    verdicts: dict[str, int] = {}
    for r in ent["exploration"]:
        if r["structure"] == S.STRUCTURE_SS:
            verdicts[r["gate_verdict"]] = verdicts.get(r["gate_verdict"], 0) + 1
    return {"date": d.isoformat(), "is_entry_day": entry_day, "ledger_open": is_open,
            "funnel": funnel(ent["suppressed"], ent["candidates"]) if entry_day else {},
            "candidates": _compact(ent["candidates"], CANDIDATE_FIELDS),
            "graded": _compact([g for g in graded if g["role"] == POL.ROLE_CHAMPION], GRADED_FIELDS),
            "unsettled": unsettled,
            "exploration": {"names": sum(verdicts.values()), "by_verdict": verdicts,
                            "graded": sum(1 for g in graded if g["role"] == POL.ROLE_EXPLORATION)},
            "open_book": {"sb_open": ent["sb_open"], "sleeves": sleeves(open_book(ledger_dir, d), sizing, ent["sb_open"])},
            "running": runs, "progress": progress,
            "ledger": {"emitted": emitted[0], "skipped": emitted[1], "exploration_emitted": explored[0],
                       "exploration_skipped": explored[1], "graded": n_graded}}


def nightly(con, d: date, force_ledger: bool = False, ledger_dir: str = LEDGER_SC_DIR,
            sb_ledger_dir: str = LEDGER_SB_DIR) -> dict:
    """The production entry point; never raises (the S-A and S-B report must still be written)."""
    try:
        return run(con, d, ledger_dir, sb_ledger_dir, force_ledger=force_ledger)
    except Exception as exc:
        return {"date": d.isoformat(), "error": f"S-C step failed: {type(exc).__name__}: {exc}"[:300],
                "candidates": [], "graded": []}
