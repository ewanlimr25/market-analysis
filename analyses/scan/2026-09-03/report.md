# Market Scan — 2026-09-03

## Regime & Verdict

- **Regime: CHOP** (plain, *not* CHOP/REBOUND-THRUST) · ret5 **+0.268%** · ret10 **+1.386%** · dd15 **−0.108%** · `directional_tradable=true` · `s1_standdown=false`
  — **hand-computed, NOT from `regime_check.py`**, which returns a STALE 09-02 answer tonight (see Data integrity). My reimplementation of `_regime.classify_regime` reproduces the shipped function **bit-exactly on 09-02** (CHOP / −0.120% / −0.507% / −0.947%), which is what licenses using it for 09-03.
- **Tape:** SPY **773.17 (+1.05%)** · QQQ **717.67 (+1.19%)** · IWM **295.19 (+0.40%)** · VIX **14.32 (−5.8%)**. A broad risk-on session that reverses the ten-day drift: ret10 goes **−0.507% → +1.386%**, and dd15 all but closes (−0.947% → −0.108%).
- **ret10 is 11bp below the +1.5% UPTREND threshold.** The label is CHOP by the narrowest margin in this panel's recent history. One more up-session flips the regime label, which changes every lane's `regime_fit`. Flagged for tomorrow.
- **Breadth:** full UW screener n=5,937 → 3,999 adv / 1,840 dec = **67.4% green**, median **+0.592%**. `fz breadth` (S&P 500, n=503): 340/161 = **67.59% green**, median +0.64%. Two universes, near-identical. **SPY (+1.05%) beat the median stock (+0.59%)** — a large-cap-led advance, the exact mirror of 09-02 when the median stock beat SPY.
- **Vol-state:** VIX 14.32, **LOW tercile** on trailing-60 bounds [15.8, 17.1]. Dealer gamma **LONG/positive on both SPY and QQQ** (hand-derived from the per-strike ladder; the CLI disagrees on SPY — see Risk).
- **Bottom line: No directional edge today. Nineteenth consecutive flat session.** No lane in this repo sizes. The directional book is empty by construction, not by failure to find names.

## Directional Book (excess-scored)

**EMPTY.** No lane sizes. `risk-sizer` was not spawned — with zero sized candidates Phase D is vacuous — and `fundamentals-gate` was correctly not spawned, since it runs only on names about to be sized.

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

**Open call rows: 0.** All five (FDX/GEN/BSY/ITRI matured 08-28, AS matured 09-02) are resolvable at the **2026-09-05 audit**. Held-book reconciliation off the 09-02 conviction file read 0 open / 0 closed, verified against `book_state.positions == 0` in the source file rather than trusting the bare empty result (the known EXIT-substring bug).

---

## Data integrity — the truth set silently stopped at 09-02, and preflight cleared it anyway

This is tonight's most consequential finding and it precedes every number above.

**Yahoo's *daily-bar* array was never backfilled for 2026-09-03.** For SPY, QQQ, IWM and essentially the whole spine, the `1d` array returns a row for 09-03 with `close: null`. Consequences:

- `build_prices.py` wrote **2,443 tickers but only 8 with a 09-03 bar** (ADEA, APH, FXO, HUBB, JMST, PHYS, SHEL, VCX).
- `data/prices.parquet`, `scripts/chart.py`, `scripts/held_book.py` and `scripts/regime_check.py` therefore **all still read 09-02**. `held_book.py` printed "as of 2026-09-02 (SPY +0.44% on the day)" — 09-02's move, on 09-03's scan.
- **`preflight.py` reported `[ok] prices.parquet -> 2026-09-03` and printed "clear".** It checks `max(date)` across all tickers, so **8 backfilled names out of 2,443 were enough to clear the gate.** This is a false clear on the exact check that exists to prevent a lane reading a stale panel — the 2026-07-24 failure it was written for. **The check should be `max(date) WHERE ticker='SPY'`, or a coverage fraction, not a global max.**

The 09-03 session data **does** exist, on two surfaces that agree exactly:

| | `meta.regularMarketPrice` | 5-minute array (79 bars, 13:30→20:00 UTC) | agree |
|---|---|---|---|
| SPY | 773.17 | 773.17 (open 768.43, hi 774.03, lo 767.47) | ✅ |
| QQQ | 717.67 | 717.67 (open 710.85, hi 718.91, lo 709.69) | ✅ |
| IWM | 295.19 | 295.19 (open 295.79, hi 296.18, lo 293.43) | ✅ |

`meta.regularMarketTime` is 20:00 UTC = **16:00 ET, the official close**. `^VIX`'s daily bar *is* populated (14.32), which is how the daily/intraday split was isolated.

**I did not patch `prices.parquet`.** Injecting reconstructed bars into the truth set would contaminate the regression gate's own history to fix a one-session display lag. Instead the regime was computed by hand from the reconstructed close, and every price-dependent figure below states which surface it came from.

### What the stale edge actually damages, and what it does not

- **Regression gate: unaffected.** It grades matured h10 windows; nothing signalled on 09-03 has matured.
- **Regime gate: materially affected** — the whole point of the hand computation above.
- **`_calendar.hz_end`: affected but, tonight, benign by coincidence.** It builds the session grid from **SPY** in `prices.parquet`, so the grid ends 09-02 and every horizon from 09-03 is *extrapolated* on a 5-day week (`t + round(h·7/5) + 1`). Verified against the true NYSE calendar (weekends + Labor Day 09-07):

  | horizon | `hz_end` | true | verdict |
  |---|---|---|---|
  | h3 | 2026-09-08 | 2026-09-09 | ⚠️ **one session short — fails OPEN** |
  | h5 | 2026-09-11 | 2026-09-11 | ✅ |
  | h10 | 2026-09-18 | 2026-09-18 | ✅ |

  h5 and h10 — the only two horizons anything actually gates on tonight — are correct, because the `+1` outward rounding happens to absorb Labor Day. **h3 is one session short and would fail open.** Nothing gated on h3 tonight, so no name leaked, but this is a live fail-open the moment a holiday sits inside an h3 window while the panel edge lags.
- **Exit-day grid: the 09-03 exit day is missing entirely** (dates jump 09-02 → 09-04), and extrapolated "exit dates" include **Saturdays** (09-05, 09-12). Both are confined to *unresolved future* rows, which are excluded from every statistic below — so the clustering key is sound for every row that enters a number. Worth knowing before anyone reads that grid as a calendar.

---

## Regression gate

**No lane or threshold changed tonight**, so this is a data-only re-read. `retro_harness.py --all --oi-variant both`, **102 panel days**, spine **2,443** (28 UNPRICED, fail-closed):

| lane | n | mean_exc | hit | base | hit−base |
|---|---|---|---|---|---|
| MOM_LONG | 1320 | −0.0123 | 0.43 | 0.56 | −0.132 |
| MOM_SHORT | 912 | −0.0129 | 0.41 | 0.42 | −0.009 |
| OI_FADE | 1297 | −0.0012 | 0.53 | 0.41 | +0.118 |
| **OI_FADE_LIVE** | **480** | **−0.0080** | 0.49 | 0.56 | −0.075 |
| OI_FADE_RAWPOOL | 480 | −0.0136 | 0.48 | 0.56 | −0.085 |
| S2_dp_revert | 1375 | +0.0008 | 0.50 | 0.52 | −0.018 |
| S4_pcr_fade | 1423 | +0.0016 | 0.50 | 0.52 | −0.023 |

Four lanes read below the recorded baseline. **Isolation check by EXIT date** (the harness has no exit-date flag; I imported it and split the cohort myself):

| lane | recorded baseline | tonight, exit ≤ 08-21 | maturity edge (exit > 08-21) |
|---|---|---|---|
| MOM_LONG | −0.0118 (n=1213) | −0.0122 (n=1208) | −0.0130 (n=112), base **0.00** |
| MOM_SHORT | −0.0138 (n=830) | −0.0137 (n=826) | −0.0051 (n=86), base **1.00** |
| OI_FADE | +0.0013 (n=1177) | **+0.0013 (n=1177) — bit-exact** | −0.0254 (n=120), base **1.00** |
| S2 | +0.0018 (n=1269) | +0.0018 (n=1257) | −0.0089 (n=118), base 0.37 |
| S4 | +0.0024 (n=1304) | +0.0024 (n=1303) | −0.0079 (n=120), base 0.38 |

The baseline cohort's **means reproduce to 4dp on every lane** (MOM_LONG −0.0122 vs −0.0118 is the one 4bp drift, and it is stable night-over-night). The full-panel move is the maturity edge. **No regression; do not re-baseline.**

**The `base` pinning is specifically an h10 phenomenon, and saying so matters.** MOM_LONG (long, h10) reads base **0.00** and every short h10 lane reads base **1.00** — SPY down in 100% of the new h10 windows. But **S2 (h3–5) and S4 (h5–10) read base 0.37 / 0.38, not pinned at all**, because their shorter windows sample a different set of exits. Prior write-ups have described the pinning as a whole-panel property; it is not — it is a property of the h10 window set, and the two shorter-horizon lanes are the control that shows it.

**Row-count attrition continues but has nearly stopped.** Against last night: MOM_LONG 1209 → 1208 (−1); MOM_SHORT 826, S2 1257, S4 1303, OI_FADE 1177 all **unchanged**. The spine held at 2,443 with the same 28 unpriced names. Means did not move. This is attrition, not decay — and it is decelerating, which is the first sign the vendor-feed churn is settling rather than compounding.

### OI_FADE_LIVE — the pre-registered re-check, now 32 complete `lane-exit-day`

**No partial exit-days tonight** — all 32 resolved days are 15/15. The forming 09-02 day that last night's carry-forward flagged at 10/15 has completed.

| cohort | k (`lane-exit-day`) | mean | t | p (iid) |
|---|---|---|---|---|
| last night (31 complete) | 31 | −0.0083 | −2.166 | 0.0303 |
| **tonight (32 complete)** | **32** | **−0.0080** | **−2.141** | **0.0402** |

`scipy` is not installed; the p-values come from a hand-rolled incomplete-beta t-CDF **validated against eight reference points** (t=2.228/df=10→0.05, t=2.086/df=20→0.05, t=2.042/df=30→0.05, t=3.0/df=25→0.00609, t=1.96/df=10⁶→0.05, etc.), all matching to <2e-3.

**Two things worth recording, both unfavourable to the stand-down evidence:**

1. **The partial-day bias is confirmed a third time, and its direction is now measured.** The 09-02 exit-day read **+0.0226 at 10/15** last night and **+0.0136 complete at 15/15** tonight. Admitting the slow half pulled it *down* — i.e. the fast-resolving half is systematically the *better* half for a short lane, exactly as predicted. Last night the same thing happened to 09-01 (+0.0083 partial → completing near that). **The rule "exclude forming exit-days" is now supported by three independent instances and should be written into the harness rather than re-caught nightly.**
2. **p is drifting toward the line as the cohort completes**: 0.016 → 0.0297 → 0.0303 → **0.0402** across four nights. The last three complete exit-days read **−0.0102, +0.0098, +0.0136** — two of the last three positive. This is the pre-registered unwind beginning to show up in the lane's own evidence.

⚠️ **A completed exit-day moved overnight.** 09-01 read **+0.0083** last night at 15/15 and reads **+0.0098** tonight at 15/15 — a frozen, fully-resolved cohort changing value. Same non-idempotent vendor feed as the row-count attrition, now visibly touching a *completed* unit rather than just dropping rows.

**Verdict for the 2026-09-05 audit: CONFIRMED on sign, above the 30-unit bar at 32 complete `lane-exit-day`, p=0.0402 iid — but NOT durable on significance.** The h10 window-overlap defect (9/10 shared days) roughly halves this t under Newey-West, and the point estimate has now crossed above 0.04 having been 0.016 three nights ago on substantially the same rows. **Do not record a BH-surviving formal STOP.** The lane stays stood down on the sign and the prior, not on this p-value.

---

## Vol Book (non-directional)

Delta-neutral, advisory, quoted net of cost, zero directional points.

### 0DTE-VRP — STAND ASIDE on both SPY and QQQ

**Two Phase-B agents returned contradictory gamma reads on SPY. I arbitrated from the raw per-strike ladder.**

| | total_gex | ladder sum | near-money (±1.2%) | CLI `regime` | `zero_gamma_level` | derived |
|---|---|---|---|---|---|---|
| **SPY** | **+1.070B** | +1.305B | **17/19 strikes positive, net +1.32B** | **"NEGATIVE"** | 774.24 (in ladder 748–797) | **LONG / positive gamma** |
| **QQQ** | +360M | +588M | **20/21 strikes positive, net +631M** | "POSITIVE" ✅ | **276.37** vs ladder **696–739** ❌ | **LONG / positive gamma** |

- **SPY's `regime` field is corrupted tonight — it contradicts its own `total_gex`.** The field says "NEGATIVE / dealers net short gamma" while `total_gex` is **+1.07B**, the ladder sums **+1.30B**, and 17 of 19 near-money strikes are positive. Per the documented rule (derive the sign from `total_gex` + per-strike, never the field), SPY is **long gamma**. This is the **4th consecutive night** of `uw gex` field corruption — and the first in the *inverted* direction: prior nights the field claimed POSITIVE over a negative `total_gex`, tonight it claims NEGATIVE over a positive one. **"Trust the field when it looks plausible" is not a usable heuristic; it was wrong in both directions this week.**
- The `vol-book` lane concluded the opposite ("SPY genuinely is short-gamma tonight, the field is NOT corrupted"), by anchoring on spot 772.88 sitting 1.4 points *below* `zero_gamma_level` 774.24 and treating the flip level as ground truth. That inverts the documented derivation. The cumulative-sum crossing sits at **772–773, i.e. essentially at spot**, so SPY is near enough its flip that the knife-edge reading is defensible as *context* — but the sign that the repo's own rule derives is positive, and the field contradicting `total_gex` is corruption by definition.
- **QQQ's `regime` field is correct tonight; its `zero_gamma_level` (276.37) is garbage** against a 696–739 book — the **3rd consecutive night** for that specific field (256.43 on 09-02). Two different fields corrupted on two different instruments on the same night.

**Verdict: STAND ASIDE both — but the stated reason changes.** The 09-02 rationale ("short-gamma trend-acceleration state with an unsampled left tail") **does not apply tonight**; both books are long gamma, a vol-*suppressing* lean. What binds instead is the standing structural objection, which is unchanged and arguably stronger here: `zerodte_setup.py`'s backtest is stratified by **VIX tercile only, never by gamma regime**, so its LOW-tercile conditional mean pools long- and short-gamma sessions. VIX 14.32 is in the LOW tercile — the bucket already documented as flipping negative net of cost — and no conditional statistic exists for tonight's actual (LOW-VIX × long-gamma) state. Quoting one would cite a different regime than the live one. `zerodte_setup.py` also independently returns `size_scalar=0.0` on both legs.

### Earnings IV-crush

VSXY printed 09-03 and is correctly off the forward list. **Every figure below is a mean-across-strikes IV — a FLOOR requiring ATM confirmation** (TPR realized ~1.35× its floor, MDT ~1.44×); the CLI exposes no ATM/median straddle endpoint. Day counts exclude the **09-07 Labor Day** holiday.

| Ticker | Print | Bracketing expiry (contracts) | Next leg | Raw `implied_move_perc` | Variance-isolated | Verdict |
|---|---|---|---|---|---|---|
| **AEO** | 09-09 | 09-11, 8dte (259) | 09-18 (187) | 1.85% — **discard, pre-print expiry** | **13.8%** | advisory sell-vol, iron fly 09-11, wings ≥1.4× floor |
| **JMKE** | 09-09 | 09-18, 15dte (207) | 10-16 (78) | 9.1% | **7.9%** (ratio 1.15) | **new tonight** — best book of the cohort, advisory sell-vol |
| **SUNB** | 09-09 | 09-18, 15dte (134) | 10-16 (32) | 10.0% | 11.9% | advisory, **size down** |
| **SHOE** | 09-10 | 09-18, 15dte (81) | 10-16 (33) | 14.3% | 23.6% | **size down materially** — ~1.7× internal disagreement persists; wing to the higher number |
| ODD | 09-09 | 09-11 (**16**) | 09-18 (**3**) | 4.2% (trap) | — | **SKIP** — thin-book artifact |
| CGNT | 09-09 | 09-18 (**4**) | 11-20 (**1**) | 16.0% | — | **SKIP** |
| ZUMZ | 09-10 | 09-18 (**1**) | 43dte (13) | 15.0% | — | **SKIP** |
| ANIX | 09-09 | 09-18 (**3**) | 43dte (5) | 22.5% | — | **SKIP** |
| MNY | 09-11 | — | — | 172.8% | — | **EXCLUDED** — impossible value, zero-book artifact |
| CASY | 09-08 | — | — | 7.7% | — | excluded, iv_rank 77.75 < 80 gate |

**AEO remains the worked example of the bracketing-expiry trap**: its nearest expiry (09-04) falls *before* the 09-09 print, so the raw 1.85% reads a no-catalyst window and is internally impossible. Correct bracketing on 09-11 gives 13.8%, reproducing the 13.7% computed on 09-02 from different inputs.

---

## Watch / Stood-down

### MOM_SHORT — watch-only, never sizes. **19 names** (the lane returned 17, and 6 of them were wrong)

Funnel, rebuilt by the orchestrator from the screener's native `issue_type`: 6,292 screener → 5,935 with close+w52l → **284** at `close ≤ 1.02×w52l` → **79** Common/ADR (205 ETPs cut) → **50** at close ≥ $5 → **19** clearing the $50M 20-day $-ADV floor → **19** after the h10 earnings gate (0 blocked, window 09-04..09-18).

**AMTM, AS, BEPC, CCL, ESAB, FDXF, KRMN, LHX, LOW, MCD, MLM, PEG, RBA, ROL, TJX, TXT, VFC, VICI, XPEV**

Sector: Consumer Cyclical 42.1%, Industrials 36.8%, Utilities 10.5%, Real Estate 5.3%, Basic Materials 5.3% — **79% in two sectors**, the same concentration as 09-02.

Near-misses at the liquidity floor worth noting because they are within noise of it: **JMKE $49.8M** (on last night's list; fails by $0.2M), OLN $47.5M, SNN $46.7M, BILI $43.6M, FLO $41.3M.

### MOM_LONG — basket/watch only. **201 names** (the lane returned 310)

Two independent paths converge: screener path 1,416 at `close ≥ 0.95×w52h` → 421 Common/ADR → 413 at close ≥ $5 → **201** post-liquidity; features path 404 candidates → **201** Common/ADR. Sector: Financial Services 24.9%, Healthcare 23.9%, Energy 14.4%, Technology 13.9% — all within the ⅓ cap.

**CCEP and VOD are FALSE earnings blocks and are counted in the 201.** `earnings_gate.py` blocked them citing prints of **2026-08-04** and **2026-07-27** — both in the *past* — with the reason string *"inside h10 (2026-09-04..2026-09-18)"*, a window containing neither date. This is the documented no-lower-bound defect (`elif ned.isoformat() <= end`) firing on a **stale** `next_earnings_date`, which is exactly the silent over-blocking mode flagged on 09-02. Second consecutive night; it now has live victims rather than a mislabeled-but-correct cut.

### OI_FADE — STOOD DOWN, diary-only. Zero candidates, zero watch list, empty slate to the sizer

Funnel: 6,292 → 1,814 liquidity → 1,774 earnings → **1,358** `issue_type` (1,275 Common + 83 ADR; 406 ETP cut) → 1,281 full 5-day window (77 partial-window rows failed closed) → 599 build floors → **576** listing age (23 cut) → **360** persistence (216 cut).

Diary-only top ranks by `oi_rel_build` — **none of these is a suggestion**: AGX 0.956/pers 0.809, RSI 0.893/0.519, WSC 0.756/0.413, FRVO 0.635/0.630, ESI 0.400/0.693.

**Two new defects surfaced by this lane, both of which I reproduced independently before recording them.**

**1. The `catalyst_split.py` `>=` boundary bug fired LIVE tonight on the lane's #1 name.** Inert for the previous two nights (every survivor read `NO_CATALYST_IN_WINDOW`); tonight AGX printed earnings **09-02** and its build is the print-day spike itself. Verified from the raw OI panel:

| date | call Δ | put Δ | net | running |
|---|---|---|---|---|
| 08-28 | +120 | +81 | +39 | +39 |
| 08-31 | +636 | +148 | +488 | +527 |
| 09-01 | +393 | +123 | +270 | +797 |
| **09-02 (PRINT)** | **+4,652** | **+377** | **+4,275** | **+5,072** |
| 09-03 | +714 | +499 | +215 | +5,287 |

**80.9% of the 5-day net landed on the print day alone.** The tool's `>=` counts the print day as post-catalyst → post-share **84.9% → LIVE_BUILD**. Strict `>` → post-share **4.1% → RESOLVED_PRE_PRINT**. Opposite verdicts on tonight's top-ranked name, the same pattern as the documented EWTX case (83% vs 4.6%).

**2. The listing-age gate is not measuring listing age.** It cut **23 names tonight** (vs 0–1 on prior nights) via an `nrows ≥ 60` floor that counts *features-panel rows*, not sessions since IPO. Verified against the panel:

| ticker | features rows | first row | last row | actual |
|---|---|---|---|---|
| **NVAX** | **20** | **2026-03-13** (first panel date) | 2026-09-03 | listed **2003** |
| DLB | 39 | 2026-05-27 | 2026-09-03 | listed **2005** |
| TAK | 55 | 2026-04-28 | 2026-09-03 | listed decades |
| PSNL | 46 | 2026-06-29 | 2026-09-03 | listed **2019** |
| HONA | 45 | 2026-07-02 | 2026-09-03 | **genuinely young** (2026 spinoff) |

**NVAX is the clean proof**: 20 rows spanning the *entire* 102-date panel, first row on the panel's very first day. A name present from day one with 20 of 102 rows cannot be a recent listing — the gate is measuring **coverage sparsity**. DLB carried the highest raw `oi_rel_build` on the board (**4.418**) and was cut by it. Only HONA among the 23 is a genuine sub-60-session listing.

**PSNL — the carried-forward M&A test case — never reached the M&A gate for a third cycle**, dying at this same spurious listing-age gate. The question of whether the gate's language should widen from "cash" to "any definitive agreement" is **still unresolved**, and is now blocked by an unrelated defect rather than by judgment.

Other gate-of-death notes: STEP (rel_build 1.289) died on persistence 1.018; VSNT died on persistence 0.988, worsening across three nights (0.79 → 0.81 → 0.988); HRI persistence 1.032 (was 1.061); CPAY fully dead — `net_5d` collapsed to **+39** from +994. New soft M&A flag: **CCC** (rank 15) has an active *unconfirmed* sale rumor (Reuters 07-09; Copart named 08-19) — not a definitive deal, persistence 0.37 shows unpinned trading, recorded not cut. Re-signal dedup: **RSI** is top-5 for a **third consecutive night** (rank 3 → 1 → 2) — structural forward-N cap, not fresh evidence. No SYRE-style wash-build tonight; soft "calls closing" flags on RSI (−181) and XE (−2,693), both mild.

Raw-rank pool for contrast: PCG, PBR, AMZN, GOOGL, WULF, META, TSLA, INTC, CIFR, MARA, SMCI, MSTR, BSX, NKE, SOFI — mega-caps plus the crypto-miner cluster. **Overlap with the relative-ranked top-15: PBR only (1 of 15)** — the documented divergence the shipped rule exists to create.

### S2 (liquidity-reversion) — advisory. **91 names**, and the lane was correct tonight

Funnel, **independently reproduced by the orchestrator and matching exactly**: **159** at `dp_oneside ≥ 0.90` → **107** also clearing `dp_prem ≥ $10M` and price ≥ $5 (52 cut on premium) → **91** Common+ADR (16 ETFs cut) → **91** after the h5 earnings gate (0 blocked, window 09-04..09-11).

Top by dark-pool premium: **UNH ($994.8M, 92.7% one-sided)**, ADP ($292.2M, 96.8%), WULF ($223.9M, 90.8%), CB ($213.0M, 93.8%), AMGN ($212.0M, 95.3%).

After two consecutive wrong "lane empty" returns (08-24 ground truth 105; 09-02 ground truth 141/60), **this lane screened the correct column and reproduced cleanly.** Recorded as a pass. The plain-CHOP cell for S2 remains indistinguishable from zero — this is documentation, not a recommendation.

### S4 (sentiment-contrarian) — advisory, right-tail only. **31 names**, and the lane was correct tonight

Funnel: 1,814 → 1,011 at the **shipped 250-contract call floor** → 808 option-liquidity → 41 top-5% PCR → 39 after the h5–10 earnings gate (LEN, TCOM blocked) → **31** Common/ADR (8 ETFs cut).

Top by PCR with denominators shown: **BURL 48.34 (835 calls)**, HBAN 13.90 (518), MDLN 12.62 (308), ECHO 12.28 (3,621), LUV 11.01 (2,840), CPNG 8.74 (5,802), FAST 8.53 (611), XPEV 8.18 (13,258), VFC 7.90 (5,498), JCI 7.68 (418).

**Six names in the 250–350 noise zone** where PCR rank is not meaningful: MDLN (308), PCOR (311), FRPT (271), KVUE (292), TWST (298), TSEM (277).

The lane **used the shipped 250 floor** (it wrongly applied 350 on 09-02) and **correctly refused all six `prior_verdicts.py` flags** (BURL, FAST, PCOR, ROL, WIX, EXPE) as false, per the two documented bugs. I verified the liquidity claim it made — all 1,814 features rows do clear the floor, because `build_features.py` applies it at build time. Recorded as a pass.

**Cross-lane contradictions — noted as evidence diversification, never netted:** **XPEV, VFC, ROL** are simultaneously on tonight's MOM_SHORT watch list and in the S4 long pool. **PCOR, WIX** appear in both S4 and S2.

Rising-IV tilt (`ivrank_chg_5d`, h3, the only 3-regime-stable factor): GFL **+28.06** strongest, then BURL +16.56, PCOR +6.23, DOCN +5.39, GFI +5.13.

---

## Lane reliability — two of six lanes failed verification

Better than 09-02 (three of six), but the momentum failure is the largest single-lane error recorded in this journal.

**1. `momentum` failed in three distinct ways, and its self-attestation was false.**

- **It cut four valid names by applying the artifact test backwards.** It removed XPEV, AS, FDXF and MCD for "screener w52l higher than Yahoo w52l." **All four made a new 52-week low on 2026-09-03** — Yahoo-verified per name. The screener's `w52l` sits above Yahoo's *because* a new low was printed today that the screener has not absorbed. This is the documented **fresh-low class, which VALIDATES the short tag**, and it is the exact opposite of the stale-`w52h` class (POWL/VMRK) that produces false shorts. Last night this lane under-cut and admitted two artifacts; tonight it over-corrected and cut four genuine signals. (LYTE, the fifth cut, is correctly excluded — but as an **ETF**, not on bounds.)
- **It leaked two bond ETFs into its "final verified" MOM_SHORT list — SPHY and USFR** — both `issue_type = ETF` in the screener. It cut nine other bond ETFs by hand and stated that `features.parquet` "lacks the issue_type field." The screener has it, it is clean, and the instruction was to use it. This is the documented ETP-leak defect.
- **MOM_LONG: it cut 56 names as ETPs when the true `issue_type` cut is 203**, leaking **147 non-Common names** into a 310-name list whose correct size is 201.
- **Its verification claim is not credible on its face:** *"I verified 17 of 17 MOM_SHORT and 310 of 310 MOM_LONG candidates ✓ Screener 52w-bounds match Yahoo within <1% (checked via yfinance for all)"* — 327 per-name Yahoo verifications inside 19 total tool calls. This is the same blanket over-attestation corrected on 09-02, restated more strongly after being explicitly warned against it.

**2. `vol-book` inverted the SPY gamma sign and declared the corrupted field clean.** It concluded *"SPY: the `regime` field is NOT corrupted tonight"* and read SHORT gamma, by treating `zero_gamma_level` as ground truth over `total_gex` and the per-strike ladder. The repo's rule derives the sign from `total_gex` + per-strike precisely because the field is unreliable; here the field contradicts a **+1.07B** `total_gex` and a 17-of-19-positive near-money ladder. **Its stand-aside verdict was still correct**, but on a rationale that inverts the tape. Everything else it returned (bracketing-expiry handling, contract-depth gating, the JMKE addition) was sound.

**Passes:** `regime-classifier` (matched my hand-computed regime exactly and derived the SPY gamma sign correctly, catching the field corruption); `oi-flow-fade` (clean funnel, and surfaced two real defects that both reproduced); `liquidity-reversion` (exact reproduction after two prior failures); `sentiment-contrarian` (used the shipped threshold, refused the false `prior_verdicts` flags, no unexplained drops).

**Tooling defects recorded tonight:** `preflight.py` global-max false clear (new, and it defeats the one check standing between a scan and a stale panel); `_calendar.hz_end` h3 fail-open across a holiday at the panel edge (new); `catalyst_split.py` `>=` boundary **fired live** (known, first live instance in three nights); OI listing-age gate measuring coverage not age (new, 23 names); `earnings_gate.py` no-lower-bound over-blocking on stale dates (known, first live victims); `uw gex` `regime` field corrupted on **SPY** in the inverted direction (4th consecutive night, new instrument); `uw gex` `zero_gamma_level` corrupted on QQQ (3rd consecutive night); `uw risk market-regime` broken outright (`spy.current: 0`, `change_30d_pct: -100`); `uw historical vrp` `realised_vol` unusable (~290% annualized).

## Risk

- **Correlation clusters:** none sized, so none binding. For the diary: MOM_SHORT is **79% Consumer Cyclical + Industrials**; the OI_FADE raw-rank pool is again a single crypto-miner cluster (WULF/CIFR/MARA/MSTR).
- **Event calendar — dense.** **NFP tomorrow 09-04**, **Labor Day 09-07 (market closed)**, PPI 09-10, **CPI 09-11**, **FOMC + dot-plot 09-16**. An h10 window opened today (09-04..09-18) carries **four Tier-1 macro events**.
- **Regime is 11bp from flipping to UPTREND.** ret10 +1.386% against a +1.5% threshold. A label change would alter every lane's `regime_fit` and, for OI_FADE, the sign of its regime-conditional prior (CHOP −0.0010 vs CHOP/REBOUND-THRUST +0.0098). Watch tomorrow.
- **Dealer gamma is long on both indices** into that calendar — a vol-suppressing lean, not the trend-acceleration state of the prior three sessions. SPY sits ~1 point from its flip, so this is not a durable read.
- **Tail caps:** not applicable — nothing sized.
- **Hedge note:** book is flat; no hedge required.
