# 70 — Exhaustive factor hunt across ALL 5 sources (Phase 7)

_Answering "have you mined ALL the data for edge?" — honestly, Phase 2 had not. Phase 2 graded the existing fleet's ~45 signals; it did not turn the panel's unused columns, multi-day derivations, or a proper cross-sectional factor model loose on the data. This phase does. Method: a unified per-(ticker,date) feature table across all 5 sources (`data/features.parquet`, 103k rows, 55 factors), then a standard **cross-sectional rank-IC + decile long-short** sweep vs forward EXCESS, regime-stratified and significance-tested (`data/build_features.py`, `factor_scan.py`)._

## 7.0 Method & honesty notes
- **rank-IC** = per-day Spearman(factor, forward-excess) averaged over days; **t-stat** = mean-IC/(σ_IC/√days). Excess nets SPY, so a nonzero IC is alpha, not beta. **Decile spread** = D10−D1 mean excess.
- **Cross-section ≈ 100–150 priced names/day** (the join restricts to the 783-name priced funnel). Multiple testing: 32 factors × 4 horizons = 128 tests → I require **|t| ≥ 3** (clears Bonferroni) **+ a regime-stable sign + a mechanism** before trusting.
- **Regime caveat:** B2 (the final ~9 days) is `na` at h≥10 (forward windows fall off the panel), so for long-horizon factors only A & B1 are resolvable — "2-regime-stable," not 3. Only h3/h5 factors get a true 3-regime read.

## 7.1 The headline: flow/premium factors are beta — now confirmed across the WHOLE column set
Every raw options-flow / premium / smart-money factor has **near-zero IC** (|t| < 2): `netprem` (t=−0.5),
`netprem_mcap` (−0.7), `bull_bear_skew` (−0.6), `hc_smart_dir` (−1.6), `hc_smart_5d` (−2.2), `dp_buy_skew`
(−1.7), `dp_oneside` (+1.6), `vol_accel` (+0.9), `netprem_5d` (−0.9). **This re-confirms the Phase-2/3
conclusion on a far wider factor set than the 45 fleet signals: aggregated options flow does not
cross-sectionally predict forward excess.** The data has now been asked the open-ended question and gives
the same answer.

## 7.2 What the hunt FOUND (the factors that clear |t|≥3 + stability + mechanism)
| Factor | Best h | IC | t | D10−D1 | Regime IC (A/B1) | Status / mechanism |
|---|---|---|---|---|---|---|
| **`pct_52w_range`** (position in 52-wk range) | 21 | +0.111 | **+6.8** | **+7.2%** | +0.12 / +0.11 | **STRENGTHENS S1 into a full momentum lane.** Monotone decile gradient (below). George-Hwang anchoring momentum. |
| **`oi_net_5d`** (5-day net call−put OI build) | 10 | −0.092 | **−7.1** | −3.2% | −0.10 / −0.09 | **NEW & orthogonal** (corr −0.17 w/ momentum): persistent call-OI building → **under**performance. A *fade-the-OI-pump* signal — consistent with "flow is contrarian." |
| **`ivrank_chg_5d`** (5-day Δ IV-rank) | 3 | +0.053 | **+5.2** | +0.9% | +0.09/+0.05 (**B2 +0.06**) | **NEW & orthogonal** (corr +0.02): rising IV-rank → short-horizon outperformance. **The only factor sign-stable across ALL 3 regimes.** |
| `iv30d` ≈ `implied_move_perc` ≈ `volatility` (collinear, corr 0.66) | 21 | +0.14 | +4.8 | +13.6% | **+0.29 / +0.07** | **LOW confidence — regime-A-concentrated.** High-IV names outperform at h21, but the effect is ~4× larger in the March selloff than the grind-up → likely **beaten-down-rebound beta**, not durable alpha. |
| `vrp_name` (iv30d − realized σ) | 21 | −0.140 | −5.1 | −13.7% | −0.26 / −0.08 | LOW confidence — same A-concentration; rich-IV names underperform, but A-loaded. |

### The 52-week-range decile gradient (h21) — the cleanest structure in the whole study
```
D1 (near 52w-low)  -3.98%   <- the S1 short leg
D2                 -0.63%
D3..D6             +1.8% .. +2.3%  .. +1.1%
D7                 +4.83%
D8                 +4.74%
D9                 +5.04%   <- the near-high LONG leg (the CLEANER half)
D10 (extreme high) +3.20%   <- very top gives a little back (classic momentum)
```
**This corrects the Phase-4 design.** I had built the momentum lane as a **short-only** near-52w-low signal
(S1). The factor hunt shows the **long/near-high leg is the stronger, cleaner half** (+4.8–5.0% at D7–D9 vs
−4.0% at D1) — exactly what George-Hwang predicts (`RESEARCH/30 §3.1`: the near-high leg is the reliable one,
the near-low short is the noisier half). The redesign's momentum lane should be the **full continuous
`pct_52w_range` factor: long the near-highs, short the near-lows** — not short-only.

## 7.3 What's genuinely new vs the original fleet
- **`oi_net_5d` as a FADE** is new and the opposite of the old `+1 multi-day OI build` line (which scored OI
  building as *bullish*). The data says persistent call-OI building **predicts underperformance** (t=−7.1,
  orthogonal to momentum). The old rubric had the sign backwards.
- **`ivrank_chg_5d`** (IV-rank momentum) is new, orthogonal, and uniquely 3-regime-stable — a short-horizon
  "vol waking up" signal the fleet never computed.
- The **high-IV-name h21 cluster** (`iv30d`/`implied_move`/`vrp_name`) is real in-sample but **regime-A
  beta** — I flag it LOW-confidence and do **not** propose a lane (it would have lost in any tape that
  didn't rebound off a selloff).

## 7.4 Design impact (updates DESIGN/40)
1. **Upgrade the momentum lane** from S1-short-only to the **full `pct_52w_range` factor (long near-high +
   short near-low)** — the long leg is the better half (the single biggest improvement this phase yields).
2. **Add `oi_net_5d` as a fade/gate** — a name with heavy 5-day call-OI building is a *caution on longs /
   confirm on shorts*, not a bullish tell. (Pre-register an orthogonality-controlled re-test.)
3. **Add `ivrank_chg_5d` as a short-horizon (h3) tilt** — provisional; the only 3-regime-stable factor.
4. **Do NOT add** the high-IV h21 cluster — labeled regime-A beta, low confidence.
5. The flow/premium factors stay cut — now re-confirmed on the full column set, strengthening D2.

## 7.5 Honest limits of this hunt
- Still **54 days / 2 resolvable regimes** for the h21 factors; t-stats are high but the independent-period
  count is low. 52w-range & oi_net are **PROVISIONAL-STRONG** (theory + |t|≥7 + A&B1-stable); ivrank_chg is
  **PROVISIONAL** (3-regime-stable but |t|=5, novel mechanism).
- Cross-section is the **783-name priced funnel**, not the full 2,357-name liquid book (pricing all of them
  is the cheap next step to tighten the IC).
- I did **not** exhaustively test all pairwise **conjunctions** (e.g. momentum ∧ oi_net_5d fade) — the
  orthogonality (corr −0.17) says a combination *should* add; that is a pre-registered next test (PR-6).
- These remain **cross-sectional** edges (rank within day); turning a +7%/21d decile spread into a tradable
  sleeve needs turnover/cost modeling (not done).

## 7.5b Harness re-validation of the new lanes (folded into artifacts)
Adding the factor-zoo lanes to `retro_harness.py` and resolving realized excess across all 54 days:
| Lane | n | mean_exc | hit | base | hit−base | median | honest profile |
|---|---|---|---|---|---|---|---|
| **OI_FADE** (short top `oi_net_5d`) | 640 | +0.0088 | 0.61 | 0.41 | **+0.205** | **+0.0207** | **the standout** — high hit AND positive median (robust, not tail-driven). Confirms the t=−7.1. |
| MOM_SHORT (near-52w-low) | 273 | +0.0081 | 0.48 | 0.38 | +0.095 | −0.0038 | the higher-hit-consistency leg |
| MOM_LONG (near-52w-high) | 344 | +0.0235 | 0.50 | 0.59 | −0.093 | −0.0007 | **high MEAN but right-skew / tail-driven** — a few momentum winners carry it; median ≈ 0, hit below the (high) long base. NOT a clean hit-rate edge at h10. |

**Correction to my own §7.2 read:** the near-high long leg is *not* unambiguously "the cleaner half." At the
tradable h10 it is **high-mean but tail-dependent** (negative hit−base, ~0 median) — you capture it only as a
diversified basket, never per-name. The factor-scan's clean monotone gradient was at **h21**; it decays toward
a tail-driven profile at h10. The **OI_FADE** lane is the genuinely robust new directional edge.

## 7.6 Net answer to "did you mine all the data?"
Now, yes — across all 5 sources, the unused columns, multi-day derivations, and a proper cross-sectional
model. The result: **the flow data is beta (reconfirmed broadly); the durable structure is price-momentum
(52-week-range, both legs) plus two new orthogonal vol/OI factors.** The microstructure panel's edge is not
in *who is trading* (flow) but in *where the price sits* (momentum) and *how vol is changing* — which is the
same lesson Phase 2/3 reached, now established on the whole dataset rather than the fleet's 45 signals.
