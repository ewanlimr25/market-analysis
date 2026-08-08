# Market Scan — 2026-07-16

## Regime & Verdict
- **Regime:** CHOP (uptrend structure intact, no directional thrust) · vol-state: SPY near zero-gamma flip / VRP **FAIR**, QQQ short-gamma-ATM + vol cheap-vs-realized (premium-buying, expansion-prone) · VIX 16.73→18.07 (mild pickup) · breadth **divergent** (pct_green 36.4%, adv 183 / dec 191; NFLX −10.94% earnings crash drove QQQ weakness, sector-contained) · `directional_tradable` = **TRUE** (thin, OI-fade/PCR-fade leaning) · `s1_standdown` = **FALSE** (SPY ret5d −0.13%, QQQ ret5d −2.4% — no crash guard; MOM_SHORT live).
- **Event risk:** FOMC 2026-07-29 rate decision is **inside the h=10 window** (07-16 → ~07-30). CPI/PPI/NFP fall outside.
- **Bottom line:** **No new sized directional edge tonight.** This is a position-management night — **1 exit (LNG), 3 cautious holds (ORCL/ICE/MAT), 1 veto (ROST)**. The only new candidate that surfaced was fundamentally vetoed. Correct modal output for a divergent CHOP tape.

## Directional Book (excess-scored)

| Ticker | Lane | Dir | Horizon | Action | Realized excess | Size | Invalidation | Gates |
|---|---|---|---|---|---|---|---|---|
| **LNG** | OI_FADE | short | h10 | **EXIT @ $259.00** | **+2.13%** (closed a winner) | drop | pre-registered 2nd-consecutive-negative net-OI print | Trigger fired: net-OI 07-15 −1,241 → 07-16 −9,912; trailing-5d net +17,983 → −2,038 (build inverted, full call-unwind). Signal-driven exit of a rule written in advance. |
| **ORCL** | MOM_SHORT | short | h10 | **HOLD, no add** | +5.78% | starter (−1 tier) | RSI reclaims >45 **AND** close > $144.22 (0-of-2 met) | Liquidity PASS. Fundamentals **fresh CAUTION** (short is catalyst-corroborated by AI-capex/credit-risk news, −33%/mo — not vetoed) but RSI 17.6 / new 52w low = extreme-oversold **bounce risk** → −1 tier, tightened monitoring. FOMC in-window. |
| **ICE** | OI_FADE | short | h10 | **HOLD, no add** | −2.76% | starter | close back above pre-build breakout, or 5d net build fully unwinds | Liquidity PASS. Deteriorating: fresh 52w high ($141.76), OI build stalled flat (~+5,023). Invalidation clause 1 is a **known untestable spec defect** on a monotonic-up path (re-flagged, not fixed tonight — gated on `retro_harness.py --all`). |
| **MAT** | OI_FADE | short | h10 | **HOLD, tight watch** | **−10.46%** (worst in book) | starter | close > $16.50 (~52w-range midpoint reclaim), or 5d net unwinds | Liquidity PASS (thinnest cushion, $74.6M ADV). Build reasserting (5d net +9,525, signal live) BUT today +5.7% pop to $14.65 closed ~1/3 of the gap to invalidation in one session. **Highest risk-of-invalidation-next-print in the book.** |
| ROST | OI_FADE | short | h10 | **VETO → watch-only** | — | watch | — | Fundamentals **VETO**: beat streak +14.47%, insider MSPR +35.5, Zacks #1 Strong Buy, rising estimates. Call-OI build is corroborated conviction, not crowding — fading it fights momentum **and** fundamentals. Not sized. |

*No new sized entries.* MOM_LONG (242-name near-52w-high basket) is tail-driven and marginal in CHOP — basket/tail note only, never a single-name call.

## Vol Book (non-directional — delta-neutral, advisory, net-of-cost)
- **Earnings IV-crush SELL-VOL — watch-and-confirm (NOT fire-now, 6–7d lead):** **INTC** (ER 07-23, IV rank 96.9, clean term-structure kink 07-24 128% → 08-14 98%) and **NOW** (ER 07-22, IV rank 97.3, clean kink). Both defined-risk iron flies with wings beyond the implied move; re-verify IV rank / kink 1–2 sessions pre-print before sizing. DPZ/TEL/CCI and thin names skipped (no clean expiry bracketing earnings, or liquidity too thin net-of-cost).
- **0DTE-VRP:** **SPY** — marginal GO, **half-size** (VRP only FAIR, iv30 13.7% vs rv 15.6%; near zero-gamma flip; open-entry iron condor, wings ≈ ±1.2%). **QQQ** — **STAND ASIDE** (short-gamma-ATM + vol cheap-vs-realized vrp −0.057 = premium-buying/expansion-prone; also 1.63× front-end backwardation — two stand-aside gates).

## Watch / Stood-down
- **ROST** — OI_FADE short vetoed on fundamentals; re-check only if the catalyst stack rolls over.
- **MOM_SHORT fresh names (watch, not sized):** OKLO, SMR, XE, INIO — deeply oversold/volatile nuclear-reversal names (high bounce risk); INIO/BDC have earnings inside h10. OKLO/SMR/XE would collapse to **one** position (nuclear/SMR theme) if ever promoted — 2026-06-23 China-complex discipline.
- **S4 PCR-fade LONGs (advisory half-cap, earnings outside horizon):** KEYS (z 7.0, ER 8/19), COKE (z 4.6), KGS (z 4.5), NTNX (z 4.6, ER 8/26). LTH/RAL/FORM/ECL/MOD excluded — earnings 7/28–7/30 inside horizon. `ivrank_chg_5d` h3 tilt unavailable (truth-set stale at 2026-06-26).
- **S2 liquidity-reversion (IC≈0 binary tag — conditioning only, do NOT rank by size):** PSA (ER 7/29), TPR (8/13), MET (8/5) are the cleaner-earnings survivors; most of the 72-name cohort has earnings 7/21–7/31. Invalidated by news/earnings gate: JPM, C, PRU.

## Risk
- **Correlation clusters:** held shorts ORCL (Technology) / ICE (Financial Services) / MAT (Consumer Cyclical) are three distinct sectors — no collapse. MAT shares Consumer Cyclical with vetoed ROST (no double-exposure while ROST unsized). LNG exit removes it from the cluster set.
- **Event risk:** FOMC 07-29 now inside the rolling h10 window; none of the three held shorts carries a hard time-stop, so all ride through the print — logged as a monitoring flag (not an additive tier cut, per no-additive-confluence). Re-underwrite as 07-29 approaches.
- **Tail caps / discipline:** every gate-driven action tonight was a downgrade or a signal-confirmed exit — no upsize; no position sized above its excess-implied ceiling. Half-cap held throughout.
- **Unshipped rule-fix proposals (gated on `retro_harness.py --all`, NOT shipped tonight):** (1) ICE's untestable invalidation clause on monotonic-up paths; (2) missing hard stop below invalidation for OI_FADE shorts; (3) entry-anchored vs rolling h10 event-risk window ambiguity for held positions.
- **Regression gate:** NOT TRIGGERED — no lane/threshold change made tonight.

---
*Metric reminder carried to conviction_2026-07-16.json: the validated factor `oi_net_5d` is **NET call-MINUS-put** OI change, not call-only. A call-only read sign-flips prints (nearly inverted the LNG/ICE/MAT reads on 2026-07-15).*
