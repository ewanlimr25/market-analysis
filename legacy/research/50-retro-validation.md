# 50 — Retrospective Validation of the Redesign (Phase 5 proof)

_The redesign, mechanically replayed against known outcomes. `artifacts/retro_harness.py` fires the redesign's lanes on every panel day under the regime gate, then resolves each call's realized **forward excess vs SPY** from the truth set — and contrasts it with the old system's actual `decision.json` calls resolved the same way. This is the proof the whole project was for._

## 5.1 Headline result
Across all 54 panel days (gross, pre-cost, excess-vs-SPY on the conditional benchmark):

### The redesign's lanes — positive excess everywhere
| Lane | n | mean excess | hit | base | **hit − base** | median | read |
|---|---|---|---|---|---|---|---|
| **S1 relative-weakness short** (h10) | 273 | **+0.81%** | 0.48 | 0.38 | **+0.095** | −0.0038 | right-skew momentum short: +9.5pp excess-hit, mean carried by the laggard tail (hold the basket, don't cherry-pick) |
| **S2 DP-concentration revert** (h5, single-name) | 336 | **+0.47%** | 0.51 | 0.49 | +0.015 | +0.0007 | small, symmetric, weak-tape reversion |
| **S4 PCR-high fade-long** (h5, advisory) | 331 | **+0.71%** | 0.52 | 0.53 | −0.015 | +0.0015 | right-skew, advisory |

The regime gate stood S1 down on **6/54** days (rebound/squeeze thrusts) — the documented momentum-crash guard firing exactly when P3 §3.1 said it should.

### The OLD system's actual calls — its biggest bets lost the most
| Old tier | n | **mean excess** | hit | base | hit − base |
|---|---|---|---|---|---|
| **HIGH** (full size) | 6 | **−8.17%** | **0.00** | 0.33 | −0.333 |
| **MEDIUM** (half size) | 15 | **−7.36%** | 0.20 | 0.13 | +0.067 |
| LOW (watch) | 43 | −0.11% | 0.47 | 0.37 | +0.093 |
| DROP | 41 | −0.28% | 0.44 | 0.39 | +0.049 |

**The old system's HIGH-conviction names — the ones it sized full — realized −8.2% vs SPY and went 0-for-6.** MEDIUM realized −7.4%. The tier ordering is not just non-monotone, it is **catastrophically inverted**: the more the additive-confluence rubric liked a name, the worse it did. This independently reproduces — and quantifies in excess terms — the tier inversion the `/calibration-audit` flagged (HIGH 0.222 vs claimed 0.774), and confirms the Phase-2 diagnosis: the heavily-scored lines (accumulation +3, multileg +2, DEX +1) were loading crowded beta that broke in the June pullback the HIGH names were sized into.

## 5.2 Worked example — 2026-06-23 (the sample envelope day)
- **Regime:** CHOP, SPY −2.8% trailing-5d (pullback) → S1 shorts **live**.
- **Redesign fired:** S1 shorts on the relative-weakness cohort — **PLTR, PDD, STLA, DPZ**, and the **China complex** (KWEB/FXI/MCHI/XPEV/LI/YINN/TME) — all within 2% of their 52-week lows; S2 long-reversion on single-name DP-concentration names; S4 fades on put-heavy laggards.
- **The old system that day** sized **long INTC + long SMH** (semis) and a MU vol-short — i.e. it leaned *into* the very semi complex that was selling off, gated only to "watch-only." The redesign's instinct (short the laggards in a pullback regime, stand aside on the semi longs) was the correct directional posture for that tape.
- (h10 outcomes for 06-23 are near the panel edge and partly unresolved — the aggregate in §5.1 is the resolved evidence.)

## 5.3 Honesty caveats (do not over-read)
1. **Old-system n is small** (HIGH=6, MED=15) and concentrated in the late-May→June `analyses/` window, which includes the June semi selloff. But these are the system's **own** outputs resolved on the **same** truth set; the sign and magnitude are stark and corroborate the audit.
2. **S1's edge is right-skew with a negative median** — most individual shorts slightly lose; the +0.81% mean and +9.5pp excess-hit come from the laggard tail that keeps falling (George-Hwang loser continuation). This is a *basket* edge, not a per-name coin-flip; size and diversify accordingly. The 06-23 cohort is also heavily **China-correlated** → the risk-sizer's correlation-cluster gate (corr≥0.70 = one position) is load-bearing here.
3. **Gross, pre-cost, single 3.5-month window**, and the A/B1/B2 regimes are sub-windows of one episode (P3 §3.2). This validates the *design logic* (stop sizing into crowded beta; fire regime-gated momentum-weakness), not a live P&L guarantee. The momentum-crash regime that inverts S1 is still unsampled.
4. **The strongest claim is the relative one:** the redesign's lanes are positive where the old system's sized tiers were −7% to −8%. Even discounting all the caveats, "would have avoided the 0-for-6 HIGH book" is the robust takeaway.

## 5.4 What this proves for the migration
- The **subtractive** core of the redesign (cut accumulation/multileg/DEX scoring; stop additive confluence) is validated: those were exactly the lines feeding the −8% HIGH book.
- The **additive** core (S1 momentum-weakness as the anchor directional lane) is validated as positive-excess and theory-grounded, with its tail risk explicitly gated.
- The **harness itself ships** as the always-on regression test: re-run `retro_harness.py --all` after any rubric/lane change to confirm the change doesn't reintroduce a negative-excess tier. This is the missing "does the change actually help outcomes" check the old calibration loop could only do retrospectively and by hand.
