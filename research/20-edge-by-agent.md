# 20 — Edge by Source / Agent / Rubric Line (Phase 2 checkpoint)

_Six parallel per-source agents extracted 45 raw signal variants and measured each against the shared, look-ahead-safe, conditional-benchmark truth set. Outcome resolution was identical across sources (shared `edge.py`). This is the keystone evidence base for the redesign._

## 2.0 Headline (the number that drives everything)
**Of 45 measured signal variants: 26 BETA · 7 NEGATIVE · 4 NOISE · 3 VOL-ONLY · 1 INCONCLUSIVE · 4 EDGE_PROVISIONAL · 0 EDGE_DURABLE.**

On this panel, **raw options-microstructure flow carries almost no durable directional alpha.** The dominant failure mode is identical in all six sources: a signal shows a *positive mean excess* that is a **right-skew illusion** — its **median excess is negative, its hit-rate sits below the (long-biased) SPY base, its IC is ~0 or negative, and its sign flips across the A/B1/B2 regimes.** It is market-direction exposure (beta) dressed as conviction. The signals the current rubric weights **most heavily** are precisely the ones that fail:

| Rubric line (weight) | Measured verdict |
|---|---|
| **+3** accumulation conjunction (DP block + OI + cum-flow) | **BETA** — DP block-accum & OI-build both beta; block-stratification only nudges IC 0.031→0.042 |
| **+2** multileg directional | **NOISE** — `MULTILEG_HEAVY` no forward edge in either direction |
| **+1** mechanized DEX flip | **ANTI-PREDICTIVE** — flips mean-revert: `DEX_FLIP_BEAR` −1.5% @h10, p=0.003, n=277 |
| **+1** multi-day OI build | **BETA** |
| **+1** cum-premium-flow accretion | **BETA** (`NET_PREM_BULL/BEAR`) |
| **+1** earnings BUY/SELL VOL | **VOL-ONLY** (real, but non-directional) |
| **−2** crowded-long continuation | **mis-specified** — the *opposite* asymmetry is what's real (see PCR below) |

> Honest scope caveat (carried into every downstream claim): 54 EOD sessions, daily horizons, a net-up tape whose single biggest move (April +12.8%) is unsampled. This says **"no durable directional alpha is detectable at EOD-aggregate / daily-horizon granularity on this panel,"** not that flow is universally worthless. It is, however, more than enough to stop paying conviction points for beta.

## 2.1 The four survivors (the entire re-derivable edge set)
All are **PROVISIONAL** (real sign-stability, but N/horizon caveats). None is a microstructure "smart-money" story — they are mean-reversion, momentum, and sentiment-contrarian.

| # | Signal | Source | Dir | Best line | Why it's edge not beta |
|---|---|---|---|---|---|
| **S1** | **NEAR_52W_LOW** (relative-weakness continuation) | screener | short | h=10 n=1894 mean_exc **+0.0092** hit 0.554 base 0.344 **hxb +0.21** p~0 (h=21 +0.027) | **Sign-stable across selloff AND grind-up** — the short beats SPY *even in the up-tape* (B1 h10 +0.0064). Genuine relative-weakness continuation, not short-beta. **Strongest directional edge found.** Gated to h≥10 (nothing at h≤5). |
| **S2** | **DP_ONESIDED_CONCENTRATION** (≥90% of DP $ on one side, clean prints) | dark pool | *non-dir* | h=5 n=795 mean_exc **+0.0099** hit 0.55 base 0.41 **hxb +0.143** p~0 | Positive in **all 3 regimes**, strongest in weak tapes; a one-sided liquidity **event** marks a 3–5d mean-reversion bounce. **NON-directional** — the sell-side mirror works identically (it is *not* "accumulation"). IC~0 ⇒ a binary regime tag, not a magnitude signal. Decays by h=10. |
| **S3** | **DP_BUYRATIO_EXTREME** (buy-side cut of S2) | dark pool | long | h=5 n=391(clean) mean_exc +0.0096 hxb +0.077 p=0.005 | Same edge as S2, buy-side slice. Provisional; essentially redundant with S2. |
| **S4** | **PCR_HIGH_LONG** (fade the put-heavy/bearish crowd) | screener | long | h=5 n=1138 mean_exc **+0.0059** hxb +0.00 ic +0.02 p=0.004 | Sign-stable positive across all 3 regimes incl. selloff (beats SPY even in down-tape ⇒ contrarian mean-reversion, not beta). Small (+0.5–1% h5–10); edge lives in mean_exc, not win-rate. |

**Honorable mention / inverted signal — S5: `SWEEP_PUT_250K` is a regime-stable CONTRARIAN-BULLISH tell.** Aggressive put sweeps consistently precede relative **out**performance (short verdict NEGATIVE, p≤0.000 @h10/h21, **negative IC** — more put-sweep premium ⇒ more outperformance), *even in the March selloff*. Put sweeps are hedging/financing flow, not bearish conviction. The current `sweep-tracker` scores these as short conviction — **exactly backwards.**

## 2.2 Hypothesis scorecard (Phase 0 → Phase 2)
| H | Claim | Verdict | Evidence |
|---|---|---|---|
| H1 | Single-leg opening-put is the strong under-weighted edge | **REFUTED** | All put tiers (PRIME/FLOOR/WHALE/1M/OTM) BETA/INCONCLUSIVE; pooled hit 0.55 < base 0.68. "+22pp" was unconditional-benchmark selection (→ `12-benchmark-inconsistency.md`). Bigger whales were *worse* (1M tier hxb −0.21). Pan-Poteshman did **not** replicate (opening calls also beta). |
| H2 | DP accumulation works as a conjunction | **REFUTED (re-framed)** | Block-stratification is beta; the real DP edge (S2) is **non-directional one-sided-concentration mean-reversion**, not accumulation. |
| H3 | cum-premium-flow is NO-INFO standalone | **CONFIRMED** | NET_PREM_BULL/BEAR BETA. |
| H4 | DEX/vanna flips have ~0 swing edge | **CONFIRMED & WORSE** | Mechanized DEX flip is **anti-predictive** (flips mean-revert; Baltussen 2021 vindicated). |
| H5 | Sweeps/persistence are noise-to-negative | **CONFIRMED** | SWEEP_CALL beta, SWEEP_RATIO_HIGH negative, sweep-persistence already removed. (Put sweeps = contrarian, S5.) |
| H6 | conviction-matrix DIRECTIONAL_LONG is a fade ex-LEAP | untested directly | LEAP OI builds all beta; consistent. |
| H7 | GEX conditions vol not direction | **CONFIRMED** | GEX sign doesn't predict signed excess; the "neg-gamma=narrower range" headline is an **ETF-vs-stock composition artifact** (vanishes within-name). |
| H8 | 0DTE VRP real but thin net-of-cost | supported | IV_RANK/IV_CRUSH = VOL-ONLY real edges; matches the repo's own validated zerodte stack. |
| H9 | The 11–12 agent fleet is heavily redundant | **CONFIRMED (strongly)** | 4 flow sources (DP/OI/flow/hotchains) all read the same correlated tape and all return BETA. The 6 sources collapse to ~3 orthogonal edges, only one of which (52w-low) is a flow-independent price signal. |
| H10 | Regime stratification is decisive | **CONFIRMED** | Nearly every "edge" was B1-grind-up beta that flipped sign in A/B2. Sign-stability-across-regimes is the only durability test that mattered. |

## 2.3 Per-rubric-line grading (the frozen `2026-06-12` rubric, graded against outcomes)
| Line | Frozen weight | Measured | Recommendation (Phase 4) |
|---|---|---|---|
| accumulation conjunction | +3 | BETA (directional); S2 is non-dir mean-rev | **Strip the +3.** Re-spec DP as a non-directional short-horizon mean-reversion tag (S2), 0 conviction points. |
| multileg directional | +2 | NOISE | **Cut to 0.** The 2nd-heaviest line is unearned. |
| mechanized DEX flip | +1 | ANTI-PREDICTIVE | **Cut to 0** (or invert as a weak mean-reversion input). Never a long-direction point. |
| multi-day OI build | +1 | BETA | **Cut to 0.** |
| conviction-matrix (LEAP) | +1 | beta (LEAP OI all beta) | **Cut / advisory only.** |
| cum-premium-flow accretion | +1 | BETA | **Cut to 0**; retain only as a liquidity/screen, never a point. |
| sector-rotation leader | +1 | untested (GICS sector flow not yet measured) | **Demote to advisory**; pre-register a sector-flow excess test. |
| earnings BUY/SELL VOL | +1 | VOL-ONLY (real) | **Keep — but as a non-directional vol line** benchmarked vs implied move, not a directional point. |
| vol-surface KINKED/BACKW. | +1 | VOL-ONLY | **Keep as vol context.** |
| crowded-long continuation | −2 | mis-specified | **Re-spec:** the supported effect is *fade the put-heavy crowd long* (S4, +1), and *don't short the call-heavy crowd* (PCR_LOW_SHORT NEGATIVE). |
| flow_conflict −3/−1 | gate | penalizes on cum-flow (a beta axis) | **Reconsider** — deducting on a non-informative axis taxes trades for noise. |
| 52-week-low weakness | (none) | **S1 — strongest edge, unscored** | **ADD** a relative-weakness continuation short line (h≥10). |

## 2.4 Per-fleet-agent grading (keep / cut / repurpose)
| Agent | Carried edge? | Action |
|---|---|---|
| `dealer-positioning-strategist` (DEX/vanna swing) | **No — anti-signal** | **CUT.** Its entire output (DEX level beta, DEX flip anti-predictive) is worse than noise. |
| `gamma-flip-tracker` (0DTE GEX) | No directional value | **Demote to vol/structure context** feeding the (separately validated) 0DTE premium-selling stack only. 0 directional points. |
| `multileg-strategist` | **No — noise** | **CUT** (carries the unearned +2). |
| `leap-positioning-radar` | No (LEAP OI beta; 90D unverifiable here) | **CUT / advisory.** |
| `accumulation-hunter` | Only as non-dir mean-reversion (S2) | **REPURPOSE** → DP one-sided-concentration **mean-reversion** tag (short-horizon, weak-tape), not "accumulation." |
| `sweep-tracker` | Inverted (S5) | **REPURPOSE** → put sweeps are a **contrarian/relative-strength** tell; never score sweeps as conviction. |
| `contrarian-scanner` | **Yes (S4)** | **KEEP**, narrowed to the validated fade (long into put-heavy crowd). |
| `earnings-scout` | Vol-only (real) | **KEEP** as non-directional vol. |
| `vol-surface-scout` | Vol-only | **KEEP** as vol. |
| `sector-rotation-strategist` | untested | **TEST then decide**; demote meanwhile. |
| `opex-pin-strategist` | untested (conditional) | Keep conditional/advisory. |
| `risk-monitor` | n/a (gating) | **KEEP** — regime/correlation gating is the right discipline and *more* important under a beta-heavy tape. |
| `fundamentals-gate` | n/a (veto) | **KEEP** (cheap veto on the few names actually sized). |
| `bull/bear debate` | n/a | **KEEP but shrink** — with fewer scored names, debate only the 1–2 real-edge names. |
| **(missing)** relative-strength / momentum | **S1 lives here, unowned** | **ADD** a momentum/relative-weakness lane. |

## 2.5 Reconciliation with `/calibration-audit` (independent vs audit)
- **Agree:** tier inversion / out-of-regime fragility (H10); DEX demotion (we go further — *invert*); sweep-persistence removal; cum-flow NO-INFO; the beta/excess problem (their C21 is the right benchmark).
- **Disagree (we go further):**
  1. The audit still treats **accumulation +3 as LOAD-BEARING** (+27.8pp in one cycle). Our regime-stratified, conditional-benchmark measurement says it is **beta** (sign-flips A/B1/B2; the +27.8pp was a single-window grind-up artifact). 
  2. The audit keeps **multileg +2 as earned**; we measure it **NOISE**.
  3. The audit runs a **C19 promotion path for the single-leg put** on the inflated unconditional-benchmark +22pp; we show that path rests on a **selection artifact** and should be closed, not promoted.
- Root cause of the disagreements: the audit graded one (mostly grind-up) window at a time and pooled regimes; the freeze stopped the *whipsaw* but kept the *over-weighted correlated lines* that a cross-regime split exposes as beta.

## 2.6 Multiple-testing & durability discipline
~45 signals × 5 horizons ≈ 225 tests. Under BH (FDR 0.10) the two p~0 survivors (S1 n=1894, S2 n=795) clear comfortably; S3 (p=0.005) and S4 (p=0.004) clear but are nearer the margin. **The primary durability evidence is sign-stability across the 3 regimes, which a single p-value cannot fake** — S1 and S4 beat SPY *in the up-tape* (the hardest test for a short / a fade). Everything labeled BETA failed precisely this test.

## 2.7 Bridge to Phase 4
The redesign is not a re-weighting — it is a **reduction**: from a 12-agent additive-confluence machine that mostly scores beta, to a small set of **orthogonal, excess-validated, regime-conditioned** signals (S1 momentum-weakness short, S2 DP-concentration mean-reversion, S4 PCR-high fade, S5 put-sweep-as-RS), an explicit **non-directional vol book** (earnings/IV/0DTE-VRP), and an honest **regime + beta** acknowledgment, with the surviving gates (`risk-monitor`, `fundamentals-gate`) kept. Phase 3 next: external-literature validation of the four survivors and of *why* the flow signals are beta.
