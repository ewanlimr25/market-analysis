"""R2 §3 of the ticker sheet: section C -- is this name's option premium rich, fair or cheap?

Every number DESIGN/70 §3 asks for, with its unit made explicit because the two conventions in
this repo differ: `iv30d` is printed as the **decimal** the screener carries, both realized vols
and both spreads are printed in **vol points** (100 x an annualized decimal), and `slope` is the
second listed expiry's ATM IV minus the first's, also in points.

    iv30d        screener, as a decimal
    iv_pct_own   percentile of today's iv30d in the name's own trailing `iv_pct_window` sessions
    rv5_21       100 x sqrt(252 x mean(intraday_rv.rv5)) over the trailing quality sessions --
                 `rv5` is a *daily realized variance* from 5-minute returns, so the window is
                 averaged and annualized once (engine/mart/intraday_rv.py). The panel lags the
                 sheet date by design; `source` carries the window's own first and last date.
    rv_c2c_21    100 x sqrt(252) x std(log close returns, ddof=0) over the last `rv_window`
                 returns ending on or before the sheet date
    spread_rv5   100 x iv30d - rv5_21          (vol points)
    spread_c2c   100 x iv30d - rv_c2c_21       (vol points)

`sc` is S-C's own `evaluate_name` verdict on this name, reported whole: the sheet grades S-C's
filters on every name the owner looks at (DESIGN/70 §6), so a failing filter is a measurement, not
a rejection. `sa` is the S-A A1 cheap-filter result when a print falls inside `sa_window_days`,
carried with the note that S-A is closed at retail execution (RESEARCH/48 G1, D23) -- also a
measurement, never a recommendation. `x1` is DESIGN/70 §4's exclusion: true when a premium
structure at the expiry S-C would use would sit on the print, or whenever the earnings sources
did not confirm.

The verdict is a label and nothing reads it: no size, no strike and no structure changes with it
(DESIGN/70 §3). It is printed beside `spread_rv5` so a reader is never handed the label alone.
"""
from __future__ import annotations

import math
from datetime import date, timedelta
from statistics import median

import numpy as np
import pandas as pd

from engine import calendar as cal
from engine.config import NAME_PARAMS, SA_PARAMS, NameParams
from engine.mart import cboe_chain_derived as derived
from engine.name import events as name_events
from engine.name.data import NameInputs
from engine.strategies import sa_filters, sc_filters
from engine.strategies.sa_filters import _num, to_date

TRADING_DAYS = 252
FRIDAY = 4
RICH, FAIR, CHEAP, CANNOT_MEASURE = "RICH", "FAIR", "CHEAP", "CANNOT_MEASURE"
IMPLIED_SOURCE = "screener implied_move_perc"
SA_FILTERS = ("F1", "F2", "F3", "F4", "F7", "F8")
SA_NOTE = ("S-A is closed at retail execution (market-analysis RESEARCH/48 G1, D23); "
           "no earnings trade is recommended")
SA_TIMING = {"pre": "premarket", "post": "postmarket"}
ETF_ISSUE_TYPE = "ETF"
SA_HOW = "labelled"
CHAIN_IV_COLUMNS = ("expiry", "strike", "iv", "underlying_price")


def evaluate(inputs: NameInputs, params: NameParams = NAME_PARAMS, events: dict | None = None) -> dict:
    """Section C of `ticker.json` for one name. `events` is `engine.name.events.evaluate`'s dict
    (the expiries the slope needs and the earnings session X1 reads); it is computed here when the
    caller has not already. Pure, and never raises: every missing input is a null with a reason."""
    events = name_events.evaluate(inputs, params) if events is None else events
    nulls: list[dict] = []
    screener = inputs.screener or {}
    iv30d = _iv30d(screener, nulls)
    rv5_21, rv5_source = _rv5_21(inputs, params, nulls)
    rv_c2c_21, c2c_source = _rv_c2c_21(inputs, params, nulls)
    history = _earnings_history(inputs, params)
    sc = _sc(inputs)
    x1 = _x1(inputs, params, events, sc)
    spread_rv5, spread_c2c = _spread(iv30d, rv5_21), _spread(iv30d, rv_c2c_21)
    return {
        "iv30d": iv30d,
        "iv_pct_own": _iv_pct_own(inputs, params, iv30d, nulls),
        "rv5_21": rv5_21, "rv_c2c_21": rv_c2c_21,
        "spread_rv5": spread_rv5, "spread_c2c": spread_c2c,
        "slope": _slope(inputs, events, nulls),
        "earnings_history": history, "median_ratio_8": _median_ratio(history),
        "sc": sc, "sa": _sa(inputs, params, events), "x1": x1,
        "verdict": _verdict(spread_rv5, spread_c2c, x1, params),
        "source": _source(inputs, events, rv5_source, c2c_source), "nulls": nulls,
    }


# --- the vol numbers --------------------------------------------------------------------------

def _iv30d(screener: dict, nulls: list[dict]) -> float | None:
    iv = _num(screener.get("iv30d"))
    if iv is None:
        nulls.append({"field": "premium.iv30d", "reason": "screener iv30d is null"})
    return iv


def _spread(iv30d: float | None, rv: float | None) -> float | None:
    """Vol points: 100 x the screener's decimal IV minus an already-annualized realized vol."""
    return None if iv30d is None or rv is None else 100.0 * iv30d - rv


def _iv_pct_own(inputs: NameInputs, params: NameParams, iv30d: float | None,
                nulls: list[dict]) -> float | None:
    """Today's iv30d as a percentile (0..100) of the name's own trailing screener history."""
    hist = inputs.screener_history
    if iv30d is None or hist is None or hist.empty or "iv30d" not in hist.columns:
        nulls.append({"field": "premium.iv_pct_own",
                      "reason": "no screener history" if iv30d is not None else "screener iv30d is null"})
        return None
    window = hist.sort_values("date").tail(params.iv_pct_window)
    values = pd.to_numeric(window["iv30d"], errors="coerce").dropna()
    if len(values) < params.iv_pct_min_sessions:
        nulls.append({"field": "premium.iv_pct_own",
                      "reason": f"{len(values)} screener sessions, fewer than "
                                f"{params.iv_pct_min_sessions}"})
        return None
    return 100.0 * float((values <= iv30d).mean())


def _rv5_21(inputs: NameInputs, params: NameParams, nulls: list[dict]) -> tuple[float | None, str]:
    """Annualized intraday realized vol over the trailing quality sessions the panel carries."""
    rv = inputs.rv
    if rv is None or rv.empty or not {"rv5", "quality"} <= set(rv.columns):
        nulls.append({"field": "premium.rv5_21", "reason": "no intraday_rv rows"})
        return None, "intraday_rv (absent)"
    quality = rv[rv["quality"].fillna(False).astype(bool)].sort_values("date").tail(params.rv_window)
    values = pd.to_numeric(quality["rv5"], errors="coerce").dropna()
    if len(values) < params.rv_min_sessions:
        nulls.append({"field": "premium.rv5_21",
                      "reason": f"{len(values)} quality intraday_rv sessions, fewer than "
                                f"{params.rv_min_sessions}"})
        return None, f"intraday_rv ({len(values)} quality sessions)"
    window = quality.loc[values.index, "date"]
    span = f"{_iso(window.min())}..{_iso(window.max())}"
    return (100.0 * math.sqrt(TRADING_DAYS * float(values.mean())),
            f"intraday_rv rv5, {len(values)} quality sessions {span} (the panel lags the sheet date)")


def _rv_c2c_21(inputs: NameInputs, params: NameParams, nulls: list[dict]) -> tuple[float | None, str]:
    """Annualized close-to-close vol over the last `rv_window` returns ending on the sheet date."""
    bars = inputs.bars
    if bars is None or bars.empty or not {"date", "close"} <= set(bars.columns):
        nulls.append({"field": "premium.rv_c2c_21", "reason": "no daily bars"})
        return None, "daily bars (absent)"
    past = bars[bars["date"] <= inputs.date].sort_values("date")
    closes = pd.to_numeric(past["close"], errors="coerce").dropna()
    returns = np.log(closes).diff().dropna().tail(params.rv_window)
    if len(returns) < params.rv_min_sessions:
        nulls.append({"field": "premium.rv_c2c_21",
                      "reason": f"{len(returns)} close-to-close returns, fewer than "
                                f"{params.rv_min_sessions}"})
        return None, f"daily bars ({len(returns)} returns)"
    value = 100.0 * float(returns.std(ddof=0)) * math.sqrt(TRADING_DAYS)
    span = f"{_iso(past['date'].iloc[-len(returns)])}..{_iso(past['date'].iloc[-1])}"
    return value, f"daily bars close-to-close, {len(returns)} returns {span}"


def _slope(inputs: NameInputs, events: dict, nulls: list[dict]) -> float | None:
    """ATM IV at the second listed expiry minus the first, in vol points; needs a live chain."""
    chain = inputs.chain
    expiries = [e for e in (to_date(x) for x in (events.get("expiries") or [])) if e]
    if chain is None or chain.empty or not set(CHAIN_IV_COLUMNS) <= set(chain.columns):
        nulls.append({"field": "premium.slope", "reason": "no live chain to read ATM IV from"})
        return None
    if len(expiries) < 2:
        nulls.append({"field": "premium.slope", "reason": "fewer than two listed expiries"})
        return None
    ivs = [derived.atm_iv(chain, e) for e in expiries[:2]]
    if any(v is None for v in ivs):
        nulls.append({"field": "premium.slope", "reason": "an expiry has no priced ATM contract"})
        return None
    return 100.0 * (ivs[1] - ivs[0])


def _iso(value) -> str | None:
    day = to_date(value) if value is not None else None
    return day.isoformat() if day is not None and not pd.isna(day) else None


# --- the prior-print table --------------------------------------------------------------------

def _earnings_history(inputs: NameInputs, params: NameParams) -> list[dict]:
    """One row per prior print: implied move, realized move and their ratio, oldest first.

    The `earnings_events` panel is the authority (it carries the screener's implied move beside
    the realized one); `earnings_history.events` only fills in prints the panel has no row for,
    and those rows carry a null `implied_move` -- a realized move without an implied one is a
    fact, an implied move invented for it would not be.
    """
    rows: dict[date, dict] = {}
    for record in _records(inputs.earnings_events):
        day = to_date(record.get("E")) if record.get("E") is not None else None
        if day is None:
            continue
        implied, realized = _num(record.get("implied_move_perc")), _abs(record.get("realized_move"))
        rows[day] = {"E": day.isoformat(), "implied_move": implied,
                     "implied_source": IMPLIED_SOURCE, "realized_move": realized,
                     "ratio": _ratio(realized, implied)}
    for record in _records(inputs.earnings_history):
        day = to_date(record.get("E")) if record.get("E") is not None else None
        if day is None or day in rows:
            continue
        realized = _first(record, ("abs_move_yahoo", "realized_move_yahoo", "panel_realized_move"))
        rows[day] = {"E": day.isoformat(), "implied_move": None, "implied_source": None,
                     "realized_move": realized, "ratio": None}
    ordered = [rows[d] for d in sorted(rows)]
    return ordered[-params.earnings_history_n:]


def _records(frame: pd.DataFrame | None) -> list[dict]:
    return [] if frame is None or frame.empty or "E" not in frame.columns else frame.to_dict("records")


def _abs(value) -> float | None:
    number = _num(value)
    return None if number is None else abs(number)


def _first(record: dict, keys) -> float | None:
    return next((v for v in (_abs(record.get(k)) for k in keys) if v is not None), None)


def _ratio(realized: float | None, implied: float | None) -> float | None:
    return None if realized is None or not implied else realized / implied


def _median_ratio(history: list[dict]) -> float | None:
    ratios = [r["ratio"] for r in history if r["ratio"] is not None]
    return float(median(ratios)) if ratios else None


# --- S-C, S-A, X1 and the verdict ---------------------------------------------------------------

def _sc(inputs: NameInputs) -> dict:
    """S-C's own F1..F9 verdict on this name, reported whole (DESIGN/70 §6: the sheet grades the
    filters, it does not obey them). S-C's frozen parameters are used as they stand."""
    row = {**(inputs.screener or {}), "adv_usd_20d": inputs.adv_usd_20d}
    ev = sc_filters.evaluate_name(row, inputs.contracts_today, inputs.date, cal.is_trading_day)
    return {"pass": bool(sc_filters.passed_all(ev)), "failing": ev["reason"],
            "expiry": ev["expiry"].isoformat() if ev["expiry"] else None,
            "dte_cal": int(ev["dte_cal"]) if ev["dte_cal"] is not None else None,
            "sigma_hold": _num(ev["sigma_hold"]),
            "verdicts": {f: (None if ev[f] is None else bool(ev[f]))
                         for f in sc_filters.FILTER_ORDER}}


def premium_expiry(sc: dict, d: date, params: NameParams) -> date:
    """The expiry a premium structure would use: S-C's own when it reached one, else the Friday
    on or after `d + dir_target_dte_cal` (DESIGN/70 §5's expiry rule, without the listed check)."""
    chosen = to_date(sc["expiry"]) if sc.get("expiry") else None
    if chosen is not None:
        return chosen
    target = d + timedelta(days=params.dir_target_dte_cal)
    return target + timedelta(days=(FRIDAY - target.weekday()) % 7)


def _x1(inputs: NameInputs, params: NameParams, events: dict, sc: dict) -> bool:
    """DESIGN/70 §4 X1: no premium structure whose expiry sits on or after the next print, and a
    null or disagreeing earnings date is treated as a print tomorrow for `x1_unknown_earnings_days`.

    Build-time amendment B2 (findings/stock-deep-dive DESIGN/70 §12): an ETF has no earnings print,
    so the null-date rule does not apply to `issue_type == "ETF"` (L1 admits ETFs; without this every
    ETF sheet was X1 forever)."""
    if (inputs.screener or {}).get("issue_type") == ETF_ISSUE_TYPE:
        return False
    if not (events.get("earnings") or {}).get("confirmed"):
        return True
    window_end = to_date(events.get("x1_window_end")) if events.get("x1_window_end") else None
    return window_end is not None and window_end <= premium_expiry(sc, inputs.date, params)


def _sa(inputs: NameInputs, params: NameParams, events: dict) -> dict | None:
    """The S-A A1 cheap filters as a measurement when a print falls inside `sa_window_days`."""
    days_to = (events.get("earnings") or {}).get("days_to")
    if days_to is None or not 0 <= days_to <= params.sa_window_days:
        return None
    screener = inputs.screener or {}
    timing = SA_TIMING.get((events.get("earnings") or {}).get("session"), "unknown")
    row = {"spot_pre": screener.get("close"), "marketcap": screener.get("marketcap"),
           "adv_usd_20d": inputs.adv_usd_20d, "implied_move_perc": screener.get("implied_move_perc"),
           "issue_type": screener.get("issue_type"), "timing": timing, "how": SA_HOW}
    verdicts = sa_filters.cheap_filters(row, SA_PARAMS)
    return {"window_days": params.sa_window_days, "days_to": int(days_to), "timing": timing,
            "filters": {f: bool(verdicts[f]) for f in SA_FILTERS},
            "first_fail": next((f for f in SA_FILTERS if not verdicts[f]), None),
            "note": SA_NOTE,
            "source": f"engine.strategies.sa_filters.cheap_filters on SA_PARAMS, "
                      f"screener {inputs.date.isoformat()}"}


def _verdict(spread_rv5: float | None, spread_c2c: float | None, x1: bool,
             params: NameParams) -> str:
    """DESIGN/70 §3's table. A label only: nothing downstream reads it."""
    if spread_rv5 is None:
        return CANNOT_MEASURE
    if (spread_rv5 >= params.rich_spread_rv5 and spread_c2c is not None
            and spread_c2c >= params.rich_spread_c2c and not x1):
        return RICH
    if (spread_rv5 <= params.cheap_spread_rv5
            or (spread_c2c is not None and spread_c2c <= params.cheap_spread_c2c)):
        return CHEAP
    return FAIR


def _source(inputs: NameInputs, events: dict, rv5_source: str, c2c_source: str) -> dict:
    day, known = inputs.date.isoformat(), inputs.sources or {}
    screener = known.get("screener", f"screener {day}")
    return {
        "iv30d": f"{screener} (a decimal, as the screener carries it)",
        "iv_pct_own": known.get("screener_history", f"screener history to {day}"),
        "rv5_21": rv5_source, "rv_c2c_21": c2c_source,
        "spread_rv5": f"vol points: 100 x iv30d ({screener}) - rv5_21 ({rv5_source})",
        "spread_c2c": f"vol points: 100 x iv30d ({screener}) - rv_c2c_21 ({c2c_source})",
        "slope": f"{known.get('chain', 'cboe_chain')} ATM IV at "
                 f"{' then '.join(events.get('expiries') or ['(no expiries)'])}, vol points",
        "earnings_history": f"{known.get('earnings_events', 'earnings_events')} + "
                            f"{known.get('earnings_history', 'earnings_history/events.parquet')}",
        "sc": f"engine.strategies.sc_filters.evaluate_name on SC_PARAMS, daily_contract {day}",
        "sa": f"engine.strategies.sa_filters.cheap_filters on SA_PARAMS, screener {day}",
    }
