# Market Scan — 2026-07-22

## Regime & Verdict
- **Regime:** CHOP · VIX 16.64 (contango/calm, VIX9D 14.88 < VIX 16.64 < VIX3M 19.54) · short-gamma (vol-amplifying, 2nd-moment only) · breadth ~48.9% green (neutral) · `directional_tradable`=true · `s1_standdown`=**FALSE**
- SPY ret5 −0.98% / ret10 +0.27% (inside the ±1.5% CHOP band). 2026-07-21's broad tech bounce **stalled but did not reverse** (QQQ −0.51%, SPY −0.12% today). Defensive/energy rotation under the surface — XLE +4.8%/+6.5% (5d/10d) leads; XLC/XLY lag. Options flow skewed bearish (UW bullish_pct 33.8%) against an SMA-uptrend = mild distribution tell.
- **Tier-1 event risk INSIDE h10:** FOMC **07-29** + PCE **07-30**. Any short opened tonight (window → ~08-05) carries both.
- **Bottom line: No NEW sized directional edge tonight.** The one clean fresh signal (FHN) is floored to WATCH by a compounding CAUTION + FOMC/PCE + near-highs-tail stack. **Maintain the held book, cut one decayed starter.** This is the modal, correct output.

## Directional Book (excess-scored)

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| ORCL | MOM_SHORT | short | h10 | +0.81% / +9.5pp | 0.55 | **HOLD (half)** | RSI>45 AND close>$144.22 (RSI 35.1, $125.84 — not close) | working +4.33% gross; lane cap blocks new starters, not maintenance |
| PLNT | OI_FADE | short | h10 | +2.07% med / hit 0.61 | 0.80 | **HOLD (half)** | 5d net-call-OI negative print (not fired, +395) OR 2nd PT raise | working +2.08%; fund. CAUTION(−1), no add, tighten watch |
| TECH | OI_FADE | short | h10 | +2.07% med | 0.80 | **CUT → skip** | new 52w high >$72.16 (not fired, $0.38 below) | thesis decayed (OI rel 0.419) + pinned at 98.7% range; proactive cover 07-23 |
| FHN | OI_FADE | short | h10 | +2.07% med / +0.88% mean | 0.80 | **WATCH (not sized)** | re-score after FOMC/PCE + off-CAUTION + off near-highs | CAUTION(−1) + event(−1) + 87.6%-range tail all compound → floored |

**New starters tonight: 0.** No name cleared the gate stack for a fresh size.

## Vol Book (non-directional, net-of-cost, delta-neutral — advisory)
- **Earnings IV-crush SELL-VOL** (07-23 prints, IV-rank 98+, backwardation confirmed): **INTC** (10.6% implied, 1.43 backwardation, liquid — cleanest), **TMO** (5.0%, thinner edge), **SAP** (7.1%, ADR — verify spread). **MSFT** (07-29, 2.4% implied) admit but thin + FOMC-day overlap → wide wings, re-confirm pre-print.
- **0DTE-VRP: STAND ASIDE** both — SPY VRP flat (+0.0001) in the LOW VIX tercile (thinnest edge); QQQ VRP negative (−0.0323) + front-end backwardation left-tail gate tripped.

## Watch / Stood-down
- **OI_FADE clean alternates (advisory):** TEL (ER already fired 07-22 AM, resolved; very liquid $470M ADV; but weak 1.11× build), PVH (ER 08-25; 11% SF/4.46 DTC), GPC (ER 10-20; $263M; clean).
- **OI_FADE tail-blocked (watch):** FIG (42.4% SF / 4.0 DTC squeeze; OI build still cleanest/most-persistent, +6919 today), QGEN (EQT/KKR/Advent takeover-rumor gap tail **UNVERIFIED live**; OI signal fading, +44 today).
- **MOM_SHORT lane-capped watch:** **PEGA** now the cleanest promotion candidate (−9.32% below 52w low, ER 10-20, clean) — first in line once the lane clears a DURABLE-N≥30 forward re-validation via `/calibration-audit`. **CNM dropped out** (recovered to +2.94% above low).
- **MOM_LONG basket (tail-only, never per-name):** 76 names, rotated tech→financials (JPM/BAC/GS/RY/TD near highs), zero ER in h10, regime_fit 0.70.
- **S2 (advisory):** NTNX (98.7% one-sided sell), EMN, TD, FORM top of 26 qualified. EXPE dropped (76.5%, fails ≥90% extreme).
- **S4 (advisory):** JBL (PCR 13.26, ER 09-24, IV-rank rising). NYT dropped (PCR collapsed to 0.906, liquidity dried).

## Risk
- **Correlation:** held shorts pairwise 60-day corr all ≈0 (ORCL/PLNT −0.015, ORCL/TECH −0.020, PLNT/TECH −0.156). No cluster. FHN has no truth-set history — quantitative corr uncomputable (data gap; non-material since unsized).
- **Event calendar:** FOMC 07-29 + PCE 07-30 both inside h10 — the binding constraint on any new multi-day short and the primary reason FHN stays unsized (rate-sensitive bank). NFP 08-07 just outside the window.
- **Tail caps applied:** FHN near-highs breakout tail (87.6% range); TECH decaying-thesis + new-high-stop proximity → cut. No squeeze/M&A tails in the sized book.
- **Data notes:** truth-set panel (`data/prices.parquet`) stale @ 2026-07-17 — all OI/liquidity/52w metrics computed from the FRESH UW panel (2026-07-22) and live Yahoo chart closes, not the stale parquet. `build_prices.py` is mid-extension on this branch to close the gap. TECH ER-date discrepancy logged (UW 08-05 vs Finnhub 08-11; both outside h10 from the 07-21 entry).

---
*Regression gate: NOT triggered — no lane or threshold change tonight. All sizing followed the standing 2026-07-18 calibration-audit rules (MOM_SHORT advisory/watch-only cap, S2/S4 advisory-only, excess-as-currency, no additive confluence).*
