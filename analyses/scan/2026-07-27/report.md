# Market Scan — 2026-07-27

## Regime & Verdict

- **Regime: CHOP** · ret5 −0.400% · ret10 −1.350% · dd15 −1.470% (`scripts/regime_check.py`, the same function the harness gates on)
- **vol-state: NEGATIVE DEALER GAMMA / vol-amplifying.** SPY net GEX ≈ −$1.39B, QQQ ≈ −$0.84B. VIX 18.67, flat d/d. SPY VRP fair (+3.05 vol pts) — no premium edge either direction at the index. GEX/DEX fed the vol-state only; no directional read taken.
- **breadth:** 328 advancers / 175 decliners (65.2% green), avg +0.77%. But `uw risk market-regime` shows only **35.2% bullish flow tickers** — a green price tape *not* confirmed by options positioning.
- **`directional_tradable` = TRUE** (all four lane cohorts exist and are populated). **`s1_standdown` = FALSE (mechanical)** — see the caveat below, which is the most important thing in this report.
- **Bottom line: ZERO new starters. Three held-book actions — CLOSE ORCL, HOLD/TIGHTEN PLNT, CLOSE PRMB (found unreconciled).** Every directional lane came back empty or was rejected at arbitration.

### ⚠ The `s1_standdown` guard was silent through a cohort-level squeeze

Today was a **violent one-day junk/oversold squeeze concentrated in exactly the MOM_SHORT target cohort, and it was invisible at the index level** (SPY +0.02%). I recomputed this directly from `data/prices.parquet` + `features.parquet` after the momentum lane reported the opposite, and verified a sample against the Yahoo chart API (HUBS 204.89→223.01, DUOL 122.24→132.82). 1-day excess vs SPY, ETPs and bad-mcap rows removed, mcap > $1B:

| Cohort (`pct_52w_range`) | n | mean excess | median excess | % positive |
|---|---|---|---|---|
| **0–10% (MOM_SHORT target)** | **87** | **+3.11%** | **+2.61%** | **89%** |
| 10–90% (control) | 486 | +0.62% | +0.62% | 64% |
| 90–100% (MOM_LONG target) | 38 | −0.06% | +0.20% | 55% |

A clean monotonic gradient — the more beaten-down the name, the harder it bounced. **The 52-week-range factor's normal sign (rank-IC t=+6.8, high beats low) was inverted today.** The cohort's trailing 5d/10d were unremarkable going in, so today *is* the event, not a multi-day thrust already in progress.

The mechanical guard reads **SPY's** ret5 (−0.40%, nowhere near the −2% trigger) and is therefore correctly silent — **the guard is index-level and structurally blind to a cohort-level squeeze.** It is not wrong; it is measuring the wrong object for this risk. Logged for `/calibration-audit`; not changed here, since a gate change requires the regression gate.

MOM_SHORT new starters were already watch-only capped, so **the inversion cost the book nothing on the entry side.** It bears only on the held ORCL short.

## Directional Book (excess-scored)

No new positions. Three actions on carried risk.

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| **ORCL** | MOM_SHORT | short | h10 | −0.03% mean (hit 0.48 vs 0.27) | 0.4 | **CLOSE (was half)** | Stop (close > $123.50, 2-day confirm) **NOT triggered**, +3.00% away — this is a proactive **horizon-driven** close, not a stop-out | liquidity PASS ($4.76B ADV) · cluster PASS · crash-gate PASS mechanically, **failed on substance** |
| **PLNT** | OI_FADE | short | h10 | +0.70% mean / +1.21% median (n=906) | 0.6 | **HOLD half** | Exit at the **earlier** of (a) **h10 = 2026-08-03 close**, or (b) first genuinely **negative `call_net`** print | liquidity PASS ($88.5M ADV) · cluster PASS · ER 08-06 now **outside** the horizon |
| **PRMB** | OI_FADE | short | h10 | +0.70% mean / +1.21% median | — | **CLOSE (unreconciled)** | Never fired across the entire hold | liquidity PASS ($63.3M ADV) |

### ORCL — CLOSE the remaining half, at tomorrow's open

Entry 2026-07-13 @ $131.54; trimmed 50% on 07-24 @ $114.99. Now **$119.90, +8.85% gross** on the remainder (was +12.58% Friday). Six reasons, in order of weight:

1. **The h10 validated horizon EXPIRES TODAY.** `hz_end('2026-07-13', 10)` = **2026-07-27**. MOM_SHORT's measured edge is an *h10* statistic; holding past it is unvalidated drift with no measured support. This alone is sufficient and is independent of today's tape.
2. Today's +4.27% (**+4.25% excess**) is a **cohort event, not idiosyncratic** — ORCL ranks **29th of 87** in the squeeze cohort (upper third; `risk-sizer`'s independent recount put it 18th of 67). A stronger-than-average participant in an *inverting* factor carries **more** forward squeeze risk, not less.
3. MOM_SHORT's negative mean **is** the momentum-crash tail. This is what it looks like arriving.
4. Tail stack against a 3%-away stop: **FOMC Wed 07-29 2pm ET**, **MSFT/META/ARM Wed AH**, **AAPL/AMZN Thu AH** — with ORCL deep in the AI-capex complex (ret10 −8.85%).
5. **A live mechanical squeeze vector.** ORCL's total GEX is fully negative (−4.68M, "strong gamma amplification"), gamma-flip 116 vs spot 119.90, and **net vanna is positive against a put-heavy public book — a further IV decline mechanically pulls in dealer buying**, independent of any fundamental catalyst. Term skew is still NORMAL (put_25d 71.2 vs call_25d 68.4), so no upside-call bid is priced *yet*.
6. Its own signal decayed: today's OI split was call +55,788 / put +55,144 = **net +644**, against ~+28k/day last week.

*Steelman considered and rejected:* ORCL is still only 2.2% up its 52-week range with RSI14 32.68 (oversold, not overbought), the stop has not triggered, and the AI-capex thesis is intact and arguably re-tested Wed/Thu. None of that survives the stack above — above all the expired horizon. Close at the open rather than working it: $4.76B ADV gives no execution-quality reason to wait, and every session of delay burns the two-session runway to FOMC.

### PLNT — HOLD at current size, exit tightened

$54.22, **+1.78% gross** (was +3.12% Friday). RSI14 55.34, `pct_52w_range` 22.3% — **not** a squeeze-cohort name; today's +1.38% sits near the mid-range control's +0.62% median, so this was not a factor event for PLNT.

The cut condition (a genuinely **negative** `call_net` print, not a put-driven net-of-puts wash) has **not** fired: tonight is call +118 / put +104 / net +14. But the build is **effectively dead** — net trajectory +750 → +395 → −4 → +180 → **+14**, with `oi_rel_build` 0.023 and `persistence_ratio` 0.562.

The exit is now the **earlier of h10 = 2026-08-03 close, or the first negative `call_net` print.** This replaces the prior open-ended 08-05 deadline and **removes the ER (08-06 pre-market) from the position entirely** — the horizon now expires before the print. It also stops the position drifting past its horizon the way PRMB did.

> Note on tooling: `hz_end('2026-07-20', 10)` returns **2026-08-04**, not 08-03. This is *not* a bug — the function is documented as extrapolating on a 5-day week past the panel edge and **deliberately rounding outward** (e.g. `hz_end('2026-07-24', 10)` returns a *Saturday*). It is a fail-closed **gating** window, so it is the wrong function to read a precise exit date from. Direct trading-day count gives 08-03 (no US holiday intervenes). Both precede the 08-06 ER, so nothing binds either way.

### PRMB — CLOSE; a silently-dropped winner, found tonight

The `oi-flow-fade` lane flagged a reconciliation gap and **it is real.** PRMB was opened as an OI_FADE **starter short on 2026-07-07 @ $24.90** (`analyses/scan/2026-07-07/decision.json`, tier MEDIUM, fundamentals CAUTION) and then **appears in no conviction or held-book file from 07-08 through 07-24** — it was never reconciled once across 12 sessions.

- Its **h10 horizon was 2026-07-21** ($23.69): PRMB −4.859% vs SPY +0.076% = **+4.94% short-excess. A clean OI_FADE win that was never recorded.**
- It then drifted 4 unreconciled sessions to today's **$22.85 (+8.23% gross)**.
- Its build was a single-day block anyway (`persistence_ratio` 0.986 — the 07-21 print was 98.6% of the 5d sum) and is long dead (+2 tonight).

**Treatment:** marked CLOSED at $22.85; **+4.94% recorded as the h10 graded outcome** for `/calibration-audit`. The extra +3.29pp of accidental post-horizon drift is **excluded from the lane's calibration credit** — the horizon-date figure is the lane's honest result; the four extra sessions were an accident, not a decision.

## Vol Book (non-directional)

Delta-neutral, advisory, **zero directional points**.

**Earnings IV-crush (SELL VOL, priced against the implied move):** the edge is where implied move *and* VRP are both rich — not where IV rank is high.

| Ticker | ER | Implied move | IV rank | VRP | $-ADV | Read |
|---|---|---|---|---|---|---|
| SIMO | 07-29 PM | 22.5% | 97.9 | **+0.318** | $181M | best crush setup |
| POWL | 08-03 PM | 20.0% | 92.3 | **+0.474** | $193M | richest VRP in set |
| MOD | 07-29 PM | 17.9% | 93.8 | **+0.382** | $382M | rich |
| STRL | 08-03 PM | 18.8% | 99.5 | **+0.243** | $548M | rich |
| PLNT | 08-06 AM | 11.3% | 89.3 | **+0.274** | $88.5M | rich — see note |

All: defined-risk iron fly / short strangle with **wings wide of the implied move**, sized for the two-sided binary tail, not the modal outcome.

**Stand aside on the IV-rank artifacts:** FORM (IV rank **100** but VRP only +0.054), KLAC (+0.063), UCTT (**−0.026**, FAIR), ALGM (+0.005, FAIR), COHU (+0.043). A high IV rank is a percentile-of-own-history statistic, not evidence the crush edge is fat. Do not lead on it. Dropped on the liquidity floor despite qualifying implied moves: BLZE, PUMP, DFH, ADTN, DHC, SPOK, EVER, OBE, HURN. BAND/ALGM/UCTT have thin chains (<100 front-expiry contracts) — a wide NBBO eats the edge; check live spreads before sizing.

**PLNT vol, separately from the directional short:** implied move **$6.12 / 11.3%**, VRP +0.274, term backwardation. A crush structure into the 08-06 print is legitimate **but must be booked and P&L-tracked as its own trade** — the directional short now exits at h10 (08-03), *before* the print, so the two never overlap. It is not a modification of the short and adds no directional exposure.

**0DTE-VRP, net of a stated 0.10%-of-notional round-trip cost:**
- **SPY** — vol_state HIGH, implied move 0.97%, iron condor wings ≈ ±1.2%, size 1.5×. **Net +0.158%** (gross 0.258%).
- **QQQ** — vol_state HIGH, implied move 1.68%, wings ≈ ±2.0%, **size halved to 0.75×** (front-end 0DTE IV 1.43× VIX, backwardation). **Net +0.281%** (gross 0.381%).
- Open-entry, hold-to-close, **never carry overnight** (QQQ's overnight leg is historically −0.081%).
- **STAND ASIDE WEDNESDAY 07-29 regardless of the morning's model read.** FOMC decision, 2:00pm ET. The validated 0DTE stack was never conditioned on a scheduled macro-binary afternoon — the same logic as the earnings gate, applied to the index book. Tuesday 07-28 stands as computed.
- **Tail caveat:** the 60-day validation sample contains **no vol shock**. The left tail is unsampled; net win-rate is not the promotion metric for a negatively-skewed short-vol book.

## Watch / Stood-down

- **MOM_SHORT — 54 names surfaced, ZERO starters.** Watch-only cap + a −0.03% mean + a regime_fit that collapses toward 0 on a day the factor inverted. Correct outcome.
- **MOM_LONG — basket DECLINED.** +0.18% mean with a **−1.06% median** is tail-driven and does not clear a MEDIUM bar, the near-high cohort was flat today (mean −0.06%), and the lane's own candidate table was unreliable (below). Not into FOMC + four mega-cap prints in 48 hours.
- **OI_FADE — zero candidates,** all cut cleanly on gates. CLYM (liquidity + ER 08-11), AVTR (ER **tomorrow**), TPG (ER 08-04), CBRG (leveraged single-stock ETP + sub-60d listing + liquidity), and 8 names cut as single-day blocks (`persistence_ratio` > 0.85: DLLL, TEX, ASIX, QNC, HRI, APGE, PRMB, SCHF).
- **ALLE — veto STANDS.** Build still positive and continuing (+221 net), no unwind, no guidance walk-back, PT raises have not reversed. **SSNC — exclusion STANDS** (build died at its 07-23 print). **TECH** — covered 07-23; re-entry only on a fresh organic build. **FHN** — fell out of the top-15 rank entirely.
- **S2 (liquidity-reversion) — 54 names, ZERO sized,** per its re-baselined +0.06% prior. Advisory only.
- **S4 (sentiment-contrarian) — its single fired name REJECTED at arbitration** (below). AGX advisory-only at best: PCR 5.86 is a real ratio, but `ivrank_chg_5d` is −4.02, which contradicts the rising-IV tilt.

## Lane defects found tonight (for `/calibration-audit`)

Four, all caught at orchestrator arbitration rather than by the lanes themselves:

1. **The momentum lane reported the cohort bounce BACKWARDS** — it claimed "median +0.01 bps, mean −0.28 bps, all moves within ±50 bps, ORCL idiosyncratic." The true cohort figures are **mean +3.11% / median +2.61% / 89% positive**. It had 1-day return data for only 28 of its 81 names, and "all moves within ±50 bps" is implausible for any equity cohort on any day — the return computation was broken, not merely thin. **This is the second consecutive session this lane has handed back a wrong tape figure** (07-24 was the stale-parquet regime inversion). Unlike 07-24, this one *would* have changed a decision if trusted: it argued for carrying ORCL.
2. **The momentum lane's ETP exclusion failed.** Its top-5 MOM_SHORT candidates were **TIP** (iShares TIPS bond ETF), **AAPD** (inverse AAPL), **BOIL** (2× nat-gas), **SKUU**, **SKHY** — all ETPs, in a lane whose prior was re-baselined *specifically* to remove ETP inflation. It also mislabelled a `close / w52h` ratio as `pct_52w_range` (reporting values like 1.1341 for a 0–100% quantity).
3. **S4's fired name was a divide-by-near-zero artifact.** PFGC's PCR of 90.06 comes from **call_volume = 16 contracts** against put_volume 1,441. Its OI-based PCR is 3489/2778 = **1.26** — no accumulated put-heavy positioning whatsoever. 1,441 puts cannot be "dispersed across strikes," as the lane claimed. The whole top of the PCR distribution is this artifact class (SLGN 714 on 14 calls, RAL 122 on 29, RSI 70 on 86). **The lane's liquidity floor is on the underlying's $-ADV ($197.9M, passes easily) — the wrong axis. It needs a minimum call-volume (denominator) floor.** REJECTED.
4. **S2 re-inflated its own prior**, characterizing its edge as "+0.5–1% vs SPY over 3–5 days" in the same report that correctly received the re-baselined **+0.06%**. It also called all 54 names LONG while ranking a mix of buy-side and sell-side one-sidedness, and wrote output to `/tmp` instead of the scratchpad. Harmless tonight (zero sized), but the list is not decision-grade.

**Also:** the PRMB reconciliation gap above is a **held-book** failure, not a lane failure — a live starter vanished from the journal for 12 sessions and was recovered only because a lane happened to surface the ticker for an unrelated reason. Worth a standing check that every prior `final_size != skip` name appears in the next run's reconciliation.

## Risk

- **Correlation clusters: none.** Trailing-60-session pairwise |corr| — ORCL/PLNT −0.042, ORCL/PRMB +0.002, PLNT/PRMB −0.326, all far below the 0.70 collapse threshold. **Gate blind spot noted:** ORCL's real risk driver is *cohort/factor* exposure (squeeze-cohort membership, ~0.49 SPY-beta as an AI-capex mega-cap), which pairwise book-correlation structurally cannot see. Not a rule violation — neither other name shares that factor — but it is the same class of blindness as the `s1_standdown` index/cohort gap above.
- **Event calendar (inside any fresh h10):** **FOMC decision Wed 07-29 2:00pm ET** (verified against federalreserve.gov; no SEP/dot-plot). **MSFT / META / ARM Wed 07-29 AH** — Azure's cc growth guide is the read-through for the whole AI-capex complex, directly sequel to the 07-23 GOOGL capex shock. **AAPL / AMZN Thu 07-30 AH.** No CPI/PPI/PCE/NFP inside the window. This week is maximally loaded: a macro binary and the four largest single-name prints inside 48 hours.
- **Tail caps applied:** MOM_SHORT provisional watch-only cap held (cost the book nothing — no new starters existed to be hurt by the inversion). Book-wide CHOP half-cap ceiling respected; no position sized above half. Short-vol quoted net-of-cost with the left tail declared unsampled. Wed 07-29 0DTE stand-aside.
- **Fundamentals gate: not spawned, deliberately.** The veto channel only fires on names about to be sized; all three actions tonight are closes or holds-at-current-size, which fundamentals verdicts do not gate.
- **Hedge note:** after tomorrow's ORCL and PRMB closes the book is a **single half-size short (PLNT)** into FOMC and four mega-cap prints — near-flat, which is the right posture given negative dealer gamma at the index (moves amplify in either direction) and a factor that just inverted violently.
- **Stale-prior warning:** the 07-07 / 07-13 / 07-20 decision envelopes for these same three names still cite **pre-correction** lane priors (+0.81%/9.5pp for MOM_SHORT, +2.07%/20.0pp/n=640 for OI_FADE). Those are known-stale. Do not re-cite them; tonight's envelope uses the 2026-07-24 re-baselined figures per CLAUDE.md invariant #6.

## Data provenance

Preflight **exit 0** after remediation: all five UW groups present for 2026-07-27 (All Options 11,499,574 rows · Dark pool 465,950 · Hot Option Chains 27,160 · OI changes 241,925 · Stock Screener 6,279). The truth-set parquets arrived **stale at 2026-07-24** and were **rebuilt** (`build_prices` → `build_returns` → `build_features`) before any lane was spawned; all three now reach 2026-07-27. Every lane was handed the authoritative regime rather than deriving it — the direct fix for the 07-24 stale-parquet inversion. Path-aware outcomes came from the Yahoo chart API via `scripts/chart.py` throughout; `mcp__yahoo-finance__*` was not used.
