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
    parts += ["", "## S-B state", "_not implemented in this cycle (DESIGN/70 §0)._", ""]
    return "\n".join(parts)
