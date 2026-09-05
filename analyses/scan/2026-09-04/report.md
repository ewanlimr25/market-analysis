# Market Scan — 2026-09-04

## Regime & Verdict

- **Regime: CHOP** (plain) · ret5 **+0.110%** · ret10 **+0.580%** · dd15 **−0.510%** · `directional_tradable=true` · `s1_standdown=false`
  — from `scripts/regime_check.py --date 2026-09-04`, **not stale**: the truth set was rebuilt tonight and reaches the trade date. Reproduced independently from a live Yahoo pull (ret10 = 770.19/765.72 − 1 = +0.584%).
- **Last night's near-flip resolved downward.** On 09-03 ret10 was +1.386%, 11bp under the +1.5% UPTREND threshold and flagged as one session from changing every lane's `regime_fit`. Tonight it reads **+0.580%**. Two independent causes, both verified: the 10-session anchor rolled from the 08-20 close (762.60) to the 08-21 close (765.72), a higher base worth ~40bp on its own, and 09-04 itself was down. **The label did not flip; it moved away from the line.**
- **Tape:** SPY **770.19 (−0.385%)** · QQQ **718.96 (+0.180%)** · IWM **296.01 (+0.278%)** · VIX **14.53 (+1.47%)**.
- **Breadth:** 3,656 Common/ADR with valid prev_close → **1,908 adv / 1,664 dec, median +0.106%**. By cap: large (≥$10B) **−0.429%** (348/556), mid **+0.080%**, small **+0.498%** (995/612).
- **Vol-state:** VIX 14.53, **LOW tercile**. Dealer gamma **SHORT/negative on both SPY and QQQ** — a flip from 09-03's long-gamma read. Derived by hand from `total_gex` + the per-strike ladder; see Risk.
- **Bottom line: No directional edge today. Twentieth consecutive flat session.** No lane sizes. The directional book is empty by construction.

## Directional Book (excess-scored)

**EMPTY.** No lane sizes. `risk-sizer` was not spawned — with zero sized candidates Phase D is vacuous — and `fundamentals-gate` was correctly not spawned, since it runs only on names about to be sized.

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

**Open call rows: 0.** Held-book reconciliation off the 09-03 conviction file read 0 open / 0 closed, verified against `book_state.positions == 0` in the source file rather than trusting the bare empty result (the known EXIT-substring bug). The five OI_FADE rows that matured 08-28/09-02 remain resolvable at the **2026-09-05 audit**.

---

## The headline: OI_FADE_LIVE's pre-registered re-check has fired, and it fired the *other* way

This is the most consequential number tonight and it cuts directly at the evidence the lane was stood down on.

The 2026-08-29 stand-down pre-registered two outcomes at the 30-`lane-exit-day` bar. **Outcome 2 has fired.**

`OI_FADE_LIVE` is now at **34 complete `lane-exit-day`, zero partial** (every one resolved 15/15 — no partial-window trap to correct for tonight):

| cohort | k (`lane-exit-day`) | mean | t | p (iid) |
|---|---|---|---|---|
| at stand-down (08-29) | 29 | −0.0093 | — | **0.028** |
| 09-02 | 32 | −0.0080 | −2.141 | 0.0402 |
| 09-03 | 33 | −0.0076 | −2.079 | 0.0457 |
| **tonight (09-04)** | **34** | **−0.0065** | **−1.730** | **0.0929** |

**The full trajectory is monotone decay across seven consecutive units:**

| k | thru | mean | t | p |
|---|---|---|---|---|
| 28 | 08-27 | −0.0101 | −2.468 | 0.0202 |
| 29 | 08-28 | −0.0093 | −2.317 | 0.0280 |
| 30 | 08-31 | −0.0094 | −2.406 | 0.0227 |
| 31 | 09-01 | −0.0087 | −2.293 | 0.0290 |
| 32 | 09-02 | −0.0080 | −2.141 | 0.0402 |
| 33 | 09-03 | −0.0076 | −2.079 | 0.0457 |
| **34** | **09-04** | **−0.0065** | **−1.730** | **0.0929** |

**It no longer survives BH(0.10)** across the three OI variants — the exact test the stand-down cited:

| rank | variant | p | BH threshold | verdict |
|---|---|---|---|---|
| 1 | OI_FADE_RAWPOOL | 0.0148 | 0.0333 | **survives** |
| 2 | **OI_FADE_LIVE** | **0.0929** | 0.0667 | **fails** |
| 3 | OI_FADE (raw rank, full pool) | 0.5064 | 0.1000 | fails |

**Three further checks, all pointing the same way:**

1. **The h10 window-overlap correction kills it outright.** Newey-West (L=9, for the 9/10 shared days in overlapping h10 windows): **t=−1.057, p=0.298**. The stand-down write-up already conceded NW "roughly halves" these t-stats; at k=34 that leaves nothing.
2. **The crypto-robustness claim has decayed too.** The 08-29 record's key argument was that `LIVE`, unlike the raw pool, did *not* depend on a few names: ex-MSTR/CELH/MARA it read **−0.0070**. Tonight the same cut reads **−0.0045, p=0.2182**. Meanwhile `RAWPOOL` ex-those-three collapses from −0.0133 to **−0.0042, p=0.3421** — so the 08-29 diagnosis of *RAWPOOL* was right and still is; it is `LIVE`'s own robustness that has eroded.
3. **The mechanism matches the pre-registration exactly.** Outcome 2 said the p=0.028 would prove to be "the 5-exit-day pinned-base increment leaking in." The maturity-edge cohort's `base` has unpinned from **1.00 → 0.80** for shorts, and `LIVE`'s exit>08-21 mean is **−0.0024** against **−0.0081** on the baseline cohort. **Five of the last ten exit-days are positive**, and the newest alone (09-04, **+0.0315**) moved p from 0.0457 to 0.0929.

**What this does and does not license.** The lane's *sign* is still negative on every cut. What has gone is the **significance** — the specific thing the stand-down rested on ("significantly negative and survives BH(0.10)"). Per the pre-registration, outcome 2 means **the lane returns to advisory**. That is the **2026-09-05 audit's call to make, not this scan's**; the audit is propose-only and due tomorrow. Recorded here as its headline input. **CLAUDE.md and the lane's status are deliberately left unchanged tonight** — a scan does not re-rate a lane.

⚠️ One favourable note for data quality: the three completed exit-days that a scan can compare night-over-night — 08-31 (−0.0102), 09-01 (+0.0098), 09-02 (+0.0136) — reproduced **bit-identically** against 09-03's report. The non-idempotent vendor drift that visibly moved a *completed* unit last night did **not** recur.

---

## Regression gate

**No lane or threshold changed tonight**, so this is a data-only re-read. `retro_harness.py --all --oi-variant both`, **103 panel days**, prices spine **2,443** (28 UNPRICED, failed closed):

| lane | n | mean_exc | hit | base | hit−base | median |
|---|---|---|---|---|---|---|
| MOM_LONG | 1348 | −0.0118 | 0.43 | 0.57 | −0.143 | −0.0137 |
| MOM_SHORT | 939 | −0.0123 | 0.42 | 0.41 | +0.010 | −0.0105 |
| OI_FADE | 1327 | −0.0014 | 0.53 | 0.41 | +0.128 | +0.0062 |
| **OI_FADE_LIVE** | **510** | **−0.0065** | 0.49 | 0.53 | −0.035 | −0.0009 |
| OI_FADE_RAWPOOL | 510 | −0.0133 | 0.48 | 0.53 | −0.047 | −0.0032 |
| S2_dp_revert | 1405 | +0.0011 | 0.50 | 0.53 | −0.030 | −0.0001 |
| S4_pcr_fade | 1453 | +0.0014 | 0.50 | 0.53 | −0.034 | −0.0004 |

**Isolation check by EXIT date** (the harness has no exit-date flag; imported it and split the cohort by hand):

| lane | recorded baseline | tonight, exit ≤ 08-21 | maturity edge (exit > 08-21) |
|---|---|---|---|
| MOM_LONG | −0.0118 (n=1213) | −0.0122 (n=1208) | −0.0080 (n=140), base **0.20** |
| MOM_SHORT | −0.0138 (n=830) | −0.0137 (n=826) | −0.0021 (n=113), base **0.76** |
| OI_FADE | +0.0013 (n=1177) | **+0.0013 (n=1177) — bit-exact** | −0.0222 (n=150), base **0.80** |
| S2 | +0.0018 (n=1269) | +0.0021 (n=1257) | −0.0079 (n=148), base 0.50 |
| S4 | +0.0024 (n=1304) | **+0.0024 (n=1303) — exact** | −0.0079 (n=150), base 0.50 |

**No regression. Do not re-baseline.** Every baseline cohort reproduces (MOM_LONG's 4bp is the one drift and it is stable night-over-night). The whole full-panel move is the maturity edge.

**The base pinning is unwinding, and it remains an h10-only phenomenon.** Long h10 base has gone 0.00 → **0.20** and short h10 base 1.00 → **0.76–0.80** as more windows mature, while **S2 (h3–5) and S4 (h5–10) sit at 0.50, never pinned at all** — the same control that made the point on 09-03, holding a second night. This unwinding is precisely what the OI_FADE_LIVE section above is measuring.

**Row-count attrition has stopped and reversed.** Against 09-03 every lane *gained* rows (MOM_LONG 1320→1348, MOM_SHORT 912→939, OI_FADE 1297→1327, S2 1375→1405, S4 1423→1453) on the added panel day. The vendor-feed churn that was dropping rows nightly has settled.

### Dormant tests — reported, not re-derived

Per the standing rule, these are waiting on their gate **firing**, which is a regime event with no schedule:
- **Crash guard:** tonight's harness reports **20/103 guard-days** — unchanged, because no guard-day has fired since 08-07. Still 20 guard-days / −0.58% / p=0.212. **Dormant, not accruing.**
- **Fundamentals veto:** VETO n=15 / −2.28%, CONFIRM n=23 / −1.21%, unchanged since 08-15. **Dormant.** Not re-derived.

---

## Vol Book (non-directional)

Delta-neutral, advisory, quoted net of cost, zero directional points.

### 0DTE-VRP — STAND ASIDE on both SPY and QQQ

**Dealer gamma flipped SHORT on both indices overnight.** I arbitrated the raw ladder myself because the two Phase-B agents disagreed on the near-money band:

| | `total_gex` | ladder (50 strikes) | near-money ±1.2% | CLI `regime` | `zero_gamma_level` | derived |
|---|---|---|---|---|---|---|
| **SPY** | **−1,169,874,208** | 745–794, sum −901.6M | n=19, 10+/9−, **net −793.4M** | FULLY_NEGATIVE ✅ | **null** (uncomputed) | **SHORT / negative** |
| **QQQ** | **−237,296,111** | 697–740, sum **+32.5M** | n=21, 14+/7−, **net −2.8M** | **POSITIVE** ❌ | **243.37** vs a 697–740 ladder ❌ | **SHORT / negative** |

- **SPY is decisively short gamma** and the field agrees for once — the ATM 770 strike alone carries **−904.1M**, dwarfing everything else in the book. Note `zero_gamma_level` came back **null**, so the flip level that misled the vol-book lane on 09-03 was not even available tonight.
- **QQQ is a knife-edge, and both agents overstated it.** `total_gex` is negative, but the displayed ladder sums **positive (+32.5M)** and the near-money band nets only **−2.8M on 14 positive vs 7 negative strikes** — the negative sits *outside* the 697–740 window. The honest read is "negative on the full book, balanced near spot," not the decisive short-gamma both lanes reported (they quoted −6.3M and −24.3M for the same band).
- **`uw gex` field corruption is now 5 consecutive nights**, tonight on QQQ; `zero_gamma_level` garbage on QQQ is 4 consecutive nights.
- **`zerodte_setup.py` is confirmed doing the documented wrong thing, live.** Its own `net_gex_0_45d` for QQQ computed **−3,303.24 (negative)** and it still emitted `dealer_gamma_regime: LONG, sell_premium: true` — because it trusts the corrupted CLI `regime` field over its own arithmetic. **That is a script that sells premium into a short-gamma tape.** Overridden to `size_scalar = 0.0`.

**Verdict: STAND ASIDE both.** The gamma leg alone disqualifies the sleeve — short gamma is the trend-acceleration / unsampled-left-tail state this book cannot underwrite. The VIX-bucket arithmetic is moot but recorded: VIX 14.53 is **LOW tercile**, whose LOW-bucket gross means (SPY 0.218%, QQQ 0.353%) net to ~0.118% / ~0.253% after the 0.10% assumed round-trip. The standing structural objection is unchanged and is exactly illustrated tonight: **`zerodte_setup.py` stratifies by VIX tercile only, never by gamma regime**, so no conditional statistic exists for tonight's actual (LOW-VIX × short-gamma) state.

### Earnings IV-crush — a new and more mechanical form of the bracketing-expiry trap

**Every `implied_move_perc` tonight is unusable, not merely a floor.** Three names — AEO, ODD, KR — return `front-end-iv-ratio` with **`near_dte_actual = 0`**: the CLI is pulling *today's* 0DTE contract (no catalyst, near_iv 710%–2,350%) as the "near" leg for names whose true bracketing expiry is days out. This is stronger than the 09-03 AEO case, where simply no expiry preceded the print; here a deep bracketing expiry **exists and is ignored**.

| Ticker | Print | Bracketing expiry (contracts) | Next leg | Raw `implied_move_perc` | ATM-straddle rebuild | Verdict |
|---|---|---|---|---|---|---|
| **AEO** | 09-09 | 09-11 (**2,576**) | 09-18 (405) | **1.58% — unusable** | **14.63%** | Advisory sell-vol. Cross-checks to 09-03's independently-derived 13.8% (1.06×) |
| **ODD** | 09-09 | 09-11 (168) | 09-18 (74) | **2.67% — unusable** | **21.57%** | Advisory; wing to 21.6% |
| **KR** | 09-11 | 09-11 (395) | 09-18 (178) | **0.61% — unusable** | **5.64%** | ⚠️ print lands **on** the expiry date — confirm KR reports pre-market or the bracket misses the move entirely; treat 5.6% as a lower bound |
| **JMKE** | 09-09 | 09-18 (210) | 10-16 (30) | 9.51% | **12.13%** (1.28×) | Cleanest book of the cohort; ratio sits in the documented 1.2–1.4× band (TPR 1.35×, MDT 1.44×) |
| **SUNB** | 09-09 | 09-18 (155) | 10-16 (118) | 16.79% | ATM put quote **missing**; synthetics give 11.4%/12.0% — *below* raw, reversing every other name | **Caution, size down** — one-sided illiquid ATM leg, a data-quality anomaly not a crush read; wing to the higher (16.8%) |
| SHOE | 09-10 | 09-18 (**17**) | — | 16.8% | ~21.3% | **SKIP** — contract count has fallen into the same thin-book class as ODD's 09-03 skip (16); the ~1.3–1.7× internal disagreement persists but the book is too thin to trust either number |
| ZUMZ | 09-10 | 09-18 (**6**) | — | — | — | **SKIP** — thin |
| ANIX | 09-09 | none brackets the print | 10-16 (4) | — | — | **SKIP** |
| MNY | — | — | — | 170.96% | — | **EXCLUDE** — impossible; no IV data |
| YRD | — | — | — | 136.1% | — | **EXCLUDE** — no tradable book |

The `iv_rank ≥ 80` gate excludes 30 names in the 40–80 band, notably CPRT (77.4), CASY (76.8), CNM (75.8), ADBE (68.8), ORCL (62.4).

---

## Watch / Stood-down

### MOM_SHORT — watch-only, never sizes. **20 names** (the lane returned 14)

Funnel, reproduced by the orchestrator and **matching the lane exactly through stage 5**: 6,293 screener → 5,936 with close+w52l → **264** at `close ≤ 1.02×w52l` → **63** Common/ADR (**201 cut**: 195 ETF, 4 null, 2 Structured Product) → **48** at close ≥ $5 → **20** clearing the $50M 20-day $-ADV floor → **20** after the h10 earnings gate (**0 blocked**).

**LULU, LHX, MCD, VICI, XYL, KRMN, ROL, NKE, TXT, AMTM, STZ, TJX, ONON, PEG, TSN, GLPI, CCL, CMS, MIDD, JOBY**

**The lane truncated this to 14** by taking a top-15 by proximity and then cutting ONON under a sector cap. **Neither step is in the lane's specification** — MOM_SHORT is a full-cohort watch list (09-03 reported 19 untruncated). The six dropped names (GLPI, CCL, CMS, MIDD, JOBY, ONON) all clear every shipped gate.

Sector: Consumer Cyclical 7, Industrials 7 (**70% in two sectors**), Real Estate 2, Consumer Defensive 2, Utilities 2 — the same concentration shape as the prior two nights.

**Yahoo-verified the top 5 individually** (`chart.py --52w`), and the 09-03 fresh-low inversion did **not** recur:

| ticker | screener w52l | Yahoo w52l | date of low | class |
|---|---|---|---|---|
| LULU | 104.44 | **97.99** | **2026-09-04** | **(c) fresh low made today — validates the short tag** |
| LHX | 258.54 | **256.05** | **2026-09-04** | **(c) fresh low today** |
| MCD | 256.12 | **255.49** | **2026-09-04** | **(c) fresh low today** |
| VICI | 25.34 | 25.34 | 2026-09-03 | clean, exact match |
| XYL | 105.29 | 105.29 | 2026-05-20 | clean, exact match — genuine standing near-low |

LULU's low is an earnings gap (**−17.38%** on the day, the tape's worst large-cap mover). Three of five are fresh lows printed today, the class that 09-03's run wrongly cut; tonight the lane kept them.

Near-misses at the liquidity floor: SNN $47.3M, BILI $43.1M, FLO $42.3M, PZZA $38.4M, MZTI $37.6M.

### MOM_LONG — basket/watch only. **181 names** (the lane returned 16)

Funnel: 6,293 → **1,417** at `close ≥ 0.95×w52h` → **419** Common/ADR (998 cut) → **410** at close ≥ $5 → **181** post-liquidity → **181** after the earnings gate.

Same unspecified top-15 truncation as the short leg. Sector shares are all under the ⅓ cap: Financial Services 27.6%, Healthcare 22.7%, Energy 13.3%, Technology 10.5%.

**VOD is a FALSE earnings block and is counted in the 181.** `earnings_gate.py` blocked it on a `next_earnings_date` of **2026-07-27** — five weeks in the *past* — while claiming the print is inside h10. This is the documented no-lower-bound defect (`elif ned.isoformat() <= end`), now on its third consecutive night. **CCEP, the other 09-03 victim, is not affected tonight** — it left the pool on the signal (93.04% of its 52w high, below the 95% threshold), not on the gate.

### OI_FADE — STOOD DOWN, diary-only. Zero candidates, zero watch list, empty slate to the sizer

Funnel: 6,293 → 1,802 liquidity → 1,776 earnings (26 blocked) → **1,366** `issue_type` (410 cut: 391 ETF, 10 null, 5 Unit, 3 Other, 1 Structured Product) → 1,293 full 5-day window (73 partial-window rows failed closed) → 606 build floors → **583** listing age (23 cut) → **343** persistence (240 cut).

Diary-only top ranks by `oi_rel_build` (persistence) — **none of these is a suggestion**: RSI 1.036/0.432, AGX 0.987/0.748, FRVO 0.887/0.432, WSC 0.689/0.382, BURL 0.673/0.802, EIX 0.536/0.554, ESI 0.493/0.557.

Raw-rank pool for contrast: PCG, AMZN, INTC, NU, AVGO, META, SMCI, NOK, WULF, PBR, CORZ, NKE, SOFI, BSX, RKLB. **Overlap with the relative-ranked top-15: 0 of 15** — total divergence tonight (09-03 had one, PBR), which is the separation the shipped rule exists to create.

**`catalyst_split.py`'s `>=` boundary bug fired on three names, one as a sign flip:**

| ticker | catalyst | `>=` (tool) | strict `>` | flip |
|---|---|---|---|---|
| **AGX** (#2) | 09-02 print | 87.1% → LIVE_BUILD | **11.9% → RESOLVED_PRE_PRINT** | yes — 2nd consecutive night, 74.9% of the 5d net still lands on the print day |
| **BURL** (#5) | 08-27 print | 58.6% → LIVE_BUILD | **−70.3% → RESOLVED_PRE_PRINT** | yes — a **sign flip**, because the 10d net is negative while the ranking-relevant 5d net is positive: a 10d-vs-5d window mismatch layered on the boundary bug |
| **PL** (#10) | 09-03 print | 18.2% → LIVE_BUILD | **14.2% → RESOLVED_PRE_PRINT** | yes — a genuine straddle of the 0.15 threshold |

**The listing-age gate cut 23 names; only 2 are genuinely young.** Real IPO dates were checked per name. **SPCX** (IPO 2026-06-12, 57 rows) and **SKHY** (2026-07-10, 39 rows) are real sub-60-session listings. The other 21 are coverage-sparsity artifacts of names listed 1995–2021 — including **DLB for a second consecutive night**, which carries `rel_build` **3.869** (3.7× tonight's actual #1) and would be the board's clear top name. **PSNL dies here for a 4th consecutive cycle** without ever reaching the M&A gate — and it is confirmed a live M&A situation (Tempus AI named as suitor, 08-20), at `rel_build` 0.481 which would rank it ~8–9. The gate blocking it is measuring the wrong thing entirely.

**M&A / catalyst notes:** CCC rechecked — the Copart rumour is still unconfirmed with no update past 08-19, and it has fallen from rank 15 to **32/343**; recorded, not cut. **FRVO exposes a scope gap**: its build coincides with a real *non-earnings* catalyst (a Google geothermal PPA, 09-01/02) that neither `earnings_gate.py` nor `catalyst_split.py` can see, both being earnings-only. The verdict is unchanged here by luck (the largest build day, +6,096, falls on 09-04, after the deal), but the tooling has no general mechanism for non-earnings catalysts.

**Re-signal dedup: all five of 09-03's top names repeat.** RSI's rank sequence is now **3 → 1 → 2 → 1** across four nights. This is the documented structural forward-N cap, not fresh evidence.

**No wash-builds** (`last_call_net` positive on all 15 survivors). Separately noted: several names show sharply negative *put*-side net on 09-04 (RSI −4,991, BURL −3,221), consistent with Friday weekly-expiry roll-off rather than fresh positioning — it mechanically inflates call-minus-put net without incremental call demand. Carried forward as a data-quality note on RSI.

### S2 (liquidity-reversion) — advisory. **90 names**, and the lane was correct again

Funnel, **independently reproduced and matching exactly**: **192** at `dp_oneside ≥ 0.90` → **103** also clearing `dp_prem ≥ $10M` and price ≥ $5 → **90** Common+ADR (11 ETFs cut) → **90** after the h5 earnings gate (0 blocked).

Top by dark-pool premium: **UNH ($1,163.4M, 96.0% one-sided)**, LIN ($477.7M, 93.7%), SU ($372.9M, 99.2%), GILD ($336.8M, 95.3%), TEVA ($185.1M, 96.6%), SE ($169.2M, 98.6%), MKSI ($166.7M, 95.3%).

**UNH repeats from 09-03** (was $994.8M / 92.7%) — larger and more one-sided tonight. Sector: Financial Services 20, Technology 13, Real Estate 10.

Second consecutive clean night after the two documented "lane empty" failures. Recorded as a pass. The plain-CHOP cell for S2 remains indistinguishable from zero — this is documentation, not a recommendation.

### S4 (sentiment-contrarian) — advisory, right-tail only. **31 names by the shipped rule** (the lane returned 28, wrong in both directions)

I re-ran the **shipped** rule from `retro_harness.py` verbatim, which matters because the shipped rule applies `issue_type` **and** the earnings gate *before* computing the 95th percentile: 6,293 → **610** clearing price ≥ $5, $50M $-ADV, `call_volume ≥ 250`, `put_volume > 0`, `call+put ≥ 1000`, Common/ADR and the **h5** earnings gate → **p95 = 2.142** → **31 candidates** (the harness itself then takes the top 15).

Top by PCR **with call denominators**: **VFC 35.26 (5,934 calls)**, DAVE 12.65 (288), DOW 6.62 (7,143), EQT 5.98 (2,610), MGM 5.63 (1,246), **XEL 5.33 (331)**, MIR 5.01 (295), ECHO 4.96 (2,445), MET 4.92 (311), LYV 4.49 (1,455), NOC 4.47 (491), WMB 4.36 (3,358), GE 4.25 (7,750), BBY 4.15 (2,773), CI 4.02 (941).

Five names sit in the 250–350 call-volume noise zone where PCR rank is not meaningful: **DAVE (288), XEL (331), MIR (295), MET (311), STRC (257)**.

**The lane's ETP handling was wrong in both directions.** It cut **XEL, UCTT and QXO as "ETFs"** — all three are `issue_type = 'Common Stock'` (Xcel Energy, Ultra Clean Holdings, QXO Inc), and XEL ranks **#6** on the shipped rule. It simultaneously **kept ETH, which is a genuine ETF**. It also applied an **h10** earnings gate where the shipped rule uses **h5**, and computed its percentile on a differently-filtered base (getting 2.21 against the shipped 2.142). The shipped rule never has an ETF problem at all, because `issue_type` precedes the percentile.

**Cross-lane contradictions — noted as evidence diversification, never netted:** **VFC** and **ROL** are simultaneously on tonight's MOM_SHORT watch list and in the S4 long pool. **CME** appears in both S4 (#31) and S2 (#10). **LHX** is on the MOM_SHORT list and in the OI_FADE diary top-15.

Rising-IV tilt (`ivrank_chg_5d`, h3, the only 3-regime-stable factor): VMRK +64.0 strongest, then NOBL +60.4, MIAX +50.7, BRX +49.6, SRE +44.9, ALKS +42.8. No overlap with the S4 pool — orthogonality holds.

**S4's `hit − base` is −0.034 tonight (−0.056 on the recorded baseline): the lane has no hit-rate edge on this panel, only a right tail.**

---

## Lane reliability — three of six lanes needed correction

**1. `momentum` — truncation not in the specification (both legs).** It reported 14 MOM_SHORT and 16 MOM_LONG against true cohorts of **20** and **181**, by taking a top-15 by proximity and then applying a sector cap of its own invention. Stages 1–5 of both funnels reproduced *exactly* against my own query, so the screening was right and only the presentation was truncated. **Credit where due: it did not repeat the 09-03 fresh-low inversion** (LULU/LHX/MCD were kept and are Yahoo-confirmed fresh lows), it used the native `issue_type` field, and it caught the VOD false block. Its Yahoo-verification claim was also honest this time (8/14 and 7/16 spot-checked, stated as such) after 09-03's blanket over-attestation.

**2. `sentiment-contrarian` — wrong ETP cut in both directions, wrong horizon.** Detailed above: three common stocks cut as ETFs, one real ETF kept, h10 applied where the shipped rule is h5, percentile computed on a non-shipped base.

**3. `regime-classifier` — numbers right, mechanism wrong.** Every figure it returned reconciles (I verified SPY/QQQ/IWM/VIX on two independent surfaces). But its explanation of the SPY-red / QQQ-green divergence — "mega-cap weakness drags SPY while breadth outside large caps is green" — **cannot be the mechanism**: AAPL, MSFT and TSLA are *heavier* weights in QQQ than in SPY, and QQQ holds no small caps at all. The actual cause is **sector rotation**, which its own data supports once split by sector rather than by cap:

| large-cap sector | n | median | adv/dec |
|---|---|---|---|
| **Industrials** | 132 | **+0.486%** | 89/42 |
| **Technology** | 163 | **+0.214%** | 90/73 |
| Consumer Cyclical | 81 | −0.112% | 38/43 |
| Utilities | 40 | −0.440% | 12/27 |
| Real Estate | 42 | −0.560% | 10/32 |
| Financial Services | 143 | −0.672% | 33/109 |
| Energy | 48 | −0.701% | 15/33 |
| Healthcare | 110 | −0.829% | 21/88 |
| Consumer Defensive | 49 | −0.837% | 8/40 |
| Communication Services | 49 | −0.930% | 16/33 |
| Basic Materials | 51 | −1.035% | 16/35 |

Technology and Industrials were the **only** green large-cap sectors, and the semis ripped (**MU +6.10%, SKHY +8.14%, TSM +2.85%**, NVDA +0.84%), offsetting AAPL −2.51% / MSFT −2.04% / TSLA −5.92% inside QQQ. SPY carries the 143 large-cap financials, 110 healthcare and 49 staples that QQQ barely holds, and those are what made it red. The cap-size table is real but is a *coincident* fact, not the cause.

**Passes:** `oi-flow-fade` (clean funnel, and it found the `hz_end` root cause below — the best diagnostic work of the night); `liquidity-reversion` (exact reproduction, second clean night); `vol-book` (corrected its 09-03 gamma inversion, derived both signs from `total_gex` + ladder as instructed, and surfaced the `near_dte_actual=0` defect).

### Tooling defects recorded tonight

**NEW — `_calendar.hz_end` fails OPEN at the panel edge, with a root cause.** `hz_end` computes `fut = [d for d in trading_days() if d > t]` off SPY in `prices.parquet`. **Once the panel is rebuilt to reach T, `fut` is empty**, so it drops into raw calendar extrapolation (`t + round(h·7/5) + 1`) which skips neither weekends nor holidays. With Labor Day inside every window tonight:

| horizon | `hz_end` | true exit | error |
|---|---|---|---|
| h3 | 2026-09-09 | 2026-09-10 | 1 session short |
| h5 | **2026-09-12 (a Saturday)** | 2026-09-14 | 2 sessions short |
| h10 | **2026-09-19 (a Saturday)** | 2026-09-21 | 2 sessions short |

This **directly contradicts the function's own docstring**, which promises the extrapolation "rounds outward … so the window is a day long rather than a day short" and that "a gate must fail CLOSED." Tonight it fails **open** on all three horizons. Worse, it fires *because* the truth set is fresh — the healthier the panel, the more certainly this triggers. **Live leak measured: exactly one name.** ABVX (reports **2026-09-21**, the true h10 exit) passes the buggy 09-19 cutoff; it is in no lane's pool (77% of its 52w high, `rel_build` 0.038), so nothing reached a list. *(Correction to the OI lane's write-up, which named AZO as a second leak: AZO reports 09-22, which is genuinely outside the true h10 window and correctly passes. My own prompt gave the lanes 09-22 as the h10 end when the correct exit is 09-21 — an over-wide window, so it fails closed and cost only AZO a slot in a diary-only funnel that emits nothing. No momentum-pool name sits anywhere in the disputed 09-19..09-22 band.)*

Others: `earnings_gate.py` no-lower-bound over-blocking on stale dates (**live on 4 names** — PURR 08-27, VOD 07-27, HLN 07-30, CCEP 08-04 — third consecutive night); `catalyst_split.py` `>=` boundary fired on **3 names**, one a sign flip (second consecutive night); OI listing-age gate measuring coverage sparsity not listing age (23 cut, 21 misclassified, second night for DLB, fourth cycle for PSNL); `uw gex` `regime` field corrupted on QQQ (**5th consecutive night**) and `zero_gamma_level` garbage on QQQ (**4th**); `zerodte_setup.py` overriding its own correct negative `net_gex_0_45d` with the corrupted field; `uw insights earnings-play` `near_dte_actual=0` contaminating `implied_move_perc` with a 0DTE near leg on 3 names (**new**); `uw risk market-regime` advisory-only.

**`preflight.py`'s global-max false clear did NOT fire tonight** — it correctly reported all three parquets STALE at 09-03 and I rebuilt them. But the defect is unfixed: it cleared on 8 backfilled names out of 2,443 on 09-03, and would do so again. The check should be `max(date) WHERE ticker='SPY'`, or a coverage fraction.

## Risk

- **Correlation clusters:** none sized, so none binding. For the diary: MOM_SHORT is **70% Consumer Cyclical + Industrials**; the OI_FADE raw-rank pool again contains a crypto/miner cluster (WULF, CORZ).
- **Event calendar — dense, and a holiday eats a session.** **Labor Day 09-07, market closed** — the next session is **Tuesday 09-08**. NFP landed today. Then **PPI 09-10**, **CPI 09-11**, **FOMC + dot plot 09-16** (with Retail Sales stacked the same morning). An h10 window opened today (09-08..09-21) carries **three Tier-1 macro events**.
- **Regime moved away from the UPTREND line**, not toward it: ret10 +1.386% → +0.580% against a +1.5% threshold. Last night's flip watch is stood down.
- **Dealer gamma flipped SHORT on both indices** into that calendar — a vol-amplifying lean, the reverse of 09-03. SPY is decisively short (ATM strike −904M); QQQ is negative on the full book but balanced near spot. With VIX in the LOW tercile, this is a low-realized-vol tape sitting on a short-gamma structure. **Vol-state only — no direction is read from gamma.**
- **Tail caps:** not applicable — nothing sized.
- **Hedge note:** book is flat; no hedge required.
