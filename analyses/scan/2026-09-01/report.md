# Market Scan — 2026-09-01

## Regime & Verdict

- **Regime: CHOP** (plain, *not* CHOP/REBOUND-THRUST) · ret5 **−0.540%** · ret10 **−0.740%** · dd15 −0.740% · `directional_tradable=true` · `s1_standdown=false`
  — `scripts/regime_check.py --date 2026-09-01`, confirmed against the harness's own `classify_regime` (`retro_harness.fire`).
- **Tape:** SPY 761.78 (**−0.687%**) · QQQ 707.64 (**−1.272%**) · IWM 290.57 (**−1.143%**). Ten-session dispersion: QQQ −1.38%, SPY −0.74%, **IWM −3.22%** — small-caps still leading down.
- **Vol-state:** VIX **16.34, +9.52% on the day** (range 14.95→16.80) — a real vol pop off yesterday's 14.92. **MID tercile** on `zerodte_setup.py`'s trailing-60 bounds [15.8, 17.3]; yesterday was LOW. VRP: SPY +1.06pp (FAIR), QQQ −2.54pp (FAIR, realized above implied). **Both SPY and QQQ dealer SHORT gamma** (derived by hand, twice, independently — see Risk).
- **Breadth:** 1,409 adv / 4,457 dec (n=5,932 non-index), median **−1.01%**, mean −1.27% — **24.0% green** on the full panel (adv/(adv+dec)); `fz breadth` reads 31.4% green on the narrower S&P-500 universe. Two universes, not a contradiction. Concordant with a red tape — **not** a distribution tell. Note the median stock fell harder than SPY: broad-based selling, not narrow mega-cap weakness.
- **Bottom line: No directional edge today. Seventeenth consecutive flat session.** No lane in this repo sizes; the directional book is empty by construction, not by failure to find names.

## Directional Book (excess-scored)

**EMPTY.** No lane sizes. `risk-sizer` was not spawned — with zero sized candidates Phase D is vacuous — and `fundamentals-gate` was correctly not spawned, since it runs only on names about to be sized.

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

## Vol Book (non-directional)

Delta-neutral, advisory, quoted net of cost, zero directional points.

### 0DTE-VRP — STAND ASIDE on both SPY and QQQ

Dealer gamma derived by hand from the per-strike book by **two independent agents**, which agreed:

| | total_gex | cumulative net GEX at strikes ≤ spot | flip in listed range | spot | derived |
|---|---|---|---|---|---|
| SPY | **−1.597B** | negative at every strike (737–786) | none below spot; turns positive ~769 | 761.49 | **SHORT gamma** |
| QQQ | **−1.064B** | negative at every strike (685–730) | none below spot; turns positive ~719–720 | 707.58 | **SHORT gamma** |

MID-tercile conditional gross expectancy (never the pooled headline — the pooling trap): SPY +0.202%/day, QQQ +0.326%/day; less ~0.10% round-trip → +0.10% / +0.23%. **Both stand aside anyway**: that backtest bucket is stratified by VIX tercile only, **not by gamma regime**, and tonight is the short-gamma trend-acceleration state whose left tail the Mar–May validation sample never priced.

### Earnings IV-crush — 4 advisory candidates

All four print inside 1–2 sessions; nearest listed expiry for every one is **2026-09-18 (17 DTE)**, which sits *after* the print and therefore does capture the event. Because a 17-day wrapper on a 1-day event dilutes the raw figure, the event variance was isolated
(`σ_event² = σ_front²·T_front − σ_back²·(T_front−1)`) rather than read off the front straddle.

| Ticker | Print | Front-end IV ratio | CLI `implied_move_perc` | Variance-isolated floor | Verdict |
|---|---|---|---|---|---|
| NTAP | 2026-09-02 | 1.299 (73.9%/56.9%) | 10.43% | 10.18% | advisory sell-vol, wide-wing iron fly |
| AGX | 2026-09-02 | 1.205 (104.2%/86.4%) | 15.06% | 12.81% | advisory sell-vol |
| OLLI | 2026-09-02 | 1.261 (72.8%/57.7%) | 10.30% | 9.63% | advisory sell-vol |
| VSXY | 2026-09-03 | 1.272 (94.4%/74.2%) | 13.85% | 12.66% | advisory, **size down** — back months only 20–21 contracts |
| BIOX | 2026-09-08 | — | 424% (artifact) | — | **SKIP** — `expiry_count=1`, `contract_count=1`, `INSUFFICIENT_DATA` |

Both figures are a **floor, not an estimate** (TPR realized 16.5% vs a 12.2% raw estimate ≈1.35×; MDT ~6.8% vs 4.72% ≈1.44×). Wings sized at ~1.4–1.5× the higher of the two. MDT is correctly off tonight's list — it printed today.

## Watch / Stood-down

- **OI_FADE — STOOD DOWN, diary-only.** Zero candidates, zero watch list, empty slate to the sizer. Funnel: **1,810** liquid → 1,757 (earnings gate) → 1,349 (`issue_type`, Common Stock + ADR — the pool the shipped rule actually joins on) → 597 (build floors) → 588 (listing age) → **354** (persistence). Diary-only top ranks by `oi_rel_build`: **VSNT 0.969/pers 0.79, CPAY 0.919/0.50, RSI 0.824/0.61, HRI 0.764/0.52, XE 0.702/0.42** — **none is a suggestion.**
  - **Re-signal dedup confirmed again, and the oscillation moved gates.** Four of last night's top five (VSNT, CPAY, RSI, HRI) recur. **FRT dropped out at a *different* gate than before** — its `net_5d` fell to +828, under the 1,000-contract absolute floor, so it was cut at build-floors rather than persistence. **DKS** cut on persistence 1.448 (worse single-day-block read than its last 0.986). **BZ** cleared `issue_type` for the first time as an ADR, then failed on persistence 1.338 *and* a negative last call_net. **AS re-signals at #9** while its 08-19 call row is still open. This is the structural forward-N cap, not new evidence.
  - **Soft diary flag on VSNT (rank 1):** `oi_build.py` prints `last call_net NEGATIVE — calls genuinely closing`, and 79% of its 5-day net (3,123/3,950) landed on 08-31 alone. Not a call; a note that the rank-1 name's build is one-day-dominated and already reversing.
  - `catalyst_split.py` — all 15 survivors read `NO_CATALYST_IN_WINDOW`; no earnings date falls inside the 08-19→09-01 build window, so the known `>=` print-day boundary bug is **structurally inert tonight** (no boundary to mis-handle) and no strict-`>` re-sum was needed.
  - The **raw-rank** pool for the same date is NVDA/PBR/PCG/META/INTC/AMZN/WMT — the documented mega-cap QQQ-beta trap, and the reason the shipped rule does not rank that way.
- **MOM_SHORT — watch-only, never sizes.** 19 names, **all Yahoo-verified as printing NEW 52-week lows today**: BLDR, MLM, QXO, CPRI, AMRZ, ONON, CRH, RUN, LII, INIO, JMKE, CCL, ESAB, KRMN, WYNN, VICI, BEPC, NKE, FDXF. All 19 are `issue_type='Common Stock'` (orchestrator-verified — zero ETP leakage, unlike 08-31). All 19 pass the h10 earnings gate. **POWL cut** as a genuine class-(a) artifact (screener `pct_52w_range` −3.32% vs Yahoo +36.16%, `w52_low_date` 2025-09-02).
- **MOM_LONG — basket/watch only.** 147 names after filters, all earnings-gated. Energy leads (+1.82%); Healthcare (−1.83%) and Technology (−3.59%) lag. No sector above the ⅓ cap.
- **S2 (liquidity-reversion) — advisory.** 11 names after gates: MA, TEL, OWL, FLUT, BX, SW, PPL, CHTR, VSH, VMRK, RY. HASI cut on the $50M ADV floor ($35.9M); ADP/XEL/ROST cut on blocking priors. Plain-CHOP cell **−0.05% row-level / −0.04% across 30 `lane-exit-day`, t=−0.09, p=0.93** — indistinguishable from zero.
- **S4 (sentiment-contrarian) — advisory, right-tail only.** 26 names. Plain-CHOP cell **+0.46% row-level / +0.45% across 30 `lane-exit-day`, t=+1.01, p=0.31**. `hit − base = −0.030` in CHOP and −0.056 pooled: **the lane has never had a hit-rate edge.** Seven names sit just above the 250-contract call floor (HBAN 494, ROST 508, EXEL 533, SW 450, RARE 374, KD 372, MTN 359, FAST 342, PNC 359) — **HBAN's PCR 26.27 rests on a 3.7% call share** and its rank is noise. Only WBD (21,910 calls / 66,451 puts), AGNC, NVS, HWM, PSKY, VFC carry books deep enough for PCR to mean anything.

## Risk

### The headline: the 31st `lane-exit-day` is a TRAP, and the re-check's p moved overnight on unchanged rows

Two separate things had to be untangled tonight, and the first one nearly produced a false headline in this very report.

**1. The 31st `lane-exit-day` must NOT be counted.** `OI_FADE_LIVE` fires exactly 15 names per signal date. Every one of the 30 complete exit-days has **15/15 resolved**. The forming 31st (exit 2026-09-01) has **4/15 resolved** — RKT, LKQ, AVT, NXPI, mean **+2.87%** — because `returns.parquet` has not yet resolved the other eleven. Counting it is the **mirror image of the partial-window artifact** the repo already banned on the lookback side in the 2026-08-22 OI_FADE re-baseline. And it is not a harmless rounding difference; it flips the pre-registered verdict:

| cohort | exit-days | mean | iid-clustered t / p | Newey-West(9) t / p |
|---|---|---|---|---|
| **complete days only (correct)** | **30** | **−0.86%** | **−2.17 / 0.0297** | −1.39 / 0.165 |
| including the partial 09-01 day | 31 | −0.74% | −1.84 / **0.0651** | −1.18 / 0.237 |
| complete, ex-MSTR/CELH/MARA | 30 | −0.63% | −1.68 / 0.0933 | −1.01 / 0.311 |

A four-name fragment of a fifteen-name day moves p from 0.030 to 0.065 — across the pre-registered 0.05 line. **Whoever runs the 2026-09-05 audit must exclude the forming exit-day or they will read the opposite verdict.** This is now the single most likely way to misgrade this lane.

**2. The same 30 exit-days moved overnight without gaining a single row.** Last night this cohort read **−0.94%, t=−2.41, p=0.016**. Tonight the identical 30 complete exit-days read **−0.86%, t=−2.17, p=0.0297** — no new observations, ~2× the p-value. The one thing that changed is that `prices.parquet` was rebuilt at the top of this scan (2,446 of 2,471 tickers priced; 25 unpriced). That is the repo's documented **non-idempotent vendor feed** — the same behaviour that made EQR resolvable at the 08-15 audit and un-resolvable a week later. Attribution to the rebuild is inference from timing, not a causal test; what is directly observed is that the cohort is not stable across re-derivations.

**What stands and what does not.** The **sign stands**: negative on the complete cohort, negative under Newey-West, negative after dropping the three crypto names, and negative on **8 of 10** non-overlapping block offsets. The stand-down therefore stands on its own terms. What does **not** stand is treating the significance claim as durable: it is iid-only (p=0.030 → 0.165 under NW), it is marginal ex-crypto (p=0.093), and it moved by 2× overnight on unchanged rows. Recommend the pre-registered re-check be recorded at the 09-05 audit as **CONFIRMED on sign, NOT DURABLE on significance** — and explicitly *not* as "BH-surviving formal STOP".

### Regression gate — informational; no lane or threshold changed tonight

`retro_harness.py --all --oi-variant both`, **100 panel days** (baseline was 93, →08-21):

| lane | baseline | tonight (full panel) | Δ |
|---|---|---|---|
| MOM_LONG | −0.0118 (1213) | −0.0119 (1298) | −0.0001 |
| MOM_SHORT | −0.0138 (830) | −0.0127 (894) | **+0.0011** |
| OI_FADE | +0.0013 (1177) | −0.0014 (1281) | **−0.0027** |
| S2 | +0.0018 (1269) | +0.0009 (1349) | −0.0009 |
| S4 | +0.0024 (1304) | +0.0017 (1396) | −0.0007 |

**Do not re-baseline.** Isolation check (exit date ≤ 2026-08-21, the cohort the baseline was measured on) reproduces it:

| lane | recorded baseline | baseline cohort tonight |
|---|---|---|
| OI_FADE | +0.0013 (1177) | **+0.0013 (1177)** — exact |
| S4 | +0.0024 (1304) | **+0.0024 (1304)** — exact |
| MOM_SHORT | −0.0138 (830) | −0.0137 (828) |
| MOM_LONG | −0.0118 (1213) | −0.0122 (1209) |
| S2 | +0.0018 (1269) | +0.0016 (1259) |

OI_FADE and S4 are bit-exact; the other three differ only in the 4–10 rows the nightly `prices.parquet` rebuild re-priced (25 tickers were unpriced tonight). **No code drift — every pooled move is the maturity edge.**

**Note the signal-date cut is the WRONG isolation here** and was checked and discarded: restricting *signal* dates ≤08-21 leaves the h10 lanes bit-identical to the full panel, because nothing signalled after 08-21 has matured yet. The baseline moved through **exits**, not new signals.

### The pinned-base cohort is unwinding, on schedule

The maturity edge is 7 `lane-exit-day` (08-24→09-01), and for every h10 lane **all 7 are base-pinned** — `base` 0.00 long / 1.00 short, i.e. SPY fell across 100% of the new h10 windows. That is the pre-registered correlated-draw signature, now in its second cycle. But the **unwind has started**: the last three exit-days reverse sign.

| exit-day | OI_FADE | OI_FADE_LIVE | MOM_LONG |
|---|---|---|---|
| 2026-08-26 | −6.07% | −4.67% | +0.67% |
| 2026-08-27 | −5.57% | −0.06% | +0.87% |
| 2026-08-28 | −0.95% | **+1.78%** | −6.19% |
| 2026-08-31 | **+1.03%** | **+0.65%** | −0.34% |
| 2026-09-01 *(partial — see above)* | +2.50% | +2.87% *(only 4/15 names resolved)* | +2.66% |

This is what was pre-registered on 08-22 and again on 08-31: **OI_FADE's −27bp is not decay**, and it should recover toward +0.0013 as the mirror windows mature. Do not read either direction as a lane changing.

### Lane defects caught tonight

1. **S4 reported a CHOP cell that cannot exist.** It returned −0.0008 on **n=1,064** rows. Only **584** of S4's 1,396 panel rows carry any CHOP label (plain CHOP 434 + CHOP/REBOUND-THRUST 150), so n=1,064 is arithmetically impossible. The true plain-CHOP cell is **+0.0046 row-level (n=434), +0.0045 across 30 `lane-exit-day`, t=+1.01**. The lane inverted the sign of its own regime cell.
2. **Momentum labelled row-level t-stats as `lane-exit-day` clustered.** It reported MOM_SHORT t=−4.27 and MOM_LONG t=−4.43 as clustered figures. Those are the **row-level** t's (n=288/358) and reproduce exactly as such; the genuine `lane-exit-day` clustered t's are **−1.85 (p=0.065)** and **−2.36 (p=0.019)** — and that is *before* the h10 overlap correction. This is the clustering trap in its cleanest form: same means, same rows, t inflated ~2.3×. Its means (−2.12% / −2.60%) and hit/base (0.37/0.32, 0.35/0.70) all reproduce exactly.
3. **S2 cited last night's CHOP cell instead of computing it**, despite being asked for a fresh derivation — it quoted −0.0001 / 29 exit-days / t=−0.02 from the 08-31 report. Tonight's actual figure is −0.0004 / **30** exit-days / t=−0.09. Directionally harmless, but a lane reporting a number it did not measure.
4. **S4 missed a blocking prior verdict.** It reported 6 blocking names (WOLF, DBX, CARR, CG, TD, TMO) and shipped **ROST at rank #5**; `prior_verdicts.py` flags ROST as carrying a prior blocking verdict, and the S2 lane independently cut it for the same reason. The two lanes disagreed on the same name in the same scan.
5. **The gamma-sign bug fired again — this time on QQQ.** `zerodte_setup.py` emitted `sell_premium=true` with `dealer_gamma_regime=LONG` and `gamma_source=cli` for QQQ, trusting a CLI `regime` field reading **"POSITIVE"** against `total_gex` **−1.064B**, with `zero_gamma_level=235.03` against spot 707.58 — ~472 points below spot and entirely outside the listed 685–730 strike range. Last night the same bug corrupted SPY; tonight SPY's field was clean and QQQ's was not, so the corruption is **not symbol-stable**. Note the script's own `gamma_disagreement` check returned **false** — it did not catch a flip level outside the listed strikes. That check is the fix worth writing.
6. **The bracketing-expiry verdict flipped between nights on identical facts.** NTAP (print 2026-09-02, nearest listed expiry 2026-09-18, 17 DTE) was **SKIPPED** on 08-31 as "no expiry brackets the print", and is an **advisory candidate** tonight. The facts did not change — the standard did. The documented trap is *expiry **before** the print*, which makes `implied_move_perc` read a no-catalyst window; an expiry 16 days **after** the print does capture the event and merely **dilutes** it, which is correctable by variance isolation rather than disqualifying. Tonight's handling is the correct one and 08-31's NTAP skip was over-strict.

### Correlation, events, carry

- **The MOM_SHORT cohort is two themes, not 19 names.** Industrials 7 (QXO, BLDR, KRMN, FDXF, LII, INIO, ESAB) + Basic Materials 3 (CRH, AMRZ, MLM) = **10/19 in the construction/building-products complex**; Consumer Cyclical 6 (NKE, CCL, ONON, WYNN, JMKE, CPRI). Under the ≥0.70 correlation rule this would collapse to ~2 positions if it ever sized. It does not size — but the concentration is the RESEARCH/50 §5.3 China-complex lesson repeating.
- **Event calendar (h10, 2026-09-02→09-16):** JOLTS/ISM 09-01 · **NFP 09-04 (Tier-1)** · **Labor Day 09-07, market closed** · **PPI 09-10** · **CPI 09-11** · **FOMC 09-15/16, decision + dot plot 09-16**. Three Tier-1 prints inside the window, FOMC at its edge.
- **Open call rows:** FDX/GEN/BSY/ITRI (entered 08-14) matured at h10 on **2026-08-28** (verified against the SPY trading calendar). AS (entered 08-19) matures **2026-09-02** — one session away, confirmed not yet reached. All five resolvable at the 09-05 audit.
- **Held-book reconciliation** against `conviction_2026-08-31.json` read 0 positions with SPY −0.69%. Verified genuine — not the EXIT-substring bug — by reading the file directly: `book_state.positions == 0`.
- **Dormant, not accruing** (do not re-derive): crash guard 20 guard-days / −0.58% / p=0.212, unchanged since 08-22 — the harness fired the guard on 20/100 panel days tonight, still no new guard-day since 08-07. Fundamentals VETO n=15 / −2.28%, CONFIRM n=23 / −1.21%, unchanged since 08-15.
