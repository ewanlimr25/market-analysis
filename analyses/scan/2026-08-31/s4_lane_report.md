# S4 Sentiment-Contrarian Lane — 2026-08-31

## Executive Summary

**Status:** ADVISORY-ONLY (never sizes)  
**Direction:** LONG  
**Horizon:** h5 (trading days) · Regime: CHOP  
**Candidates:** 15 names (top 5% put-call ratio) + secondary ivrank_tilt 

**No sized allocation. This lane never sizes under any regime.**

---

## Critical Framing

⚠️ **S4 has NEVER had a hit-rate edge.** The baseline panel shows:
- **hit − base = −0.056** (negative — the lane loses more often than SPY baseline)
- Positive **mean excess (+0.25%) is RIGHT-TAIL ONLY**, not a robust hit-rate effect
- This is not a high-probability setup; it captures the occasional +2–5% outlier, but with below-baseline win-rate

**The 2026-08-17 call-volume floor fix (≥250):** Removed PCR-denominator artifacts (names with 3 calls vs 2,046 puts, printing PCR 682). These removed names were **supplying the right tail** — the mean-excess *dropped* from +0.41% to +0.25% when the fix was applied, confirming the artifacts were doing the work.

---

## Mechanical Selection (Point-in-Time, 2026-08-31)

**Gates applied:**
1. **Liquidity floor:** price ≥$5 AND 20d $-ADV ≥$50M (fail-closed)
2. **Option liquidity:** call_volume ≥250 AND put_volume >0 AND (call+put)≥1000
   - The call_volume floor is independent; it is not subsumed by the combined floor
3. **No earnings inside h5 window:** next earnings > 2026-09-08 (trading-day boundary)
4. **ETPs excluded:** issue_type ∈ {Common Stock, ADR}

**All 15 surviving candidates verify on all gates.**

---

## S4 PCR-Fade Candidates (h5, LONG)

| Ticker | PCR | Call | Put | Price | $ADV | IV5d | Note |
|--------|-----|------|-----|-------|------|------|------|
| INFY | 20.68 | 251 | 5191 | $12.06 | $206.7M | +1.72 | High PCR leader; prior blocking (stale) |
| PPL | 12.93 | 513 | 6634 | $34.13 | $269.2M | +27.00 | Also in ivrank_tilt; rising IV |
| ROST | 11.51 | 939 | 10807 | $228.54 | $618.2M | -5.06 | Prior blocking (vol setup) |
| PENG | 9.82 | 632 | 6208 | $49.08 | $82.7M | +0.08 | Clean |
| BAX | 9.02 | 827 | 7462 | $26.00 | $187.7M | +5.12 | Clean |
| RARE | 6.00 | 389 | 2335 | $25.21 | $53.9M | +12.24 | Clean |
| FIS | 5.19 | 304 | 1577 | $40.77 | $258.1M | -5.08 | Clean |
| WY | 4.55 | 455 | 2068 | $23.37 | $123.8M | -8.19 | Clean |
| FITB | 4.14 | 313 | 1296 | $53.77 | $283.3M | -9.29 | Clean |
| EW | 4.00 | 727 | 2907 | $90.75 | $278.0M | -2.86 | Clean |
| PPG | 3.84 | 415 | 1595 | $112.17 | $161.2M | +9.84 | Clean |
| WING | 3.67 | 287 | 1054 | $109.48 | $135.7M | -6.56 | Clean |
| RCL | 3.58 | 8264 | 29588 | $268.74 | $413.1M | -2.67 | Large options book |
| NVS | 3.56 | 942 | 3357 | $152.06 | $218.2M | +2.63 | Clean |
| CTAS | 3.44 | 321 | 1104 | $201.79 | $382.0M | -1.65 | Clean |

**Prior verdicts:** INFY and ROST carry prior blocking verdicts from prior weeks; INFY was a stale long_caution (2026-08-03) and ROST a vol-earnings setup. Both are carried for transparency but represent known challenges.

---

## Secondary Tilt — IVRANK_CHG_5D (h3)

**Profile:**
- **Mechanism:** Rising 5-day IV-rank is the only factor **sign-stable across ALL 3 regimes**
- **Baseline:** IC rank +0.053 (t=+5.2), decile spread +0.9%, no regime concentration
- **Horizon:** h3 (short-horizon, 1 week)
- **Orthogonality:** Corr +0.02 with PCR (independent signal)

**Top candidates (IV-rank rising >+25 points):**

| Ticker | IV5d | Price | $ADV | Note |
|--------|------|-------|------|------|
| JMKE | 43.57 | $21.45 | $99.0M | Emerging vol |
| IONS | 39.54 | $60.36 | $139.7M | Tech exposure |
| ADC | 38.56 | $72.25 | $109.5M | Clean |
| HR | 38.33 | $19.04 | $62.8M | Clean |
| NLY | 35.18 | $22.92 | $145.6M | mREIT vol tick |
| FTV | 32.93 | $58.84 | $131.2M | Aerospace supply |
| NWSA | 27.54 | $30.71 | $120.3M | Media |
| KRG | 27.12 | $25.80 | $66.7M | REIT |
| **PPL** | 27.00 | $34.13 | $269.2M | **In both lanes** |
| FRVO | 26.89 | $15.38 | $55.8M | Clean |

**PPL overlap:** The ticker appears in both S4 (PCR rank #2) and ivrank_tilt (rank #9). This is NOT a confluence signal — the two lanes are orthogonal and score independently. No summing of signals per invariant #2.

---

## Regime-Conditional Validated Excess (Baseline)

**Historical panel (2026-08-15 baseline, 93 days, 2,471-ticker universe):**
- S4 pooled: **+0.25%, n=1241, hit − base = −0.056**
- S4 CHOP cell (2026-08-28 measurement): **+0.0061, t=1.30, p=0.192** (not significant)

**Caveat:** The CHOP cell from 08-28 carries <30 exit-day units, so it is below the DURABLE-N bar and subject to correlated-draw caveats.

**Ivrank_tilt:** No regime-conditional measurement yet (novel factor, pre-registered for validation); baseline IC +0.053 across all regimes with no regime split material.

---

## Invalidations

**S4 PCR-fade:**
- Put-heavy turns out **informed** (name gaps down on real news after being designated as a put-heavy crowd-fade)
- Inform-to-hedging ratio flips against the hedge assumption

**Ivrank_tilt:**
- IV-rank rolls back over within the h3 window (vol mean-reverts)
- Mean-revert floor broken (IV-rank falls below entry point)

---

## Observation Notes

1. **No sized allocation — S4 never sizes**, regardless of measured excess or regime fit.
2. **Right-tail profiling:** If following this lane on a portfolio basis, weight heavily toward the highest-PCR names (INFY, PPL, ROST) as they carry the historical outperformance.
3. **Orthogonal lanes:** PPL and any other overlaps with MOM_SHORT / MOM_LONG / other lanes are scored independently; no confluence crediting.
4. **Ivrank_tilt:** A separate advisory h3 tilt. Do not stack onto the S4 score.

---

## Risk & Regime Context

- **Regime:** CHOP (ret5 +0.470%, ret10 −0.730%, dd15 −1.300%, s1_standdown=False)
- **Vol state:** VIX 14.43 (10d low; dealer gamma flipped SHORT on both SPY and QQQ at spot)
- **Dealer positioning:** Both SPY and QQQ now net short-gamma at spot — trend-acceleration regime with an unsampled left tail
- **Breadth:** Broad red; median stock −0.463%, **2× SPY's −0.227% move** — risk-off tone despite index flatness

**Tail risk:** With dealer short gamma on both legs and VIX in the 10-day low range, hedging flows amplify moves in both directions. Long premium structurally favored over short premium.

---

*Report generated: Phase B, Market Scan 2026-08-31*  
*Truth-set edge: 2026-08-31 (returns unresolved forward)*
