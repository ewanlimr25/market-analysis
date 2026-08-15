# Market Scan — 2026-08-14

## Regime & Verdict

- **Regime: UPTREND** · ret5 +0.400% · ret10 +3.920% · dd15 −2.350% · `directional_tradable=TRUE` · `s1_standdown=FALSE`
- **Vol-state:** VIX 14.25 (LOW tercile), falling from 16.50 on 08-04. SPY GEX positive (+$2.02B), spot pinned essentially *at* the flip (776.06 vs zero-gamma 774.67). QQQ GEX positive (+$652M) but spot within 0.07% of its flip, and the two gamma reads disagree. SPY VRP FAIR (iv30d 11.76% vs realized 12.49%); QQQ realized (23.24%) running hotter than implied (18.17%).
- **Breadth:** 250 advancers / 245 decliners, pct_green 49.7%, on a day SPY itself closed −0.20%. Structurally healthy: 246 names within 5% of 52w highs vs 64 within 5% of lows (~3.8:1).
- **Bottom line: No directional edge today. ZERO new starters; the book stays FLAT for a 5th consecutive session.** The one name carried at WATCH (NRG) was CUT on a fired invalidation.

### Two regime facts that constrain everything below

**1. dd15 is not a drawdown.** `dd15 = min(last 15 closes) / close_10_back − 1`. Tonight's −2.350% is driven by the **07-29 dip to 729.46** measured against the 07-31 anchor (747.03) — an excursion *behind* us, not current distance from highs. Recomputed by hand: −2.352%. SPY is **0.4% off its high, at 98.0% of its 52w range**, having printed a fresh 52w high (779.37) on 08-13. This metric was misread in the opposite direction on 08-12; it is stated explicitly here to stop the error recurring in either direction.

**2. The regime mechanically expires inside the horizon.** Holding price flat and rolling the 10-session window forward:

| Session | c10 anchor rolls in | ret10 if flat | Label |
|---|---|---|---|
| Mon 08-17 | 08-03 (757.67) | +2.46% | UPTREND |
| **Tue 08-18** | 08-04 (771.33) | **+0.65%** | **CHOP** |
| Wed 08-19 | 08-05 (769.79) | +0.85% | CHOP |
| Thu 08-20 | 08-06 (768.56) | +1.01% | CHOP |
| Fri 08-21 | 08-07 (773.26) | +0.40% | CHOP |

Anything entered tonight on h10 (window 08-14 → ~08-28) spends **roughly 9 of 10 sessions outside the regime that would justify it**. No further price movement is required for this; it is pure window arithmetic off the 08-03→08-07 rally rolling out.

## Directional Book (excess-scored)

**Empty. No candidate reached a sizing band.**

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

Six names cleared the full OI_FADE mechanical stack (STUB, FDX, GEN, INSW, BSY, ITRI) — liquidity, earnings gate, `catalyst_split`, `issue_type`, news. All six failed at **Phase C, before the gate stack was even reached**, on one decisive fact:

**Not one of them clears the raw top-15 cohort the +0.59% prior was measured on.** Verified independently by the orchestrator on the 1,503-name features spine the harness itself uses:

| Ticker | `oi_net_5d` | raw rank | pct_52w_range | note |
|---|---|---|---|---|
| STUB | 5,676 | **55** / 1503 | 10.6% | −71% off high; best of the cohort, still 3.7× outside top-15 |
| FDX | 2,669 | 108 | 93.6% | near highs |
| GEN | 2,227 | 119 | 74.8% | |
| BSY | 764 | 235 | 28.0% | |
| INSW | 616 | 259 | **97.9%** | −1.2% off high; ADV $50.3M, barely over floor |
| ITRI | 565 | 273 | 37.0% | |

`validated_excess` is therefore **not established** for any of them, so none can reach MEDIUM (+0.3–1%) or HIGH (≥+1%). This is the same selection-rule discount that has held COO and NRG at WATCH for four consecutive nights. Citing +0.59% here would be citing a number measured on a different cohort.

Two names carry an additional, independent problem:

- **INSW — cut, not watched.** At 97.9% of its 52w range it is effectively at a fresh high. Shorting it directly opposes the strongest cross-sectional factor in the study (`pct_52w_range`, rank-IC t=+6.8) — the same factor whose long leg would flag this name. The lane itself flagged it as closest to the ENS breakout-chase failure mode, and its $50.3M ADV sits a hair over the floor.
- **STUB — the NRG setup exactly.** 10.6% of range, −71% off its high, $8.08, heavy call accumulation (23,441 fresh calls today) on a bounce after a bad print. Beaten-down name + heavy call build + short = precisely what just cost this book its only carried position.

### Cohort-level caution (new tonight)

Tonight's call-OI building is **not froth at the highs — it is bottom-fishing in broken names.** Of the raw `oi_net_5d` top-15, **8 sit below 30% of their 52w range**: MSTR 3.8%, TTD 3.0%, MARA 15.1%, NFLX 21.2%, TSLA 22.3%, ACHR 22.5%, META 25.2%, SPCX 29.1%.

That makes an OI_FADE short in this cohort structurally the same trade as MOM_SHORT — the one lane knowingly carrying negative excess (−0.0128) — while carrying the V-rebound risk NRG just realized. Treated as a cohort-level caution, not six independent names.

## Vol Book (non-directional)

Delta-neutral, quoted net of cost, 0 directional points.

**0DTE-VRP — STAND ASIDE, both symbols.**

| | aggregate gamma | spot vs flip | VIX tercile | pooled net | **conditional net (tonight's bucket)** | verdict |
|---|---|---|---|---|---|---|
| SPY | POSITIVE | above flip (long gamma) — agree | LOW | +0.119% | **−0.078%** (0.022% gross − 0.10% cost) | STAND ASIDE |
| QQQ | POSITIVE | at/below flip (short gamma) — **disagree** | LOW | +0.241% | **−0.009%** (0.091% gross − 0.10% cost) | STAND ASIDE |

The pooled headline says sell premium on both. It is the wrong number: pooled `net_expectancy` averages across all VIX terciles, and tonight sits in the **LOW** bucket where the conditional net is negative for SPY and ~breakeven-negative for QQQ. QQQ fails independently on gamma-sign disagreement (aggregate sign drives range/wing-width; spot-vs-flip drives the sell decision — they answer different questions and disagree here, so it fails closed).

**Earnings IV-crush — ROST, advisory only.** Prints 08-20 (IV-rank 93.2, backwardation, front/back 4.46). ATM 245-strike straddle on the 08-21 bracketing expiry: call $9.00 + put $8.95 = **$17.95 → 7.31% implied move** (median IV ~64.5%). Net of a half-spread cross (~$1.15): **~6.8% net credit**. Wing floor: treat 7.31% as a *lower bound* and set wings no tighter than **~9.5–10% OTM** — TPR realized −16.5% against a ~12.2% raw-IV estimate on 08-13, live evidence that straddle-tight wings breach.

This resolves last night's specific objection (no net-of-cost quote existed) but **does not promote the name**: the earnings IV-crush stack has no backtested harness, so it stays advisory per the standing 08-10 decision. KC / YRD / VWAV structurally qualify but are not sizable — no clean ATM pair or no usable chain.

⚠️ `implied_move_perc` in the screener is unusable for large-caps: it reads **0.47% for ROST, 0.60% TJX, 0.43% LOW**, all printing next week at IV-rank 71–93. Straddle-derived numbers only.

## Watch / Stood-down

**CUT tonight — NRG** (OI_FADE short, WATCH 3 nights, never sized, no realized loss). Overdetermined on two independently sufficient grounds:
1. **Price invalidation fired** — close $126.24 vs standing "close above $124.71" (08-05 swing high, tracked unchanged 4 nights). Closed *at* the session high: O 120.00 / H 126.25 / C 126.24, **+5.42%** on a day SPY was −0.20% (~+5.6% day-excess against the short).
2. **Mechanical invalidation fired** — `oi_build.py` last net **−1,056** (call_net −110): calls genuinely closing. Build died in sequence: +20,900 → +13,239 → +1,997 → +89 → −1,056; rel_build 0.835 → 0.604 → 0.424 → 0.395.

Do not carry to a 4th watch night. **COO** and **WEC** remain CUT from 08-13 and were correctly not re-proposed (COO's build partially re-formed but its raw rank is 304; WEC printed call_net −3,516 on its ex-dividend date, persistence 2.374).

**OI_FADE watch (4):** FDX, GEN, BSY, ITRI — mechanically clean, outside the measured cohort. **STUB** and **INSW** excluded above.

**MOM_SHORT watch-only (6)** — never sizes (baseline −0.0128). All Yahoo-verified genuinely near-52w-low, most having printed that low within three sessions:

| | close | 52w low | pct_range | invalidation |
|---|---|---|---|---|
| ROL | 36.20 | 35.98 (today) | 0.7% | 35.98 |
| RBA | 84.26 | 83.62 (today) | 1.8% | 83.62 |
| NKE | 40.73 | 40.00 | 1.8% | 40.00 |
| GPI | 263.95 | 259.24 | 2.1% | 259.24 |
| AMRZ | 46.69 | 46.03 | 3.3% | 46.03 |
| GME | 18.66 | 18.33 | 3.4% | 18.33 |

**MOM_LONG basket/watch (~275)** — never sizes (baseline −0.0108), DURABLE-N unmet.

**S2 — UNVERIFIED, not advisory-cleared.** The lane returned 70 names as having "cleared all hard gates" but ran **no news verification**, which its charter requires and which prior nights enforced fail-closed. Downgraded to mechanically-screened-but-unverified.

**S4 advisory (harness-consistent top-15):** RYN, UTZ, LTH, COCO, BMRN, CHRW, LBRT, FDXF, MOH, ECHO, STT, CAR, PGR, CAMT, FITB. Never sizes (+0.0035).

## Risk

- **Event cluster inside the horizon.** PCE + Q2 GDP 2nd estimate (Wed 08-26), NVDA earnings (Wed 08-26 after close), and Jackson Hole with the new Fed Chair's first keynote (Thu–Sat 08-27→29) all land within three days of each other — right at the h10 exit for anything entered tonight. The mechanical CHOP transition (08-18) *precedes* that cluster, so the back half of the window is range-bound-and-ambiguous into peak event risk.
- **Regime cap.** The out-of-regime half-cap overlay is binding in principle (UPTREND for 1 of ~10 sessions) but non-binding in practice — nothing reached a sizing band.
- **Correlation.** Not load-bearing tonight; no positions. Noted for future OI_FADE cohorts: the raw top-15 is dominated by two tight clusters — crypto-proxies (MSTR, MARA, IREN, WULF, RIOT) and mega-cap tech (NVDA, GOOGL, AAPL, TSLA, META, NFLX, AMZN). Shorting the raw top-15 is close to shorting QQQ-beta plus crypto-beta.
- **Hedge note.** No book, no hedge required.

### Methodology findings logged tonight (follow-ups, not applied)

Each needs a paired lane+harness fix and a full regression-gate run before shipping; none were applied tonight.

1. **S4 live lane is more permissive than the harness grading it.** The harness applies `(call_volume + put_volume) >= 1000` and `LIMIT 15`; the live lane applied neither. Result: **67%** of its cohort fails the harness's own floor, and 33% had call_volume < 10 (CSL: 1 call, 26 puts, PCR 26; USFD: 3 calls; SLM: 3 calls). Median call volume in the selection cohort was 25 contracts. The report above uses the harness-consistent list.
2. **`pct_52w_range` split artifact is inside the harness, not just the lane.** IESC carries UW `week_52_high` 408.26 against a true 816.51 — an exact 2:1 un-split-adjusted error implying the close is 185% of its 52w high. Correctly read it is 92.6% of high and **fails** the ≥95% MOM_LONG screen. It appeared in `retro_harness.py`'s own MOM_LONG top-15, so the MOM_LONG −0.0108 (n=1066) baseline is measured on a partly-corrupted cohort.
3. **`prior_verdicts.py` conflates "previously vetoed" with "previously mentioned."** HBM was flagged `PRIOR BLOCKING VERDICT` on the strength of its own prior S2 advisory listings, where it had been explicitly *cleared*. This dropped one of the three names S2 carried last night on a false exclusion.
4. **Lane-reported raw ranks are computed on a different population than the baseline.** OI_FADE ranked on its own 1,198-ticker panel; the baseline uses the 1,503-name features spine. Conclusions matched tonight (all six far outside top-15) but the absolute figures differed materially (BSY 389 vs 235, ITRI 465 vs 273).

---

*Next `/calibration-audit` due 2026-08-15 (tomorrow) — first cohort spanning non-overlapping exit-day windows. Count distinct exit-days, not rows.*
