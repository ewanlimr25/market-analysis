# Market Scan — 2026-07-28

## Regime & Verdict

- **Regime: CHOP** · ret5 −0.990% · ret10 −1.460% · dd15 −1.820% (`scripts/regime_check.py`, the same function the harness gates on)
- **vol-state: FULLY_NEGATIVE dealer gamma on both indices** — SPY total GEX −$947.1M, QQQ −$1,076.6M → **vol-amplifying**, realized moves should run larger than usual in both directions. VRP **FAIR** both (SPY +2.77%, QQQ +0.55%) — no premium edge either side. VIX 18.21, down from 18.67, i.e. *not* bid into peak event risk. GEX/DEX fed the vol-state only; no directional read taken.
- **breadth: price/flow divergence.** Price breadth green (S&P500 71.0%, broad mcap>$1B 61.9%) but flow breadth only **36.9% bullish** tickers. `uw risk market-regime` = TRANSITIONAL/CHOPPY, "reduce size". SPY below its 20sma (746.65) and 50sma (744.86). Sector flow *into* Tech and Comm Services — the MSFT/META/AAPL/AMZN complex — and *out of* cyclicals: pre-earnings positioning, not broad risk-on.
- **`directional_tradable` = TRUE** (all four lane cohorts non-empty pre-gate) · **`s1_standdown` = FALSE**
- **Bottom line: ZERO new starters. One held short maintained (PLNT, HOLD to 08-03), one close executed today (ORCL, +10.0% blended short-excess). One watch-only S4 name (HOG).**

Preflight was **not** clean on first run — the truth-set parquets ended 07-27, one session behind the trade date. All three were rebuilt (`build_prices` → `build_returns` → `build_features`) and preflight re-run clear before any lane read them. This is the failure mode that produced an inverted regime on 07-24.

---

## The AI-capex repricing broadened into semicap + memory — and the index is hiding it

This is the most important thing on the tape tonight, and no directional lane can see it.

| Ticker | Close | ret5 | ret10 | pct_52w_range |
|---|---|---|---|---|
| **SKHY** (SK hynix ADR) | 130.17 | **−24.3%** | **−32.9%** | 2.8% — new 52w low today |
| LRCX | 269.61 | −16.3% | **−22.1%** | 51.4% |
| MRVL | 174.47 | −16.1% | −21.6% | — |
| AMAT | 476.46 | −15.6% | −20.0% | 55.0% |
| WDC | 463.51 | −15.5% | −17.7% | — |
| KLAC | 190.80 | −12.3% | −17.2% | — |
| AMD | 454.62 | −16.5% | −17.1% | — |
| MU | 820.53 | −15.5% | −16.5% | 62.3% |
| STX | 747.30 | −16.2% | −14.9% | — |
| **ARM** *(reports Wed AH)* | 244.74 | −15.5% | −13.0% | — |
| **QCOM** *(reports Wed AH)* | 162.88 | −6.1% | −8.6% | — |
| NVDA | 197.01 | −5.0% | −7.0% | — |
| TSM | 392.31 | −7.6% | −6.7% | — |
| ORCL *(closed today)* | 119.96 | −5.6% | −6.2% | 2.4% |
| AVGO | 380.91 | −1.5% | −2.1% | — |
| **SPY** | 740.86 | **−1.0%** | **−1.5%** | 86.2% |

Verified in `data/prices.parquet` and re-verified against the Yahoo chart API.

1. **The index is masking a violent rotation.** SPY −1.5% over 10 days while semicap equipment and memory are −15% to −22% and SK hynix is −33%. Same AI-capex repricing logged in the 2026-W30 weekly review, now accelerated and broadened from the hyperscaler/software leg (ORCL) into the equipment and memory supply chain.
2. **The 52-week-range factor is structurally blind to it.** LRCX/AMAT/MU are 35–38% off their highs yet still sit at **51–62% of their 52-week range**, because they had roughly tripled into June. They are not MOM_SHORT candidates and will not be at these levels — they are *control-cohort* names. This is precisely why tonight's 10–90% control bucket printed −0.90% mean excess: the damage is in the middle of the distribution, where no directional lane looks. **Observation for the journal, not a proposed signal.**

**Why it matters in the next 48 hours:** MSFT and META — the two largest capex guiders — report Wed AH; ARM and QCOM report Wed AH into a −13.0% and −8.6% ten-day tape; AAPL/AMZN Thu AH. All stacked on FOMC Wed 2pm into fully-negative dealer gamma. Wednesday and Thursday's capex commentary is the direct catalyst that either extends this repricing or reverses it violently. **That is the principal reason nothing new was sized tonight.**

---

## The 07-27 cohort squeeze REVERSED — the guard was correctly silent

Last night flagged a violent one-day squeeze in the `pct_52w_range` 0–10% cohort (the MOM_SHORT target) that the index-level `s1_standdown` guard is structurally blind to. **It did not persist.** Two independent recomputes (orchestrator + regime-classifier, differing universe hygiene, both spot-checked against the Yahoo chart API):

| Cohort (`pct_52w_range`) | 07-27 (squeeze day) | 07-28 (today) |
|---|---|---|
| **0–10% (MOM_SHORT target)** | +2.35% to +3.68% mean · 80–89% positive | **−0.40% to −1.15% mean · 33–49% positive** |
| 10–90% (control) | +0.66% mean | −0.78% to −0.90% mean |
| **90–100% (MOM_LONG target)** | +1.22% mean | **+0.59% to +1.48% mean · 64–79% positive** |

The 52-week-range factor's **normal sign reasserted** today (near-high beats near-low). The inversion was a single session that round-tripped. Caveat: some of the 0–10% dispersion is earnings-idiosyncratic given the print calendar (BKNG +6.7%, POWL −8.3%, FRMI −13.1%), so this is one day of reversal against one day of squeeze — direction unambiguous, n thin. **The proposed cohort-arm to `s1_standdown` remains a `/calibration-audit` proposal, not a live patch** (a gate change requires the regression gate).

### Corrections to the 07-27 record
- The 07-27 flag listed **SKHY** among "all ETPs" in the momentum lane's failed exclusion. **That was wrong.** SKHY is **SK hynix Inc. ADR**, $1.11T market cap, `issue_type = ADR`. The ETP is **SKUU** (GraniteShares 2x Long SK Hynix Daily ETF). TIP, AAPD and SKUU were correctly identified; SKHY was not. Tonight's momentum lane classified it correctly and its ETP filter verified as biting (1,874 → 1,451 names, 423 excluded, zero ETPs in output).
- `pct_52w_range` is stored on a **0–1 scale** and legitimately exceeds 1.0 for names trading above their trailing 52-week high. The 07-27 "1.1341 mislabelled ratio" flag was most likely a misread of a valid value.

---

## Directional Book (excess-scored)

**No new positions.** One held short.

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| **PLNT** | OI_FADE | short | h10 → **2026-08-03** | +0.70% mean / +1.21% median (n=906) | 0.6 | **HOLD half** (no add) | Exit at the **earlier** of (a) **2026-08-03 close** (h10, direct trading-day count) or (b) first genuinely **negative `call_net`** print. **Plus a new discretionary stop: close > $59.50, 2-day confirm** | liquidity PASS ($55.94, $94.4M ADV) · cluster PASS (sole position) · fundamentals **CAUTION** · ER 08-06 falls *after* the exit |

> **New tonight — a discretionary stop was added at $59.50 (2-day confirm), ~6.4% above spot.** This is a *supplement* to the pre-registered exit rule, not a replacement, and it is explicitly discretionary: it bounds event-window tail risk across FOMC + five Mag7 prints rather than expressing any measured edge. Flagged plainly because the repo's discipline is pre-registered exits, and a hand-added stop is the kind of thing that should never pass unremarked. Next run must check whether it was hit before re-deriving any stop, and must not treat it as vestigial if PLNT has moved meaningfully in the position's favor.

### PLNT — HOLD the remaining 4 sessions

Marked at $55.94 vs $55.20 entry (07-20): **−1.51% short-excess**. The position is losing, and the honest read is that the evidence is genuinely mixed. It holds anyway, because the pre-registered exit rule governs and neither leg has fired:

**Cut condition NOT met — the build re-accelerated.** Tonight's OI print: call **+1,197** / put +21 = net **+1,176**, the largest single-day call build of the entire 5-day window (trajectory +395 / −4 / +180 / +14 / **+1,176**). `persistence_ratio` rose to 0.668, still under the 0.85 single-block disqualifier. The only near-zero print (−4 on 07-23) was previously established as a put-driven wash, not a call unwind.

**The pre-registered analyst soft-invalidation has NOT fired.** This clause had been carried unresolved for six sessions ("PLNT is one confirmed analyst PT raise away… if landed, CUT"). Full record since the 07-20 Canaccord $80→$82 move: Deutsche Bank **CUT** $61→$55 (07-22); Wells Fargo flat $65 reiteration (07-20); William Blair flat Hold reiteration (07-27). **Zero additional raises, zero upgrades to Buy.** The marginal analyst tape tilts *bearish*. Clause resolved, not triggered.

**Corroborating the short:** PLNT's dark-pool **block-tier prints are overwhelmingly sell-side** — 07-27 buy_ratio **0.16** ($29.4M, 9 trades), 07-28 buy_ratio **0.00** ($10.4M, 187,690 shares, *zero* buy volume) — on ~1.35× normal share volume. That is institutional distribution into a +3.17% up day. Separately, the +1,197 call-OI build came with **negative** net call premium (−$45,693): the calls are being **written**, not bought. *Caveat: DP one-sidedness is the S2 factor and measures only +0.06% excess standalone — this is corroboration for an existing position, not independent evidence.*

**Cutting against the short:** a clean **4/4 EPS beat streak**, net (noisy) insider buying, rev +14.4% / EPS +31.4% YoY. And today's **+3.17% is unexplained** — no dated name-specific catalyst was found — landing on the same session as the record call build. That pattern fits early positioning into the 08-06 print, which falls *after* our 08-03 exit. Inference, not evidence, but it is the main risk carried into the final four sessions. Fundamentals accordingly downgraded **CONFIRM → CAUTION**.

**What would change this:** a genuinely negative `call_net` print (cover immediately), or a fresh Buy upgrade / 2nd–3rd PT raise (cover). Otherwise the position closes at the **2026-08-03 close** regardless of mark. Holding past h10 is unvalidated drift — the lesson ORCL and PRMB both taught this month.

*Exit-date note:* `hz_end('2026-07-20', 10)` returns **08-04** because it rounds outward — correct fail-closed behavior for earnings-gate windows, wrong for a precise exit. Direct trading-day counting gives **08-03** (6 observed sessions + 4 projected, no US market holiday intervenes). **08-03 governs.**

---

## Vol Book (non-directional) — advisory throughout

- **0DTE-VRP, Wed 07-29 (FOMC): STAND ASIDE.** `zerodte_setup.py` returns `GO_PREMIUM_SELL_INTRADAY` for both SPY and QQQ — **overridden**. The validated stack was never conditioned on a scheduled macro binary. Independently corroborated by the raw data: SPY front-end IV ratio **1.33×** and QQQ **1.42×** are both in **backwardation**, which lights one of the model's own two hard stand-aside gates. Two independent reasons to sit out, not one.
- **0DTE 07-30+:** cannot be scored until Wednesday's post-FOMC export. FOMC resolves before Thursday's cash session, so Thursday is not itself sitting on a live binary — re-score fresh on its own merits. The real hazard is **Friday 07-31's open**, which gaps in MSFT/META/ARM (Wed AH) *and* AAPL/AMZN (Thu AH) together.
- **Earnings IV-crush:** only **PLNT (08-06)**, **MSFT** and **FSLR** clear all three legs (IV-rank ≥80 + genuine backwardation + positive VRP). **META, AAPL and AMZN fail on VRP** (−0.006 / −0.040 / +0.090 with iv-pctile 77) — gross option richness that does not survive netting against realized vol, exactly the Vilkov failure mode. **Do not size those three.** ARM has the fattest implied move (11.0%) and steepest backwardation (1.93×) but its IV-rank disagrees across sources (82.7 vs 59.5) — watch-only.
- **PLNT vol structure stands** (implied move 10.9% / ≈$6.10, VRP +0.265, IV-rank 87.5, backwardation) and **does not overlap** the directional short, which exits 08-03 before the 08-06 print. If taken it must be booked and P&L-tracked as its **own** structure, never as a modification of the short.
- Nothing here has cleared the standing promotion bar (vol-shock day sampled + tail-aware net expectancy). **Thin book or none is the correct posture into this event stack.**

---

## Watch / Stood-down

- **HOG** (S4 sentiment-contrarian, long, h5–10) — **WATCH, not sized.** The first S4 name this month to survive scrutiny: vol_PCR 5.37 (95th pctl 3.76) on a *real* denominator of **307 calls** (clears the new ≥75 floor that killed PFGC's 16-call artifact), OI-PCR 1.183 = 84.1st percentile, liquidity PASS ($68.9M ADV), earnings clear (next print 11-03), no prior verdict. Tape is a textbook setup: four-session post-earnings capitulation from $28.45 → $24.79 (−12.9%) despite a *raised* 07-23 outlook, then today a reversal bar (open 24.53, low 24.45, close 25.29, +1.78% excess, closing near the high).
  **Held at watch because the mechanism is contradicted.** `net_put_premium` = **−$11,791** (puts net **SOLD**) and `net_call_premium` = **+$4,669** (calls net bought) — netprem +$16,460, flow reads *bullish*. S4 fades a crowd that **bought** puts; on a premium-weighted basis that crowd does not exist here. The whole options book is ~**$66K of premium across 1,956 contracts** (~$0.34/contract) — too thin to call a crowd. Against a **+0.44% advisory-only** prior, over a horizon running through FOMC + five Mag7 prints, on a rate/consumer-sensitive name in a vol-amplifying negative-gamma tape, that is not enough. Re-look post-FOMC.
  *Note: premium-signed PCR is **not** part of the validated S4 spec. It was weighed as evidence quality, **not** applied as a new gate — doing so would be an unvalidated patch (invariant #5). Logged as a `/calibration-audit` proposal.*
  *No `fundamentals-gate` was run on HOG. That is correct per gate 4 — the gate is spawned only on names about to be sized, and HOG is not. It must be run before HOG can ever move past watch.*
- **SKHY** (SK hynix ADR) — MOM_SHORT cohort, **watch-only capped**. $130.17, new 52-week low today, ret5 −24.3% / ret10 −32.9%, $6.55B ADV, no scheduled earnings in h10. Four consecutive down days closing near the low each session; notably it *fell* 7.5% on 07-27 while the near-52w-low cohort squeezed +2.4–3.7%, i.e. genuine distress rather than cohort noise. Not sized: MOM_SHORT's prior is **−0.03% mean** and shorting after −33% in 10 sessions is the momentum-crash tail the lane's negative mean describes.
- **FRVO** (Fervo Energy) — MOM_SHORT cohort, **watch-only capped**. $21.12, ret5 −21.7%, pct_52w_range 1.6%, $70.3M ADV, ER 09-28. Carries a prior CAUTION (07-07) and sits outside the 783-name truth-set panel (data gap, unverified).
- **MOM_LONG** — 298 names pass screening; basket/tail-only by construction (+0.18% mean, median −1.06%), never sized per-name. No basket initiated into the event stack.
- **S2 liquidity-reversion** — 24 names cleared all gates, **nothing advisable**. Prior is +0.06% (≈zero) and a 3–5 day horizon opened today runs straight through FOMC and every mega-cap print.
- **OI_FADE near-misses** — HRI (rel_build 1.70, persistence 0.57, catalyst LIVE), TPG (1.49, 0.43), AME (0.53, 0.41) all cut **solely** on earnings inside h10. The dense print calendar is what emptied this lane, not signal quality.

---

## Risk

- **Event stack:** FOMC Wed 07-29 2pm ET (no SEP) · MSFT/META/ARM/QCOM Wed AH · AAPL/AMZN Thu AH · NFP Fri 08-07 · CPI Wed 08-12. Five of the Mag7 report inside 48 hours, stacked on FOMC, into fully-negative dealer gamma on both indices.
- **Correlation clusters:** none active — PLNT is the sole live position, so the cluster gate is trivially satisfied.
- **Tail caps applied:** MOM_SHORT watch-only cap held (SKHY, FRVO unsized); S4 advisory cap held (HOG unsized); vol book capped by the unsampled left tail into a mega-cap AI-capex print week.
- **Held-book reconciliation:** swept **every** July envelope for names with a real size (29 found) and cross-checked against the audit resolvers. All 29 appear in `analyses/audit/2026-07-25/resolved_calls.json`. The PRMB failure was therefore specifically a **live held-book management** gap (it drifted 4 sessions past its h10 unmanaged), *not* a calibration-grading gap — the audit catches grading; the nightly reconciliation is what missed the exit. Tonight's book is fully reconciled: PLNT live, ORCL closed.
- **Regression gate:** not required — no lane logic or threshold was changed tonight; `git status` clean. Any proposed fix (cohort arm on `s1_standdown`, premium-signed PCR corroboration for S4) must clear `python3 scripts/retro_harness.py --all` against the `4ec89dc` baseline before shipping.

### Resolved for `/calibration-audit`

**ORCL (MOM_SHORT short) — CLOSED 2026-07-28 at the open, $118.18.** Entry 07-13 $131.54.

| Leg | Exit | ORCL | SPY | Short excess |
|---|---|---|---|---|
| First half | 07-24 @ $114.99 | −12.58% | −1.37% | **+11.21%** |
| Second half | 07-28 open @ $118.18 | −10.16% | −1.33% | **+8.82%** |
| **Blended** | | | | **≈+10.02%** |

Closed on **h10 horizon expiry**, not a stop — the $123.50 stop never triggered. Worth recording: ORCL made a **new 52-week low intraday today ($114.50)** and then reversed to close $119.96. On a short, the $118.18 open fill therefore captured **more** than a close fill would have — **+8.82% vs +7.69% short-excess (+1.13pp)**, or +10.16% vs +8.80% gross. *(The sizer's envelope originally asserted the opposite sign in `calls[ORCL].invalidation`; corrected in place, and its `watchlist_write_back` had it right.)* A single +10% short-excess win against a lane whose measured mean is **−0.03%** is a tail draw, not a validation of MOM_SHORT — it should be logged as one observation in a fat-tailed distribution and must **not** be used to argue for lifting the watch-only cap.
