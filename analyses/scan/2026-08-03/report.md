# Market Scan — 2026-08-03

## Regime & Verdict

- **Regime: UPTREND/REBOUND-THRUST** · `ret5 +2.510%` · `ret10 +2.100%` · `dd15 −1.700%`
- **Vol-state:** long-gamma on both indices but **fragile** — SPY `total_gex +$1.286B`, spot 757.93 vs zero-gamma 756.06 (**+0.25%** above the flip); QQQ `+$774.4M`, spot 700.19 vs 699.22 (**+0.14%**). VIX 15.86, VIX/VIX3M **0.838** (steep contango).
- **Breadth:** 67.59% green (340 advancers / 163 decliners) — breadth confirms the price move.
- `directional_tradable` = **TRUE** · `s1_standdown` = **TRUE**
- **Bottom line: NO DIRECTIONAL EDGE TODAY.** Zero new starters across all five lanes. One held position (PLNT) closed on its pre-registered h10 time stop, **+0.33% realized short excess**. The vol book is the only actionable output.

### The crash gate fired — by 0.0139pp

`s1_standdown` fired on **leg (a1) alone**: `ret5 +2.5139%` against a `+2.5%` threshold. SPY closing **$0.103 lower** (757.567 vs the actual 757.67) would have left the gate off.

- Leg (a2) — `ret5 > 1.5% AND dd15 < −2.0%` — **did not fire**: dd15 is −1.700%, inside the requirement.
- Leg (b) — inapplicable (ret5 positive).

This is the exact V-rebound the guard exists to catch: the 07-29 hawkish-hold drop (SPY −1.54%, three dissents *for a hike*), the 07-30 cool-PCE rally (+1.68%), weekly hammers on SPY/QQQ, and the thrust still accelerating into today (+1.42%). The 2026-W31 review flagged Friday as a near-miss within 0.4pp; today it crossed.

**The rule is pre-registered and binds regardless of margin** — overriding it on thinness is precisely the discretionary move the framework disfavors. And it costs nothing tonight: MOM_SHORT is watch-only capped for new starters under invariant #6 and its baseline excess is negative, so no live sizing depended on the gate either way.

## Directional Book (excess-scored)

**EMPTY.** No name in any lane cleared its bar.

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

### Held position — closed today

| | PLNT |
|---|---|
| Lane / dir | OI_FADE short, half size |
| Entry | 2026-07-20 @ **$55.25** (panel close; the 07-31 file recorded $55.20) |
| Exit | 2026-08-03 @ **$56.23** — h10 window `07-21 → 08-03`, confirmed via `_calendar.hz_end()` |
| Gross | **−1.77%** |
| SPY, same window | +2.10% |
| **Since-entry short excess** | **+0.33%** |

A **positive-excess resolution despite a negative gross P&L** — the distinction invariant #1 exists to preserve. The path was violent: **+2.89%** excess at its 07-22 peak, **−3.40%** at the 07-29 FOMC trough, back to +0.33% at the bell.

Pre-registered leg (b) ("first genuinely negative `call_net`") **never confirmed** — today's net-OI printed **+66** (call +72 / put +6) after Friday's lone −335. The $59.50 discretionary stop was never approached (max close over the whole hold: $56.23). The position exited on the timer, as designed. PLNT reports 2026-08-06, so it is earnings-blocked for any re-entry.

## Vol Book (non-directional, delta-neutral, advisory)

### Earnings IV-crush — SELL-VOL

All four clear iv_rank, imminent catalyst, **genuine** term-structure backwardation, and the liquidity floor. Structures are wide-wing defined-risk, sized for the binary's two-sided tail; resolve against **realized vs implied move**, never direction.

| Ticker | ER | iv_rank | Implied move | Term structure |
|---|---|---|---|---|
| TWLO | 08-06 | 96.7 | 12.1% | 4d 173.2% → 11d 117.7% → 18d 95.7% (`near_dte_actual=4`, not guarded) |
| TTMI | 08-05 | 97.6 | 18.5% | 18d 127.4% → 46d 112.2% → 74d 104.7% |
| ONTO | 08-06 | 96.8 | 17.7% | 18d 112.5% → 46d 109.1% → 137d 100.2% |
| MKSI | 08-05 | 96.1 | 15.7% | 18d 104.2% → 46d 91.5% → 74d 91.4% |

> **`net_expectancy` is deliberately null.** No per-ticker realized-vs-implied crush history or live bid/ask feed was available tonight, and the lane declined to invent one. The qualitative edge (realized undershoots implied) stands; **verify live spreads before any fill.**

**Excluded:** ACLS, NVMI — genuine backwardation but options OI too thin (10/19/39 and 57/4/31 contracts) to support wide wings without material slippage. MCD, KHC, LDOS, CACI — implied moves (3.4–8.4%) too small to clear a realistic spread cost.

### 0DTE-VRP — GO both, half-size and below

| | SPY | QQQ |
|---|---|---|
| Verdict | GO_PREMIUM_SELL_INTRADAY | GO_PREMIUM_SELL_INTRADAY |
| Structure | iron fly centred **758.0**, wings ±0.8% | iron fly centred **700.43**, wings ±1.41% |
| Size | **×0.5** | **×0.25** |
| Net mean P&L | **+0.139%/day** | **+0.269%/day** |
| Caution | none | genuine front-end backwardation |

Enter at/after the open once the gap resolves; **never carry overnight** — QQQ's overnight leg is an outright loser (−0.085%/day). Stand aside if the open gaps beyond the wings.

**Left-tail caveat:** the 60-day validation window contains no vol-shock day — this is a floor, not a promise. Both indices sit only fractionally above their flip (SPY +0.25%, QQQ +0.14%), so a modest pullback flips either into short gamma. **Re-verify at tomorrow's open; this is not a standing condition.**

## Watch / Stood-down

**MOM_LONG — BASKET_WATCH, 7bp short.** Measured excess **+0.23%** vs the +0.30% bar, and the median is **negative (−0.91%)** — the mean is tail-carried, so the miss is more meaningful than 7bp suggests. Funnel: 457 near-high → 253 post-ETP → 162 post-earnings → **41 present in prices.parquet** → 32 after prior verdicts. Sector concentration 28.1% Industrials / 28.1% Financials, inside the ⅓ cap. All 32 verified present in prices.parquet.

`AMP BAC BNS CR CROX DAL DXCM ETN FCNCA FITB GE GM HIG HON ITW JCI JLL KO LYV MMM NEU NUE RS SCHW SHEL SNOW SWK TGT UBS VLO VSXY WTW`

**MOM_SHORT — STOOD_DOWN.** 2 of 5 passed earnings: CLBK (fail-closed, absent from prices.parquet) and GME. See the process finding below on GME.

**OI_FADE — NO_NAME_CLEARED, fourth consecutive session** (07-29, 07-30, 07-31, 08-03). All 15 top-build candidates die on ≥1 independent gate: 5 earnings-in-window, 5 single-day-block mechanism failures (`persistence > 0.85`), 5 liquidity, 4 ETP, 1 sustained fundamentals VETO (AVTR), 1 resolved-pre-print (KBR — reconfirming the 2026-W31 adjudication). Shorting into a V-rebound thrust is a live headwind; regime_fit was held well below the 0.35 used in W31.

**S2 — ADVISORY/WATCH, 8 names, all below starter** on a regime headwind (the lane's edge concentrates in weak/whipsaw tapes, not trending risk-on). All clean on earnings (h5), liquidity, ETP, and coverage (8/8 present in prices.parquet — verified). h5 window closes 2026-08-11.
`KO WELL GME RTX BNS ADSK EXE CTAS`

**S4 — NO FIRE.** Basket ~**−0.4%**, below starter. Funnel: 96 top-5% PCR → 62 post-earnings → 43 post-ETP → **9 present in prices.parquet** → 6 after the option-liquidity floor. JEF is the cleanest and still lacks a fundamentals verdict; SMTC is an `ivrank_chg_5d` h3 tilt only; CSGP is premium-already-harvested (−22.3%).

**KKR:** the 07-24 h5 earnings block has resolved (reported 07-30), but the separate **2026-07-21/22 EQT/KKR/Advent takeover-rumor tail-block was never re-verified and still stands.**

## Risk

- **Event calendar:** NFP **Fri 08-07** (Tier-1, 4 sessions out — inside any h5 window opened now); **CPI 08-12** and **PPI 08-13** (both Tier-1, inside h10). Any h10 position opened this week carries two Tier-1 prints, arriving while the long end is at multi-year highs (10y 4.74%, 30y 5.28%) on a term-premium move.
- **Phase D was a no-op, recorded as an explicit adjudication, not a silent skip.** With zero names about to be sized, `risk-sizer` had an empty book and `fundamentals-gate` was **not** spawned — Phase D rule 4 gates only names about to be sized. This follows the 07-31 precedent (JEF/DKS/DPZ declined for the same reason).
- **Flow/price divergence (advisory):** `uw risk market-regime` reads composite **TRANSITIONAL** with `bullish_pct 40` (bearish_flow 3770 vs bullish_flow 2514) while price sits at highs. Positioning is more cautious than the tape.
- **IWM still refuses to confirm:** +1.13% over 5d against SPY's +2.51%, echoing last week's flat weekly candle.
- **Correlation clusters:** no live positions, so no cluster exists. Note GME appears in **two orthogonal lanes in opposite directions** (S2 long on 93.3% buy-side DP concentration, $240.6M; MOM_SHORT on a genuine near-52w-low). Per invariant #2 these are never summed — and here they outright conflict. Both are sub-starter/stood-down, so nothing to resolve.

---

## Process findings

**1. Truth set was stale; rebuilt before scanning.** `preflight.py` exited 1 — parquets ended 2026-07-31 against an 08-03 trade date. All three rebuilt (prices/returns/features now reach 08-03, exit 0). Every lane would otherwise have scored off Friday's panel.

**2. `held_book.py:31` EXIT-substring bug bit again (second occurrence).** `CLOSED = (..., "EXIT")` is matched with `in`, so the verdict `HOLD_TO_BINDING_EXIT` is filtered out as closed and the tool printed *"no open positions"* while PLNT was live on its final session. PLNT was reconciled by hand. **One-word fix:** match the terminal verdicts exactly rather than by substring.

**3. `prices.parquet` coverage gap — ROOT CAUSE FOUND.** `build_features.py` builds its spine from the **live screener universe** (2,462 tickers, refreshed nightly); `build_prices.py` reads `data/universe.json`, a **static 785-symbol list frozen 2026-06-28**. Any name that became liquid after June 28 can never enter prices.parquet, so the correlation-cluster gate goes blind and returns an empty result that reads as a pass. Coverage is **783/2,462 = 31.8%**, and it cost real supply tonight: 121/162 MOM_LONG, 34/43 S4, and 12/15 OI_FADE candidates were fail-closed on it. **Fix:** regenerate `universe.json` from the screener spine. Not done mid-scan — it shifts the harness baseline panel and requires a regression-gate re-run under invariant #6.

**4. `earnings_gate.py:64` checks only the upper bound.** `elif ned.isoformat() <= end:` has no lower bound, so a **past** earnings date is blocked and mislabeled *"inside h10"* (LZM was blocked on a 07-29 print that had already happened). It fails closed, so it is safe. **Blast radius is narrow:** of 3,685 names with dates, 130 are "past" — but 114 of those report *today*, where blocking is defensible. Only **16** are unambiguously wrong. **Do not patch in isolation:** `retro_harness.py:63,76,138` carries the identical one-sided bound and does *not* import this script, so fixing the lane path alone would make live lanes more permissive than the instrument that grades them — the exact live-vs-measurement divergence invariant #6 was written for. **Route to `/calibration-audit` as a paired fix + regression-gate re-run.**

**5. The momentum lane inverted its own Yahoo verification (third instance of this class).** It excluded GME as a "false short" on a failed 52w check. The check actually **confirmed** the candidate: Yahoo shows a genuine fresh 52-week low of **18.545 set today**, pct_range 5.4%. The screener's `week_52_low` is stale at **19.93 — above the 19.06 close** — which is what drove `pct_52w_range` to −0.1065 (the *out-of-range* class, which the lane also mislabeled as "in-range-but-wrong"). No live consequence: the standdown and the invariant-#6 cap both bind regardless. But this is the third time a lane has run a gate script and misreported its output (07-31 earnings gate "0 dropped"; the ROST `prior_verdicts` bug). **Independent orchestrator re-runs remain mandatory.**

**6. OI_FADE reported honestly.** Its earnings and liquidity gate results were independently re-run and reproduced **exactly**, name for name. Worth recording alongside the failures.

**7. Both known vol instrument bugs were symptom-free tonight.** `zerodte_setup.py` and `uw options-structure gex` agreed on gamma sign for SPY and QQQ, and the GEX label matched its payload on both (last week's QQQ `FULLY_NEGATIVE` mislabel not reproduced). Neither is fixed — absence of symptom is not a fix.

**8. `near_dte_actual` guard worked, and the correct call was the non-obvious one.** Both SPY and QQQ front-end ratios carried `near_dte_actual=1` and were properly flagged as artifacts. But pulling the **full** `iv-term-structure` showed QQQ's near-term hump is **genuine** (dte1–4 ≈ 25–27% vs dte7–32 belly ≈ 22.6–25%) — so the 0DTE backwardation caution and QQQ's ×0.25 size are real, not artifactual. The guard flags the *2-point ratio*; it does not by itself settle whether the underlying condition is real.

**9. Forward-decay watch on OI_FADE is untested this session.** No new OI_FADE position opened, so nothing from 08-03 enters the post-hygiene-fix h10 cohort maturing 08-03→08-07 as a new signal day. That cohort — the first read on the current engine, and the test of the audit's −3.73% new-evidence decay signal — still resolves this week. **Next audit due 2026-08-08.**
