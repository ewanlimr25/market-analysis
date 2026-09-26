"""S-C, the weekly run (DESIGN/90 §2 to §4; R3 of §10): pure functions from one entry session's
screener rows and `daily_contract` rows to candidates, the suppressed table and dropped structures,
then the chronological run with the §4 caps and settlement at expiry.

Entry: the last session of each ISO week (`sb_proxy.entry_sessions`). Selection: `sc_filters` F1..F10
per variant (C1, C2). Structures and caps: `sc_structures`. Settlement (§3): tier-4 intrinsic against
the expiry close in entry-share terms --

    prices       `prices.parquet` (Yahoo) close on the expiry session, scaled by the split factor
    daily_contract  the last print's underlying price that session, when the Yahoo close is absent
    last_close   a name with no close from its last price date to expiry while `prices` runs past
                 it (delisting, cash merger): its last close in [entry, expiry), `corporate_action`

Yahoo closes are split-adjusted to the fetch date and the screener's close on the entry session is
not, so `raw_entry / yahoo_entry` is the split factor between entry and the fetch; applied to the
Yahoo expiry close it gives the expiry price in entry-share terms whether the split fell inside the
window or after it. A factor within `SPLIT_TOL` of 1 is noise and taken as 1; otherwise the row is
flagged `corporate_action = split` and the harness reports with and without such rows. Nothing here
may be tuned before the read.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any, Callable, Iterable, Mapping

import pandas as pd

from engine import calendar as cal
from engine import policy as POL
from engine.config import SC_PARAMS, SC_POLICY_ID, SC_SIZING, SC_VARIANTS, SCParams, SCSizing
from engine.strategies import sc_filters as F
from engine.strategies import sc_structures as S

REASON_F10, REASON_C2 = "F10", "C2_sector"
SOURCE_PRICES, SOURCE_PRINTS, SOURCE_LAST = "prices", "daily_contract", "last_close"
CA_SPLIT, CA_DELISTED = "split", "delisted"
SPLIT_TOL = 0.05                  # |raw / yahoo − 1| below this is close-vs-close noise, not a split
CAP_OPEN = S.CAP_OPEN
IsSession = Callable[[date], bool]


@dataclass(frozen=True)
class WeekInput:
    entry: date
    universe: pd.DataFrame        # `sc_data.load_entry_universe` rows
    contracts: pd.DataFrame       # `daily_contract` rows of the universe on `entry`
    wing_resolver: Callable[[list[str]], Any]   # selected tickers -> a resolver (`.mark`) for their wings


@dataclass
class WeekResult:
    candidates: list[dict] = field(default_factory=list)
    suppressed: list[dict] = field(default_factory=list)
    dropped: list[dict] = field(default_factory=list)


@dataclass(frozen=True)
class Settlement:
    close: float | None
    source: str | None
    corporate_action: str | None = None
    split_factor: float = 1.0


@dataclass(frozen=True)
class RunResult:
    trades: pd.DataFrame
    suppressed: pd.DataFrame
    dropped: pd.DataFrame


# ---- one entry week ------------------------------------------------------------------------------

def _evaluate(week: WeekInput, params: SCParams, is_session: IsSession) -> list[dict]:
    by_u = {u: g for u, g in week.contracts.groupby("underlying_symbol")} if len(week.contracts) else {}
    empty = pd.DataFrame()
    evs = []
    for row in week.universe.to_dict("records"):
        ev = F.evaluate_name(row, by_u.get(row["ticker"], empty), week.entry, is_session, params)
        evs.append({**ev, "close": row.get("close"), "_rows": by_u.get(row["ticker"], empty)})
    return evs


def _suppressed(ev: Mapping[str, Any], reason: str, variant: str | None) -> dict:
    return {"ticker": ev["ticker"], "entry": ev["entry"], "variant": variant, "reason": reason}


def _selection_cuts(evs: list[dict], variant: str, chosen: set[str]) -> list[dict]:
    out = []
    for ev in evs:
        if not F.passed_all(ev) or ev["ticker"] in chosen:
            continue
        reason = REASON_C2 if variant != F.VARIANT_C1 and not ev.get("c2") else REASON_F10
        out.append(_suppressed(ev, reason, variant))
    return out


def entry_week(week: WeekInput, sizing: SCSizing = SC_SIZING, params: SCParams = SC_PARAMS,
               is_session: IsSession = cal.is_trading_day, variants: tuple[str, ...] = SC_VARIANTS) -> WeekResult:
    """Candidates (one row per variant x selected name x structure, with the F10 rank), the suppressed
    table (first failing filter per name; F10 / C2 cuts per variant) and dropped structures."""
    evs = _evaluate(week, params, is_session)
    res = WeekResult(suppressed=[_suppressed(ev, ev["reason"], None) for ev in evs if ev["reason"] is not None])
    tops = {v: F.select_top(evs, v, params) for v in variants}
    selected = sorted({e["ticker"] for top in tops.values() for e in top})
    resolver = week.wing_resolver(selected) if selected else None
    built: dict[str, S.BuildResult] = {}
    for variant in variants:
        top = tops[variant]
        res.suppressed.extend(_selection_cuts(evs, variant, {e["ticker"] for e in top}))
        for ev in top:
            if ev["ticker"] not in built:
                rows = ev["_rows"]
                built[ev["ticker"]] = S.build(ev, rows[rows["expiry"].map(F.to_date) == ev["expiry"]], resolver, sizing, params)
            b = built[ev["ticker"]]
            for structure, row in b.structures.items():
                res.candidates.append(POL.stamp({**row, "variant": variant, "rank": ev["rank"], "E": week.entry},
                                                SC_POLICY_ID, POL.ROLE_CHAMPION, POL.SA_GATE_PASS))
            res.dropped.extend({**d, "variant": variant} for d in b.dropped)
    return res


# ---- settlement ----------------------------------------------------------------------------------

def split_factor(raw_entry: float | None, yahoo_entry: float | None) -> float:
    if not raw_entry or not yahoo_entry or raw_entry <= 0 or yahoo_entry <= 0:
        return 1.0
    f = raw_entry / yahoo_entry
    return 1.0 if abs(f - 1.0) < SPLIT_TOL else f


def _last_close(ticker: str, entry: date, expiry: date, closes: Mapping[tuple[str, date], float]) -> tuple[date, float] | None:
    held = [(d, c) for (t, d), c in closes.items() if t == ticker and entry <= d < expiry]
    return max(held) if held else None


def settlement_for(ticker: str, entry: date, expiry: date, raw_entry: float | None,
                   closes: Mapping[tuple[str, date], float], print_closes: Mapping[tuple[str, date], float],
                   *, prices_through: date | None) -> Settlement:
    """The expiry close in entry-share terms, where it came from, and any corporate action (§3)."""
    f = split_factor(raw_entry, closes.get((ticker, entry)))
    ca = CA_SPLIT if f != 1.0 else None
    y = closes.get((ticker, expiry))
    if y is not None:
        return Settlement(y * f, SOURCE_PRICES, ca, f)
    p = print_closes.get((ticker, expiry))
    if p is not None:
        return Settlement(float(p), SOURCE_PRINTS, None, 1.0)
    if prices_through is not None and expiry <= prices_through:
        last = _last_close(ticker, entry, expiry, closes)
        if last is not None:
            return Settlement(last[1] * f, SOURCE_LAST, CA_DELISTED, f)
    return Settlement(None, None)


UNGRADED = {"graded": False, "settle_close": None, "settle_source": None, "corporate_action": None, "split_factor": None,
            "debit_exit": None, "gross_usd": None, "exit_cost_usd": None, "cost_usd": None, "net_usd": None,
            "exit_tier_max": None, "ror": None}


def grade(row: Mapping[str, Any], s: Settlement) -> dict:
    if s.close is None:
        return {**row, **UNGRADED}
    g = S.settle(row, s.close)
    return {**row, **g, "graded": True, "settle_close": s.close, "settle_source": s.source,
            "corporate_action": s.corporate_action, "split_factor": s.split_factor,
            "ror": g["net_usd"] / float(row["risk_usd"])}


# ---- the run -------------------------------------------------------------------------------------

def _cap_week(entry: date, candidates: list[dict], book: list[dict], sizing: SCSizing, sb_open: bool) -> list[dict]:
    open_ = [r for r in book if r["cap_pass"] and r["expiry"] > entry]
    return S.apply_caps(candidates, open_, sizing, sb_open=sb_open)


def run(weeks: Iterable[WeekInput], closes: Mapping[tuple[str, date], float],
        print_closes: Mapping[tuple[str, date], float], *, prices_through: date | None,
        sb_open_on: Callable[[date], bool], sizing: SCSizing = SC_SIZING, params: SCParams = SC_PARAMS,
        is_session: IsSession = cal.is_trading_day) -> RunResult:
    """Chronological: entry week, caps against the open book, settlement wherever the close is known.
    Every selected structure is kept (the harness reads all of them); `cap_pass` is the portfolio view."""
    trades, suppressed, dropped, book = [], [], [], []
    for week in sorted(weeks, key=lambda w: w.entry):
        wk = entry_week(week, sizing, params, is_session)
        suppressed.extend(wk.suppressed)
        dropped.extend(wk.dropped)
        capped = _cap_week(week.entry, wk.candidates, book, sizing, sb_open_on(week.entry))
        book.extend(capped)
        for row in capped:
            s = settlement_for(row["ticker"], row["entry"], row["expiry"], row["close"], closes, print_closes,
                               prices_through=prices_through)
            trades.append(grade(row, s))
    return RunResult(_frame(trades, ["entry", "variant", "structure", "rank"]),
                     _frame(suppressed, ["entry", "ticker", "variant"]), _frame(dropped, ["entry", "variant", "ticker"]))


def _frame(rows: list[dict], keys: list[str]) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    return df.sort_values(keys, kind="mergesort", na_position="first").reset_index(drop=True)
