"""Synthetic S-C inputs shared by the R3 and R5 tests: a four-name universe (AAA and BBB pass, CCC fails
F3 with a priceable pair, DDD fails F8), $1-grid chains with an ATM 50 pair, fixed model wings."""
from __future__ import annotations

from datetime import date

import pandas as pd

from engine import marking as M
from engine.strategies import sc as SC


def is_session(d: date) -> bool:
    return d.weekday() < 5


def screener(ticker: str, **over) -> dict:
    base = {"ticker": ticker, "issue_type": "Common Stock", "is_index": False, "close": 50.0, "marketcap": 5e9,
            "adv_usd_20d": 120e6, "iv30d": 0.45, "next_earnings_date": date(2027, 1, 29), "sector": "Healthcare"}
    return {**base, **over}


def contract(u: str, typ: str, k: float, exp: date, vwap: float, size: int = 40, spread: float = 0.05) -> dict:
    return {"underlying_symbol": u, "option_chain_id": f"{u}{exp:%y%m%d}{typ[0].upper()}{int(k * 1000):08d}",
            "option_type": typ, "strike": k, "expiry": exp, "size_late": size, "vwap_late": vwap,
            "late_rel_spread": spread, "late_last_bid": None, "late_last_ask": None, "last_nbbo_bid": None,
            "last_nbbo_ask": None}


def chain(u: str, exp: date, atm_size: int = 40, spread: float = 0.05) -> list[dict]:
    rows = [contract(u, "call", 50.0, exp, 3.00, atm_size, spread), contract(u, "put", 50.0, exp, 2.80, atm_size, spread)]
    return rows + [contract(u, t, float(k), exp, 1.0) for k in range(45, 56) if k != 50 for t in ("call", "put")]


class Wings:
    def mark(self, contract, d, when):
        return M.Mark(0.30 if contract.option_type == "call" else 0.40, 0.05, 3, M.SOURCE_MODEL)


def week(entry: date, exp: date, spread_by_name: dict[str, float] | None = None) -> SC.WeekInput:
    spread_by_name = spread_by_name or {"AAA": 0.04, "BBB": 0.05}
    universe = pd.DataFrame([screener("AAA"), screener("BBB", sector="Technology"),
                             screener("CCC", marketcap=40e9), screener("DDD")])
    rows = chain("CCC", exp)                                                # F3 fails; the pair prices
    for name, spread in spread_by_name.items():
        rows += chain(name, exp, spread=spread)
    rows += [{**r, "size_late": 2} for r in chain("DDD", exp)]              # F8: nothing prints 5 lots
    return SC.WeekInput(entry, universe, pd.DataFrame(rows), lambda names: Wings())
