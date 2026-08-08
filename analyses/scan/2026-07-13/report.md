# Market Scan — 2026-07-13 (Mon, post-market)

## Regime & Verdict
- **Regime:** UPTREND, shallow/late-stage — 2d pullback off the fresh SPY high 754.95 set 2026-07-10. `directional_tradable = true`, `s1_standdown = false` (MOM_SHORT and OI_FADE shorts LIVE, not crash-gated).
- **Vol-state:** GEX **FULLY NEGATIVE** on both SPY and QQQ this week — the whole index complex is short-gamma, an amplifying/whippy 2nd-moment conditioner only, no direction read. VIX popped **+14%** (15.03 → 17.16) heading into CPI — a pre-print vol-of-vol bid, not a regime break.
- Flow-breadth bearish-skewed (33.8% bullish-flow tickers) — noted as a flow-vs-price dissent, not gated.
- **Event calendar (h10 window 07-13 → ~07-27):** CPI 07-14 (T+1), PPI 07-15 (T+2), Retail Sales 07-16, U Mich 07-17 — four Tier-1 macro prints inside the window, front-loaded into days 1–4. FOMC 07-29 falls just outside it.
- **Bottom line: 2 sized calls, both starter, both short** (ICE new; ORCL new) — plus one carried-forward open position (MAT, unchanged). The book stays thin and short-tilted into a print-heavy week; nothing sizes above starter. This is intentional — the late-stage-uptrend-into-CPI/PPI backdrop is exactly when the half-cap-no-auto-full discipline should bind hardest, not loosen.

## Directional Book (excess-scored)
| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | Size | Fundamentals | Invalidation | Gates |
|---|---|---|---|---|---|---|---|---|---|
| **MAT** *(carry-fwd, not re-sized)* | OI_FADE | short | h10 (→~07-27) | +2.07% median (n=640) | 0.5 | **starter** *(unchanged)* | CONFIRM (carried; Goldman Sell, 3rd PT cut, fresh 52w low) | Close > $16.50, or OI build unwinds | liq PASS ($13.84, $65.7M ADV) · entered 07-10 $13.33, now ~$13.84 · thesis intact/accreting |
| **ICE** | OI_FADE | short | h10 (→~07-27) | +2.07% median (n=640) | 0.35 | **starter** | CAUTION −1 (beat-streak + strong margins fight the short; insider selling backs it) | Close back above pre-build breakout, or OI unwinds | liq PASS ($137.67, $708.7M ADV) · no earnings-in-horizon (07-30 outside) · CAUTION knocked half→starter |
| **ORCL** | MOM_SHORT | short | h10 (→~07-27) | +0.81% mean (n=273) | 0.45 | **starter** | CONFIRM (BBB− downgrade / "first domino" narrative) | RSI reclaims >45 + close back above range, or rating reversed | liq PASS ($131.54, $4.54B ADV) · no earnings-in-horizon · standout of the 17-name MOM_SHORT cohort, never single-name HIGH regardless of CONFIRM |

*No name is sized above starter tonight.* MAT is an existing position, not a new decision — flagged separately to avoid double-counting. Every other deviation from a lane's implied ceiling was a **downgrade** (ICE half→starter on CAUTION), consistent with half-cap-no-auto-full and the hard "never up-size" rule.

## Vol Book (non-directional, delta-neutral, net-of-cost, advisory — 0 directional points)
- **Earnings IV-crush SELL-VOL** (CPI/PPI/Retail-Sales/U-Mich all land mid-cluster — realized-vol risk is elevated this week):
  - **NFLX** primary — cleanest and most liquid (IV rank 100, implied move 6.86%, front/back 2.08×, ER 07-16 postmarket, 3d out).
  - **TSM** secondary (liquid, ER 07-16 premarket, 3d out). **ASML, CAG** (ER 07-15 premarket, 2d out) and **CTAS, ABT** (2-3d out) — advisory/half-size, richness not independently re-verified this run.
  - **CAG** small-size only — thin options liquidity despite adequate equity ADV.
  - **MAN excluded/veto** — equity ADV clears the $50M floor but the options chain itself is illiquid; a delta-neutral structure can't be entered/exited at a fair net-of-cost price. Equity-liquidity-floor pass does not override an illiquid options market.
- **0DTE-VRP: HARD STAND-ASIDE both SPY and QQQ.** SPY — the VIX-spike gate fired (+14% pop into CPI/PPI, negative gamma into two Tier-1 prints is the opposite of a clean VRP setup). QQQ — negative 30d VRP (premium-buying/cheap vol) + negative gamma + front-end backwardation all argue for *buying* convexity, not selling it. No premium-selling this week on either index.

## Watch / Stood-down
- **Fundamentals VETO → watch-only:** ESI (active $14.5B Solstice M&A target signed 07-06 — crowded call OI is merger-arb positioning, not a bearish signal; **re-tag as merger-arb**, drop from OI_FADE).
- **OI_FADE borderline persistence/identity → watch:** OLED, QXO (also MOM_SHORT cohort members below), AI (identity/ticker-ambiguity caveat), BIRK (thin history / foreign-private-issuer structure distorts relative-build ranking — same artifact family as the prior JPST flag).
- **Earnings-in-horizon → held at watch:** GTX, CSX (OI_FADE signal real, but earnings fall inside the 07-13→~07-27 window).
- **MOM_SHORT 17-name cohort, missing fundamentals verdicts → held at watch (cannot size unverified):** JOBY, SMR, ECHO, CPRT *(prior VETO 07-10 carried as informational caution)*, NNE, HONA, ROAD, QXO, HLI, OLED, STWD, XE, BDC, PATK, DLB, CNM. Flagged for next-run fundamentals-gate spawn. ORCL is the one cohort member sized (see book above).
- **MOM_LONG basket** (222 names, tail-driven +2.35% mean, documented never per-name HIGH): top-proximity energy refiner cluster **PBF/DINO/MPC/VLO/PSX** — collapsed to **one** correlation-cluster slot (crack-spread/refining-margin theme, assumed corr ≥ 0.70).
- **S4 sentiment-contrarian (advisory-size-only lane):** WCN (PCR 127, 99.6th pct) — CAUTION −1 (puts likely routine hedging, not informed) **and** earnings 07-22 fall inside the h5-10 hold window (binary event risk). Held at watch/advisory regardless of the lane's own +0.71% median — S4 is advisory-size-only by design.
- **S2 liquidity-reversion: EMPTY.** No name cleared the catalyst-verification gate tonight.

## Risk
- **Correlation clusters collapsed:** `mom_long_energy_refiner_cluster_20260713` (PBF/DINO/MPC/VLO/PSX) → 1 slot. MOM_SHORT cohort treated as one basket exposure (no pairwise correlation matrix computed this run — momentum-crash tail-cap discipline already forbids per-name HIGH regardless). ICE vs ORCL checked and NOT clustered — distinct sectors (financial exchange vs software), no assumed correlation.
- **Event calendar (h10 window 07-13 → ~07-27):** CPI 07-14, PPI 07-15, Retail Sales 07-16, U Mich 07-17 — four Tier-1 macro prints front-loaded into days 1-4, treated as defined-risk-through-print macro tag on the whole short book, not an automatic −1 (consistent with 07-10 precedent). WCN earnings 07-22 is name-specific event risk on the one advisory long. FOMC 07-29 falls just outside the window — awareness only.
- **Tail caps applied:** OI_FADE (MAT carried, ICE) and MOM_SHORT (ORCL) all sized for the momentum-crash/squeeze tail against an up-biased tape — none above starter, none single-name HIGH. MOM_LONG kept basket-only (energy cluster collapsed). Vol-short sized for the left tail, quoted net-of-cost, with the MAN options-illiquidity veto and the hard SPY/QQQ 0DTE stand-aside both erring toward caution given negative gamma across the board this week.
- **Hedge note:** GEX fully negative on *both* SPY and QQQ (not just QQQ, as on 07-10) — the whole index book is short-gamma into a four-print macro week. This is the most fragile vol backdrop of the last several scans; size discipline (nothing above starter) is doing real work tonight, not just following the standing policy mechanically.

---
*Envelope: `decision.json` (v2, validated against `schemas/decision_envelope.v2.schema.json` — PASS). Conviction persisted: `conviction_2026-07-13.json` (MAT carry-forward + ICE + ORCL) for next-run adverse-flow exit checks. `watchlist_write_back_confirmation`: 28 names written back to `decision.json`'s `watchlist_write_back` array (ESI, OI_FADE watch cohort, MOM_SHORT watch cohort, MOM_LONG energy cluster, WCN, MAN) — CONFIRMED. No lane/threshold change this scan → regression gate not triggered.*
