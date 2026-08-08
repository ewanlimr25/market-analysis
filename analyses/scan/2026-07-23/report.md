# Market Scan — 2026-07-23

## Regime & Verdict
- **Regime:** PULLBACK (shift from CHOP) · VIX 18.70 (+12.4% d/d, **contango intact** VIX9D 18.15 < VIX 18.70 < VIX3M 20.60 — vol-pop, not stress) · **short-gamma/vol-expansion intensifying** (SPY GEX −2.47B / QQQ −1.18B, both FULLY_NEGATIVE) · breadth 42.35% green · `directional_tradable`=true · `s1_standdown`=**FALSE**
- SPY 738.18, **ret5 −1.67% / ret10 −1.80%** — ret10 crosses below the −1.5% band → PULLBACK. SPY now under both 20-SMA (745.92) and 50-SMA (745.05); third down day in four. Damage is concentrated in single-name earnings (TSLA −14.5% Q2 miss, GOOGL capex-guide sell-off — both reported 07-22 AH), **not** a broad rotation break; multi-week Energy leadership intact.
- **Tier-1 event cluster INSIDE h10:** FOMC **07-29** + Core PCE **07-30**, with Mag7 stacked on both (MSFT/META 07-29, AAPL/AMZN 07-30). NFP 08-07 just outside (day 11).
- **Bottom line: No new sized directional edge tonight.** Every Phase-B lane returned watch/advisory only — the workhorse OI_FADE lane found **no fresh short that clears the gate stack**, and MOM_SHORT stays lane-capped. **Maintain the held book (ORCL, PLNT); TECH cut confirmed.** This is the modal, correct output.

## Directional Book (excess-scored)

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| ORCL | MOM_SHORT | short | h10 | +0.81% / +9.5pp | 0.65 | **HOLD (half)** | RSI>45 AND close>$144.22 (close $120.04, RSI low — far off) | working **+8.74% gross**; +3.37% short-excess today; lane cap blocks new starters, not maintenance |
| PLNT | OI_FADE | short | h10 | +2.07% med / hit 0.61 | 0.80 | **HOLD (half)** | negative **call_net** print (TIGHTENED) OR 2nd PT raise (0/unmet) | working +1.76%; OI stalled to a wash (−4, not a reversal); fund. **CONFIRM**; close before 08-06 ER |
| FHN | OI_FADE | short | h10 | +2.07% med | 0.80 | **WATCH (not sized)** | re-verify on organic flow after block rolls off + FOMC/PCE + off-CAUTION | **downgraded** — headline build is a 97.7% single-day block artifact rolling off 07-24 |

**New starters tonight: 0.** No name cleared the gate stack for a fresh size.

### Held-book reconciliation (path-aware, live Yahoo chart-API closes + fresh 07-23 UW OI panel)
- **ORCL** (short @ $131.54, 07-13): close **$120.04** → **+8.74% gross**. Fell −4.61% on the risk-off day vs SPY −1.24% = **+3.37% short-excess**. Now sitting essentially *at* its 52w-low. Invalidation far off. **HOLD.**
- **PLNT** (short @ $55.20, 07-20): close **$54.23** → **+1.76% gross**. Net call−put OI trajectory +20,219 → +24,376 → +750 → +395 → **−4** (07-23): a stall/wash (calls still gross-opening +179), **not** a call unwind. Fundamentals **CONFIRM** (0 post-print PT raises; a DB cut 07-22 supports the short). **HOLD**, invalidation tightened, plan exit before the 08-06 ER (h10 boundary).
- **TECH** (short @ $71.63, 07-21): **cover executed at the 07-23 open $71.80 → −0.24% gross.** No green-day stop-out; dead-signal cut executed cleanly. **Dropped from the book.**

## Vol Book (non-directional, net-of-cost, delta-neutral — advisory)
- **Earnings IV-crush SELL-VOL** (all IV-rank 96–100, backwardation confirmed, wide defined-risk wings): **CDNS** & **WHR** (07-27), **SWKS** & **ECL** (07-28), **SIMO** (07-29, **FOMC overlap → wider wings**), **FSLR / ALGM / EME** (07-30, **PCE overlap → wider wings**). Macro-overlap names: treat the implied move as a *floor* for wing placement, not a ceiling.
- **0DTE-VRP: STAND ASIDE both SPY & QQQ.** Rising-VIX left-tail gate tripped (VIX +12.4% into short-gamma/FULLY_NEGATIVE GEX; `size_scalar` 0.0); QQQ additionally trips the front-end-backwardation gate (0DTE IV 1.44× VIX). Re-check at tomorrow's open once the gap resolves.

## Watch / Stood-down
- **OI_FADE — no clean fresh fade cleared.** Top builds all fail ≥1 hard gate: earnings-in-h10 (AVTR 07-29, SSNC/ALLE 07-23, CACI 08-05, TEX 07-30, SRRK 08-06, PRMB 08-05), near-52w-high (FR 84%), squeeze (SRRK 19%SF, CBRS), SPAC/shell (CCXI = Churchill Capital XI), sub-60td listing (CBRS = Cerebras). Carried alternates cleaned up: **TEL** decaying/reversing (today −1,492), **PVH** a put-unwind sign artifact, **GPC** genuine call-OI unwind → **all three dropped**. **FIG** still building but now *doubly* blocked (42% SF squeeze **+** ER 08-05 now inside h10).
- **MOM_SHORT lane-capped watch:** new cohort leader **QS** (−9.39% below 52w-low); **PEGA dropped out** (recovered above threshold). Cohort tight (14 names). First promotion only after a DURABLE-N≥30 forward re-validation via `/calibration-audit`.
- **MOM_LONG basket (tail-only, never per-name):** contracted 76→60 names, now ~50% Financial Services (correlation-cluster flag), regime_fit **reduced** in PULLBACK.
- **S2 liquidity-reversion (advisory, long-tilt crosswind in PULLBACK):** JPM (95% BUY, clean), KMI (92.5% SELL), GM (91.7% BUY), ED (92.1% SELL, borderline ER 08-06), SPG (91.7% BUY). NTNX dropped (72.76%, fails 90%). TPC/MCK news-gated, LBRDK floor-failed.
- **S4 sentiment-contrarian (advisory, half-cap):** **JBL** cleanest (PCR 19.81, ER 09-24, $458.6M ADV, IV-rank rising), then LI, AMRZ. UAA/GFI flagged catalyst-unverified (informed-put risk — fade fails when put-heaviness is informed).

## Risk
- **Correlation:** held shorts ORCL (Technology) / PLNT (Consumer Cyclical) — different sectors, ~0 historical corr, no cluster. FHN (Financials) unsized so corr immaterial. MOM_LONG basket 50% financials flagged for the correlation-cluster gate if ever expressed.
- **Event calendar:** FOMC 07-29 + PCE 07-30 (+ Mag7 both days) inside h10 — the binding constraint on any new multi-day short and the primary reason FHN stays unsized. PLNT's ER 08-06 sits on the h10 boundary → exit before the print.
- **Tail caps applied:** FHN near-highs (85%) + block-artifact signal-quality downgrade → WATCH. No sized new tails. 0DTE left-tail regime → both indices stand aside.
- **Data notes:** truth-set panel (`data/prices.parquet`) stale @ 2026-07-17 — all OI/liquidity/52w/price metrics computed from the FRESH UW 2026-07-23 panel + live Yahoo chart closes, not the stale parquet. `build_prices.py` is mid-extension on this branch (`chore/extend-truthset-panel`) to close the gap.

---
*Regression gate: NOT triggered — no lane or threshold change applied tonight. All sizing followed the standing 2026-07-18 calibration-audit rules (MOM_SHORT advisory/watch-only cap, S2/S4 advisory-only, excess-as-currency, no additive confluence, universe hygiene). The PLNT invalidation tightening and FHN signal-quality downgrade are per-name Phase-D judgment calls, not standing lane rules. Three OI_FADE artifact-screen refinements proposed by the lane (persistence-ratio >0.85 block-roll-off flag, SPAC/shell exclusion, sub-60td-listing exclusion) are logged as candidate lane-hardening for `/calibration-audit` — NOT applied tonight; they did not alter tonight's zero-starter outcome (every affected name was already blocked on other gates).*
