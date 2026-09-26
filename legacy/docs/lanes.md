# Validated lanes — full detail

Priors from `research/20`, `50`, `70`. Harness column re-baselined **2026-08-15** on the FULL liquid
universe (panel→08-14, 88 days, 2,471-ticker spine), **except OI_FADE, whose row carries 2026-08-29
figures on the 98-day panel** (panel→08-28) because its shipped rule was re-graded twice since.
Parentheses hold the **prior 785-ticker-spine figure**, so each pair shows what the universe refresh
revealed — not a live prior and not one cycle of drift. Separately, every pre-07-24 figure was measured on a universe with a calendar-day earnings gate
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

**Where a lane's shipped rule differs from the rule its prior was measured on, this table quotes the
SHIPPED rule** (added 2026-08-29). OI_FADE is the case that forced it: the raw-rank prior and the live
`oi_rel_build` rule carry **opposite signs**, and the table had been quoting the one the engine does not
run. Forward as of 2026-09-05, no lane clears BH(0.10) under the governing `cluster_id` unit, so there is
still no forward STOP — but MOM_LONG is BH-significant negative under the `lane-exit-day` view
(−4.65%, 14 units, p=0.008), which is a caveat, not a STOP, because it sits below the 30-unit bar.

⚠️ **At h10, quote Newey-West next to any clustered p** (added 2026-09-05). `lane-exit-day` clustering
fixes the *unit*, not the 9/10-day *overlap* between consecutive h10 windows, so the clustered t is an
upper bound on significance. Ignoring this is what put `OI_FADE_LIVE` in a stand-down it never earned.

| Lane | Dir | Horizon | Realized (harness, 2026-08-15 baseline) | Note |
|---|---|---|---|---|
| `oi-flow-fade` (OI_FADE) | short | h10 | **`OI_FADE_LIVE` (shipped rule): −0.65%, n=510, 34 `lane-exit-day`, p=0.093 — FAILS BH(0.10); NW(L=9) p=0.290.** Raw-rank full pool, reference only: −0.14%, n=1327 | **ADVISORY — watch-only since 2026-09-05; never sizes.** Four findings, in order. (1) **2026-08-22, artifact removal, not decay:** `oi_net_5d` is `avg()` over a window not requiring 5 obs, so partial-window names inflated into the top-15 — 75/1237 rows carried +2.77% vs +0.13%; `hit − base` *improved* (+0.155 → +0.184), so mean was removed, not hit-rate. (2) **2026-08-22, no validated positive edge:** corrected +0.0013 is indistinguishable from zero (79 `lane-exit-day`, p=0.767); demoted from sizing to advisory. **The ranking was NOT changed** — a counterfactual claiming raw beat `oi_rel_build` omitted the lane's own tiny-base floors and is retracted. (3) **2026-08-29, stood down to diary-only** on `OI_FADE_LIVE` −0.0093, p=0.028, surviving BH(0.10). (4) **2026-09-05, the re-check fired on OUTCOME 2 and the stand-down is retracted.** At 34 complete `lane-exit-day` (zero partial) it reads −0.0065, **p=0.0929, failing BH(0.10)**; the lane returns to advisory. ⚠️ **Two 08-29 claims are dead and must not be re-cited:** the p=0.028 was **uncorrected** — Newey-West reads **0.143 on that very cohort**, so the lane was never significant under the overlap correction — and ex-MSTR/CELH/MARA robustness decayed −0.0070 → **−0.0045, p=0.218**. ⚠️ **The sign is still negative on every cut**; advisory restores a watch list, not an endorsement. The raw-pool baseline crossing zero (+0.0013 → −0.0014) remains **three tickers** — MSTR/MARA/CELH on five consecutive sessions into one crypto squeeze; drop them and it is **+0.0017**, so it is NOT decay and must NOT be re-baselined. The open 08-22 question — whether the FLOORS help or hurt (1177 rows → 360, that subset negative) — is unchanged and 34 `lane-exit-day` still cannot settle it. Forward book separately frozen at ~88 cluster-units by re-signal dedup. [`regression-gate.md`](regression-gate.md#the-oi_fade_live-re-check-fired-on-outcome-2--lane-restored-to-advisory-2026-09-05) |
| `momentum` MOM_SHORT (near-52w-low) | short | h10 | **−1.40% mean**, median −1.50%, hit 0.40 vs 0.36, n=828 *(785-spine: −0.43%, hit 0.46 vs 0.29, n=351)* | Crash-gated (`s1_standdown`) + **watch-only cap for new starters**. The negative mean is the binding read — and on the full universe the **hit−base collapsed +16.2pp → +3.7pp**, so "wins often, loses big" was itself a subset artifact. Do not cite the +16.2pp figure. See [`regression-gate.md`](regression-gate.md#mom_short-a-knowingly-negative-recorded-exception) for the full history. |
| `momentum` MOM_LONG (near-52w-high) | long | h10 | **−1.22% mean**, median −1.56%, hit 0.43 vs 0.64, n=1121 *(785-spine: +0.08%, n=506)* | **WATCH/BASKET ONLY — this lane never sizes.** The full universe turns it outright negative, corroborating the forward book's BH(0.10)-negative read. Basket only, never per-name HIGH; sector-concentration capped (gate #7). Enforced by `risk-sizer.md`'s advisory map and confirmed forward: **0 of 52 resolved calls were ever sized**. Day-clustered it is the worst lane in the book. ⚠️ **Its BH(0.10) significance has RETURNED (2026-08-29):** under the `lane-exit-day` view it reads **−4.65%, 14 units, p=0.008, BH-SIGNIF** — it had lapsed at 08-15 (p=0.008 → 0.029 against an m=5 cut of 0.02), so "no lane clears BH in any view" was true only for 08-15/08-22 and **must not be re-cited**. It is still **not a STOP**: the governing `cluster_id` unit reads −1.45%, p=0.440 (ns), and 14 `lane-exit-day` is below the 30-unit bar, so this is a correlated-draw caveat. PROVISIONAL-N, below the DURABLE-N bar a STOP requires — and the lane never sizes regardless. |
| `liquidity-reversion` (S2) | long | h3–5 | +0.11%, n=1185 *(785-spine: +0.07%, n=559)* | DP one-sided concentration, news-gated; advisory-only. Held its mean on double the n. |
| `sentiment-contrarian` (S4) | long | h5–10 | **+0.25%, n=1241** *(pre-fix: +0.48%; 08-15 baseline: +0.41%, n=1202; 785-spine: +0.39%, n=396)* | PCR-high fade; + ivrank_chg_5d h3 tilt (advisory). **Re-baselined 2026-08-17 after the call-volume floor fix** (`S4_MIN_CALL_VOLUME = 250`): the old filter's combined `call+put ≥ 1000` floor left the CALL leg unconstrained, so NWG cleared it on **3 call contracts** vs 2,046 puts and printed PCR 682 at rank #1. Panel-wide the median S4 pick carried just **154** calls (p25 = 66). The drop is **artifact removal, not decay** — but note the two things it exposes: (1) the removed names were supplying the lane's right tail, and (2) **`hit − base` was already negative before the fix** (−0.041 → −0.056), so S4 has never had a hit-rate edge here. ⚠️ **The forward +1.25% (48 units, 2026-08-15) is NOT clean** — those rows were selected by the buggy filter too, so the "only lane positive forward as well as historically" claim is unverified until forward rows accumulate under the corrected floor. Treat S4 forward as pre-registered from 2026-08-17. See [`regression-gate.md`](regression-gate.md#s4-re-baseline-00041--00025-2026-08-17--artifact-removal-not-decay). |
| `vol-book` | non-dir | event/0DTE | VOL-ONLY | Earnings IV-crush + 0DTE-VRP, net-of-cost. |
| `fundamentals-gate` | veto | — | risk filter | Finnhub = veto, not alpha (`research/80`). |
