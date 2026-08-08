# Market Scan — 2026-07-20 (Monday)

## Regime & Verdict
- **Regime:** CHOP (soft, leaning risk-off) · vol-state = short-gamma / rising-vol (VIX 18.65, +24% in 7d; SPY GEX ≈ −$1.94B, QQQ GEX ≈ −$701M, both FULLY_NEGATIVE) · breadth weak (32.6% green, 338 dec / 164 adv) · `directional_tradable = TRUE` · `s1_standdown = FALSE`
- SPY 742.09 — gapped up, faded all session, closed near the low below Friday and below both 20/50DMA (a failed-rally / distribution candle, **not** a rebound). QQQ in a confirmed downtrend (ret10 −3.70%), leading the tape down. This is a genuine risk-off CHOP, not the stealth-grind-up "CHOP" that burned the shorts in the last forward window.
- **Bottom line: no high-conviction directional edge tonight. ONE marginal new starter (PLNT, OI_FADE short, small end), plus held-book management (ORCL hold, ICE exit, MAT cut).** The most robust lane (OI-fade) produced clean names, but fundamentals knocked them all down (ROST VETO, FIG squeeze-watch, PLNT/DINO caution), and the entire MOM_SHORT lane remains on the 2026-07-18 audit's provisional watch-only cap. Mostly a watch list — a correct, common output for this tape.

## Directional Book (excess-scored)
| Ticker | Lane | Dir | Horizon | validated_excess (prior) | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| **PLNT** | OI_FADE | short | h10 | +2.07% med / +0.88% mean (n=640) | ~0.5, −1 CAUTION | **starter (half-cap)** | 5d net call-OI build unwinds (≤0), or close reclaims pre-build breakout, or a 3rd post-print PT raise | liq-floor ✓ · fundamentals CAUTION (beat-and-lower supports short; PT-raise squeeze risk) · no ER in window (08-05) · OI-fade sizing kept per audit |

*Only PLNT clears a real size. All other candidates below fell to watch/drop — see Watch / Stood-down.*

## Held-position reconciliation (carried from 2026-07-17 conviction)
| Ticker | Lane | Entry | Close 07-20 | Gross P&L | State | Action |
|---|---|---|---|---|---|---|
| **ORCL** | MOM_SHORT short | @131.54 (07-13) | 121.38 (−3.98% d) | **+7.7%** | working; inval $144.22 far; ER 09-08 | **HOLD** — carried forward |
| **ICE** | OI_FADE short | @137.67 (07-13) | 141.57 (+1.37% d) | **−2.8%** | build unwound (5d net +1.4k, was net-negative 07-14→17); **ER 07-30 inside window** | **EXIT / cover** |
| **MAT** | OI_FADE short | @13.33 (07-10) | 14.14 | **−6.1%** | signal decaying (today −349); stop $16.50 far; ER 08-04 | **CUT / TRIM** on decay |

ICE is the clean exit: the crowded-call catalyst dissipated without price follow-through, and holding an OI-fade short through the 07-30 earnings print is the S2/IBM earnings-gate lesson.

## Vol Book (non-directional, delta-neutral, advisory)
- **Earnings IV-crush SELL-VOL (this week):** INTC (07-23, IVR 100, implied move 11.56%, term-structure backwardation 1.62×), CHTR (07-24, 2.13×), TXN (07-22), NOW (07-22) — all confirmed genuine event-kinks, wide-wing iron flies only (8–19% implied moves run over narrow structures). KLAC/CDNS next. Mag-7 (MSFT/META 07-29, AAPL/AMZN 07-30) building term-structure backwardation but IVR not yet at admission bar / outside the ~7d window — re-screen Tue/Wed, do not size yet.
- **0DTE-VRP:** SPY GO, net-of-cost +0.16%/day, standard size, no gate tripped — thin but real. QQQ fragile: net +0.27%/day on paper but front-end-backwardation caution (half-sized) AND on the wrong side of the 30d VRP (vol cheap vs realized). **Thin, standard-size-only, no scale-up night** into FOMC/PCE week; SPY is the cleaner sell if choosing one. The 0DTE validation sample contains no vol-shock day — treat GO as a floor, not a promise.

## Watch / Stood-down
- **FIG** (OI_FADE) — cleanest OI-fade persistence, but CAUTION + on a public "squeeze-watch / bears love to hate" list with fresh Buy re-rates (BofA $30 PT). Squeeze risk is the exact failure mode of a crowded-call fade → watch, not sized.
- **DINO** (OI_FADE) — high persistence but earnings 07-28 inside h10 + refining sector tailwind (Hormuz/crack spreads) → event-capped to watch.
- **ROST** (OI_FADE) — **DROPPED** (fundamentals VETO: insider buying +35.5 MSPR, beat streak, ROE 38%, 47 new stores, Zacks #1 — strong bullish contradiction to a short).
- **CRNX** — cross-lane conflict (near-52w-high MOM_LONG tag vs OI_FADE short tag) → explicitly no conviction, watch.
- **CPRI** (MOM_SHORT) — cleanest CONFIRM short in the scan (rev −21.8%, no insider support, PT cuts), but the whole MOM_SHORT lane is provisionally capped to advisory/watch per the 2026-07-18 audit. First promotion candidate when the lane clears a DURABLE-N (≥30) forward-positive re-validation.
- **QXO + Industrials cluster** (CNM/HONA/KTOS/CPRT/ESAB/ECHO) — MOM_SHORT near-52w-low basket, collapsed to one cluster and capped to watch. QXO carries CAUTION (strongest insider buying of the cohort = squeeze risk) offset by misses + a regulatory probe.
- **MOM_LONG** (near-52w-high) — basket/tail-only, regime_fit 0.25 (unfavorable in risk-off) → not promoted, no single names.
- **S2 liquidity-reversion** — advisory only (long-tilted, 0.7× regime discount → ~+0.33%, IC≈0). SHOP/BNY/CL (short-side prints), VST/SPG (long-side). Not sized.
- **S4 sentiment-contrarian** — EMPTY (only SKHY qualified; rejected as informed: IPO vol + earnings 07-29).

## Risk
- **Event cluster inside h10:** FOMC 07-29, PCE 07-30, MSFT/META 07-30 AMC, AAPL/AMZN 07-31, TSLA/GOOGL 07-22 — any h10 short opened this week spans FOMC/PCE. PLNT (ER 08-05) clears it; ICE (ER 07-30) does not → part of the exit rationale. NFP 08-07 just outside the window — flag next scan.
- **Correlation clusters:** MOM_SHORT skews Industrials (7 of 15) — collapsed to one position. OI-fade had Basic-Materials + Consumer-Cyclical clusters 3–4 deep — moot tonight since only PLNT sized.
- **Tail caps applied:** OI-fade sized for the crowded-call-squeeze tail (PLNT starter only, at the small end); MOM_SHORT provisional watch-cap (momentum-crash + quiet-grind-up guard); vol-short quoted net-of-cost with the unsampled left-tail caveat.
- **Yellow flag (surfaced, not overridden):** OI_FADE forward excess was −3.04% in CHOP (n=18) in the 2026-07-18 audit — but that window was a mislabeled risk-on grind-up; tonight's CHOP is genuinely risk-off and the SPY-momentum standdown does not fire (SPY ret5 −0.95%, ret10 −1.22%). PLNT starter is within policy but deliberately small.
- **Hedge note:** short-gamma dealers both indices amplify realized moves; VIX rising into a triple-catalyst week (FOMC + PCE + Mag-7). Net book is 1 new small starter short + 1 working held short (ORCL) — low gross, no index hedge required at this exposure.
