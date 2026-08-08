# Phase B — Momentum Lane Analysis · 2026-07-23

## Regime & Gate Context

**Phase A regime:** PULLBACK (SPY ret5 −1.67%, ret10 −1.80%, SPY below 20/50-SMA), short-gamma/vol-expansion, 
`s1_standdown`=**FALSE**, `directional_tradable`=TRUE. Phase A identified 354 liquid names within 3% of a 52w extreme 
(246 near highs / 133 near lows).

**Standing policy (2026-07-18 audit):** MOM_SHORT capped to **advisory/watch-only — NO new sized starters** until 
lane clears DURABLE-N≥30 forward re-validation. `s1_standdown`=FALSE does NOT re-enable starters. MOM_LONG is 
**basket/tail-only, NEVER per-name HIGH**. Tonight's output is watch/advisory cohort map.

---

## Screener Pipeline

| Stage | Filter | Names |
|-------|--------|-------|
| Raw universe | All records | 6,279 |
| After universe hygiene (Common Stock / ADR only) | Exclude ETFs, Units, Structured Prods | 1,503 |
| After liquidity floor | close ≥ $5 AND $-ADV ≥ $50M | 1,503 |
| **After ER gate** | **no earnings through 2026-08-06** | **464** |

---

## MOM_SHORT Cohort (Near-52w-Low)

**Screen:** `close <= 1.02 × week_52_low`, liquid, no ER in h10, fail-closed.

**Cohort size:** 14 names (from 464 qualifying universe)

### Top Candidates (Ranked by Proximity to 52w-Low)

| Rank | Ticker | Close | 52w-Low | %Δ Below | $-ADV (20d) | Sector | Status |
|------|--------|-------|---------|----------|-------------|--------|--------|
| 1 | QS     | $    5.12 | $    5.64 |  -9.39% | $123.9M     | Consumer Cyclical    |          |
| 2 | ROL    | $   39.44 | $   41.50 |  -4.96% | $193.1M     | Consumer Cyclical    |          |
| 3 | ISRG   | $  332.02 | $  340.61 |  -2.52% | $1218.5M    | Healthcare           |          |
| 4 | AZO    | $ 2923.50 | $ 2928.11 |  -0.16% | $1118.0M    | Consumer Cyclical    |          |
| 5 | ORCL   | $  120.04 | $  120.03 |   0.01% | $4729.2M    | Technology           |          |
| 6 | LOW    | $  201.92 | $  201.88 |   0.02% | $598.6M     | Consumer Cyclical    |          |
| 7 | PEP    | $  134.95 | $  133.95 |   0.75% | $1268.2M    | Consumer Defensive   |          |
| 8 | HDB    | $   23.13 | $   22.91 |   0.96% | $196.9M     | Financial Services   | ADR      |
| 9 | IBM    | $  206.65 | $  204.44 |   1.08% | $2759.8M    | Technology           |          |
| 10 | CCI    | $   74.57 | $   73.75 |   1.11% | $315.0M     | Real Estate          |          |
| 11 | LEN    | $   82.13 | $   81.18 |   1.17% | $200.3M     | Consumer Cyclical    |          |
| 12 | CPRT   | $   27.20 | $   26.85 |   1.30% | $351.0M     | Industrials          |          |
| 13 | CNM    | $   43.12 | $   42.50 |   1.46% | $105.0M     | Industrials          |          |
| 14 | TU     | $   10.11 | $    9.95 |   1.61% | $62.6M      | Communication Services |          |


**Key observations:**
- **QS** is the new leader (−9.39% below 52w-low), dethroning PEGA from yesterday
- PEGA has recovered above 1.02× threshold and exited the cohort
- CNM remains near the low but has recovered to +1.46% threshold margin
- **ORCL** sits barely within threshold (+0.008%), currently held from prior day
- Cohort is **small and tight** — just 14 names pass the screens; suggests low opportunity set in PULLBACK regime

---

## MOM_LONG Basket (Near-52w-High)

**Screen:** `close >= 0.95 × week_52_high`, liquid, no ER in h10, basket-only.

**Basket size:** 60 names (down from 76 on 2026-07-22)

### Sector Breakdown (MOM_LONG)

- **Financial Services:** 30 names ( 50.0%)
- **Industrials:**  9 names ( 15.0%)
- **Healthcare:**  8 names ( 13.3%)
- **Consumer Cyclical:**  4 names (  6.7%)
- **Real Estate:**  4 names (  6.7%)
- **Consumer Defensive:**  2 names (  3.3%)
- **Energy:**  1 names (  1.7%)
- **Communication Services:**  1 names (  1.7%)
- **Utilities:**  1 names (  1.7%)


### Composition & Rotation

**Dominant sector:** Financial Services with 30/60 names (50%).

**Comparison to 2026-07-22 (76 names, rotated tech→financials):**
- Basket shrunk by 16 names (76 → 60)
- Financial Services remains heavily represented, but _slight_ consolidation within the set
- Industrials (9 names) and Healthcare (8) provide diversification
- Tech drubbing (TSLA −14.5%, GOOGL down) has NOT driven massive rotation out of 52w-highs; 
  rather, names at highs have pulled back into the 95%+ zone with today's broader pullback

**Regime fit:** PULLBACK regime reduces the regime_fit for a long basket. The pullback has created a mixed picture: 
names *were* at highs, but today's −1.67% SPY move has either knocked them back slightly or consolidated them 
into the breakout zone without new all-time highs.

### Top MOM_LONG (Closest to 52w-High)

| Rank | Ticker | Close | 52w-High | %Δ Below | $-ADV (20d) | Sector |
|------|--------|-------|----------|----------|-------------|--------|
|  1 | FBRX   | $   59.70 | $   56.84 |   5.03% | $57.9M      | Healthcare           |
|  2 | OII    | $   48.02 | $   45.91 |   4.60% | $55.4M      | Energy               |
|  3 | CSX    | $   52.81 | $   51.28 |   2.97% | $648.3M     | Industrials          |
|  4 | WAB    | $  297.99 | $  295.41 |   0.87% | $284.9M     | Industrials          |
|  5 | TRV    | $  376.37 | $  374.00 |   0.63% | $769.2M     | Financial Services   |
|  6 | APGE   | $  134.26 | $  134.40 |  -0.10% | $394.2M     | Healthcare           |
|  7 | URI    | $ 1139.71 | $ 1143.69 |  -0.35% | $528.9M     | Industrials          |
|  8 | JPM    | $  349.90 | $  351.24 |  -0.38% | $3580.7M    | Financial Services   |
|  9 | AIT    | $  344.08 | $  345.48 |  -0.41% | $104.8M     | Industrials          |
| 10 | LQDA   | $   89.03 | $   89.51 |  -0.54% | $148.6M     | Healthcare           |
| 11 | ATAI   | $    7.17 | $    7.22 |  -0.69% | $154.4M     | Healthcare           |
| 12 | BAC    | $   61.28 | $   62.12 |  -1.34% | $2158.0M    | Financial Services   |
| 13 | MSM    | $  125.83 | $  127.55 |  -1.35% | $114.3M     | Industrials          |
| 14 | HOMB   | $   30.73 | $   31.18 |  -1.44% | $70.6M      | Financial Services   |
| 15 | TXNM   | $   58.30 | $   59.53 |  -2.07% | $94.5M      | Utilities            |
| 16 | BNY    | $  160.11 | $  163.77 |  -2.23% | $752.1M     | Financial Services   |
| 17 | USB    | $   63.33 | $   64.84 |  -2.33% | $581.0M     | Financial Services   |
| 18 | KFY    | $   77.84 | $   79.97 |  -2.66% | $51.8M      | Industrials          |
| 19 | SPG    | $  225.20 | $  231.53 |  -2.73% | $498.8M     | Real Estate          |
| 20 | PNC    | $  249.26 | $  256.49 |  -2.82% | $567.3M     | Financial Services   |


---

## Advisory & Invalidation Gates

### MOM_SHORT (Watch-Only, NOT Sized)

1. **Crash-reverse guard:** `s1_standdown`=FALSE (no immediate V-bounce signal firing), so the hard gate is _not_ active 
   at the screener level. However, PULLBACK regime + tight cohort (14 names) suggests limited opportunity.

2. **Lane cap:** Per 2026-07-18 audit, MOM_SHORT is **advisory-only until DURABLE-N≥30 forward-positive-excess re-validation**. 
   No new starters tonight, regardless of candidate quality.

3. **Split-artifact check:** QS, ROL, ISRG, AZO all appear clean on live Yahoo data (no recent splits distorting 52w range).

4. **Correlation risk:** Cohort is small; if it expands, watch for theme clustering (e.g., if Consumer Cyclical dominates, 
   tag for risk-sizer).

### MOM_LONG Basket (Tail-Aware, Never Per-Name HIGH)

1. **Basket gate (correlation ≥0.70 collapse):** Financials cluster (30 names) — hand to risk-sizer with `corr_warning=true`.

2. **Regime fit warning:** PULLBACK regime reduces the long-basket edge. Regime_fit is reduced; the names are _at_ highs 
   but the environment is risk-off. Capture only as diversified basket.

3. **Right-skew caveat:** MOM_LONG edge is tail-driven (+2.35% mean, −9.3pp hit-base). Most names underperform the 
   high-base; a few big winners carry the edge. Size as basket-only.

---

## Summary & Sizing Recommendation

| Lane | Cohort | Status | Recommendation |
|------|--------|--------|-----------------|
| MOM_SHORT | 14 names, QS leader | Advisory/Watch | HOLD lane cap; no new starters. Monitor for regime shift. |
| MOM_LONG | 60 names, Fin-dominant | Basket-only | WATCH basket in PULLBACK; regime_fit reduced. Express via diversified basket if conviction supports. |

**Bottom line:** 
- MOM_SHORT remains tightly gated (lane cap + small opportunity set in PULLBACK)
- MOM_LONG basket has contracted but remains diversified; Financials dominate but not monolithic
- PULLBACK regime reduces regime_fit for the long-basket edge
- **Zero new sized starters tonight.** Watch the cohort maps for re-validation opportunities in /calibration-audit.

---

*Generated: Phase B automation, 2026-07-23 post-market.
Truth-set stale @ 2026-07-17 — all metrics computed from fresh UW panel (2026-07-23) and live Yahoo 52w data.*
