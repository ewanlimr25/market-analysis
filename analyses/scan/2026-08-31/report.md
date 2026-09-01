# Market Scan — 2026-08-31

## Regime & Verdict

- **Regime: CHOP** · ret5 +0.470% · ret10 −0.730% · dd15 −1.300% · `directional_tradable=true` · `s1_standdown=false`
- **Vol-state:** VIX 14.92 (+3.40% on the day), **LOW tercile** on `zerodte_setup.py`'s own trailing-60 definition. SPY VRP −0.06pp (FAIR); QQQ VRP −4.39pp (iv30d 16.67% vs realized 21.05% — QQQ implied is running *under* realized). Both SPY and QQQ dealer **SHORT gamma** (derived, see Risk).
- **Breadth:** 27.0% green (136 adv / 362 dec / 5 unch), median −0.69%, concordant with SPY −0.30% — not a distribution tell.
- **Tape:** SPY 767.05 (−0.30%) · QQQ 716.76 (+0.05%) · IWM 293.93 (−0.62%). Ten-session dispersion is the story: QQQ −1.80%, SPY −0.73%, **IWM −3.33%**.
- **Bottom line: No directional edge today. Sixteenth consecutive flat session.** No lane in this repo sizes; the directional book is empty by construction, not by failure to find names.

## Directional Book (excess-scored)

**EMPTY.** No lane sizes. `risk-sizer` was not spawned — with zero sized candidates Phase D is vacuous — and `fundamentals-gate` was correctly not spawned, since it runs only on names about to be sized.

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

## Vol Book (non-directional)

Delta-neutral, advisory, quoted net of cost, zero directional points.

**0DTE-VRP — STAND ASIDE on both SPY and QQQ.**

Dealer gamma derived by hand from the per-strike book (the repo's documented convention is *spot vs the zero-gamma flip*, **not** the sign of aggregate `total_gex` — `zerodte_setup.py:14`):

| | total_gex | cum. net gex at strikes ≤ spot | flip in listed range | spot | derived |
|---|---|---|---|---|---|
| SPY | −1.034B | **−8.19e8** | none (742–791) | 766.92 | **SHORT gamma** |
| QQQ | +0.197B | **−2.30e8** | **720.0** | 716.17 | **SHORT gamma** (spot below flip) |

LOW-tercile conditional gross expectancy (never the pooled headline — the pooling trap): SPY +0.142%/day, QQQ +0.202%/day; less ~0.10% round-trip → +0.042% / +0.102%. **Both stand aside anyway**: that backtest bucket is stratified by VIX tercile only, *not* by gamma regime, and tonight is the short-gamma trend-acceleration state whose left tail the Mar–May validation sample never priced. QQQ carries the second independent reason (VRP −4.39pp, realized above implied).

**Earnings IV-crush**

| Ticker | Print | IV rank | Bracketing expiry | Tool `implied_move_perc` | ATM-straddle median-IV **floor** | Verdict |
|---|---|---|---|---|---|---|
| MDT | 2026-09-01 | 97.9 | 2026-09-04 (4 DTE, brackets cleanly) | 4.72% | **6.80%** | Advisory sell-vol candidate — defined-risk iron fly, wings well beyond 6.8% |
| NTAP | 2026-09-02 | 94.1 | 2026-09-18 (18 DTE) | 10.23% | n/a | **SKIP** — no expiry brackets the print; nearest is 16 days past it, so any structure prices non-event vol |

MDT's raw figure understates the straddle floor by ~1.4×, consistent with the TPR precedent that the raw-IV move is a **lower bound**, not an estimate. Size for realized potentially running 1.3–1.5× the floor.

## Watch / Stood-down

- **OI_FADE — STOOD DOWN, diary-only.** Zero candidates, zero watch list, empty slate to the sizer. Funnel: 1,667 liquid → 1,612 (earnings gate) → 1,298 (`issue_type`) → 463 (build floors) → 437 (listing age) → **299** (persistence). Diary-only top ranks: CPAY, VSNT, FRT, HRI, RSI — none is a suggestion.
- **MOM_SHORT — watch-only, never sizes.** A cohort of names printing **fresh 52-week lows today**: PCG, KRMN, WYNN, LII, MLM, VICI, NRG, ESAB (all Yahoo-verified, all made new lows on 2026-08-31). Earnings gate: 23/23 pass (nothing prints inside h10 — post-season).
- **MOM_LONG — basket/watch only.** ~140 names after filters; energy (SLB, VLO, DINO, MPC, PSX) and software (CRWD, TEAM, DT, OKTA) lead. APGE / CRNX flagged for a deal-pinned check (near-flat realized vol at the 52w high).
- **S2 (liquidity-reversion) — advisory.** 9 names: RPM, CSL, CNC, SNA, DOX, FTV, CART, VSNT, SMG. Regime-conditional excess in CHOP is **−0.0001 (29 exit-days, t=−0.02)** — indistinguishable from zero.
- **S4 (sentiment-contrarian) — advisory, right-tail only.** 15 names; CHOP cell **+0.0053 (29 exit-days, t=1.18)**. `hit − base = −0.056` on the panel: **the lane has never had a hit-rate edge.**

## Risk

### The substantive finding tonight: `lane-exit-day` clustering does not correct for overlapping h10 windows

Every OI_FADE_LIVE exit-day is base-pinned (0.00 or 1.00) **by construction** — the lane fires 15 names on one signal date at one horizon, so all 15 share a single SPY window and `base_hit` can only be 0 or 1. More importantly, consecutive exit-days share **9 of their 10 return days**. Thirty `lane-exit-day` is therefore nothing like thirty independent observations, and the repo's iid-clustered t overstates every h10 significance claim:

| lane | exit-days | mean | iid-clustered t / p (**current method**) | Newey-West(9) t / p | non-overlapping blocks |
|---|---|---|---|---|---|
| OI_FADE_LIVE | 30 | −0.0094 | −2.41 / **0.016** | −1.52 / **0.128** | 2/10 offsets sig. |
| MOM_SHORT | 69 | −0.0122 | −2.24 / 0.025 | −1.35 / 0.178 | 3/10 offsets sig. |
| MOM_LONG | 89 | −0.0115 | −1.96 / 0.050 | −1.29 / 0.198 | 2/10 offsets sig. |

Caveat on the correction itself: Newey-West is badly biased at n=30, and the block test has only 3 observations per offset. Neither is authoritative. But they agree, and the direction of the bias is not in doubt.

### The pre-registered OI_FADE_LIVE re-check has FIRED — and it splits

`OI_FADE_LIVE` reached **exactly 30 `lane-exit-day`** tonight, the bar set in `docs/regression-gate.md`. On the repo's current method it satisfies pre-registered outcome #1 (still negative, p=0.016) → formal Step-3 STOP. Under the overlap correction it satisfies neither cleanly (p=0.128).

What is **not** in doubt: the **sign**. Negative on 9 of 10 non-overlapping block offsets; −0.0071 (p≈0.057) after dropping MSTR/CELH/MARA. **The stand-down stands** — a negative point estimate is ample reason not to size. What does not survive is the *significance* claim, and it should not be promoted to "BH-surviving formal STOP" at the 09-05 audit on the iid p-value alone. Note this cuts at the 2026-08-29 evidence too, whose p=0.028 was computed the same way.

Sub-cohort check: exits ≤08-07 (before both recent one-way increments) read **−0.0014, 14 exit-days, p≈0.83**. The negative sign is concentrated in the last two increments.

### Regression gate — informational; no lane or threshold changed tonight

`retro_harness.py --all --oi-variant both`, 99 panel days (baseline was 93, →08-21):

| lane | baseline | tonight | Δ |
|---|---|---|---|
| MOM_LONG | −0.0118 (1213) | −0.0120 (1294) | −0.0002 |
| MOM_SHORT | −0.0138 (830) | −0.0129 (888) | **+0.0009** |
| OI_FADE | +0.0013 (1177) | −0.0017 (1267) | **−0.0030** |
| S2 | +0.0018 (1269) | +0.0010 (1347) | −0.0008 |
| S4 | +0.0024 (1304) | +0.0020 (1394) | −0.0004 |

**Do not re-baseline.** Restricting to exits ≤2026-08-21 reproduces the recorded baseline essentially bit-exactly — OI_FADE **+0.0013 (n=1177)** and S4 **+0.0024 (n=1304)** are exact; MOM_SHORT −0.0137 (828), MOM_LONG −0.0122 (1209), S2 +0.0016 (1259). No code drift; every pooled move is the new maturity-edge cohort.

That cohort is **one correlated draw**: 6 exit-days (08-24→08-31), `base` pinned **0.00 long / 1.00 short — SPY fell in 100% of the new h10 windows** — and all five lanes negative in it (MOM_LONG −0.90%, MOM_SHORT −0.15%, OI_FADE −4.01%, S2 −0.78%, S4 −0.51%). This is the pre-registered pinned-base signature. **Pre-registering the unwind:** when a mirror increment arrives (SPY up across its h10 windows, `base` pinned 1.00 long / 0.00 short), expect OI_FADE's pooled figure to recover toward +0.0013 and MOM_SHORT to give back its +0.0009 — neither will be decay nor a fix.

### Lane defects caught tonight

1. **Momentum leaked ETPs again** — SCHR, BNDX, IEF, BIV are all `issue_type = 'ETF'`. The screener's clean field exists; the lane rolled its own sector filter. Same defect as 2026-07-29.
2. **Momentum misquoted its own CHOP cell** — reported MOM_SHORT CHOP excess as −2.20% while quoting the matching row/unit/t figures (282 rows, 24 exit-days, t=−1.93). The actual cell is **−1.77%**; −2.20% is the whole-book `exit-session` figure from CLAUDE.md. MOM_LONG's −2.66% checked out (−2.65%).
3. **Momentum wrongly claimed the earnings gate was unavailable** — `scripts/earnings_gate.py` ran fine, 23/23 pass.
4. **Momentum mischaracterized the 52w-range defect.** It cut PCG as a "false short / data artifact". PCG's true `pct_52w_range` is 3.0% — it *is* near its 52-week low. All eight verified names printed new 52-week lows **today**, so the out-of-range screener readings are **same-day staleness that validates the short tag**, the opposite of the known in-range-but-wrong class that manufactures false shorts. Both classes exist; they need different handling.
5. **`zerodte_setup.py` emitted `sell_premium=True` for SPY tonight** off the corrupted CLI `regime` field (reads POSITIVE against total_gex −1.03B) and a garbage `flip=305.49`. The known 0DTE gamma-sign bug, firing live and overridden here. `zero_gamma_level` is corrupted on both names (305.49 / 212.59 against spot 767 / 717, both far outside the listed strike ranges 742–791 / 695–738).
6. **Phase A read QQQ gamma off the aggregate sign** (+197M → "LONG gamma"), the exact error mode `zerodte_setup.py:14` documents. Cumulative-to-spot is −2.30e8 with the flip at 720 → SHORT. Corrected above.
7. **S4's INFY rests on the denominator floor** — PCR 20.68 on **251 calls** against a floor of 250, in a $206.7M-ADV name. The 2026-08-17 floor fix moved the threshold but this is the same artifact class one contract over the line. Only RCL (8,264 calls / 29,588 puts) carries a book deep enough for its PCR to mean anything.
8. **Screener `issue_type` is NULL for SUNB and MAIR**, both genuine operating common stocks; they fail closed out of OI_FADE. Correct behaviour, but a screener-hygiene note.
9. **`catalyst_split.py`'s `>=` print-day boundary caught live on DCI** — `>=` read LIVE_BUILD (213% post-catalyst, counting the 08-26 print day itself); strict `>` gives **1.8%** → RESOLVED_PRE_PRINT. DCI was independently persistence-cut, so tonight's cohort is unchanged, but it is a clean reproduction of the EWTX defect.

### Correlation, events, carry

- No correlation clusters to collapse — the book is empty.
- **Event calendar (h10):** JOLTS 09-01 · **NFP 09-04 (Tier-1, inside the horizon)** · PPI 09-10 · CPI 09-11 · FOMC convenes 09-15.
- **Open call rows:** FDX/GEN/BSY/ITRI (entered 08-14) matured at h10 on **2026-08-28** — CLAUDE.md records "~08-31"; the trading-day count says 08-28. AS (entered 08-19) matures **2026-09-02**. All five will be resolvable at the 09-05 audit.
- Held-book reconciliation against `conviction_2026-08-28.json` read 0 positions. Verified genuine (not the EXIT-substring bug) by reading the file directly: `book_state.positions == 0`.
- Re-signal dedup confirmed again: FRT (rank 13→14→3), DKS (4th straight session oscillating across the persistence gate), BZ, AS (41 mentions since 08-17, never sized). The lane's forward N is structurally capped, as recorded.
