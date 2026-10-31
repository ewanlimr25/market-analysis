"""The ticker list the truth set (`scripts/truthset/build_prices.py`) and the FINRA loader
(`engine.mart.short_interest`) fetch: `data/universe.json` plus every name the books hold (findings
market-analysis D39, O14).

`universe.json` is the liquid gate (close >= 5 and $ADV >= 50M on any panel day). The books hold names
outside it, and both readers fail open on them: an open S-A / S-C / name-sheet row with no truth-set close
settles on the last print however fresh `prices.parquet` is, and a watch-basket name with no FINRA row
reads `days_to_cover` as null, so `C-SHORT` goes null. "Held" is therefore every ungraded ledger row of
any role (exploration rows settle too) and the watch basket's §1 universe over every panel day, a union
like `build_universe.py`'s, so a name never drops out of the list and its history never stops and restarts.

Index underlyings (`is_index` in the screener: VIX, SPX, NDX, ...) are left out: Yahoo serves them only
under a caret symbol, and a bare `VIX` request would at best fail and at worst file another security's
bars as the settlement close. They keep settling on the last print, labelled.
"""
from __future__ import annotations

import json
import os
from typing import Callable, Iterable

import pandas as pd

from engine import ledger as L
from engine.config import DATA, LEDGER_DIR, LEDGER_NAME_DIR, LEDGER_SB_DIR, LEDGER_SC_DIR

UNIVERSE_FILE = os.path.join(DATA, "universe.json")
HELD_LEDGER_DIRS = (LEDGER_DIR, LEDGER_SB_DIR, LEDGER_SC_DIR, LEDGER_NAME_DIR)


def open_tickers(signals: pd.DataFrame, graded: pd.DataFrame) -> set[str]:
    """Tickers of the signal rows with no graded row on the full ledger key (`L.KEY`), any role."""
    if signals.empty:
        return set()
    if graded.empty:
        return set(signals["ticker"].dropna())
    graded_keys = set(graded[L.KEY].astype(str).itertuples(index=False, name=None))
    keys = signals[L.KEY].astype(str).itertuples(index=False, name=None)
    is_open = [k not in graded_keys for k in keys]
    return set(signals.loc[is_open, "ticker"].dropna())


def combine(universe: Iterable, held: Iterable, indices: Iterable) -> list[str]:
    """Sorted union of the universe and the held names, without index underlyings or blank tickers."""
    names = {t for t in (*universe, *held) if isinstance(t, str) and t}
    return sorted(names - set(indices))


def held_ledger_tickers(ledger_dirs: Iterable[str] = HELD_LEDGER_DIRS) -> set[str]:
    """Open tickers across the ledgers; a ledger never written holds nothing."""
    held: set[str] = set()
    for d in ledger_dirs:
        held |= open_tickers(L.read_signals(d), L.read_ledger(d))
    return held


def _panel_dates() -> list:
    from engine.mart import store
    return store.available_dates("daily_contract")


def basket_universe_tickers() -> set[str]:
    """The watch basket's §1 universe (`engine.watch.universe`) on any panel day."""
    from engine.watch import universe as U
    return set(U.build_universe(_panel_dates())["ticker"])


def screener_index_tickers() -> set[str]:
    """Every ticker the screener flags `is_index` on any panel day."""
    from engine.watch import universe as U
    panel = U.load_screener_panel(_panel_dates())
    return set(panel.loc[panel["is_index"].fillna(False).astype(bool), "ticker"])


def _read_universe(path: str) -> list[str]:
    if not os.path.exists(path):
        return []
    with open(path) as fh:
        return json.load(fh)


def load(universe_path: str = UNIVERSE_FILE, ledger_dirs: Iterable[str] = HELD_LEDGER_DIRS,
         basket_tickers: Callable[[], set[str]] = basket_universe_tickers,
         index_tickers: Callable[[], set[str]] = screener_index_tickers) -> list[str]:
    """The fetch list: `universe_path` plus the open ledger rows plus the basket universe, less indices."""
    held = held_ledger_tickers(ledger_dirs) | basket_tickers()
    return combine(_read_universe(universe_path), held, index_tickers())
