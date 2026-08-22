# Weekly Review — 2026-W34 (Mon 2026-08-17 → Fri 2026-08-21)

Panel/truth-set preflight **clear** (5/5 UW groups; prices/returns/features all reach 2026-08-21).
Weekly panel now **31 weeks (25 full 5-day weeks)**, 2026-01-19 → 2026-08-17, 2,435 tickers.

Convention note: `w_ret` is the weekly **open→close** return from `weekly_features.py`, as in every prior
weekly review. Friday-to-Friday close-to-close is quoted separately where it matters
(SPY −1.368%, QQQ −2.412%, IWM −1.681%).

---

## 1. The Week in Pictures (DIARY — documentation, 0 signal)

### Weekly candles

| | O | H | L | C | w_ret | close_pos | body_frac | structure vs prior |
|---|---|---|---|---|---|---|---|---|
| **SPY** | 776.18 | 776.78 | 762.04 | **765.72** | **−1.35%** | 0.25 | 0.71 | lower_low, **no** higher_high, follow-through **F** |
| **QQQ** | 732.95 | 734.58 | 708.52 | **713.44** | **−2.66%** | 0.19 | 0.75 | **OUTSIDE WEEK**, HH+LL, follow-through **F** |
| **IWM** | 303.96 | 304.33 | 297.04 | **299.96** | **−1.32%** | 0.40 | 0.55 | lower_low, follow-through **F** |

**The three-week up-streak ended, and it ended badly for the Nasdaq specifically.** 07-27 (+0.28%),
08-03 (+3.18%) and 08-10 (+0.48%) were three consecutive up weeks on SPY; this week broke the run with
all three indices failing follow-through simultaneously.

**SPY's upper wick was 0.60 of a 14.74-point range.** The high was made at Monday's open and never
revisited. That is a rejection-from-the-open week, not a week that tried and failed at a higher level.

**QQQ printed a bearish OUTSIDE week** — a higher high *and* a lower low than the prior week, closing in
the bottom fifth (close_pos 0.189) on a 0.749 body. It is the strongest single structural tag on the
board. **SPY did not print one** (its high, 776.78, never exceeded the prior week's 779.37). That
divergence is the week in one line: the damage was Nasdaq-shaped, not index-shaped.

**Last week's partial repair failed and re-broke.** QQQ's gap to its 2026-06-15 panel-peak weekly close
(740.62) **widened from −1.29% to −3.67%** — the first widening since the gap started being tracked in
W31. SPY and IWM both set panel-high weekly closes *last* week and both fell straight back below them
(−1.37%, −1.68%).

### Catalyst anchoring — **no Tier-1 print landed this week**

**This must be said explicitly, because it governs what §3 is allowed to accrue.** No CPI, PPI, PCE, NFP
or FOMC decision was released Mon–Fri. CPI (08-12) and PPI (08-13) were the *prior* week. This was a
deliberately data-light week, and **the macro arm of the PR-WT pre-registration accrues nothing from it** —
the second such week in three (W32 also had none; W33 had CPI+PPI and accrued one observation).

| Event | Day | Reaction |
|---|---|---|
| **FOMC minutes**, late-July meeting | Wed 08-19 | 9–3 hold; **Hammack, Kashkari and Logan each dissented for a quarter-point HIKE**, and the hawkishness ran past the dissenters ("policy tightening would likely be necessary if inflation did not decline"). SPY **+0.21%** — the tape read hawkish minutes as relief and unwound pre-positioning. **Fully reversed the next session: Thu −0.84%, the week's worst day.** |
| **MRNA/Merck Phase 3 melanoma readout** | Wed 08-19, pre-market | intismeran autogene met its primary RFS endpoint. MRNA **+176.97% on the day** — its best ever, ~28x average volume — **+129.20% on the week** to $145.13 on $2.9B ADV, after giving back ~20% intraday. A material part of XLV's +4.33%. |
| Retail earnings (HD, TGT, WMT) + Reddit's S&P 500 debut | Tue–Thu | No attributable index dislocation. |

Daily path: **−0.47 / −0.68 / +0.21 / −0.84 / +0.41**. Only two green sessions, and the first was
given back immediately.

### Regime trajectory (`scripts/regime_check.py --range`)

| Day | Label | ret5 | ret10 | dd15 | s1_standdown |
|---|---|---|---|---|---|
| Mon 08-17 | **UPTREND** | −0.050% | +1.980% | −3.720% | False |
| Tue 08-18 | CHOP | −0.400% | −0.500% | −5.430% | False |
| Wed 08-19 | CHOP | −0.440% | −0.090% | −3.650% | False |
| Thu 08-20 | CHOP | −1.960% | −0.780% | −2.800% | False |
| Fri 08-21 | **CHOP** | −1.370% | −0.980% | −2.020% | False |

**UPTREND → CHOP rollover, not a confirmed downtrend** — ret10 never breached −1.5%. W33's carry-forward
item 3 called this exactly ("regime flips to CHOP on Tuesday 08-18 by window arithmetic alone").

### Vol-state overlay

- **VIX 15.19 → 15.13**: flat net, whippy path (15.19 / 15.84 / 14.89 / **16.01** / 15.13). **VVIX −8.1%**
  (93.92 → 86.27) — vol-of-vol *compressed* while spot VIX gyrated.
- **Term structure CONTANGO all week** (VIX3M 18.50 / VIX 15.13 = 0.818). **No backwardation despite the
  down week** — the market never priced this as a stress event.
- **VRP FAIR**: IV30 12.70% vs realized-30d 12.54%, +0.16pt. No premium-selling edge.
- **SPY dealer GEX FULLY_NEGATIVE** (−894.8M, no zero-gamma flip in range) = vol-amplification regime,
  consistent with the whippy sessions. **QQQ GEX near-flat**; the CLI's "POSITIVE" label
  (zero_gamma 207.89 vs spot 713) is the known artifact and is **overridden for a third consecutive session**.

### Breadth — two universes, both true, reconciled

| Measure | Universe | Reading |
|---|---|---|
| % of names up on the week | full liquid common-stock spine, ≥$50M ADV (n=1,468) | **41.0%** (median −1.01%, mean −0.73%) |
| Equal- vs cap-weight | S&P 500 | **RSP −0.49% vs SPY −1.37% → +0.87pp** |
| Above 50dma / 200dma | S&P 500, Fri close | 57.8% / 69.6% |

**Reconciliation:** it was a **majority-down week in count**, but the *depth* of the damage was
concentrated in mega-cap tech and semis — so the equal-weighted tape beat the cap-weighted index while
most individual names still fell. Both figures are real; they measure different universes, and quoting
either alone misleads. Daily %-green ping-ponged 26.2 / 44.6 / 56.7 / 31.2 / **66.0** and ended on a
genuinely broad Friday bounce.

### Sector leadership and the cross-asset tell

| Winners | | Losers | |
|---|---|---|---|
| XLV | **+4.33%** | SMH | **−4.66%** |
| XLE | +2.79% | XLK | −3.53% |
| XLB | +1.90% | XLU | −3.48% |
| | | XLI | −3.36% |

*(all `week_context.py` series share the same window — no staleness flags)*

**The cross-asset tape is where this week actually explains itself:**

| IBIT | SLV | USO | GLD | UUP | TLT | IEF | HYG |
|---|---|---|---|---|---|---|---|
| **+22.59%** | +7.25% | +6.35% | +5.45% | −0.75% | +0.01% | −0.24% | −0.13% |

**Dollar down, hard assets up, long-duration equity down — and credit and duration completely flat.**
This was not a flight to quality; it was a rotation out of AI/semis into hard assets and defensives.
Note the oddity worth recording: **the bond market did not blink at minutes showing three dissents for a
hike.** Gold, silver, oil and bitcoin all rallied hard into a hawkish read.

### Notable flow (0 signal)

Largest dark-pool premium: SPY $51.1B (62,554 prints), **MU $38.9B (112,327)**, **SNDK $33.3B (118,964)**,
QQQ $33.2B, NVDA $28.9B, AAPL $21.0B, MSFT $18.5B, TSLA $14.5B. MU and SNDK printing at mega-cap-index
scale is the week's standout single-name concentration.

Clean single-name movers (Common/ADR, ≥$50M ADV):

- **UP** — MRNA +129.20%, PURR +58.38%, ASST +47.95%, TEM +39.52%, PSNL +30.91%, MSTR +28.17%,
  AMR +26.47%, SBET +26.36%, BMNR +26.27%, AU +25.88%
- **DOWN** — KLAR −31.07%, WYFI −29.81%, AAP −24.70%, AEHR −24.12%, FN −23.42%, MXL −21.49%,
  OUST −21.13%, **NBIS −21.09% on $5.9B ADV**, TTMI −21.04%

The down list is a coherent **AI/semis supply-chain unwind** (AEHR test, FN optical, MXL, TTMI PCB, NBIS
AI-cloud). The up list is crypto-treasury (MSTR, BMNR, SBET) and gold (AU) — the same hard-asset rotation.

**W33 carry-forward item 5 is RESOLVED, and it resolved the bearish way.** AVGO's −8.13% divergence while
SMH was +0.88% did *not* mean-revert: AVGO fell another **−6.24%** and the rest of semis caught down to it
(INTC −12.13%, AMD −8.00%, NVDA −4.64%, SMH −4.66%). META −6.77% was the notable non-semi mega-cap break.

---

## 2. Validated Weekly Setups (SCORED — excess)

### `calls[]` is EMPTY. Nothing sized. **Fifth consecutive weekly review with no scored setup.**

`held_book.py` against `conviction_2026-08-21.json` reads **0 open / 0 closed**, and that file's own
`book_state.positions=0` confirms the empty result is real rather than the known held_book EXIT-substring
bug. The daily book has now been **flat for 10 consecutive sessions**.

Phase D (`risk-sizer`) was **vacuous** and `fundamentals-gate` was **correctly not spawned** — both run
only on names about to be sized.

### OI_FADE — `NO_NAME_CLEARED`

**The binding constraint is measurement at the lane level, not a gate on any name.**

- **CHOP-conditional excess +0.0014** (n=359, t=0.28, 95% CI [−0.0088, +0.0117]) — indistinguishable
  from zero and **below the +0.3% starter floor**. Pooled (+0.0029, n=1237) is *also* below the floor,
  so both readings agree; per the regime-stratified rule, the CHOP figure is the one that governs.
- Both figures are **h10**, the only validated horizon. A 2–4 week (h10–h21) hold is an **unvalidated
  extrapolation stacked on an already sub-floor prior** — more speculative, not less.

**Orchestrator verification (I did not take the lane's word for this).** I reproduced
`retro_harness.py:94-111`'s selection SQL verbatim at both horizons and the lane's report matches exactly:

- **h10 top-15**: META, INTC, BULL, AMZN, RKT, GME, WULF, MARA, CIFR, CORZ, SOFI, AS, NOK, QXO, TSLA — population **1,399**
- **h21 top-15**: GME drops (reports 09-08, inside the window), **AAPL** enters at #15 — population **1,377**

**The selection-rule mismatch is still total.** The live lane's `rel_build` top-15 — AS 1.81, ULS 1.26,
VIRT 0.98, NXPI 0.78, PR 0.62, NYT 0.60, VIK 0.56, ACMR 0.51, TJX 0.50, ALHC 0.49, CAKE 0.49, FRT 0.46,
PSNL 0.41, DK 0.39, PTEN 0.38 — overlaps the harness population by **1 of 15 (AS alone)**. Fourteen of
fifteen live candidates cannot inherit the prior under any horizon. **6+ consecutive sessions/weeks
unresolved**; a standing 2026-08-22 audit item.

Name-level dispositions:

- **AS — DEAD.** Its mechanical invalidation **fired** (last call_net −5,956, net −3,446) and it was
  `DROPPED_FROM_WATCH` on 08-21 on three independent grounds. Re-entry requires *all* of: last_call_net
  positive again, rank inside the true top-15, and fundamentals CONFIRM.
- **RKT — EXCLUDED.** ValueAct 9.9% activist stake (disclosed 08-14, re-verified live). Catalyst-informed
  positioning — exactly the activist/M&A gap the 7-gate stack is known to pass.
- **QXO — single-day-block caution.** 90,017 of its 99,968 10d net (**90.1%**) landed on 08-21 alone with
  no news catalyst; persistence 0.90–0.91 flags a block, not organic building.
- **BULL — cleanest survivor, WATCH-ONLY.** Organic persistence 0.432, a real post-print earnings-beat
  catalyst, LIVE_BUILD on **both** catalyst_split boundary conventions (53.3% `≥` / 45.5% `>`), no prior
  block, no deal-pinning. Recorded for tracking; **not sized**.

**Correlation note that would have mattered had the floor cleared:** 4 of the true top-15 (WULF, MARA,
CIFR, CORZ) are bitcoin miners, in a week when IBIT rose **+22.59%**. Fading that cohort would be **one
correlated bet, not four** — and would be short a hard-asset rally.

### MOM_LONG — `BASKET_WATCH` (never sizes)

Harness **−0.0127** (n=1154), tail-driven (median −1.56%); DURABLE-N bar unmet; 0 of 52 resolved calls
sized at the 2026-08-15 audit. **225 candidates** after liquidity + sector filters. Top 10: **APGE, CRNX,
WEX, VIRT, FBRX, IQV, BIO, DBRG, BBVA, ILMN**. All clear the h21 earnings gate (window end 2026-09-20).
Sector mix Healthcare 28.4% / Energy 14.7% / FinSvc 13.8%, inside the 33% cap. I verified all ten carry
`issue_type` Common Stock or ADR (BBVA is the ADR) and that their screener 52w bounds reconcile with Yahoo.

**Honest caveat, raised by the lane and confirmed:** the basket's Healthcare/Energy tilt mirrors the week's
winners, so at a 2–4 week hold **this basket is materially a sector-momentum bet in disguise** — precisely
the beta-in-disguise risk invariant 1 exists to catch. The 225 count shows **no sign of the W33 filter
failure** (that run reported ~535 and rationalised it as "horizon expansion").

### MOM_SHORT — `BASKET_WATCH` (never sizes)

Harness **−0.0137** (n=830), 0-for-9 forward (−5.3%) — the one recorded invariant-6 exception.
**Crash guard NOT fired**: `s1_standdown=False` (ret5 −1.370% is not a >+2.5% up-thrust; ret10 −0.980%
does not breach the −2%/−2% unconfirmed-dip test). The lane ran ungated and still sizes nothing on
baseline grounds alone.

**I re-ran the 52-week check myself rather than accept the lane's spot-check**, because stale or
un-split-adjusted UW `w52h` is the known manufacturer of false shorts. **All names confirm against Yahoo**
(`scripts/chart.py`, path-aware) — screener and Yahoo agree on every one, no artifact this week:

| | CPRI | NRG | ONON | BWXT | GXO | LHX | AZO |
|---|---|---|---|---|---|---|---|
| % of 52w range | 0.3% | 0.8% | 1.8% | 2.5% | 3.3% | 3.5% | 3.8% |
| 52w low..high | 13.61..28.27 | 112.50..189.96 | 29.63..51.08 | 154.59..241.82 | 45.00..66.85 | 262.68..379.23 | 2902.20..4388.11 |

**Method deviation recorded:** the lane excluded ETPs by filtering NaN **sector** rather than the mandated
Stock Screener `issue_type` field. It leaked **no ETF** this week, but it did admit **MAIR**, whose
`issue_type` is NULL. MAIR is a real operating company (Madison Air Solutions, Basic Materials, $4.65B
mcap) — **not** an ETP — but an unclassified `issue_type` fails the mandated strict filter, so I dropped
it **fail-closed**, taking the roster 8 → 7. APP and FRVO were correctly excluded on prior blocking
verdicts. **NRG carries a blocking verdict that does not transfer** — it was cut from *OI_FADE* on 08-14
on a fired mechanical invalidation, a different lane's disposition; it is carried here on watch only.

**Structural note, and it matters:** despite SMH −4.66%, **there are no semis or tech names in this
roster**, because they are nowhere near 52-week lows — APP sits −59% off its peak but still far above its
52w low. That is a real screen property, not a filter bug, and it means **this lane is structurally blind
to the exact sector that broke this week.**

---

## 3. Weekly Technicals — PRE-REGISTERED (documented, 0 points, NOT sized)

| Feature | This week | Would signal | Status | Pre-reg bar |
|---|---|---|---|---|
| **QQQ bearish OUTSIDE week** | **FIRED.** HH+LL, close_pos 0.189, body 0.749. Base rate QQQ 5/31 (SPY 1/31, IWM 3/31) | Bearish weekly reversal / trend failure | PRE-REGISTERED | PR-WT — **counter-evidence**: the 4 prior resolved QQQ outside weeks were followed by −1.96, **+2.89, +2.31, +0.86** (mean +1.03%), i.e. historically a *bounce*. n=4 is meaningless |
| **SPY failed follow-through, close_pos<0.30 + lower_low** | **FIRED.** cpos 0.250, body 0.710, upper wick 0.60pt | Distribution / rejection-from-the-open | PRE-REGISTERED | PR-WT — 6 prior obs: −1.50, −2.07, −2.23, +3.43, +0.57, +1.10 → **3-up/3-down**, non-informative. SPY follow_through base rate 21/30 (70%) |
| **reversal-after-catalyst** | **FIRED on MINUTES**: Wed +0.21% → Thu −0.84% | The bearish arm of the event-conditioned feature | PRE-REGISTERED | PR-WT — **accrues ZERO to the Tier-1/macro arm; no Tier-1 print landed.** Logged separately as a minutes-arm obs |
| **QQQ repair-gap failure** | Gap to the 06-15 peak **widened −1.29% → −3.67%**; SPY/IWM fell back below panel-high closes set last week | Failed repair = distribution at the highs | PRE-REGISTERED | PR-WT — first *widening* since tracking began in W31 |
| **index structure divergence** | QQQ outside; SPY made **no** higher high; IWM closed mid-range (0.401) | Concentrated mega-cap-tech damage, not index-wide reversal | PRE-REGISTERED | PR-WT — **new arm, 1 obs** |
| candle-pattern arms (inside / hammer-hanging / star) | **None fired.** SPY inside 0, outside 1, hammer 3, star 1 over 31 wks | Nothing this week | PRE-REGISTERED | PR-WT — SPY's arms **unreachable** at this accrual rate |

Two of the fired arms have **historical evidence pointing the opposite way to their own narrative** — the
QQQ outside week "should" mean reversal and has in fact been followed by a bounce 3 times in 4. **That
contradiction is left standing and unresolved**, because nothing here is scored and resolving it would be
exactly the narrative-fitting this layer exists to prevent.

Panel: **31 weeks / 25 full 5-day weeks** against a ≥2-year, ≥30-obs-per-arm bar — roughly a quarter of
the minimum history.

---

## 4. Carry-forward

### How last week's Layer-2 calls did

**W33 scored nothing** (`calls[]` empty), so there is nothing to grade. Five straight weekly reviews with
no scored setup; the daily book is flat for 10 sessions.

**This week the discipline was cheap and, for once, arguably paid.** SPY −1.37%, QQQ −2.41% Fri→Fri: a
flat book beat a long book. But the honest counterfactual is unchanged from W33 — **the week's money was
in dispersion** (MRNA +129%, INTC −12%), and **no validated lane in this engine addresses dispersion.**
That is a scope fact, not a miss, and it is now the third consecutive week it has been the true story.

### Last week's items, resolved

1. **Regime flipped to CHOP on Tue 08-18**, exactly as item 3 predicted by window arithmetic.
2. **AVGO's semis divergence (item 5) resolved bearishly** — AVGO −6.24% again and the rest of semis
   caught down (SMH −4.66%), rather than AVGO mean-reverting up.
3. **The OI_FADE selection-rule mismatch (item 2) was carried again, undecided, for a 6th+ period** —
   which is precisely what item 2 warned against.
4. **GEN's 52-week-high anchor (item 6) rolls off ~08-22** — still pending, now imminent.
5. **AS ran its full course inside the week**: rank 17 → 15 → 12 (crossing into the measured population),
   then killed on 08-21 by a fired invalidation plus the fundamentals veto. The pre-registered two-leg
   carry trigger from 08-20 resolved cleanly and the name is out.

### What rolls into next week

1. **`/calibration-audit` is due tomorrow, 2026-08-22, and it is the important item.** 23 open call-rows
   (11 OI_FADE, 5 MOM_SHORT, 7 S4), 174 open suppressed candidates, and the 08-03→08-07 crash-guard block
   all mature 08-17→08-22 — **the first genuinely non-overlapping cohort, now deferred twice**. Count
   distinct **exit-days**, not rows.
2. **Decide the OI_FADE selection-rule mismatch at that audit — do not carry it a seventh time.** This
   week it was again *total* (1/15 overlap, orchestrator-verified). Two options stand: add the live-lane
   screens to the harness and re-baseline, or formally record the prior as inherited/discounted.
3. **A Tier-1 cluster lands in week 1 of any hold opened this weekend**: **PCE + NVDA earnings 08-26**,
   **Jackson Hole 08-27/29** with **Warsh's first keynote as chair on 08-28**, then NFP 09-04, PPI 09-10,
   CPI 09-11, FOMC 09-15/16. NVDA reports straight into the semis break documented above.
4. **Watch whether the hard-asset rotation persists or reverses.** Gold, silver, oil and bitcoin all
   rallied hard into hawkish minutes while credit and duration sat flat. If that unwinds, XLV/XLE
   leadership — and therefore the entire MOM_LONG basket tilt — unwinds with it.
5. **MOM_SHORT is structurally blind to the semis break.** If SMH keeps falling, semis will eventually
   enter the 52w-low screen; until then the lane cannot express the tape's clearest trend.
6. **BULL is the only OI_FADE name worth re-checking Monday** — cleanest survivor, watch-only, and it
   only matters if the lane's CHOP-conditional excess clears the +0.3% floor, which it does not today.
