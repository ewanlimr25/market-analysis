"""The S-B nightly step (DESIGN/80 §7), called by `make daily` after the S-A steps.

`nightly(con, d, force_ledger)` refreshes the CBOE series (fail-soft) and runs `run(...)`, which
is pure given its loaders: the gate for d and for the next session, tonight's candidates when d is
the last session of its week, grading of every signal whose expiry is d, the open-position count
per sleeve, and the running forward P&L. Everything lands in `signals.json["sb_state"]`.
"""
from __future__ import annotations

from datetime import date
from typing import Callable

import pandas as pd

from engine import calendar as cal
from engine import ledger as L
from engine.config import (LEDGER_SB_DIR, SB_LEDGER_OPENS, SB_PARAMS, SB_SIZING, SB_UNDERLYINGS, SB_VOL_INDEX,
                           SBParams, SBSizing)
from engine.mart import index_vol as IV
from engine.strategies import sb, sb_data
from engine.strategies import sb_gate as G
from engine.strategies import sb_proxy as P
from engine.strategies import sb_structures as SB
from engine.validation import stats as S

RowsLoader = Callable[[object, tuple[str, ...], date], pd.DataFrame]
CloseLoader = Callable[[object, str, date], float | None]


def ledger_open(d: date) -> bool:
    return d >= SB_LEDGER_OPENS


def is_entry_day(d: date) -> bool:
    """The last session of d's ISO week: the next session falls in a different week."""
    nxt = cal.next_session(d)
    return nxt.isocalendar()[:2] != d.isocalendar()[:2]


def refresh_index_vol() -> dict:
    """Refresh the CBOE series; never raises (the file on disk is used on failure)."""
    try:
        df = IV.refresh()
        return {"ok": True, "through": str(IV.latest_date(df))}
    except Exception as exc:  # network / parse
        return {"ok": False, "error": str(exc)[:200]}


def _gate_dict(state: G.GateState) -> dict:
    return {"date": state.date.isoformat(), "asof": state.asof.isoformat() if state.asof else None, "reason": state.reason,
            "on": state.on, "known": state.known, "vix": state.vix, "vix3m": state.vix3m, "x": state.x, "x_median": state.x_median}


def _gates(index_vol: pd.DataFrame, t: date, prev: date, params: SBParams) -> dict[str, G.GateState]:
    return {u: G.gate(index_vol, t, prev, SB_VOL_INDEX[u], params) for u in SB_UNDERLYINGS}


def open_positions(ledger_dir: str, d: date) -> dict[str, int]:
    """Signals whose expiry is after d, per sleeve (graded rows are closed by construction)."""
    sig = L.read_signals(ledger_dir)
    if sig.empty:
        return {}
    open_ = sig[pd.to_datetime(sig["post"]).dt.date > d]
    return {f"{u}-{s}": int(n) for (u, s), n in open_.groupby(["underlying", "structure"]).size().items()}


def _default_close_loader(con, ticker: str, d: date):
    close, _ = sb_data.settle_close(con, ticker, d)
    return close


def _candidates(con, d: date, index_vol: pd.DataFrame, gates: dict, rows_loader: RowsLoader, params: SBParams,
                sizing: SBSizing, open_now: dict[str, int]) -> tuple[list[dict], list[dict]]:
    rows_all = rows_loader(con, SB_UNDERLYINGS, d)
    trades, skipped = [], []
    for u in SB_UNDERLYINGS:
        rows_u = rows_all[rows_all["underlying_symbol"] == u] if len(rows_all) else pd.DataFrame()
        res = sb.entry_candidates(u, d, rows_u, gates[u], P._x_on(index_vol, d, SB_VOL_INDEX[u]), params, sizing, cal.is_trading_day)
        for t in res.trades:
            if open_now.get(f"{u}-{t['structure']}", 0) >= sizing.max_open_per_sleeve:
                skipped.append({**{k: t[k] for k in ("ticker", "underlying", "entry", "E", "variant", "structure", "gate_reason")}, "reason": "cap_open"})
            else:
                trades.append(t)
        skipped.extend(res.skipped)
    return trades, skipped


def _grade_due(con, d: date, ledger_dir: str, close_loader: CloseLoader) -> tuple[list[dict], list[dict]]:
    due = L.pending(ledger_dir, d)
    graded, unsettled = [], []
    for sig in (due.to_dict("records") if len(due) else []):
        close = close_loader(con, sig["underlying"], d)
        if close is None:
            unsettled.append({k: sig[k] for k in L.KEY} | {"reason": "no_settlement_close"})
            continue
        graded.append(sb.grade_position(sig, float(close), sb_data.SETTLE_PRICES))
    return graded, unsettled


def running(ledger: pd.DataFrame) -> list[dict]:
    if ledger.empty or "ror" not in ledger.columns:
        return []
    out = []
    for (u, s), g in ledger.groupby(["underlying", "structure"]):
        nw = S.nw_t(g["ror"], 2)
        out.append({"sleeve": f"{u}-{s}", "n": nw["n"], "mean_ror": nw["mean"], "nw_t": nw["t"], "net_usd_total": float(g["net_usd"].sum())})
    return out


def _jsonable(rows: list[dict]) -> list[dict]:
    if not rows:
        return []
    return [{k: (v.isoformat() if isinstance(v, date) else (None if isinstance(v, float) and pd.isna(v) else v)) for k, v in r.items()}
            for r in rows]


def run(con, d: date, ledger_dir: str = LEDGER_SB_DIR, index_vol: pd.DataFrame | None = None,
        rows_loader: RowsLoader = sb_data.load_entry_rows, close_loader: CloseLoader = _default_close_loader,
        force_ledger: bool = False, params: SBParams = SB_PARAMS, sizing: SBSizing = SB_SIZING) -> dict:
    iv = IV.on_sessions(index_vol if index_vol is not None else IV.load_index_vol(), cal.is_trading_day)
    prev, nxt = cal.prev_session(d), cal.next_session(d)
    gates, gates_next = _gates(iv, d, prev, params), _gates(iv, nxt, d, params)
    entry_day = is_entry_day(d)
    is_open = ledger_open(d) or force_ledger
    open_now = open_positions(ledger_dir, d)
    trades, skipped = _candidates(con, d, iv, gates, rows_loader, params, sizing, open_now) if entry_day else ([], [])
    graded, unsettled = _grade_due(con, d, ledger_dir, close_loader)
    emitted = L.emit(ledger_dir, pd.DataFrame(trades), d) if is_open and trades else (0, 0)
    n_graded = L.grade(ledger_dir, pd.DataFrame(graded), d)[0] if is_open and graded else 0
    return {"date": d.isoformat(), "index_vol_through": str(IV.latest_date(iv)) if len(iv) else None,
            "is_entry_day": entry_day, "gate": {u: _gate_dict(g) for u, g in gates.items()},
            "gate_next": {u: _gate_dict(g) for u, g in gates_next.items()},
            "candidates": _jsonable(trades), "skipped": _jsonable(skipped), "graded": _jsonable(graded), "unsettled": _jsonable(unsettled),
            "open_positions": open_positions(ledger_dir, d), "running": running(L.read_ledger(ledger_dir)),
            "ledger": {"emitted": emitted[0], "skipped": emitted[1], "graded": n_graded, "ledger_open": is_open}}


def nightly(con, d: date, force_ledger: bool = False) -> dict:
    """The production entry point: refresh CBOE (fail-soft), then `run` with the mart loaders."""
    refresh = refresh_index_vol()
    try:
        state = run(con, d, LEDGER_SB_DIR, None, sb_data.load_entry_rows, _default_close_loader, force_ledger)
    except Exception as exc:  # the S-A report must still be written
        state = {"date": d.isoformat(), "error": f"S-B step failed: {exc}"[:300], "candidates": [], "graded": [], "gate": {}}
    return {**state, "refresh": refresh}
