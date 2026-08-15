# Weekly Review — 2026-W33 (Mon 2026-08-10 → Fri 2026-08-14)

Panel/truth-set preflight **clear** (5/5 UW groups; prices/returns/features all reach 2026-08-14).
Weekly panel now **30 weeks (24 full 5-day weeks)**, 2026-01-19 → 2026-08-10, 2,438 tickers.

Convention note: `w_ret` below is the weekly **open→close** return, as produced by
`weekly_features.py` and as used in every prior weekly review. Friday-to-Friday close-to-close is
slightly different and is quoted separately where it matters (SPY +0.40%, QQQ +1.11%, IWM +1.17%).

---

## 1. The Week in Pictures (DIARY — documentation, 0 signal)

### Weekly candles

| | O | H | L | C | w_ret | close_pos | body_frac | structure vs prior |
|---|---|---|---|---|---|---|---|---|
| **SPY** | 772.60 | 779.37 | 769.20 | **776.34** | **+0.48%** | 0.70 | 0.37 | higher_high, follow-through **T** |
| **QQQ** | 722.39 | 734.39 | 715.50 | **731.07** | **+1.20%** | 0.82 | 0.46 | higher_high, follow-through **T** |
| **IWM** | 300.51 | 305.18 | 299.08 | **305.09** | **+1.52%** | 0.99 | 0.75 | higher_high, follow-through **T** |

**The character of the tape changed completely while the direction did not.** All three indices made
higher highs and confirmed the prior week for a second straight up-week. But last week was a
conviction expansion candle (bodies 0.81–0.85 of range); this week the bodies collapsed.

**SPY's range was 10.17 points — 1.31% of close — the narrowest full 5-day week in all 24 full weeks
of the panel** (next narrowest: 2026-04-20 at 12.19 / 1.71%). Its wicks were near-balanced (3.03 up,
3.40 down) around a 0.37 body. That is a digestion candle, not a thrust.

**Order of strength inverted from last week: IWM > QQQ > SPY.** IWM closed at `close_pos` 0.985 —
essentially on its weekly high, upper wick 0.09 of a 6.10 range — and was the only index to retain
its body fraction (0.812 → 0.751). SPY and QQQ both more than halved theirs.

**The QQQ repair gap narrowed but did not close.** At 731.07 QQQ is still **−1.29%** below its
2026-06-15 panel-peak weekly close of 740.62 — better than last week's −2.38%, still not repaired.
SPY and IWM both set new panel-high weekly closes.

### The real story: a flat index over enormous single-name dispersion

SPY moved +0.40% Fri→Fri. Underneath it:

| | wk % (Fri→Fri) | | wk % (Fri→Fri) |
|---|---|---|---|
| **SNDK** | **+35.38%** | META | −0.38% |
| **MU** | **+10.72%** | MSFT | −0.92% |
| AMD | +6.42% | AAPL | −2.36% |
| TSLA | +4.17% | GOOGL | −2.37% |
| IWM | +1.17% | AMZN | −4.31% |
| SPY | +0.40% | **AVGO** | **−8.13%** |

A **43-point spread** between the best and worst mega/large-cap in a week the index went nowhere.
Memory/storage ripped; mega-cap internet and AVGO were sold. This is what the weekly candle hides.

### Catalyst anchoring — a full Tier-1 week (unlike W32)

| Day | Event | SPY | QQQ | IWM | Reaction |
|---|---|---|---|---|---|
| Mon 08-10 | — | −0.03% | −0.30% | −0.52% | **XLE +4.66%** — the oil/Hormuz channel, alone |
| Tue 08-11 | — | −0.32% | −0.34% | +0.34% | Drift; XLE +1.25% |
| **Wed 08-12** | **July CPI** | **+0.25%** | **+0.73%** | +0.57% | +0.1% m/m, 3.4% y/y; core +0.2%, 2.5% — in line, both −0.1pp from June. XLK +1.49% |
| **Thu 08-13** | **July PPI** | **+0.70%** | **+1.16%** | +0.26% | Headline flat, core +0.2% **below** expectations, annual 4.7% vs 5.0%. **The week's engine** — SPY's fresh 52w high close 777.88 / intraweek 779.37 |
| Fri 08-14 | **Retail sales + UMich** | −0.20% | −0.14% | **+0.52%** | Retail sales dipped; large caps gave back, **small caps added**, XLE +1.39% |

**Two Tier-1 prints landed mid-week and both were benign, and that is what set the week's structure.**
September rate-**hike** odds fell to 42% after CPI — note the sign: this cycle prices a possible hike,
not a cut, so "cool inflation" is unambiguously the risk-on read.

**The dispersion had a separate, non-macro cause and it is recorded separately.** SanDisk's Investor
Day on 08-13 (FY28–30 growth model, 100% cash return), a +4% overnight Kospi on AI-infrastructure
optimism, and the 08-03 SNDK/SK Hynix High-Bandwidth-Flash tie-up drove SNDK +13.67% Thu and +7.39%
Fri. **The macro pre-registration arm accrues the index structure; it must not accrue the dispersion.**

### Regime trajectory (Mon→Fri, `scripts/regime_check.py --range`)

| Date | Label | ret5 | ret10 | dd15 | s1_standdown |
|---|---|---|---|---|---|
| 08-10 | UPTREND | +2.030% | +4.590% | −1.300% | **False** |
| 08-11 | UPTREND | −0.100% | +4.010% | −1.540% | **False** |
| 08-12 | UPTREND | +0.350% | +5.900% | 0.000% | **False** |
| 08-13 | UPTREND | +1.210% | +4.880% | −1.650% | **False** |
| 08-14 | UPTREND | +0.400% | +3.920% | −2.350% | **False** |

**The structural event of the week: the crash guard lapsed exactly at the week boundary.**
`s1_standdown` was **True every session of W32** and **False every session of W33**, and the label
dropped its qualifier (UPTREND/REBOUND-THRUST → UPTREND). `ret5` fell to +2.030% on Monday, under the
+2.5% trigger, and never returned. Last week's carry-forward item #3 called this exactly — and this is
**the first full week in this cycle that MOM_SHORT and OI_FADE were both mechanically live.**

**`dd15 = 0.000%` on 08-12 is not "at the highs."** Verified by hand: `dd15 = min(last 15 closes) /
close_10_back − 1`, and on 08-12 the 10-day anchor (07-29, 729.46) **was** the 15-day minimum — a
trough-anchored window. By Friday the anchor had rolled and dd15 read −2.350%.

**Forward decay confirmed, twice, independently, at flat price:** Mon 08-17 still UPTREND
(ret10 +2.46%); **Tue 08-18 flips to CHOP** (ret10 +0.65%) as the 08-04 gap-up day rolls out of the
trailing-10 window. Pure window arithmetic — no price movement required.

### Vol-state overlay

VIX ground monotonically lower all week (15.46 → 15.28 → 14.55 → 14.63 → **14.25**) with clean
contango (**VIX9D 10.61 < VIX 14.25 < VIX3M 18.46**) — no near-term event premium bid.

SPY and QQQ dealer books **both** flipped negative→positive gamma mid-week and **both closed Friday
barely above their flip** (SPY 776.06 vs 774.67, +0.18%; QQQ 730.41 vs 729.92, +0.07%). The
vol-suppression cushion is real but **thin** — a ~0.2–0.3% pullback would push either back under.
VRP: SPY **FAIR** (−0.73%); QQQ **PREMIUM_BUYING** (−5.06%, IV cheap versus trailing realized).

*Caveat carried forward:* the vol pass reported gamma-source agreement **across SPY and QQQ**.
Friday's daily scan failed QQQ closed on disagreement **within QQQ's own gamma sources**. Those are
different tests — aggregate sign drives range/wing-width, spot-vs-flip drives regime — so the scan's
fail-closed flag **stands**. Two QQQ sessions (08-10, 08-13) also returned flip levels near 211–220
against a 720–732 spot; discarded as a data-quality artifact.

**Breadth is the dissent.** Options-flow bullish **35.1%**; price breadth **49.7% green** (250 adv /
245 dec) in a week SPY closed at a panel high. **AVGO −5.94% on Friday alone**, into NVDA's 08-26
print. UW's own classifier reads **TRANSITIONAL** against the mechanical UPTREND (advisory only).

### Sector leadership (`week_context.py`, no staleness flags — all series same window)

**XLE +7.67%**, a dominant outlier at ~4.8× the next sector (and +4.66% on Monday alone). Then
XLU +1.60, XLC +1.53, XLP +1.14, XLK +1.08, XLV +1.02, XLF +0.97, SMH +0.88, XLI +0.72, XLRE +0.65.
Laggards: **XLB −0.60, XLY −1.39**. Energy-up / consumer-discretionary-down is the consumer-squeeze
signature, consistent with Friday's soft retail sales.

### Notable flow (0 signal)

SPY $41.0B (60,795 prints), **MU $37.3B** (100,070), **SNDK $32.1B** (119,453), NVDA $26.4B,
QQQ $26.2B, SPCX $17.3B, MSFT $16.3B, AAPL $16.1B, INTC $11.4B, AMD $11.0B. The #2 and #3 single-name
prints were also the week's two biggest movers — concentration and realized move coincided.

---

## 2. Validated Weekly Setups (SCORED — excess)

### `calls[]` is EMPTY. Nothing sized. Fourth consecutive weekly review with no scored setup.

**OI_FADE — `NO_NAME_CLEARED`** (short). Run on the trailing **15 trading days** (07-27→08-14, ≈3
calendar weeks), ranked by `oi_rel_build`, floors `abs(net_15d) ≥ 1,000` and `avg_30d_call_oi ≥ 1,000`,
ETFs cut via `issue_type`. Population after floors: 1,908.

The **selection-rule mismatch applies to every candidate**: the live lane ranks by `rel_build`, but the
+0.59% mean / +0.95% median / n=1087 baseline was measured on the **top-15 by raw `oi_net_5d`**, with no
persistence and no `catalyst_split` filter. Best raw-rank proximity in the entire pool is SIRI at
**35/1198** — still outside that population. **Nothing here inherits that prior.** Two further discounts
compound it: the h10 prior is being stretched to an h10–h21 hold (unvalidated extrapolation), and the
prior is itself inflated because the harness applies no ETP/earnings hygiene to OI_FADE.

WATCH: **SIRI, GEN, EG, FDX, ITRI**. Three of this week's four CUTs were catalyst-hygiene catches, not
rank calls:

- **TRMB — textbook print-day-boundary artifact.** `catalyst_split`'s `>=` counts the 08-05 print day
  itself as post-catalyst, and 08-05 alone is **+8,024 of +12,733 contracts (63% of the 15d net)**.
  Re-summed with strict `>`, post-share collapses **83.8%/99.3% → 20.8%**. Resolved earnings reaction,
  not a persisting crowd.
- **USFD** — persistence 0.993, a single 08-07 block of +7,572 of +7,625; its own `last_call_net`
  invalidation had already fired.
- **DBX, MRCY** — both `RESOLVED_PRE_PRINT`.
- **BSY — downgraded to EXCLUDED, diverging from Friday's daily carry.** 94% of its build landed in the
  last two sessions while it sits at 28.0% of its 52-week range: the NRG/STUB bottom-fishing profile
  Standing Rule #10 exists to catch.

**EG is the one genuine weekly-only find.** It never clears the 5-day floor at all — its build predates
the trailing five sessions, so the daily lane is structurally blind to it — but the 15-day view shows
organic accretion (persistence 0.47) that is genuinely post-catalyst (79.6% strict). This is the
specific thing running the weekly expression is *for*.

**MOM_SHORT — `BASKET_WATCH`** (short), 6 names, no dropouts, no tighter new entrant. The crash guard is
**no longer standing it down** — but it still does not size, for an independent reason: the PROVISIONAL
tail cap holds it to watch-only pending a DURABLE-N (≥30) forward window, and its recorded baseline is
knowingly negative (−0.0128, n=803).

All six Yahoo-verified path-aware, all `issue_type = Common Stock` (no ETP leak), all liquidity-verified:

| | close | 52w low | set | pct range | 20d $-ADV |
|---|---|---|---|---|---|
| ROL | 36.20 | 35.98 | **08-14** | 0.7% | $235.4M |
| RBA | 84.26 | 83.62 | **08-14** | 1.8% | $131.7M |
| NKE | 40.73 | 40.00 | 06-26 | 1.8% | $813.7M |
| GPI | 263.95 | 259.24 | **08-13** | 2.1% | $56.9M |
| AMRZ | 46.69 | 46.03 | **08-10** | 3.3% | $159.5M |
| GME | 18.66 | 18.33 | **08-13** | 3.4% | $116.9M |

**Five of the six set their 52-week low during this week — in the same week SPY printed a fresh
52-week high.** That is invisible to a daily scan and is the single clearest piece of evidence that the
index close is not describing the tape.

**MOM_LONG — `BASKET_WATCH`** (long), ~250 equity names. Never sizes (−0.0108, n=1066). Verified
exemplars: **NEU, CRNX, BNS**, each Yahoo-confirmed at 100.0% of 52-week range.

### Lane returns that did not survive verification

Three corrections were made to lane output this week. All were caught by re-running the lane's own
claim, per the Phase-B reconciliation rule.

1. **MOM_LONG's count and its explanation were both wrong.** The lane reported "~535 names" and
   attributed the jump from the daily ~275 to *"horizon expansion — weekly bars show more names near
   52w-high due to a longer resolution window."* That is a rationalisation of a filter failure: the
   lane explicitly declined to apply `issue_type` ("live lane responsible for full issue_type
   filtering"). Recomputed on the 08-14 screener at `pct_52w_range ≥ 0.95`:

   | | count |
   |---|---|
   | **ETF** | **560** |
   | Common Stock | **250** |
   | ADR / other / null | 24 |
   | raw total | 834 |

   **67% ETP contamination**, and equity-only 250 is in line with the daily ~275 — so there is no
   horizon effect to explain. Two of the lane's five exemplars are unusable: **BOXX is `issue_type=ETF`**
   — a T-bill box-spread cash proxy that sits at 100% of its 52-week range *by construction* and would
   therefore top this screen every week in perpetuity; and **HEIA 404s on Yahoo** (Heineken trades as
   HEIA.AS in Amsterdam, not a US symbol), so it cannot be path-aware verified at all. Separately, 172
   screener names show `pct_52w_range > 1.0` and 26 show `< 0` — the known stale/un-split-adjusted bug.

2. **OI_FADE misread FDX's range position.** The lane reported `pct_52w 0.589`; Yahoo says **93.6%**
   (52w 178.33 … 345.37, close 334.64). Friday's daily scan was right. FDX's disposition is unchanged at
   WATCH, but the error **inverted the reasoning** — FDX is in fact the strongest near-highs/exhaustion
   fit in the cohort, which is the lane's actual validated setup, not a mid-range name.

3. **GEN's invalidation label was wrong — inherited from Friday's daily scan, not the weekly lane.**
   `$29.87` was recorded as "confirmed 52-week high, 2026-08-10". It is GEN's **intraday high of 08-10**,
   a 4-session-old local swing high. GEN's true 52-week high is **$31.88, set 2025-08-22**, so true range
   position is **75.9%**, not 88.5%. The level is still usable as an invalidation (~4.9% above spot) but
   the label was false — and **the $31.88 anchor rolls out of the trailing 52-week window around
   2026-08-22**, which will mechanically lift GEN's range position with no price move at all.

A fourth error was contained rather than corrected: **MOM_SHORT returned an invalidation for each name
equal to that name's 52-week LOW** — i.e. *below* spot on a short, a stop sitting exactly where the trade
works best. Nothing wrong reached the envelope, because `lane_status[]` carries no invalidation field,
but the lane must be fixed before it is ever trusted to emit a sized call.

The regime claim was the one lane return that arbitrated clean:
`regime_check.py --claim-label UPTREND --claim-ret10 0.0392` → **exit 0, checks out**.

---

## 3. Weekly Technicals — PRE-REGISTERED (documented, 0 points, NOT sized)

| Feature | This week | Would signal | Status | Pre-reg bar |
|---|---|---|---|---|
| SPY weekly range compression | 10.17 pts = **1.31% of close — narrowest full week in the 24-week panel** | Volatility expansion pending — **directionless**; says nothing about which way | PRE-REGISTERED | PR-WT |
| reversal-after-CPI | **Did not fire.** CPI Wed +0.25% → Thu followed through +0.70%; only −0.20% Fri fade | A same-week reversal of the catalyst move = the bearish arm. This week is the *continuation* arm | PRE-REGISTERED | PR-WT — **first genuine Tier-1 obs in 3 weeks**; accrual 1 (continuation) |
| follow_through | **TRUE all three**, 2nd straight up week (QQQ/IWM were FALSE last week) | Continuation — but SPY base rate is **21/30 weeks (70%)**, so close to unconditional | PRE-REGISTERED | PR-WT |
| higher_high + body compression | SPY 0.849→0.368, QQQ 0.813→0.460, IWM 0.812→0.751, with breadth dissent | Waning thrust / distribution into highs — **the bearish arm** | PRE-REGISTERED | PR-WT |
| IWM close_pos extreme | **0.985**, upper wick 0.09; led Friday +0.52% while SPY/QQQ red | Broadening risk appetite / small-cap leadership | PRE-REGISTERED | PR-WT |
| candle-pattern arms | **None fired.** Panel base rates: inside **0/30**, outside 1/30, hammer 3/30, star 1/30 | Nothing this week | PRE-REGISTERED | PR-WT — **unreachable at this accrual rate** |

Two of these point opposite ways — *body compression + breadth dissent* reads distribution, *IWM
close_pos 0.985* reads broadening. **The contradiction is left standing.** Neither is scored, so
nothing needs to resolve it, and resolving it would be exactly the narrative-fitting the Layer-3 split
exists to prevent.

The panel is **30 weeks against a ≥2-year / ≥30-obs-per-arm bar** — roughly a quarter of the minimum
history, and three of the four candle arms have ≤3 observations in the entire panel.

---

## 4. Carry-forward

### How last week's Layer-2 calls did

**W32 scored nothing** (`calls[]` empty), so there is nothing to grade. `held_book.py` reads **0 open
positions**; the daily book has now been flat for **five consecutive sessions**. Four straight weekly
reviews with no scored setup.

**This week the cost of that discipline was small, and that is worth recording plainly**, because last
week it was not: the tape delivered +0.48% on SPY, and the book missed almost nothing. The
counterfactual that actually stings is different — the *dispersion* (SNDK +35%, AVGO −8%) was where the
week's money was, and no validated lane in this engine addresses it. That is a scope fact, not a miss.

### Last week's items, resolved

1. **The 2026-08-08 `/calibration-audit` ran.** Verdict: **no lane earns a STOP**; all five printed
   below baseline but both invariant-#6 isolation checks proved that is data, not code (byte-identical
   harness; the baseline cohort reproduces the recorded figures to the digit). The 190-row increment is
   one correlated macro rally — `base` pinned at 1.00 for every long lane and 0.00 for every short lane.
   The post-fix h10 cohort **did not confirm** OI_FADE's decay signal (+1.35% vs the −3.73% that raised
   the flag), but spans only 3 exit-days.
2. **The stand-down margin lapsed** — item #3 called it correctly, and it happened exactly at the week
   boundary. Both suppressed lanes ran live all week. Neither produced a sized call anyway.
3. **CPI 08-12 and PPI 08-13 landed** as flagged, both inside week 1 of any weekly hold.
4. **QQQ's repair gap** closed from −2.38% to **−1.29%** — improving, still open.

### What rolls into next week

1. **`/calibration-audit` is due tomorrow, 2026-08-15**, and it is the important item. 41 open rows
   mature 08-10→08-21 and the 08-03→08-07 crash-guard block matures 08-18→08-22 — **the first cohort
   spanning non-overlapping windows.** Count distinct **exit-days**, not rows.
2. **The OI_FADE selection-rule mismatch is now 5+ consecutive sessions/weeks unresolved** and should be
   decided at that audit, not carried again. Two options on the table: add the live-lane screens to the
   harness and re-baseline, or formally record the +0.59% prior as inherited/discounted. Carrying it
   undecided is what lets a WATCH list accumulate names that provably do not inherit the prior.
3. **Regime flips to CHOP on Tuesday 08-18** by window arithmetic alone. Anything entered on Monday
   spends ~9 of 10 sessions outside the regime that would justify it.
4. **A dense event cluster sits inside any 2–4 week hold**: HD 08-18, TGT 08-19, WMT 08-20 (the retail
   cluster lands right on the CHOP-decay date), then **GDP + PCE 08-26, NVDA earnings 08-26 AH, and
   Jackson Hole 08-27/29** — Kevin Warsh's first keynote as chair on 08-28. CPI 09-11 and FOMC 09-15/16
   close the horizon out.
5. **AVGO −8.13% on the week, −5.94% on Friday alone, going into NVDA's 08-26 print** is the tell worth
   watching — a mega-cap semis divergence while SMH was +0.88%.
6. **GEN's 52-week-high anchor rolls off around 08-22**, mechanically lifting its range position with no
   price move. Any range-position gate applied to GEN after that date is measuring a different thing.
7. **Two lane defects need fixing before either lane is trusted to size**: MOM_SHORT's inverted
   invalidation levels, and MOM_LONG's refusal to apply `issue_type` (67% ETP contamination this week).
   Both were contained here only because neither lane sizes.
8. **`prices.parquet` coverage gap persists** — unchanged root cause (frozen `universe.json` spine at
   785 names vs the ~2,460 live screener spine). Treat absentees as fail-closed.
