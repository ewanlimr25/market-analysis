# Market Scan — 2026-07-10 (Fri, post-market)

## Regime & Verdict
- **Regime:** UPTREND · vol suppressed/pinned at index (SPY GEX+, ZG 754.15 ≈ spot; VIX 15.03, 15d low) with a latent **tech vol-amplification** skew (QQQ short-gamma, spot well below ZG) · breadth healthy (67% green, 338/163 A/D) **but** options-flow positioning bearish-skewed (33.4% bullish across 6,261 names — crowded-hedge backdrop) · `directional_tradable = true` · `s1_standdown = false`
- SPY 754.95 (+1.37% 5d, +2.81% 10d, −0.72% off 52w high); above 20/50/200-SMA. Composite regime reads "TRANSITIONAL" only because of the flow-positioning skew, not a price-breadth divergence.
- **Bottom line: 2 regime-appropriate calls** — both starter-size shorts. The two most robust lanes (OI-flow-fade, MOM_SHORT) both point short and are LIVE (crash-gate off), but the fundamentals veto + earnings-in-horizon gate thinned the book to one clean-CONFIRM name and one CAUTION. **This is a thin, short-tilted book on an up tape — sized accordingly.**

## Directional Book (excess-scored)
| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | Size | Fundamentals | Invalidation | Gates |
|---|---|---|---|---|---|---|---|---|---|
| **MAT** | OI_FADE | short | h10 (→07-24) | +2.1% median (hit 0.61 vs 0.41, n=640) | 1.0 (shorts live) | **starter** | CONFIRM (Goldman→Sell 07-09, 3rd PT cut, fresh 52w low) | OI build reverses / breakout on real catalyst | liq PASS · no earn-in-horizon (08-04) · downsized: Consumer-Cyclical is this week's sector-**inflow** destination (squeeze headwind) |
| **OLED** | OI_FADE | short | h10 (→07-24) | +2.1% median (as above) | 1.0 | **starter** | CAUTION −1 (insider MSPR +74.7 buying into the short) | OI build reverses / earnings 07-30 surprise | liq PASS · Tech = sector **outflow** (tailwind) · CAUTION knocked half→starter |

*No name is sized above starter.* Every deviation from a lane's implied ceiling was a **downgrade** — consistent with half-cap-no-auto-full.

## Vol Book (non-directional, delta-neutral, net-of-cost, advisory — 0 directional points)
- **Earnings IV-crush SELL-VOL** (rank by implied-vs-realized richness, wide wings — CPI/PPI mid-horizon realized-vol risk):
  - **NFLX** (primary — most liquid, IV-rank 99.1, earn 07-16) · **TSM** (secondary, IV-rank 88.0, 2.4x, earn 07-16)
  - **JNJ** cautious (4.4x richness is an *anomaly* — verify no idiosyncratic catalyst before entry, earn 07-15) · **STT** half (IV-rank 78.3, just under 80 gate, earn 07-16) · **ASML** half (earn 07-15) · **CAG** small (thin liquidity, earn 07-15)
  - **Bank cluster JPM/BAC/C/WFC EXCLUDED** — IV-rank 22–51 (below 80 gate); WFC implied move actually *cheaper* than its realized average. The "obvious" macro-calendar candidate is not a crush candidate — exactly the screen-vs-reality gap the lane catches.
- **0DTE-VRP premium-selling:** **no clean sell today.** SPY marginal quarter-size only (30d VRP FAIR, VIX below sample floor — out-of-sample-low). QQQ **stand-aside** (30d VRP PREMIUM_BUYING −7.3% + negative gamma both argue for *buying* convexity, not selling).

## Watch / Stood-down
- **VETO → watch-only:** TDG (3/3 beat streak, +13.3% rev, Zacks upgrade + raised guidance this week), CPRT (3/4 beats, founder Jay Adair returns 07-31 w/ growth/M&A mandate). Both showed ≥2-of-3 fundamentals-fight-the-short + a live bullish catalyst — correctly not shorted.
- **CAUTION, MOM_SHORT ceiling already starter → watch:** GPOR (rev +90.7% YoY + S&P 600/1500 index-inclusion bid), XE (<3mo history, ARK bought ~$15M, Russell inclusion 07-08, UBS/TD Cowen Buy above price).
- **Earnings-in-horizon → held at watch:** SLM (07-23, top OI-fade rel-build 1.40x), ACI (07-23), FR (07-22), TEL (07-22).
- **Missing fundamentals verdict → held (cannot size unverified):** XENE, INSP, TYL, HIW, GFL, GIL, PCAR, UDR, JOBY, CSGP, PATK. Flagged for next-run fundamentals-gate spawn (priority: HIW — 0.58x, not earnings-gated).
- **Advisory lanes (not in directional book):**
  - **S2 liquidity-reversion** (long-tilt, h3–5, +0.47%, MODERATE): SELL_LOSERS bounce KEY (94.7% sell-side, $71.6M), GNRC (92.2%). BUY_FADE tier needs next-session DP-concentration validation. CPK **dropped** (failed $50M liquidity floor). Half-cap max, decays by h10.
  - **S4 sentiment-contrarian** (PCR-fade long, h5–10, +0.71%, LOW-MOD advisory): FSS (PCR-z 19.85 + IV-rank rise), MSM (z 10.14), TDY (z 8.43). HCA **cut** (informed Barclays downgrade same-day). Short mirror NOT fired (measured negative).
- **MOM_LONG basket** (documented, never per-name HIGH, tail-driven +2.35% mean): CROX/CAKE/PAG/EAT/EXTR/OII/EXPD/NSC/CM/RY/UNP/MUFG/ETSY/TIGO. Theme clusters noted, not sized.
- **BOIL excluded** from MOM_SHORT (2× leveraged nat-gas ETP — artifact).

## Risk
- **Correlation clusters collapsed:** `oi_fade_reit` FR/HIW/UDR → 1 slot (all within 6% of 52w high, crowded-call-at-top; all held at watch). MOM_LONG theme clusters (railroads NSC/UNP/EXPD; banks CM/RY/MUFG; discretionary CROX/CAKE/EAT/ETSY) documented, never per-name.
- **Event calendar (h10 window 07-10 → 07-24):** CPI 07-14, PPI 07-15, big-bank Q2 earnings 07-14 (all Tier-1) — defined-risk-through-print, macro tag on the whole book, not an automatic −1. Vol-book earnings TSM/STT/NFLX 07-16. FOMC 07-29 just outside the window — flagged as approaching.
- **Tail caps applied:** OI_FADE/MOM_SHORT sized for the up-tape short-squeeze tail (MAT's sector-inflow downsize; GPOR index-inclusion + XE ARK/Russell squeeze flags → both to watch). MOM_LONG kept basket-only. Vol-short sized for the left tail, quoted net-of-cost (JNJ-anomaly + STT-borderline caveats).
- **Hedge note:** QQQ negative gamma = the fragile leg; any tech-heavy add wants tighter vol sizing. Book is net-short into a pinned-but-complacent index (VIX 15) — small, single-theme-diversified, half-cap.

---
*Envelope: `decision.json` (v2, validated vs schema). Conviction persisted: `conviction_2026-07-10.json` for next-run adverse-flow exit checks. No lane/threshold change this scan → regression gate not triggered.*
