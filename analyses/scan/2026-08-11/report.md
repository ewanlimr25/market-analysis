# Market Scan — 2026-08-11

## Regime & Verdict

- **Regime: UPTREND** · ret5 **−0.100%** · ret10 **+4.010%** · dd15 **−1.540%** (`scripts/regime_check.py`, authoritative)
- **Vol-state:** VIX 15.28 (LOW tercile), normal contango (VIX3M 18.91). **SPY dealer gamma SHORT** — spot 770.60 vs zero-gamma flip 789.87, **2.44% below** (last night: pinned *at* the flip). QQQ spot 718.26 vs flip 769.03, 6.6% below, short gamma — **both sources now agree**, the first agreement on the short side this stretch.
- **Breadth:** price breadth 54.67% green vs options-flow bullish **36.1%** — an **18.6pt gap that persisted even as the tape strengthened**. Rotation OUT of Technology + both Consumer sectors, INTO Energy / Financials / Industrials (Tech outflow now two-session-persistent).
- `directional_tradable` = **TRUE** · `s1_standdown` = **FALSE**
- **Bottom line: no new starters. Zero directional calls sized for a TENTH consecutive session (07-29 → 08-11); the book stays FLAT for a SEVENTH.** Two OI_FADE shorts reached Phase D and both landed at WATCH on two *independently sufficient* gates. Vol book empty.

### What actually changed tonight

The crash/rebound guard expired on 08-10, and tonight is the session that shows what its lifting meant: **the thrust has fully flattened.** ret5 has decayed +5.53% (08-05 peak) → +3.51% → +2.03% (08-10) → **−0.10%** tonight. The UPTREND label is now trailing a decayed number rather than describing live acceleration — ret10 (+4.01%) is carrying the label on its own.

Simultaneously SPY dealer gamma went from *pinned at the flip* to **2.44% clear below it**, and QQQ's two gamma sources resolved their 08-10 disagreement — to SHORT, not to a tradeable long-gamma read. Aggregate gamma sign (wing-width) and spot-vs-flip (regime/sell decision) are reported separately below and were not merged.

Read together — decayed thrust, persistent flow/price breadth divergence, short gamma on both index books, and three consecutive Tier-1 macro prints — this is a **transitional tape wearing an uptrend label**, not a confidently in-regime one.

---

## Directional Book (excess-scored)

**EMPTY — no name sized.** Both Phase D candidates are shown for the record at their final tier.

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| COO | OI_FADE | short | h10 | +0.59% mean / +0.95% med (n=1087, pooled) | 0.42 | **watch** | close > ~$80.50 (recent-high reclaim / short-covering), or any fact reversing the UBS Neutral $75 PT | liq PASS · earnings PASS (09-09) · catalyst no-cat · cluster PASS · **fundamentals CAUTION −1** · **event-risk −1** |
| NRG | OI_FADE | short | h10 | +0.59% mean / +0.95% med (n=1087, pooled) | 0.35 | **watch** | close > **$124.71** (post-crash swing high, 08-05 intraday); gap-fill toward pre-print $138.47 = hard invalidation; LS Power / Texas BYOP confirmation = hard invalidation | liq PASS · earnings PASS (11-05) · catalyst **LIVE_BUILD both boundaries** · cluster PASS · **fundamentals CAUTION −1** · **event-risk −1** |

### Tier arithmetic — why nothing sized

OI_FADE's pooled prior (**+0.59% mean**) sits in the **MEDIUM (+0.3–1%) starter band** on its own. Two separate gates each apply −1 tier, and **either one alone** takes starter → WATCH:

1. **Fundamentals CAUTION** (−1) on both names.
2. **Event risk** (−1): CPI 08-12, PPI 08-13, Advance Retail Sales 08-14 — three Tier-1 prints on **days 1–3** of the h10 window an 08-11 entry opens (closes ~08-26).

This is **overdetermined, not a close call**, and explicitly **not** an additive-confluence downgrade — two independent gates reaching the same floor. Half-cap/no-auto-full never came into play; neither name approached the ≥1% HIGH band.

The out-of-regime half-cap (P0.6) *would* have been applied on tonight's transitional read, but is **non-binding** — the starter band already sits below the half ceiling.

### Per-name notes

**COO — Cooper Companies** ($76.82, Healthcare/medical devices, $150.5M ADV, Common Stock)
Build **accelerated**: rel_build 1.029 → **1.317**, net_5d +4,619 → **+6,113**, persistence 0.659 (organic, <0.85). But **66% of the 5-day build landed in a single session (today, +4,028)**. Per the standing M&A-rumor gate gap, the news tape was checked directly — **nothing COO-specific in the 08-05→08-11 window**; no deal, rumor, or activist catalyst. The spike is positioning, not fundamentals. That is a build-*quality* concern layered on top of the formal gates, not itself a gate.
Fundamentals **CAUTION, explicitly unchanged from 08-10 — no new fact on either side.** Contradicting the short: 4/4 EPS beat streak, insider MSPR +40.33 (net buying), D/E 0.30. Confirming it: EPS growth −42.61% YoY, revenue +6.09%, ~63–65x trailing P/E, UBS Neutral PT **$75, below spot**. Short float 4.30%, days-to-cover 2.96 — low squeeze risk. RSI 67.49.
Worth carrying: COO has closed **higher in 6 of the last 7 sessions** ($72.32 → $76.82, +6.2%) and is ~4.6% below the $80.50 reference. This is a call-OI build *into strength*, on a name approaching overbought.

**NRG — NRG Energy** ($119.79, Utilities/IPP, $383.2M ADV, Common Stock) — **new, no prior adjudication**
Mechanically the **cleaner build of the two**: persistence **0.315** (well-distributed across five sessions) vs COO's 0.659, on 2.5× the liquidity. net_5d +66,359 (call +74,076 / put +7,717), rel_build 0.835.
**Catalyst boundary re-verified by hand.** NRG gapped **−15.5% on its 08-04 Q2 print** ($138.47 → $117.04, 13.8M sh vs ~2.6M normal). The shipped `catalyst_split` `>=` reads 60.4% post-catalyst; **the strict `>` recompute reads 66.3%** — because the print day itself was net **−5,937** (calls *closed* into the print). Excluding it **raises** the share. Both boundaries agree **LIVE_BUILD**: the known print-day defect **strengthens** this name rather than flipping it — the opposite of the EWTX case that killed that name on 08-10. The build is a genuine post-crash dip-buying crowd rebuilding call exposure well past the print.
Fundamentals **CAUTION**. Confirming the short: **second consecutive EPS miss** (Q1 −17.63%, Q2 −13.08%), insiders did **not** buy the dip (3mo MSPR −60.91; July −100, Aug −69.63), leverage **high** (D/E 5.55–9.78). Contradicting it: a dated, post-crash bullish catalyst stack — SeekingAlpha upgrade to Buy (08-06) citing the LS Power acquisition and a new 1.2-GW Texas hyperscaler BYOP project (~$500M incremental annual EBITDA); Scotiabank (08-05) and Evercore ISI (08-05) both reiterate Outperform at **$211 / $195 — roughly 63–76% above spot**. Forward P/E 11.10, PEG 0.69, EPS Next Y +22.42%.
The risk here is a **fundamentals re-rating, not a covering squeeze** (short float 3.06%, days-to-cover 2.12). Since the crash NRG has held a tight **$116.56–$124.71** band, closing mid-band.

---

## Vol Book (non-directional)

**EMPTY — 0DTE-VRP stands aside on both SPY and QQQ**, for cleaner reasons than last night's source conflict.

The pooled headline `net_expectancy` is **positive** (SPY +0.127%/day, QQQ +0.255%/day) — but it **pools all VIX terciles**. Tonight is unambiguously **LOW tercile** (VIX 15.28), and the conditional net-of-cost is **negative for both**:

| | pooled (all terciles) | LOW-tercile gross | **LOW-tercile NET** (−0.1% round-trip) |
|---|---|---|---|
| SPY | +0.127%/day | −0.018%/day | **−0.118%/day** |
| QQQ | +0.255%/day | +0.040%/day | **−0.060%/day** |

Acting on the **conditional**, not the pooled figure. Independently, both books are **dealer-short-gamma** (spot below flip) — a structural stand-aside on its own. QQQ additionally shows front-end backwardation (0DTE IV 1.35× VIX). And CPI/PPI land inside the next two 0DTE sessions — event vol this sleeve's validation sample never priced.

**Earnings IV-crush — ADVISORY ONLY, no backtested harness exists for this stack.** Four candidates in confirmed backwardation: TRMB (08-12, IV-rank 100, ~8.0% implied vs 2.42% typical, ~3.3×, best liquidity) · ALMS (08-12, ~25.0% implied vs 4.44%, ~5.6×, thin OI) · RRGB (08-12, ~15.9%, **no realized-vol cross-check available — unconfirmed**) · BSP (08-13, ~13.5%, liquidity-marginal). All three 08-12 names print **into CPI** — the implied move embeds single-name risk, not a macro-print tape, so wings need sizing well past it. Not sized.

---

## Watch / Stood-down

- **MOM_SHORT — 12 names** (APP, WING, RBA, ONON, VICI, ALHC, ACM, PEG, CMS, GME, ROL, GPI), up from 7 on 08-10. Watch-only, **never sizes** — knowingly negative baseline (−0.0128, n=803), the one recorded exception to "no lane negative-excess". `s1_standdown` is FALSE, so the standing invariant, not tonight's regime, is the binding cap.
  - **Data-quality:** 4 of 12 (APP, WING, RBA, ONON) carried **negative** UW `pct_52w_range` (stale w52l above close). All four Yahoo-verified as **genuine** near-lows (0.1% / 0.4% / 0.3% / 3.6% of range) — the screener filter works, the reported field is corrupt.
  - **GPI re-emerged** after being dropped 08-10 on a split/adjustment artifact — flagged, not promoted; re-verify before it is ever scored.
- **MOM_LONG — 20-name basket top slice.** Basket/watch only, never sizes; baseline −0.0108 (n=1066), DURABLE-N bar unmet. **All 20** carried UW `pct_52w_range` **>1.0** (out of range); all 20 Yahoo-verified as genuine near-highs (96–100%).
- **S2 — 80 names** post-gate (41 BUY-side). Advisory-only, never sizes. **The lane did not complete its news gate** — the full list is carried as **news-unverified** and was deliberately withheld from the structured write-back.
- **S4 — 17 names**, all gates pass. Advisory-only, never sizes. Plus a 4-name `ivrank_chg_5d` h3 tilt (LYG, LBRT, IMAX, INCY) reported separately, never stacked.

---

## Risk

- **Correlation clusters:** COO (Healthcare) and NRG (Utilities/IPP) share no sector, factor, or catalyst thread — two singleton clusters. No pairwise coefficient was computed; sector distinctness was treated as sufficient for two unrelated names. **A numeric check should gate any future night that pairs two OI_FADE names inside the same sector.**
- **Event calendar:** CPI 08-12 · PPI 08-13 · Advance Retail Sales 08-14 (all Tier-1) · UMich prelim 08-14 (Tier-2). FOMC 09-15/16, outside the window.
- **Tail caps:** N/A — OI_FADE is not one of the gate-6 tail-capped lanes (MOM_SHORT / S2-long / vol-short), and none of those sized.
- **Hedge note:** book is flat; no hedge required.
- **Short gamma + three Tier-1 prints** means realized vol tomorrow is likely understated by VIX 15.28. Anything opened here should assume wider realized ranges than the LOW tercile implies.

### Tooling defects found tonight (worth fixing, not blocking)

1. **`finnhub_enrich.py` `leverage_flag` is wrong** — labelled NRG's D/E of 5.55–9.78 as **"low"**. Both Finnhub's own metric and `fz` disagree with the script's own label. A threshold bug in the classifier; it would soften a genuinely levered name's risk read.
2. **`fz` CLI** does not expose `Recom` / `Target Price` in any view checked (overview / valuation / technical / financial / ownership), and bare `fz news <T>` / `fz insider --ticker` return malformed output. Analyst PTs had to come from Finnhub news; **insider-cluster data was unavailable** for both names.
3. **Phase D hand-rolled `jsonschema`** instead of `scripts/validate_decision.py`. Re-validated with the prescribed script — **VALID**. (Envelope also patched: NRG's invalidation was an unevidenced "~$125"; now pinned to the actual $124.71 post-crash swing high from `chart.py`.)

---

*Truth-set parquets (prices / returns / features) were **stale by one session** at preflight and were rebuilt before any lane read — prices 2,449 tickers / 342,980 rows, features 85 dates / 2,478 tickers. Re-verified clear. Prior book (`conviction_2026-08-10.json`) confirmed genuinely flat — 0 open, 0 closed — checked against the file directly, not on the bare `held_book.py` empty result.*
