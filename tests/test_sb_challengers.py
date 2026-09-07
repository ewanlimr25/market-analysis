"""G10: S-B challengers from the CBOE vol-index family (RESEARCH/47-edge-gaps.md §2).

Covers: the additional-condition evaluator (column thresholds, the two VIX-floor forms), the
composed proxy run (subset of the champion, identical pricing on kept weeks -- champion unchanged
when the condition is a tautology), the summary table function, and registration-draft validation
(including that a draft under `ledger/challengers/drafts/` is invisible to `open_challengers`).
"""
from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from engine.improve import adjudicate as ADJ
from engine.improve import sb_challengers as C
from engine.strategies import sb_gate as G
from engine.strategies import sb_proxy as P

pytestmark = pytest.mark.unit


# ---- fixtures -------------------------------------------------------------------------------------

def _sessions(start: date, n: int) -> list[date]:
    out, d = [], start
    while len(out) < n:
        if d.weekday() < 5:
            out.append(d)
        d += timedelta(days=1)
    return out


def _synthetic_inputs(n_sessions: int = 80) -> P.ProxyInputs:
    """Mirrors `tests/test_sb_proxy.py::_synthetic_inputs`: VIX rising linearly so G2 (level above
    its 20-session median) turns ON only after the warm-up window fills."""
    sessions = _sessions(date(2026, 1, 5), n_sessions)
    vix = [15.0 + 0.05 * i for i in range(n_sessions)]
    iv = pd.DataFrame({"date": sessions, "vix": vix, "vix3m": [v + 2 for v in vix],
                       "vxn": [v + 5 for v in vix], "vix9d": [v - 1.0 for v in vix]})
    closes = {(u, d): 100.0 + (0.1 * i if u == "SPY" else -0.1 * i) for i, d in enumerate(sessions) for u in ("SPY", "QQQ")}
    return P.ProxyInputs(index_vol=iv, closes=closes, sessions=sessions)


def _synthetic_ext(inputs: P.ProxyInputs) -> pd.DataFrame:
    """VVIX and SKEW oscillate so a mid-grid threshold keeps roughly half the champion-ON weeks."""
    n = len(inputs.sessions)
    vvix = [90.0 + 20.0 * np.sin(i / 5.0) for i in range(n)]
    skew = [130.0 + 15.0 * np.cos(i / 7.0) for i in range(n)]
    return pd.DataFrame({"date": inputs.sessions, "vvix": vvix, "skew": skew})


@pytest.fixture
def inputs() -> P.ProxyInputs:
    return _synthetic_inputs()


@pytest.fixture
def merged(inputs) -> pd.DataFrame:
    ext = _synthetic_ext(inputs)
    return C.merged_vol_frame(inputs.index_vol, ext)


@pytest.fixture
def champion(inputs) -> pd.DataFrame:
    return P.run_proxy(inputs, gate_mode="both")


# ---- evaluate_condition ----------------------------------------------------------------------

def test_evaluate_condition_column_le_reads_the_prior_close_and_fails_closed_on_missing_data(inputs, merged):
    from engine.config import SB_PARAMS
    ch = C.Challenger("t", "test", C.KIND_COLUMN_LE, "vvix", 100.0, "p", 100.0)
    t, prev = inputs.sessions[30], inputs.sessions[29]
    index_vol = inputs.index_vol
    state = G.gate(index_vol, t, prev, "vix", SB_PARAMS)
    result = C.evaluate_condition(ch, state, "SPY", merged, index_vol)
    row = merged[merged.date == prev].iloc[0]
    assert result == bool(row["vvix"] <= 100.0)
    unknown_state = G._unknown(t, "test")
    assert C.evaluate_condition(ch, unknown_state, "SPY", merged, index_vol) is None
    empty_merged = merged.iloc[0:0]
    assert C.evaluate_condition(ch, state, "SPY", empty_merged, index_vol) is None


def test_evaluate_condition_vix_floor_absolute_differs_by_underlying(inputs):
    from engine.config import SB_PARAMS
    index_vol = inputs.index_vol
    t, prev = inputs.sessions[30], inputs.sessions[29]
    ch = C.CHALLENGERS[0]
    assert ch.kind == C.KIND_VIX_FLOOR_ABS
    spy_state = G.gate(index_vol, t, prev, "vix", SB_PARAMS)
    qqq_state = G.gate(index_vol, t, prev, "vxn", SB_PARAMS)
    assert spy_state.x == pytest.approx(index_vol[index_vol.date == prev].vix.iloc[0])
    assert C.evaluate_condition(ch, spy_state, "SPY", pd.DataFrame(), index_vol) == (spy_state.x >= C.VIX_FLOOR_ABS["SPY"])
    assert C.evaluate_condition(ch, qqq_state, "QQQ", pd.DataFrame(), index_vol) == (qqq_state.x >= C.VIX_FLOOR_ABS["QQQ"])


def test_evaluate_condition_vix_floor_relative_needs_the_full_window():
    from engine.config import SB_PARAMS
    sessions = _sessions(date(2025, 1, 6), 300)
    vix = [15.0 + 0.01 * i for i in range(len(sessions))]
    index_vol = pd.DataFrame({"date": sessions, "vix": vix, "vix3m": [v + 2 for v in vix],
                              "vxn": [v + 5 for v in vix], "vix9d": [v - 1 for v in vix]})
    ch = C.Challenger("t", "test", C.KIND_VIX_FLOOR_REL, None, None, "p", 0.25)
    early_t, early_prev = sessions[100], sessions[99]      # fewer than 252 prior sessions
    state_early = G.gate(index_vol, early_t, early_prev, "vix", SB_PARAMS)
    assert C.evaluate_condition(ch, state_early, "SPY", pd.DataFrame(), index_vol) is None
    late_t, late_prev = sessions[280], sessions[279]        # >= 252 prior sessions
    state_late = G.gate(index_vol, late_t, late_prev, "vix", SB_PARAMS)
    result = C.evaluate_condition(ch, state_late, "SPY", pd.DataFrame(), index_vol)
    assert isinstance(result, bool)
    # a rising-VIX series: the current level is always above its trailing 25th percentile
    assert result is True


# ---- composed proxy run: subset, identical pricing on kept weeks -------------------------------

def test_champion_is_unchanged_when_the_challenger_condition_is_a_tautology(inputs, merged, champion):
    tautology = C.Challenger("taut", "always true", C.KIND_COLUMN_LE, "vvix", 10_000.0, "p", 10_000.0)
    out = C.run_challenger_proxy(inputs, tautology, merged)
    cols = ["underlying", "structure", "entry", "expiry", "ror", "net_usd"]
    pd.testing.assert_frame_equal(champion[cols].reset_index(drop=True), out[cols].reset_index(drop=True))


def test_a_binding_condition_is_a_strict_subset_with_identical_pricing_on_kept_weeks(inputs, merged, champion):
    ch = C.Challenger("mid", "vvix <= 95", C.KIND_COLUMN_LE, "vvix", 95.0, "p", 95.0)
    out = C.run_challenger_proxy(inputs, ch, merged)
    assert 0 < len(out) < len(champion)
    assert set(zip(out.underlying, out.structure, out.entry)) <= set(zip(champion.underlying, champion.structure, champion.entry))
    for u, s in [("SPY", "PS"), ("SPY", "IC"), ("QQQ", "PS"), ("QQQ", "IC")]:
        check = C.matched_diff_check(champion, out, u, s)
        if check["n_matched"]:
            assert check["mean_diff"] == pytest.approx(0.0, abs=1e-9)
            assert check["max_abs_diff"] == pytest.approx(0.0, abs=1e-9)


def test_evaluate_condition_never_lets_through_an_entry_the_champion_gate_refused(inputs, merged):
    """No challenger can ever be a superset of the champion: run every registered challenger and
    check every one of its rows also appears in the champion's own set."""
    champion_keys = set(zip(*[P.run_proxy(inputs, gate_mode="both")[c] for c in ("underlying", "structure", "entry")]))
    for ch in C.CHALLENGERS:
        out = C.run_challenger_proxy(inputs, ch, merged)
        if out.empty:
            continue
        out_keys = set(zip(out.underlying, out.structure, out.entry))
        assert out_keys <= champion_keys, ch.challenger_id


# ---- summary statistics -----------------------------------------------------------------------

def test_gate_footprint_is_the_share_of_total_entry_weeks_kept(inputs, merged, champion):
    ch = C.Challenger("mid", "vvix <= 95", C.KIND_COLUMN_LE, "vvix", 95.0, "p", 95.0)
    out = C.run_challenger_proxy(inputs, ch, merged)
    total = C.total_entry_weeks(inputs)
    fp = C.gate_footprint(out, "SPY", total)
    assert 0.0 <= fp <= 1.0
    assert fp == pytest.approx(out[out.underlying == "SPY"]["entry"].nunique() / total)
    assert C.gate_footprint(pd.DataFrame(), "SPY", total) == 0.0
    assert C.gate_footprint(out, "SPY", 0) == 0.0


def test_kept_vs_dropped_partitions_the_champion_population(inputs, merged, champion):
    ch = C.Challenger("mid", "vvix <= 95", C.KIND_COLUMN_LE, "vvix", 95.0, "p", 95.0)
    out = C.run_challenger_proxy(inputs, ch, merged)
    stat = C.kept_vs_dropped(champion, out, "SPY", "PS")
    champ_n = len(champion[(champion.underlying == "SPY") & (champion.structure == "PS")])
    assert stat["n_kept"] + stat["n_dropped"] == champ_n
    assert stat["n_kept"] == len(out[(out.underlying == "SPY") & (out.structure == "PS")])


def test_worst_month_reports_zero_months_when_nothing_is_kept():
    empty = pd.DataFrame(columns=["underlying", "structure", "entry", "expiry", "ror", "net_usd", "month"])
    wm = C.worst_month(empty, "SPY", "PS")
    assert wm["n_months"] == 0 and wm["worst_month"] is None and np.isnan(wm["worst_month_usd"])


def test_positive_windows_counts_only_windows_with_positions(inputs, merged):
    ch = C.Challenger("mid", "vvix <= 95", C.KIND_COLUMN_LE, "vvix", 95.0, "p", 95.0)
    out = C.run_challenger_proxy(inputs, ch, merged)
    positive, seen = C.positive_windows(out, "SPY", "PS")
    assert 0 <= positive <= seen <= 3          # at most P1, P2, P3


# ---- the summary table function ----------------------------------------------------------------

def test_build_summary_has_one_row_per_challenger_per_sleeve(inputs, merged, champion):
    small = C.CHALLENGERS[:3]
    out = C.build_summary(inputs, merged, champion, challengers=small)
    assert len(out) == len(small) * 4          # 4 sleeves
    assert set(out.challenger_id) == {c.challenger_id for c in small}
    for col in ("footprint", "n_positions", "mean_ror", "nw_t", "units_lost_diff", "matched_max_abs_diff",
               "n_required", "adjudicate_on"):
        assert col in out.columns
    # every kept-weeks matched-diff check is ~0 (identical pricing to the champion on those weeks)
    assert out["matched_max_abs_diff"].fillna(0).abs().max() < 1e-9
    # n_required and adjudicate_on are the same for every challenger (driven by the champion's own dispersion)
    assert out["n_required"].nunique() == 1 and out["adjudicate_on"].nunique() == 1


def test_all_fourteen_pre_stated_challengers_are_distinct_and_form_the_deflation_trial_count():
    assert C.TRIAL_COUNT == len(C.CHALLENGERS) == 14
    assert len({c.challenger_id for c in C.CHALLENGERS}) == 14


# ---- registration drafts ----------------------------------------------------------------------

def test_draft_registration_matches_the_REG_REQUIRED_shape_once_registered_is_a_real_date():
    plan = {"n_required": 15, "adjudicate_on": "2026-12-25", "series_source": "test", "lag": 2, "inflation": 1.0}
    ch = C.CHALLENGERS[0]
    draft = C.draft_registration(ch, "SPY-PS", plan)
    assert draft["registered"] == C.PENDING_MARKER
    with pytest.raises(ValueError):
        ADJ.validate_registration(draft)          # PENDING marker is not ISO-parseable: refused on purpose
    live_shaped = {**draft, "registered": "2026-12-01"}
    ADJ.validate_registration(live_shaped)         # the rest of the shape is REG_REQUIRED-compliant
    assert set(ADJ.REG_REQUIRED) <= set(draft.keys())
    assert len(draft["params_diff"]) == 1
    assert draft["draft"] is True and draft["sleeve"] == "SPY-PS"


def test_every_challenger_draft_validates_once_registered_is_a_real_date():
    plan = {"n_required": 15, "adjudicate_on": "2026-12-25", "series_source": "test", "lag": 2, "inflation": 1.0}
    for ch in C.CHALLENGERS:
        draft = C.draft_registration(ch, "SPY-PS", plan)
        ADJ.validate_registration({**draft, "registered": "2026-12-01"})


def test_drafts_under_ledger_challengers_drafts_are_invisible_to_open_challengers(tmp_path):
    """The safety property `scripts/sb_challengers.py --drafts` relies on: `open_challengers` lists
    `ledger/challengers/` non-recursively, so a subdirectory of drafts is never opened."""
    ledger_root = tmp_path / "ledger"
    drafts_dir = ledger_root / "challengers" / "drafts"
    drafts_dir.mkdir(parents=True)
    plan = {"n_required": 15, "adjudicate_on": "2026-12-25", "series_source": "test", "lag": 2, "inflation": 1.0}
    draft = C.draft_registration(C.CHALLENGERS[0], "SPY-PS", plan)
    import json
    with open(drafts_dir / f"{draft['policy_id']}.json", "w") as fh:
        json.dump(draft, fh)
    assert ADJ.open_challengers(str(ledger_root), "sb") == []


def test_power_plan_reads_the_champions_realised_dispersion_from_an_explicit_marked_path(tmp_path):
    marked = tmp_path / "sb_marked.parquet"
    pd.DataFrame({"entry": pd.date_range("2026-03-13", periods=10, freq="7D").date,
                 "ror": np.linspace(0.02, 0.08, 10)}).to_parquet(marked)
    plan = C.power_plan(min_effect=0.01, marked_path=str(marked))
    assert plan["n_required"] >= 2
    assert date.fromisoformat(plan["adjudicate_on"]) >= date(2026, 9, 11)
    assert "series_source" in plan and "sb_marked.parquet" in plan["series_source"]
