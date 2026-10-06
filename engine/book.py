"""`make book`: the paper book on one page -- every open champion position and the closed P&L per
strategy and structure, read from the three forward ledgers.

Each trade is counted once. Variants that took the same trade (S-A's A1 and A2, S-C's C1 and C2) share a
(ticker, E, structure) and appear as one row with `variants` = "A1+A2"; exploration rows (one-contract
copies, DESIGN/100 §6) stay out of the book and are only counted. Structures are NOT summed into one
total: S-A's SS and IC, and S-C's SS and IB, are alternative trades on the same name, read separately
at their reads. `risk_usd` is the max loss for defined-risk structures and the 3-sigma stress loss for
straddles (S-A: a 3x implied move; S-C: 3 sigma_hold). Closed rows show `post`, the session the position
was graded (S-A: the morning after the print; S-B and S-C: expiry). Read-only: nothing here writes a ledger or touches a frozen parameter.
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import date

import pandas as pd

from engine import ledger as L
from engine import policy as POL
from engine.config import LEDGER_DIR, LEDGER_SB_DIR, LEDGER_SC_DIR

TRADE_KEY = ["ticker", "E", "structure"]
SA_STRIKES = ("k", "k_dn", "k_up")                  # straddle strike and the condor wings
SB_STRIKES = ("k_p1", "k_p2", "k_c1", "k_c2")
SC_STRIKES = ("k", "k_dn", "k_up")
SUMMARY_COLS = ["structure", "open_n", "open_risk_usd", "closed_n", "wins", "net_usd", "mean_ror"]


@dataclass(frozen=True)
class Strategy:
    name: str
    ledger_dir: str
    strikes: tuple[str, ...]


@dataclass(frozen=True)
class Book:
    strategy: Strategy
    open: pd.DataFrame
    closed: pd.DataFrame
    exploration_open: int


STRATEGIES = (Strategy("S-A", LEDGER_DIR, SA_STRIKES), Strategy("S-B", LEDGER_SB_DIR, SB_STRIKES),
              Strategy("S-C", LEDGER_SC_DIR, SC_STRIKES))


def _keys(df: pd.DataFrame, cols: list[str]) -> pd.Series:
    return df[cols].astype(str).agg("|".join, axis=1) if len(df) else pd.Series(dtype=str)


def _once(df: pd.DataFrame) -> pd.DataFrame:
    """One row per trade, with the variants that took it joined into `variants`."""
    if df.empty:
        return df.assign(variants=pd.Series(dtype=str))
    key = _keys(df, TRADE_KEY)
    variants = df.assign(_k=key).groupby("_k")["variant"].agg(lambda v: "+".join(sorted(set(map(str, v)))))
    first = df.assign(_k=key).drop_duplicates("_k")
    return first.assign(variants=first["_k"].map(variants)).drop(columns="_k").reset_index(drop=True)


def _role(df: pd.DataFrame, role: str) -> pd.DataFrame:
    return df[df["role"] == role] if len(df) else df


def load(strategy: Strategy) -> Book:
    signals, graded = L.read_signals(strategy.ledger_dir), L.read_ledger(strategy.ledger_dir)
    graded_keys = set(_keys(graded, L.KEY))
    is_open = ~_keys(signals, L.KEY).isin(graded_keys) if len(signals) else pd.Series(dtype=bool)
    still_open = signals[is_open] if len(signals) else signals
    return Book(strategy, _once(_role(still_open, POL.ROLE_CHAMPION)), _once(_role(graded, POL.ROLE_CHAMPION)),
                int(len(_role(still_open, POL.ROLE_EXPLORATION))))


def summary(book: Book) -> pd.DataFrame:
    """Per structure: open count and risk, closed count, wins, net $ and mean return on risk."""
    rows = []
    for s in sorted(set(book.open.get("structure", [])) | set(book.closed.get("structure", []))):
        o = book.open[book.open.structure == s] if len(book.open) else book.open
        c = book.closed[book.closed.structure == s] if len(book.closed) else book.closed
        ror = (c.net_usd / c.risk_usd) if len(c) else pd.Series(dtype=float)
        rows.append({"structure": s, "open_n": len(o), "open_risk_usd": float(o.risk_usd.sum()) if len(o) else 0.0,
                     "closed_n": len(c), "wins": int((c.net_usd > 0).sum()) if len(c) else 0,
                     "net_usd": float(c.net_usd.sum()) if len(c) else 0.0,
                     "mean_ror": float(ror.mean()) if len(c) else None})
    return pd.DataFrame(rows, columns=SUMMARY_COLS)


# ---- rendering -------------------------------------------------------------------------------------
def _usd(v, signed: bool = False) -> str:
    return "—" if v is None or pd.isna(v) else (f"{v:+,.2f}" if signed else f"{v:,.2f}")


def _strikes(row: pd.Series, cols: tuple[str, ...]) -> str:
    """Low to high: a put spread reads long/short put, a condor wing/short/short/wing."""
    ks = sorted({float(k) for k in (row.get(c) for c in cols) if k is not None and not pd.isna(k)})
    return "/".join(f"{k:g}" for k in ks) or "—"


def _table(header: list[str], rows: list[list[str]]) -> list[str]:
    return ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)] + ["| " + " | ".join(r) + " |" for r in rows]


def _open_rows(book: Book) -> list[list[str]]:
    df = book.open.sort_values(["expiry", "ticker", "structure"]) if len(book.open) else book.open
    return [[str(r.ticker), str(r.structure), str(r.variants), str(r.E)[:10], str(r.expiry)[:10],
             _strikes(r, book.strategy.strikes), f"{int(r.contracts)}", _usd(r.credit_entry), _usd(r.risk_usd)]
            for _, r in df.iterrows()]


def _closed_rows(book: Book) -> list[list[str]]:
    df = book.closed.sort_values(["post", "ticker", "structure"]) if len(book.closed) else book.closed
    return [[str(r.ticker), str(r.structure), str(r.variants), str(r.E)[:10], str(r.post)[:10],
             _usd(r.net_usd, signed=True), f"{r.net_usd / r.risk_usd:+.2%}"] for _, r in df.iterrows()]


def _section(book: Book) -> list[str]:
    out = [f"## {book.strategy.name}", ""]
    s = summary(book)
    if s.empty:
        return out + ["_no positions yet_", ""]
    out += _table(["structure", "open", "open risk $", "closed", "wins", "net $", "mean return on risk"],
                  [[r.structure, str(r.open_n), _usd(r.open_risk_usd), str(r.closed_n), str(r.wins),
                    _usd(r.net_usd, signed=True), "—" if r.mean_ror is None or pd.isna(r.mean_ror) else f"{r.mean_ror:+.2%}"]
                   for r in s.itertuples()]) + [""]
    if len(book.open):
        out += [f"Open ({len(book.open)}):", ""] + _table(
            ["ticker", "structure", "variants", "entered (E)", "expiry", "strikes", "contracts", "credit", "risk $"],
            _open_rows(book)) + [""]
    if len(book.closed):
        out += [f"Closed ({len(book.closed)}):", ""] + _table(
            ["ticker", "structure", "variants", "entered (E)", "closed", "net $", "return on risk"], _closed_rows(book)) + [""]
    if book.exploration_open:
        out += [f"Exploration book: {book.exploration_open} open one-contract rows (not in the totals above).", ""]
    return out


def render(books: list[Book], asof: date) -> str:
    lines = [f"# Paper book — {asof.isoformat()}", "",
             "Paper only: nothing here is a live order. Champion positions, each trade once (variants that took "
             "it are listed). Structures are not added together: on S-A and S-C they are alternative trades on "
             "the same name. Risk is the max loss, or the 3-sigma stress loss for straddles; net $ is after costs.",
             ""]
    for book in books:
        lines += _section(book)
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="the paper book on one page (read-only)")
    ap.add_argument("--out", help="also write the page to this path")
    args = ap.parse_args(argv)
    page = render([load(s) for s in STRATEGIES], date.today())
    sys.stdout.write(page)
    if args.out:
        with open(args.out, "w") as fh:
            fh.write(page)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
