# Market Scan — 2026-07-30

## Regime & Verdict
- **Regime: CHOP** · ret5 **+0.480%** · ret10 **−1.200%** · dd15 −2.830% · `directional_tradable=TRUE` · `s1_standdown=FALSE`
- **Vol-state:** VIX **17.09, −17.3% on the day** — the 07-29 spike to 20.66 fully round-tripped in a single session. SPY GEX **−$366.9M FULLY_NEGATIVE**; QQQ **NEGATIVE** (spot 683.77 vs zero-gamma 729.4). Dealer-short-gamma on both = **vol-expansion** conditioning. VRP **FAIR** both indices (SPY +0.0126, QQQ −0.0057) — nothing rich to sell. Front-end backwardation SPY 1.296× / QQQ 1.445×.
- **Breadth: DIVERGENT.** SPY closed **+1.68%** on only **39.17% green** (197 adv / 304 dec); UW bullish_pct 35.7%, trend CHOPPY/TRANSITIONAL. Today's bounce was **narrow and mega-cap/Tech-led, not breadth-confirmed.** QQQ +3.30% on the day but still −1.22% ret5 / −3.17% ret10 — the AI-capex repricing leg has **not** round-tripped.
- **Bottom line: no new directional edge tonight — zero new starters.** Two names cleared every mechanical lane gate and **both were VETOED at gate 4 on fundamentals.** One held short (PLNT) is carried at unchanged half size with **2 sessions to a binding exit**. Vol book has two clean earnings-crush candidates; the 0DTE sleeve stands down.

## Directional Book (excess-scored)

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| **PLNT** | OI_FADE | short | h10 | +0.70% (n=906, hit 0.56 vs 0.38) | 0.5 | **half (HOLD)** | earliest of **08-03 close (binding h10)** · first negative `call_net` (not triggered: +233/+42/net +191) · close > $59.50, 1-day confirm (6.29% away, ACTIVE) | all PASS |

No new starters. Everything else below is watch or advisory.

### Why the two clean signals were killed
Both cleared liquidity, ETP, earnings-window, catalyst-split and persistence — then failed the fundamentals veto channel, which exists precisely to separate *crowding* from *corroborated conviction*.

- **AVTR — VETO.** Cleanest OI signal of the night (oi_net_5d **+101,124**, rel_build 2.713, persistence **0.47** = genuinely organic). The 2026-W29 objection against it (single-day block, persistence ~1.0) **is resolved**. But: Q2 beat +8.58% with FY guidance **raised**, and **five same-day PT raises on 07-30** (WFC $14→16, Stifel $8→15, Evercore $10.5→14, MS $10→14, RBC $9→14), zero cuts, insider MSPR +33.33. Price **+22.12% ret5**, RSI 75.68. This is the ROST/ALLE pattern exactly.
- **HRI — VETO carried and reinforced from 07-29.** The recorded re-admit condition was specific: *the analyst tape must turn.* It did the opposite — KeyBanc **raised** $165→$185 and BNP **raised** $160→$165 on 07-29, zero cuts. **Condition NOT MET.** Separately, ret5 −10.62% means an entry would short a completed collapse, and the lane's edge is measured on the general population of heavy-call-build names, not on names already down double digits.

*Recorded for fairness:* HRI's PE ~99× and D/E 4.18 are genuinely stretched, and the −14.6% unwind off the 07-28 high reads as a valuation reset — a real reason the short could still work. It is not enough to overturn a gate whose bar is "do the fundamentals contradict the thesis."

## Vol Book (non-directional, delta-neutral, 0 directional points)

**Earnings IV-crush — SELL VOL.** Note the screen inverted the usual assumption: most of the IV-rank ≥ 80 list is IV-**cheap** vs its own realized post-print history (TWLO 2.7% implied vs 13.5% realized; AKAM 2.8% vs 14.9%; AMD 3.5% vs 9.1%; PLTR 2.2% vs 12.4%) — IV rank is a *level*, not an edge. Four names are actually rich:

| Symbol | Earnings | Implied | Realized avg / max | Verdict |
|---|---|---|---|---|
| **LDOS** | 08-04 | 8.5% | 1.7% / 6.2% (n=7) | **SELL** — iron fly 08/21, wings beyond the 6.2% realized-max |
| **TRMB** | 08-05 | 8.6% | 2.4% / 5.4% (n=8) | **SELL** — best liquidity of the group |
| **TTMI** | 08-05 | 19.7% | 7.9% / 16.6% (n=8) | SELL, **reduced size** — thin chain (~900 opt/day) |
| **UCTT** | 08-03 | 22.3% | 10.3% / **28.2%** | **EXCLUDED** — worst historical print *exceeds* today's implied move |

All defined-risk, wings set at the realized-**max** print, never at the implied move. ATM spreads run ~16–24% on these monthlies; no measured cost constant exists for this sleeve, so `net_expectancy` is left **null** rather than fabricated.

**0DTE-VRP — STAND DOWN, both indices.** The script returned `GO_PREMIUM_SELL_INTRADAY` with positive net math (SPY gross +0.246% → **net +0.146%/day**; QQQ +0.376% → **net +0.276%/day**) and was **overridden**: front-end backwardation on *both* (1.296× / 1.445×) + dealer-short-gamma on *both* + a fresh ~21% one-day VIX round-trip is the unsampled-left-tail combination the tail cap exists for. The 60-day sample behind those averages contains no analog.

> **Maintenance item (not patched tonight):** `scripts/zerodte_setup.py` **misclassified QQQ as long-gamma** — its `recommend()` path sums net gamma over 0–45DTE instead of using the spot-vs-zero-gamma-level convention the CLI `gex` command applies, so it picked the quiet/mean-reverting branch. Logged, not fixed: a code edit tonight would trip the regression gate mid-scan.

## Watch / Stood-down
- **OI_FADE mechanism failures — OLLI, INFY.** Both fail the lane's *own* multi-day-build test: persistence **0.974** (OLLI: +6,672 of a +6,850 build landed in ONE session, today) and **0.993** (INFY: a ~108K-contract single-session block). A same-day mega-block on a dealer-short-gamma bounce day is at least as consistent with systematic hedging as with crowd positioning. **Re-check 07-31** — if the build persists a second session, they re-enter. No fundamentals gate was run on either, correctly: they fail upstream of gate 4, and this repo gates only names about to be sized.
- **MOM_SHORT — watch-only (SNPS, WSO, LHX, VICI).** Capped by CLAUDE.md invariant #6: the lane's **−0.03% mean** is a known-negative recorded exception. WSO is the archetype of the lane's risk (RSI 22.2, ret2 −15.45%). BLDR/QXO/PEG earnings-blocked.
- **MOM_LONG — 108-name near-high basket, watch-only BY THE RUBRIC** (+0.18% mean is below the +0.3% MEDIUM threshold; median −1.06%, tail-driven). Cohort data has been supportive three sessions running, but the validated prior is what sizes.
- **S2 (advisory, +0.06%)** — 40 survivors; top PLD, FCX, DHI, CFG. The lane's own read: one-sided concentration is a **binary event gate with IC ≈ 0**, not a ranking signal — do not read the biggest print as the best candidate. Five vetoed on same-day/recent earnings (ITW, PNC, CBRE, GFL, ACGL).
- **S4 (advisory, +0.44%)** — 37 candidates, 86% assessed **LIVE** PCR rather than stale 07-29 fear. Top: QTWO (147.0), RGEN (82.2), JEF (81.3). Caution: 11 names show `ivrank_chg_5d < −25` — hedging premium already partly harvested.

## Risk
- **Correlation clusters:** none. Max pairwise 0.15 across the measurable set — nothing near the 0.70 collapse threshold. PLNT is the sole open position.
- **Event calendar (10 td):** PLTR 08-03 · AMD 08-04 · **NFP 08-07 (Tier-1)** · SMCI 08-11 · **CPI 08-12 (Tier-1)**. No FOMC. **PLNT's binding 08-03 exit lands clear of its own 08-06 print (3 trading days) and ahead of both Tier-1 macro events.**
- **Tail caps applied:** MOM_SHORT watch-only (invariant #6); MOM_LONG basket-only; S2/S4 advisory-only; 0DTE stood down; UCTT excluded on a breached left tail.
- **CHOP half-cap ceiling:** non-binding — nothing cleared above half in the first place. PLNT was already at half from entry.
- **PLNT stop is NOT vestigial.** Tested rather than asserted: over 133 two-day windows only **2 (~1.5%)** cleared the +6.29% needed to reach $59.50. Low-probability but *not* arithmetically unreachable — the vestigial precedent describes a *winning* position whose stop has been outrun, which is the opposite geometry. Kept live and unchanged; not tightened further, since with 2 sessions left a tighter stop adds whipsaw without shortening a resolution the h10 exit already caps.

### Two process findings
1. **Gate-1 dissent — raised by `risk-sizer`, DECLINED by the orchestrator.** It argued the tape *shape* is a textbook V-rebound and asked to treat `s1_standdown` as FIRED for MOM_SHORT despite the mechanical FALSE. Declined: `regime_check.py` is the authoritative gate the retro harness scores against, and hand-flipping the recorded flag would corrupt the exact field `/calibration-audit` uses to grade whether the crash gate works. The caution is real and recorded — Phase A raised it independently — but it changes nothing operationally, since MOM_SHORT is already unsized under invariant #6. If the shape recurs, codify a proper up-thrust detector via `/calibration-audit` rather than re-litigating nightly.
2. **MOM_LONG lane bug, second consecutive night.** The lane again returned **ROST** inside its own basket; ROST carries a standing fundamentals VETO/DROP from 2026-07-20. It still does not run `prior_verdicts.py` against its own output. Excluded by the orchestrator both nights. Flagged 07-29, unfixed — worth a maintenance ticket.

### Data note
Preflight initially **failed (exit 1)**: the truth-set parquets ended 07-29, one session behind the trade date. Rebuilt `prices` / `returns` / `features` through 2026-07-30 before any lane ran; re-run went clean (exit 0). This is the failure that produced an inverted regime read on 2026-07-24 — no lane read a stale panel tonight.
