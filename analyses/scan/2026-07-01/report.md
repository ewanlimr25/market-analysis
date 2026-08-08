# Market Scan — 2026-07-01

## Regime & Verdict
- **Regime:** `CHOP/REBOUND-THRUST` · vol-state: VIX 16.6 (−11% wk), **VRP NEGATIVE** (SPY IV30 13.9 < RV 15.4; QQQ 24.6 < RV 28.9), SPY **short-gamma** near spot (moves amplified, not range-bound), term FLAT, 1y skew TAIL_HEDGING · breadth **37% bullish** (soft) · `directional_tradable = FALSE` · `s1_standdown = TRUE`
- **Bottom line:** **No directional edge sized for entry today.** Modal regime + stand-down vol + watch list into a holiday-shifted NFP and a 3-day weekend. Reassess the full book **Mon 2026-07-06** post-NFP.

Regime is **live-Yahoo authoritative** — the truth-set parquet is stale at 2026-06-26, so `retro_harness --date` falls back to a stale regime and is NOT used. `s1_standdown` fires cleanly: ret5 **+1.71%**, drawdown15 **−3.32%** (the 06-26 dip → +2.4% V-rebound 06-29/30 → mild fade today is the exact momentum-crash/V-rebound shape). uw market-regime = TRANSITIONAL / half sizes; its "iron condors in range" tag is **overridden** by negative VRP + short-gamma.

## Directional Book (excess-scored)
*Empty for entry — every expression is WATCH / STOOD_DOWN / advisory. This is the correct modal output.*

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| NVDA | OI_FADE | short | h10 | +0.88% (lane prior) | 0.35 | **watch** | insider buying / AI catalyst breakout | fund **CONFIRM**; isolate (not cluster); defined-risk puts only; post-NFP 07-06 earliest |
| AMZN | OI_FADE | short | h10 | +0.88% (lane prior) | 0.20 | **watch** | it's a QQQ-beta short; do not size | cluster→**1 QQQ-beta** (corr −0.64 w/ SPY; mega-heavy-day excess **−0.43%**); NFLX ER inside h10 |
| CG | OI_FADE | short | h10 | +0.88% (lane prior) | 0.20 | **watch** | confirmed M&A behind the build | **4.24× rel-build** but near-52w-low + "Very Group up for sale" → do NOT fade a takeover |
| CEG | MOM_SHORT | short | h10 | +0.81% (lane prior) | 0.00 | **skip** | n/a — leg suppressed | **STOOD DOWN** (s1_standdown); cohort rep (CEG/T/ACM/NOG/OLED/GPI…) |
| CNC | MOM_LONG | long | h10 | +2.35% (tail-driven) | 0.30 | **watch** | breadth stays narrow / risk-off | fund **CONFIRM**; healthcare cluster = 1 position; basket-only, hit<base |
| HUM | MOM_LONG | long | h10 | +2.35% (tail-driven) | 0.30 | **watch** | loses breakout | fund **CONFIRM**; same healthcare cluster (noted, not summed) |
| BKNG | S2_dp_revert | long | h5 | +0.47% | 0.50 | **watch** | concentration not repeated / news | ADVISORY; DP buy-heavy 90%; below sizing bar |
| DLR | S4_pcr_fade | long | h5 | +0.71% | 0.40 | **watch** | put crowd informed (gap down) | ADVISORY; cleanest liquid high-PCR (ETFs are artifacts) |

**Why nothing sizes (the two arguable calls, pressure-tested by an adversarial fleet):**
- **OI_FADE mega-tech short — refuted as sizeable.** The single most robust lane historically, but today's top `oi_net_5d` names are all mega-caps whose **relative** build is weak (0.13–0.27× their own 30d-avg call OI; only CG at 4.24× is extreme, and CG is a do-not-fade takeover). By the corr≥0.70 gate the cluster collapses to **one QQQ-beta short**: an empirical panel test found the short-leg-only basket has **corr −0.64 with SPY forward return** (+4.2% on down days, **−1.3% on up days**), and on **mega-cap-heavy days (today's exact composition) historical short-excess was NEGATIVE (−0.43%)**. The real edge is a *beta-neutral* long-low-OI / short-high-OI dispersion spread — the naked high-OI leg is structural beta, the exact failure mode the redesign forbids. Only NVDA survives as an *idiosyncratic* sliver (froth + insider MSPR −100), and even that is event-blocked this week.
- **MOM_LONG near-52w-high basket — real factor, wrong regime.** Tail-driven (hit **0.50 < 0.59 base**, median ~0); the tail needs a **trending, broad-participation** tape. Today is the opposite — CHOP/REBOUND-THRUST, narrow 37% breadth, tech rolling over, TRANSITIONAL half-size — and 7/20 names are one healthcare cluster, breaking the diversification the edge requires. WATCH; CNC/HUM are the fundamentally-confirmed subset to revisit if the tape turns trending.

## Vol Book (non-directional)
**STAND DOWN — no delta-neutral edge clears net-of-cost.**
- **0DTE-VRP / index premium-sell:** actively **adverse**, not merely un-edged — negative VRP means you collect less than the tape moves before cost, and short-gamma amplifies/trends rather than ranges (breaks the condor assumption). NFP Thu + closed Fri add an unmanageable 3-day gap. The uw "iron condors in range" heuristic is overridden.
- **Earnings IV-crush:** no fuel — only thin **PENG** (07-07, IV-rank 98 but 23.7% implied-move small-cap gap), **AZZ** (07-08), **PEP** (07-09, tiny 1.1% move). Pre-earnings-season lull + holiday-thinned liquidity → below the net-of-cost bar. Stand aside.
- **Long vol:** off-mandate and penalized by long-weekend theta (closed Fri + weekend decay, MMs mark holiday vol down) — "cheap" IV still bleeds.

## Watch / Stood-down
- **OI_FADE dispersion factor** — the *real* edge is beta-neutral long-low-OI / short-high-OI (within-mega-cap rank-IC −0.178, t=−6.7). Track it; only expressible as a spread, never a naked high-OI-leg short. Re-check post-NFP.
- **NVDA (standalone)** — most robust idiosyncratic fade; if ever taken, defined-risk long puts, token quarter (≤0.2× half-cap), **Mon 07-06 earliest**, cut on insider-buying / real-catalyst breakout.
- **CNC / HUM** — MOM_LONG healthcare subset, fundamentals CONFIRM, sector inflow today; ERs 07-28/29 just beyond h10. Only post-holiday token candidate if the tape turns trending/broad.
- **CG** — extreme relative call-build but M&A-speculation near 52w-low → do NOT fade; needs a news gate.
- **PFE** — heavy call-OI build but fundamentals **CAUTION/VETO** the short (GLP-1 Medicare-coverage tailwind + insider buying); build may be legit.
- **China sleeve {BABA, KWEB, EWZ}** — separate idiosyncratic OI-fade beta from mega-tech; watch, unsized.
- **MOM_SHORT cohort (stood down)** — CEG/T/ACM/NOG/OLED/GPI/BCE/RAM/STWD (defensive/rate-sensitive; TIPS-ETF pct52 artifacts excluded).
- **S2 (BKNG/MRNA/WING/YUM)** and **S4 (put-heavy crowd)** — advisory only, below the sizing bar.

## Risk
- **Dominant risk is EVENT/GAP, not signal.** NFP holiday-shifted to **Thu 07-02 08:30** (likely early close) sits inside every horizon, then **NYSE closed Fri 07-03** → a binary Tier-1 macro gap that cannot be managed for a 3-day weekend.
- **Short-gamma** (negative near-spot GEX) = amplified, trend-following moves — hostile to both fades and premium-selling.
- **s1_standdown = TRUE** → all momentum shorts off, sizing capped. Breadth narrow (37%), tech rolling over (QQQ −1.52%, −$484M out), thin holiday liquidity = whippy fills / wider gaps.
- **Correlation clusters collapsed:** mega-tech OI-fade → 1 QQQ-beta (do not size); healthcare MOM_LONG → 1 position. **No additive confluence** — orthogonal agreement (tech outflow + QQQ fade + soft breadth corroborating an OI short) is *noted, never summed*.
- **Discipline:** enter nothing directional into the print/weekend. If any single expression is ever taken it is **defined-risk long premium only** (negative VRP makes owning convexity relatively cheap; never sell gamma here), token quarter, well inside the half-cap ceiling. Re-run the book **Mon 2026-07-06** on live data.

---
*Method note: UW panel export for 2026-07-01 is fresh across all five groups. All lane signals computed live (replicating `retro_harness.fire()` thresholds; `oi_net_5d` recomputed from the OI-changes panel since `features.parquet` is stale at 06-26). Regime from live Yahoo SPY (chart API, path-aware). Two arguable directional expressions pressure-tested by a 7-agent adversarial fleet (4 skeptic lenses → bull/bear → independent judge); all converged on WATCH/0.*
