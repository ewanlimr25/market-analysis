"""Finviz short-interest fields via the `fz` CLI (`fz quote --agent <TICKER>`), for on-demand,
single-ticker use only (RESEARCH/47 §2 G9; RESEARCH/20 §10).

`fz` (`~/printing-press/library/finviz/finviz-pp-cli`) scrapes Finviz's quote page, which carries an
84-field grid including `Short Float`, `Short Ratio` and `Short Interest` -- confirmed present in the
live HTML fetched directly from `finviz.com/quote.ashx?t=AAPL` (all 84 `snapshot-td2` cells, verified
2026-09-07). **But** the CLI's own JSON output (`fz quote --agent AAPL|TSLA|GME`, both cached and
`--no-cache --data-source live`) returns only a fixed 14-key `fundamentals` subset (Book/sh, Cash/sh,
the dividend fields, Employees, Enterprise Value, IPO, Income, Index, Market Cap, Payout, Sales) on
every ticker tried -- no P/E, no RSI, no `Short Float`/`Short Ratio`/`Short Interest`, and the same 14
keys appear verbatim across three unrelated names. That is a regression in `fz`'s own quote parser (it
lives in `~/printing-press`, a separate repo -- fixing it is out of scope here), not a missing-data
condition on Finviz's side. `short_float` still calls the documented interface, as specified, and fails
soft with the reason above when the fields are absent, so a caller sees a clear "not available from this
tool today" rather than a KeyError -- and picks the field up automatically once `fz` is fixed upstream.

**Rate limit.** `fz`'s own default is 2 req/s (`fz --help`: `--rate-limit float ... (default 2)`)
against a scrape target with no published API terms. Call this on demand for one name at a time (an
S-A/S-C candidate, a G4 cross-section spot check) -- never loop it over the whole universe.
"""
from __future__ import annotations

import json
import subprocess
from typing import Callable

FZ_BIN = "fz"
FIELDS = ("Short Float", "Short Ratio", "Short Interest")
SUBPROCESS_TIMEOUT_S = 30


def _run_fz(ticker: str, runner: Callable = subprocess.run) -> str:
    """Network boundary: `fz quote --agent <ticker>`. Raises (FileNotFoundError, TimeoutExpired,
    CalledProcessError) on any failure -- `short_float` is the fail-soft wrapper around this."""
    proc = runner([FZ_BIN, "quote", "--agent", ticker], capture_output=True, text=True,
                   timeout=SUBPROCESS_TIMEOUT_S, check=True)
    return proc.stdout


def parse_quote(stdout: str) -> dict:
    """`fz quote --agent` JSON text -> the parsed object. Raises ValueError on unparseable JSON."""
    try:
        return json.loads(stdout)
    except (json.JSONDecodeError, TypeError) as exc:
        raise ValueError(f"unparseable fz quote output: {exc}") from exc


def _unavailable(reason: str) -> dict:
    return {"available": False, "reason": reason, "short_float": None, "short_ratio": None,
            "short_interest": None}


def short_float(ticker: str, runner: Callable = subprocess.run) -> dict:
    """Fail-soft, on-demand, one ticker at a time; never raises.

    `{"available": True, "reason": None, "short_float": ..., "short_ratio": ...,
    "short_interest": ...}` when `fz` returns the fields, else `{"available": False, "reason": ...,
    "short_float": None, "short_ratio": None, "short_interest": None}`."""
    try:
        stdout = _run_fz(ticker, runner)
        quote = parse_quote(stdout)
    except FileNotFoundError:
        return _unavailable("fz is not on PATH")
    except subprocess.TimeoutExpired:
        return _unavailable(f"fz quote timed out after {SUBPROCESS_TIMEOUT_S}s")
    except subprocess.CalledProcessError as exc:
        return _unavailable(f"fz quote exited {exc.returncode}: {(exc.stderr or '')[:200]}")
    except ValueError as exc:
        return _unavailable(str(exc))
    fundamentals = quote.get("fundamentals", {}) if isinstance(quote, dict) else {}
    values = {f: fundamentals.get(f) for f in FIELDS}
    if all(v is None for v in values.values()):
        return _unavailable("Short Float/Short Ratio/Short Interest absent from fz quote's "
                             "fundamentals grid (known fz regression, see module docstring)")
    return {"available": True, "reason": None, "short_float": values["Short Float"],
            "short_ratio": values["Short Ratio"], "short_interest": values["Short Interest"]}
