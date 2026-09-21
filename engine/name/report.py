"""`report.md` from `ticker.json` (findings/stock-deep-dive DESIGN/70 §8): one page, sections A to H,
generated from the JSON alone, no model. Every line prints the number beside its label so the
reader is never given a label alone (§3: the premium verdict always sits next to `spread_rv5`)."""
from __future__ import annotations

from typing import Any


def _n(v: Any, fmt: str = "{:,.2f}", none: str = "—") -> str:
    if v is None or (isinstance(v, float) and v != v):
        return none
    try:
        return fmt.format(v)
    except (TypeError, ValueError):
        return str(v)


def _pct(v: Any) -> str:
    return _n(None if v is None else 100 * v, "{:+.1f}%")


def _line_a(t: dict) -> str:
    q = t["liquidity"]
    verdict = "CAN_PRICE" if q["can_price"] else f"CANNOT_PRICE ({q['failing']})"
    return (f"A  {verdict}   contracts {_n(q['contracts'], '{:,}')} · hot-chain {_n(q['hot_chain_days'], '{}')}/21 · "
            f"ADV ${_n(q['adv_usd'], '{:,.0f}')} · ATM spread {_pct(q['atm_spread'])} (tier {_n(q['tier'], '{}')})")


def _line_b(t: dict) -> str:
    e = t["events"]
    earn = e["earnings"]
    srcs = " = ".join(f"{s['name']} {s['date'] or '?'}" for s in earn["sources"])
    conf = "confirmed" if earn["confirmed"] else "NOT CONFIRMED (X1 for 45d)"
    macro = " · ".join(f"{m['event']} {m['date']}" for m in e["macro"]) or "no FOMC in 45d"
    return (f"B  Earnings {earn['date'] or '?'} {earn['session'] or ''} session {earn.get('session_date') or '?'} [{conf}: {srcs}] · "
            f"ex-div {e['ex_div'] or '—'} · expiries {', '.join(e['expiries']) or '—'} · {macro}")


def _line_c(t: dict) -> str:
    p = t["premium"]
    sc = p["sc"]
    sc_txt = "S-C: passes F1..F9" if sc["pass"] else f"S-C: fails {sc['failing']}"
    f6 = (sc.get("verdicts") or {}).get("F6")
    if f6 is not None and not sc["pass"] and sc["failing"] != "F6":
        sc_txt += f"; F6 {'passes' if f6 else 'fails'} at {_n(p['iv30d'], '{:.3f}')}"
    sa = p.get("sa")
    sa_txt = f" · S-A A1: {sa.get('first_fail') or 'passes'} (measurement only; S-A closed at execution)" if sa else ""
    return (f"C  Premium {p['verdict']}   iv30d {_n(None if p['iv30d'] is None else 100 * p['iv30d'], '{:.1f}')} "
            f"(own pct {_n(p['iv_pct_own'], '{:.0f}')}) · rv5_21 {_n(p['rv5_21'], '{:.1f}')} / c2c {_n(p['rv_c2c_21'], '{:.1f}')} · "
            f"spread {_n(p['spread_rv5'], '{:+.1f}')} / {_n(p['spread_c2c'], '{:+.1f}')} · slope {_n(p['slope'], '{:+.1f}')}\n"
            f"   prior prints: {len(p['earnings_history'])}, median realized/implied {_n(p['median_ratio_8'])} · {sc_txt}{sa_txt}"
            + (" · X1: no premium structure on this sheet" if p.get("x1") else ""))


def _line_d(t: dict) -> str:
    r = t["range"]
    sf = r.get("straddle_front") or {}
    return (f"D  Range  1σ box to {sf.get('expiry') or '?'} ±${_n(r['box_1s_front'])} (straddle {_n(sf.get('mark'))}, {sf.get('mark_source') or '—'}) · "
            f"1σ 30d ±${_n(r['box_1s_21'])} · ATR14 {_n(r['atr14'])} · GEX {r['gex_sign'] or '—'}, ZGL {_n(r['zero_gamma'])} "
            f"({(r.get('source') or {}).get('gex_total') or (r.get('source') or {}).get('zero_gamma') or 'no chain'})")


def _line_e(t: dict) -> str:
    f = t["flags"]
    b, si, vix = f.get("borrow") or {}, f.get("si") or {}, f.get("vix") or {}
    form4 = f.get("form4") or {}
    return (f"E  Flags  borrow {_pct(b.get('fee') / 100 if b.get('fee') is not None else None)} (decile {_n(b.get('decile'), '{:.1f}')}, IBKR {b.get('date') or '—'})"
            f"{' X2' if f.get('x2') else ''} · SI {_pct(si.get('pct_float'))} / DTC {_n(si.get('dtc'), '{:.1f}')} "
            f"(FINRA {si.get('settlement') or '—'}, pub {si.get('publication') or '—'}){' X5 defined-risk preferred' if f.get('x5') else ''} · "
            f"beta {_n(f.get('beta_250'), '{:.2f}')}\n"
            f"          analyst: {len(f.get('analyst') or [])} changes last 10 sessions · Form 4: {form4.get('buys', 0)} buys / "
            f"{form4.get('sells', 0)} sells 30d · VIX {_n(vix.get('vix'), '{:.1f}')} {vix.get('term') or ''}, {f.get('regime') or '—'}")


def _line_f(t: dict) -> str:
    c = t["context"]
    return (f"F  {c['sentence']}\n   context: ret21 {_pct(c['ret_21'])} · ret63 {_pct(c['ret_63'])} · 52w pos {_n(c['w52_pos'])} · "
            f"flow pct universe {_n(c['flow_pct_universe'], '{:.0f}')} / self {_n(c['flow_pct_self'], '{:.0f}')}")


def _struct_line(s: dict) -> str:
    legs = " ".join(f"{_n(l.get('strike'), '{:g}')}{l.get('right')}{'+' if l.get('side') == 1 else '-'}" for l in s.get("legs") or [])
    if s["family"] == "SHARES":
        legs = f"entry {_n(s.get('entry'))} stop {_n(s.get('stop'))} target {_n(s.get('target'))}"
    prob = f"P(in) {_n(s.get('p_inside'))}" if s.get("p_inside") is not None else f"P(touch) {_n(s.get('p_touch'))}"
    excl = f"  [{s['excluded_by']}]" if s.get("excluded_by") else ""
    note = f"  ({s['note']})" if s.get("note") else ""
    return (f"   {s['family']:<15} {legs:<40} {s.get('credit_debit') or ''} {_n(s.get('mark'))}  max loss {_n(s.get('max_loss'))}  "
            f"BE {'–'.join(_n(b) for b in s.get('breakevens') or []) or '—'}  {prob}  cost {_n(s.get('cost'))}  n={s.get('n', 0)}  "
            f"${_n(s.get('usd_at_risk'), '{:,.0f}')}{excl}{note}")


def _line_g(t: dict) -> str:
    st = t["structures"]
    if not st:
        return "G  Structures: none (CANNOT_PRICE)"
    exp = next((s["expiry"] for s in st if s.get("expiry")), None)
    return f"G  Structures (expiry {exp or '—'})\n" + "\n".join(_struct_line(s) for s in st)


def _line_h(t: dict) -> str:
    rows = t["ledger_rows"]
    if not rows:
        return "H  Ledger: no row (CANNOT_PRICE or unpriced)"
    parts = [f"{r['policy_id']} {r['role']} {r['structure']} [{r['gate_verdict']}] {'written' if r['written'] else r['reason']}" for r in rows]
    tag = f" · context_read {t['context_read']}" if t.get("direction") else ""
    return "H  Ledger: " + " · ".join(parts) + tag


def render(t: dict) -> str:
    head = f"{t['ticker']} — {t['date']} — {t['policy_id']} — E ${t['E']:,.0f}" + (f" — DIRECTION {t['direction']}" if t.get("direction") else "")
    nulls = ", ".join(f"{n['field']} ({n['reason']})" for n in t["nulls"]) or "none"
    body = [head, _line_a(t), _line_b(t), _line_c(t), _line_d(t), _line_e(t), _line_f(t), _line_g(t), _line_h(t), f"nulls: {nulls}"]
    return "```\n" + "\n".join(body) + "\n```\n"
