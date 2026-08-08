# Market Scan — 2026-07-08

## Regime & Verdict
- **Regime:** UPTREND (marginal/chop-adjacent) · `directional_tradable` = **TRUE** · `s1_standdown` = **FALSE**
- **Vol-state:** negative-gamma / vol-expansion-prone — 2nd-moment conditioner only, no direction read
- **Breadth:** narrow, ~23–33% participation, Tech-concentrated divergence (index strength ≠ broad strength)
- **Regime cap:** both UW and Finviz independently call for **HALF position sizes book-wide** on this tape.
  This is a ceiling on top of (not a replacement for) the excess-implied size — it binds on the OI_FADE
  HIGH-lane name (which would otherwise cap at half anyway) and is a no-op on the starter-tier names.
- **Event risk:** June CPI **2026-07-14** + PPI **2026-07-15** (both Tier-1) fall inside the h10 window opened
  by any short taken this week (~07-08→07-22), and inside the S2 h5 window (~07-09→07-15) even more tightly
  than last week. Bank earnings cluster 7/14–15 also sits in this window. Applied as
  **defined-risk-through-print** on the idiosyncratic single-name OI_FADE/S2 theses (not macro-directional
  bets), consistent with 07-07 treatment — not an automatic −1 tier.
- On a beta-heavy, negative-gamma, narrow-breadth tape the gate stack matters **more**, not less
  (`RESEARCH/50 §5.1`: ungated additive-confluence realized −8.2%, 0-for-6).

> **Bottom line: a small, gate-thinned book — 4 sized names (1 half, 3 starter).** OI_FADE contributes UDR
> (half, cleanest persistent build, CONFIRM) and AROC (starter, tail-capped down from the HIGH-lane half
> ceiling for a decaying build + offsetting revenue growth). NRG is OI_FADE's third clean-build candidate
> but is **VETOed** by fundamentals — watch-only, not sized. CGNX is a tape-beta trap (0.71 SPY beta) in a
> Tech-concentrated narrow-breadth regime — shorting it here is effectively fighting the one thing propping
> up the index — watch-only regardless of flow. S2 contributes PG and IBM at starter (both CONFIRM). The
> MOM_SHORT industrials cluster (SPCX/GGG/TXNM/PATK/FDXF, corr≥0.70, collapsed to one theoretical position)
> is **held at watch — no fundamentals verdict on file**, flagged back to the orchestrator for next-run
> spawn. S4's only candidate, AWR, **fails the liquidity floor outright** ($35.2M ADV < $50M) and is
> dropped — a correction to the Phase-B "Advisory/half" tag, which did not verify liquidity. MOM_LONG fired
> no named candidates — basket composition (Financials 21.9% + Real Estate 11.8%, a crowded rate-narrative
> cluster) is noted but not actionable without tickers, and the narrow-breadth caveat argues against
> chasing this leg even if it were.

## Directional Book (excess-scored)
| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | Size | Invalidation | Gates |
|---|---|---|---|---|---|---|---|---|
| **UDR** | OI_FADE | short | h10 | +2.1% median (hit 0.61 vs 0.41, n=640) | 0.65 | **half** | Close > $42.00, or the 5d net call-OI build fully unwinds without downside follow-through | CONFIRM (3/4 EPS miss, insider MSPR −27.67, Truist downgrade 7/8) · liquidity PASS ($39.83, $161.2M ADV) · cluster: SUI–UDR corr 0.68 < 0.70 gate, SUI is watch-only so no live pair to collapse · event: CPI/PPI defined-risk-through-print; earnings 7/27–29 outside h10 · tail cap: HIGH-lane half ceiling, no squeeze risk (SI 4.53%/DTC 3.32), standalone REIT (not mega-cap beta) |
| **AROC** | OI_FADE | short | h10 | +2.1% median (hit 0.61 vs 0.41, n=640) | 0.45 | **starter** | Close > $42.23, or the 5d build decays further and flips negative without downside follow-through | CONFIRM (insider MSPR −100, SA downgrade 7/7) · liquidity PASS ($39.56, $94.5M ADV) · cluster: standalone Energy, no ≥0.70 partner · event: CPI/PPI defined-risk-through-print; earnings 8/03 outside h10 · **tail cap: decaying daily build magnitude + offsetting +22.66% YoY revenue growth downgrades one tier below the HIGH-lane half ceiling** (documented judgment, not a fundamentals downgrade — verdict remains CONFIRM) |
| **PG** | S2_dp_revert | long | h5 | +0.47% (moderate lane) | 0.50 | **starter** | Same-day news/catalyst invalidates the reversion mechanism, or the one-sided DP concentration unwinds without the expected 3–5d reversal | CONFIRM (insider MSPR +55, Citi buy-ahead-of-earnings) · liquidity PASS ($148.40, $1.39B ADV) · cluster: standalone Consumer Defensive · event: CPI/PPI both fall inside the h5 window — noted, not gated (short-horizon mean-reversion long, not a macro-directional bet); earnings 7/29 outside h5 · tail cap: no same-day catalyst identified; Citi note supports rather than contradicts the thesis |
| **IBM** | S2_dp_revert | long | h5 | +0.47% (moderate lane) | 0.50 | **starter** | Same as above; also re-check ahead of IBM's 7/22 earnings before any hold-through past this window | CONFIRM (beat-streak 4/4, RSI 64.9) · liquidity PASS ($302.05, $2.46B ADV) · cluster: standalone Technology, long-only so no tape-beta-trap concern (contrast CGNX) · event: CPI/PPI inside h5, noted not gated; earnings 7/22 outside h5, flagged for re-check · tail cap: no same-day catalyst identified |

**Cut to watch/dropped (not sized, detail below):** OI_FADE — NRG (VETO), CGNX (tape-beta trap), TDG/SLM/ENSG/INSP/SUI/NESR/VVX/ORA (single-day-print artifacts, not persistent). MOM_SHORT — SPCX/GGG/TXNM/PATK/FDXF (industrials cluster, missing fundamentals verdict). S4 — AWR (liquidity FAIL, dropped). S2 — MU (disqualified upstream, 61.6% two-sided flow, not a concentration event).

## Vol Book (non-directional)
- **JNJ** (primary) — earnings 2026-07-15 premarket, IVR 86.3, implied move **1.41%** ($3.71). IV rich vs.
  realized (the "kink" the lane targets). Liquidity PASS ($263.40, $2.42B ADV). Small size, wide wings,
  two-sided tail; net-of-cost expectancy not independently recomputed — do not enter until it prices
  net-positive.
- **NFLX** (primary) — earnings 2026-07-16 postmarket, IVR 97.0, implied move **2.00%** ($1.51). Liquidity
  PASS ($75.59, $3.73B ADV). Same structure discipline as JNJ.
- **CTAS** (primary) — earnings 2026-07-15 premarket, IVR 85.9, implied move **1.64%** ($2.96). Liquidity
  PASS ($180.17, $392.6M ADV). Same structure discipline.
- **ASML / ABT / STT** (secondary) — IVR 95.3 / 93.7 / 81.9 respectively, implied moves 3.54% / 1.56% /
  5.68%; earnings 7/15–7/16, all premarket except NFLX. All clear the $50M liquidity floor comfortably.
  STT is the one bank name that survives the "banks excluded IVR<80" screen (81.9 clears); it also sits in
  the 7/14–15 bank-earnings cluster called out in the event calendar — that cluster **is** the trade for
  STT, not a separate downgrade.
- **0DTE-VRP (SPY/QQQ): STAND ASIDE both books.** VRP negative net-of-cost; GEX fully negative. No edge to
  sell premium in a negative-gamma tape — the unsampled left tail is not compensated here.

## Watch / Stood-down
- **OI_FADE VETO (dropped entirely):** **NRG** — beat-streak + insider buying + bullish AI-power catalyst
  directly contradicts the fade thesis.
- **OI_FADE tape-beta trap (watch, not a fundamentals question):** **CGNX** — 0.71 SPY beta; in a
  Tech-concentrated narrow-breadth regime, shorting the one mega-beta Tech name in the cohort is a QQQ-beta
  short in disguise (`RESEARCH/50 §5.3` logic extended from the mega-cap OI_FADE case) — held at watch
  regardless of flow signal quality.
- **OI_FADE single-day-print artifacts (not persistent, lane requires a 5-session build):** **TDG, SLM,
  ENSG, INSP, SUI, NESR, VVX, ORA.** SUI additionally sits at a sub-threshold 0.68 correlation with UDR
  (noted, not collapsed — gate is ≥0.70 and SUI isn't live regardless).
- **MOM_SHORT industrials cluster — held at watch, missing fundamentals verdict (flagged back to
  orchestrator for next-run spawn):** **SPCX, GGG, TXNM, PATK, FDXF.** All five sit near their 52-week lows
  (SPCX $148.30 vs. 52w-low $147.11; GGG, TXNM, PATK, FDXF similarly compressed) and correlate ≥0.70 as a
  single industrials/rate-sensitive theme — collapsed to **one theoretical position** (`cluster_id
  mom_short_industrials_cluster_0708`) that will size at starter (the MOM_SHORT lane ceiling for a +0.81%
  mean edge) *if and only if* a fundamentals verdict clears next run. Not S1-crash-gated
  (`s1_standdown`=FALSE) — the block here is purely the missing veto check, not the regime.
- **S4 sentiment-contrarian — AWR dropped, liquidity FAIL:** close $83.58, 20d $-ADV **$35.18M**, below the
  $50M fail-closed floor. This corrects the Phase-B "Advisory/half" pre-size, which did not verify
  liquidity — per the fail-closed rule, a name that cannot be verified liquid is dropped, not merely
  downsized. With AWR out, the S4 lane contributes nothing today.
- **S2 disqualified upstream:** **MU** — 61.6% two-sided options flow, not a genuine one-sided DP
  concentration event; the mean-reversion mechanism this lane trades does not apply.
- **MOM_LONG — no named candidates fired.** Composition note only: the near-52w-high universe skews
  Financials (21.9%) + Real Estate (11.8%), a crowded rate-narrative cluster, and MOM_LONG is basket-only
  by construction (never per-name HIGH, tail-driven +2.35% mean). The narrow-breadth caveat argues this
  leg would likely stall if breadth ever expands — not a today problem since there's nothing to size.

## Risk
- **Correlation clusters applied:** (1) SUI–UDR at 0.68, sub-threshold, no collapse, and moot since SUI
  isn't live; (2) SPCX/GGG/TXNM/PATK/FDXF at ≥0.70, collapsed to one theoretical MOM_SHORT position, held
  at watch pending fundamentals. No other pairwise correlations ≥0.70 identified among today's sized names
  (UDR/AROC/PG/IBM span four different sectors — Real Estate, Energy, Consumer Defensive, Technology — with
  no shared theme).
- **Tape-beta trap gate:** CGNX excluded on the mega-cap-QQQ-beta logic extended to single-name narrow-
  breadth exposure — a reminder that this gate isn't only about literal OI_FADE-cohort mega-cap dominance;
  it's about any short whose realized behavior is closer to "short the index's one working sector" than
  "short an idiosyncratic flow signal."
- **Event overhang:** CPI (7/14) + PPI (7/15) sit inside every h10 window opened this week and inside the
  S2 h5 window even more tightly than 07-07's read (PPI now lands on day ~5 of a 5-day window that starts
  closer to today). Applied as defined-risk-through-print on UDR/AROC (OI_FADE) and PG/IBM (S2) — not an
  automatic downgrade, since none of these are macro-directional bets. Bank-earnings cluster 7/14–15 is the
  trade itself for STT (vol book), not a separate risk.
- **Liquidity floor caught one real miss:** AWR ($35.18M ADV) fails the $50M fail-closed floor outright —
  dropped, not downsized, correcting the Phase-B "Advisory/half" pre-size tag. All four sized directional
  names and all six vol-book names clear the floor with real margin (lowest is AROC at $94.5M ADV).
- **Regime-cap discipline:** the book-wide HALF ceiling from UW+Finviz is a no-op here except on UDR, which
  was already capping at half from its own HIGH-lane excess. No name was sized above half; the hard rule
  (never up-size above the excess-implied size) held throughout — AROC's tail-cap and AWR's liquidity drop
  are both downgrades, never upgrades.
- **Missing-verdict discipline:** the MOM_SHORT industrials cluster is a real, regime-appropriate,
  correlation-collapsed candidate sitting on the sideline purely because its fundamentals verdict hasn't
  been run yet — flagged back to the orchestrator, not silently dropped or silently sized.
- **Hedge note:** with only one short (UDR, half) and one starter short (AROC) against two starter longs
  (PG and IBM), net book exposure is modestly long and small. In a negative-gamma, narrow-breadth tape this
  is a deliberately thin book — consistent with invariant #3 ("most days have no directional edge — say
  so"), even though today does clear the bar for a handful of names.

---
*Envelope: `decision.json` (schema v2, validated — see confirmation below). Conviction write-back persisted
to `conviction_2026-07-08.json` for next run's adverse-flow exit check (UDR, AROC, PG, IBM). Regression gate
not run tonight — no lane/threshold changes made.*
