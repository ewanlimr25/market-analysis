# Market Scan — 2026-07-02

## Regime & Verdict
- **Regime:** `CHOP / ROTATION (post-NFP)` · vol-state: **VIX 16.15** (−2.7% d, **−14.5% wk** — event vol released post-NFP), VVIX 88.8 (low). QQQ **iv_rank 73** vs SPY **iv_rank 17** = tech-specific IV stress even as index vol collapses · breadth **split: 61% price-green (broad) but 35% bullish *flow* (defensive positioning)** · SPY above 20/50-SMA (structural uptrend), ret10 **+0.52%** (CHOP) · `directional_tradable = TRUE (gate OPEN)` · `s1_standdown = FALSE`
- **Bottom line:** **No directional entry sized today — but the posture is upgraded from yesterday's hard stand-down.** The regime *gate* opened (s1_standdown cleared; the blocking NFP binary has now printed with VIX crushed), yet the *tape* blocks entry: a one-day-old rotation on a CHOP tape into a **3-day holiday gap** (NYSE closed Fri 07-03) with holiday-thin liquidity. The corroborated **rotation out of mega-tech into defensive/value** is pre-registered as **Monday 2026-07-06's MOM_LONG candidate**, sized only on trend confirmation.

**Regime is live-Yahoo authoritative** (truth-set parquet stale at 06-26 → `retro_harness --date` falls back to a stale regime and is NOT used). The key day-over-day change: `s1_standdown` **flipped FALSE**. Yesterday ret5 was +1.71% (> the 1.5% floor, dd15 −3.32%) → the momentum-crash/V-rebound guard fired. Today the thrust **decayed**: ret5 **+1.427%** (below the 1.5% floor), dd15 −1.62% (above −2%) → *both* stand-down conditions fail. QQQ round-tripped almost its entire 06-29/30 V-rebound (736.40 → 712.60), unwinding the "junk-rally" shape. Per the harness's own 58-day history, s1_standdown fires only **6/58 days** — FALSE is the normal state; yesterday was the rare exception, and we've reverted.

## Directional Book (excess-scored)
*Empty for ENTRY. Every row below is WATCH / ADVISORY — the gate is open but the calendar (3-day holiday gap) and the tape (CHOP, tail-lane, defensive flow) block sizing. This is the correct output.*

| Ticker | Lane | Dir | Horizon | validated_excess (58d) | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| VRTX | MOM_LONG | long | h10 | +2.35% (tail-driven, hit 0.50<0.59) | 0.45 | **watch** | rotation reverses / tech V-bounces Mon | healthcare leader near 52w-high; **basket rep**, never per-name; sector **inflow** |
| ALL | MOM_LONG | long | h10 | +2.35% (tail-driven) | 0.45 | **watch** | loses breakout / risk-off | insurer leader; same MOM_LONG basket (Financials/Healthcare/Industrials); noted, not summed |
| OLED | MOM_SHORT | short | h10 | +0.81% / +9.5pp hit | 0.25 | **watch** | 61% broad-green tape firms laggards | lane un-gated (s1_standdown FALSE) BUT shorting a laggard into broad-green + VIX-crush = fighting breadth; NOT a tech-rotation name |
| CG | OI_FADE | short | h10 | +0.88% / +20.5pp hit | 0.10 | **skip** | — | **4.24× / 0.74 rel-build (most extreme)** BUT M&A-speculation near 52w-low → **DO NOT fade a takeover** (unchanged from 07-01) |
| NVDA | OI_FADE | short | h10 | +0.88% (lane prior) | 0.20 | **watch** | insider buying / AI catalyst | mega-tech cluster = **QQQ-beta trap** (rel-build 0.007; hist mega-heavy-day excess −0.43%); only idiosyncratic sliver, not sized |
| BKNG | S2_dp_revert | long | h5 | +0.47% | 0.40 | **watch** | concentration not repeated / news | ADVISORY; DP buy-heavy 97.3% (repeat) — below sizing bar |
| JXN | S4_pcr_fade | long | h5 | +0.71% | 0.35 | **watch** | put crowd informed | ADVISORY; cleanest liquid high-PCR (insurer, PCR 85) |

**Why nothing sizes today (the gate is open — this is a calendar/tape call, not a stand-down):**
- **MOM_LONG defensive-leadership basket — the real candidate, wrong day to enter.** This is the cleanest expression of a rotation corroborated **four independent ways**: (1) QQQ −1.73% / dd15 −4.22% vs SPY flat vs IWM firm (ret10 +2.66%); (2) uw sector flow **Technology −$590M OUT**, Healthcare +$22M / Industrials +$14M IN; (3) the MOM_LONG scan itself is Healthcare/biotech (MRNA/PTGX/VRTX/IBB/ILMN/DVA) + insurers (AXS/ALL/CB/CINF/KIE) near 52w-highs; (4) broad 61% price breadth. **But** the lane is **tail-driven** (mean +2.35% from a few winners; hit 0.50 < 0.59 base, median −0.0007) and needs a **trending, broad-participation** tape — today is CHOP (ret10 +0.52%), uw is TRANSITIONAL/half-size, and *flow* breadth is defensive (35% bullish). You do not chase a **one-day-old** rotation on a tail-lane into a **3-day holiday gap**. Pre-register; size Monday on trend confirmation.
- **MOM_SHORT — un-gated but no clean expression.** s1_standdown FALSE turns the short leg back on, but its near-52w-low candidates (OLED/TU/MAT/XE) are idiosyncratic laggards, **not** the mega-tech rotation names, and shorting laggards into a 61%-green, VIX-crushed tape fights the broadening. The tech *outflow* is in names near their **highs** (NVDA/MSFT…), which only OI_FADE would short — and that's the beta trap.
- **OI_FADE — beta trap again.** Raw `oi_net_5d` is entirely mega-tech + ETFs (NVDA/MSFT/AMZN/AAPL/META/GOOGL, rel-build 0.007–0.027× their own base) = a QQQ-beta short (hist −0.43% on mega-heavy days). The only **extreme relative** build is **CG (0.74×)** — the same M&A-takeover name near a 52w-low that is a **do-not-fade**. No sizeable idiosyncratic OI short exists today.

## Vol Book (non-directional)
**STAND ASIDE — no delta-neutral edge clears net-of-cost through the holiday.**
- **0DTE-VRP:** no session tomorrow (**NYSE closed Fri 07-03**); premium sold today bleeds theta over a closed Friday + weekend, and MMs mark holiday vol down. Next 0DTE opportunity **Mon 07-06**.
- **Earnings IV-crush:** the fuel is **Q2 season start 07-15/16** — TSM (iv_rank 100), ASML (100), NFLX (93), JNJ (79), ABT (96), CTAS (92) — but that's **~2 weeks out**, too early to sell (you'd hold the vol-short at risk for 10 sessions before the crush). Near names are below the net-of-cost bar: PENG (07-07, small-cap 20%+ gap), AZZ (07-08), PEP (07-09, iv_rank 81 but tiny implied move). **Pre-register the 07-15/16 slate** to work from Monday/mid-month.
- **Long vol:** off-mandate and penalized by long-weekend theta (closed Fri + weekend decay) — cheap IV still bleeds.

## Watch / Stood-down
- **MOM_LONG rotation basket (PRIMARY Monday candidate)** — Healthcare/biotech (MRNA, PTGX, VRTX, IBB, ILMN, DVA) + insurers (AXS, ALL, CB, CINF, KIE) + industrials near 52w-highs, in the sectors taking inflow. Size Monday 07-06 **only if** the rotation persists on a trending (not choppy) tape; basket-only, half-cap ceiling, never per-name conviction.
- **CG** — most extreme relative call-OI build (0.74×) but M&A-speculation near 52w-low → do NOT fade; needs a confirmed no-deal news gate.
- **NVDA (standalone)** — largest absolute call-builder, idiosyncratic froth + insider MSPR −100; only ever as an *isolated* defined-risk long-put sliver, never inside the mega-cap cluster.
- **China/metals OI sleeve {KWEB, BABA, EWZ, SLV, GLD, IBIT}** — large absolute OI build but tiny relative build = ETF/beta, not a name signal; watch, unsized.
- **MOM_SHORT laggards {OLED, TU, MAT, XE, RAM}** — un-gated but fighting breadth; watch only. (T-bill/TIPS ETFs SHV/JPST/SHY/VGSH etc. are 52w-low *artifacts*, excluded.)
- **S2 advisory** — BKNG (buy 97%), plus sell-heavy SNOW/ACN/TD/MCHP/PEG/PLD. **S4 advisory** — JXN/THG (insurers), BIRK, CHDN. All below the sizing bar.

## Risk
- **Dominant risk is the 3-day holiday gap, not signal.** NYSE **closed Fri 07-03**; anything entered at today's close holds through a closed Friday + weekend into Monday 07-06 on holiday-thinned liquidity (poor fills, wider gaps). NFP is now *behind* us (resolved this morning, VIX crushed) — so the gap is un-catalysed, but still un-manageable for 3 days. CPI 07-14 sits at/just past the h10 edge.
- **Rotation is one day old.** QQQ is oversold on the day (−1.73%, iv_rank 73); a Monday mean-reversion bounce in mega-tech would unwind the "long defensives / short tech" thesis. Confirmation (a second rotation day, trend) is the trigger, not today's single print.
- **Breadth is split** — broad price participation (61% green) but defensive options flow (35% bullish, bearish flow dominant). A tail-driven MOM_LONG wants participation *and* chasing; it has the first, not the second.
- **No additive confluence.** The four corroborating reads of the rotation (price dispersion + sector flow + MOM_LONG composition + breadth) are **noted as evidence-type diversification, never summed** into a size. The book sizes on one lane's measured excess × regime-fit or it does not size.
- **Discipline:** enter nothing directional into the holiday gap. When the MOM_LONG basket is taken (earliest Mon 07-06, on trend confirmation) it is **basket-only, half-cap ceiling**, defined-risk where possible (VIX 16 makes owning convexity cheap). Re-run the full book **Mon 2026-07-06** on live data.

---
*Method note: UW panel export for 2026-07-02 is fresh across all five groups (post-NFP EOD). Regime computed live from Yahoo SPY chart API (path-aware) replicating `retro_harness.classify_regime` exactly — s1_standdown FALSE confirmed at the 1.5% ret5 boundary. All lane signals computed live against the 07-02 panel (`oi_net_5d` recomputed from the OI-changes panel over the last 5 sessions since `features.parquet` is stale at 06-26; relative-build normalization applied to avoid the mega-cap beta trap). Regression gate `retro_harness.py --all` re-run: **GREEN**, no lane negative-excess (MOM_LONG +2.35%, MOM_SHORT +0.81%, OI_FADE +0.88%, S2 +0.47%, S4 +0.71%; 58-day panel). No lane/threshold changed this run.*
