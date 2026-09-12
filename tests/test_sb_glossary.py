"""The S-B report appendix: every column the report writer emits has a glossary row, the frozen
thresholds it quotes are the config values, and the report ends with it."""
from __future__ import annotations

import re

import pytest

from engine.config import SB_GO_T_MIN, SB_SCALE_MIN_POSITIONS
from engine.validation import run_sb_report as R
from engine.validation import sb_glossary as G

pytestmark = pytest.mark.unit

DSR_COLS = ("sr", "sr_star", "deflated_sr", "dsr_prob", "sr_star_null", "deflated_sr_null", "dsr_prob_null", "skew", "kurt")
GO_COLS = ("n_proxy", "mean_proxy", "nw_t_proxy", "bh_pass", "mean_p1", "mean_p2", "mean_p3", "n_marked", "mean_marked",
           "gap_ror", "worst_over_median", "deflated_sr", "deflated_sr_null", "forward_n", "c1_proxy", "c2_marked",
           "c3_month", "c4_dsr", "c4_dsr_null", "c5_scale", "verdict")
MONTH_COLS = ("n_months", "median_month_usd", "worst_month", "worst_month_usd", "worst_over_median", "months_negative",
              "month_rule_pass")
TAIL_COLS = ("worst_ror", "worst_entry", "best_ror", "mean_win_ror", "worst_decile_share_of_loss", "full_width_losses",
             "mean_without_worst_1pct", "mean_without_best_1pct")


def _terms(text: str) -> str:
    return " ".join(re.findall(r"\| `([^`]+)` \|", text))


def test_every_report_column_has_a_glossary_row():
    terms = _terms(G.appendix())
    for col in (*R.SLEEVE_COLS, *DSR_COLS, *GO_COLS, *MONTH_COLS, *TAIL_COLS, "pbo", "mean_logit", "n_combinations"):
        assert col in terms, col


def test_other_structure_names_and_columns_are_covered():
    from engine.validation.sb_alt_structures import ALT_STRUCTURES, TABLE_COLS
    text = G.other_structures()
    for name in ALT_STRUCTURES:
        assert name in text, name
    terms = _terms(G.appendix())
    for col in TABLE_COLS:
        assert col in terms or col in ("n", "structure", "underlying", "nw_t", "hit", "mean_ror", "worst_ror", "mean_margin_usd"), col
    assert "mean_margin_usd" in text


def test_sensitivity_names_and_skip_reasons_are_covered():
    text = G.sensitivities()
    for name in ("base", "gate_off", "g1_only", "g2_only", "costs_x2", "wing_1.5", "band_0.15", "OFF:G1", "OFF:G2",
                 "no_tier1_", "degenerate_strikes"):
        assert name in text, name


def test_thresholds_are_read_from_config():
    text = G.appendix()
    assert f"nw_t ≥ {SB_GO_T_MIN:g}" in text
    assert f"≥ {SB_SCALE_MIN_POSITIONS}" in text
    assert "2023-09-08" in text and "2026-11-06" in text


def test_report_ends_with_the_appendix(monkeypatch, tmp_path):
    monkeypatch.setattr(R.B, "OUT_DIR", str(tmp_path))     # no parquet: every section is the empty placeholder
    text = R.build()
    assert text.rstrip().endswith("none moves before the read.")
    assert text.index(G.APPENDIX_TITLE) > text.index("Go / no-go")
