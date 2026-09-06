"""`report.md` from `signals.json` (DESIGN/70 §5): one page, templated, no model."""
from __future__ import annotations

from typing import Any

NO_EVENT = "no event tonight clears the filters"
CANDIDATE_COLS = ["ticker", "variant", "structure", "expiry", "k", "k_up", "k_dn", "credit_entry",
                  "credit_net_pct", "risk_usd", "n", "entry_tier_max", "cap_pass"]
SUPPRESSED_COLS = ["ticker", "variant", "first_fail"]
GRADED_COLS = ["ticker", "variant", "structure", "net_pct", "net_usd", "exit_tier_max", "model_exit"]
RUNNING_COLS = ["variant", "structure", "n", "dates", "mean_net_pct", "t", "net_usd_total"]
PCT_COLS = {"credit_net_pct", "net_pct", "mean_net_pct"}


def _cell(col: str, v: Any) -> str:
    if v is None or v != v:
        return "—"
    if isinstance(v, bool):
        return "yes" if v else "no"
    if col in PCT_COLS and isinstance(v, (int, float)):
        return f"{100 * v:+.2f}%"
    if isinstance(v, float):
        return f"{v:,.2f}"
    return str(v)


def table(rows: list[dict], cols: list[str]) -> str:
    present = [c for c in cols if any(c in r for r in rows)]
    head = "| " + " | ".join(present) + " |\n|" + "---|" * len(present)
    body = "\n".join("| " + " | ".join(_cell(c, r.get(c)) for c in present) + " |" for r in rows)
    return head + "\n" + body


def _preflight(pf: dict) -> str:
    status = "clear" if pf.get("ok") else "WARN"
    warnings = pf.get("warnings") or []
    return f"Preflight: {status}" + (" — " + "; ".join(map(str, warnings)) if warnings else "")


def render(signals: dict) -> str:
    d = signals["date"]
    parts = [f"# S-A daily — {d} ({signals.get('season', '')})", "", _preflight(signals.get("preflight", {})), ""]
    cands = signals.get("candidates", [])
    parts.append(f"## Tonight's candidates ({len(cands)})")
    parts.append(table(cands, CANDIDATE_COLS) if cands else f"_{NO_EVENT}._")
    sup = signals.get("suppressed", [])
    parts += ["", f"## Suppressed ({len(sup)})", table(sup, SUPPRESSED_COLS) if sup else "_none_"]
    graded = signals.get("graded", [])
    parts += ["", f"## Graded today ({len(graded)})", table(graded, GRADED_COLS) if graded else "_none due_"]
    running = signals.get("season_running", [])
    parts += ["", "## Season to date (forward ledger)", table(running, RUNNING_COLS) if running else "_ledger empty_"]
    led = signals.get("ledger", {})
    parts += ["", f"Ledger: emitted {led.get('emitted', 0)} (skipped {led.get('skipped', 0)}), graded {led.get('graded', 0)}; "
                  f"ledger {'open' if led.get('ledger_open') else 'CLOSED (before 2026-10-01; nothing written)'}."]
    parts += ["", "## S-B state", render_sb(signals.get("sb_state")), ""]
    return "\n".join(parts)


SB_CANDIDATE_COLS = ["underlying", "structure", "expiry", "k_p1", "k_p2", "k_c1", "k_c2", "credit_entry", "max_loss_usd", "n", "entry_tier_max"]
SB_GRADED_COLS = ["underlying", "structure", "entry", "expiry", "settle_close", "net_usd", "ror"]
SB_RUNNING_COLS = ["sleeve", "n", "mean_ror", "nw_t", "net_usd_total"]
SB_SKIPPED_COLS = ["underlying", "structure", "reason"]
PCT_COLS.update({"ror", "mean_ror"})


def _gate_line(label: str, gates: dict) -> str:
    if not gates:
        return f"{label}: no gate evaluated"
    bits = []
    for u, g in gates.items():
        vals = f" (VIX {g.get('vix')}, VIX3M {g.get('vix3m')}, X {g.get('x')} vs median {g.get('x_median')})" if g.get("known") else ""
        bits.append(f"{u} {g.get('reason')}{vals}")
    first = next(iter(gates.values()))
    return f"{label} ({first.get('date')}, from {first.get('asof') or 'n/a'} closes): " + " · ".join(bits)


def render_sb(state: dict | None) -> str:
    if not state:
        return "_no S-B state (step not run)._"
    if state.get("error"):
        return f"**{state['error']}**"
    parts = [_gate_line("Gate", state.get("gate", {})), "", _gate_line("Next session", state.get("gate_next", {})), ""]
    refresh = state.get("refresh")
    if refresh is not None:
        parts += [f"CBOE refresh: {'ok through ' + str(refresh.get('through')) if refresh.get('ok') else 'FAILED (' + str(refresh.get('error')) + '); using the file on disk'}"
                  + f"; index-vol through {state.get('index_vol_through')}", ""]
    parts.append(f"Entry day: {'yes' if state.get('is_entry_day') else 'no'}.")
    cands = state.get("candidates", [])
    parts += ["", f"### S-B positions tonight ({len(cands)})", table(cands, SB_CANDIDATE_COLS) if cands else "_none_"]
    skipped = state.get("skipped", [])
    if skipped:
        parts += ["", f"### S-B skipped ({len(skipped)})", table(skipped, SB_SKIPPED_COLS)]
    graded = state.get("graded", [])
    parts += ["", f"### S-B graded at expiry today ({len(graded)})", table(graded, SB_GRADED_COLS) if graded else "_none due_"]
    unsettled = state.get("unsettled", [])
    if unsettled:
        parts += ["", f"_{len(unsettled)} position(s) due today have no settlement close yet; they stay pending._"]
    open_ = state.get("open_positions", {})
    parts += ["", "Open positions: " + (", ".join(f"{k} {v}" for k, v in open_.items()) if open_ else "none")]
    running = state.get("running", [])
    parts += ["", "### S-B forward ledger to date", table(running, SB_RUNNING_COLS) if running else "_ledger empty_"]
    led = state.get("ledger", {})
    parts += ["", f"S-B ledger: emitted {led.get('emitted', 0)} (skipped {led.get('skipped', 0)}), graded {led.get('graded', 0)}; "
                  f"ledger {'open' if led.get('ledger_open') else 'CLOSED (before 2026-09-11; nothing written)'}."]
    return "\n".join(parts)
