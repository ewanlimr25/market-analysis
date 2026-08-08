# Market Scan — 2026-08-06

## Regime & Verdict

- **Regime:** UPTREND/**REBOUND-THRUST** · ret5 **+3.620%** · ret10 **+4.120%** · dd15 −1.180%
- **Vol-state:** VOL-ACCELERATION-PRONE. VIX **15.15** at a cycle low (15.81 → 16.50 → 15.86 prior sessions),
  but dealers are net **SHORT gamma** in both indices: SPY spot 768.85 vs zero-gamma flip **814.60** (−5.6%),
  QQQ spot 715.47 vs flip **749.31** (−4.5%). Aggregate GEX is positive in both (SPY +33.3M, QQQ +127.2M) —
  that sign sets range/wing-width only; **spot-vs-flip sets the regime**. Suppressed vol sitting on an
  acceleration-prone book. VRP FAIR both names (SPY −0.0041, QQQ −0.0424).
- **Breadth:** pct_green **40.16%** (202 adv / 299 decl of 503), flow-bullish **34.1%** — on a flat tape
  (SPY −0.16%). Net inflow concentrated almost entirely in Technology. `uw risk market-regime` reads
  TRANSITIONAL/reduce-size despite the mechanical UPTREND. **Breadth divergence: YES.**
- `directional_tradable` = **TRUE** (regime admits lanes) · `s1_standdown` = **TRUE**
- **Stand-down margin:** ret5 +3.620% vs the +2.5% trigger → **+1.12pp**. Trajectory this streak:
  08-03 +0.01pp → 08-04 +1.61pp → 08-05 **+3.03pp (peak)** → 08-06 **+1.12pp**. The 5-day return fell
  5.530% → 3.620% overnight. **The thrust is decelerating, not reversing** — dd15 is only −1.18%, so
  there is no pullback underneath it. Roughly 1.1pp more decay ends the stand-down.

**Bottom line: no directional edge today. ZERO new starters for a SEVENTH consecutive session
(07-29, 07-30, 07-31, 08-03, 08-04, 08-05, 08-06); the book stays FLAT for a fourth. The vol book is
EMPTY for a second consecutive session.**

Tonight is **worse than 08-05, not the same**. On 08-05, OI_FADE had two names (EXLS, UCTT) that cleared
the entire mechanical stack and were blocked *only* by the regime. Tonight **neither survives to the regime
question**: EXLS is mechanism-invalidated and UCTT has decayed out of the selection cohort. The lane is back
to a pure zero-mechanically-clean night.

## Directional Book (excess-scored)

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | **none** | — | — |

*Empty is a valid and common output (`RESEARCH/20 §2.0`). Nothing scored; nothing sized.*

## Vol Book (non-directional)

**EMPTY — second consecutive session.** Both stacks were checked; neither clears net-of-cost.

- **0DTE-VRP — STAND ASIDE, both names.** `sell_premium=false`, `size_scalar=0.0` for SPY and QQQ.
  Mechanical gate: dealers net **short gamma** (spot below the zero-gamma flip in both), a
  trend-acceleration regime this sleeve's unsampled left tail cannot survive. VIX 15.15 sits in the LOW
  tercile (bounds 16.5/18.1). QQQ additionally shows front-end backwardation (0DTE IV **1.54× VIX**), an
  independent gap-risk flag. *Gamma-sign discipline held per `5b3daec`: SPY's positive aggregate GEX would
  read "quiet" on the sign alone — the flip is the arbiter, and it says short gamma.*
- **Earnings IV-crush — no certifiable candidate.** 14 names screened (≤7d, IV-rank ≥80); 10 excluded on
  liquidity (premium in the tens/hundreds of dollars). Of the four with real flow:
  | Ticker | DTE | Implied move | Realized history | Read |
  |---|---|---|---|---|
  | FLR | 1 | ~11.6% | mean abs 9.5%, incl. −27.0/−15.2/−13.6/+15.6% | Rich IV is **paid-for tail**, not free premium |
  | AAON | 4 | ~14.6% | mean abs 8.6%, incl. +31.5%, −22.9% | Binary that prices fair |
  | SION | 4 | ~47.6% | 6 quarters only, −10.9…+13.4% | Too little history to trust |
  | ENVX | 6 | ~6.5% | mean abs 3.3%, no >13% print in 10 qtrs | Closest to textbook — but no spread data to certify net-of-cost |
  Not "no candidates" — no candidate whose richness survives its own realized tail **and** a net-of-cost
  check. ENVX is the one worth a chain check tomorrow.

## Watch / Stood-down

### OI_FADE — zero starters; all 15 top-relative-build names die on an independent gate
Nine fail the **liquidity floor** outright (HNI $31.2M ADV, EYE $40.5M, DLLL $36.3M + `issue_type=ETF`,
LZM $3.94, HSTM $5.0M, TORO $0.2M, LNSR $0.2M, SLN $6.1M + ADR, MYGN $3.18). The six survivors:

| Ticker | rel_build | persistence | last call_net | Binding failure |
|---|---|---|---|---|
| MRCY | 3.356 | 0.669 | — | **Earnings** — reports 08-18, inside h10. (66.9% one-day build, but PLTR-partnership news, not M&A) |
| HIG | 1.240 | **1.902** | **−31** | **Mechanism** — build already unwinding (+11,567 on 08-04, then −5,310, −157) |
| HXL | 1.204 | **0.992** | +16 | **Mechanism** — 99.2% is one 08-03 block; 3rd identical session |
| EWTX | 1.165 | 0.824 | — | **Earnings** — reports 08-06, inside h10 |
| WSC | 1.146 | 0.926 | — | **Earnings** + catalyst_split **RESOLVED** (only 3.4% of build survived the print) |
| CCXI | 1.132 | 0.384 | — | **SPAC/shell** — Churchill Capital Corp XI, `issue_type` **null** → fail-closed |

**Carried watch names — both downgraded** (orchestrator re-ran `oi_build.py`, figures reproduce exactly):
- **EXLS — CUT, mechanism-invalidated.** rel_build **1.344 → 0.964** (now below 1.0, out of the top-15),
  persistence **0.833 → 1.09** (past the 0.85 fail threshold), and **last call_net −184 — calls genuinely
  closing**. That is the lane's textbook "OI build reverses" invalidation. No longer merely regime-blocked.
- **UCTT — still mechanically clean, but decayed out of the cohort.** rel_build **1.109 → 0.982**,
  persistence 0.591 → 0.634, **last call_net +795 (positive)**; today's −237 net is puts opening (+1,032),
  not calls closing, so no invalidation trigger fires. catalyst_split still LIVE (35.9% post the 08-03 print).
  It simply no longer ranks — tonight's #15 sits at 1.132.
- **AZN — CUT stands, now on two independent grounds.** The BMS merger rumor **died** (denial 08-05, +6%),
  and the mechanism is separately invalidated: persistence 1.017, **last call_net −3,276**. The new
  M&A-rumor gate flagged last session is still worth writing into the standing stack.

**Forward-decay watch:** no resolvable row tonight — this was a gate-failure night, not an outcome night.
Today sits inside the 08-03→08-07 maturation window for the first post-hygiene-fix h10 cohort. That window
closes 08-07 and the **audit due 08-08 is the first that can grade the current engine** against the
2026-08-01 new-evidence cohort's −3.73% / hit−base −0.53 decay signal.

### MOM_SHORT — 3 genuine near-52w-lows, triply stood down
All three **orchestrator-verified against the Yahoo chart API** — and unlike 08-05, **the lane's own reads
were correct this time** (closes matched to the cent; last session all three were wrong):

| Ticker | Close | 52w low | pct_range | off_high | Note |
|---|---|---|---|---|---|
| APP | $335.67 | 332.19 (**2026-08-06**) | 0.8% | −55.0% | low set TODAY |
| XPEV | $11.68 | 11.54 (**2026-08-06**) | 0.8% | −58.6% | low set TODAY; ADR |
| WING | $116.62 | 116.25 (**2026-08-06**) | 0.2% | −66.3% | low set TODAY |

Stood down on three independent grounds: (1) `s1_standdown` leg (a), +1.12pp margin; (2) invariant #6
watch-only cap for new starters; (3) the lane's own baseline is **negative** (−0.0008 mean). UW `week_52_low`
was **stale on all three** (higher than the chart-API truth) — the field remains unusable for this lane.
8 of 11 screener candidates (72.7%) fail-closed on the prices.parquet coverage gap.

### MOM_LONG — BASKET_WATCH, barred on three counts
49 of 199 candidates in coverage (**150 fail-closed, 75.4%**). Basket excess **+0.23% vs the +0.30% bar**,
median negative, tail-carried. **Sector concentration ~38% Financial Services — exceeds the 1/3 cap (gate #7).**
Second, independent bar: `risk-sizer.md` blocks starter sizing until a **DURABLE-N (≥30)** forward window
re-clears positive excess, re-enabled via `/calibration-audit`, not ad hoc. Top by proximity: VSXY, RTX,
RVMD, CAKE, AMP, SCHW, NEU, BAC, V, HIG — note **7 of 10 printed their 52w high today**, and **HIG is
simultaneously an OI_FADE short candidate** (cut on mechanism) — a cross-lane conflict, never netted.

### S2 dark-pool reversion — ADVISORY (never sizes)
Pipeline: 192 DP candidates → 102 after ETP exclusion (**90 removed**) → 92 after earnings h5 (10 blocked:
BCE, CWST, ED, KRMN, PAYO, RGA, RLAY, SLF same-day; HRB 08-11, SPG 08-10) → **83** after liquidity
(9 failed, all sub-$50M ADV). **The requested lane-coherence split was delivered:**
- **(a) POSITIVE `dp_buy_skew` — 53 names, the validated long-tilted setup.** Largest: RTX ($458.6M,
  90.5% one-sided), TJX ($447.3M, 91.9%), CMCSA ($315.2M, 95.4%), ICE ($306.2M, 94.0%), REGN ($293.3M, 97.1%).
- **(b) NEGATIVE `dp_buy_skew` — 30 names, sell-side concentration. UNVALIDATED**, a different microstructure
  setup than the one this lane backtested. Listed for monitoring only, never blended with (a).

### S4 PCR-fade — ADVISORY (never sizes) · **cohort corrected 23 → 18**
**Lane error found and corrected.** S4 reported "ETP exclusion — all pass, no ETF contamination". That is
**false**: five names in its 23 carry `issue_type = 'ETF'` in tonight's screener, which labeled them
correctly — the lane's own filter leaked them. **Stripped: HYG** (iShares HY Corp Bond), **IYR** (US Real
Estate), **MDY** (SPDR MidCap 400), **ITB** (US Home Construction), **AIQ** (Global X AI). This is the
recurring "lanes roll their own ETF filter instead of using `issue_type`" defect.

Corrected cohort (**18** h5 / 17 h10). Highest genuine PCR: NWG 193.3 (ADR), RCI 71.0, SAIC 64.9, ARCB 33.2,
WHR 23.4 (42.5k put OI), BSP 21.7 (ADR), TXT 14.0, ELAN 13.8, XEL 13.8, ALL 12.9, CME 8.4, COKE 8.0, EXE 7.1,
ARE 6.7, FORM 6.5, VIK 6.3, MSCI 6.2, SCCO 6.1. **VIK fails h10** (reports 08-19, inside window) — h5 only.
PCR denominators checked: no thin-call artifacts (min call_volume 19, RCI — flagged). No blocking prior
verdicts. Separate, non-stackable `ivrank_chg_5d` h3 tilt cohort: DFTX, IAG, FLR, CCXI, PL, EIX, ROAD, WSC,
GLNG, EQX — advisory, **not** added to any PCR score.

## Risk

- **Correlation clusters:** none live — zero positions, zero starters. Note for any future engagement:
  MOM_LONG's in-coverage basket is ~38% Financial Services, a single-cluster concentration that would
  collapse to one position under the ≥0.70 rule.
- **Event calendar (next 10 sessions):** **NFP (July) Fri 08-07** — one session out; **CPI (July) Wed 08-12**;
  **PPI (July) Thu 08-13**, back-to-back with CPI. FOMC 09-15/16 is outside the window. Nothing is open, so
  none of this binds tonight — but all three sit inside any h5 or h10 window opened from here.
- **Tail caps applied:** MOM_SHORT capped watch-only (momentum-crash tail + negative baseline);
  vol-short stood aside on the unsampled left tail under short gamma.
- **Hedge note:** no exposure to hedge. The live tension is a cycle-low VIX on a short-gamma dealer book
  into NFP+CPI+PPI — cheap optionality if anything is opened, but nothing justifies opening it tonight.

### Data-quality issues carried forward
1. **`prices.parquet` coverage gap — unfixed, worsening in impact.** `build_prices.py` reads a
   `universe.json` frozen at 785 symbols (783 written tonight) while `build_features.py` uses the live
   screener spine (**2,468**). Fail-closed 150/199 MOM_LONG (75.4%) and 8/11 MOM_SHORT (72.7%) tonight.
   Basket composition is clean but **not complete**.
2. **S4 ETF leakage** (above) — five ETFs in a lane that reported zero contamination.
3. **Momentum lane false alarm:** it flagged **VSXY** as an "inverse VIX ETF" that escaped the filter.
   The screener says **Victoria's Secret & Co., `issue_type` = Common Stock**. Not an ETP; the lane's
   contamination claim is wrong in the opposite direction. (MOM_LONG is barred regardless.)
4. **UW `week_52_low` stale on all 3 MOM_SHORT names** — chart-API verification remains mandatory.
5. **`earnings_gate.py` one-sided bound** — the OI_FADE lane flagged that the window check compares
   `ned.isoformat() <= end` with no lower-bound check. Both affected names (EWTX, WSC) were fail-closed
   BLOCKED either way, so nothing turned on it tonight. Worth a fix.
6. **EWTX `next_earnings_date` possibly stale** — labeled 08-06, but the stock gapped +16.5% on 08-04
   (38.38 → 44.70) then went flat, a pattern more consistent with a clinical readout than a print.

### Streak-count correction
Prior framing carried "seventh consecutive REBOUND-THRUST session". Verified against `analyses/scan/*`:
the current REBOUND-THRUST stand-down run is **4 sessions (08-03 → 08-06)**. REBOUND-THRUST also appeared
07-01 and 07-06, but 07-20 → 07-31 were CHOP/PULLBACK with `s1_standdown=False`, breaking continuity.
**Seven** is the correct count for the *zero-starter* streak, which is a different thing.
