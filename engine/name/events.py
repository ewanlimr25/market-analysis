"""R2 of the ticker sheet: section B, the dated things that constrain an expiry (DESIGN/70 §1, §7).

**Earnings-session agreement rule** (decided before any row was read, 2026-09-20):

    Each source `(date, hour)` maps to a set of plausible *earnings sessions* -- the first session
    whose close reflects the print:

        `bmo`                 -> {date}
        `amc`                 -> {next_session(date)}
        unknown / None hour   -> {date, next_session(date)}
        a null date           -> no set

    `confirmed` is true iff Finnhub (the primary) is non-null AND the intersection of all non-null
    sources' sets is non-empty. `earnings.session` is that intersection's earliest element and
    `earnings.date` is the primary's date. The `session` field of the section is `"pre"` for bmo,
    `"post"` for amc and `"unknown"` otherwise, taken from the primary. `days_to` is calendar days
    from the sheet date to the session.

Why sessions and not dates: the three feeds disagree by a day *by construction* -- Finnhub dates an
after-close print on the day it is announced, the screener's `next_earnings_date` on the session
that reacts to it. Comparing raw dates would mark an agreeing pair as a disagreement and hand X1 a
45-day block it has not earned; comparing the sessions the print can first be priced in compares
the thing X1 actually cares about. A genuine disagreement (BL: Finnhub 11-04 amc, screener 11-05,
yfinance 11-03) still fails, and fails closed.

The section reports the resolved session as `session_date` beside the `pre`/`post` label so the
sheet can print both; `x1_window_end` is the date through which X1 blocks a premium structure --
the earnings session when confirmed, else `date + x1_unknown_earnings_days` (DESIGN/70 §4 X1).
"""
from __future__ import annotations

from datetime import date, timedelta

import pandas as pd

from engine import calendar as cal
from engine.config import NAME_PARAMS, NameParams
from engine.name.data import NameInputs

SOURCE_NAMES = ("finnhub", "screener", "yfinance")
PRIMARY = "finnhub"
HOURS_PRE = ("bmo", "pre", "premarket", "before_market_open", "before market open")
HOURS_POST = ("amc", "post", "postmarket", "after_market_close", "after market close")
SESSION_PRE, SESSION_POST, SESSION_UNKNOWN = "pre", "post", "unknown"
FOMC = "FOMC"


def _to_date(value) -> date | None:
    """A date / Timestamp / ISO string to `datetime.date`; None for null, NaT or unparseable."""
    if value is None or value == "" or value is pd.NaT:
        return None
    try:
        stamp = pd.Timestamp(value)
    except (TypeError, ValueError):
        return None
    return None if pd.isna(stamp) else stamp.date()


def session_label(hour) -> str:
    """`pre` / `post` / `unknown` from a source's hour field, whatever its spelling."""
    text = str(hour).strip().lower() if hour is not None else ""
    if text in HOURS_PRE:
        return SESSION_PRE
    if text in HOURS_POST:
        return SESSION_POST
    return SESSION_UNKNOWN


def session_set(d, hour) -> set[date] | None:
    """The plausible earnings sessions for one source's `(date, hour)`; None when the date is null.

    A `bmo` date that is not itself a session (a weekend or a holiday) rolls forward to the next
    one: the close that first reflects the print is what the set names, never the calendar day.
    """
    day = _to_date(d)
    if day is None:
        return None
    own = day if cal.is_trading_day(day) else cal.next_session(day)
    label = session_label(hour)
    if label == SESSION_PRE:
        return {own}
    if label == SESSION_POST:
        return {cal.next_session(day)}
    return {own, cal.next_session(day)}


def evaluate(inputs: NameInputs, params: NameParams = NAME_PARAMS) -> dict:
    """Section B of `ticker.json`: the earnings session, the ex-dividend date, the first two
    listed expiries and the FOMC dates inside the window, plus the X1 window end.

    Never raises: a source that is null, a chain that is absent and an unparseable dividend date
    are all nulls with a reason. Pure -- `inputs` is not mutated.
    """
    nulls: list[dict] = []
    earnings = _earnings(inputs, nulls)
    expiries, expiry_source = _expiries(inputs, params, nulls)
    return {
        "earnings": earnings,
        "ex_div": _ex_div(inputs, nulls),
        "expiries": expiries,
        "macro": [{"date": d, "event": FOMC} for d in (inputs.fomc or [])],
        "x1_window_end": _x1_window_end(inputs, earnings, params),
        "source": _source(inputs, expiry_source),
        "nulls": nulls,
    }


# --- the earnings block ----------------------------------------------------------------------------

def _earnings(inputs: NameInputs, nulls: list[dict]) -> dict:
    """The three opinions, the session they agree on (if any), and whether the rule confirms it."""
    raw = inputs.earnings_dates or {}
    opinions = {name: (raw.get(name) or {}) for name in SOURCE_NAMES}
    sets = {name: session_set(v.get("date"), v.get("hour")) for name, v in opinions.items()}
    known = [s for s in sets.values() if s]
    agreed = set.intersection(*known) if known else set()
    primary = opinions[PRIMARY]
    primary_date = _to_date(primary.get("date"))
    confirmed = primary_date is not None and bool(agreed)
    session = min(agreed) if agreed else (min(sets[PRIMARY]) if sets[PRIMARY] else None)
    if primary_date is None:
        nulls.append({"field": "events.earnings.date",
                      "reason": primary.get("reason") or "finnhub /calendar/earnings gave no date"})
    elif not agreed:
        nulls.append({"field": "events.earnings.confirmed",
                      "reason": "the earnings sources disagree on the session: "
                                + ", ".join(f"{n} {opinions[n].get('date')} {opinions[n].get('hour')}"
                                            for n in SOURCE_NAMES if sets[n])})
    return {
        "date": primary_date.isoformat() if primary_date else None,
        "session": session_label(primary.get("hour")) if primary_date else None,
        "session_date": session.isoformat() if session else None,
        "sources": [{"name": n, "date": _iso(opinions[n].get("date")),
                     "hour": opinions[n].get("hour")} for n in SOURCE_NAMES],
        "confirmed": confirmed,
        "days_to": (session - inputs.date).days if session else None,
    }


def _iso(value) -> str | None:
    day = _to_date(value)
    return day.isoformat() if day else None


# --- ex-dividend, expiries, X1 ---------------------------------------------------------------------

def _ex_div(inputs: NameInputs, nulls: list[dict]) -> str | None:
    """The screener's next dividend date when it is still ahead of the sheet date, else null."""
    raw = (inputs.screener or {}).get("next_dividend_date")
    day = _to_date(raw)
    if day is None:
        nulls.append({"field": "events.ex_div",
                      "reason": "screener next_dividend_date is null" if raw in (None, "")
                                else f"screener next_dividend_date is not a date: {raw!r}"})
        return None
    return day.isoformat() if day > inputs.date else None


def _expiries(inputs: NameInputs, params: NameParams, nulls: list[dict]) -> tuple[list[str], str]:
    """The first two listed expiries at least `slope_min_dte_cal` calendar days out.

    The live chain is the authority on what is listed; `contracts_today` (only the expiries that
    actually printed) is the fallback when there is no chain.
    """
    chain, day = inputs.chain, inputs.date
    frame, source = (chain, "chain") if chain is not None and not chain.empty \
        else (inputs.contracts_today, "daily_contract")
    if frame is None or frame.empty or "expiry" not in frame.columns:
        nulls.append({"field": "events.expiries",
                      "reason": "no chain and no daily_contract rows to list expiries from"})
        return [], "none"
    listed = sorted({e for e in (_to_date(x) for x in frame["expiry"].dropna().unique()) if e})
    ahead = [e for e in listed if (e - day).days >= params.slope_min_dte_cal][:2]
    if len(ahead) < 2:
        nulls.append({"field": "events.expiries",
                      "reason": f"fewer than two listed expiries {params.slope_min_dte_cal}+ "
                                f"calendar days out on {source}"})
    return [e.isoformat() for e in ahead], source


def _x1_window_end(inputs: NameInputs, earnings: dict, params: NameParams) -> str:
    """X1's last blocked date: the earnings session when confirmed, else the unknown-earnings window."""
    if earnings["confirmed"] and earnings["session_date"]:
        return earnings["session_date"]
    return (inputs.date + timedelta(days=params.x1_unknown_earnings_days)).isoformat()


def _source(inputs: NameInputs, expiry_source: str) -> dict:
    day, known = inputs.date.isoformat(), inputs.sources or {}
    chain = known.get("chain", "cboe_chain")
    return {
        "earnings": known.get("earnings_dates",
                              "finnhub /calendar/earnings + screener next_earnings_date + yfinance calendar"),
        "ex_div": known.get("screener", f"screener {day}"),
        "expiries": chain if expiry_source == "chain"
                    else (f"daily_contract {day}" if expiry_source == "daily_contract" else "none"),
        "macro": known.get("fomc", "FOMC published calendar (engine.name.data.FOMC_DATES)"),
    }
