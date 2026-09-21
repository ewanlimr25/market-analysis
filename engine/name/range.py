"""R3 section D of the ticker sheet: the range block (DESIGN/70 §4D, §7 `range`, §8 line D).

Five numbers and their sources: the front-expiry ATM straddle (the 1σ box to that expiry, in
dollars), the 1σ box to 21 sessions from `sc_filters.sigma_hold`, Wilder ATR(14) from the daily
bars, the chain's total gamma exposure with its sign, and the zero-gamma strike. Nothing here
decides anything -- §4 says only X1..X6 change a structure or a size, and none of them reads this
block; it is the scale the reader measures a structure's width against.

`zero_gamma` is **the strike nearest spot at which cumulative GEX over ascending strikes changes
sign**, `None` when the running total never changes sign. This is deliberately *not*
`uw gex`'s zero-gamma level, which is the *first* ascending crossing and on NVDA 2026-09-18 reports
68.58 -- a strike 70% below spot that no reader would call the gamma flip (DECISIONS D10: the uw
definition is a definition, not a bug, and it is why this block computes GEX from the full CBOE
chain and never prints `uw gex`'s ZGL). Every crossing is reported in `zero_gamma_all_crossings`
so a reader can see the others and judge the choice.

Pure: every input frame is read, never mutated, and the returned dict is strict JSON
(`engine.schema.clean`) with dates as ISO strings. A missing input is a `None` plus an entry in
`nulls`, never an exception.
"""
from __future__ import annotations

from datetime import date

import pandas as pd

from engine import marking
from engine.config import NAME_PARAMS, NameParams
from engine.mart import cboe_chain_derived as derived
from engine.name.data import NameInputs
from engine.schema import clean
from engine.strategies import sc_filters
from engine.watch import indicators

BOX_21_DTE_CAL = 30                 # "1σ 21d": 21 sessions ~ 30 calendar days (DESIGN/70 §8 line D)
LIVE_CHAIN_SOURCE = "cboe_chain"
CALL, PUT = "C", "P"                # the chain's spelling
DC_CALL, DC_PUT = "call", "put"     # `daily_contract`'s spelling of the same thing


def _as_date(value) -> date | None:
    if value is None or isinstance(value, date):
        return value if not isinstance(value, pd.Timestamp) else value.date()
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def _num(value) -> float | None:
    """A finite float, or None for anything else (NaN, None, a string that is not a number)."""
    try:
        out = float(value)
    except (TypeError, ValueError):
        return None
    return None if out != out or out in (float("inf"), float("-inf")) else out


# ---- the pure pieces ---------------------------------------------------------------------------

def sign_crossings(strikes: list[float], cumulative: list[float]) -> list[float]:
    """Every strike whose cumulative GEX carries the opposite sign to the last non-zero one before
    it, ascending. A cumulative value of exactly zero is neither sign and starts no crossing."""
    out, last = [], 0.0
    for k, c in zip(strikes, cumulative):
        sign = (c > 0) - (c < 0)
        if sign and last and sign != last:
            out.append(float(k))
        last = sign or last
    return out


def zero_gamma(per_strike: pd.DataFrame, spot: float | None) -> tuple[float | None, list[float]]:
    """`(the crossing nearest spot, every crossing)` over ascending strikes (D10; see the module
    docstring). Without a spot the nearest cannot be chosen and only the list is returned."""
    if per_strike is None or per_strike.empty:
        return None, []
    ordered = per_strike.sort_values("strike")
    crossings = sign_crossings(ordered["strike"].tolist(), ordered["gex"].cumsum().tolist())
    if not crossings or spot is None:
        return None, crossings
    return min(crossings, key=lambda k: abs(k - spot)), crossings


def gex_sign(total: float | None) -> str | None:
    """`"+"` / `"-"`; `None` for a null total and for an exact zero (which has no sign)."""
    if total is None or total == 0:
        return None
    return "+" if total > 0 else "-"


def straddle_from_chain(chain: pd.DataFrame, expiry: date, spot: float, chain_date: str) -> dict | None:
    """The ATM straddle at `expiry` from live quotes: the strike nearest `spot` at which both a
    call and a put carry a mid. `mark` is call mid + put mid, in dollars of underlying."""
    sub = chain[chain["expiry"] == expiry].dropna(subset=["strike", "mid"])
    if sub.empty:
        return None
    legs = {r: sub[sub["right"] == r].set_index("strike")["mid"].to_dict() for r in (CALL, PUT)}
    strike = _nearest_both(legs[CALL], legs[PUT], spot)
    if strike is None:
        return None
    return {"expiry": expiry.isoformat(), "strike": float(strike),
            "mark": float(legs[CALL][strike]) + float(legs[PUT][strike]),
            "mark_source": f"{LIVE_CHAIN_SOURCE} {chain_date}", "tier": None}


def straddle_from_contracts(rows: pd.DataFrame, expiry: date, spot: float,
                            params: NameParams = NAME_PARAMS) -> dict | None:
    """The same pair from the day's `daily_contract` rows, marked by `marking.print_mark(row,
    "late")` at tier <= `params.atm_tier_max`. A pair with no late print on one leg is not a pair."""
    if rows is None or rows.empty or "option_type" not in rows.columns:
        return None
    sub = rows[rows["expiry"] == expiry]
    marks = {}
    for spelling, right in ((DC_CALL, CALL), (DC_PUT, PUT)):
        side = {}
        for row in sub[sub["option_type"] == spelling].to_dict("records"):
            mark = marking.print_mark(row, marking.WHEN_LATE)
            strike = _num(row.get("strike"))
            if mark is not None and mark.tier <= params.atm_tier_max and strike is not None:
                side[strike] = mark
        marks[right] = side
    strike = _nearest_both(marks[CALL], marks[PUT], spot)
    if strike is None:
        return None
    call, put = marks[CALL][strike], marks[PUT][strike]
    tier = max(call.tier, put.tier)
    return {"expiry": expiry.isoformat(), "strike": float(strike), "mark": call.price + put.price,
            "mark_source": f"daily_contract tier {tier}", "tier": tier}


def front_expiry(inputs: NameInputs, params: NameParams = NAME_PARAMS,
                 events: dict | None = None) -> tuple[date | None, str, str | None]:
    """`(the front expiry, its source, a reason when there is none)`.

    R2's `events.expiries[0]` when the sheet already chose one, else the nearest listed expiry with
    at least `params.slope_min_dte_cal` calendar days to run (the same 7-day floor §3 puts on the
    term-slope expiries: an expiry inside a week is a gamma instrument, not a range).
    """
    listed = (events or {}).get("expiries") or []
    chosen = _as_date(listed[0]) if listed else None
    if chosen is not None:
        return chosen, f"events.expiries[0] {chosen.isoformat()}", None
    min_dte = params.slope_min_dte_cal
    chain, meta = inputs.chain, inputs.chain_meta or {}
    if chain is not None and not chain.empty and "expiry" in chain.columns:
        far = chain[[_dte(e, inputs.date) >= min_dte for e in chain["expiry"]]]
        expiry = derived.front_expiry(far)
        if expiry is not None:
            return _as_date(expiry), f"{meta.get('source') or 'chain'} {meta.get('date')}", None
    rows = inputs.contracts_today
    if rows is not None and not rows.empty and "expiry" in rows.columns:
        far = [_as_date(e) for e in rows["expiry"] if _dte(e, inputs.date) >= min_dte]
        if far:
            return min(far), f"daily_contract {inputs.date.isoformat()}", None
    return None, f"daily_contract {inputs.date.isoformat()}", (
        f"no listed expiry at least {min_dte} calendar days out on the chain or in the day's contracts")


def _dte(expiry, d: date) -> int:
    e = _as_date(expiry)
    return -1 if e is None else (e - d).days


def _nearest_both(calls: dict, puts: dict, spot: float) -> float | None:
    both = sorted(set(calls) & set(puts), key=lambda k: (abs(k - spot), k))
    return both[0] if both else None


def atr14(bars: pd.DataFrame, d: date, n: int = indicators.ATR_PERIOD) -> tuple[float | None, date | None]:
    """`(Wilder ATR(n) at the last bar on or before `d`, that bar's date)`. `(None, last)` when
    fewer than `n + 1` bars are available -- Wilder needs `n` true ranges and a true range needs a
    previous close."""
    if bars is None or bars.empty or not {"high", "low", "close", "date"} <= set(bars.columns):
        return None, None
    sub = bars[bars["date"] <= d].dropna(subset=["high", "low", "close"]).sort_values("date")
    if sub.empty:
        return None, None
    last = _as_date(sub["date"].iloc[-1])
    series = indicators.wilder_atr_series(sub["high"].astype(float).tolist(),
                                          sub["low"].astype(float).tolist(),
                                          sub["close"].astype(float).tolist(), n)
    return (series[-1] if series else None), last


def spot_price(inputs: NameInputs) -> tuple[float | None, str, str | None]:
    """The reference price the ATM strike and `zero_gamma` are measured against: the screener close
    (DESIGN/70 §4D), else the chain's underlying, else the day's contract rows."""
    d = inputs.date.isoformat()
    close = _num((inputs.screener or {}).get("close"))
    if close is not None:
        return close, f"screener {d}", None
    chain, meta = inputs.chain, inputs.chain_meta or {}
    if chain is not None and not chain.empty and "underlying_price" in chain.columns:
        under = _num(chain["underlying_price"].dropna().iloc[0]) if chain["underlying_price"].notna().any() else None
        if under is not None:
            return under, f"{meta.get('source') or 'chain'} {meta.get('date') or d}", None
    rows = inputs.contracts_today
    if rows is not None and not rows.empty and "underlying_last" in rows.columns:
        last = _num(rows["underlying_last"].dropna().iloc[0]) if rows["underlying_last"].notna().any() else None
        if last is not None:
            return last, f"daily_contract {d}", None
    return None, f"screener {d}", "no screener row, chain or contract row carries a price"


# ---- the section -------------------------------------------------------------------------------

def evaluate(inputs: NameInputs, params: NameParams = NAME_PARAMS, events: dict | None = None) -> dict:
    """The DESIGN/70 §7 `range` dict for one name on one session.

    `events` is R2's section (its `expiries[0]` is the front expiry); with `events=None` the front
    expiry is derived here from the chain, and failing that from the day's `daily_contract` rows.
    Never raises: every field that cannot be filled is `None` with its reason in `nulls`.
    """
    d = inputs.date.isoformat()
    meta = inputs.chain_meta or {}
    chain_source = f"{meta.get('source') or 'none'} {meta.get('date') or d}"
    nulls: list[dict] = []
    spot, spot_source, spot_reason = spot_price(inputs)
    if spot_reason:
        nulls.append({"field": "spot", "reason": spot_reason})

    expiry, expiry_source, expiry_reason = front_expiry(inputs, params, events)
    straddle, straddle_reason = _straddle(inputs, params, expiry, spot)
    if straddle is None:
        nulls.append({"field": "straddle_front",
                      "reason": expiry_reason or spot_reason or straddle_reason})
        nulls.append({"field": "box_1s_front", "reason": "no front straddle to measure"})

    box_21, box_21_reason = _box_1s_21(inputs)
    if box_21_reason:
        nulls.append({"field": "box_1s_21", "reason": box_21_reason})
    atr, bars_end = atr14(inputs.bars, inputs.date)
    if atr is None:
        nulls.append({"field": "atr14", "reason": _atr_reason(inputs, bars_end)})

    gex = _gex(inputs, spot)
    nulls.extend(gex["nulls"])
    return clean({
        "straddle_front": straddle,
        "box_1s_front": None if straddle is None else straddle["mark"],
        "box_1s_21": box_21,
        "atr14": atr,
        "gex_total": gex["total"],
        "gex_sign": gex["sign"],
        "zero_gamma": gex["zero_gamma"],
        "zero_gamma_all_crossings": gex["crossings"],
        "spot": spot,
        "source": {
            "straddle_front": straddle["mark_source"] if straddle else expiry_source,
            "box_1s_front": straddle["mark_source"] if straddle else expiry_source,
            "box_1s_21": f"screener {d}",
            "atr14": f"earnings_history/bars <= {bars_end.isoformat()}" if bars_end else "earnings_history/bars",
            "gex_total": chain_source, "gex_sign": chain_source, "zero_gamma": chain_source,
            "spot": spot_source,
        },
        "nulls": nulls,
    })


def _straddle(inputs: NameInputs, params: NameParams, expiry: date | None,
              spot: float | None) -> tuple[dict | None, str | None]:
    """The front ATM straddle from the live chain, else from the day's prints, else `(None, why)`."""
    if expiry is None or spot is None:
        return None, "no front expiry or no spot price"
    meta = inputs.chain_meta or {}
    is_live = meta.get("source") == LIVE_CHAIN_SOURCE and str(meta.get("date")) == inputs.date.isoformat()
    if is_live and inputs.chain is not None and not inputs.chain.empty:
        out = straddle_from_chain(inputs.chain, expiry, spot, str(meta.get("date")))
        if out is not None:
            return out, None
    out = straddle_from_contracts(inputs.contracts_today, expiry, spot, params)
    if out is not None:
        return out, None
    stale = "" if is_live else f" (the stored chain is {meta.get('source') or 'absent'} {meta.get('date') or ''})".rstrip()
    return None, (f"no ATM call/put pair at {expiry.isoformat()} carries a quote or a tier "
                  f"<= {params.atm_tier_max} print{stale}")


def _box_1s_21(inputs: NameInputs) -> tuple[float | None, str | None]:
    """`sigma_hold(close, iv30d, 30)`: the 1σ box to 21 sessions, in dollars (DESIGN/70 §8 line D)."""
    row = inputs.screener or {}
    close, iv = _num(row.get("close")), _num(row.get("iv30d"))
    if close is None or iv is None:
        missing = "close" if close is None else "iv30d"
        return None, f"screener {missing} is null" if row else "no screener row"
    return sc_filters.sigma_hold(close, iv, BOX_21_DTE_CAL), None


def _atr_reason(inputs: NameInputs, bars_end: date | None) -> str:
    if inputs.bars is None or inputs.bars.empty:
        return "no daily bars"
    return (f"fewer than {indicators.ATR_PERIOD + 1} bars on or before {inputs.date.isoformat()}"
            if bars_end else f"no bar on or before {inputs.date.isoformat()}")


def _gex(inputs: NameInputs, spot: float | None) -> dict:
    """Total GEX, its sign and the zero-gamma strike from the full chain (DESIGN/70 §4D, D10)."""
    chain = inputs.chain
    if chain is None or chain.empty:
        reason = (inputs.chain_meta or {}).get("reason") or "no chain"
        return {"total": None, "sign": None, "zero_gamma": None, "crossings": [],
                "nulls": [{"field": "gex_total", "reason": reason},
                          {"field": "zero_gamma", "reason": reason}]}
    per_strike = derived.gex_per_strike(chain)
    total = derived.total_gex(chain)
    nulls = []
    if per_strike.empty:
        nulls.append({"field": "gex_total",
                      "reason": "no strike on the chain carries positive gamma and open interest"})
        total = None
    zgl, crossings = zero_gamma(per_strike, spot)
    if zgl is None:
        nulls.append({"field": "zero_gamma", "reason": (
            "cumulative GEX never changes sign over the listed strikes" if not crossings
            else "no spot price to choose the crossing nearest it")})
    return {"total": total, "sign": gex_sign(total), "zero_gamma": zgl,
            "crossings": crossings, "nulls": nulls}
