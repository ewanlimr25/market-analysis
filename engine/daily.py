"""`make daily DATE=YYYY-MM-DD` (DESIGN/70 §5): preflight, append the mart, tonight's S-A
candidates with every filter's verdict, grade yesterday's signals into the forward ledger, then the
S-B step (DESIGN/80 §7, `engine/sb_daily.py`), and write analyses/daily/<date>/signals.json +
report.md. Deterministic; no model call; the only network use is the CBOE refresh, fail-soft.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import date

import duckdb
import pandas as pd

from engine import calendar as cal
from engine import ledger as L
from engine import marking as M
from engine import portfolio
from engine import report as R
from engine import schema as SCH
from engine import sb_daily as SD
from engine.config import ANALYSES_DAILY, LEDGER_DIR, SA_PARAMS, SCRIPTS, SIZING
from engine.mart import daily_contract, earnings_events
from engine.strategies import sa, sa_data
from engine.strategies import sa_filters as F
from engine.strategies import sa_structures as ST
from engine.validation import stats as S
from engine.backtest_sa import LOAD_MCAP_HI, LOAD_MCAP_LO

LEDGER_OPENS = date(2026, 10, 1)      # Season 3 ledger opens (DESIGN/70 §7 P7)


def ledger_open(d: date) -> bool:
    return d >= LEDGER_OPENS


def sb_ledger_dir(ledger_dir: str) -> str:
    """The S-B ledger lives beside the S-A one: `<ledger_dir>/sb` (the default is `LEDGER_SB_DIR`)."""
    return os.path.join(ledger_dir, "sb")


def preflight(d: date) -> dict:
    cmd = [sys.executable, os.path.join(SCRIPTS, "preflight.py"), "--date", d.isoformat(), "--json"]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return json.loads(out.stdout) if out.stdout.strip() else {"ok": False, "warnings": [out.stderr.strip()[:200]]}
    except (OSError, subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
        return {"ok": False, "warnings": [f"preflight failed: {exc}"]}


def append_mart(d: date, con) -> dict:
    """Append `daily_contract` and `earnings_events` for d; both are no-ops when present."""
    contracts = daily_contract.build_day(d, con)
    events = earnings_events.build_day(d, con)
    return {"daily_contract_rows": int(len(contracts)), "earnings_events_rows": int(len(events))}


def _events_for_pre(con, d: date) -> pd.DataFrame:
    ev = sa_data.load_events(con)
    return ev[ev.pre == d] if len(ev) else ev


def candidates(con, d: date) -> sa.RunResult:
    """Entry-only S-A evaluation of every event with pre == d (no exit marks exist yet)."""
    events = _events_for_pre(con, d)
    if events.empty:
        return sa.RunResult(pd.DataFrame(), pd.DataFrame(), pd.DataFrame())
    pre_rows = sa_data.load_pre_rows(con, events, LOAD_MCAP_LO, LOAD_MCAP_HI)
    spreads = sa_data.load_spread_history(con, events)
    prices = sa_data.load_prices(con, set(events.ticker), {d})
    iv30d = sa_data.load_iv30d(con, set(events.ticker), {d})
    rows = {(r["option_chain_id"], F.to_date(r["date"])): r for r in pre_rows.to_dict("records")}
    model = sa_data.build_model_inputs(prices, iv30d, spreads, pd.DataFrame(), {})
    res = sa.run(events, pre_rows, M.MarkResolver(rows, model), SA_PARAMS, SIZING, with_exit=False)
    trades = portfolio.apply_caps(res.trades, SIZING) if len(res.trades) else res.trades
    return sa.RunResult(trades, res.suppressed, res.dropped)


def _exit_legs(sig: dict, resolver: M.MarkResolver, post: date) -> list[ST.Leg] | None:
    legs = []
    for rec in json.loads(sig["legs_json"]):
        contract = ST.make_contract(sig["ticker"], date.fromisoformat(rec["expiry"]), rec["option_type"], float(rec["strike"]))
        exit_ = resolver.mark(contract, post, M.WHEN_EARLY)
        if exit_ is None:
            return None
        legs.append(ST.leg_from_record(rec, sig["ticker"], exit_))
    return legs


def grade_rows(signals: pd.DataFrame, resolver: M.MarkResolver) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Mark every stored leg at `early` on `post` and recompute the P&L from the stored entry."""
    graded, dropped = [], []
    for sig in signals.to_dict("records"):
        post = F.to_date(pd.Timestamp(sig["post"]))
        legs = _exit_legs(sig, resolver, post)
        if legs is None:
            dropped.append({k: sig[k] for k in L.KEY} | {"reason": "unmarkable_exit"})
            continue
        priced = ST.price_legs(legs, int(sig["contracts"]))
        notional = float(sig["notional_usd"])
        graded.append({**sig, **priced, "net_pct": priced["net_usd"] / notional, "gross_pct": priced["gross_usd"] / notional,
                       "cost_pct": priced["cost_usd"] / notional, "exit_tier_max": max(l.exit.tier for l in legs),
                       "model_exit": any(l.exit.tier == 3 for l in legs)})
    return pd.DataFrame(graded), pd.DataFrame(dropped)


def grade_due(con, d: date, ledger_dir: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    due = L.pending(ledger_dir, d)
    if due.empty:
        return due, pd.DataFrame()
    ids = {rec["option_chain_id"] for legs in due.legs_json for rec in json.loads(legs)}
    exit_rows = sa_data.load_rows_for_contracts(con, ids, {d})
    tickers = set(due.ticker)
    prices = sa_data.load_prices(con, tickers, {d})
    iv30d = sa_data.load_iv30d(con, tickers, {d})
    spreads = {(t, d): None for t in tickers}
    rows = {(r["option_chain_id"], F.to_date(r["date"])): r for r in exit_rows.to_dict("records")} if len(exit_rows) else {}
    model = sa_data.build_model_inputs(prices, iv30d, spreads, pd.DataFrame(), {})
    return grade_rows(due, M.MarkResolver(rows, model))


def season_running(ledger: pd.DataFrame, season: str) -> list[dict]:
    if ledger.empty:
        return []
    sub = ledger[ledger.season == season]
    out = []
    for (v, s), g in sub.groupby(["variant", "structure"]):
        ct = S.cluster_t(g.net_pct, g.pre.astype(str))
        out.append({"variant": v, "structure": s, "n": ct["n"], "dates": ct["G"], "mean_net_pct": ct["mean"],
                    "t": ct["t"], "net_usd_total": float(g.net_usd.sum())})
    return out


def _jsonable(df: pd.DataFrame) -> list[dict]:
    if df.empty:
        return []
    return json.loads(df.to_json(orient="records", date_format="iso", default_handler=str))


def run_daily(d: date, ledger_dir: str = LEDGER_DIR, out_root: str = ANALYSES_DAILY, con=None,
              force_ledger: bool = False) -> dict:
    con = con or duckdb.connect()
    pf = preflight(d)
    mart = append_mart(d, con)
    cands = candidates(con, d)
    graded, dropped = grade_due(con, d, ledger_dir)
    is_open = ledger_open(d) or force_ledger
    emitted = L.emit(ledger_dir, cands.trades, d) if is_open and len(cands.trades) else (0, 0)
    n_graded = L.grade(ledger_dir, graded, d)[0] if is_open and len(graded) else 0
    running = season_running(L.read_ledger(ledger_dir), earnings_events.season_of(d))
    signals = assemble(d, pf, mart, cands, graded, dropped, running,
                       {"emitted": emitted[0], "skipped": emitted[1], "graded": n_graded, "ledger_open": is_open},
                       SD.nightly(con, d, force_ledger, sb_ledger_dir(ledger_dir)))
    write_outputs(signals, os.path.join(out_root, d.isoformat()))
    return signals


def assemble(d: date, pf: dict, mart: dict, cands: sa.RunResult, graded: pd.DataFrame, dropped: pd.DataFrame,
             running: list[dict], ledger_counts: dict, sb_state: dict) -> dict:
    """The `signals.json` document (schemas/signals.schema.json): stamped, strict-JSON clean."""
    both_dropped = pd.concat([cands.dropped, dropped]) if len(dropped) or len(cands.dropped) else pd.DataFrame()
    body = {"date": d.isoformat(), "season": earnings_events.season_of(d), "preflight": pf, "mart": mart,
            "candidates": _jsonable(cands.trades), "suppressed": _jsonable(cands.suppressed),
            "dropped": _jsonable(both_dropped), "graded": _jsonable(graded), "season_running": running,
            "ledger": ledger_counts, "sb_state": sb_state}
    return SCH.clean(SCH.stamp(body))


def write_outputs(signals: dict, out_dir: str) -> list[str]:
    """Write signals.json (strict JSON) and report.md; returns the schema violations (empty = valid)."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "signals.json"), "w") as fh:
        fh.write(SCH.dumps(signals))
    with open(os.path.join(out_dir, "report.md"), "w") as fh:
        fh.write(R.render(signals))
    try:
        return SCH.validate(signals)
    except Exception as exc:  # the schema file or jsonschema itself; never blocks the nightly
        return [f"validation could not run: {exc}"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--ledger-dir", default=LEDGER_DIR)
    ap.add_argument("--out-root", default=ANALYSES_DAILY)
    ap.add_argument("--force-ledger", action="store_true", help="write the ledger before 2026-10-01 (testing)")
    a = ap.parse_args()
    d = cal.parse_date(a.date)
    if not cal.is_trading_day(d):
        print(f"{d} is not a trading day", file=sys.stderr)
        return 1
    sig = run_daily(d, a.ledger_dir, a.out_root, force_ledger=a.force_ledger)
    print(f"{d}: {len(sig['candidates'])} candidates, {len(sig['suppressed'])} suppressed, "
          f"{len(sig['graded'])} graded; report at {os.path.join(a.out_root, d.isoformat(), 'report.md')}")
    errors = SCH.validate(sig)
    if errors:
        print(f"WARN signals.json does not match schemas/signals.schema.json ({len(errors)}):", file=sys.stderr)
        for e in errors[:20]:
            print(f"  {e}", file=sys.stderr)
    else:
        print(f"signals.json: VALID ({SCH.REPORT_KIND} {SCH.SCHEMA_VERSION})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
