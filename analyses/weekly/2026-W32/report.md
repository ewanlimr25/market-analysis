# Weekly Review — 2026-W32 (Mon 2026-08-03 → Fri 2026-08-07)

Panel/truth-set preflight **clear** (5/5 UW groups; prices/returns/features all reach 2026-08-07).
Weekly panel now 29 weeks (23 full 5-day weeks), 2026-01-19 → 2026-08-03.

---

## 1. The Week in Pictures (DIARY — documentation, 0 signal)

### Weekly candles

| | O | H | L | C | w_ret | close_pos | body_frac | structure vs prior |
|---|---|---|---|---|---|---|---|---|
| **SPY** | 749.44 | 776.85 | 748.80 | **773.26** | **+3.18%** | 0.87 | 0.85 | higher_high, follow-through **T** |
| **QQQ** | 688.30 | 728.54 | 685.82 | **723.03** | **+5.05%** | 0.87 | 0.81 | higher_high, follow-through **F** (reversed prior wk) |
| **IWM** | 292.90 | 303.06 | 292.40 | **301.56** | **+2.96%** | 0.86 | 0.81 | higher_high, follow-through **F** (reversed prior wk) |

A conviction candle in all three: body 0.81–0.85 of range, close at 0.86–0.87, higher highs, and
almost no lower wick (0.02–0.06). Not inside, not outside — a clean directional expansion week.

**Best week since:** SPY +3.18% and IWM +2.96% are the best since **2026-04-13**; QQQ +5.05% is the
best since **2026-05-04** (not April — the press framing is right for SPY/IWM, wrong for QQQ).

**The rebound did not fully repair the damage.** SPY (773.26) and IWM (301.56) both closed at a
**new panel-high weekly close**. QQQ — the week's *best* performer — did **not**: at 723.03 it is
still **−2.38%** below its 2026-06-15 peak weekly close of 740.62. The index that ran hardest is the
one still furthest underwater, because it had the deepest hole (three straight down weeks into 07-27:
−3.12%, −2.55%, −0.53%).

### Daily path — the gain was front-loaded, then re-lit on Friday

| Day | SPY | QQQ | IWM | What drove it |
|---|---|---|---|---|
| Mon 08-03 | +1.42% | +1.76% | +1.72% | Tech/semis recovery leg begins |
| **Tue 08-04** | **+1.80%** | **+3.40%** | +1.85% | **The week's engine.** S&P record close; Bessent floats a Strait-of-Hormuz reopening deal "today or tomorrow"; PHLX semis +6%, best 4-day chip rally since 2020 |
| Wed 08-05 | −0.20% | −0.90% | −0.64% | 5-day win streak ends; oil pressure, Dow −450 |
| Thu 08-06 | −0.16% | −0.37% | −0.51% | Hormuz deal *uncertainty*; Brent to $83 → higher-energy-cost/Fed-hike worry. Single-name earnings damage: APP −20%, WDC −13%, SNDK −6%, CRM −3% |
| Fri 08-07 | +0.61% | +1.17% | +1.11% | **July jobs report undershoots** → hike odds fall, yields drop, risk bid returns |

**The same catalyst drove both directions.** Hormuz *deal hope* powered Tuesday's record; Hormuz
*deal uncertainty* (and the Brent move to $83 it implied) drove the Wed–Thu fade. Friday's soft
payrolls print overrode the oil channel entirely. This is one story with a sign flip mid-week, not
three unrelated ones.

### Catalyst anchoring — Tier-1 macro

**One Tier-1 print landed: July payrolls, Friday 08-07** (a jobs week throughout — JOLTS, ADP,
claims, NFP). **No CPI, no PPI, no FOMC this week.**

The distinction matters for the pre-registration ledger: the week's *structure* was set on **Tuesday
by a geopolitical/energy headline and a semis bid**, not by the Tier-1 print, which landed on the
last day and added ~0.6–1.2%. **The macro-reversal pre-registration arm accrues almost nothing from
this week** — there was one macro event, it came on day 5, and it produced continuation, not a
reversal (Friday closed at its high; the weekly close_pos is 0.87).

### Regime trajectory (Mon→Fri, from `scripts/regime_check.py --range`)

| Date | Label | ret5 | ret10 | dd15 | s1_standdown |
|---|---|---|---|---|---|
| 08-03 | UPTREND/REBOUND-THRUST | +2.510% | +2.100% | −1.700% | **True** |
| 08-04 | UPTREND/REBOUND-THRUST | +4.110% | +3.080% | −2.520% | **True** |
| 08-05 | UPTREND/REBOUND-THRUST | +5.530% | +2.990% | −2.400% | **True** |
| 08-06 | UPTREND/REBOUND-THRUST | +3.620% | +4.120% | −1.180% | **True** |
| 08-07 | UPTREND/REBOUND-THRUST | +3.510% | **+4.650%** | −1.280% | **True** |

Label never changed; ret10 more than doubled (+2.10% → +4.65%). `s1_standdown` was **True every
session** — the crash guard stood the momentum-short leg down for the entire week. Stand-down margin
Friday: ret5 +3.510% vs the +2.5% trigger = **+1.01pp still above**, and the decay *flattened* on
Friday (−0.11pp, vs −1.91pp the session before) while ret10 kept rising. The thrust stopped
decelerating — the stand-down is not about to lapse on its own.

**Vol-state** (from the same-date 2026-08-07 `/market-scan`, run post-close tonight — not re-derived):
VIX **14.90**, a fresh cycle low (15.86 → 16.50 → 15.81 → 15.15 → 14.90), LOW tercile. Dealers net
**long gamma in both indices** (SPY 772.84 vs flip 772.36; QQQ 722.39 vs flip 721.08) — a regime
change from short-gamma on 08-05/08-06, though SPY's cushion is razor-thin (~0.5pt). Breadth 321
adv / 180 decl (63.8% green), **but options-flow bullish is only 37.7% — a breadth-vs-flow
divergence: price breadth is not confirmed by flow.**

### Sector leadership (5-session, from `week_context.py` — no staleness flags, all series same window)

| Leaders | | Laggards | |
|---|---|---|---|
| SMH | **+7.80%** | XLE | **−3.44%** |
| XLK | +7.20% | XLU | −1.67% |
| XLB | +4.82% | XLRE | −0.20% |
| XLY | +3.25% | XLP | +0.08% |
| XLI | +2.97% | XLF | +1.16% |

A **~11.2pp** spread, and it is a clean risk-on/duration-off rotation: semis and tech lead by a wide
margin, defensives (XLU, XLP, XLRE) are flat-to-negative. **XLE −3.44% is the week's most
informative divergence** — energy *equities* fell hardest in a week whose dominant headline was a
Middle East supply chokepoint. The Hormuz *reopening* trade (more supply) dominated the week's
energy tape even though Brent spiked to $83 late on Thursday as the deal wobbled.

### Notable flow (diary only, 0 signal)

Largest dark-pool premium: SPY $56.7B · **MU $39.7B** (110,959 prints) · QQQ $39.2B · NVDA $30.7B ·
**SNDK $26.9B** (113,203 prints) · MSFT $25.3B · AAPL $20.5B · SPCX $18.6B · AMD $18.2B.
Memory/storage is conspicuous: MU and SNDK together carry more DP premium than QQQ, and SNDK printed
the week's highest print-count while falling 6% on earnings Thursday. Recorded, not scored.

---

## 2. Validated Weekly Setups (SCORED — excess)

### `calls[]` is EMPTY — no scored setup, third consecutive week (W30, W31, W32)

| Lane | Disposition | Dir | regime_fit | Binding constraint |
|---|---|---|---|---|
| **MOM_SHORT** | `STOOD_DOWN` | short | 0.10 | Crash guard, 5/5 sessions |
| **MOM_LONG** | `BASKET_WATCH` | long | 0.65 | **Tier math**, not regime |
| **OI_FADE** | `NO_NAME_CLEARED` | short | **0.20** ↓ | Hard Rule #2 regime stand-down |

**MOM_SHORT — whole-lane stand-down, the most decisive of the three.** `s1_standdown` fired every
session; ret5 +3.510% trips the raw +2.5% up-thrust trigger outright — the sharpest arm of the guard,
not the softer drawdown-conditioned one. UPTREND/REBOUND-THRUST is precisely the squeeze leg the gate
exists to avoid shorting into. The lane's screener found 6 names at ≤1.02× w52l (smallest opportunity
set in a month) but they were never adjudicated: gate #1 zeroes the lane before candidate work begins.
Independently, MOM_SHORT is watch-only-capped for new starters (invariant #6, mean −0.0008), so no
live sizing depends on it regardless.

**MOM_LONG — best regime the lane has seen forward, and it still cannot size.** regime_fit lifted
0.40 → 0.65; a confirmed uptrend is the right tape for a long-momentum basket. The bar is arithmetic,
not regime — and it binds *before* any gate is consulted: validated excess **+0.23% < the +0.30%
starter bar**, on a **negative median (−0.91%, n=483, hit-vs-base −9.3pp)** — most constituents
underperform and a few winners carry the mean — plus the DURABLE-N bar. 223 candidates cleared
hygiene (2,597 ETP wrappers cut on `issue_type`, $5/$50M floor, trading-day h21 earnings gate);
sector cap passes at Financial Services 71/223 = 31.8%. Note this cohort uses ≥0.95× w52h against the
daily lane's ~99.4% — **it is a much wider object than the daily 3-name basket, not the same thing.**

> **Data-quality arbitration — the lane's own recommendation was wrong.** It flagged HALO / ABNB /
> FIVN / NTRA as suspected split-or-acquisition artifacts (closes 11.8–19.9% *above* the recorded
> `w52h`) and advised excluding them. `scripts/chart.py --52w` settled it: **all four set a genuine
> new 52-week high on 2026-08-07 itself** — ABNB 178.07 vs 178.45 (99.4%), HALO 103.12 vs 103.29
> (99.6%), FIVN 33.99 vs 34.10 (99.5%), NTRA 322.10 vs 323.01 (99.5%), each −0.2/−0.3% off high. The
> screener field had simply not caught up to a breakout week. Acting on the lane's advice would have
> cut its four strongest names. **Direction matters on this field:** an un-split-adjusted `w52h`
> manufactures false *shorts*; a *stale* one makes real breakouts look like corrupt data.
> FIVN separately remains absent from `prices.parquet` — correlation UNVERIFIED, fail-closed.

**OI_FADE — cleared no name for a third straight week, and the regime got worse, not better.**
regime_fit **0.70 (W30) → 0.35 (W31) → 0.20**: W31 was a single-session flip with VIX 15.99 and only
SPY barely in positive gamma; W32 confirmed the thrust 5/5 with VIX at a cycle-low 14.90 and **both**
indices in positive dealer gamma. Full stack on a 10-day window (net call-minus-put confirmed):

- **Persistence ≥0.85** removed 15 of the top 30 (KLTR, DOO, HNI, XPEL, EYE, LZM, HSTM, NXPI, ALKT,
  **USFD 0.999**, INFY, SLN, DBX, HIG, DLLL)
- **Liquidity** cut TORO, LNSR, AYA, SPCU, DIG · **ETP/`issue_type`** cut MTUM (ETF) and **CCXI**
  (NULL → fail-closed; verified as Churchill Capital Corp XI, a blank-check SPAC shell, $0.00M sales,
  2 employees — the most *organic-looking* build in the panel at persistence 0.252, and a clean false
  positive the NULL rule caught)
- **Earnings h21** blocked MRCY (08-18) · **catalyst_split** cut QGEN (6.1% post-print), SOLV (−6.2%),
  WSC (3.7%) as resolved pre-print positioning
- **M&A/rumor** cleared the survivors — EG's 08-05 headline is Everest *selling* its Mexico unit to
  Fairfax, not being acquired; nothing like the AZN or NXPI/Ambarella pattern
- **AVTR** cleared mechanically (catalyst LIVE 97.4%) but carries a **sustained fundamentals VETO for
  a second week** — the same 07-29 gap that *held* (~+15% above pre-print) plus five PT raises at or
  above spot. Shorting a completed gap that held is the exact pattern W31 named.

Two names cleared everything — **UTHR** (rel_build 1.947, persistence 0.693, catalyst LIVE 67.2%,
fundamentals CONFIRM: Q2 revenue missed on flagship Tyvaso, insider MSPR −31.76) and **EG**
(rel_build 1.859, persistence 0.493, catalyst LIVE 81.2%) — and **both are regime-blocked**. EG is
additionally marginal: insider signal is net *buying* (MSPR +97.64), three PT raises above the
$374.96 close, last-day `call_net` negative.

> **Cross-lane arbitration — this corrects tonight's daily scan.** The daily scan listed USFD and
> UTHR as having "cleared the entire mandatory stack, blocked ONLY by Hard Rule #2 (regime)."
> Re-running `oi_build.py` at both windows reproduces both lanes exactly and shows that attribution
> is **wrong on the persistence gate**. At the **5-day window the daily scan itself used**, USFD is
> **1.074** and UTHR is **1.031** — both above the 0.85 single-block disqualifier, so both should
> have been cut on **mechanism** before regime was ever consulted. At 10 days USFD is still 0.999
> (cut at every horizon); UTHR falls to 0.693 and passes.
>
> **UTHR's pass is horizon-dependent and largely mechanical** — widening the window enlarges the
> denominator and dilutes a one-day build, and `catalyst_split` shows 67.2% of it landed on/after the
> 08-05 print. UTHR is **not** the unambiguously clean "cleanest short on file in over a week" the
> daily scan framed it as; it is a post-print single-session build that only looks organic at 10 days.
> Nothing sizes either way this week, but this is a live trap **if the stand-down lapses — and the
> margin is only +1.01pp.** Flagged for the 2026-08-08 audit.

---

## 3. Weekly Technicals — PRE-REGISTERED (documented, 0 points, NOT sized)

Panel: **29 weeks / 23 full weeks**. The PR-WT bar is **≥2 years and ≥30 weekly observations per
arm**, cross-regime sign-stable, BH-surviving at FDR 0.10. Nothing below is remotely close, and two
of the features below are actively instructive about *why* the bar exists.

| Feature | This week | Would signal | Status | Pre-reg bar |
|---|---|---|---|---|
| **Weekly hammer → reversal** | SPY & QQQ both printed a hammer in **W31** (lower_low, lower-wick 0.80/0.78 of range, body 0.11) — and W32 delivered +3.18%/+5.05% | Bullish reversal off a weekly low | **PRE-REGISTERED** | PR-WT |
| **Large-body / high-close thrust week** | All three: body_frac 0.81–0.85, close_pos 0.86–0.87, higher_high | Continuation into the next 1–2 weeks | **PRE-REGISTERED** | PR-WT |
| **Follow-through (confirm prior wk)** | SPY **True**; QQQ & IWM **False** (both reversed a down week) | Divergent — SPY continuation vs QQQ/IWM reversal | **PRE-REGISTERED** | PR-WT |
| **Reversal-after-Tier-1-macro** | **No reversal.** Only Tier-1 print (NFP) landed Friday and produced continuation; weekly close_pos 0.87 | Fade the catalyst-day move | **PRE-REGISTERED** | PR-WT |
| **Inside / outside week** | Neither, in any index | — (no signal to accrue) | **PRE-REGISTERED** | PR-WT |

### Two what-ifs that argue *against* their own features

Both were run on the panel (indices, full 5-day weeks) purely as documentation.

**Weekly hammer/hanging — the feature that "worked" this week has a NEGATIVE panel mean.**
n=8 occurrences, mean next-week **−0.71%**, up only **3 of 8**.

| | wk | next-wk |
|---|---|---|
| IWM | 04-27 | +1.96% |
| QQQ | 05-18 | −4.34% |
| QQQ | 06-08 | −4.78% |
| QQQ | 07-06 | −3.12% |
| **QQQ** | **07-27** | **+5.05%** |
| SPY | 02-02 | −1.11% |
| SPY | 06-08 | −2.50% |
| **SPY** | **07-27** | **+3.18%** |

The two hammers that fired this week are the **two best observations in the entire sample**, and the
other six average −2.32%. A feature whose sign flips on 2 of 8 observations is noise. This is
precisely the week where a Layer-3 pattern would have felt most compelling and would have been most
dangerous to size.

**Large-body thrust week — looks great, and the N is fake.**
n=7 matured, mean next-week **+2.12%**, up **6 of 7**. But every one of the seven comes from just
**three calendar weeks** (2026-04-06, 04-13, 05-04) counted across three highly-correlated indices —
and all three sit inside the same April–May post-drawdown rebound. **Effective independent N ≈ 3, in
one regime episode.** This is the cluster trap the calibration-audit book already warned about
(per-name/per-index stats faking the N); aggregated to the episode it carries no information at all.

Neither feature moves toward Layer 2. Both accrue to the `/calibration-audit` ledger as observations.

---

## 4. Carry-forward

### How last week's Layer-2 calls did
**W31 scored nothing** (`calls[]` empty; OI_FADE `NO_NAME_CLEARED`, MOM_LONG `BASKET_WATCH`), so
there is nothing to grade. The book is **flat — `held_book.py` reads 0 open positions** — and tonight's
daily scan marks an **eighth consecutive session with zero new starters** (07-29 → 08-07) and a fifth
flat session. Three straight weekly reviews with no scored setup is the engine behaving as designed in
a regime that suppresses two of its three lanes, not a failure to find anything.

**The cost of that discipline this week was real and should be stated plainly:** the tape ran
+3.18% / +5.05% / +2.96% and the book participated in none of it. That is the correct outcome — the
long lane fails on measured excess (+0.23% < +0.30%) and the short lanes were crash-guarded against
exactly this thrust — but it is the scenario in which the rules are most tempting to override.

### What rolls into next week

1. **The 2026-08-08 `/calibration-audit` is due tomorrow and is the week's most important open item.**
   The first post-fix h10 OI_FADE cohort (30 rows) **matured 08-03 → 08-07, closing today**. It is the
   live test of the 2026-08-01 audit's first real decay signal (new-evidence cohort −3.73%, hit−base
   −0.53). The lane correctly declined to hand-reconstruct which scan rows constitute that cohort
   rather than emit a number that is not the audit's own. **This becomes checkable tomorrow.**
2. **The persistence-attribution defect** (above): the daily scan's 5-day window disqualifies both
   UTHR and USFD on persistence, yet reported them as regime-blocked only. Worth deciding at the audit
   whether the daily lane applies the ≥0.85 rule at its own window, and whether persistence should be
   window-normalized — the metric mechanically falls as the window widens.
3. **The stand-down margin is the thing to watch.** +1.01pp above trigger, and Friday's decay
   *flattened* (−0.11pp vs −1.91pp) while ret10 kept rising. If it lapses, MOM_SHORT and OI_FADE both
   reactivate into a tape at cycle-low VIX — and UTHR would be the first name up, on a build whose
   cleanliness is horizon-dependent. Pre-decide that one before it becomes live.
4. **Event risk inside a 2–4 week hold:** **CPI 08-12 and PPI 08-13** both land in week 1 of any
   weekly hold (−1 tier on anything ever sized). FOMC 09-15/16 sits just outside a 4-week hold.
5. **Breadth-vs-flow divergence** (63.8% green tape vs only 37.7% bullish options flow) and **QQQ
   still −2.38% below its June peak** are the two facts that argue this rebound is less complete than
   the headline weekly candles suggest. Neither is scored; both are worth carrying.
6. **`prices.parquet` coverage gap persists** — FIVN absent, correlation fail-closed. Unchanged root
   cause (frozen `universe.json` spine).
