# Weekly Review — 2026-W35 (Mon 2026-08-24 → Fri 2026-08-28)

Panel/truth-set preflight **clear** (5/5 UW groups; prices/returns/features all reach 2026-08-28).
Weekly panel now **32 weeks (26 full 5-day weeks)**, 2026-01-19 → 2026-08-24, 2,435 tickers.

Convention note: `w_ret` is the weekly **open→close** return from `weekly_features.py`, as in every prior
weekly review. Friday-to-Friday close-to-close is quoted separately where it matters
(SPY **+0.47%**, QQQ **+0.42%**, IWM **−1.40%**).

---

## 1. The Week in Pictures (DIARY — documentation, 0 signal)

### Weekly candles

| | O | H | L | C | w_ret | close_pos | body_frac | structure vs prior |
|---|---|---|---|---|---|---|---|---|
| **SPY** | 764.78 | 775.29 | 762.08 | **769.35** | **+0.60%** | 0.55 | 0.35 | **INSIDE WEEK**, follow-through **F** |
| **QQQ** | 709.66 | 724.12 | 702.70 | **716.43** | **+0.95%** | 0.64 | 0.32 | lower_low, no higher_high, follow-through **F** |
| **IWM** | 299.55 | 300.39 | 295.67 | **295.75** | **−1.27%** | **0.02** | 0.81 | lower_low, follow-through **T** |

**The index tape and the stock tape disagreed all week, and that is the whole story.** SPY and QQQ both
closed higher; IWM fell 1.4%; and **only 38.6% of the liquid common-stock spine rose** (median −0.86%).

**SPY printed the first INSIDE WEEK of the entire 32-week panel** — 1 of 26 full weeks, and it is this one.
Its high (775.29) sat 1.49 under last week's 776.78 and its low (762.08) came in **4 cents** above last
week's 762.04. A week that never left the prior week's range on either side, to within a nickel.

**IWM closed at close_pos 0.017 — the single lowest weekly close position in the 26-week panel (0th
percentile).** It made a lower low, closed on it, on a 0.81 body, and it was the only one of the three
that *confirmed* last week's direction (follow_through **T**). Small caps did not participate in the
index bounce at all.

**QQQ made a lower low and still closed up 0.95%** — a rejection of the 702.70 washout rather than a
trend continuation. Its bearish outside week from W34 did **not** follow through downward.

**The repair-gap tracker reversed direction.** QQQ's gap to its 2026-06-15 panel-peak weekly close
(740.62) **narrowed −3.67% → −3.27%**, the first narrowing after W34 recorded the first widening.
Against the *full-5-day-week* peak (08-10) SPY is −0.90% (from −1.37%), QQQ −2.00% (from −2.41%) — but
**IWM widened, −1.68% → −3.06%.** Two indices repairing, one deteriorating.

### Catalyst anchoring — **two Tier-1-class events landed, and Friday reversed on one of them**

| Event | Day | Reaction |
|---|---|---|
| **PCE (July)** | Wed 08-26 | Headline **3.7% y/y vs 3.6% expected** (unchanged m/m), core **3.3% in line**. Slightly hot. SPY **+0.02%** on the day (O 764.73 → C 766.08, +0.18% o→c); 10y yield +1bp to 4.649%. **The dollar rose the most in ~4 weeks.** A genuinely muted equity response to an upside inflation surprise. |
| **NVDA FY27 Q2** | Wed 08-26, post-close | **EPS $2.22, revenue $96.2B (+106% y/y)** — a blowout. NVDA gapped +6.3% Thursday open and closed **+8.74%** (209.66 → 227.98). **Then gave back −4.30% on Friday** (cpos 0.06), ending the week only **+1.32%**. |
| **Jackson Hole — Warsh's first keynote as Fed Chair** | Fri 08-28 | Warsh: inflation "too high", price stability "predominant focus", 2% PCE a firm target. **September rate-HIKE odds jumped to ~57%**; 2y yield to 4.35%. Markets rallied into and through the speech, **then reversed after midday**: SPY made the week's high at 775.29 and closed 769.35 — **cpos 0.15, −0.31% open-to-close**. QQQ cpos 0.15, IWM cpos 0.02. |

Daily SPY path: **−0.29 / +0.32 / +0.02 / +0.66 / −0.23**. The week's gain was made entirely on
Thursday's NVDA-led gap, and Friday took back a third of it.

**Pre-registration bookkeeping (this governs what §3 may accrue):** PCE is a Tier-1 macro print and
**accrues one observation to the macro arm** — the first since W33. The Warsh keynote is logged to the
**Fed-communication arm**, separately, on the same precedent W34 used for the FOMC minutes; it is not a
scheduled data release and must not be pooled with CPI/PPI/PCE/NFP/FOMC-decision observations.

### Regime trajectory (`scripts/regime_check.py --range 2026-08-24:2026-08-28`)

| Day | Label | ret5 | ret10 | dd15 | s1_standdown |
|---|---|---|---|---|---|
| Mon 08-24 | CHOP | −1.190% | −1.240% | −1.350% | False |
| Tue 08-25 | CHOP | −0.200% | −0.600% | −1.030% | False |
| Wed 08-26 | CHOP | −0.390% | −0.830% | −1.280% | False |
| Thu 08-27 | CHOP | **+1.110%** | −0.870% | −1.960% | False |
| Fri 08-28 | **CHOP** | +0.470% | −0.900% | −1.770% | False |

**Five-for-five plain CHOP, `s1_standdown` FALSE every session** — the flattest regime week in the
journal. `ret10` barely moved (−1.24% → −0.90%). Thursday was a **double near-miss** on the crash guard
(ret5 +1.11% vs the 1.5% leg, dd15 −1.96% vs the −2% leg); by Friday it was a clean miss on both legs.
The CHOP label has now held for **nine consecutive sessions** (since Tue 08-18).

### Vol-state overlay

| | Mon 08-24 | Tue 08-25 | Wed 08-26 | Thu 08-27 | Fri 08-28 |
|---|---|---|---|---|---|
| **VIX** | 15.85 | 15.45 | 15.21 | 14.51 | **14.43** |
| **VVIX** | 88.64 | 85.67 | 85.24 | 82.90 | 86.63 |
| **VVIX/VIX** | 5.59 | 5.54 | 5.61 | 5.71 | **6.00** |
| **SPY dealer gamma** | SHORT −1.284B | SHORT −503M | SHORT −964M | **AT FLIP** +21.7M | SHORT −615.8M |
| **QQQ dealer gamma** | SHORT −548M | ON FLIP −167.6M | SHORT −225.8M | **LONG +736.7M, pinned** | SHORT −218.9M |

- **VIX fell every session, closing at a 10-day low (14.43, −8.96% on the week)** — yet **VVIX/VIX rose all
  week and popped +5.1% on Friday** (5.71 → 6.00) as spot VIX made its low. Vol-of-vol richening against a
  falling spot VIX, on the day of the Warsh keynote, is a hedging-demand tell underneath a calm headline
  print. Vol-state only — never a direction.
- **Term structure: CONTANGO.** VIX3M/VIX = 17.48/14.43 = **1.212** Friday, a steep front-cheap curve. No
  backwardation at any point.
- **VRP FAIR all week, no premium-selling edge.** SPY IV30d fell 13.04% → 11.63%, tracking VIX; Friday's
  VRP **−0.27pp** (IV30d 11.63% vs realized30d 11.90%) reproduced exactly on an independent re-query.
  QQQ ran persistently negative (−4.18pp Friday, IV 16.87% vs realized 21.05%) — IV *cheap* to realized.
- **Dealer gamma flipped twice.** Thursday was the week's outlier: SPY sat exactly on its zero-gamma flip
  while **QQQ was cleanly long-gamma and pinned (+736.7M)** — the only long-gamma session of the week —
  and that is the session the NVDA gap was absorbed into. By Friday both were short again. Friday's
  reading was re-derived independently from the raw per-strike ladder and reproduces the nightly scan
  exactly (SPY −615.8M, cross ≈790; QQQ −218.9M, single-signed negative).

**Three tool defects were re-confirmed or newly found this week, and all three are recorded because each
one would have silently corrupted a figure in this report:**

1. **The `uw gex` `regime` field is corrupted in BOTH directions.** It printed `FULLY_NEGATIVE` for SPY on
   Friday while the ladder plainly carries positive strikes (772: +$99.7M). It had previously printed
   `POSITIVE` against a −1.28B total on 08-24. **The header's `total_gex` also disagrees in sign with the
   ladder sum** (−139.78M vs +45.6M). Derive the sign from the cumulative per-strike ladder up to spot,
   and nothing else.
2. **NEW — `uw historical vrp --date <past date>` returns a frozen `realised_vol`.** All five dates
   08-24→08-28 returned SPY 0.119 and QQQ 0.2105 — Friday's values — while the same-night reports
   recorded 12.30% (08-26) and 12.29% (08-27). **Historical VRP cannot be re-derived; only same-night
   figures are trustworthy.** The weekly VRP path above is therefore reconstructed from the nightly
   reports, not re-queried.
3. **NEW — `^VIX3M`/`^VIX9D`/`^VIX6M`/`^VXV` return only a single current-session snapshot** from the
   Yahoo chart API regardless of range parameters. **Only Friday's term structure is verifiable**; the
   Mon–Thu contango path cannot be reconstructed and is not claimed above.

**One genuine data gap, stated rather than estimated:** `%` of names above their **200dma is NOT
COMPUTABLE** — `prices.parquet` spans 2026-01-15→2026-08-28, about 155 trading days, short of the 200 a
true 200dma needs. (Above-50dma Friday: **52.9%**.) W34 quoted a 200dma figure for the S&P 500 from an
external source; it is not derivable from this repo's own data and is omitted here rather than carried.


### Sector leadership — **a near-total reversal of W34**

| W35 winners | | W35 losers | |
|---|---|---|---|
| XLC | **+1.43%** | XLV | **−1.98%** |
| XLK | +1.30% | XLI | −1.73% |
| XLF | +1.08% | XLE | −1.51% |
| XLU | −0.09% | XLRE | −1.33% |

*(all `week_context.py` series share the same window — no staleness flags)*

**Spearman rank correlation between W34 and W35 sector leadership: −0.434.** Last week's #1 (XLV, +4.33%)
is this week's #12 (−1.98%). Last week's #11 (XLK, −3.53%) is this week's #2 (+1.30%). XLE went 2 → 10.
SMH went 12 → 8 (−4.66% → −1.30%).

**W34 carry-forward item 4 is RESOLVED, and it resolved as the unwind.** The hard-asset rotation did not
persist:

| GLD | SLV | USO | UUP | IBIT | TLT | IEF | HYG |
|---|---|---|---|---|---|---|---|
| **−3.42%** | **−4.30%** | **−3.67%** | **+1.00%** | +0.50% | +1.01% | +0.03% | +0.16% |

Every leg reversed: gold, silver and oil down hard, **dollar up**, and gold-miner AU **−6.62%** after
+25.88% last week. Credit and duration again did essentially nothing — TLT +1.01%, HYG +0.16% — so for
the second week running **the bond market declined to ratify the equity narrative**, this time into a
hawkish Fed keynote that moved September hike odds to 57%.

### Breadth — the index rose while the median stock fell

| Measure | Universe | Reading |
|---|---|---|
| % of names up on the week | Common/ADR, ≥$50M ADV (n=**1,299**) | **38.6%** (median **−0.86%**, mean −1.14%) |
| Equal- vs cap-weight | S&P 500 | **RSP −0.44% vs SPY +0.47% → −0.91pp** |

**This is the exact mirror of W34**, when equal-weight *beat* cap-weight by +0.87pp on a down week. This
week cap-weight beat equal-weight by 0.91pp on an up week. Both weeks the mega-caps drove the divergence;
the sign of the index return simply flipped. **A narrow, mega-cap-led advance on deteriorating breadth.**

### Notable flow (0 signal)

Largest dark-pool premium: **NVDA $54.2B (154,491 prints)** — the week's standout, roughly 60% larger
than SPY's $33.9B — then SPY, **MU $28.0B**, QQQ $25.1B, **SNDK $21.2B**, MSFT $16.1B, IVV $15.8B,
VOO $14.4B, TSLA $13.6B, AAPL $12.9B. MU and SNDK printing at index scale for a **second consecutive
week** is the standing single-name concentration.

Clean single-name movers (Common/ADR, ≥$50M ADV):

- **UP** — CAPR +52.46%, ANF +36.15%, **OKTA +23.01%**, **CRM +22.39%**, ASST +19.32%, GAP +18.59%,
  **ESTC +16.26%**, **CRWD +13.78%**, **NOW +12.63%**, XMTR +12.59%
- **DOWN** — IESC −54.78%, VISN −45.94%, **DKS −26.27%**, DY −25.09%, AEHR −20.56%, AXTI −17.12%,
  AGX −16.72%, QBTS −16.67%, **BURL −16.40%**, LUNR −16.10%

**The up-list is an enterprise-software earnings cohort** (CRM, OKTA, NOW, CRWD, ESTC) and the
down-list is led by **retail dispersion** (DKS −26.3%, BURL −16.4% against ANF +36.2%, GAP +18.6%).
Mega-cap tech led: **MSFT +6.27%, META +5.11%, AAPL +3.35%, AMZN +3.02%** — while **NVDA managed only
+1.32% on a 106%-growth print** and SMH fell 1.30%. **Software over semis, inside an up-tape for tech.**

---

## 2. Validated Weekly Setups (SCORED — excess)

### `calls[]` is EMPTY. Nothing sized. **Sixth consecutive weekly review with no scored setup.**

`held_book.py --prior analyses/scan/2026-08-28/conviction_2026-08-28.json` reads **0 open / 0 closed**,
and that file's `book_state.positions=0` plus an empty `calls[]` in the 08-28 envelope confirm the empty
result is real rather than the known held_book EXIT-substring bug. The daily book has now been **flat for
15 consecutive sessions**.

Phase D (`risk-sizer`) was **vacuous** and `fundamentals-gate` was **correctly not spawned** — both run
only on names about to be sized.

### The regime cell that governs everything below

Tonight is **plain CHOP** (`s1_standdown=FALSE`). The pooled "CHOP" row must not be used — it collapses
plain CHOP with CHOP/REBOUND-THRUST and **OI_FADE's sign flips between them**. I recomputed the whole
table myself from `retro_harness.fire()`/`resolve()` rather than quoting the lanes:

| Lane | n rows | exit-days | mean excess | clustered mean | **t (exit-day)** | verdict |
|---|---|---|---|---|---|---|
| MOM_LONG | 354 | 24 | **−0.0266** | −0.0265 | **−2.51** | significantly NEGATIVE |
| MOM_SHORT | 282 | 24 | −0.0220 | −0.0177 | −1.93 | negative, marginal |
| OI_FADE | 344 | 23 | −0.0010 | −0.0009 | −0.13 | indistinguishable from zero |
| *(S2 — daily lane, not re-run weekly)* | 410 | 28 | +0.0007 | +0.0007 | +0.18 | — |
| *(S4 — daily lane, not re-run weekly)* | 417 | 28 | +0.0061 | +0.0060 | +1.30 | — |

For contrast, the **CHOP/REBOUND-THRUST** stratum reads OI_FADE **+0.0098** (n=148, 10 exit-days,
t=+1.31) and MOM_LONG −0.0309. Collapsing the two gives OI_FADE a misleading +0.0023.

**Every cell is under 30 exit-days and carries the invariant-6 correlated-draw caveat.** The only
statistically real number is MOM_LONG's negative excess — an argument *against* the near-52w-high basket,
not for anything.

### ⚠️ Lane-return arbitration — the momentum lane's excess figures were wrong and are not used

The `momentum` lane reported **MOM_SHORT plain-CHOP excess of +2.29% (n=216)** and **MOM_LONG −2.04%
(n=340)**, with no t-statistics and with "commands" that were placeholder pseudo-code rather than
runnable queries. **MOM_SHORT's sign is inverted.** My reproduction — which matches all five nightly
scans this week bit-for-bit — reads **MOM_SHORT −0.0220 (n=282, 24 exit-days, t=−1.93)**. The lane also
reported its MOM_LONG funnel as "185 → **20** after the h21 earnings gate"; the true count is
**185 → 180** (the gate cuts 5 names, not 165), and its own explanatory line ("88 blocked by earnings
≥ 2026-10-29") is self-contradictory, since a print on 10-29 falls *outside* a window ending 09-27.
**The lane's rankings were correct and reproduced exactly; its statistics and funnel counts did not.**
This is the standing "verify the lane's reported gate result yourself" failure mode, and it is the second
consecutive week a lane has handed back a figure that would have mis-scored its own regime-fit.

### OI_FADE — `NO_NAME_CLEARED`

**Zero candidates survive, for the second consecutive session, and the weekly horizon provably cannot
change that.**

Funnel (lane-reported, spot-checked): 5,370 tickers with OI rows → 3,616 with a full 5-day window
(1,754 dropped fail-closed) → 1,296 past the tiny-base floors → top-15 by `oi_rel_build`
(DCI, FTEC, HONA, MBUU, IRD, DKS, MNRO, ZURA, DYN, NBIZ, UHALB, EYPT, BZ, BTCZ, TUYA) → **0 survivors**:
−8 on the $50M/$5 liquidity floor, −3 ETPs (FTEC, NBIZ, BTCZ), −1 listing age (HONA, 51 trading days),
−2 persistence >0.85 (DCI 0.991, DKS 1.143), −1 on invalidation (BZ: 80.4% of the 5d net on 08-27 alone
**and** `last_call_net` negative on 08-28).

**The weekly-horizon extension is a provable no-op this week.** Every one of the 15 names reports between
10-29 and 12-03 — outside *both* `hz_end(10)=2026-09-12` and `hz_end(21)=2026-09-27`. The earnings gate
is the only horizon-dependent gate, and it never engages; liquidity, ETP, listing-age, persistence and
concentration are all horizon-independent. **The h10 and h21 top-15 sets are bit-identical**, so the
weekly disposition equals the daily one by construction rather than coincidence. That is a cleaner
statement of the null than any prior week has produced.

**The selection-rule mismatch is total again — and it is worse than a two-way gap.** I verified this
directly rather than accepting the lane's numbers:

- **Harness raw-rule top-15** (`fire(T,'raw')`): BABA, SPCX, INTC, NVDA, PBR, SOFI, META, WULF, GOOGL,
  AAPL, WMT, TSLA, PCG, IREN, ASST — **overlap with the live cohort: 0/15.**
- **Harness live-rule top-15** (`fire(T,'live')`): **EMPTY.** The variant that grades the live rule
  returned no names at all on 08-28.
- The lane separately reports a **third** construction (liquidity/ETP/age/earnings filtered *before*
  ranking by `oi_rel_build`) that overlaps the live cohort by 1 name and the raw list by 1 name.
  **Filtering order alone produces a nearly-disjoint third top-15.**

The raw list is once again **pure mega-cap beta** (BABA, INTC, NVDA, META, GOOGL, AAPL, WMT, TSLA) — the
documented artifact. This is the **8th+ consecutive period** the mismatch has been carried undecided, and
it is a standing audit item that has now been deferred past its own deadline.

*(Minor discrepancy recorded: the lane's raw top-15 listed VALE and MARA where `fire()` returns SPCX and
NVDA — 13/15 agreement. The lane re-implemented the query instead of calling `fire()`. It does not change
the 0/15 overlap conclusion.)*

### MOM_LONG — `BASKET_WATCH` (never sizes)

Funnel, reproduced independently: 1,871 liquid names → 392 within 5% of the 52w high → **185** after the
`issue_type` Common/ADR filter (207 ETPs cut at source; **0 NULL `issue_type`**, so no fail-closed drops
this week) → **181** at h10 → **180** at h21.

Harness top-15 at h21: ESTC, TEAM, DINO, ZETA, FRSH, DK, MPC, GEN, BOX, APGE, CRNX, VLO, SEIC, DBRG, TECH.

**I Yahoo-verified all fifteen with `chart.py --52w`, and cut the top-ranked name:**

| | ESTC | TEAM | DINO | ZETA | FRSH | DK | MPC | GEN | BOX | APGE | CRNX | VLO | SEIC | DBRG | TECH |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yahoo pct_52w_range | **87.7%** | 96.7% | 99.2% | 98.2% | 98.2% | 97.6% | 99.9% | 98.0% | 92.0% | 100.0% | 99.9% | 99.7% | 98.6% | 99.3% | 99.1% |
| off high | **−7.5%** | −2.3% | −0.4% | −1.0% | −0.9% | −1.6% | −0.1% | −0.9% | −3.3% | −0.0% | −0.1% | −0.2% | −0.5% | −0.3% | −0.4% |

**ESTC is a FALSE LONG and is CUT.** The screener ranked it **#1** with `close/week_52_high = 1.04` —
close *above* the recorded high, the out-of-range signature. Its true Yahoo high is **108.00, set on
08-28 itself**; at 99.91 it sits 7.5% below, and `0.95 × 108.00 = 102.60` means **ESTC fails the lane's
own gate on correct data.** This is the `pct_52w_range` defect firing in its long-leg mirror: the daily
scan had it as WATCH_FLAGGED, and at the weekly horizon it is a hard fail. The other fourteen are
genuine — eleven set their 52-week high this week.

**Sector concentration BREACHES the 33% cap.** Technology is 6/15 = **40.0%** (Energy 26.7%, Healthcare
20.0%). After cutting ESTC it is 5/14 = **35.7% — still a breach.** And the tilt is toward **XLK, this
week's #2 sector**, so for the second consecutive week the basket is **materially a sector-momentum bet
in disguise** — last week it was Healthcare/Energy mirroring W34's winners, this week it is Technology
mirroring W35's. That the tilt *rotates to follow the winning sector* is itself the finding: the screen
is picking up sector beta, which is exactly the risk invariant 1 exists to catch.

Sizing is barred regardless: plain-CHOP excess **−0.0266, t=−2.51, p=0.012** — the one lane with a
*significantly negative* excess in this cell — plus the standing DURABLE-N bar and basket-only status.

**TECH carries a prior disposition:** it was double-filed by the 08-27 lane into both the near-low and
the deal-pinned near-high lists; the orchestrator ruled it belongs only in the deal-pinned near-high
list. My reproduction confirms it is at 99.1% of range (near-HIGH), so MOM_LONG is the correct lane —
but it remains **deal-pinned** and would not size on that ground alone.

### MOM_SHORT — `BASKET_WATCH` (never sizes)

Funnel: 1,871 → 86 within 2% of the 52w low → **24** after `issue_type` (62 ETPs cut; 0 NULL) → **23** at
both h10 and h21. The lane's funnel here was correct.

Harness top-15: VISN, INIO, FRVO, TLN, ESAB, CRUS, NRG, CMS, VICI, TJX, OLN, PEG, APTV, ONON, BEPC.

**Crash guard NOT fired** — `s1_standdown=FALSE` on all five sessions. ret5 +0.470% is 2.03pts short of
the +2.5% up-thrust bar, and dd15 −1.77% fails the ≥2% dip precondition, with the dip leg (ret5 < −2%)
the wrong sign entirely. The lane ran ungated and still sizes nothing on baseline grounds alone
(**−0.0220, t=−1.93** in this cell; harness pooled −0.0130).

**MIDD stays cut, and the diagnosis from 08-28 holds.** The lane re-surfaced it and this time failed it
correctly: screener range 110.82–180.13 vs Yahoo **89.16–148.55**, both legs ~1.22× Yahoo's — an
unadjusted corporate action, not a one-sided stale print. At 112.75 it is 1.26× its true 52w low, well
outside the 1.02× gate.

**On the "10 stale names" the lane flagged: that framing is wrong and I am not carrying it.** For names
like TJX (screener low 134.17 vs Yahoo 133.55) and APTV (45.28 vs 44.88), the screener's `week_52_low`
simply has not yet absorbed a low set *that same session* — which the 08-28 conviction independently
recorded as **genuine fresh 52-week lows**. That lag makes the screener understate how extended the name
is, i.e. it is **conservative and cannot manufacture a false short**. It is the opposite failure mode
from MIDD's, and conflating the two would retire good candidates for the wrong reason.

**The sector composition is the notable feature:** Utilities is 6 of 15 (FRVO, TLN, NRG, CMS, PEG, BEPC)
= **40%, a breach of the same 33% cap.** For a short leg in a week when XLU was roughly flat (−0.09%)
and the hard-asset/defensive trade unwound, that is a concentrated bet on one rate-sensitive sector.
**And the lane remains structurally blind to the week's actual dispersion** — DKS −26.3%, BURL −16.4%,
DY −25.1% are nowhere near 52-week lows, so the screen cannot see the retail and services breaks that
were the week's clearest single-name damage.

---

## 3. Weekly Technicals — PRE-REGISTERED (documented, 0 points, NOT sized)

**Reproducibility basis, stated explicitly because last week's was not:** every figure below is computed
from `data/weekly_features.parquet` restricted to **full 5-day weeks only (n=26)**, with the forward
return defined as `w_close[t+1]/w_close[t] − 1`. The exact predicate for each arm is given in the row.

| Feature | This week | Would signal | Status | Pre-reg bar |
|---|---|---|---|---|
| **SPY INSIDE WEEK** (`inside_week`) | **FIRED — the first and only one in the panel, 1/26.** H 775.29 < 776.78, L 762.08 > 762.04 (by 4¢) | Compression / pending range expansion | PRE-REGISTERED | PR-WT — **zero prior observations. No forward evidence exists in either direction.** |
| **IWM close_pos 0.017** (`lower_low & close_pos<0.15`) | **FIRED.** Lowest weekly close position in the 26-week panel (0th percentile), 0.81 body | Capitulation / trend continuation down | PRE-REGISTERED | PR-WT — fires 3/26; **2 prior resolved: −1.71%, +4.01%** (mean +1.15%). n=2, non-informative |
| **QQQ failed follow-through** (`~follow_through`) | **FIRED.** Made a lower low, still closed +0.95% | Trend indecision | PRE-REGISTERED | PR-WT — fires 12/26; **11 resolved: mean −0.52%, median −1.60%** |
| **SPY failed follow-through** (`~follow_through`) | **FIRED.** cpos 0.55, body 0.35 | Trend indecision | PRE-REGISTERED | PR-WT — fires 7/26; **6 resolved: mean +0.43%, median +0.52%** — opposite sign to QQQ's same arm |
| **reversal-after-catalyst — Tier-1 macro arm** | **DID NOT FIRE.** PCE (Wed 08-26) came in hot (3.7% vs 3.6%) and SPY closed **+0.02%**; no reversal | The event-conditioned feature | PRE-REGISTERED | PR-WT — **accrues 1 macro-arm observation** (first since W33), recorded as a *null* reaction |
| **reversal-after-catalyst — Fed-communication arm** | **FIRED.** Warsh keynote Fri: SPY rallied to the week's high 775.29, closed 769.35, **cpos 0.15**; QQQ cpos 0.15, IWM cpos 0.02 | Bearish arm of the event-conditioned feature | PRE-REGISTERED | PR-WT — **separate arm**, same precedent W34 used for the FOMC minutes. 2 obs total. Must not be pooled with the macro arm |
| **repair-gap tracker** | **DIVERGED for the first time.** QQQ narrowed −3.67% → −3.27%; SPY −1.37% → −0.90%; **IWM widened −1.68% → −3.06%** | Failed repair = distribution at the highs | PRE-REGISTERED | PR-WT — first *within-tracker divergence* since W31 |
| **index structure divergence** | **FIRED, 2nd obs.** SPY inside / QQQ lower-low-but-up / IWM lower-low-and-closed-on-it | Damage rotating down the cap scale | PRE-REGISTERED | PR-WT — new arm from W34, **2 obs** |
| candle-pattern arms (outside / hammer-hanging / star) | **None fired** on any of the three | Nothing this week | PRE-REGISTERED | PR-WT — SPY's arms remain unreachable at this accrual rate |

### W34's fired arms, resolved

- **QQQ bearish OUTSIDE week → bounced again.** W34 flagged that the historical evidence pointed *opposite*
  to the pattern's own narrative. It did so again: QQQ +0.42% the following week. On the full-5-day panel
  the arm now has **5 resolved observations: −1.96, −1.74, +2.31, +2.69, +0.42 → mean +0.34%, 3 up / 2
  down.** The "bearish reversal" reading remains unsupported, and the contradiction stands unresolved —
  as it should, since resolving it by narrative is exactly what this layer forbids.
- **SPY failed follow-through + cpos<0.30 + lower_low → +0.47%.** Arm now 2 resolved, both positive.

### ⚠️ A discipline failure in this layer, and it is the most important thing in §3

**W34's §3 base rates do not reproduce, under any predicate or panel basis I tried.** W34 reported the
SPY arm as *"6 prior obs: −1.50, −2.07, −2.23, +3.43, +0.57, +1.10"* and the QQQ outside-week arm as
*"−1.96, +2.89, +2.31, +0.86 (mean +1.03%)"*. Testing three predicate variants × two panel bases (all
32 weeks vs full-5-day-only) yields **six candidate value sets, and not one matches either list** — only
a single value (+0.57) appears anywhere in mine.

The cause is that **the arm predicates and the panel basis were never written down.** An arm described in
prose as "failed follow-through, close_pos<0.30 + lower_low" fires 2/26 here but was reported as 6
observations; "QQQ outside week" gives −1.96/−1.74/+2.31/+2.69 on the 5-day panel, not W34's list.

**This matters more than any individual number.** The entire justification for Layer 3 is that features
are *pre-registered* — fixed in advance so that accrual toward the PR-WT bar is honest. **An arm whose
definition is not recorded cannot accrue anything**, because next week's run will re-derive a different
base rate and nobody will notice. Layer 3 has been running for five weeks in this state.

**Action, carried as a hard item:** each PR-WT arm needs a written predicate (exact column expression),
a fixed panel basis, and a fixed forward-return definition, stored in the repo rather than restated in
prose each week. Until that exists, **all §3 base rates prior to this week should be treated as
non-auditable**, and this week's are the first that are reproducible from the stated basis. This does
not touch Layers 1–2 or any sizing decision — nothing in §3 has ever been scored, which is precisely why
the defect survived five weeks undetected.

Panel: **32 weeks / 26 full 5-day weeks** against a ≥2-year, ≥30-obs-per-arm bar — roughly a quarter of
the minimum history.

---

## 4. Carry-forward

### How last week's Layer-2 calls did

**W34 scored nothing** (`calls[]` empty), so there is nothing to grade. **Six straight weekly reviews
with no scored setup; the daily book is flat for 15 sessions.**

The discipline was again close to costless: SPY +0.47%, QQQ +0.42%, IWM −1.40% Fri→Fri, with **38.6% of
the liquid spine up and a median stock at −0.86%**. A flat book beat the median stock for the second
week running. But the honest counterfactual is unchanged and now in its **fourth** consecutive week:
**the week's money was in dispersion** — CRM +22%, OKTA +23%, ANF +36% against DKS −26%, DY −25%,
IESC −55% — and **no validated lane in this engine addresses dispersion.** That is a scope fact, not a
miss, and its persistence is itself the observation.

### The regression gate: three lanes below baseline, and it is data, not decay

`retro_harness.py --all --oi-variant both` on the 98-day panel:

| Lane | Recorded baseline (08-22, 93d) | Pooled now (98d) | Δ |
|---|---|---|---|
| MOM_LONG | −0.0118 (n=1213) | −0.0117 (n=1279) | **above** |
| MOM_SHORT | −0.0138 (n=830) | −0.0130 (n=874) | **above** |
| OI_FADE | +0.0013 (n=1177) | **−0.0018** (n=1252) | **−31bp** |
| S2_dp_revert | +0.0018 (n=1269) | +0.0013 (n=1338) | −5bp |
| S4_pcr_fade | +0.0024 (n=1304) | +0.0021 (n=1379) | −3bp |

**Isolation check (a) is trivially satisfied: no lane or harness code has changed since the baseline was
adopted.** The last two commits touching `scripts/` are both from 2026-08-22 — the baseline-adoption day
itself — and the working tree is clean. Any drift since is data by construction.

**Isolation check (b), the exit-day cohort split, is decisive.** Splitting every harness row on its
**exit-day** (the entry-date split is the wrong unit — no entry from this week has matured yet):

| Lane | Baseline cohort (exit ≤ 08-21) | vs recorded | **Increment (exit 08-24→28)** |
|---|---|---|---|
| MOM_LONG | −0.0122 (n=1209, 83 exit-days) | −4 rows | −0.0020 (n=70, **5 exit-days**), base **0.00** |
| MOM_SHORT | −0.0137 (n=828, 63) | −2 rows | −0.0003 (n=46, **5**), base **1.00** |
| **OI_FADE** | **+0.0013 (n=1177, 79)** | **BIT-IDENTICAL** | **−0.0500 (n=75, 5)**, base **1.00** |
| S2_dp_revert | +0.0016 (n=1264, 88) | −5 rows | −0.0046 (n=74, 5) |
| **S4_pcr_fade** | **+0.0024 (n=1304, 88)** | **BIT-IDENTICAL** | −0.0032 (n=75, 5) |

**The baseline cohort reproduces — OI_FADE and S4 bit-identically.** The entire pooled drift is a
**5-exit-day increment with a pinned base**: SPY fell across **100%** of the h10 windows ending 08-24→28
(base 0.00 for the long lane, 1.00 for both short lanes). Per-day, OI_FADE reads −0.0633 / −0.0611 /
−0.0607 / −0.0557 / −0.0095 with hit pinned at **exactly 0.33 on the first four days and n=15 every
day** — the signature of **one cohort of 15 names graded on four overlapping windows, not four
independent draws**. Friday breaks the pattern (hit 0.53), which is the dilution the 08-28 scan
pre-registered as the start of the unwind.

**Conclusion: OI_FADE's −31bp is not decay, and the baseline must NOT be re-pointed to the 98-day panel** —
re-baselining on a 5-exit-day pinned-base cohort would bake one draw into the reference, the exact error
CLAUDE.md's 2026-08-22 worked example was written to prevent. The lane is already advisory-only, so
nothing about sizing changes either way.

*(Second-order note: MOM_LONG lost 4 rows, S2 5, MOM_SHORT 2 from their own baseline cohorts — the Yahoo
retraction non-idempotency, flagged in the 08-28 conviction for MOM_LONG and here confirmed to reach S2
and MOM_SHORT as well. OI_FADE and S4 were untouched. The audit book is not append-only unless the
ledger restores it.)*

### Items resolved this week

1. **W34 item 4 — the hard-asset rotation — RESOLVED as the unwind.** Gold −3.42%, silver −4.30%, oil
   −3.67%, AU −6.62%, dollar +1.00%. XLV and XLE, W34's #1 and #2, are W35's #12 and #10. Sector
   leadership rank correlation **−0.434**.
2. **W34 item 3 — the Tier-1 cluster — landed.** PCE (muted, +0.02%) and NVDA (+106% revenue, gapped
   +8.7%, then gave back 4.3% Friday to finish +1.32% on the week). Warsh's keynote moved September
   hike odds to ~57% and produced the week's cleanest reversal.
3. **W34 item 6 — BULL** did not reappear in any OI_FADE cohort; the lane returned zero candidates.
4. **W34 item 2 — the OI_FADE selection-rule mismatch was carried AGAIN, for an 8th+ period,** and the
   decision deadline (the 08-22 audit) has now passed twice.

### What rolls into next week

1. **`/calibration-audit` is overdue — it was due TODAY, 2026-08-29, and CLAUDE.md still says so.** This
   is the top item. The book has 485 call rows and 561 lane_status candidate rows accumulated across all
   envelopes; the suppressed cohort crossed into PROVISIONAL last cycle (21 lane-periods, −1.74%,
   p=0.008) while the call book added almost nothing. **Count distinct exit-days, not rows.**
2. **Decide the OI_FADE selection-rule mismatch at that audit — this is the 8th+ deferral.** It is now
   demonstrably worse than a two-way gap: the raw rule returns a mega-cap beta list (BABA/INTC/NVDA/
   META/GOOGL/AAPL/WMT/TSLA), the harness's live variant returns **nothing at all**, and the lane's
   third construction — same rule, different *filter order* — yields a near-disjoint top-15. **Three
   constructions, ~0 mutual overlap.** Either the harness adopts the live screens and re-baselines, or
   the prior is formally recorded as inherited/discounted. It should not be carried a ninth time.
3. **Write down the PR-WT arm definitions** (§3). Until each arm has a stored predicate, panel basis and
   forward-return definition, Layer 3 accrues nothing auditable — and it has been in that state for five
   weeks.
4. **A dense Tier-1 cluster sits inside any 2–4-week hold opened now:** **NFP 09-04, PPI 09-10, CPI
   09-11, FOMC decision + dot plot 09-15/16**, then **PCE 09-30** and the **FY2026 appropriations
   deadline 09-30** (shutdown risk). With September hike odds at ~57% after Warsh, the FOMC is a live
   two-sided event rather than a formality.
5. **Watch whether IWM's break extends.** It is the only index that confirmed last week's direction, it
   closed at the panel's lowest weekly close position, and its repair-gap widened while SPY's and QQQ's
   narrowed. If small-caps keep breaking, MOM_SHORT will finally get candidates in something other than
   Utilities — the roster is currently **40% Utilities**, a 33%-cap breach on a lane that never sizes.
6. **MOM_LONG's sector tilt rotates to follow the winning sector** — Healthcare/Energy in W34, Technology
   (40%, cap breach) in W35. Two consecutive weeks is a pattern worth pre-registering as a lane-quality
   check rather than re-noting each week.
7. **ESTC is the live example of the long-leg `pct_52w_range` trap** and should be re-checked Monday: the
   screener will keep ranking it #1 until its `week_52_high` absorbs the 108.00 print from 08-28.
