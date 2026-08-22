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
| `oi-flow-fade` (OI_FADE) | short | h10 | **+0.13% mean, n=1177, hit 0.54 vs 0.36** (post full-window fix; was +0.38%/n=1176) | ⚠️ **ADVISORY ONLY — demoted from sizing 2026-08-22; this was the last lane that sized, so the book now sizes nothing.** Two things changed. (1) **Artifact removal, not decay:** `oi_net_5d` is `avg()` over a window not requiring 5 obs, so partial-window names inflated into the top-15 — 75/1237 rows carried +2.77% vs +0.13% for full-window rows, 60 of them in the panel's first four days; paired by exit-day the artifact is worth +0.21pp, p=0.018. `hit − base` *improved* (+0.155 → +0.184), so mean was removed, not hit-rate. (2) **No validated edge:** corrected +0.0013 is indistinguishable from zero (79 exit-days, p=0.767) and the live lane's floored selection reads −0.0081 (24 exit-days, p=0.080). **The ranking was NOT changed** — a first counterfactual claiming raw beat `oi_rel_build` omitted the lane's own tiny-base floors and is retracted; faithfully floored `oi_rel_build` (−0.0081) beats raw (−0.0093) and the persistence gate helps. The open question is the FLOORS (1177 rows → 360, and that subset is negative), which 24 exit-days cannot settle. Forward book separately frozen at ~80 cluster-units by re-signal dedup. [`regression-gate.md`](regression-gate.md#oi_fade-the-baseline-carried-an-artifact-and-the-rules-are-not-distinguishable-2026-08-22) |
| `momentum` MOM_SHORT (near-52w-low) | short | h10 | **−1.40% mean**, median −1.50%, hit 0.40 vs 0.36, n=828 *(785-spine: −0.43%, hit 0.46 vs 0.29, n=351)* | Crash-gated (`s1_standdown`) + **watch-only cap for new starters**. The negative mean is the binding read — and on the full universe the **hit−base collapsed +16.2pp → +3.7pp**, so "wins often, loses big" was itself a subset artifact. Do not cite the +16.2pp figure. See [`regression-gate.md`](regression-gate.md#mom_short-a-knowingly-negative-recorded-exception) for the full history. |
| `momentum` MOM_LONG (near-52w-high) | long | h10 | **−1.22% mean**, median −1.56%, hit 0.43 vs 0.64, n=1121 *(785-spine: +0.08%, n=506)* | **WATCH/BASKET ONLY — this lane never sizes.** The full universe turns it outright negative, corroborating the forward book's BH(0.10)-negative read. Basket only, never per-name HIGH; sector-concentration capped (gate #7). Enforced by `risk-sizer.md`'s advisory map and confirmed forward: **0 of 52 resolved calls were ever sized**. Day-clustered it is the worst lane in the book (−4.99%, 14 basket-days, p=0.029) but **its 08-08 BH(0.10) significance has lapsed** (p=0.008 → 0.029; the m=5 cut is 0.02) — as of 2026-08-15 **no lane clears BH in any view**. PROVISIONAL-N, below the DURABLE-N bar a STOP requires. |
| `liquidity-reversion` (S2) | long | h3–5 | +0.11%, n=1185 *(785-spine: +0.07%, n=559)* | DP one-sided concentration, news-gated; advisory-only. Held its mean on double the n. |
| `sentiment-contrarian` (S4) | long | h5–10 | **+0.25%, n=1241** *(pre-fix: +0.48%; 08-15 baseline: +0.41%, n=1202; 785-spine: +0.39%, n=396)* | PCR-high fade; + ivrank_chg_5d h3 tilt (advisory). **Re-baselined 2026-08-17 after the call-volume floor fix** (`S4_MIN_CALL_VOLUME = 250`): the old filter's combined `call+put ≥ 1000` floor left the CALL leg unconstrained, so NWG cleared it on **3 call contracts** vs 2,046 puts and printed PCR 682 at rank #1. Panel-wide the median S4 pick carried just **154** calls (p25 = 66). The drop is **artifact removal, not decay** — but note the two things it exposes: (1) the removed names were supplying the lane's right tail, and (2) **`hit − base` was already negative before the fix** (−0.041 → −0.056), so S4 has never had a hit-rate edge here. ⚠️ **The forward +1.25% (48 units, 2026-08-15) is NOT clean** — those rows were selected by the buggy filter too, so the "only lane positive forward as well as historically" claim is unverified until forward rows accumulate under the corrected floor. Treat S4 forward as pre-registered from 2026-08-17. See [`regression-gate.md`](regression-gate.md#s4-re-baseline-00041--00025-2026-08-17--artifact-removal-not-decay). |
| `vol-book` | non-dir | event/0DTE | VOL-ONLY | Earnings IV-crush + 0DTE-VRP, net-of-cost. |
| `fundamentals-gate` | veto | — | risk filter | Finnhub = veto, not alpha (`research/80`). |
