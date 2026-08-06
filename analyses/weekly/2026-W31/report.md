# Weekly Review — 2026-W31 (Mon 2026-07-27 → Fri 2026-07-31)

**Verdict: NO SCORED SETUP.** Second consecutive week with an empty `calls[]`. All three Layer-2 lanes
produced a lane-level disposition and no sized single-name call. Layers 1 and 3 ship as documentation.

Preflight clear (5/5 UW panel groups, truth set through 2026-07-31). Envelope validates against
`schemas/weekly_review.schema.json`.

---

## 1. The Week in Pictures (DIARY — documentation, 0 signal)

### Weekly candles

| | O | H | L | C | w_ret (O→C) | c/c | close_pos | body | structure |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 744.91 | 748.90 | 729.10 | 747.03 | +0.28% | **+1.10%** | 0.906 | 0.107 | lower_low, **HAMMER**, follow_through FALSE |
| QQQ | 691.68 | 695.77 | 661.14 | 687.99 | −0.53% | +0.55% | 0.775 | 0.107 | lower_low, **HAMMER**, follow_through TRUE |
| IWM | 293.98 | 295.52 | 287.83 | 291.20 | −0.95% | **+0.01%** | 0.438 | 0.362 | lower_low, **no hammer**, follow_through TRUE |

SPY and QQQ both printed a textbook **weekly hammer** — a lower low, a tiny body (10.7% of range on both),
and a close near the top. SPY's lower wick is 8.5× its upper wick; QQQ's is 6.6×, and 26.85 points long.
SPY's `follow_through` went **FALSE** — the first week in three that did not confirm the prior week's
direction.

**IWM refused to confirm.** Same lower low, but a mid-range close (0.438) on a body three times as thick,
and **flat on the week** (291.17 → 291.20, +0.01%) while SPY added +1.10%.

### Catalysts, anchored to the reaction

Unlike 2026-W30 (zero Tier-1 prints), this week carried **two**, back to back, in opposite directions.

| Day | Event | Reaction (panel-measured) |
|---|---|---|
| **Wed 07-29** | **FOMC — hawkish hold.** 3.50–3.75% held on a **9-3** vote; all three dissents (Hammack, Kashkari, Logan) were **for a HIKE** | SPY **−1.54%**, QQQ −2.04%, Dow −2.19% (worst since Apr-2025). Breadth **31.80%**. VIX 18.21→20.66. Regime → **PULLBACK** |
| **Thu 07-30** | **Core PCE — cooler.** +0.1% m/m vs +0.2% est (3.3% y/y in line); Q2 GDP 1.5% from 2.1% | SPY **+1.68%** — *more than erased the FOMC day in one session*. QQQ +3.30%, XLK +5.50%, SMH +6.88%. VIX −17.3%. Regime → **CHOP** |
| Wed 07-29 a/c | **MSFT** (Azure +43% cc, rev beat) vs **META** (opex +55% vs rev +28%, NI −14%, soft guide) | Next session: **MSFT +15.51%**, **META −7.95%** |
| Thu 07-30 a/c | **AMZN** (AWS beat) vs **AAPL** (Services + China miss) | Next session: **AMZN +15.32%** (biggest day in a decade), **AAPL −7.35%** |
| Thu–Fri | **Long end breaks to multi-year highs** | 10y 4.68→**4.74%** (Fri high 4.75%, highest since Jan-2025); 30y 5.16→**5.28%** (highest since 2007). Both closed *at* their weekly highs |

The yield move is the one that matters, and it came **after** the dovish PCE print — a term-premium move,
not an inflation-expectations move.

### Regime trajectory — a full round trip in five sessions

```
Mon 07-27  CHOP      ret5 −0.400%  ret10 −1.350%  dd15 −1.470%  s1=False
Tue 07-28  CHOP      ret5 −0.990%  ret10 −1.460%  dd15 −1.820%  s1=False
Wed 07-29  PULLBACK  ret5 −2.400%  ret10 −3.360%  dd15 −3.360%  s1=False   ← FOMC
Thu 07-30  CHOP      ret5 +0.480%  ret10 −1.200%  dd15 −2.830%  s1=False   ← PCE
Fri 07-31  CHOP      ret5 +1.100%  ret10 +0.500%  dd15 −1.860%  s1=False
```

`ret10` finished **positive for the first time since 2026-07-10**, a 3.9pp swing off Wednesday.

**Crash-guard near-miss, recorded deliberately.** `s1_standdown` is FALSE, but Friday sits just inside two
legs of the trigger: leg (a2) fires at `ret5 > 1.5%` with `dd15 < −2.0%`, and the actual state is
**+1.100% / −1.860%** — within 0.4pp and 0.14pp. This *is* the unconfirmed-V-rebound shape the guard exists
to catch. Contrast 2026-W30, where `ret10 −2.12%` was past the −2% confirmed-downtrend boundary and the
guard was affirmatively inapplicable.

**Vol state.** VIX 18.58 → 18.67 → 18.21 → 20.66 → 17.09 → **15.99**, ending −14.0% on the week and at the
lowest close since 07-13. VIX/VIX3M = 15.99/19.02 = **0.84**, steep contango. Dealer gamma **flipped**: SPY
`total_gex` **+$1.19B, POSITIVE**, zero-gamma level **746.93 against a 747.06 spot** — SPY closed **0.13
points above its flip**, after being FULLY_NEGATIVE every session of last week. QQQ `total_gex` −$8.2M ≈ zero,
also at the flip.

> ⚠️ **Data-quality flag.** `uw options-structure gex` labelled QQQ `FULLY_NEGATIVE` ("All strikes have
> negative net GEX") while its own `per_strike` array carries clearly positive strikes (678 +2.3M, 681 +4.6M,
> 687 +70.2M, 688 +94.1M). The label contradicts its own payload. `total_gex ≈ 0, at the flip` is the read
> used here. Consistent with the previously-recorded 0DTE QQQ gamma-sign defect.

**Breadth did not confirm.** 64.96 / 60.46 / 31.80 / 57.40 / **45.07**% green. Friday closed SPY **+0.72% on
45.07% breadth** — the two strongest index sessions were the two narrowest relative to their index move.

### Sector leadership — a complete inversion of last week

```
XLY  +6.11%   ← AMZN alone            XLK  −0.30%
XLC  +1.82%   ← GOOGL +11.38%         XLI  −1.54%
XLF  +1.12%                           XLB  −1.62%
XLP  +1.09%                           XLRE −1.92%
XLV  −0.01%                           SMH  −3.68%
XLE  −0.12%                           XLU  −4.19%   ← worst
```

Last week's top three (XLE +3.36%, XLU +2.48%, XLI +1.81%) are three of this week's **bottom five**. Last
week's worst (XLY −5.22%) is this week's **best**. The rate proxies were hit precisely as the long end broke.

**The XLK paradox:** XLK finished **−0.30% in a week its largest holding gained +21.75%.** Two enormous
mega-cap gains were fully offset by breadth-wide tech damage (SMH −3.68%, MU −10.63%, SNDK −15.43%,
AAPL −7.24%, NVDA −2.94%). XLK also traded an intraweek low of 166.46 — 5.4% under the prior Friday close.
Verified independently against the Yahoo chart API (175.88 → 175.35).

### Notable flow (diary only, 0 signal)

SPY $70.2B · **MU $56.9B (175.5k prints)** · QQQ $50.5B · **SNDK $35.0B (152.8k)** · NVDA $27.1B ·
AAPL $24.8B · MSFT $22.3B · AMZN $16.8B.

MU and SNDK repeat as the anomaly for a **second consecutive week and both got larger** (MU $46.2B/144k →
$56.9B/175k; SNDK $26.8B/107k → $35.0B/153k). MU printed more dark-pool prints than SPY and QQQ **combined**
for the second week running — while falling −10.63%. SNDK printed 152.8k while falling −15.43%, on a daily
path of −11.02 / −14.25 / −7.32 / **+25.99** / −5.09.

---

## 2. Validated Weekly Setups (SCORED — excess)

**`calls[]` is empty.** No name cleared the full stack in either scored lane.

### OI_FADE — `NO_NAME_CLEARED`, regime_fit 0.70 → **0.35**

The regime moved **against** this lane. The PULLBACK that supported it lasted exactly one session; `ret10`
finished positive, VIX closed at 15.99, and SPY crossed back into positive dealer gamma.

30 names ranked on a 10-day build window. Cuts: **liquidity** ($5 / $50M ADV) removed 14 · **persistence**
≥0.85 removed DBX 0.882, INFY 1.090, SSNC 1.143, TEX 0.927, YMM 0.985 · **ETP** (`issue_type`) removed MTUM,
NOWL, and SHAZ (NULL — fail-closed) · **earnings h21** blocked QGEN, SOLV, TPG, GMED.

Four names reached final adjudication; **all four die**:

- **AVTR** — by far the strongest mechanical signal in the panel: `rel_build` **4.082** (10d), net **+175,675**
  on a 43,034 base, persistence 0.271 organic, ADV $172.6M, earnings 11-04 clear, catalyst **LIVE** with
  63.4% of the build accruing *on or after* the 07-29 print (+40,486 / +47,578 / +23,325 on 07-29/30/31 — it
  **accelerated through its own catalyst**). **Fundamentals VETO sustained**; both re-admit halves tested and
  unmet on 07-30 and 07-31. The 07-31-datelined PT-raise item was a lagged republication of the 07-30 actions.
- **HRI** — VETO sustained and *worsening*: printed +2.89% on 07-31, so the "shorting a completed collapse
  into an active bounce tail" objection is stronger.
- **KBR** — **RESOLVED_PRE_PRINT**. Only 12.5% of the build (+1,656 of +13,298) accrued after its 07-30 print;
  the build **died at its catalyst**. Spent positioning, not a crowd.
- **ALLE** — carries the 07-24 VETO *and* has now failed the lane's own mechanism: `last_call_net` **−945**,
  calls genuinely closing, the pre-registered OI_FADE invalidation.

Every VETO in this set is the same pattern — a positive-surprise gap that **held**, plus post-print PT raises.
This week's Layer-3 earnings arm went **0-for-4** on catalyst-gap reversals. The PEAD objection to fading held
beats is accumulating evidence, not weakening.

### MOM_SHORT — `STOOD_DOWN`, regime_fit 0.60 → **0.25**

Capped watch-only for new starters by CLAUDE.md invariant #6. This week the regime independently agrees: the
crash-guard near-miss above is exactly the V-rebound shape a fresh short should not be opened into.

Clean after full hygiene **and** an independent per-name Yahoo 52-week verification: **BLDR** 1.6%, **PATK**
1.9%, **LII** 2.2%, **ALNY** 2.6%, **COIN** 2.7%, **QS** 3.1%, **MSTR** 3.5%, **CRH** 3.8%, **GPI** 5.8%,
**OLN** 6.1%, **HDB** 7.9%. None sized.

### MOM_LONG — `BASKET_WATCH`, regime_fit 0.30 → **0.40**

Better tape than last week (`ret10` positive, index hammer), still under the bar. Two independent reasons:
the prior is **+0.18% mean on a −1.06% median**, tail-driven — the fresh harness read gives +0.0023 mean /
**−0.0091 median** / hit 0.47 vs base 0.60 (**hit−base −0.130**, n=483), i.e. the basket loses *more often*
than the benchmark and wins only on the tail; and +0.18–0.23% sits under the +0.3% starter threshold.
Re-entry condition unchanged and unmet: `ret10 > +1%` for ≥2 consecutive weeks (currently +0.500%, one week).

**Composition rotated again** — seven names, all Yahoo-verified: **ILMN** 99.3%, **ING** 99.0%, **BMY** 98.5%,
**WBS** 98.1%, **BPOP** 98.0%, **CAKE** 96.8%, **ENVA** 96.4%. Healthcare + financials — a *different* set from
last week's industrials/insurance/rails. Two weeks running the near-52w-high cohort contains **essentially zero
mega-cap technology**, and it still does not in the very week MSFT gained +21.75% and AMZN +17.00% — both
remain well below their own 52-week highs.

### Regression gate — `retro_harness.py --all`, 78 panel days

| Lane | Baseline (4ec89dc, 73d) | Now (78d) | |
|---|---|---|---|
| MOM_LONG | +0.0018 | **+0.0023** | PASS |
| MOM_SHORT | −0.0003 | **−0.0008** | ⚠️ **below** |
| OI_FADE | +0.0070 | **+0.0071** | PASS |
| S2_dp_revert | +0.0006 | **+0.0021** | PASS |
| S4_pcr_fade | +0.0044 | **+0.0051** | PASS |

MOM_SHORT drifting −0.0003 → −0.0008 is **not** a regression caused by a change — no lane or threshold was
touched, and the panel grew 73→78 days (n 281→317), so it is not like-for-like. But it is a further
deterioration in the one lane already carrying a written negative-excess exception, and it **reinforces** the
watch-only cap. Not re-baselined here; that is a `/calibration-audit` + CLAUDE.md decision.

---

## 3. Weekly Technicals — PRE-REGISTERED (documented, 0 points, NOT sized)

| Feature | This week | Would signal | Status |
|---|---|---|---|
| Weekly hammer SPY+QQQ after a lower low, **IWM refusing** | SPY cpos 0.906 / body 0.107 / wick 8.5×; QQQ 0.775 / 0.107 / 6.6×; IWM 0.438 / 0.362, **no hammer**, flat on the week | Textbook bullish reversal → long tilt. IWM non-confirmation + 45.07% Friday breadth cut hard against it | PRE-REGISTERED, PR-WT |
| **Reversal-after-catalyst — Tier-1 MACRO arm** (first observation in 3 weeks) | FOMC −1.54% Wed **fully reversed** by PCE +1.68% Thu; net over both Tier-1 sessions **+0.11%** | Tier-1 move reversed by the next Tier-1 print → fade the catalyst day. **Opposite result to W30's single-name arm**, where the gap held | PRE-REGISTERED, PR-WT |
| Reversal-after-catalyst — **single-name earnings** arm | 4 mega-caps in 48h, split **exactly 2-2**. MSFT +15.51%, AMZN +15.32% vs META −7.95%, AAPL −7.35%. **0-for-4 reversed** | Capex punished only when revenue doesn't carry it — reframes W30's "AI-capex repricing" as *capex-without-revenue*. PEAD-consistent; already applied as an OI_FADE tail cap | PRE-REGISTERED, PR-WT |
| Rates-driven sector inversion | 10y →4.74%, 30y →5.28%, both closing at weekly highs *after* the dovish print. XLU −4.19% / XLRE −1.92% worst; last week's top 3 are this week's bottom 5 | Rotation is rates-driven, not risk-appetite → argues against reading the hammer as broad risk-on | PRE-REGISTERED, PR-WT |
| Index calm masking record dispersion (**XLK paradox**) | SPY +1.10%, XLK −0.30%; ~37pp spread between best and worst mega-cap | Index regime labels carry less information than usual → favour cross-sectional lanes over index-directional reads. **Not allowed to alter any regime_fit this week** | PRE-REGISTERED, PR-WT |
| Dealer gamma flip | SPY +$1.19B POSITIVE, **0.13 pts above** zero-gamma 746.93; QQQ ≈0, also at the flip | Short→long gamma = dampening, lower realized vol. At 0.13 pts it inverts on any gap down → signals *fragility of state*, never direction (CLAUDE.md: GEX feeds vol-state ONLY) | PRE-REGISTERED, PR-WT |

**PR-WT bar:** ≥2 years / ≥30 weekly obs per arm / cross-regime sign-stable / BH-surviving at FDR 0.10. This
panel has ~20 weekly observations — no power. `/calibration-audit` accrues.

---

## 4. Carry-forward

### Open position

**PLNT** — OI_FADE short, half size, entered 2026-07-20 at 55.20.

| | |
|---|---|
| Close 07-31 | 55.91 |
| Gross | **−1.29%** (adverse — it's a short and the stock is up) |
| **Since-entry excess vs SPY** | **−0.62%** (SPY 742.09 → 747.03, +0.67%) |
| Binding exit | **2026-08-03 close (Monday) — ONE session remains** |

Computed by hand, since-entry, *not* read off `held_book.py`'s TODAY-only `excess` column. Verdict unchanged:
**HOLD to the binding h10 exit.** Pre-registered leg (b) "first genuinely negative `call_net`" is not strictly
triggered; the discretionary $59.50 stop is 6.42% away and is **live, not vestigial** (the vestigial precedent
applies to a position that has run >10% *in its favour*, and this one is adverse).

> 🐛 **Helper bug found — `scripts/held_book.py` silently dropped this live position.** `CLOSED = ("CLOSED",
> "DROPPED", "CUT_CONFIRMED", "COVER", "EXIT")` is matched as a **substring** against `verdict`
> (`held_book.py:45`). PLNT's verdict is `HOLD_TO_BINDING_EXIT` — which contains `"EXIT"` — so the only open
> position in the book was filtered out as closed and the tool reported *"no open positions carried in that
> file"*. A live half-size short went invisible to the reconciliation helper. This is the exact failure the
> script exists to prevent.

### 🚨 Data integrity — `pct_52w_range` is wrong *inside* [0,1], and it only manufactures FALSE SHORTS

The recorded failure mode covers values falling **outside** [0,1]. This week found a second, more dangerous
class: values that are **in range and still wrong**, from a stale, **un-split-adjusted `w52h`** in the UW feed.

| | features `p52` | Yahoo actual | `w52h` in panel | Yahoo 52w high |
|---|---|---|---|---|
| **KLAC** | 0.0058 (52w **low**) | **44.4%** (mid-range) | 2431.29 | 307.37 |
| **BKNG** | 0.0076 (52w **low**) | **52.4%** (mid-range) | 5794.99 | 231.80 |
| **CLBK** | 0.0073 (52w **low**) | **83.2%** — *near its 52w **HIGH***, only −7.9% off | 25.83 | 11.74 |

An inflated `w52h` blows up the denominator and drags `pct_52w_range` toward zero, so **the corruption can
only push names into the SHORT cohort, never the long one.** Consistent with observation: all seven MOM_LONG
survivors verified clean (96.4–99.3%), while three MOM_SHORT names were corrupt. **KLAC ($2.5B ADV) and BKNG
($1.2B ADV) were the two largest and most liquid names in the short cohort.** **CLBK was carried as a
MOM_SHORT candidate in Friday's daily scan** while actually sitting 7.9% off its 52-week high — a
sign-inverted candidate. Nothing was sized (the lane is watch-only capped), so no money was at risk.

**The screen does not fail-close correctly.** `w52h/close > 3×` flags 25 of 94 (26.6%) post-ETP near-low names
— but most of those are *genuine* 70–80% drawdowns (TTD −80.3%, MSTR −77.5%, QS −72.6%, all verified real),
and it **misses CLBK entirely** at 2.39×. The only sound rule is a **direct Yahoo 52-week cross-check on every
surfaced MOM_SHORT candidate** before it can be scored — cheap, since the lane surfaces <20 names. Applied
that way throughout this review.

### Rolling into next week

- **2026-W30's Layer-2 output was also empty**, so there is no prior weekly call to resolve. Its diary
  observation that the memory melt-up reversed on 07-24 **extended for a full week** (MU −10.63%,
  SNDK −15.43%) — recorded as a diary observation that continued, not as a tradeable signal.
- **OI_FADE is the lane to watch** — it is the only one with a robust prior (+0.0071, hit 0.56 vs 0.41 base,
  n=979) and it is being blocked by fundamentals vetoes rather than by mechanism failure, four weeks running.
  AVTR's build accelerating *through* its catalyst is the strongest mechanical signal seen in weeks; if the
  analyst tape turns and guidance deteriorates, the re-admit condition is live.
- **NFP** is the next Tier-1 print and sits inside any h5–h21 window opened now.
- Two open helper defects to fix before they bite something sized: the `held_book.py` substring match, and the
  absence of any `pct_52w_range` sanity check in the momentum lane.
