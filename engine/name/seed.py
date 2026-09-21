"""The `sdd-llm-1.0` seed (findings/stock-deep-dive DECISIONS D8, DESIGN/70 §10 R5).

The old deep-dive book — 62 decisions, 125 structures, 9 trade plans and their 18 option legs — was
graded once, offline, in `findings/stock-deep-dive/artifacts/outcomes/` and written to
`results/*.csv`. This module loads those CSVs into `ledger/name/` under `policy_id sdd-llm-1.0`,
`role champion`, so the new tool's first comparison row exists on day one and the old book is never
re-derived from a live feed (`market-analysis/RESEARCH/10 §6.1`, the `resolved_ledger.py` rule).

Files read (all under `results/`):

  E_calibration_rows.csv   62 decisions, one per (ticker, decision date): bias, entry, stop, conf
  B_path_rows.csv          the 22 LONG/SHORT decisions walked +/-1R; `hz_*` is the horizon-matched
                           window, which is the outcome seeded as `r_share`
  CD_structure_rows.csv    125 structures at expiry, with `family`, `ror` and `status`
  G_plans_stock.csv        the 9 trade plans' share legs; the limit-fill rows at review 2026-09-18
  G_plans_options.csv      their 18 option legs at expiry

Row shape. The ledger KEY is `(ticker, E, variant, structure, policy_id, role)` with `E` the
decision date, `variant` `"decision"` (the book) or `"plan"` (the trade plans), and `structure`
`"SHARES"` for a share line or `"<family>#<idx>"` for an option structure. The index is part of the
key because three decisions wrote two structures of the same family (ENPH 05-22, ENVX 06-26 and
RDDT 05-22 each hold a call and a put debit spread), and a bare family would collide and be dropped
by the ledger's write-once rule. The bare family is kept beside it in `family`.

`post` is the date the outcome was fixed: the +/-1R or stop/target event date for a share line, the
expiry for an option structure, and the corpus review date 2026-09-18 where neither exists (a
no-fill, an inconclusive walk, a position still open). `gate_verdict` is the old skill's own bias
label, which is the only gate this book ever had. `context_read` is `"narrate"` on every row: every
one of these decisions was made after the full research run (D13).

A row with no resolved outcome is still seeded, with `r_share` / `ror` null, so the corpus is
complete and the resolved share can be read off the ledger rather than assumed.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import date

import pandas as pd

from engine import ledger as L
from engine.config import LEDGER_NAME_DIR, SEED_POLICY_ID
from engine.policy import ROLE_CHAMPION

RESULTS_DIR = os.path.expanduser("~/Development/findings/stock-deep-dive/artifacts/outcomes/results")
SOURCE_PREFIX = "findings/stock-deep-dive artifacts/outcomes results/"
SEED_REVIEW = date(2026, 9, 18)        # the corpus review date; the last bar in artifacts/outcomes/bars.parquet
CONTEXT_READ = "narrate"               # D13: every old decision was made after the full research run
SHARES = "SHARES"
DECISION, PLAN = "decision", "plan"
EXPIRED = "EXPIRED"
FILES = ("E_calibration_rows.csv", "B_path_rows.csv", "CD_structure_rows.csv",
         "G_plans_stock.csv", "G_plans_options.csv")
NUMERIC = ("entry", "stop", "target", "r_share", "ror", "conviction", "conf", "n")
COLUMNS = ("ticker", "E", "variant", "structure", "policy_id", "role", "gate_verdict", "pre", "post",
           "family", "direction", "entry", "stop", "target", "r_share", "ror", "outcome", "n",
           "context_read", "conviction", "conf", "source")
SIGN = {"LONG": 1, "SHORT": -1}


# ---- the source's own labels ----------------------------------------------------------------------

def family_of(structure_type: str) -> str:
    """The port of `artifacts/outcomes/lib.py::classify_structure`, family only.

    `CD_structure_rows.csv` carries `family` already; `G_plans_options.csv` carries only the free
    text `type`, so the plans' legs are classified here with the same rule that classified theirs.
    """
    t = (structure_type or "").lower()
    if "condor" in t:
        return "IC"
    if "calendar" in t:
        return "calendar"
    if "strangle" in t:
        return "long_strangle"
    if "straddle" in t:
        return "long_straddle"
    if "credit" in t or re.search(r"\bbear call\b", t) or re.search(r"\bbull put\b", t):
        return "debit_vertical" if "debit" in t else "credit_vertical"
    if "debit" in t or re.search(r"\bbear put\b", t) or re.search(r"\bbull call\b", t) or "spread" in t:
        return "debit_vertical"
    if t.startswith("long call") or t.startswith("long put"):
        return "long_single"
    return "unknown"


def _num(value) -> float:
    """A float, or NaN where the source left the cell empty."""
    return float(value) if pd.notna(value) else float("nan")


def _iso(value, default: date | None = None) -> str | None:
    if pd.isna(value) or value in ("", None):
        return default.isoformat() if default else None
    return pd.Timestamp(value).date().isoformat()


def _text(value) -> str | None:
    return str(value) if pd.notna(value) else None


def _row(source: str, **fields) -> dict:
    base = {"policy_id": SEED_POLICY_ID, "role": ROLE_CHAMPION, "n": 1, "context_read": CONTEXT_READ,
            "family": None, "direction": None, "entry": float("nan"), "stop": float("nan"),
            "target": float("nan"), "r_share": float("nan"), "ror": float("nan"), "outcome": None,
            "conviction": float("nan"), "conf": float("nan"), "source": SOURCE_PREFIX + source}
    return {**base, **fields}


# ---- the four books --------------------------------------------------------------------------------

def decision_rows(calibration: pd.DataFrame, path: pd.DataFrame) -> list[dict]:
    """One share row per decision (62). The 22 LONG/SHORT decisions carry the horizon-matched
    +/-1R walk (`hz_*`); the 40 RANGE/NEUTRAL decisions never had a directional outcome."""
    walks = {(r.ticker, _iso(r.date)): r for r in path.itertuples()}
    out = []
    for d in calibration.itertuples():
        E = _iso(d.date)
        w = walks.get((d.ticker, E))
        sign, entry = SIGN.get(str(d.bias)), _num(d.entry)
        target = entry + sign * _num(w.R) if (w is not None and sign) else float("nan")
        out.append(_row("E_calibration_rows.csv", ticker=d.ticker, E=E, variant=DECISION, structure=SHARES,
                        gate_verdict=str(d.bias), pre=E, post=_iso(w.hz_date, SEED_REVIEW) if w is not None else SEED_REVIEW.isoformat(),
                        direction={1: "long", -1: "short"}.get(sign), entry=entry, stop=_num(d.stop), target=target,
                        r_share=_num(w.hz_R) if w is not None else float("nan"),
                        outcome=_text(w.hz_outcome) if w is not None else None,
                        conviction=_num(d.conviction), conf=_num(d.conf)))
    return out


def structure_rows(structures: pd.DataFrame) -> list[dict]:
    """One row per structure (125), graded intrinsic at expiry; `ror` null while a row is open."""
    out = []
    for s in structures.itertuples():
        resolved = str(s.status) == EXPIRED
        E = _iso(s.date)
        out.append(_row("CD_structure_rows.csv", ticker=s.ticker, E=E, variant=DECISION,
                        structure=f"{s.family}#{s.idx}", family=str(s.family), gate_verdict=str(s.bias),
                        pre=E, post=_iso(s.expiry, SEED_REVIEW),
                        ror=_num(s.ror) if resolved else float("nan"),
                        outcome=("WIN" if float(s.win) > 0 else "LOSS") if resolved else str(s.status),
                        conviction=_num(s.conviction), conf=_num(s.conf)))
    return out


def plan_share_rows(plans: pd.DataFrame) -> list[dict]:
    """One row per trade plan (9): the limit-fill share leg at the 2026-09-18 review, which is the
    fill rule that requires the entry to have traded (RESEARCH/15 §G)."""
    out = []
    for p in limit_fill_plans(plans).itertuples():
        E = _iso(p.plan_date)
        out.append(_row("G_plans_stock.csv", ticker=p.ticker, E=E, variant=PLAN, structure=SHARES,
                        gate_verdict=str(p.bias), pre=E, post=_iso(p.event_date, SEED_REVIEW),
                        direction=str(p.direction), entry=_num(p.entry), stop=_num(p.stop), target=_num(p.t1),
                        r_share=_num(p.r), outcome=str(p.outcome), conf=_num(p.conf)))
    return out


def plan_option_rows(options: pd.DataFrame, plans: pd.DataFrame) -> list[dict]:
    """One row per trade-plan option leg (18). The plan's bias and confidence live on the share
    file, so they are joined from it; the family is classified from the leg's own `type`."""
    meta = {(p.ticker, _iso(p.plan_date)): p for p in limit_fill_plans(plans).itertuples()}
    idx = options.groupby(["ticker", "plan_date"]).cumcount()
    out = []
    for (o, i) in zip(options.itertuples(), idx):
        E, resolved = _iso(o.plan_date), str(o.status) == EXPIRED
        plan = meta.get((o.ticker, E))
        out.append(_row("G_plans_options.csv", ticker=o.ticker, E=E, variant=PLAN,
                        structure=f"{family_of(o.type)}#{i}", family=family_of(o.type),
                        gate_verdict=str(plan.bias) if plan is not None else None,
                        pre=E, post=_iso(o.expiry, SEED_REVIEW),
                        ror=_num(o.ror) if resolved else float("nan"),
                        outcome=("WIN" if _num(o.pnl) > 0 else "LOSS") if resolved else str(o.status),
                        conf=_num(plan.conf) if plan is not None else float("nan")))
    return out


def limit_fill_plans(plans: pd.DataFrame) -> pd.DataFrame:
    return plans[(plans["review"] == SEED_REVIEW.isoformat()) & (plans["fill"] == "limit")].reset_index(drop=True)


# ---- load, build, write ----------------------------------------------------------------------------

def load_results(results_dir: str = RESULTS_DIR) -> dict[str, pd.DataFrame]:
    """The five graded CSVs. A missing file is named, not silently skipped."""
    missing = [f for f in FILES if not os.path.exists(os.path.join(results_dir, f))]
    if missing:
        raise FileNotFoundError(f"{results_dir} is missing {missing}; the seed reads the frozen artifacts of D8")
    return {f: pd.read_csv(os.path.join(results_dir, f)) for f in FILES}


def build_rows(results_dir: str = RESULTS_DIR) -> pd.DataFrame:
    """The whole seeded corpus as one ledger-shaped frame, ordered decisions, structures, plans."""
    csv = load_results(results_dir)
    plans = csv["G_plans_stock.csv"]
    rows = (decision_rows(csv["E_calibration_rows.csv"], csv["B_path_rows.csv"])
            + structure_rows(csv["CD_structure_rows.csv"])
            + plan_share_rows(plans)
            + plan_option_rows(csv["G_plans_options.csv"], plans))
    df = pd.DataFrame(rows, columns=list(COLUMNS))
    for col in NUMERIC:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    duplicates = df[df.duplicated(subset=L.KEY, keep=False)]
    if len(duplicates):
        raise ValueError(f"the seed built {len(duplicates)} rows that share a ledger key: "
                         f"{duplicates[L.KEY].to_dict('records')}")
    return df


def counts(rows: pd.DataFrame) -> dict[str, int]:
    """The four books, by the shape of their key."""
    is_share = rows["structure"] == SHARES
    return {"decisions": int(((rows["variant"] == DECISION) & is_share).sum()),
            "structures": int(((rows["variant"] == DECISION) & ~is_share).sum()),
            "plans": int(((rows["variant"] == PLAN) & is_share).sum()),
            "plan_options": int(((rows["variant"] == PLAN) & ~is_share).sum()),
            "total": int(len(rows))}


def write(rows: pd.DataFrame, ledger_dir: str, on: date = SEED_REVIEW) -> dict[str, int]:
    """Emit and grade the same rows: they are already-graded history, and the signals file keeps
    `engine.ledger.pending` consistent. The ledger's write-once rule makes a second run a no-op."""
    emitted, emit_skipped = L.emit(ledger_dir, rows, on)
    graded, grade_skipped = L.grade(ledger_dir, rows, on)
    return {"emitted": emitted, "emit_skipped": emit_skipped, "graded": graded, "graded_skipped": grade_skipped}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Seed the 62-decision deep-dive corpus into ledger/name/ (D8).")
    ap.add_argument("--ledger-dir", default=LEDGER_NAME_DIR)
    ap.add_argument("--results-dir", default=RESULTS_DIR)
    ap.add_argument("--dry-run", action="store_true", help="build and count the rows, write nothing")
    a = ap.parse_args(argv)
    rows = build_rows(a.results_dir)
    print(f"{SEED_POLICY_ID}: " + " · ".join(f"{k} {v}" for k, v in counts(rows).items()))
    if a.dry_run:
        print(f"dry run: nothing written to {a.ledger_dir}")
        return 0
    out = write(rows, a.ledger_dir)
    print(f"{a.ledger_dir}: emitted {out['emitted']} (skipped {out['emit_skipped']}), "
          f"graded {out['graded']} (skipped {out['graded_skipped']})")
    if out["graded"] == 0:
        print("the seed has already run; the ledger is write-once and nothing was rewritten (D8)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
