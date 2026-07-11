# Weekly Review — 2026-W28 (Mon 2026-07-06 → Fri 2026-07-10)

> THREE layers, never blended. Layer 1 = diary (0 signal). Layer 2 = validated momentum/OI-fade lanes (scored in excess). Layer 3 = weekly technicals (**PRE-REGISTERED, 0 points, never sized**). Truth-set parquet is stale at 2026-06-26 → all W28 bars + carry-forward built path-aware from the live Yahoo chart API; OI build from the fresh `chain-oi-changes` panel (through 07-10).

## 1. The Week in Pictures (DIARY — documentation, 0 signal)
| Sym | O | H | L | C | w_ret | close_pos | body | structure vs prior |
|---|---|---|---|---|---|---|---|---|
| SPY | 748.74 | 755.42 | 739.51 | 754.95 | **+1.37%** | 0.97 | 0.39 | **new-high breakout**; HH (755.42>751.31) **+** HL (739.51>732.09); closed at 0.97 of range; big lower wick from the Wed flush, fully reclaimed |
| QQQ | 719.93 | 726.39 | 700.91 | 725.51 | **+1.81%** | 0.97 | 0.22 | **weekly hammer / bear-trap**; undercut prior-wk low (700.91<705.17) then V-recovered to close **best of the three**; lw 0.75; mega-tech leadership reclaimed |
| IWM | 297.75 | 300.41 | 290.68 | 295.99 | **−0.53%** | 0.55 | 0.18 | lower-high **+** lower-low; **only major to close red** — small-caps the laggard a 2nd week |

- **The story — a risk-on grind to new highs, and mega-tech took back the wheel.** The leadership ordering flipped clean out of W27: last week was **SPY > QQQ > IWM** (defensive/value rotation); this week is **QQQ (+1.81%) > SPY (+1.37%) > IWM (−0.53%)** — growth back on top, small-caps still lagging. SPY printed a **new closing high (754.95)**, a hair under the 06-15 high 756.68, with textbook HH+HL breakout structure. QQQ is the tell: it **undercut the prior week's low intraday (700.91 < 705.17) then reversed hard** to close +1.81% — a weekly hammer / bear-trap that reclaimed mega-tech leadership after it lagged in W27. IWM couldn't confirm (lower-high, lower-low, red).
- **Catalyst anchored — June FOMC minutes, Wed 2026-07-08** (Warsh's first meeting):
  - Funds held **3.50–3.75%** unanimously, but the minutes showed a deep **9-8 hawkish/dovish split** — *a few officials weighed HIKES* ("nine hawkish dots"; Warsh's deliberate silence). Futures now price funds toward **~4% by year-end** despite the soft June NFP.
  - **Reaction: shrugged off.** Muted on the day (QQQ dipped to its weekly low 700.91, VIX spiked to 18.91 intraday), but the hawkish tone **did not hold** — risk-on reasserted Thu-Fri to new highs, **VIX crushed to 15.03** (low 14.96, the lowest in the sequence). A tape that overrides a hawkish macro print is itself a risk-on structural signal (§3).
- **Regime trajectory:** TRENDING-up, low-vol, risk-on — a **regime FLIP from W27's CHOP/ROTATION**. Mon new-high push (SPY 751.28, VIX 15.57) → shallow Wed flush on the minutes → sharp Thu-Fri reassertion to SPY 754.95, VIX 15.03. ret10 now positive and rising (vs +0.52% last week). Momentum-rebound tail is live *against* shorts.
- **Sector leadership — a FULL REVERSAL of W27's defensive rotation.** Leaders (07-02→07-10): **Energy +3.49%, Semis +3.16%, Tech +2.87%, Comm +1.86%.** Laggards: **Materials −2.15%, Health −1.77%, Industrials −1.08%, Staples −1.02%, Utilities −0.76%.** W27's defensive winners are this week's laggards — which is exactly why the W27 defensive-basket watch names would have lost (ABBV −5.64%, §4).
- **Notable flow (diary only):** call-OI build normalized by `avg_30_day_call_oi` with the pinned gates. The naive leaderboard all *excludes*: **TECH 2.69×** (confirmed M&A target — Merck KGaA $11.3B, 06-26), **RSI 1.72×** (near-52w-high = uptrend build), **TEL / SHOO / SLM / ENSG / CGNX** (earnings inside the 2–4wk hold), **CBRS** (IPO 05-14, <60td listed), **UNM** ($3.8B Fortitude Re deal 07-06). **Honesty correction:** last week's diary flagged **CG at 3.77×** — a persistence check shows **97% of that build landed in a single day** (two ~100k OTM call blocks) = a lumpy institutional hedge, not crowd accretion; the naive 2wk-sum overstated it. The **one** clean, persistent, beta-neutral, non-deal fade is **MAT** (§2). Mega-cap tech call-build persists = QQQ-beta trap; crypto-beta bid again (BTDR/MSTR).

## 2. Validated Weekly Setups (SCORED — excess) — **ONE SCORED SHORT: MAT (starter/half-cap)**
| Ticker | Lane | Dir | H | validated_excess | regime_fit | tier | size | note |
|---|---|---|---|---|---|---|---|---|
| **MAT** | **OI_FADE** | **short** | 10 | **+0.0088** | 0.50 | **MEDIUM** | **starter** | **the scored call** — see below |
| MOM_LONG basket | MOM_LONG | long | 10 | +0.0235 | 0.55 | WATCH | watch | regime finally favorable, but tail-driven/dilute → basket-only, not sized |
| MOM_SHORT | MOM_SHORT | short | 10 | +0.0081 | 0.10 | STOOD_DOWN | skip | new-high tape = the momentum-rebound tail; stood down |

- **MAT (Mattel) — the one clean OI_FADE short.** Persistent call-OI build **every one of 10 days**, accelerating into 07-09/10, normalized 0.90× `avg_30_day_call_oi`, max single-day share 0.40 (passes the persistence check that killed CG). **Beta-neutral** (toys/consumer-disc, no cluster overlap), not mega-cap-beta, not an ETF/new-listing, not a deal, **not near-high** (pct_52w_range **0.031** — fresh 52w low 07-09). **Fundamentals confirm the short:** Goldman cut MAT **to Sell on 07-09**, the same day it hit a fresh low — i.e. a crowd piling into **bounce-bet calls on a battered name**, the textbook crowded-embedded-leverage fade (hit 0.61 vs 0.41 base, n=640). Entry 07-10 close **$13.33**, liquid (~$65M/day). **Size = starter/half-cap only** (shorting into a new-high VIX-15 tape is the standing headwind; OI_FADE is orthogonal to momentum so the tape is a *haircut*, not a veto). **Earnings 08-04 (~18td) → run to h10 and flatten before the print.**
- **Momentum:** MOM_LONG's regime-fit *improved* (0.45→0.55) — the tape is finally TRENDING-up, the condition this tail-driven lane needs — but the cohort is dilute (480 names, 46% ETFs) with Financials/Healthcare cluster-correlation risk, and the edge is tail-driven (median ~0). **Basket-only, never per-name → WATCH.** Gate to half-cap only if ret10 sustains >+1% for ≥2wk and the cohort tightens. **MOM_SHORT stood down:** new closing highs + VIX 15.03 = the momentum-rebound tail that just squeezed all three W26 shorts (§4).
- **Vol book:** non-directional; the VIX-15.03 crush sets up cheap protection into next week's bank-earnings + June-CPI cluster (pre-registered, W29).

## 3. Weekly Technicals — PRE-REGISTERED (documented, 0 points, NOT sized)
| Feature | This week | Would signal | Status | Pre-reg bar |
|---|---|---|---|---|
| SPY new-high breakout (HH+HL) | +1.37%, HH 755.42, HL 739.51, close_pos 0.97, new close 754.95 (<06-15 high 756.68) | trend-continuation long **if** it clears 756.68 and holds | **PRE-REGISTERED** | PR-WT (≥2yr / ≥30 wk / cross-regime / BH) |
| QQQ weekly hammer / bear-trap | undercut 705.17 to 700.91 then closed +1.81% (best), lw 0.75, close_pos 0.97 | mega-tech leadership reclaimed / failed-breakdown long | **PRE-REGISTERED** | PR-WT |
| IWM lower-high + lower-low (2nd wk) | LH 300.41, LL 290.68, only major red (−0.53%) | small-caps failing to confirm = narrow/large-cap-led advance | **PRE-REGISTERED** | PR-WT |
| reversal-after-catalyst (hawkish FOMC shrugged off) | hawkish 9-8 minutes dipped QQQ + spiked VIX 18.91 Wed → fully reclaimed to new highs, VIX 15.03 | 'buy-the-hawkish-dip' vol-crush regime-strength tell | **PRE-REGISTERED** | PR-WT |

**These earn ZERO conviction and are never sized.** Candlestick evidence is weak-to-null on liquid names (Marshall-Young-Rose 2006) and this panel is ~25 weeks — statistically meaningless for a weekly-pattern claim. They graduate to Layer 2 only by clearing PR-WT on the extended panel; `/calibration-audit` accrues them.

## 4. Carry-forward — W26 sized book, RESOLVED at h10 (marked 07-10; final resolves 07-13)
Entered 06-26 close, marked 07-10 close (h9, effectively final). SPY **+3.56%** on the window. Excess: short beats SPY when the name underperforms.

| Ticker | Lane | name ret | **excess (final)** | read |
|---|---|---|---|---|
| MARA | OI_FADE short | −13.34% | **+16.90%** | **big win** (partly idiosyncratic miner move) |
| NVDA | OI_FADE short | +9.57% | **−6.01%** | **loss** — flipped from a mid-flight small win; the mega-tech V-recovery hit it |
| FXI | MOM_SHORT short | +5.98% | **−2.42%** | loss — China/beta rallied |
| CME | MOM_SHORT short | +8.72% | **−5.16%** | loss — exchange squeeze continued |
| MSTR | MOM_SHORT short | +14.98% | **−11.42%** | loss — crypto-beta squeeze |
| *ABBV (watch, unsized)* | MOM_LONG | −2.08% | *−5.64%* | would-have-**lost** — the defensive rotation reversed |

- **The lane split held to the end, with a sharpening lesson.** **MOM_SHORT went 0-for-3** (avg **−6.3%** excess) — shorting near-52w-low laggards into a VIX-crushed, new-high tape is the momentum-rebound tail the leg is gated against, confirmed the hard way. **OI_FADE finished +5.4% avg but 1-for-2:** MARA a huge win, **but NVDA flipped from a mid-flight win to a −6.0% loss on this week's mega-tech V-recovery** — a live reminder that even in the most-robust lane, a **mega-cap-beta** name (NVDA) is a QQQ-beta trap. Equal-weight the 5-name book ≈ **−1.6%** excess, *entirely* from the MOM_SHORT squeezes; strip them and OI_FADE is solidly green.
- **The takeaway sizes this week's MAT call:** OI_FADE works when the name is **idiosyncratic and beta-neutral** (MARA idiosyncratic-win; NVDA beta-loss). MAT is toys, near its own 52w low on a downgrade — the beta-neutral kind. **W27 had no sized calls.** All W26 names roll into `/calibration-audit` (final at 07-13).

---
*Layer-1 candles + carry-forward built path-aware from the live Yahoo chart API (truth-set parquet stale at 2026-06-26); OI build from the fresh `chain-oi-changes` panel (10-file trailing window, 06-26→07-10), normalized by `avg_30_day_call_oi` with persistence + Common-Stock + deal/earnings/near-high/listing-age gates; FOMC minutes web-anchored. Envelope: `decision.json` (weekly schema w1.0, validated). W28 outcomes unresolved (live panel edge).*
