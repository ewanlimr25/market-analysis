# Market Scan — 2026-08-20

## Regime & Verdict
- **Regime: CHOP** · ret5 **−1.964%** · ret10 **−0.775%** · dd15 **−2.800%** · vol-state **MID VIX tercile** (VIX **16.01**, +7.52% from 14.89)
- `directional_tradable` = **True** · `s1_standdown` = **False**, but by only **~4bp** (the unconfirmed-dip arm needs ret5 < −2.0%; actual −1.964%)
- Regime arbitrated: `regime_check.py --date 2026-08-20 --claim-label CHOP --claim-ret10 -0.00775` → **exit 0**. Phase A independently re-derived all three metrics off live Yahoo closes (SPY **762.60**) and reproduced `_regime.py`'s exact `drawdown15` formula — this is a live read, not a stale-parquet fallback.
- Preflight **clear**: 5/5 UW groups present for 08-20; truth set **rebuilt tonight** (prices 355,288 rows / 2,446 tickers; features 178,003 rows / 2,488 tickers / **92 dates**) and reaches the trade date.
- Tape: SPY down **5 of the last 6 sessions** off the 08-13 high (777.88 → 762.60), now ~+0.2% above its 20dma. Breadth **confirms** rather than diverges — 31.2% green, 342 decliners vs 157 advancers, bullish_pct 34.6%. This is an early-stage pullback developing inside CHOP, not a single-index print.

**Bottom line: no directional edge today. Zero new starters — the book stays flat for a 9th consecutive session.** But tonight is not a repeat of the previous eight: **AS crossed into the measured population and became sizable for the first time**, then was stopped by a *different* gate. The adjudication moved one full step down the stack, and last night's stated rationale turned out to rest on a mischaracterization of the harness rule. Both are recorded below.

## Directional Book (excess-scored)

**Empty.** No name reached a sizing band.

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| AS | OI_FADE | short | h10 | **+0.0034 (established)** | 1.0 | **watch** | n/a — not sized | all hygiene PASS; **fundamentals VETO** |

## The AS adjudication — and a correction to last night's reasoning

### What actually changed: AS entered the harness's measured population
Last night AS was withheld on the stated ground that the OI_FADE prior is *"computed on the raw top-15 by `oi_net_5d`"*, against which AS ranked *"~26–30 of 1,174, roughly 2x outside."*

**That description of the harness rule was wrong.** I read the source rather than the summary. `retro_harness.py:96-111` applies its filters **before** ranking:

```sql
WHERE f.oi_net_5d IS NOT NULL AND f.close>=5
  AND f.close*f.avg30_volume>=50e6
  AND (e.ned IS NULL OR e.ned > hz_end(T,10))
  AND e.it IN ('Common Stock','ADR') AND e.idx=false
ORDER BY f.oi_net_5d DESC LIMIT 15
```

So the +0.0034 prior grades a **filtered** top-15, not a raw one. The raw ranking — which is what last night's "~26–30" came from — is not the population the prior was ever measured on. (The **08-18** scan had this right, describing the rule as "raw oi_net_5d top-15 **after** price≥$5, $-ADV≥$50M, earnings-clear"; the 08-19 write-up regressed to the raw framing.)

Reproducing that exact SQL for the last four sessions:

| Date | AS harness rank | top-15 cutoff | AS `oi_net_5d` |
|---|---|---|---|
| 2026-08-17 | >40 | 16,340 | — |
| 2026-08-18 | >40 | 15,663 | — |
| 2026-08-19 | **17** | 16,107 | 15,002 |
| 2026-08-20 | **15** | 18,310 | **18,310** |

**Last night's withhold was still the correct call** — AS was rank 17, genuinely outside — but it was right for a partly wrong reason, and the margin was one slot, not "2x outside." Tonight AS genuinely crossed. The 08-19 conviction file **pre-registered exactly this trigger** ("if AS's rank moves into the harness's actual top-15 population, which would make it inherit the measured prior"), so re-scoring it is the pre-registered condition firing, not re-litigation of a prior stop.

Tonight's harness population, verified: META, WULF, CIFR, AMZN, MARA, BULL, INTC, SOFI, RKT, CORZ, GOOGL, NOK, GME, SMCI, **AS (15)**. Next out: AAPL (16).

### Every hygiene gate passed, on the numbers
- **Build**: `net_5d +91,551` (call +119,911 / put +28,360) · `rel_build` **1.763** · persistence **0.603** · last call_net **+9,345** (positive — mechanical invalidation not fired). AS is simultaneously **#1 by the live lane's own `oi_rel_build` rule** among all liquid, non-ETP, persistence-clean names — the first convergence of the two rules on a single name.
- **Liquidity** PASS, script-sourced: **$32.53**, 20d $-ADV **$176.7M**.
- **Earnings** PASS: reports 2026-11-17, clear of the h10 window (2026-08-21 .. **2026-09-04**).
- **Catalyst-split** LIVE_BUILD on **both** boundary conventions. The 08-18 Q2 print sits inside the window; post-print net is **+41,700 strict (`>`)** and **+49,900 loose (`>=`)**. The two agree — no inversion of the EWTX kind. The second-largest day of the whole build (08-19, +33,349) is post-print.
- **Not deal-pinned / not mechanically explained**: no M&A, no ANTA stake change, no secondary; the lockup already expired 5/17/26.
- **Correlation** PASS: corr(AS, SPY) **0.322** over 30d, well under the 0.70 cluster threshold.

### Why it still did not size: the fundamentals veto
`fundamentals-gate` returned **VETO**. The underlying contradicts the short hard: 4/4 EPS beat streak, Q2 revenue **+32% YoY**, gross margin **65.6% (+710bps YoY)**, FY26 guidance **raised twice** (most recently at the 08-18 print), balance sheet delevered to **net cash $573M / $0 non-current borrowings** (verified against the Q2 6-K by hand, since `finnhub_enrich`'s `leverage_flag` is a known mislabeller), Street consensus "Strong Buy" with avg PT ~$50 against a $32.53 close.

Per Phase C, `score = validated_excess × regime_fit × (1 − fundamental_contradiction)` — the veto channel zeroes the score. **AS does not size.** The veto is the designated authority and was not overridden.

Worth recording alongside it, because it cuts both ways: the gate's own `key_risks` note the **Q3 EPS guide MISSED** ($0.31–0.33 vs $0.39 est), **Truist cut its PT $50→$42**, three senior execs sold in early August, and — in its own words — "the technical/flow read and the fundamental read are genuinely in tension here." Short float 7.38% / days-to-cover 2.77 / squeeze_pressure **LOW**, so the veto is not resting on squeeze risk. The price action is entirely consistent with the fade thesis: AS fell 36.73 (08-05) → 32.57 (08-17), popped to 34.02 on the beat-and-raise, then **gave the entire pop back today, −4.38%, with no identified company-specific news**. RSI14 39.2, `pct_52w_range` 26.1%, −23.9% off the 52w high.

### PRE-REGISTERED for the 2026-08-22 audit: does the fundamentals veto anti-select OI_FADE?
This is the structural question tonight raises, and it should be tested rather than argued.

The harness's OI_FADE population carries **no fundamentals veto**. The +0.0034 / hit 0.54-vs-0.38 prior was therefore measured across a top-15 that necessarily *includes* fundamentally strong, beat-and-raise names — because a heavy call build is very often *caused* by good news. If the live engine vetoes precisely those names, it is selecting on a variable the prior never conditioned on, and the live lane cannot realize the measured edge no matter how long it runs.

Note the specific reason given — "beat-and-raise, not a crowd to fade" — is a judgment about the *lane's thesis*, not a risk observation. A beat-and-raise is fully public information; chasing it with calls afterward is the archetypal crowded-call setup, and is categorically different from the RKT/ValueAct or AZN-rumor cases (non-public or mechanically-driven positioning), which the lane already excludes on its own. The gate's genuinely risk-flavoured findings here (Q3 guide miss, PT cut, insider sales) actually lean *toward* the short.

**Testable at the audit**: split the harness's historical OI_FADE calls by whether the name had a positive earnings surprise / raised guidance inside the build window, and measure realized excess in each bucket. If the beat-and-raise bucket carries the lane's edge, the veto is destroying the lane. If it drags, the veto is earning its place. **Propose-only — no code or gate changes tonight.**

## Vol Book (non-directional, delta-neutral, quoted net-of-cost)

**0DTE-VRP: STAND ASIDE on both SPY and QQQ — but the reason changed from last night, and it matters.**
- **Tercile correction.** `zerodte_setup.py`'s actual `vix_tercile_bounds` are **[16.0, 17.3]**. VIX 16.01 therefore sits in the **MID** tercile — by **0.01**. (Phase A carried a LOW-tercile bound of 16.1; the script's own value governs.) In MID, conditional net is **positive** for both: SPY gross 0.209% → **+0.109% net**, QQQ gross 0.348% → **+0.248% net**, after a 0.10% round-trip cost. So unlike the previous eight sessions, the VIX-tercile pooling trap is *not* what kills the trade tonight.
- **Both are killed on gamma instead.** Keeping the 08-05 distinction intact: *aggregate GEX sign* drives range/wing-width — SPY `total_gex −1.87B`, **FULLY_NEGATIVE**, `zero_gamma_level: null` (no flip in range); *spot-vs-flip* drives the sell decision — SPY reads **SHORT gamma**, the left tail this sleeve never sampled.
- **QQQ tool artifact confirmed, and it would have inverted the verdict.** The CLI reports `zero_gamma_level 208.83` against spot **710.77** — a "flip" 71% below spot, which is not a real crossover, and `zerodte_setup.py` naively read spot>flip as **LONG gamma** off that bad number. Verified directly against the per-strike book: `total_gex −777M` and **every strike from 689–715 around spot is net-negative**. QQQ dealers are **short** gamma, same as SPY. Overridden. QQQ additionally trips its own front-end backwardation caution (0DTE IV 1.35× VIX) — two independent vetoes, not one.

**Earnings IV-crush: four names now carry real net-of-cost quotes — advisory, not sized.**
The bracketing-expiry trap fired on **all four**; the CLI's `implied_move_perc` is **4–6× too low** in every case because it reads a pre-print window. Corrected to the **08-28** bracket (confirmed as the first expiry after each print):

| Ticker | Print | CLI `implied_move_perc` | Corrected ATM-straddle move | Iron fly, net credit | Max loss (net) |
|---|---|---|---|---|---|
| HPQ | 08-26 | 1.72% | **10.14%** | +7.82% | 7.35% |
| OKTA | 08-26 | 2.28% | **13.28%** | +7.71% | 6.45% |
| ADSK | 08-27 | 2.28% | **8.83%** | +5.01% | 3.86% |
| BBWI | 08-26 | 2.40% | **11.85%** | +8.24% | 9.79% |

These cross-validate against the audit's logged priors (OKTA ~14.4%, HPQ ~10.3%). Straddle price is the primary number; the median-IV annualized figure is used only as a sanity **floor**, per the TPR precedent (realized −16.5% against a ~12.2% raw-IV estimate).
**Not sized.** All four bracket expiries (08-28) sit *on top of* PCE + NVDA (08-26) **and inside Jackson Hole (08-27→08-29)**. That stacks a macro-vol tail on the idiosyncratic earnings tail at the same expiration — the unsampled-left-tail cap cannot be satisfied against two compounding binaries. **CM, A, EH** excluded outright: no expiry cleanly brackets their prints (08-21 is before, 09-18 dilutes with 3+ weeks of ordinary diffusion), so no defensible implied-move quote exists. **KTCC** excluded — 7 contracts total, untradeable.

**ROST resolved — calibration data, no P&L.** Flagged 08-19 with an implied-move **floor of 6.47%**, correctly not sized (no net-of-cost construction existed pre-print). Realized **−2.43%** close-to-close (234.69 → 228.99). Realized well inside the floor — a clean crush win the book did not take. Logged as a thesis calibration point, not a trade result.

## Watch / Stood-down
- **AS** (OI_FADE) — excess now **established and positive** for the first time; withheld on the fundamentals veto. Carried WATCH with a two-legged, sharper re-examine trigger (below).
- **MOM_SHORT** — 9 Yahoo-verified names: ALHC, AMRZ, APP, APTV, CMS, MLM, PEG, QXO, ROL. Watch-only capped, never sizes (knowingly negative-excess, the one recorded exception to the no-negative-lane invariant). **Data-quality note: 12 of 21 candidates (57%) failed live Yahoo 52w verification** — BWXT, CPRI, CRH, ESAB, FDXF, FRVO, GME, GXO, LII, MDLN, MIDD, ONON — on stale or un-split-adjusted `w52l`. That is the known false-shorts-only failure mode, and it remains the single dirtiest input in the engine.
- **MOM_LONG** — 86-name basket, never sizes; DURABLE-N bar unmet.
- **S2** — 92 names cleared all gates (advisory-only, never sizes). Recorded with a caveat: the lane itself reports **"IC ≈ 0: binary timing tag, not a magnitude signal — all passing names have equal reversion probability."** A 92-name list whose own ranking is non-informative is a cohort, not a watch list; treat the ordering as meaningless.
- **S4** — 37 names (advisory-only, never sizes). The **08-17 call-volume floor is verified biting**: cohort minimum call_volume **258** against the floor of 250, so the NWG-class artifact (PCR 682 on three calls) is genuinely excluded. hit−base remains negative (−0.044) — right-tail only, no hit-rate edge.

## Risk
- **Event stack inside any fresh h10 window (ends 2026-09-04):** PCE **08-26** + **NVDA earnings 08-26** (same day), then **Jackson Hole 08-27→08-29** with Fed Chair Warsh's first keynote on **08-28**. Three high-impact catalysts Wed–Fri of next week.
- **Both crash-guard arms are live from opposite sides**, which is itself a marker of an undecided tape: the unconfirmed-dip arm needs ret5 < −2.0% and sits at −1.964% (~4bp away); the rebound arm already satisfies its dd15 < −2% leg (−2.80%) and needs only ret5 > +1.5%. A dovish PCE, a strong NVDA print, or a dovish Warsh debut could each independently push ret5 through the rebound trigger intraweek — a live **squeeze vector against any short cohort opened tonight**. This is a substantive argument against opening an OI_FADE short into this window, independent of the fundamentals veto.
- **Correlation:** no clusters — nothing sized, and AS was a single name at corr 0.322 to SPY.
- **Tail caps:** vol-short sleeve not deployed; the four earnings iron flies are defined-risk but explicitly not sized against the compounding 08-28 macro binary.
- **Hedge note:** book is flat. No hedge required.

## Process notes
- **Regression gate run (no code changed tonight, so all drift is panel growth by construction — 89 → 92 panel days):**

| Lane | Tonight | 08-17 baseline | Δ |
|---|---|---|---|
| MOM_LONG | −0.0117 (n=1170) | −0.0127 | +0.0010 |
| MOM_SHORT | −0.0136 (n=822) | −0.0137 | +0.0001 |
| OI_FADE | **+0.0034 (n=1218)** | +0.0038 | −0.0004 |
| S2 | +0.0019 (n=1229) | +0.0014 | +0.0005 |
| S4 | +0.0017 (n=1262) | +0.0025 | −0.0008 |

  No regression: two lanes up, two marginally down, one flat, all within panel-growth drift and no code path touched. **OI_FADE remains the only lane with both positive mean and positive hit−base (+0.161)**; S2 (−0.034) and S4 (−0.044) are right-tail-only. Baseline **not re-adopted tonight** — that is the 2026-08-22 audit's call.
- **Data hygiene:** `~/Documents/Stocks/Stock Screener/stock_screener.parquet` (12KB, written 20:23) is **corrupt — no magic bytes at end of file**. The harness's `stock-screener-*.parquet` glob excludes it by naming pattern, so nothing is currently broken, but any naive `*.parquet` read of that directory dies. Flagged, not fixed.
- **Agenda for 2026-08-22 (`/calibration-audit`), now two items:**
  1. The **OI_FADE rule gap** — the live lane ranks by `oi_rel_build`, the baseline grades the filtered `oi_net_5d` top-15. AS converged both rules tonight for the first time, but the gap itself is unresolved and remains the repo's most important open item.
  2. **NEW — does the fundamentals veto anti-select OI_FADE?** Test spec written above. Propose-only.
