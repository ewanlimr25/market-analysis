"""R3 section E of the ticker sheet: the flag row (DESIGN/70 §4 X2/X5, §7 `flags`, §8 line E).

Seven rows the reader sees and two exclusions the sheet acts on. The rows -- borrow, FINRA short
interest, beta to SPY, analyst changes, Form 4, the VIX term pair and the regime label -- are
printed with the date each one actually carries, which is rarely the sheet date: FINRA settles a
fortnight before it publishes, and the regime label is as of its own session. Only two of them
change anything, and only through §4: **X2** (no short-share expression when the borrow fee is in
the top decile of the day's universe or fewer than `x2_available_min` shares are available) and
**X5** (short float at or above `x5_short_float_min` marks the share line `defined-risk preferred`).

Both exclusions are one-sided: they fire on data, never on its absence. A null borrow row or a null
short float leaves `x2` / `x5` `False` *and* writes an entry in `nulls` saying the rule could not be
evaluated -- "the sheet does not know" is not "the sheet says no", and the reader is told which one
they are looking at.

Pure: frames and dicts are read, never mutated; the returned dict is strict JSON
(`engine.schema.clean`) and no missing input raises.
"""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

from engine.config import NAME_PARAMS, NameParams
from engine.name.data import NameInputs
from engine.schema import clean

BETA_WINDOW = 250                 # §7 `beta_250`: the last 250 sessions both series have ..
BETA_MIN_RETURNS = 120            # .. and at least 120 return observations inside them, else null
CONTANGO, BACKWARDATION = "contango", "backwardation"
BUY_CODE, SELL_CODE = "P", "S"    # Finnhub transaction codes: open-market purchase / sale


def _num(value) -> float | None:
    try:
        out = float(value)
    except (TypeError, ValueError):
        return None
    return None if out != out else out


def reason_for(inputs: NameInputs, field: str, default: str) -> str:
    """The loader's own reason for a null field (`NameInputs.nulls`), else `default`."""
    for entry in inputs.nulls or []:
        if entry.get("field") == field and entry.get("reason"):
            return entry["reason"]
    return default


# ---- the rows ----------------------------------------------------------------------------------

def borrow_row(borrow: dict | None) -> dict | None:
    """`{fee, available, date, decile, stale_days}` from the IBKR row; the decile is the fee's
    percent rank over that day's universe (0..1), which is what X2 reads."""
    if not borrow:
        return None
    return {"fee": _num(borrow.get("fee_rate")), "available": _num(borrow.get("available_shares")),
            "date": borrow.get("asof"), "decile": _num(borrow.get("decile")),
            "stale_days": borrow.get("stale_days")}


def si_row(si: dict | None) -> dict | None:
    """`{pct_float, dtc, settlement, publication, position}`; `pct_float` is the finviz/yfinance
    short float X5 reads, the other four are FINRA's own semi-monthly row."""
    if not si:
        return None
    return {"pct_float": _num(si.get("short_float")), "dtc": _num(si.get("days_to_cover")),
            "settlement": si.get("settlement_date"), "publication": si.get("publication_date"),
            "position": _num(si.get("current_short_position"))}


def vix_row(index_vol: dict | None) -> dict | None:
    """`{vix, vix3m, vxn, term, date}`; `term` is contango when VIX3M is above VIX, else
    backwardation, and `None` when either leg is missing (a term with one point is not a term)."""
    if not index_vol:
        return None
    vix, vix3m = _num(index_vol.get("vix")), _num(index_vol.get("vix3m"))
    term = None if vix is None or vix3m is None else (CONTANGO if vix3m > vix else BACKWARDATION)
    return {"vix": vix, "vix3m": vix3m, "vxn": _num(index_vol.get("vxn")), "term": term,
            "date": index_vol.get("date")}


def form4_counts(rows: list | None) -> dict:
    """Finnhub insider rows counted by transaction code: `P` buys, `S` sells, everything else
    (`M` option exercises, `F` tax withholding, `A` grants) in `other` -- they are not opinions."""
    rows = list(rows or [])
    codes = [str(r.get("code") or "").strip().upper() for r in rows]
    buys = sum(1 for c in codes if c == BUY_CODE)
    sells = sum(1 for c in codes if c == SELL_CODE)
    return {"buys": buys, "sells": sells, "other": len(codes) - buys - sells, "rows": rows}


def beta_250(bars: pd.DataFrame, spy_bars: pd.DataFrame, window: int = BETA_WINDOW,
             min_returns: int = BETA_MIN_RETURNS) -> tuple[float | None, int, date | None]:
    """`(OLS slope of the name's daily log returns on SPY's, the number of returns, the last
    common session)`.

    The join comes first and the returns second: a name quoted on fewer sessions than SPY is
    regressed on SPY's move over the *same* intervals, never on a one-day SPY move against a
    multi-day name move. `None` under `min_returns` observations or on a degenerate market series.
    """
    merged = _common_closes(bars, spy_bars)
    if merged is None or len(merged) < 2:
        return None, 0, None
    merged = merged.tail(window)
    last = merged["date"].iloc[-1]
    y = np.diff(np.log(merged["close"].to_numpy(dtype=float)))
    x = np.diff(np.log(merged["spy"].to_numpy(dtype=float)))
    if len(x) < min_returns:
        return None, int(len(x)), last
    sx, sy = x - x.mean(), y - y.mean()
    denom = float((sx * sx).sum())
    if denom == 0:
        return None, int(len(x)), last
    return float((sx * sy).sum() / denom), int(len(x)), last


def _common_closes(bars: pd.DataFrame, spy_bars: pd.DataFrame) -> pd.DataFrame | None:
    """`[date, close, spy]` on the sessions both series have, ascending; None when either is absent."""
    for frame in (bars, spy_bars):
        if frame is None or frame.empty or not {"date", "close"} <= set(frame.columns):
            return None
    left = bars[["date", "close"]].dropna()
    right = spy_bars[["date", "close"]].dropna().rename(columns={"close": "spy"})
    merged = left.merge(right, on="date", how="inner").sort_values("date")
    return merged[(merged["close"] > 0) & (merged["spy"] > 0)]


# ---- the two exclusions (DESIGN/70 §4; they fire on data, never on its absence) -----------------

def x2_short_share(borrow: dict | None, params: NameParams = NAME_PARAMS) -> tuple[bool, str | None, str | None]:
    """X2: `(fires, why it fired, why it could not be evaluated)`.

    Fires when the IBKR fee is in the top decile of that day's universe or fewer than
    `params.x2_available_min` shares are available to borrow. With no borrow row it is `False` and
    the third element says so: a rule that cannot see its input has not passed, it is unevaluated.
    """
    if not borrow:
        return False, None, "X2 cannot fire on a missing borrow row: it is unevaluated, not passed"
    decile, available = borrow.get("decile"), borrow.get("available")
    if decile is not None and decile >= params.x2_borrow_decile:
        return True, "borrow fee in the top decile of the day", None
    if available is not None and available < params.x2_available_min:
        return True, (f"available shares {available:,.0f} below "
                      f"{params.x2_available_min:,.0f}"), None
    if decile is None and available is None:
        return False, None, "borrow row carries neither a fee decile nor an available-share count"
    return False, None, None


def x5_short_float(si: dict | None, params: NameParams = NAME_PARAMS) -> tuple[bool, str | None]:
    """X5: `(fires, why it could not be evaluated)`. Fires at short float >=
    `params.x5_short_float_min` of float; a null short float leaves it `False` and unevaluated."""
    pct = (si or {}).get("pct_float")
    if pct is None:
        return False, ("X5 cannot fire on a missing short float: it is unevaluated, not passed")
    return bool(pct >= params.x5_short_float_min), None


# ---- the section -------------------------------------------------------------------------------

def evaluate(inputs: NameInputs, params: NameParams = NAME_PARAMS) -> dict:
    """The DESIGN/70 §7 `flags` dict for one name on one session. Never raises: an absent input is
    `None` plus a `nulls` entry, and every flag's `source` names the date the flag itself carries."""
    d = inputs.date.isoformat()
    nulls: list[dict] = []
    borrow = borrow_row(inputs.borrow)
    si = si_row(inputs.short_interest)
    vix = vix_row(inputs.index_vol)
    beta, beta_n, beta_last = beta_250(inputs.bars, inputs.spy_bars)
    regime = (inputs.regime or {}).get("label")

    if borrow is None:
        nulls.append({"field": "borrow", "reason": reason_for(inputs, "borrow", "no borrow row")})
    if si is None:
        nulls.append({"field": "si", "reason": reason_for(inputs, "short_interest", "no short-interest row")})
    elif si["pct_float"] is None:
        nulls.append({"field": "si.pct_float",
                      "reason": reason_for(inputs, "short_interest.short_float", "no short float")})
    if vix is None:
        nulls.append({"field": "vix", "reason": reason_for(inputs, "index_vol", "no index_vol row")})
    if regime is None:
        nulls.append({"field": "regime", "reason": reason_for(inputs, "regime", "no regime label")})
    if beta is None:
        nulls.append({"field": "beta_250", "reason": _beta_reason(beta_n)})

    x2, x2_reason, x2_null = x2_short_share(borrow, params)
    if x2_null:
        nulls.append({"field": "x2", "reason": x2_null})
    x5, x5_null = x5_short_float(si, params)
    if x5_null:
        nulls.append({"field": "x5", "reason": x5_null})

    return clean({
        "borrow": borrow, "si": si, "beta_250": beta, "beta_n": beta_n,
        "analyst": list(inputs.analyst or []), "analyst_n": len(inputs.analyst or []),
        "form4": form4_counts(inputs.form4), "vix": vix,
        "regime": regime, "regime_asof": (inputs.regime or {}).get("asof"),
        "regime_stale": bool((inputs.regime or {}).get("stale", False)),
        "x2": x2, "x2_reason": x2_reason, "x5": x5,
        "source": _sources(inputs, borrow, si, vix, beta_last, d),
        "nulls": nulls,
    })


def _beta_reason(n: int) -> str:
    if n == 0:
        return "no session is common to the name's bars and SPY's"
    return f"{n} common return observations, fewer than the {BETA_MIN_RETURNS} beta_250 requires"


def _sources(inputs: NameInputs, borrow: dict | None, si: dict | None, vix: dict | None,
             beta_last: date | None, d: str) -> dict:
    """Every flag's own date -- FINRA's settlement and publication, IBKR's as-of, the regime's
    session -- not the sheet date, which almost none of them carry."""
    stored = inputs.sources or {}
    return {
        "borrow": f"borrow (IBKR) {borrow['date']}" if borrow else stored.get("borrow", f"borrow (IBKR) {d}"),
        "si": (f"short_interest (FINRA) settlement {si['settlement']}, published {si['publication']}"
               f" + short float {(inputs.short_interest or {}).get('short_float_source') or 'n/a'}"
               if si else stored.get("short_interest", f"short_interest (FINRA) <= {d}")),
        "beta_250": (f"earnings_history/bars x SPY {BETA_WINDOW} sessions to "
                     f"{beta_last.isoformat() if beta_last else d}"),
        "analyst": stored.get("analyst", f"yfinance upgrades_downgrades <= {d}"),
        "form4": stored.get("form4", f"finnhub /stock/insider-transactions <= {d}"),
        "vix": f"index_vol {vix['date']}" if vix else stored.get("index_vol", f"index_vol {d}"),
        "regime": (f"_regime.classify_regime asof {(inputs.regime or {}).get('asof')}"
                   if inputs.regime else stored.get("regime", f"_regime.classify_regime {d}")),
        "x2": f"borrow (IBKR) {borrow['date']}" if borrow else f"borrow (IBKR) {d}",
        "x5": (f"short float {(inputs.short_interest or {}).get('short_float_source')}"
               if si else f"short_interest (FINRA) <= {d}"),
    }
