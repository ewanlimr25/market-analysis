"""`report.md` from `signals.json` (DESIGN/70 §5): one page, templated, no model."""
from __future__ import annotations

from typing import Any

from engine.watch.conditions import ALL_CONDITIONS as WB_CONDITION_IDS

NO_EVENT = "no event tonight clears the filters"
CANDIDATE_COLS = ["ticker", "variant", "structure", "expiry", "k", "k_up", "k_dn", "credit_entry",
                  "credit_net_pct", "risk_usd", "contracts", "entry_tier_max", "cap_pass"]
SUPPRESSED_COLS = ["ticker", "variant", "first_fail"]
GRADED_COLS = ["ticker", "variant", "structure", "role", "net_pct", "net_usd", "exit_tier_max", "model_exit"]
RUNNING_COLS = ["policy_id", "role", "variant", "structure", "n", "dates", "mean_net_pct", "t", "net_usd_total"]
EXPLORATION_COLS = ["ticker", "structure", "expiry", "k", "credit_entry", "credit_net_pct", "risk_usd", "gate_verdict"]
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
    explore = signals.get("exploration", [])
    if explore or signals.get("exploration_dropped"):
        parts += ["", f"## Exploration book tonight ({len(explore)}; one contract per structure for every priceable event, filters ignored, first failing filter recorded)",
                  table(explore, EXPLORATION_COLS) if explore else "_none priceable_"]
    graded = signals.get("graded", [])
    parts += ["", f"## Graded today ({len(graded)})", table(graded, GRADED_COLS) if graded else "_none due_"]
    running = signals.get("season_running", [])
    parts += ["", "## Season to date (forward ledger)", table(running, RUNNING_COLS) if running else "_ledger empty_"]
    led = signals.get("ledger", {})
    parts += ["", f"Ledger: emitted {led.get('emitted', 0)} (skipped {led.get('skipped', 0)}), exploration {led.get('exploration_emitted', 0)} "
                  f"(skipped {led.get('exploration_skipped', 0)}), graded {led.get('graded', 0)}; "
                  f"ledger {'open' if led.get('ledger_open') else 'CLOSED (before 2026-10-01; nothing written)'}."]
    parts += ["", "## S-B state", render_sb(signals.get("sb_state")), ""]
    if "sc_state" in signals:
        parts += ["", "## S-C state", render_sc(signals.get("sc_state")), ""]
    parts += ["", "## Watch basket (wb-1.0, exploration, paper only)", render_wb(signals.get("watch_basket")), ""]
    return "\n".join(parts)


SB_CANDIDATE_COLS = ["underlying", "structure", "expiry", "k_p1", "k_p2", "k_c1", "k_c2", "credit_entry", "max_loss_usd", "contracts", "entry_tier_max"]
SB_GRADED_COLS = ["underlying", "structure", "entry", "expiry", "settle_close", "net_usd", "ror"]
SB_RUNNING_COLS = ["policy_id", "role", "sleeve", "n", "mean_ror", "nw_t", "net_usd_total"]
SB_EXPLORATION_COLS = ["underlying", "structure", "expiry", "k_p1", "k_p2", "k_c1", "k_c2", "credit_entry", "max_loss_usd", "gate_verdict"]
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
    explore = state.get("exploration", [])
    if state.get("is_entry_day"):
        parts += ["", f"### S-B exploration book tonight ({len(explore)}; one contract per sleeve, gate ignored, gate verdict recorded)",
                  table(explore, SB_EXPLORATION_COLS) if explore else "_none (no markable position)_"]
    graded = state.get("graded", [])
    parts += ["", f"### S-B graded at expiry today ({len(graded)})", table(graded, SB_GRADED_COLS + ["role"]) if graded else "_none due_"]
    unsettled = state.get("unsettled", [])
    if unsettled:
        parts += ["", f"_{len(unsettled)} position(s) due today have no settlement close yet; they stay pending._"]
    open_ = state.get("open_positions", {})
    parts += ["", "Open positions: " + (", ".join(f"{k} {v}" for k, v in open_.items()) if open_ else "none")]
    running = state.get("running", [])
    parts += ["", "### S-B forward ledger to date", table(running, SB_RUNNING_COLS) if running else "_ledger empty_"]
    led = state.get("ledger", {})
    parts += ["", f"S-B ledger: emitted {led.get('emitted', 0)} (skipped {led.get('skipped', 0)}), exploration {led.get('exploration_emitted', 0)} "
                  f"(skipped {led.get('exploration_skipped', 0)}), graded {led.get('graded', 0)}; "
                  f"ledger {'open' if led.get('ledger_open') else 'CLOSED (before 2026-09-11; nothing written)'}."]
    return "\n".join(parts)


# ---- S-C (findings DESIGN/90 §7) -------------------------------------------------------------------

SC_CANDIDATE_COLS = ["variant", "rank", "ticker", "sector", "structure", "close", "iv30d", "expiry", "dte_cal", "k", "k_up", "k_dn",
                     "credit_entry", "max_loss_usd", "stress_loss_usd", "entry_cost_usd", "contracts", "sigma_hold", "cap_pass", "cap_reason"]
SC_GRADED_COLS = ["ticker", "variant", "structure", "E", "expiry", "settle_close", "settle_source", "corporate_action", "net_usd", "ror"]
SC_SLEEVE_COLS = ["pair", "positions", "open_risk_usd", "budget_usd", "max_sector_positions"]
SC_RUNNING_COLS = ["policy_id", "role", "pair", "n", "weeks", "mean_ror", "nw_t", "net_usd_total"]
SC_FILTER_ORDER = ("F1", "F2", "F3", "F4", "F7", "F5", "F6", "F8", "F9")


def _sc_funnel(funnel: dict) -> str:
    stops = [f"{f} {funnel[f]}" for f in SC_FILTER_ORDER if funnel.get(f)]
    tail = [f"{k} {v}" for k, v in sorted(funnel.items()) if ":" in k]
    return "Stopped at: " + (" · ".join(stops) or "none") + ("; " + " · ".join(tail) if tail else "")


def render_sc(state: dict | None) -> str:
    """Friday: funnel, positions, exploration counts; every night: graded, open book, progress to the read."""
    if not state:
        return "_no S-C state (step not run)._"
    if state.get("error"):
        return f"**{state['error']}**"
    parts = [f"Entry day: {'yes' if state.get('is_entry_day') else 'no'}; ledger "
             f"{'open' if state.get('ledger_open') else 'CLOSED (opens 2026-10-02; nothing written)'}."]
    if state.get("is_entry_day"):
        cands = state.get("candidates", [])
        ex = state.get("exploration", {})
        parts += ["", _sc_funnel(state.get("funnel", {})),
                  "", f"### S-C positions tonight ({len(cands)}; paper, before the read)", table(cands, SC_CANDIDATE_COLS) if cands else "_none selected_",
                  "", f"Exploration book: {ex.get('names', 0)} priceable names at one contract each, by first failing filter: "
                      + (", ".join(f"{k} {v}" for k, v in sorted(ex.get("by_verdict", {}).items())) or "none")]
    graded = state.get("graded", [])
    parts += ["", f"### S-C graded at expiry ({len(graded)})", table(graded, SC_GRADED_COLS) if graded else "_none due_"]
    if state.get("unsettled"):
        parts += ["", f"_{len(state['unsettled'])} row(s) due have no settlement close yet; they are retried each night._"]
    book = state.get("open_book", {})
    parts += ["", f"### S-C open book (S-B open: {'yes' if book.get('sb_open') else 'no'}; the 40% budget binds only then)",
              table(book.get("sleeves", []), SC_SLEEVE_COLS) if book.get("sleeves") else "_empty_"]
    running = state.get("running", [])
    parts += ["", "### S-C forward ledger to date (entry-week series)", table(running, SC_RUNNING_COLS) if running else "_ledger empty_"]
    progress = state.get("progress", [])
    parts += ["", "Progress to the read: graded entry-weeks " + ", ".join(f"{p['forward_weeks']} of {p['required']} ({p['pair']})" for p in progress)]
    led = state.get("ledger", {})
    parts += ["", f"S-C ledger: emitted {led.get('emitted', 0)} (skipped {led.get('skipped', 0)}), exploration {led.get('exploration_emitted', 0)} "
                  f"(skipped {led.get('exploration_skipped', 0)}), graded {led.get('graded', 0)}."]
    return "\n".join(parts)


# ---- watch basket (DESIGN/110-watch-basket.md §7 R2) ----------------------------------------------

WB_BASKET_COLS = ["ticker", "bull", "bear", "episode", *WB_CONDITION_IDS]
WB_READ_SENTENCE = ("Paper rows; read on the later of 2026-12-01 and 100 LONG episodes (DESIGN/110 "
                     "§6); nothing here is a trade.")


def _wb_dist_line(label: str, dist: dict) -> str:
    if not dist:
        return f"{label}: n/a"
    return f"{label}: " + ", ".join(f"{k}:{v}" for k, v in sorted(dist.items(), key=lambda kv: int(kv[0])))


def _wb_row_for_table(entry: dict) -> dict:
    """One basket-list entry as a table row: ticker/bull/bear/episode plus a tick column per
    condition id ("x" true, "?" null, blank false -- DESIGN/110 §3's "individually and
    collectively" made visible per name, not just per stack count)."""
    true_ids, null_ids = set(entry.get("true_ids", [])), set(entry.get("null_ids", []))
    out = {"ticker": entry["ticker"], "bull": entry["bull"], "bear": entry["bear"], "episode": entry["episode"]}
    out.update({cid: ("x" if cid in true_ids else ("?" if cid in null_ids else "")) for cid in WB_CONDITION_IDS})
    return out


def _wb_borrow_line(b: dict | None) -> str:
    """Which IBKR snapshot C-SHORT read: exact, a fallback (with its age), or none (d1.5 `borrow`)."""
    if not b:
        return "Borrow snapshot: not recorded (pre-d1.5 document)."
    if b.get("asof") is None:
        return "Borrow snapshot: **none within the fallback window**; C-SHORT read borrow as null."
    age = b.get("stale_days") or 0
    how = "the session's own" if age == 0 else f"fallback, {age} day{'s' if age != 1 else ''} old"
    return f"Borrow snapshot: {b['asof']} ({how}); fee known for {b.get('names_with_fee', 0)} names."


def render_wb(state: dict | None) -> str:
    if not state:
        return "_no watch-basket state (step not run)._"
    if not state.get("available"):
        return f"**unavailable: {state.get('reason')}**"
    dist = state.get("count_distribution", {})
    parts = [f"Universe: {state.get('universe_n', 0)} names.", _wb_borrow_line(state.get("borrow")),
             _wb_dist_line("Bull counts", dist.get("bull", {})),
             _wb_dist_line("Bear counts", dist.get("bear", {})), ""]
    for label, key in (("LONG", "long"), ("SHORT", "short"), ("VOL", "vol")):
        rows = state.get(key, [])
        parts += [f"### {label} ({len(rows)})",
                  table([_wb_row_for_table(r) for r in rows], WB_BASKET_COLS) if rows else "_none_", ""]
    parts.append(f"CONFLICT (logged only, never a basket, DESIGN/110 §3): {len(state.get('conflict', []))}.")
    led_line = (f"Ledger: emitted {state.get('wb_emitted', 0)} (skipped {state.get('wb_skipped', 0)}), "
                f"graded {state.get('wb_graded', 0)}; "
                f"ledger {'open' if state.get('ledger_open') else 'CLOSED (before 2026-09-08; nothing written)'}.")
    parts += ["", led_line, "", WB_READ_SENTENCE]
    return "\n".join(parts)
