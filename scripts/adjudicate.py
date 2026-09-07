#!/usr/bin/env python3
"""Register and adjudicate (DESIGN/100 §4, §5). Reads ledger rows only; writes one file per verdict.

  register  --strategy sb --policy-id sb-c1 --idea "VIX floor 15" --param vix_floor=15 --min-effect 0.01 --registered 2026-12-05 [--sd]
  run       --policy sb-c1 [--as-of YYYY-MM-DD]            challenger vs champion, paired, once
  champion  --strategy sb --n-required 26 [--as-of]         champion vs its bar (t part; the report holds the rest)
  gate      --strategy sb --min-effect 0.01 --n-required 20 [--as-of]   gate-ON vs gate-OFF on the exploration book
  basket    --policy wb-1.0 [--basket LONG|SHORT|VOL] [--as-of]   the watch-basket read (DESIGN/110 §6); omit
                                                                   --basket to read all three
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from engine import ledger as L                                   # noqa: E402
from engine import policy as POL                                 # noqa: E402
from engine.config import LEDGER_DIR                             # noqa: E402
from engine.improve import adjudicate as A                       # noqa: E402
from engine.improve import basket_read as BR                     # noqa: E402
from engine.improve import power as PW                           # noqa: E402
from engine.improve.spec import spec                             # noqa: E402
from engine.watch.wb_ledger import read_ledger as read_wb_ledger  # noqa: E402
from power import champion_series                                # noqa: E402

WB_POLICY_ID = "wb-1.0"


def _ledger(strategy: str, root: str) -> pd.DataFrame:
    return L.read_ledger(spec(strategy).ledger_dir(root))


def cmd_register(a) -> int:
    sp = spec(a.strategy)
    key, _, val = a.param.partition("=")
    if not key or not val:
        raise SystemExit("--param must be name=value")
    try:
        value = json.loads(val)
    except json.JSONDecodeError:
        value = val
    series, source = champion_series(a.strategy, a.ledger_dir)
    if a.sd is None and series.empty:
        raise SystemExit("no series for the realised sd; pass --sd")
    registered = date.fromisoformat(a.registered)
    plan = PW.plan(a.min_effect, series if len(series) else None, sp.lag, registered, a.units_per_week or sp.units_per_week, sd=a.sd)
    reg = {"policy_id": a.policy_id, "strategy": a.strategy, "champion": sp.champion_id, "idea": a.idea,
           "params_diff": {key: value}, "registered": registered.isoformat(), "n_required": plan["n_required"], "unit": sp.unit,
           "adjudicate_on": plan["adjudicate_on"],
           "test": f"paired difference in {sp.metric} (challenger minus champion) per {sp.unit} on rows matched by {A.MATCH_KEY}; one-sided t, Newey-West lag {sp.lag}; alpha {A.ALPHA}",
           "min_effect": a.min_effect, "kill": f"early FAIL if the paired mean is below -{a.min_effect} at half n_required",
           "power": {k: plan[k] for k in ("sd", "sd_source", "inflation", "alpha", "power")} | {"series_source": source},
           "script_sha256": A.script_sha256()}
    path = A.register(a.ledger_dir, reg)
    print(json.dumps(reg, indent=1))
    print(f"registered -> {path}; commit it before the first shadow night")
    return 0


def cmd_run(a) -> int:
    reg_path = os.path.join(a.ledger_dir, A.CHALLENGERS_DIR, f"{a.policy}.json")
    reg = A.load_registration(reg_path)
    if reg["script_sha256"] != A.script_sha256():
        raise SystemExit("the adjudication script has changed since registration; re-register the challenger (DESIGN/100 §5)")
    sp = spec(reg["strategy"])
    led = _ledger(reg["strategy"], a.ledger_dir)
    champ = A.rows_for(led, reg["champion"], POL.ROLE_CHAMPION)
    chall = A.rows_for(led, reg["policy_id"], POL.ROLE_CHALLENGER)
    units = A.paired_units(champ, chall, sp, date.fromisoformat(reg["registered"]))
    stats = A.series_stats(units, sp.lag)
    as_of = date.fromisoformat(a.as_of)
    verdict, reason = A.challenger_verdict(stats, reg, as_of)
    payload = {"policy_id": reg["policy_id"], "kind": "challenger", "as_of": as_of.isoformat(), "verdict": verdict, "reason": reason,
               "stats": stats, "registration": reg}
    print(json.dumps(payload, indent=1, default=str))
    if verdict in (A.NOT_DUE, A.INSUFFICIENT):
        print(f"{verdict}: no verdict, nothing written; re-run when {reg['n_required']} units have accrued")
        return 0
    path = A.write_adjudication(a.ledger_dir, reg["policy_id"], payload)
    print(f"-> {path}")
    if verdict == A.PROMOTE:
        print(f"PROMOTE: bump {sp.champion_id} in engine/config.py and the frozen-params test to {reg['params_diff']}, "
              f"record it in DECISIONS.md; the old champion's rows stay under their own policy_id")
    return 0


def cmd_champion(a) -> int:
    sp = spec(a.strategy)
    led = _ledger(a.strategy, a.ledger_dir)
    rows = A.rows_for(led, sp.champion_id, POL.ROLE_CHAMPION)
    stats = A.series_stats(A.unit_means(rows, sp), sp.lag)
    verdict, reason = A.champion_verdict(stats, a.n_required, sp.go_t)
    payload = {"policy_id": sp.champion_id, "kind": "champion", "as_of": a.as_of, "verdict": verdict, "reason": reason, "stats": stats,
               "n_required": a.n_required, "go_t": sp.go_t}
    print(json.dumps(payload, indent=1, default=str))
    print(f"-> {A.write_adjudication(a.ledger_dir, f'{sp.champion_id}-{a.as_of}', payload)}")
    return 0


def cmd_gate(a) -> int:
    sp = spec(a.strategy)
    led = _ledger(a.strategy, a.ledger_dir)
    rows = A.rows_for(led, sp.champion_id, POL.ROLE_EXPLORATION)
    stats = A.gate_stats(rows, sp)
    verdict, reason = A.gate_verdict(stats, a.min_effect, a.n_required)
    payload = {"policy_id": sp.champion_id, "kind": "gate", "as_of": a.as_of, "verdict": verdict, "reason": reason, "stats": stats,
               "min_effect": a.min_effect, "n_required": a.n_required}
    print(json.dumps(payload, indent=1, default=str))
    print(f"-> {A.write_adjudication(a.ledger_dir, f'gate-{a.strategy}-{a.as_of}', payload)}")
    return 0


def cmd_basket(a) -> int:
    if a.policy != WB_POLICY_ID:
        raise SystemExit(f"basket only knows policy {WB_POLICY_ID!r}, got {a.policy!r}")
    as_of = date.fromisoformat(a.as_of)
    ledger = read_wb_ledger(os.path.join(a.ledger_dir, "wb"))
    baskets = [a.basket] if a.basket else list(BR.BASKETS)
    for basket in baskets:
        result = BR.read(ledger, basket, as_of)
        payload = {"policy_id": WB_POLICY_ID, "kind": "basket", "basket": basket, "as_of": result["as_of"],
                   "verdict": result["verdict"], "reason": result["reason"], "n_episodes": result["n_episodes"],
                   "projected_date": result.get("projected_date"), "stats": result.get("stats", {})}
        print(json.dumps(payload, indent=1, default=str))
        if result["verdict"] == BR.NOT_DUE:
            print(f"{basket}: NOT_DUE, nothing written")
            continue
        path = A.write_adjudication(a.ledger_dir, f"{WB_POLICY_ID}-{basket}", payload)
        print(f"{basket} -> {path}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger-dir", default=LEDGER_DIR)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("register")
    r.add_argument("--strategy", required=True); r.add_argument("--policy-id", required=True); r.add_argument("--idea", required=True)
    r.add_argument("--param", required=True); r.add_argument("--min-effect", type=float, required=True)
    r.add_argument("--registered", default=date.today().isoformat()); r.add_argument("--sd", type=float, default=None)
    r.add_argument("--units-per-week", type=float, default=None)
    r.set_defaults(fn=cmd_register)
    x = sub.add_parser("run"); x.add_argument("--policy", required=True); x.add_argument("--as-of", default=date.today().isoformat()); x.set_defaults(fn=cmd_run)
    c = sub.add_parser("champion"); c.add_argument("--strategy", required=True); c.add_argument("--n-required", type=int, required=True)
    c.add_argument("--as-of", default=date.today().isoformat()); c.set_defaults(fn=cmd_champion)
    g = sub.add_parser("gate"); g.add_argument("--strategy", required=True); g.add_argument("--min-effect", type=float, required=True)
    g.add_argument("--n-required", type=int, required=True); g.add_argument("--as-of", default=date.today().isoformat()); g.set_defaults(fn=cmd_gate)
    k = sub.add_parser("basket"); k.add_argument("--policy", required=True); k.add_argument("--basket", choices=list(BR.BASKETS), default=None)
    k.add_argument("--as-of", default=date.today().isoformat()); k.set_defaults(fn=cmd_basket)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
