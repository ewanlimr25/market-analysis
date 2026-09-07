"""One-shot adjudication (DESIGN/100 §4, §5): a challenger against its champion, a champion against
its bar, or a gate against what it refused, from ledger rows only. Every function is pure given
its frames; the CLI in scripts/adjudicate.py wires the ledger, the registration file and the
output file. The registration records a hash of this module and the CLI; an edited script is
refused so the test cannot drift toward the answer.
"""
from __future__ import annotations

import hashlib
import json
import os
from datetime import date

import numpy as np
import pandas as pd
from scipy import stats as sps

from engine import policy as POL
from engine.config import REPO
from engine.improve.spec import StrategySpec
from engine.validation import stats as S

CHALLENGERS_DIR, ADJUDICATIONS_DIR = "challengers", "adjudications"
LOG_FILE = "LOG.md"
SCRIPT_PATHS = (os.path.join(REPO, "engine", "improve", "adjudicate.py"), os.path.join(REPO, "scripts", "adjudicate.py"))
REG_REQUIRED = ("policy_id", "strategy", "champion", "idea", "params_diff", "registered", "n_required", "unit",
                "adjudicate_on", "test", "min_effect", "kill", "script_sha256")
MATCH_KEY = ["ticker", "E", "structure"]
PROMOTE, FAIL, INSUFFICIENT, NOT_DUE = "PROMOTE", "FAIL", "INSUFFICIENT", "NOT_DUE"
PASS = "PASS"
ALPHA = 0.05


# ---- registration --------------------------------------------------------------------------------

def script_sha256(paths: tuple[str, ...] = SCRIPT_PATHS) -> str:
    h = hashlib.sha256()
    for p in paths:
        with open(p, "rb") as fh:
            h.update(fh.read())
    return h.hexdigest()


def validate_registration(reg: dict) -> None:
    missing = [k for k in REG_REQUIRED if k not in reg]
    if missing:
        raise ValueError(f"registration is missing {missing}")
    if not isinstance(reg["params_diff"], dict) or len(reg["params_diff"]) != 1:
        raise ValueError("params_diff must change exactly one parameter (DESIGN/100 §4)")
    for k in ("registered", "adjudicate_on"):
        date.fromisoformat(reg[k])
    if int(reg["n_required"]) < 2 or float(reg["min_effect"]) <= 0:
        raise ValueError("n_required must be >= 2 and min_effect > 0")


def load_registration(path: str) -> dict:
    with open(path) as fh:
        reg = json.load(fh)
    validate_registration(reg)
    return reg


def open_challengers(ledger_root: str, strategy: str) -> list[str]:
    """Registered challengers of a strategy with no adjudication file yet."""
    cdir, adir = os.path.join(ledger_root, CHALLENGERS_DIR), os.path.join(ledger_root, ADJUDICATIONS_DIR)
    if not os.path.isdir(cdir):
        return []
    out = []
    for name in sorted(os.listdir(cdir)):
        if not name.endswith(".json"):
            continue
        reg = load_registration(os.path.join(cdir, name))
        if reg["strategy"] == strategy and not os.path.exists(os.path.join(adir, f"{reg['policy_id']}.json")):
            out.append(reg["policy_id"])
    return out


def register(ledger_root: str, reg: dict) -> str:
    """Write ledger/challengers/<policy_id>.json; one open challenger per strategy, never a duplicate id."""
    validate_registration(reg)
    path = os.path.join(ledger_root, CHALLENGERS_DIR, f"{reg['policy_id']}.json")
    if os.path.exists(path):
        raise FileExistsError(f"{reg['policy_id']} is already registered ({path}); a challenger is never re-registered")
    live = open_challengers(ledger_root, reg["strategy"])
    if live:
        raise ValueError(f"{reg['strategy']} already has an open challenger {live}; one at a time (DESIGN/100 §4)")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        json.dump(reg, fh, indent=1)
        fh.write("\n")
    return path


# ---- statistics ---------------------------------------------------------------------------------

def _entered_after(df: pd.DataFrame, spec: StrategySpec, registered: date) -> pd.DataFrame:
    return df[pd.to_datetime(df[spec.entry_col]).dt.date > registered]


def unit_means(df: pd.DataFrame, spec: StrategySpec, col: str | None = None) -> pd.Series:
    """Mean of the metric per independent unit, ordered by unit."""
    col = col or spec.metric
    if df.empty:
        return pd.Series(dtype=float)
    units = pd.to_datetime(df[spec.unit]).dt.date
    return df.assign(_u=units).groupby("_u")[col].mean().sort_index()


def one_sided_p(t: float, n: int) -> float:
    """P(T >= t) on n - 1 df; the registered test is one-sided in the challenger's favour."""
    return float(sps.t.sf(t, df=max(n - 1, 1))) if np.isfinite(t) else float("nan")


def paired_units(champion: pd.DataFrame, challenger: pd.DataFrame, spec: StrategySpec, registered: date) -> pd.Series:
    """Per-unit mean of (challenger − champion) on rows matched by (ticker, E, structure), entered after registration."""
    if champion.empty or challenger.empty:
        return pd.Series(dtype=float)
    a = _entered_after(champion, spec, registered)[MATCH_KEY + [spec.unit, spec.metric]]
    b = _entered_after(challenger, spec, registered)[MATCH_KEY + [spec.metric]]
    m = a.merge(b, on=MATCH_KEY, suffixes=("_champ", "_chall"))
    if m.empty:
        return pd.Series(dtype=float)
    m["_diff"] = m[f"{spec.metric}_chall"] - m[f"{spec.metric}_champ"]
    return unit_means(m, spec, "_diff")


def series_stats(units: pd.Series, lag: int) -> dict:
    x = units.dropna()
    if len(x) < 3:
        return {"n_units": int(len(x)), "mean": float(x.mean()) if len(x) else float("nan"), "se": float("nan"), "t": float("nan"),
                "p_one_sided": float("nan"), "worst_unit": float(x.min()) if len(x) else float("nan"),
                "hit": float((x > 0).mean()) if len(x) else float("nan")}
    nw = S.nw_t(x.to_numpy(), lag)
    return {"n_units": int(nw["n"]), "mean": nw["mean"], "se": nw["se"], "t": nw["t"], "p_one_sided": one_sided_p(nw["t"], nw["n"]),
            "worst_unit": float(x.min()), "hit": nw["hit"]}


def challenger_verdict(stats: dict, reg: dict, as_of: date, alpha: float = ALPHA) -> tuple[str, str]:
    n, need, mean = stats["n_units"], int(reg["n_required"]), stats["mean"]
    min_effect = float(reg["min_effect"])
    if n >= max(2, need // 2) and np.isfinite(mean) and mean < -min_effect:
        return FAIL, f"early stop: paired mean {mean:+.4f} below -min_effect at {n} of {need} units (DESIGN/100 §8)"
    if n < need:
        due = date.fromisoformat(reg["adjudicate_on"])
        if as_of < due:
            return NOT_DUE, f"{n} of {need} units; adjudication date {due.isoformat()}"
        return INSUFFICIENT, f"{n} of {need} units on the adjudication date; no verdict, keep accruing"
    if np.isfinite(stats["p_one_sided"]) and stats["p_one_sided"] < alpha and mean > 0:
        return PROMOTE, f"paired mean {mean:+.4f}, t {stats['t']:.2f}, one-sided p {stats['p_one_sided']:.4f} < {alpha} on {n} units"
    return FAIL, f"paired mean {mean:+.4f}, one-sided p {stats['p_one_sided']:.4f} on {n} units; the challenger did not beat the champion"


def champion_verdict(stats: dict, n_required: int, go_t: float) -> tuple[str, str]:
    n = stats["n_units"]
    if n < n_required:
        return INSUFFICIENT, f"{n} of {n_required} units"
    if np.isfinite(stats["t"]) and stats["t"] >= go_t and stats["mean"] > 0:
        return PASS, f"mean {stats['mean']:+.4f}, NW t {stats['t']:.2f} >= {go_t} on {n} units (the full season bar is in the report)"
    return FAIL, f"mean {stats['mean']:+.4f}, NW t {stats['t']:.2f} < {go_t} on {n} units"


def gate_stats(exploration: pd.DataFrame, spec: StrategySpec) -> dict:
    """Gate-ON units against gate-OFF units on the exploration book; Welch t on unit means."""
    if exploration.empty:
        return {"n_on": 0, "n_off": 0, "mean_on": float("nan"), "mean_off": float("nan"), "diff": float("nan"), "t": float("nan"), "p_one_sided": float("nan")}
    is_on = exploration["gate_verdict"].astype(str) == spec.gate_on
    on, off = unit_means(exploration[is_on], spec), unit_means(exploration[~is_on], spec)
    out = {"n_on": int(len(on)), "n_off": int(len(off)), "mean_on": float(on.mean()) if len(on) else float("nan"),
           "mean_off": float(off.mean()) if len(off) else float("nan")}
    out["diff"] = out["mean_on"] - out["mean_off"]
    if len(on) >= 2 and len(off) >= 2:
        t, p2 = sps.ttest_ind(on, off, equal_var=False)
        out["t"], out["p_one_sided"] = float(t), float(p2 / 2 if t > 0 else 1 - p2 / 2)
    else:
        out["t"], out["p_one_sided"] = float("nan"), float("nan")
    return out


def gate_verdict(stats: dict, min_effect: float, n_required: int, alpha: float = ALPHA) -> tuple[str, str]:
    if min(stats["n_on"], stats["n_off"]) < n_required:
        return INSUFFICIENT, f"ON {stats['n_on']} / OFF {stats['n_off']} units of {n_required} each"
    if np.isfinite(stats["diff"]) and stats["diff"] >= min_effect and stats["p_one_sided"] < alpha:
        return "KEEP", f"gate-ON beats gate-OFF by {stats['diff']:+.4f} (p {stats['p_one_sided']:.4f}); the gate earns its keep"
    return "CANDIDATE_FOR_REMOVAL", f"gate-ON minus gate-OFF {stats['diff']:+.4f} (p {stats['p_one_sided']:.4f}); register its removal as a challenger"


# ---- output -------------------------------------------------------------------------------------

def write_adjudication(ledger_root: str, name: str, payload: dict) -> str:
    """Write ledger/adjudications/<name>.json once; an existing verdict is never rewritten."""
    adir = os.path.join(ledger_root, ADJUDICATIONS_DIR)
    path = os.path.join(adir, f"{name}.json")
    if os.path.exists(path):
        raise FileExistsError(f"{path} exists; an adjudication runs once (DESIGN/100 §5)")
    os.makedirs(adir, exist_ok=True)
    with open(path, "w") as fh:
        json.dump(payload, fh, indent=1, default=str)
        fh.write("\n")
    with open(os.path.join(adir, LOG_FILE), "a") as fh:
        fh.write(f"- {payload.get('as_of')} `{name}` **{payload.get('verdict')}** — {payload.get('reason')}\n")
    return path


def champion_rows(ledger: pd.DataFrame, policy_id: str) -> pd.DataFrame:
    return ledger[(ledger["policy_id"] == policy_id) & (ledger["role"] == POL.ROLE_CHAMPION)] if len(ledger) else ledger


def rows_for(ledger: pd.DataFrame, policy_id: str, role: str) -> pd.DataFrame:
    return ledger[(ledger["policy_id"] == policy_id) & (ledger["role"] == role)] if len(ledger) else ledger
