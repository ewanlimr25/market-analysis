# Validated lanes — full detail

Priors from `research/20`, `50`, `70`. Harness column re-baselined **2026-08-08** on the FULL liquid
universe (panel→08-07, 83 days, 2,471-ticker spine). Parentheses hold the **prior 785-ticker-spine
figure**, so each pair shows what the universe refresh revealed — not a live prior and not one cycle of
drift. Separately, every pre-07-24 figure was measured on a universe with a calendar-day earnings gate
and, for OI_FADE, no ETP exclusion at all; those corrections are described in the per-lane notes below and
in [`regression-gate.md`](regression-gate.md).

**Read this whole table against the regression-gate history:** the two momentum legs fell hard because the
old spine was a flattering subset, OI_FADE was untouched by tripling the universe, and S2/S4 held their
means on double the n. Nothing here is a decay signal.

**These are HISTORICAL-panel priors.** The forward book is graded separately by `/calibration-audit`; as of
2026-08-08 the forward cluster-unit read is softer on every lane except S4 (see
`analyses/audit/2026-08-08/SUMMARY.md`), but no lane cleared BH(0.10), so none is stopped.

| Lane | Dir | Horizon | Realized (harness, 2026-08-08 baseline) | Note |
|---|---|---|---|---|
| `oi-flow-fade` (OI_FADE) | short | h10 | hit 0.55 vs 0.38, **+0.95% median / +0.59% mean, n=1087** *(785-spine: +0.93% med / +0.54% mean, n=1050)* | **Most robust — and the universe refresh proved it.** Tripling the spine added only 37 rows and moved the mean +0.0054→+0.0059: the edge was never a subset artifact. Heavy call-OI build; heavy 5d call-OI build → underperform. Pre-07-24 figure was inflated ~2× by leveraged/thematic ETFs (SOXS 3× inverse semis et al.) the live lane never trades. **Forward watch — decay signal NOT confirmed:** the 08-01 audit flagged a −3.73% new-evidence cohort (hit−base −0.53) as possible decay and named the post-fix h10 cohort as the test. That cohort matured and **reversed the sign: +1.99%, hit−base +0.67** (9 units, 3 exit-days, ANECDOTE). Neither read is durable — do not act on either; re-test when the 17 open h10 rows mature. |
| `momentum` MOM_SHORT (near-52w-low) | short | h10 | **−1.28% mean**, median −1.39%, hit 0.40 vs 0.37, n=803 *(785-spine: −0.43%, hit 0.46 vs 0.29, n=351)* | Crash-gated (`s1_standdown`) + **watch-only cap for new starters**. The negative mean is the binding read — and on the full universe the **hit−base collapsed +16.2pp → +2.9pp**, so "wins often, loses big" was itself a subset artifact. Do not cite the +16.2pp figure. See [`regression-gate.md`](regression-gate.md#mom_short-a-knowingly-negative-recorded-exception) for the full three-step history. |
| `momentum` MOM_LONG (near-52w-high) | long | h10 | **−1.08% mean**, median −1.37%, hit 0.43 vs 0.62, n=1066 *(785-spine: +0.08%, n=506)* | **WATCH/BASKET ONLY — this lane never sizes.** The full universe turns it outright negative, corroborating the forward book's BH(0.10)-negative read. Basket only, never per-name HIGH; sector-concentration capped (gate #7). Enforced by `risk-sizer.md`'s advisory map and confirmed forward: **0 of 52 resolved calls were ever sized**. It is also the one lane clearing BH(0.10) negative on the forward book under day-clustering (−4.65%, p=0.008, 14 basket-days, PROVISIONAL-N — below the DURABLE-N bar a STOP requires). |
| `liquidity-reversion` (S2) | long | h3–5 | +0.09%, n=1123 *(785-spine: +0.07%, n=559)* | DP one-sided concentration, news-gated; advisory-only. Held its mean on double the n. |
| `sentiment-contrarian` (S4) | long | h5–10 | +0.35%, n=1145 *(785-spine: +0.39%, n=396)* | PCR-high fade; + ivrank_chg_5d h3 tilt (advisory). Held its mean on ~3× the n. The only lane positive forward as well as historically. |
| `vol-book` | non-dir | event/0DTE | VOL-ONLY | Earnings IV-crush + 0DTE-VRP, net-of-cost. |
| `fundamentals-gate` | veto | — | risk filter | Finnhub = veto, not alpha (`research/80`). |
