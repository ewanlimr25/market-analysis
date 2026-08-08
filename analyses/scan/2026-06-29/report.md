# Market Scan — 2026-06-29

> Live post-market scan (fresh 2026-06-29 panel export, 20:08 EDT). Scoring currency = **excess-vs-SPY (conditional)**, never raw win-rate. Regime is path-aware (Yahoo chart API + live `uw` 06-29), **not** the stale harness fallback (see note).

## Regime & Verdict
- **Regime: PULLBACK_IN_UPTREND / TRANSITIONAL** · SPY 741 (below 20dma 742.83, above 50dma 735.14; −2.55% from 90d high) · ret5 −0.46% · ret10 −0.10% · **breadth weak/divergent (37.9% bullish flow; 3879 bearish vs 2366 bullish tickers on an up-day)**.
- **Today = sharp V-rebound:** SPY **+1.65%**, QQQ **+2.49%** off a 2–4% multi-day dip; VIX **17.65, −4.1% today / −20.6% off its 15d high (22.2)**.
- **vol-state** (2nd-moment, NOT a direction): VIX falling but dealers **NET SHORT GAMMA** (SPY GEX negative, spot 740.7 < ZGL 764.2 → hedging amplifies moves); front-end **BACKWARDATION 1.12**; term-skew **TAIL_HEDGING**. Normalizing, not complacent.
- `directional_tradable: true` (**half-cap** — TRANSITIONAL + weak breadth) · `s1_standdown: **true**` (live overlay).

> **⚠ Harness/truth-set staleness (important):** `retro_harness.py --date 2026-06-29` returns `CHOP, ret5 −2.38%, s1_standdown False` — but `data/{returns,prices,features}.parquet` max out at **2026-06-26**, so the harness silently falls back to the 06-26 regime. It **cannot classify 06-29** until the truth-set is rebuilt. The numbers above are the **live path-aware read** and are authoritative for this scan. (Lane *priors* are cross-year backtested constants and remain valid.)

- **Bottom line:** Low-conviction tape. The one robust directional lane (**OI-fade short**) is live and regime-appropriate, but today's V-rebound + short-gamma make fresh shorts timing-risky → **3 starter/half OI-fade shorts after correlation collapse**, sized for the squeeze tail. **`s1_standdown` suppresses the entire MOM_SHORT leg** (the V-rebound off a dip is the momentum-crash trap). MOM_LONG is basket-WATCH only. **The actionable book today is the VOL BOOK** (a genuinely rich early-July earnings IV-crush menu) — the modal "thin directional edge, here's the vol book + watch list" output.

## Directional Book (excess-scored)
| Ticker | Lane | Dir | H | validated_excess | regime_fit | size | tier | gates |
|---|---|---|---|---|---|---|---|---|
| AMZN | OI_FADE | short | 10 | +0.0088 (hit−base +0.205, n=640) | 1.0 | **half** | MEDIUM | mega-cap-internet cluster (AMZN/GOOGL/META) → sized once; +111k/+7.9% 5d call-OI build; ER 07-30 outside h10; fund CAUTION |
| IBM | OI_FADE | short | 10 | +0.0088 | 1.0 | starter | MEDIUM | single (legacy-tech, uncorrelated); heaviest *relative* build +22.6%; ER 07-22 outside h10 |
| DVN | OI_FADE | short | 10 | +0.0088 | 1.0 | starter | MEDIUM | single (energy, sector-diversifying); build +11.3%; ER 08-04 outside h10 |

**Why these three and not the other ~17 OI-fade fires** (the discipline):
- **No additive confluence** — each scores on the OI-fade lane alone. **CRM dropped:** OI_FADE-short (+53.6k build) **AND** S2_dp_revert-long (DP SELL-heavy 0.034 extreme) → lanes conflict, they don't net.
- **Correlation-cluster collapse (corr ≥ 0.70 = one position):** mega-cap-internet (AMZN/GOOGL/META) → 1 (AMZN rep); crypto-proxy (MSTR/BMNR/MARA) → 1 (watch). Picked uncorrelated singles (IBM legacy-tech, DVN energy) for breadth.
- **Live V-rebound overlay → squeeze-prone OI-fade names deferred:** MSTR/BMNR/MARA are heavy call-OI builds **but near 52w-low + crypto-reflexive** = exactly what squeezes on a V-rebound day → **WATCH, not sized**. Sized names are mid-range pct52 (AMZN 0.54, IBM 0.55, DVN 0.50), not squeeze-from-the-lows.
- **Nice structural property:** short crowded-call mega-caps (AMZN) + WATCH long new-high semis (MOM_LONG basket) ≈ a roughly tech-neutral relative-value posture, which suits a no-clear-direction TRANSITIONAL tape.
- **Half-cap, no auto-full** (invariant #4): nothing sizes full; caps at MEDIUM.

## Vol Book (non-directional) — *the meat today*
Delta-neutral, quoted **net-of-cost**, 0 directional points. A real early-July earnings cluster (not the pre-season quiet I expected):
| Symbol | ER | iv_rank | implied move | note |
|---|---|---|---|---|
| **NKE** | 06-30 PM | 81 | ~8% | most liquid ($992M ADV); short strangle/condor, harvest crush if realized < implied |
| **STZ** | 06-30 PM | 64 | ~5% | defined-risk condor |
| **FDS** | 07-01 AM | **91** | ~10% | richest IV-rank of the liquid menu |
| **PEP** | 07-09 AM | 75 | ~2% | liquid large-cap; tight condor |
| **PENG** | 07-07 PM | **97** | ~23% | richest IV but wide move + small-cap gap risk → **minimal, defined-risk only** |

- **0DTE-VRP: STAND ASIDE this week.** Dealers **short gamma** (below ZGL 764) → realized can spike and hedging amplifies moves; **NFP 07-02 + Jul-3 holiday** thin tape add gap risk → premium-selling is negative/too-risky net-of-cost. Favor the defined earnings IV-crush plays instead.

## Watch / Stood-down
- **STOOD DOWN — MOM_SHORT cohort** (`s1_standdown=true`): near-52w-low names NOG / CPRT / TU / INGR / CME / ICE / T / TMUS / CTSH / NDAQ / BSX / ROL / HLI / SSNC. **Entire S1 short leg suppressed** on the live V-rebound. regime_fit 0 today.
- **WATCH — OI-fade clustered/deferred:** GOOGL, META (via AMZN cluster); MSTR/BMNR/MARA (crypto squeeze tail).
- **WATCH — MOM_LONG basket** (tail-driven, median ≈ 0, hit−base −0.093; **basket only, never per-name**): semis AMAT / GLW / PANW / ALAB / ACMR / UCTT / ICHR / OUST / ALGM (+ AIP) and biotech RVMD / CYTK / LGND / HNGE. regime_fit 0.5 into a weak-breadth bounce. **Heavy semis correlation** — would collapse to ~1 position if sized.
- **ADVISORY (never sized) — S2_dp_revert longs:** DLTR (DP BUY 0.985), SHW (0.979), BRKB (0.922), CSCO (0.982) — extreme one-sided DP liquidity events, news-gated reversion (+0.47%, h3–5).
- **ADVISORY — S4_pcr_fade longs:** ACN, CTSH (high PCR). Extreme-PCR outliers (PCVX 406, MDLN 38, VIK 36) **excluded as 1-day artifacts** (the reason `put-call-extremes` was deprecated for z-score). Never sized.
- **DROP:** CRM (lane conflict). CTSH also sits in *both* the stood-down MOM_SHORT cohort and the S4 advisory list → conflicting orthogonal signals → no action.

## Risk
- **Correlation clusters are load-bearing:** ~20 raw OI-fade fires + the whole MOM_SHORT/MOM_LONG screens collapse to **3 sized, uncorrelated shorts** (mega-cap-internet / legacy-tech / energy). Without collapse the book is one levered "mega-cap + crypto down" bet.
- **Event calendar (in-horizon):** **June NFP ~07-02** (Tier-1, inside all horizons), **US market holiday 07-03** (thin liquidity), CPI + Q2 banks ~07-14 (just past h10). All sized names' earnings are outside h10 (verified: 07-22 to 08-04).
- **Tail caps applied:** AMZN half (mega-cap squeeze tail + live V-rebound); IBM/DVN starter; vol-shorts sized for the unsampled left tail and quoted net-of-cost; 0DTE-VRP stood aside under short-gamma.
- **Fundamentals gate:** marked CAUTION on the sized shorts (AMZN/IBM/DVN are fundamentally sound → fades are *tactical*, not fundamental shorts) → reinforces starter/half. *(Live `fundamentals-gate` agent not separately run — subagent tool-execution was intermittently blacked out this session; the directional book is baskets/starters, not single high-conviction sizes, so the veto channel is advisory-pending, not load-bearing here.)*
- **Hedge note:** book is net-short into a fresh +1.65% V-rebound with dealers short-gamma (up-moves amplified) → the risk is a continuation squeeze. Half/starter sizing + the squeeze-prone-name deferral + h10 horizon are the hedges; invalidations are the per-name OI-build reversals / breakout reclaims.

---
*Generated by `/market-scan` (live). Lanes computed inline via the same DuckDB screener / dark-pool / OI queries the `retro_harness` reference uses (subagent layer was unreliable this session; ran direct). Outcomes unresolved — `/calibration-audit` grades forward excess per lane per regime after the truth-set rebuild past 06-29. No lane/threshold changed this run → regression gate not triggered. Envelope: `decision.json` (v2, schema-valid).*
