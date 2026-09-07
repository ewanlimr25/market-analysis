"""G10: S-B challengers from the CBOE vol-index family (findings/market-analysis
RESEARCH/47-edge-gaps.md §2; DESIGN/80 §8 idea ledger; DESIGN/100 §4-§6 registration rules).

Every challenger here is ONE additional condition ANDed onto the frozen champion gate
(`engine.strategies.sb_gate.gate`), evaluated at the same `t-1` close the champion reads, on the
three-year proxy sleeve (`engine.strategies.sb_proxy`). Neither `sb_gate.py` nor `sb_proxy.py` is
edited; this module composes their pure functions from the outside. Because a challenger only ever
*removes* champion-ON weeks, on the weeks a challenger fires the champion fires too and the two
price an identical trade (DESIGN/80's position construction is deterministic given the entry
session, underlying and structure) -- so the DESIGN/100 §4 "paired difference on matched entry
nights" is ~0 by construction (`matched_diff_check`, a validity check, not a decision statistic).
The decision statistic is `kept_vs_dropped`: does the additional condition's kept-week population
out-earn the champion weeks it drops (the "units lost")? That is the same Welch-t comparison
`engine.improve.adjudicate.gate_stats` already runs for the gate audit (DESIGN/100 §6), because a
one-parameter S-B challenger of this family *is* a gate-tightening candidate.

Threshold grids are pre-stated constants below, derived once from the CBOE history before any
challenger P&L was computed (VVIX/SKEW: quartiles of the full fetched history through
2026-09-04; the ratio grids: quartiles of the P1-P3 proxy window, `DESIGN/80 §6.4`), never
searched over after seeing a result. Every value in a grid is run and reported; nothing here picks
a "best" threshold (`RESEARCH/47-edge-gaps.md` G10).
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import date

import numpy as np
import pandas as pd
from scipy import stats as sps

from engine import config
from engine.config import SB_PARAMS, SB_SIZING, SBParams, SBSizing
from engine.improve import adjudicate as ADJ
from engine.improve import power as PW
from engine.mart import index_vol as IV
from engine.strategies import sb_gate as G
from engine.strategies import sb_proxy as P
from engine.strategies import sb_structures as SB
from engine.validation import sb_harness as H
from engine.validation import stats as S

# ---- pre-stated threshold grids (DESIGN/80 §8 idea ledger item 1; RESEARCH/47 G10) --------------

CHALLENGER_MIN_EFFECT = 0.010     # ROR units; the DESIGN/100 §4 example registration's value, reused here
CHALLENGER_STRATEGY = "sb"

# (a) VIX floor -- the idea ledger's first entry (DESIGN/80 §8, D21). Absolute F=14 for VIX is the
# ledger's own number; the "equivalent VXN level for QQQ" it asks for but does not give is computed
# once here as 14 x mean(VXN/VIX) over the P1-P3 proxy window (2023-09-08 .. 2026-09-04, = 1.2557),
# rounded to the nearest $0.50 -> 17.5. Relative form: 25th percentile of the trailing 252 sessions
# (the ledger's own window and percentile), computed per entry date, fail-closed under 252 sessions.
VIX_FLOOR_ABS = {"SPY": 14.0, "QQQ": 17.5}
VIX_FLOOR_REL_WINDOW = 252
VIX_FLOOR_REL_PCTILE = 0.25

# (b) VIX9D/VIX <= x: short-term term structure not (or barely) inverted. Grid brackets the P1-P3
# quartiles (25th 0.867, 50th 0.925, 75th 0.990) around the natural x=1.00 "not inverted" boundary.
VIX9D_VIX_MAX = (0.90, 0.95, 1.00)

# (c) VVIX <= x: quartiles of the full CBOE VVIX history through 2026-09-04 (25th 84.4, 50th 92.4,
# 75th 103.9), rounded to the nearest 5.
VVIX_MAX = (85.0, 95.0, 105.0)

# (d) SKEW <= x: quartiles of the full CBOE SKEW history through 2026-09-04 (25th 121.8, 50th 128.8,
# 75th 139.3), rounded to the nearest 5.
SKEW_MAX = (125.0, 135.0, 145.0)

# (e) VIX/VIX3M <= x: a stricter contango requirement than G1 (VIX3M > VIX). Grid brackets the P1-P3
# quartiles (25th 0.850, 60th 0.897, 80th 0.947).
VIX_VIX3M_MAX = (0.85, 0.90, 0.95)

KIND_VIX_FLOOR_ABS, KIND_VIX_FLOOR_REL, KIND_COLUMN_LE = "vix_floor_abs", "vix_floor_rel", "column_le"


@dataclass(frozen=True)
class Challenger:
    challenger_id: str
    label: str
    kind: str
    column: str | None       # for KIND_COLUMN_LE
    threshold: float | None  # for KIND_COLUMN_LE
    param_name: str          # for the registration draft's params_diff (exactly one key)
    param_value: object


def _column_le_challengers(prefix: str, label_fmt: str, column: str, thresholds: tuple[float, ...],
                           param_name: str, fmt: str = "{:.2f}") -> tuple[Challenger, ...]:
    return tuple(Challenger(f"sb-c-{prefix}-{fmt.format(x)}", label_fmt.format(x), KIND_COLUMN_LE, column, x,
                            param_name, x)
                for x in thresholds)


CHALLENGERS: tuple[Challenger, ...] = (
    Challenger("sb-c-vixfloor-abs", "VIX floor, absolute (VIX>=14 SPY / VXN>=17.5 QQQ)",
              KIND_VIX_FLOOR_ABS, None, None, "vix_floor_abs", dict(VIX_FLOOR_ABS)),
    Challenger("sb-c-vixfloor-rel", "VIX floor, relative (25th pctile of trailing 252 sessions)",
              KIND_VIX_FLOOR_REL, None, None, "vix_floor_rel_pctile", VIX_FLOOR_REL_PCTILE),
    *_column_le_challengers("vix9dvix", "VIX9D/VIX <= {:.2f}", "vix9d_vix_ratio", VIX9D_VIX_MAX, "vix9d_vix_ratio_max"),
    *_column_le_challengers("vvix", "VVIX <= {:.0f}", "vvix", VVIX_MAX, "vvix_max", fmt="{:.0f}"),
    *_column_le_challengers("skew", "SKEW <= {:.0f}", "skew", SKEW_MAX, "skew_max", fmt="{:.0f}"),
    *_column_le_challengers("vixvix3m", "VIX/VIX3M <= {:.2f}", "vix_vix3m_ratio", VIX_VIX3M_MAX, "vix_vix3m_ratio_max"),
)
TRIAL_COUNT = len(CHALLENGERS)     # for the deflation charge (RESEARCH/47 G10 "report the trial count")


# ---- inputs ---------------------------------------------------------------------------------------

def merged_vol_frame(index_vol_base: pd.DataFrame, index_vol_ext: pd.DataFrame) -> pd.DataFrame:
    """Left join of the base (vix/vix3m/vxn/vix9d) and ext (vvix/skew/ratios) mart tables on date;
    every base row is kept even where the ext table has no row."""
    if index_vol_base is None or index_vol_base.empty:
        return index_vol_base
    return index_vol_base.merge(index_vol_ext, on="date", how="left")


def _on_sessions(df: pd.DataFrame, is_session) -> pd.DataFrame:
    """Like `index_vol.on_sessions`, but shape-agnostic (the merged frame carries extra columns
    `index_vol.on_sessions`'s own empty-frame fallback does not know about)."""
    if df is None or df.empty:
        return df
    keep = df["date"].map(is_session)
    return df[keep.astype(bool)].reset_index(drop=True)


def _full_history_sessions(index_vol_full: pd.DataFrame) -> pd.DataFrame:
    """Session rows over the FULL fetched CBOE history (not restricted to the proxy's own 754-day
    window), for the relative VIX floor's 252-session lookback only. The proxy's three-year window
    starts too close to its own beginning for a 252-session trailing window to ever fill inside it
    (DESIGN/80's own session rule, `on_sessions`, dropped rows with no VIX3M/VXN print, which is
    reused here directly since the CBOE history predates `engine.calendar`'s 2026-2027 coverage)."""
    if index_vol_full is None or index_vol_full.empty:
        return index_vol_full
    keep = index_vol_full["vix3m"].notna() & index_vol_full["vxn"].notna()
    return index_vol_full[keep].sort_values("date").reset_index(drop=True)


# ---- the additional condition ----------------------------------------------------------------------

def _vix_floor_relative(index_vol_base: pd.DataFrame, asof: date, x_col: str, x_value: float | None,
                        window: int = VIX_FLOOR_REL_WINDOW, pctile: float = VIX_FLOOR_REL_PCTILE) -> bool | None:
    if x_value is None:
        return None
    dates = index_vol_base["date"].tolist()
    try:
        i = dates.index(asof)
    except ValueError:
        return None
    lo = max(0, i - window + 1)
    win = pd.to_numeric(index_vol_base.iloc[lo:i + 1][x_col], errors="coerce")
    if len(win) < window or win.isna().any():
        return None
    return bool(x_value >= float(win.quantile(pctile)))


def evaluate_condition(ch: Challenger, state: G.GateState, underlying: str, merged: pd.DataFrame,
                       index_vol_base: pd.DataFrame) -> bool | None:
    """None means unknown; the challenger fails closed on that entry, the champion gate's own
    convention (`sb_gate.gate`). Always read at `state.asof` (t-1), never at the entry session."""
    if not state.known or state.asof is None:
        return None
    if ch.kind == KIND_VIX_FLOOR_ABS:
        if state.x is None:
            return None
        return bool(state.x >= VIX_FLOOR_ABS[underlying])
    if ch.kind == KIND_VIX_FLOOR_REL:
        return _vix_floor_relative(index_vol_base, state.asof, config.SB_VOL_INDEX[underlying], state.x)
    if ch.kind == KIND_COLUMN_LE:
        if merged is None or merged.empty:
            return None
        row = merged[merged["date"] == state.asof]
        if row.empty or ch.column not in row.columns:
            return None
        v = row[ch.column].iloc[0]
        return None if pd.isna(v) else bool(v <= ch.threshold)
    raise ValueError(f"unknown challenger kind {ch.kind!r}")


# ---- the composed proxy run --------------------------------------------------------------------

def run_challenger_proxy(inputs: P.ProxyInputs, ch: Challenger, merged_vol: pd.DataFrame,
                         params: SBParams = SB_PARAMS, sizing: SBSizing = SB_SIZING,
                         start: date | None = None, end: date | None = None) -> pd.DataFrame:
    """Champion gate AND `ch`'s condition, both read at t-1; capped per sleeve on the challenger's
    own (narrower) entry set. `sb_gate.py` and `sb_proxy.py` are called, never edited."""
    sessions = inputs.sessions
    if not sessions:
        return pd.DataFrame()
    entries = P.entry_sessions(sessions, start or sessions[0], end or sessions[-1])
    index = {d: i for i, d in enumerate(sessions)}
    session_set = set(sessions)
    index_vol = IV.on_sessions(inputs.index_vol, session_set.__contains__)
    merged = _on_sessions(merged_vol, session_set.__contains__)
    full_history = _full_history_sessions(inputs.index_vol)     # relative VIX floor only (see docstring)
    rows = []
    for t in entries:
        i = index[t]
        if i == 0:
            continue
        expiry = SB.proxy_expiry(t, sessions, params)
        if expiry is None:
            continue
        for u in config.SB_UNDERLYINGS:
            x_col = config.SB_VOL_INDEX[u]
            state = G.gate(index_vol, t, sessions[i - 1], x_col, params)
            if not G.is_on(state, "both"):
                continue
            if not evaluate_condition(ch, state, u, merged, full_history):
                continue
            x_t = P._x_on(index_vol, t, x_col)
            spot, settle = inputs.closes.get((u, t)), inputs.closes.get((u, expiry))
            if x_t is None or spot is None or settle is None:
                continue
            for s in config.SB_STRUCTURES:
                row = P.proxy_position(u, s, t, expiry, spot, x_t, settle, params, sizing)
                if row is not None:
                    rows.append({**row, **P._gate_fields(state, "both"), "challenger_id": ch.challenger_id})
    entered, _ = SB.cap_open_positions(rows, sizing.max_open_per_sleeve)
    if not entered:
        return pd.DataFrame()
    return pd.DataFrame(entered).sort_values(["entry", "underlying", "structure"], kind="mergesort").reset_index(drop=True)


def total_entry_weeks(inputs: P.ProxyInputs, start: date | None = None, end: date | None = None) -> int:
    sessions = inputs.sessions
    if not sessions:
        return 0
    return len(P.entry_sessions(sessions, start or sessions[0], end or sessions[-1]))


# ---- summary statistics -------------------------------------------------------------------------

def gate_footprint(challenger_df: pd.DataFrame, u: str, entries_total: int) -> float:
    if entries_total == 0 or challenger_df is None or challenger_df.empty:
        return 0.0
    kept = challenger_df[challenger_df["underlying"] == u]["entry"].nunique()
    return kept / entries_total


def sleeve_window_stats(df: pd.DataFrame, u: str, s: str, window: str | None = None, lag: int = config.SB_NW_LAG) -> dict:
    sub = df[(df["underlying"] == u) & (df["structure"] == s)] if len(df) else df
    if window and "window" in getattr(sub, "columns", []):
        sub = sub[sub["window"] == window]
    x = sub["ror"].to_numpy() if len(sub) else np.array([])
    nw = S.nw_t(x, lag)
    return {"n": nw["n"], "mean_ror": nw["mean"], "nw_t": nw["t"], "nw_p": nw["p"], "hit": nw["hit"]}


def positive_windows(df: pd.DataFrame, u: str, s: str) -> tuple[int, int]:
    """(# proxy windows P1/P2/P3 with n>0 and mean_ror>0, # windows with any positions)."""
    seen, positive = 0, 0
    for w in H.PROXY_WINDOWS:
        st = sleeve_window_stats(df, u, s, w)
        if st["n"] > 0:
            seen += 1
            if st["mean_ror"] > 0:
                positive += 1
    return positive, seen


def matched_diff_check(champion_df: pd.DataFrame, challenger_df: pd.DataFrame, u: str, s: str) -> dict:
    """DESIGN/100 §4's "paired difference on matched entry nights", as a validity check: on the
    weeks a subset-style challenger fires the champion fires too and prices the identical trade, so
    this should be ~0. A nonzero value would mean the composition changed how a kept position is
    priced, which it must not."""
    key = ["underlying", "structure", "entry"]
    if champion_df is None or champion_df.empty or challenger_df is None or challenger_df.empty:
        return {"n_matched": 0, "mean_diff": float("nan"), "max_abs_diff": float("nan")}
    c = champion_df[key + ["ror"]]
    h = challenger_df[(challenger_df["underlying"] == u) & (challenger_df["structure"] == s)][key + ["ror"]]
    m = h.merge(c, on=key, suffixes=("_chall", "_champ"))
    if m.empty:
        return {"n_matched": 0, "mean_diff": float("nan"), "max_abs_diff": float("nan")}
    diff = m["ror_chall"] - m["ror_champ"]
    return {"n_matched": int(len(m)), "mean_diff": float(diff.mean()), "max_abs_diff": float(diff.abs().max())}


def kept_vs_dropped(champion_df: pd.DataFrame, challenger_df: pd.DataFrame, u: str, s: str) -> dict:
    """The decision statistic: Welch t between the challenger's kept weeks and the champion weeks
    it drops ("units lost"), the same math `engine.improve.adjudicate.gate_stats` runs for the gate
    audit (DESIGN/100 §6) -- a one-parameter subset challenger of this family IS a gate-tightening
    candidate, not a differently-priced alternate."""
    champ = champion_df[(champion_df["underlying"] == u) & (champion_df["structure"] == s)] if len(champion_df) else champion_df
    kept = challenger_df[(challenger_df["underlying"] == u) & (challenger_df["structure"] == s)] if len(challenger_df) else challenger_df
    kept_entries = set(kept["entry"]) if len(kept) else set()
    dropped = champ[~champ["entry"].isin(kept_entries)] if len(champ) else champ
    kx = kept["ror"].to_numpy() if len(kept) else np.array([])
    dx = dropped["ror"].to_numpy() if len(dropped) else np.array([])
    out = {"n_kept": int(len(kx)), "n_dropped": int(len(dx)),
          "mean_kept": float(kx.mean()) if len(kx) else float("nan"),
          "mean_dropped": float(dx.mean()) if len(dx) else float("nan")}
    out["diff"] = out["mean_kept"] - out["mean_dropped"] if len(kx) and len(dx) else float("nan")
    if len(kx) >= 2 and len(dx) >= 2:
        t, p2 = sps.ttest_ind(kx, dx, equal_var=False)
        out["t"], out["p_one_sided"] = float(t), float(p2 / 2 if t > 0 else 1 - p2 / 2)
    else:
        out["t"], out["p_one_sided"] = float("nan"), float("nan")
    return out


def worst_month(challenger_df: pd.DataFrame, u: str, s: str) -> dict:
    tab = H.monthly_table(challenger_df)
    row = tab[(tab["underlying"] == u) & (tab["structure"] == s)]
    if row.empty:
        return {"n_months": 0, "worst_month": None, "worst_month_usd": float("nan"), "worst_over_median": float("nan")}
    r = row.iloc[0]
    return {"n_months": int(r["n_months"]), "worst_month": r.get("worst_month"),
           "worst_month_usd": float(r.get("worst_month_usd", float("nan"))),
           "worst_over_median": float(r.get("worst_over_median", float("nan")))}


def champion_realised_sd(marked_path: str) -> tuple[pd.Series, str]:
    """The champion's realised dispersion for `scripts/power.py`'s n_required, from the marked
    layer already on disk (`data/backtest/sb_marked.parquet`, untouched) -- the same fallback
    `scripts/power.py`'s `champion_series` uses before the ledger has rows."""
    bt = pd.read_parquet(marked_path)
    if "entry" in bt.columns:
        bt = bt.sort_values("entry")
    label = os.path.relpath(marked_path, config.REPO) if os.path.isabs(marked_path) else marked_path
    return bt["ror"], f"backtest {label} (n={len(bt)})"


def power_plan(min_effect: float = CHALLENGER_MIN_EFFECT, marked_path: str | None = None,
              start: date = config.SB_LEDGER_OPENS, units_per_week: float = 1.0) -> dict:
    """Shared across every challenger of this strategy: n_required depends on the champion's own
    realised dispersion and `min_effect`, not on which challenger is being registered next
    (DESIGN/100 §4)."""
    from engine.improve.spec import spec
    sp = spec(CHALLENGER_STRATEGY)
    series, source = champion_realised_sd(marked_path or sp.backtest_file)
    out = PW.plan(min_effect, series, sp.lag, start, units_per_week)
    out["series_source"] = source
    return out


# ---- registration draft ---------------------------------------------------------------------------

PENDING_MARKER = "PENDING-2026-12-01"    # not ISO-parseable on purpose: `validate_registration`
                                          # (and a stray `open_challengers`/`register` call) must
                                          # not treat this as a live registration before the read.


def build_summary(inputs: P.ProxyInputs, merged: pd.DataFrame, champion: pd.DataFrame,
                  challengers: tuple[Challenger, ...] = CHALLENGERS) -> pd.DataFrame:
    """One row per (challenger, sleeve): the gate footprint, positions, mean ROR and NW t, sign
    consistency across the proxy windows, the worst month, the units-lost comparison against the
    champion, and the matched-trade validity check (RESEARCH/47-edge-gaps.md G10)."""
    entries_total = total_entry_weeks(inputs)
    plan = power_plan()
    rows = []
    for ch in challengers:
        out = run_challenger_proxy(inputs, ch, merged)
        for u, s in H.SLEEVES:
            footprint = gate_footprint(out, u, entries_total)
            st = sleeve_window_stats(out, u, s)
            kvd = kept_vs_dropped(champion, out, u, s)
            matched = matched_diff_check(champion, out, u, s)
            wm = worst_month(out, u, s)
            pos_windows, seen_windows = positive_windows(out, u, s)
            rows.append({
                "challenger_id": ch.challenger_id, "label": ch.label, "sleeve": H.sleeve_name(u, s),
                "underlying": u, "structure": s, "footprint": footprint,
                "n_positions": st["n"], "mean_ror": st["mean_ror"], "nw_t": st["nw_t"], "nw_p": st["nw_p"],
                "hit": st["hit"], "positive_windows": pos_windows, "windows_seen": seen_windows,
                "worst_month": wm["worst_month"], "worst_month_usd": wm["worst_month_usd"],
                "worst_over_median": wm["worst_over_median"],
                "kept_n": kvd["n_kept"], "dropped_n": kvd["n_dropped"], "mean_kept": kvd["mean_kept"],
                "mean_dropped": kvd["mean_dropped"], "units_lost_diff": kvd["diff"], "units_lost_t": kvd["t"],
                "units_lost_p": kvd["p_one_sided"], "matched_n": matched["n_matched"],
                "matched_mean_diff": matched["mean_diff"], "matched_max_abs_diff": matched["max_abs_diff"],
                "n_required": plan["n_required"], "adjudicate_on": plan["adjudicate_on"],
            })
    return pd.DataFrame(rows)


def draft_registration(ch: Challenger, sleeve: str, plan: dict, registered: str = PENDING_MARKER,
                       min_effect: float = CHALLENGER_MIN_EFFECT) -> dict:
    """The exact `REG_REQUIRED` shape `engine.improve.adjudicate.validate_registration` accepts,
    plus `draft: true` and `sleeve` (extra fields validate_registration ignores). With
    `registered=PENDING_MARKER` (the on-disk default) this does NOT pass validate_registration --
    intentionally, so it can never be mistaken for a live one; `tests/test_sb_challengers.py`
    validates the shape with `registered` swapped for a placeholder ISO date."""
    return {
        "policy_id": ch.challenger_id,
        "strategy": CHALLENGER_STRATEGY,
        "champion": config.SB_POLICY_ID,
        "idea": f"{ch.label} (RESEARCH/47-edge-gaps.md G10; DESIGN/80 §8 idea ledger)",
        "params_diff": {ch.param_name: ch.param_value},
        "registered": registered,
        "n_required": int(plan["n_required"]),
        "unit": "post",
        "adjudicate_on": plan["adjudicate_on"],
        "test": ("paired difference in net excess per unit risk, challenger minus champion, on matched "
                 "entry nights; one-sided t with Newey-West lag = overlap; alpha 0.05"),
        "min_effect": min_effect,
        "kill": "if after n_required/2 units the paired mean is below -min_effect, stop early and record FAIL",
        "script_sha256": ADJ.script_sha256(),
        "draft": True,
        "sleeve": sleeve,
        "power_note": ("n_required from min_effect and the champion's realised sd at registration "
                       f"({plan['series_source']}, NW lag {plan['lag']} inflation {plan['inflation']:.3f}); "
                       "shared across every G10 challenger of this strategy"),
    }
