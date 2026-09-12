"""The column-and-symbol appendix of the S-B report (DESIGN/80 §6), emitted at the end of
`run_sb_report` so every weekend's `sb_report.md` carries its own key. Static text; the numbers it
quotes are the frozen parameters, read from `engine.config` so the appendix cannot drift from them."""
from __future__ import annotations

from engine.config import (SB_DSR_TRIALS, SB_GO_MONTH_LOSS_MULT, SB_GO_T_MIN, SB_NW_LAG, SB_PARAMS, SB_PBO_BLOCKS,
                           SB_SCALE_MIN_POSITIONS, SB_SIZING, SB_WINDOWS, BH_FDR)

APPENDIX_TITLE = "Appendix: columns and symbols"


def _rows(items: list[tuple[str, str]]) -> str:
    return "\n".join(["| term | meaning |", "|---|---|", *(f"| `{k}` | {v}" + " |" for k, v in items)])


def _windows() -> str:
    return "; ".join(f"`{k}` {a.isoformat()} to {b.isoformat()}" for k, (a, b) in SB_WINDOWS.items())


def vocabulary() -> str:
    p = SB_PARAMS
    return _rows([
        ("sleeve", "one (underlying, structure): `SPY-PS`, `SPY-IC`, `QQQ-PS`, `QQQ-IC`. Never pooled across sleeves."),
        ("PS / IC", "put spread (short `p1`, long `p2`) / iron condor (the put spread plus short `c1`, long `c2`). §3.5"),
        ("p1, p2, c1, c2", f"the four legs; targets `S(1-m)`, `S(1-2m)`, `S(1+m)`, `S(1+2m)` with wings at {p.wing_sigma:g}σ. §3.4"),
        ("proxy", "layer 1: three years of positions priced from CBOE closes with a fixed smile and spread (§5.1). "
                  "Every leg is tier 3."),
        ("marked", "layer 2: positions priced from the panel's late prints (§5.2), each leg a tier-1 print. "
                   "Pooled = the `P3` window only."),
        ("forward", "layer 3: `ledger/sb/`, the paper positions the nightly emits from 2026-09-11. §5.3"),
        ("window", f"a proxy sub-period ({_windows()}); `pooled` = all three."),
        ("gate, ON / OFF:G1 / OFF:G2 / UNKNOWN", "G1 = `VIX3M > VIX` (contango); G2 = `X > median(X, prior "
         f"{p.median_window} sessions)`. ON needs both; `OFF:G1` failed G1 first, `OFF:G2` failed G2; UNKNOWN = an "
         "input missing, fail closed. Read on the prior session's closes. §2"),
        ("X, x, mean_x", "the vol index for the underlying: VIX for SPY, VXN for QQQ. `x` on a row is the entry "
                         "session's close; `mean_x` its average over the rows. §3.3"),
        ("m", "the σ unit `X/100 × sqrt(DTE_cal/365)`; strikes sit at 1m and 2m from spot. §3.3"),
        ("tier", "mark quality of a leg: 1 = late print with size ≥ "
                 f"{p.leg_size_min} (marked entries); 3 = proxy model price; 4 = intrinsic at expiry (every exit). "
                 "`entry_tier_max` is the worst leg on the row."),
        ("credit", "net premium received per share at entry; `width` the distance `p1 − p2` (or the wider wing for an IC)."),
        ("max_loss_usd / risk_usd / contracts", "max loss per contract `(width − credit) × 100`; `contracts` is the "
         f"largest count with max loss ≤ {SB_SIZING.max_loss_frac:.0%} of ${SB_SIZING.equity:,.0f}; `risk_usd` = "
         "max loss × contracts. §4"),
        ("net_usd, net_usd_total", "P&L of the position at the frozen sizing after costs (half-spread per leg touch plus "
                                   "$0.65 a contract), and its sum over the cell. §3.8"),
        ("ror, mean_ror, median_ror", "return on risk = `net_usd / risk_usd`; the primary unit. A full-width loss is −100%."),
        ("hit", "share of positions with `ror > 0`."),
        ("mean_risk_usd", "average `risk_usd` over the rows of the cell."),
        ("credit_over_width, mean_credit_over_width", "credit as a share of width: how much of the max loss is collected up front."),
        ("cost_over_credit, mean_cost_over_credit", "round-trip cost as a share of the credit collected."),
    ])


def statistics() -> str:
    return _rows([
        ("n / expiries", "positions in the cell / distinct expiry sessions (the clusters)."),
        ("nw_t, nw_p", f"Newey-West (Bartlett, lag {SB_NW_LAG}) t of the mean `ror` on the entry-ordered series, "
                       "and its p (Student t, n − 1 df). The primary t: weekly entries overlap three-deep. §6.1"),
        ("cl_t, cl_p", "the same mean with the SE clustered by expiry session; the companion t, G − 1 df."),
        ("bh_pass", f"Benjamini-Hochberg at FDR {BH_FDR:g} across the four sleeves on `nw_p`: true if the sleeve is "
                    "rejected (its p survives the multiplicity charge). §6.3"),
        ("sr", "per-position Sharpe, `mean(ror) / sd(ror)`, not annualised."),
        ("sr_star", f"the expected best Sharpe among {SB_DSR_TRIALS} null trials (4 sleeves + 2 alternates), charging "
                    "the observed cross-sleeve variance of the Sharpe. §6.3"),
        ("deflated_sr", "`sr − sr_star`; > 0 is criterion 4. The pre-registered estimator."),
        ("dsr_prob", "probabilistic Sharpe: P(true SR > `sr_star`) given the sample's skew and kurtosis."),
        ("sr_star_null, deflated_sr_null, dsr_prob_null", "the same three charging the null sampling variance `1 / min(n)` "
         "instead of the observed cross-sleeve variance (D16). Reported beside the pre-registered version; when the "
         "two disagree the read records both and the null benchmark governs."),
        ("skew, kurt", "sample skew and non-excess kurtosis of `ror` (a normal has kurt 3). Hold-to-expiry spreads are "
                       "bimodal, so these are large."),
        ("pbo", f"probability of backtest overfitting (CSCV over {SB_PBO_BLOCKS} entry blocks): the share of in-sample / "
                "out-of-sample splits in which the best sleeve in-sample ranks below the median out-of-sample. 0.5 is "
                "coin-flip; the four sleeves are the configurations."),
        ("mean_logit, n_combinations", "mean logit of the out-of-sample rank across splits (negative = worse than median); "
                                       "number of splits (half of the blocks in-sample)."),
        ("n_months, median_month_usd, worst_month, worst_month_usd", "net $ per expiry month at the frozen sizing; "
                                                                      "the median month, and the worst month and its $."),
        ("worst_over_median", f"`−worst_month_usd / median_month_usd`; the month rule needs a positive median and this "
                              f"ratio ≤ {SB_GO_MONTH_LOSS_MULT:g}. §6.7(3)"),
        ("months_negative / month_rule_pass", "count of losing months / the rule's verdict."),
        ("worst_ror, worst_entry, best_ror, mean_win_ror", "the single worst and best positions (and the worst one's "
                                                            "entry date); mean `ror` over winning positions."),
        ("worst_decile_share_of_loss", "share of all losses (in `ror`) sitting in the worst tenth of positions: tail concentration."),
        ("full_width_losses", "positions that lost at least 98% of risk (the spread finished fully in the money)."),
        ("mean_without_worst_1pct / mean_without_best_1pct", "mean `ror` with the worst / best 1% of positions removed: "
                                                                "how much of the mean is one tail."),
    ])


def sensitivities() -> str:
    p = SB_PARAMS
    return _rows([
        ("base", "the frozen rule: gate ON, frozen costs, wings at 2σ, strike band ±0.25σ."),
        ("gate_off", "a position every entry Friday regardless of the gate (the gate's marginal value is base vs this)."),
        ("g1_only / g2_only", "gate = contango only / level-above-median only."),
        ("costs_x2", "every cost doubled (proxy only)."),
        ("wing_1.5", "wings at 1.5σ instead of 2σ."),
        ("band_0.15", f"marked only: nearest tier-1 strike within ±0.15σ instead of ±{p.strike_band_sigma:g}σ."),
        ("skipped reason `OFF:G1`, `OFF:G2`", "no entry because the gate was off (which condition failed first)."),
        ("skipped reason `no_tier1_<leg>`", "no strike with a tier-1 print inside the band for that leg (marked layer only)."),
        ("skipped reason `degenerate_strikes`", "the order `p2 < p1 < S < c1 < c2` did not hold."),
    ])


def verdict_columns() -> str:
    return _rows([
        ("n_proxy, mean_proxy, nw_t_proxy", "pooled proxy count, mean `ror` and NW t."),
        ("mean_p1, mean_p2, mean_p3", "mean `ror` in each proxy window; criterion 1 needs all three > 0."),
        ("n_marked, mean_marked", "marked positions and their mean `ror` (the `P3` panel window)."),
        ("gap_ror", "on the (entry, sleeve) pairs both layers hold, `proxy mean − marked mean`; criterion 2 allows a gap "
                    "up to the marked round-trip cost."),
        ("forward_n", f"graded positions in `ledger/sb/`; criterion 5 needs ≥ {SB_SCALE_MIN_POSITIONS} with a positive mean."),
        ("c1_proxy", f"mean > 0, `nw_t ≥ {SB_GO_T_MIN:g}`, `bh_pass`, and a positive mean in every window."),
        ("c2_marked", "marked mean > 0 and the overlap check passes."),
        ("c3_month", "the month rule (`worst_over_median`)."),
        ("c4_dsr", "`deflated_sr > 0`, the pre-registered estimator."),
        ("c4_dsr_null", "`deflated_sr_null > 0`, the D16 companion; reported, does not enter the verdict."),
        ("c5_scale", "the forward count trigger for sizing above one contract."),
        ("verdict", "`GO-MIN`: clears 1 to 4, one contract at the read. `GO-SCALE`: also 5. `NO-GO`: fails one of 1 to 4 "
                    "(the note names which). `NOT YET`: the proxy holds no positions for the sleeve."),
    ])


def appendix() -> str:
    return "\n".join([
        f"\n## {APPENDIX_TITLE}\n",
        "Layers, gate and position columns (DESIGN/80 §2 to §5):\n", vocabulary(),
        "\nStatistics (§6.1 to §6.5):\n", statistics(),
        "\nSensitivities and skip reasons (§6.6; descriptive, cannot promote a configuration):\n", sensitivities(),
        "\nGo / no-go columns (§6.7; read 2026-12-01):\n", verdict_columns(),
        "\nPercentages are `ror` unless the column says `usd`. Every threshold above is read from `engine/config.py`; "
        "none moves before the read.\n",
    ])
