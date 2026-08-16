# Validated lanes — full detail

Priors from `research/20`, `50`, `70`. Harness column re-baselined **2026-08-15** on the FULL liquid
universe (panel→08-14, 88 days, 2,471-ticker spine). Parentheses hold the **prior 785-ticker-spine
figure**, so each pair shows what the universe refresh revealed — not a live prior and not one cycle of
drift. Separately, every pre-07-24 figure was measured on a universe with a calendar-day earnings gate
and, for OI_FADE, no ETP exclusion at all; those corrections are described in the per-lane notes below and
in [`regression-gate.md`](regression-gate.md).

**Read this whole table against the regression-gate history:** the two momentum legs fell hard because the
old spine was a flattering subset, OI_FADE was untouched by tripling the universe, and S2/S4 held their
means on double the n. Nothing here is a decay signal.

⚠️ **Every figure below is depressed by a correlated draw.** The 08-15 increment is 317 rows across only
**5 exit-days** (08-10→08-14) with `base` pinned 1.00/0.00 — the continuation of the rally that also set
the 08-08 baseline. Rows matured at the 08-07 edge still reproduce the previous figures (OI_FADE
*exactly*). When the window unwinds these means will rise on their own; **that is not a lane improving.**

**These are HISTORICAL-panel priors.** The forward book is graded separately by `/calibration-audit`; as of
2026-08-15 the forward cluster-unit read is softer on every lane except S4 (see
`analyses/audit/2026-08-15/SUMMARY.md`), but no lane cleared BH(0.10), so none is stopped.

| Lane | Dir | Horizon | Realized (harness, 2026-08-15 baseline) | Note |
|---|---|---|---|---|
| `oi-flow-fade` (OI_FADE) | short | h10 | hit 0.54 vs 0.36, **+0.77% median / +0.37% mean, n=1159** *(785-spine: +0.93% med / +0.54% mean, n=1050)* | **Most robust — and the universe refresh proved it.** Tripling the spine added only 37 rows and moved the mean +0.0054→+0.0059: the edge was never a subset artifact. It is also **flat across regimes** (CHOP +0.0039 / PULLBACK +0.0036 / UPTREND +0.0034), rare stability for the only lane that sizes. Heavy call-OI build; heavy 5d call-OI build → underperform. Pre-07-24 figure was inflated ~2× by leveraged/thematic ETFs (SOXS 3× inverse semis et al.) the live lane never trades. The +0.59%→+0.37% dip is the 5-exit-day 08-10→08-14 increment (−0.0286, n=74, base 0.00); the 08-07 cohort still prints +0.0059 exactly. **Forward watch — decay signal NOT confirmed, now deferred twice:** the 08-01 audit flagged a −3.73% cohort as possible decay; the post-fix cohort **reversed the sign (+1.99%, hit−base +0.67**, 9 units, 3 exit-days). 08-15 forward reads −0.65% (81 units, p=0.605) on 6 new units across 4 exit-days in a +3.3–5.9% tape. None of these is durable — do not act on any; re-test when the 11 open + 4 pending h10 rows mature 08-17→08-22. |
| `momentum` MOM_SHORT (near-52w-low) | short | h10 | **−1.40% mean**, median −1.50%, hit 0.40 vs 0.36, n=828 *(785-spine: −0.43%, hit 0.46 vs 0.29, n=351)* | Crash-gated (`s1_standdown`) + **watch-only cap for new starters**. The negative mean is the binding read — and on the full universe the **hit−base collapsed +16.2pp → +3.7pp**, so "wins often, loses big" was itself a subset artifact. Do not cite the +16.2pp figure. See [`regression-gate.md`](regression-gate.md#mom_short-a-knowingly-negative-recorded-exception) for the full history. |
| `momentum` MOM_LONG (near-52w-high) | long | h10 | **−1.22% mean**, median −1.56%, hit 0.43 vs 0.64, n=1121 *(785-spine: +0.08%, n=506)* | **WATCH/BASKET ONLY — this lane never sizes.** The full universe turns it outright negative, corroborating the forward book's BH(0.10)-negative read. Basket only, never per-name HIGH; sector-concentration capped (gate #7). Enforced by `risk-sizer.md`'s advisory map and confirmed forward: **0 of 52 resolved calls were ever sized**. Day-clustered it is the worst lane in the book (−4.99%, 14 basket-days, p=0.029) but **its 08-08 BH(0.10) significance has lapsed** (p=0.008 → 0.029; the m=5 cut is 0.02) — as of 2026-08-15 **no lane clears BH in any view**. PROVISIONAL-N, below the DURABLE-N bar a STOP requires. |
| `liquidity-reversion` (S2) | long | h3–5 | +0.11%, n=1185 *(785-spine: +0.07%, n=559)* | DP one-sided concentration, news-gated; advisory-only. Held its mean on double the n. |
| `sentiment-contrarian` (S4) | long | h5–10 | +0.41%, n=1202 *(785-spine: +0.39%, n=396)* | PCR-high fade; + ivrank_chg_5d h3 tilt (advisory). Held its mean on ~3× the n. The only lane positive forward as well as historically (+1.25%, 48 units, 2026-08-15). |
| `vol-book` | non-dir | event/0DTE | VOL-ONLY | Earnings IV-crush + 0DTE-VRP, net-of-cost. |
| `fundamentals-gate` | veto | — | risk filter | Finnhub = veto, not alpha (`research/80`). |
