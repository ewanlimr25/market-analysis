"""The ticker-sheet input fixtures: three real names on 2026-09-18, loaded offline.

`tests/fixtures/name/<TICKER>/<DATE>/` is `engine.name.data.write_inputs` output from a live
`load_inputs(..., online=True)` run on 2026-09-20, trimmed so each directory stays small: the chain
to the 6 nearest expiries and both bar series to 2 years (`sources` says so on the trimmed fields).
Everything else -- `universe_today`'s 6,310 screener rows included -- is whole.

The three names are chosen against `findings/stock-deep-dive/RESEARCH/20 §1.2` and DESIGN/70 §2:

| ticker | why |
|---|---|
| `NVDA` | the liquid one: 2,051 contracts on the day, clears every L1..L6 floor, fails S-C F3 and F6 |
| `BL`   | the thin one: 15 contracts on the day, fails L3 (< 300) -- a `CANNOT_PRICE` sheet |
| `OKLO` | mcap $7.4B and `iv30d` 0.697: inside S-C's F3 and F6 bands, but no 5-lot ATM pair at the monthly (S-C F8, sheet L6 under B1) |

No test that uses these touches the network or `~/Documents/Stocks`.
"""
from __future__ import annotations

import os

from engine.name.data import NameInputs, read_inputs

FIXTURE_TICKERS = ("NVDA", "BL", "OKLO")
FIXTURE_DATE = "2026-09-18"
FIXTURE_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures", "name")


def fixture_dir(ticker: str, d: str = FIXTURE_DATE) -> str:
    return os.path.join(FIXTURE_ROOT, ticker.upper(), d)


def load_fixture(ticker: str, d: str = FIXTURE_DATE) -> NameInputs:
    """The stored `NameInputs` for one fixture name. Raises `FileNotFoundError` when it is absent
    (a missing fixture is a broken checkout, not a null the sheet should paper over)."""
    path = fixture_dir(ticker, d)
    if not os.path.isdir(path):
        raise FileNotFoundError(f"no name fixture at {path}")
    return read_inputs(path)
