# 30 — External Reality Check (Phase 3 checkpoint)

_Each surviving measured edge (+ the two structural negatives) stress-tested against published microstructure/anomalies literature and current-regime commentary. Goal: separate theory-grounded edges from in-sample flukes; flag confidence. Full agent output in `data/phase3_validations.json`._

## 3.0 The two best-supported conclusions are the NEGATIVES (they license the cuts)

### "Raw EOD options flow is beta, not alpha" — **STRONG support**
The Phase-2 finding (26/45 flow signals load as beta, sign-flipping selloff↔grind-up) is exactly what the literature predicts at this granularity:
- **Lakonishok-Lee-Pearson-Poteshman (2007)**: non-market-maker option activity is *overwhelmingly directional speculation*, not hedging → net buying pressure is a **leveraged long on the underlying** (and, in aggregate, on the market).
- **Ge-Lin-Pearson (2016)**: the dominant reason option volume predicts returns is the **embedded-leverage** (directional-bet) channel, not information.
- **Pan-Poteshman (2006)**: the *only* flow that predicts is **signed, opening-position, intraday, account-level** flow — precisely the granularity an EOD-aggregate panel destroys. Heuristically-signed daily aggregates collapse to contemporaneous/lagged beta.
- **McLean-Pontiff (2016)**: published predictors decay ~58% post-publication; widely-watched "smart-money flow" signals are exactly the kind arbitraged toward beta.
> **Verdict: near-zero standalone-alpha confidence in sweeps / whale-prints / net-premium / ask-imbalance / OI as measured.** This is the strongest external result in the study and it *directly authorizes* cutting the flow-scoring lines. The sign-flip across regimes is the smoking gun.

### "Dealer GEX/DEX condition volatility, not direction" — **STRONG support** (H4/H7/H8 ✓)
- **Barbon-Buraschi (2021, "Gamma Fragility")** + **Baltussen-Da-Lammers-Martens (2021, JFE)**: dealer gamma is a **second-moment** effect — short-gamma hedging amplifies realized vol and induces *intraday* momentum that **reverses by/after the close**. At a **daily** horizon, therefore, a DEX/gamma flip should be **mean-reverting (anti-predictive)** — exactly what Phase 2 measured (`DEX_FLIP_BEAR` −1.5%/h10). The directional **null** (GEX sign ⊥ signed return) is a clean, durable, mechanism-backed claim.
- **Dim-Eraker-Vilkov (2024)** + **Vilkov (2023/26)**: the 0DTE/VRP short-vol edge is *real but positive-mean / negatively-skewed and cost-and-tail-fragile* (H8 ✓).
> **Verdict: use GEX/DEX/0DTE as vol/structure/regime conditioners only — 0 directional points.** The practitioner "zero-gamma-flip predicts direction" (SqueezeMetrics/Karsan) claim has **no academic support** for signed-return prediction.

## 3.1 The directional survivors — confidence-graded

### S1 · 52-week-low relative-weakness short — **STRONG support; the one trustworthy directional edge**
- **Mechanism (triangulated):** George-Hwang (2004) 52-week-high **anchoring momentum** (the near-low = loser leg; underreaction to bad news that pushes price off the anchor) + Grinblatt-Han **disposition/capital-gains-overhang** + Da-Gurun-Warachka **frog-in-the-pan** (continuous low-salience info diffuses slowly).
- **Horizon match is textbook-perfect:** all three are *intermediate-horizon* (weeks-to-months) underreaction effects → an edge **absent at h≤5 and emerging at h10, strengthening at h21** is exactly right; at daily horizons the literature predicts the *opposite* (short-term reversal), so the h≤5 null is **confirmatory, not contradictory.**
- **The risks the in-sample window did NOT see:**
  1. **Momentum-crash regime** (Daniel-Moskowitz 2016): the near-low short leg has option-like negative beta and **crashes upward** in panic-state high-vol **V-rebounds / junk rallies / short-squeezes**. Our 3.5-month sample (steady selloff + grind-up + mild pullback) plausibly contains **none** of these → sign-stability here does **not** inoculate the tail. **The single biggest sizing caveat in the whole redesign.**
  2. **The short leg is the noisier half** (Lasfer-Ye 2024: the unconditional near-low effect is insignificant; the near-*high* long leg is the clean one).
  3. **Options-carry leakage:** near-low names carry rich put skew / elevated IV (crash + lottery premium), so part of the realized underperformance is **already priced into puts** — erodes the edge net of options carry.
> **Verdict: HIGH confidence in sign/mechanism/horizon → the redesign's anchor directional edge — but regime-gate it (stand down in post-selloff V-rebound / junk-rally / squeeze tape) and treat the short as the fragile leg.**

### S2 · Dark-pool one-sided concentration → mean-reversion — **MODERATE; re-spec required**
- The **directional half** is strongly grounded: uninformed one-sided liquidity demand → transient price pressure → reversal, **amplified in weak tapes** (Lehmann 1990; Campbell-Grossman-Wang 1993; Chordia-Subrahmanyam 2004; **Nagel 2012** — reversal returns *are* liquidity-provision returns and spike with VIX/turmoil → matches "strongest in weak tapes"). Dark-pool-specific: **Zhu 2014 / Comerton-Forde-Putnins** — dark venues disproportionately attract *uninformed* flow, so a 90%-one-sided dark print selects for non-informational pressure.
- **The NON-directional "both sides bounce up" headline is the fragile part** — *not* what a clean price-pressure model predicts. Most-likely benign explanation: reversal is **asymmetric/long-biased** (Lehmann: losers bounce more than winners fade) + the up-drift, so weak-tape conditioning makes the **sell-side (long) leg dominate** while the buy-side leg is near-noise. It **fails when the print is informed/news-driven.**
> **Verdict: MODERATE → trade as a DIRECTIONAL, long-tilted, news/earnings-gated short-horizon (3–5d) liquidity-provision reversal — not the non-directional "accumulation" headline.** A conditioning input, not a high-conviction line.

### S4 · PCR-high contrarian-long — **MIXED; LOW-to-MODERATE**
- Real mechanism for the contrarian-long: crash-insurance/variance-premium **overpricing** of puts (Garleanu-Pedersen-Poteshman 2009; Bollen-Whaley 2004) + short-term reversal + up-drift, at the h5–10 variance-unwind window.
- **But it directly contradicts the strongest single-name informedness results** (Pan-Poteshman: signed opening put buying predicts **down**-continuation; Xing-Zhang-Zhao smirk). Reconciliation: raw **unsigned EOD total-volume PCR** blends *informed* directional puts (continuation) with *hedging* puts (overpriced, no info); at h5–10 the hedging-overpricing channel dominates.
- **Contamination risks:** top-5% raw PCR over-samples **small/illiquid** names (bid-ask-bounce masquerading as edge); when put-heavy is **informed** (earnings/guidance) the fade gets run over.
> **Verdict: LOW-MODERATE → keep only with an option-liquidity floor + earnings exclusion; a small advisory fade, never a high-conviction line.**

### S5 · Put sweeps = contrarian-bullish (inverted) — **MIXED; LOW-to-MODERATE, confounded**
- "Puts ≠ bearish" is well-supported (Bollen-Whaley, GPP hedging demand; negative VRP makes the **put leg** lose — robust, horizon-insensitive). But the **inverted directional edge on the underlying** is contradicted by Pan-Poteshman (opening puts → down) and Chakravarty (sweeps are informed).
- **High confound:** put-sweep **notional $ scales with market cap** → "big put-sweep $" ≈ **megacaps**, the exact cohort that led this grind-up. Excess-vs-SPY does **not** strip a megacap-vs-rest tilt → the negative IC may be a **relabeled size/liquidity/recent-momentum factor**, not a put-flow edge.
> **Verdict: adopt only the SAFE half — "do not score put sweeps as bearish conviction" (well-supported) — and do NOT build a "fade put sweeps long" line (fragile, size-confounded).**

## 3.2 A cross-cutting honesty caveat (from the literature agents)
The A/B1/B2 "regimes" are **sub-windows of a single ~3.5-month episode**, not independent years. Sign-stability across them is **weaker evidence than cross-year robustness** — it rules out *local* beta but not *period-specific* factor exposure. Every confidence label above is therefore **conditional on 2026-H1-like conditions**; the redesign must say so and must keep the regime/crash guards that protect against the unsampled states (esp. S1's momentum-crash).

## 3.3 What Phase 3 changes vs Phase 2
| Edge | Phase-2 label | Phase-3 adjustment |
|---|---|---|
| Flow signals (26) = beta | BETA | **STRONG external confirm** → cut with confidence |
| GEX/DEX directional | anti/noise | **STRONG external confirm** → vol-only |
| S1 52w-low short | provisional | **upgraded grounding**, but **add momentum-crash regime gate** + treat short as fragile leg |
| S2 DP concentration | provisional (non-dir) | **re-spec to directional long-tilted, news-gated**; non-dir headline dropped |
| S4 PCR-high long | provisional | **downgrade to advisory** + liquidity floor + earnings exclusion |
| S5 put-sweep inverted | honorable mention | keep only the **"don't score puts as bearish"** half; drop the fade-long line |

## 3.4 Bridge to Phase 4
The evidence base now says the redesign's **highest-confidence content is subtractive** (stop paying for beta and anti-signals — STRONG-supported) and its **positive directional content is one theory-grounded, crash-guarded momentum-weakness edge (S1)** plus **modest, heavily-conditioned mean-reversion/contrarian inputs (S2/S4)** and a **validated non-directional vol book** (earnings IV-crush / 0DTE-VRP). Design accordingly: a lean, regime-first workflow that is honest that most days have **no directional edge**, sizes the few real ones for their documented tail risks, and never dresses beta as conviction.
