# Weekly Review — 2026-W27 (Mon 2026-06-29 → Thu 2026-07-02, holiday-shortened)

> THREE layers, never blended. Layer 1 = diary (0 signal). Layer 2 = validated momentum/OI-fade lanes (scored in excess). Layer 3 = weekly technicals (**PRE-REGISTERED, 0 points, never sized**). Fri 07-03 = NYSE holiday (Independence Day observed); last trading day Thu 07-02. Truth-set parquet is stale at 2026-06-26 → all W27 bars built path-aware from the live Yahoo chart API.

## 1. The Week in Pictures (DIARY — documentation, 0 signal)
| Sym | O | H | L | C | w_ret | close_pos | body | structure vs prior |
|---|---|---|---|---|---|---|---|---|
| SPY | 736.53 | 751.31 | 732.09 | 744.78 | **+2.17%** | 0.66 | 0.43 | **bullish reversal** of W26; marginal higher-high, closed upper-half |
| QQQ | 713.99 | 737.62 | 705.17 | 712.60 | **+0.86%** | 0.23 | 0.04 | **inside-week doji**; +4.2% Mon-Tue → **reversed −3.2%**, closed near lows — *bounce failed* |
| IWM | 298.11 | 302.72 | 294.68 | 297.58 | **−0.75%** | 0.36 | 0.07 | marginal higher-high then **faded** — small-cap leadership stalled |

- **The story — a recovery week that mega-tech did *not* lead.** SPY reclaimed ~63% of W26's selloff (**+2.17%**), but it **outperformed both QQQ (+0.86%) and IWM (−0.75%)**. That ordering is the whole tell: when the cap-weighted index beats both its tech-heavy *and* its small-cap cousins, the gains came from **large-cap ex-tech** — the defensive/value rotation. QQQ round-tripped (rallied +4.2% Mon-Tue to 737.62, then a **failed rally** −3.2% Wed-Thu back to 712.60, closing near its lows with a 23.6-pt upper wick, an **inside-week doji**). IWM poked a marginal new high Wed then faded red. Leadership handed off from small-caps (the W26 rotation winner) to **large-cap defensives** (Healthcare / Financials / Industrials).
- **Catalyst anchored — June NFP, Thu 2026-07-02** (holiday-shifted off the usual first Friday):
  - **+57K vs +115K consensus (a MISS).** Unemployment ticked to **4.2%** but on a *falling* participation rate (61.5%, lowest since Mar-2021); Apr/May revised **−74K** combined; leisure/hospitality **−61K**.
  - **Reaction:** a soft print **quieted the rate-*hike* conversation** the hawkish Warsh Fed had opened (2Y −3.5 bp to 4.13%), and **VIX was crushed to 16.15 (−12% on the week)**. But the relief **faded intraday**: SPY −0.13%, **QQQ −1.73%** on NFP day. The week's gains were banked **Mon-Tue, pre-print** — NFP itself was *sell-the-relief* in tech, not a fresh leg up.
- **Regime trajectory:** relief-bounce risk-on into the week (Mon SPY +1.65%, VIX 18.41→16.45) → **CHOP / ROTATION** by Thu (ret10 +0.52%, above 20/50-SMA, uw regime *TRANSITIONAL / half-size*). Vol bled lower every session (VIX **18.41 → 16.15**).
- **Notable flow (diary only):** trailing ~2wk net **call**-OI build, ranked *relative* (build ÷ 30d-avg, per the beta-trap rule): **CG 3.77×** (takeover-driven, not fadeable), TEL 2.53× (iv_rank 92), **RSI 2.31× / CGNX 2.23× — near 52w-*highs*, i.e. uptrend build, not a fade**, FOXA 1.98× (iv_rank 100). Mega-cap tech build persists but is a QQQ-beta trap. Single-name: **MSTR squeezed +22.4%** (crypto-beta risk-on) — a live drag on last week's short book (§4).

## 2. Validated Weekly Setups (SCORED — excess) — **NO SIZED CALL THIS WEEK**
A "no scored setup" week is a normal, correct output. Nothing sizes, for reasons that all point the same way:

| Ticker | Lane | Dir | H | validated_excess | tier | size | why not sized |
|---|---|---|---|---|---|---|---|
| VRTX | MOM_LONG | long | 10 | +0.0235 | WATCH | watch | tail-driven; needs a **trending** tape — CHOP (ret10 +0.52%) fails it; basket-only |
| ALL | MOM_LONG | long | 10 | +0.0235 | WATCH | watch | insurer leg of the same defensive basket → collapses to ONE position; not sized |
| OLED | MOM_SHORT | short | 10 | +0.0081 | WATCH | watch | shorting a laggard into a **VIX-crushed risk-on** tape = fighting the tape (see §4 squeezes) |
| CG | OI_FADE | short | 10 | +0.0088 | DROP | skip | top relative-build (3.77×) but **takeover-driven** — deal positioning, not fadeable froth |

- **Momentum** (both legs): the regime is CHOP, not trend. MOM_LONG is tail-driven and needs a broad trending tape to pay; MOM_SHORT's candidates are idiosyncratic near-52w-low laggards, and shorting weakness into a 61%-green, VIX-crushed week is exactly the momentum-rebound setup that **squeezed CME and MSTR** out of last week's book (§4).
- **OI-fade:** the top *relative*-build name is CG (3.77×) but it's a takeover build (skip). The rest of the leaderboard is either near-52w-**high** momentum (RSI 0.99, CGNX 0.88 — call-build *confirms* an uptrend, it doesn't fade one) or earnings/IV-elevated. Mega-cap tech build remains a **QQQ-beta trap**. No clean beta-neutral, non-deal, idiosyncratic fade with a fundamentals confirm → **nothing scored**.
- **Vol book:** non-directional; no weekend 0DTE; Q2 earnings IV-crush fuel (TSM/ASML/NFLX 07-15/16, iv_rank 90-100) is ~2 weeks out — pre-registered, too early to sell.

## 3. Weekly Technicals — PRE-REGISTERED (documented, 0 points, NOT sized)
| Feature | This week | Would signal | Status | Pre-reg bar |
|---|---|---|---|---|
| SPY bullish reversal / higher-high | +2.17%, HH 751.31, close_pos 0.66, still < 06-15 high 756.68 | recovery long **if** it reclaims 756.68 | **PRE-REGISTERED** | PR-WT (≥2yr / ≥30 wk / cross-regime / BH) |
| QQQ inside-week doji, **failed rally** | inside_week, body 0.04, close_pos 0.23, 23.6-pt upper wick | mega-tech distribution / down if next wk loses 705.17 | **PRE-REGISTERED** | PR-WT |
| IWM higher-high **fade** | HH 302.72 then −0.75%, close_pos 0.36 | rotation OUT of small-caps → large-cap value | **PRE-REGISTERED** | PR-WT |
| reversal-after-catalyst (soft NFP) | QQQ reversed its Mon-Tue rally down through NFP; SPY flat | 'sell-the-relief' vol-crush fade tell | **PRE-REGISTERED** | PR-WT |

**These earn ZERO conviction and are never sized.** Candlestick evidence is weak-to-null on liquid names (Marshall-Young-Rose 2006) and this panel is ~24 weeks — statistically meaningless for a weekly-pattern claim. They graduate to Layer 2 only by clearing PR-WT on the extended panel; `/calibration-audit` accrues them.

## 4. Carry-forward — last week's (W26) sized book, mid-flight
Entered 06-26 close, marked at 07-02 (~4 of 10 sessions; **h10 resolves ~07-10, NOT final**). Excess = short beats SPY when the name underperforms (SPY +2.17% on the window):

| Ticker | Lane | name ret | **excess (mid-flight)** | read |
|---|---|---|---|---|
| MARA | OI_FADE short | −14.72% | **+16.88%** | big win (partly idiosyncratic miner move) |
| NVDA | OI_FADE short | +1.19% | **+0.97%** | small win |
| FXI | MOM_SHORT short | +1.01% | **+1.15%** | small win |
| CME | MOM_SHORT short | +7.06% | **−4.89%** | **loss** — exchange rallied |
| MSTR | MOM_SHORT short | +22.43% | **−20.26%** | **big loss** — crypto-beta squeeze |
| *ABBV (watch, unsized)* | MOM_LONG | +3.05% | *+0.88%* | would-have-won small |

- **The lane split is the lesson.** **OI_FADE is 2-for-2** (NVDA + MARA, avg **+8.9%** excess) — the most-robust lane holding up. **MOM_SHORT is the drag:** FXI won small but **CME and MSTR got squeezed hard** in the recovery/risk-on tape — precisely the momentum-rebound tail the short leg is gated against. Equal-weight the 5-name book and it's ≈ **−1.2%** excess mid-flight, *entirely* from the two MOM_SHORT squeezes; strip them and the book is solidly green.
- **Carries into next week:** watch whether QQQ confirms the failed-bounce (loses 705.17) or the defensive rotation broadens; whether the CME/MSTR squeezes mean-revert before the ~07-10 h10 resolution. All five roll into `/calibration-audit`.

---
*Layer-1 candles + carry-forward built path-aware from the live Yahoo chart API (truth-set parquet stale at 2026-06-26); OI build from the panel `chain-oi-changes-*` (10-file trailing window), ranked relative per the mega-cap beta-trap rule; NFP web-anchored. Envelope: `decision.json` (weekly schema w1.0, validated). W27 outcomes unresolved (live panel edge).*

**Sources:** [CNBC — June 2026 jobs report (+57K, 4.2%)](https://www.cnbc.com/2026/07/02/jobs-report-june-2026-.html) · [BLS Employment Situation — June 2026](https://www.bls.gov/news.release/archives/empsit_07022026.htm) · [Kiplinger — weak June jobs report quiets the rate-hike talk](https://www.kiplinger.com/investing/economy/jobs-report-june-2026-what-to-expect)
