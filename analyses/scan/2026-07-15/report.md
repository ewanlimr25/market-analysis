# Market Scan — 2026-07-15 (Wed, post-market)

## Regime & Verdict
- **Regime: CHOP (uptrend-leaning).** SPY 754.81. ret5d **+1.26%**, ret10d **+1.08%** — short of the +1.5% UPTREND cutoff. 15d drawdown −0.08%: SPY is pinned at its short-term ceiling (07-10 high 755.42), not trending.
- `directional_tradable = TRUE`. `s1_standdown = FALSE` — the 06-15→06-26 dip (−3.42%) recovered as a 13-session grind (+3.54%), not a 5-day thrust, so the crash/V-rebound guard is OFF and MOM_SHORT/OI_FADE shorts stay live.
- **Breadth:** pct_green 51.09% (257/246 of 503) — balanced. Options-flow bullish only 35.3% against price at highs: a mild price/flow divergence, advisory distribution tell.
- **Sector rotation:** OUT of Technology / Industrials / Healthcare; INTO Communication Services / Consumer Cyclical / Financial Services.
- **Vol-state (2nd-moment only):** VIX 15.67. SPY VRP **FAIR** (−0.023, iv30d 13.18% vs rv30 15.52%, iv_rank 13.1 — vol is *cheap*, not rich). QQQ VRP **PREMIUM_BUYING** (−0.071, iv30d 23.12% vs rv30 30.21% — realized running *above* implied). SPY dealer gamma **NEGATIVE**, spot pinned ~0.1% below the zero-gamma flip (~755) — two-way vol-expansion knife's-edge.
- **Event calendar (h10 window 07-16 → 07-29):** **FOMC 07-29** (Tier-1, no SEP) lands exactly on the window close. CPI (07-14) and PPI (07-15) already resolved. **Q2 earnings season sits inside the window** — this is the binding fact tonight.
- **Bottom line: 4 open carry-forward shorts, all held unchanged; ZERO new directional entries.** Every new candidate with a tradable signal has earnings inside the h10 window; the only two names with clean calendars are the two lowest-quality names in the cohort. This is the framework's modal "no new directional edge" output, and it is the correct one.

## Directional Book (excess-scored)

### Carry-forward — held, not re-sized (no invalidation triggered)
| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | Size | Excess now | Invalidation test |
|---|---|---|---|---|---|---|---|---|
| **LNG** | OI_FADE | short | h10 (→~07-28) | +2.07% median (n=640) | 0.40 | **starter** *(unchanged)* | **+3.87%** | NOT hit. $255.83 « $300.89. **First negative net print (−1,241)** after 4 positive — early-warning, see note. 5d net **+17,983**, not unwound |
| **ORCL** | MOM_SHORT | short | h10 (→~07-27) | +0.81% mean (n=273) | 0.45 | **starter** *(unchanged)* | **+0.03%** | NOT hit — requires BOTH RSI>45 (actual **30.41**) AND close above range high $144.22 (actual **$132.49**). Neither met |
| **ICE** | OI_FADE | short | h10 (→~07-27) | +2.07% median (n=640) | 0.35 | **starter** *(unchanged)* | **−0.82%** | Not triggered per letter — 5d net **+5,037**, not unwound. **But see spec defect below** |
| **MAT** | OI_FADE | short | h10 (→~07-24) | +2.07% median (n=640) | 0.50 | **starter** *(unchanged)* | **−3.99%** | NOT hit. $13.86 « $16.50. **Pre-registered trigger tested and did NOT confirm** — see note |

### New entries
**None.** See "Stood-down" below for the gate-by-gate reason on each.

---

## Key adjudications tonight

### MAT — the pre-registered trigger was tested and did not fire
The 07-14 conviction note pre-registered a concrete exit: *"if tomorrow's OI print is ALSO negative, treat that as confirmation of the reversal and flag for exit."* Tonight's net print is **+4,129** (after 07-14's −2,269). The build **reasserted**; 5d net **+13,338**. The trigger did not confirm, so MAT holds — despite excess deteriorating to **−3.99%**, the worst in the book. This is the pre-registered rule executing as written, not a discretionary rescue. Consumer Cyclical is rotation-**IN** tonight = headwind for the short (reflected in regime_fit 0.50).

### LNG — first negative print is an early-warning, not an exit (consistency with the MAT precedent)
LNG's `adverse_flow_exit_check` narrative says *"if the daily OI print turns negative … flag for exit"* — and tonight's net print **is** negative (−1,241). But LNG's **formal `invalidation` field** — the binding contract — reads *"the 5-day net call-OI build fully unwinds without downside follow-through,"* and 5d net is **+17,983**: nowhere near unwound.

These two documents conflict, and the conflict is resolved by precedent that was **vindicated tonight**: on 07-14 MAT printed its own first negative (−2,269) and was explicitly held as *"early-warning only, not a trigger"* requiring confirmation. Tonight MAT printed **+4,129** — the single negative was **noise**. Applying a stricter single-print rule to LNG than the one just proven correct on MAT would be inconsistent and would exit the book's **best position (+3.87%)** on a signal empirically shown to be a false alarm. **LNG holds; flagged for confirmation next run** — a second consecutive negative print changes the read.

### ICE — invalidation is unfit for purpose (spec defect, flagged not fixed)
ICE now has **two consecutive negative net prints** (07-14 −116, 07-15 −294), ratio decayed 0.337 → 0.177, and excess has turned adverse (−0.82%). Its stated invalidation has two clauses and **neither can do its job**:
1. *"Close back above the pre-build breakout level"* — **untestable against ICE's actual path.** ICE never fell below any level; it rose monotonically from $122.91 (06-29) to $139.84 tonight. A "close back above" condition can never fire on a name that never went below, no matter how wrong the short gets.
2. *"5-day net build fully unwinds"* — not met (5d net +5,037).

So ICE holds by the letter of its rule while having **no functioning exit**. This is logged as a spec defect. Re-specifying it is a rule change and **must clear `python3 scripts/retro_harness.py --all` first** — it does not ship tonight.

### ORCL — the 07-14 give-back concern was correct (calibration evidence)
The 07-14 hold-note explicitly flagged give-back risk after ORCL realized +3.10% excess in one day (~3.8× the lane's entire h10 mean). It gave back **all of it in one session** (+3.10% → **+0.03%**) on a $127.94 → $132.49 bounce. The invalidation still fires on neither clause (RSI 30.41, close « $144.22), so it holds at starter. The concern was correctly identified and is now a data point for `/calibration-audit`: front-loaded excess in this lane mean-reverts.

---

## Watch / Stood-down (gate-by-gate)

### OI_FADE — the strongest lane produced a real cohort that the event gate disqualifies
The h10 window is **07-16 → 07-29 (10 trading days)**. Q2 earnings land inside it for four of five candidates:

| Ticker | Signal quality | Earnings | Verdict |
|---|---|---|---|
| **DINO** (HF Sinclair, Energy) | **Cleanest tonight** — net OI positive all 5 sessions and *accelerating* (+3,099/+131/+2,778/+2,980/**+29,751**), 5d net **+38,739**, ratio 0.720, ADV $208.8M | **07-28 — INSIDE** | **watch** |
| **ESI** (Element Solutions) | ratio 0.731, 4/5 days positive | **07-29 — INSIDE** (on window close) | **watch** |
| **TEL** (TE Connectivity) | positive all 5 but front-loaded/decaying (5,093 → 74) | **07-22 — INSIDE** | **watch** |
| **AGEN** (Agenus) | ratio 1.884 | 08-10 — outside | **watch** — floors pass by ~1% ($5.01 vs $5.00; $50.7M vs $50M ADV); binary-catalyst biotech, $211M cap, prior round-trip history |
| **WSC** (WillScot) | **decelerating** (7,500 → 1,198 → 662) | 07-30 — outside by 1 day | **watch** — third consecutive downgrade (squeeze float 10.73%/7.6 days, ADV $53.1M = 6% over floor) |

**DINO deserves its own paragraph** because it is the best signal of the night and is being stood down anyway. It is a textbook OI_FADE setup: crowded, accelerating call build into a **fresh 52-week high** ($83.93, exactly 100% of range). But sizing it would stack four independent risks — (a) shorting a fresh 52w high, i.e. the "fading strength" case where hard rule 2's up-biased-tape discipline binds hardest; (b) **earnings 07-28 inside the window**; (c) **FOMC 07-29 on the window close**; (d) CHOP regime. The 07-14 precedent is decisive: **LNG** was sized starter with only *two* such risks, and its acceptability was argued explicitly on *"earnings 08-06 safely outside the h10 window."* DINO has strictly more risk than LNG had, plus the one disqualifier LNG lacked. Consistency therefore puts DINO **below starter → watch**. Note also a genuine cross-lane conflict: at 100% of 52w range DINO is simultaneously a MOM_LONG basket constituent (long) and an OI_FADE candidate (short). Not summed, per hard rule 2 — noted only; MOM_LONG's median ≈ 0 makes it weak evidence either way.

**No `fundamentals-gate` was spawned tonight, deliberately.** Phase D step 4 gates only *names about to be sized*; nothing is. And fundamentals is a **veto channel only, never a promotion mechanism** (`research/80`) — it could not rescue any watch-tier name, only cut it further. Spawning it could not have changed a single disposition.

### MOM_SHORT — 20 names, nothing sized
Top candidate **PNR** verified at **exactly 0.0% of its 52w range** ($64.33, at its low) — a clean near-low name — but **earnings 07-28 falls inside the h10 window**. Same event gate. MOM_SHORT's +0.81% maps to the starter band; an event-gated starter lands at watch. Cluster: IND (CPRT/ORLY/CNM) tagged headwind on Industrials rotation-OUT.

### MOM_LONG — 189 names, basket-only by lane design
+2.35% mean but **median ≈ 0 and hit-base −9.3pp**: tail-driven, never a per-name HIGH. `cluster_id: mom_long_basket_20260715`. FIN cluster (11 names) carries HIGH rate-beta correlation into FOMC 07-29. Watch/basket only.

### S2 liquidity-reversion — 56 names returned, **all watch; lane defect found**
The lane returned 56 "≥90% buy-side concentrated" names with `validated_excess_h5` **empty for every row** — the Phase C score is literally undefined, so nothing can size regardless. But auditing the classifier surfaced a real defect:

| Ticker | Lane's claim | Strict buy (price ≥ ask) | **% printed AT midpoint** |
|---|---|---|---|
| ADBE | "90.1% buy-side" | **3.2%** | **92.6%** |
| LOW | "91.2% buy-side" | **1.2%** | **96.1%** |
| BNS | "98.7% buy-side" | **1.1%** | **97.8%** |
| TRP | — | 0.8% | 98.3% |
| NSC | — | 0.7% | 98.2% |
| GM | — | 3.0% | 94.2% |
| **MNST** | "93.7% buy-side" | **90.8%** | 6.1% |

A **midpoint print is by definition neither buyer- nor seller-initiated** — a negotiated cross carrying zero directional information. The lane classifies mid prints as "buys," manufacturing a 90%+ one-sided read out of ~95% directionally-null volume. ADBE's headline "90.1% buy-side" is really **3.2% buy-side and 92.6% nothing**.

Under a defensible classifier (price ≥ ask), only **15 of 1,294** liquid names clear 90% — **1.2% of the universe**, genuinely extreme — vs the lane's 56. Of the lane's headline names only **MNST** (90.8% strict) and partially BMY (81.2%) reflect real at-or-above-ask aggression. Genuine strict-qualifying cohort: HEFA, MNST, SCZ, TLH, AAAC, CRNX, SCHQ, FESM, GGB, IGOV, FLDR, GSK, EWW, EWJV, BSBR (mostly ETFs — excluded by lane rule anyway).

**Same artifact family as the JPST tiny-base trap and the single-day-print family: a filter that looks selective while selecting noise.** Logged as a proposed rule-set fix; **does not ship tonight** — any threshold change must clear `retro_harness.py --all`.

### S4 sentiment-contrarian — 31 names, advisory-only by lane design → watch; **news gate unreliable**
- **`SLAB` is Silicon Laboratories Inc. — the lane called it "Broadcom"** and attached Broadcom's EU-antitrust and Apple $30B chip-deal news to it. Broadcom is **AVGO**; wrong company entirely. Verified against live Yahoo (`SLAB → Silicon Laboratories Inc., $218.19`). Nothing sized on it (S4 is advisory-only), but that error would have been load-bearing in any lane that could size. **S4's catalyst verification is not trustworthy tonight.**
- **MAT appears in the S4 *long* cohort** (PCR 34.1) while we hold MAT **short** via OI_FADE — a direct cross-lane contradiction. The S4 lane correctly killed it itself: tagged `catalyst_informed` because the put-heaviness follows Goldman's SELL downgrade and Roth/Citi target cuts, i.e. the puts are **informed**, not hedging-overpricing. The lane's own exception logic worked. No conflict materializes.
- `ivrank_chg_5d` h3 tilt: **no fresh data** — `features.parquet` max date is 2026-06-28, stale vs the 07-15 trade date. Not surfaced.

### Regime-data integrity note (does not change tonight's gating)
The `momentum` and `sentiment-contrarian` lanes both independently reported **`ret5d = −2.38%, ret10d = −1.19%`** — sign-flipped and wrong. Live Yahoo and Phase A both give **+1.26% / +1.08%**. Two lanes emitting *identical* wrong figures indicates both hit the known stale-regime fallback (`harness-date-stale-fallback`: `retro_harness --date` silently returns stale regime past the truth-set edge). **Impact contained**: both lanes were passed the Phase A context as binding and their CHOP label coincidentally matched, and gating tonight used the live read throughout. Flagged because it is a live, reproducible bug and the coincidence of the label matching should not be relied on again. Both lanes also carried stale 52-week levels (PNR quoted "$69.93" vs actual $64.33; DAVE "$419.86" vs actual $438.19) — the names still qualified on the live read, but the lane-reported figures should not be trusted.

---

## Vol Book (non-directional, delta-neutral, net-of-cost, advisory — 0 directional points)

### 0DTE-VRP — **HARD STAND-ASIDE, both legs**
`scripts/zerodte_setup.py` returned `GO_PREMIUM_SELL_INTRADAY` for both SPY and QQQ. **Overridden on the live read** — that verdict is built only from VIX-tercile + GEX-regime and **has no VRP input at all**.
- **SPY — stand aside.** VRP FAIR (−0.023), iv_rank 13.1: vol is *cheap*, not rich — not a premium-selling setup by definition. Dealer gamma NEGATIVE with spot ~0.1–0.3% below the zero-gamma flip (~755) = genuine two-way vol-expansion knife's-edge, not the quiet long-gamma case the wing-sizing backtest assumes. That backtest contains **no vol-shock day** and does not condition on flip-proximity.
- **QQQ — stand aside.** VRP PREMIUM_BUYING (−0.071): **realized is running above implied**, so selling premium here sells *cheap* vol — it fights the lane's own measured edge. Front-end backwardation confirmed two independent ways (front/far ratio 1.091; 0DTE IV 31.2% vs 30d 24.4%), hitting the lane's explicit stand-aside gate.

### QQQ GEX tool is broken — confirmed independently
Phase A flagged `zero_gamma_level: 300.35` against spot 717.41 as anomalous. Confirmed and worse: `total_gex` is **negative (−354,621,492)** while the tool's own `regime` label says **"POSITIVE"** — internally contradictory. Hand-reconstructing the per-strike cumulative sum puts the real local flip at **strike ~720–722**, i.e. spot 717.41 is *just below* it, in **negative-gamma** territory — the same knife's-edge as SPY, **not** the comfortable long-gamma regime the label implied. This *reinforces* the QQQ stand-aside rather than offsetting it. Data-quality flag: do not read the QQQ GEX label without reconstructing.

### Earnings IV-crush SELL-VOL — panel-confirmed dates only, advisory
The conflicting web dates for big tech are **resolved by the panel**: TSLA/GOOG/GOOGL **07-22**; MSFT/META **07-29** (outside horizon). None clear the iv_rank ≥ 80 floor anyway (TSLA 40.3, GOOGL 72.7, GOOG 74.8) — excluded on the vol-rank gate regardless of date.

| Symbol | Earnings | IV rank | Term structure | Implied move | $-ADV |
|---|---|---|---|---|---|
| **NFLX** | 07-16 postmkt | 100 | BACKWARDATION (2.96×) | 7.6% | $3.68B — deepest chain (27k contracts) |
| **ABT** | 07-16 premkt | 100 | BACKWARDATION (2.08) | 4.4% | $1.20B |
| **NOW** | 07-22 postmkt | 100 | near-flat front (1.035) | 3.3% | $2.33B |
| **TXN** | 07-22 postmkt | 90.3 | BACKWARDATION (1.86) | 3.5% | $3.00B |
| **TEL** | 07-22 premkt | 96.5 | BACKWARDATION (1.41) | 3.2% | $466M |
| **CCI** | 07-22 postmkt | 96.4 | BACKWARDATION (1.54) | 2.0% | $372M |
| **PM** | 07-22 premkt | 89.7 | BACKWARDATION (1.28) | 1.9% | $988M — thin chain (~275), widen fills |
| **CB** | 07-21 postmkt | 83.8 | BACKWARDATION (1.48) | 1.6% | $582M |
| **STLD** | 07-20 postmkt | 89.8 | BACKWARDATION (1.46) | 3.2% | $336M |
| **DPZ** | 07-20 premkt | 89.0 | BACKWARDATION (1.51) | 2.7% | $312M |

Excluded on options-liquidity despite passing the equity floor: **MAN** (151 near-term contracts, thinning to 1–7), **KALU** (2 contracts). Excluded on price/ADV floor: TNL, CCS, FNGR.

**Net-of-cost caveat (binding):** this repo carries **no calibrated per-name net-expectancy backtest** for earnings IV-crush. `RESEARCH/20 §2.1` and `RESEARCH/30 §3.1` validate the *mechanism* only. Per the permanent-advisory rule, this is quoted as **directionally-positive-in-mechanism but advisory-only** — not a sized net-expectancy figure. Defined-risk iron fly, wings set **outside** the implied move with real room, half-cap. **TEL note:** it is simultaneously an OI_FADE short candidate (stood down) and a vol-crush name — different lanes, not summed; its 07-22 earnings is exactly why the directional short was gated.

---

## Risk
- **The dominant risk tonight is calendar, not price.** The h10 window (07-16 → 07-29) contains Q2 earnings for essentially every quality name in the OI_FADE and MOM_SHORT cohorts, and closes on **FOMC 07-29**. Mid-July structurally cannot support a clean 10-day directional book — that, not signal absence, is why nothing new sizes. DINO's signal is real and was stood down purely on this.
- **Open book concentration:** 4/4 positions are **shorts**; 3/4 are **OI_FADE**. That is a single-lane, single-direction book. If the OI_FADE mechanism is regime-impaired in this grind-up tape, all four correlate. No new short was added tonight, which incidentally caps that exposure.
- **Carry-forward P&L is bifurcated:** LNG +3.87% and ORCL +0.03% vs ICE −0.82% and MAT −3.99%. Net book excess ≈ **−0.23%** across four starter positions.
- **ICE has no functioning exit** (spec defect above) — the single highest-priority fix in the queue.
- **Rotation:** Consumer Cyclical (MAT) and Financial Services (ICE) are both rotation-**IN** = headwinds for those two shorts, reflected in their regime_fit.
- Every deviation from a lane's implied ceiling tonight was a **downgrade**. No name was upsized on the strength of any move, signal, or fundamentals verdict. No position was trimmed on profit — no such rule exists and none was invented.

## Proposed rule-set fixes (queued, NOT shipped — each requires `retro_harness.py --all` to pass)
1. **S2 buy/sell classifier**: stop counting midpoint prints as buy-side; require `price ≥ nbbo_ask` for "buy" and add an `at_mid_share` exclusion. Would cut tonight's 56 → 15.
2. **ICE-class invalidation spec**: "close back above X" is untestable on monotonically-rising paths. Invalidations need a clause that can fire on the actual path realized.
3. **S4 news gate**: ticker→company resolution must be verified against a primary source (the SLAB/Broadcom error).
4. **Single-day-print concentration floor** for OI_FADE (`max single-day |build| ÷ |5d net| ≥ ~85%`) — still unpinned, still caught only by lane judgment; third consecutive scan flagging it.
5. **Stale-regime fallback**: lanes calling the regime helper past the truth-set edge get silently wrong `ret5/ret10`. Should fail loudly.
