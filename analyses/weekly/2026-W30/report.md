# Weekly Review — 2026-W30 (Mon 2026-07-20 → Fri 2026-07-24)

**Bottom line:** an AI-capex repricing week disguised as a quiet one. SPY fell only 1.09%, but that number
hides a ~9pp sector spread and a single-session Mag-7 shock. **No Layer-2 call is scored.** Two OI_FADE names
cleared every mechanical gate and both were killed on grounds the lane cannot see by itself.

---

## 1. The Week in Pictures (DIARY — documentation, 0 signal)

### Weekly candles

| | Open | High | Low | Close | w_ret | close_pos | body | Structure |
|---|---|---|---|---|---|---|---|---|
| **SPY** | 747.06 | 750.02 | 735.21 | 738.93 | **−1.09%** | 0.25 | 0.55 | lower low, follow-through, 2nd down week |
| **QQQ** | 702.16 | 710.05 | 682.48 | 684.23 | **−2.55%** | **0.06** | 0.65 | lower low, follow-through, **closed on the dead low** |
| **IWM** | 295.01 | 296.75 | 290.17 | 291.17 | **−1.30%** | 0.15 | 0.58 | lower low, follow-through, 4th down week |

All three made lower lows, closed in the bottom quartile of their range, and confirmed the prior week's
direction. No inside week, no outside week, no hammer or star on any index. SPY closed below both its 20-SMA
(746.15) and 50-SMA (745.07). QQQ is now −5.6% over two weeks.

### Catalysts, anchored to price

**No Tier-1 macro landed all week** — no CPI, PPI, PCE, FOMC or NFP. The entire week's structure came from a
two-name earnings cluster.

| When | Event | Price reaction |
|---|---|---|
| Wed 07-22 AH | **GOOGL Q2** — beat, but FY26 **capex guidance raised to $195–205B** from $180–190B | GOOGL **−7.1%** Thu, −7.80% on the week. Sold *despite* a beat |
| Wed 07-22 AH | **TSLA Q2** | TSLA **−14.5%** Thu — worst earnings-reaction day on record; −17.81% on the week |
| Thu 07-23 | **Mag-7 capex de-rating** | Mag-7 index −4.8% intraday, **~$767B erased in one session**. META −3.4%, AMZN −4.6% on *no company news* — pure read-through. Nasdaq −1.66%. **Regime flipped CHOP → PULLBACK here** |
| Thu 07-23 | Red Sea tanker attacks lift crude | XLE +3.36%, top sector — exogenous, orthogonal to the equity story |
| Mon–Thu | **Memory/storage melt-up** (DRAM contract prices +95% in Q1'26; MU fiscal-Q3 revenue +346% YoY) | MU **+8.48%**, STX **+8.13%**, SNDK **+6.03%** on the week — **all three reversed hard Friday** (MU −7.0%, SNDK −10.8%, STX −6.8%) |

The mechanism worth remembering: **Alphabet was sold on a good quarter.** The market repriced AI capex
intensity, not earnings quality — which is why the damage was surgical (mega-cap growth) rather than broad.

### Regime trajectory

| | Regime | ret5 | ret10 | breadth %green | VIX | SPY GEX | s1_standdown |
|---|---|---|---|---|---|---|---|
| Mon 07-20 | CHOP | −0.95% | −1.22% | 32.6 | 18.65 | −1.94B | FALSE |
| Tue 07-21 | CHOP | — | — | 45.5 | 17.05 | less neg | FALSE |
| Wed 07-22 | CHOP | −0.98% | +0.27% | 48.9 | 16.64 | short-γ | FALSE |
| Thu 07-23 | **PULLBACK** | −1.67% | −1.80% | 42.4 | 18.70 | −2.47B | FALSE |
| Fri 07-24 | **PULLBACK** | −0.587% | **−2.122%** | 72.2 | 18.58 | −1.556B | FALSE |

**A grind-down, not a crash.** ret10 deepened through −2% while ret5 *stabilized* (−1.67% → −0.59%). Vol
**round-tripped rather than expanded** — VIX 18.65 → 16.64 → 18.70 → 18.58, ending −0.4% on the week — but GEX
stayed FULLY_NEGATIVE on both SPY and QQQ every session, and VRP stayed FAIR throughout (no premium-selling
edge opened). The crash guard never fired on any day.

Friday's breadth print is the week's best single tell: **72.2% green while SPY closed +0.10%.** The median
stock rallied; the cap-weighted index was dragged by its largest members. Options-flow breadth was only 33%
bullish over the same session — a hedging tell, two-sided, not a short-book confirmation.

### Sector leadership

`XLE +3.36% · XLU +2.48% · XLI +1.81% · XLB +1.44% · XLRE +1.17% · XLV +0.92%` — then
`SMH +0.84% · XLK +0.17% · XLF +0.09%` — then `XLP −1.24% · XLC −3.93%` (GOOGL/META) ·
`XLY −5.22%` (TSLA, worst). An ~8.6pp spread inside a −1.09% index.
Money flow confirms: **out of** Technology (−$392.5M) and Consumer Cyclical (−$160.6M), **into** Consumer
Defensive and Energy.

> **Corrected.** An earlier live-feed read had XLC a session stale (last bar 07-23) and gave −6.45% over a
> 07-16→07-23 window. The panel figure is **−3.93%** over the correct 07-17→07-24 window. The lag was
> transient and did not reproduce; all sector figures above are now measured off `data/prices.parquet`.

The structural item: **the near-52w-high cohort now contains essentially no mega-cap technology.** It is
industrials, insurance, rails and regional banks (OII, TRV, FAF, PKG, WAB, CSX, RTX, BAC, SPG). That cohort
survived the week precisely because it is not what got de-rated.

### Notable flow (diary only — raw flow measures as beta here, `research/20`, `70`)

Dark-pool premium: SPY $52.1B (61k prints) · **MU $46.2B (144k prints)** · QQQ $33.8B (65k) ·
**SNDK $26.8B (107k)** · NVDA $25.6B (87k) · AMD $18.0B · TSLA $16.9B · AAPL $14.9B.

MU printed **more individual prints than SPY and QQQ combined** and ranked second in dollars to SPY alone.
The memory complex absorbed institutional-scale two-way volume into its melt-up, then reversed on Friday.

---

## 2. Validated Weekly Setups (SCORED — excess)

### `calls[]` is EMPTY. No Layer-2 call is scored this week.

| Lane | Disposition | Fit | Why nothing sized |
|---|---|---|---|
| **OI_FADE** | NO_NAME_CLEARED | 0.70 | Two names cleared every mechanical gate; both already killed — see below |
| **MOM_LONG** | BASKET_WATCH | 0.30 | Basket-only always; long-near-high into a confirmed PULLBACK fights the tape |
| **MOM_SHORT** | STOOD_DOWN | 0.60 | Watch-only cap for new starters (invariant #6) — **not** the crash guard |

**OI_FADE — the most favorable regime this lane has seen in weeks, and still nothing to trade.**

- **ALLE** — `net_10d +4,308` (call +4,531 / put +223), `rel_build 2.539`, `persistence 0.412`, ADV $223M,
  earnings 10-22 clear of h21. Genuinely organic: the build **continued after the print** (+880 on 07-23,
  +653 on 07-24). **Fundamentals VETO stands** — Q2 EPS $2.40 vs $2.256 (+6.4%), revenue +13% YoY, FY26
  guidance **raised**, and two same-day PT raises (JPM $150→$170, Baird $175→$190) both *above* the $153.36
  close. The gap held while the tape sold off = idiosyncratic strength. A PEAD tail cap applies on top.
- **SSNC** — mechanically top-ranked (`rel_build 2.493`) but **invalidated by catalyst resolution.**
  Independently verified: the entire build (+335 / +3,070 / +731 on 07-20/21/22) landed **before** its 07-23
  after-close print, then went **+0 and +1** on 07-23/07-24 while the stock gapped **+10.35%** (66.95 → 73.88).
  That is resolved pre-print positioning that already paid — not a crowd left to fade.
- **ACVA** — strictly worse than last week: still fails the $50M floor ($25.6M/day), *now also* earnings-blocked
  (08-10 inside h21), and `last_call_net` has turned negative (calls genuinely closing).
- Also cut: AVTR/MWH/HRI/AVIR/AARD/SCM/CACI (earnings inside h21) · SLGN/BKE/FHN/OSIS/TASK/DLLL/EQPT
  (persistence ≥0.85, single-block artifacts) · BITQ/IBX/CBRG (ETP).

> **Helper-script coverage gap found.** `earnings_gate.py` **passes** SSNC, because it only checks *forward*
> earnings — it cannot see a catalyst that already landed *inside the build window*. Nothing was mis-sized
> (the 07-24 scan had caught it independently), but the gate does not protect this case on its own.

**MOM_SHORT — the stand-down reason matters.** `s1_standdown = FALSE` on all five sessions, affirmatively so
on Friday: ret10 −2.12% is past the −2% confirmed-downtrend boundary, so this is explicitly *not* the
unconfirmed-V-bounce the guard exists to catch. The lane is capped anyway by standing policy because its
re-baselined excess is **negative (−0.03% mean, n=281)**. The +20.6pp hit-base is **not** the binding read.
Six names pass full hygiene (ORCL held, plus ACI, CCI, CMCSA, OKLO, AZO); none sized.

---

## 3. Weekly Technicals — PRE-REGISTERED (documented, 0 points, NOT sized)

| Feature | This week | Would signal | Status | Bar |
|---|---|---|---|---|
| Triple-index confirming lower-low week | SPY+QQQ+IWM all lower-low, all follow-through TRUE, all closed bottom-quartile | Trend continuation → short tilt or stand-aside for longs | PRE-REGISTERED | PR-WT (≥2yr) |
| QQQ close on the dead low | close_pos 0.06, body_frac 0.65 | Unresolved selling into next week's open | PRE-REGISTERED | PR-WT |
| Reversal-after-catalyst (**Tier-1 macro arm**) | **No observation** — zero Tier-1 prints landed | n/a — arm needs a dated macro print | PRE-REGISTERED | PR-WT |
| Reversal-after-catalyst (**earnings-cluster arm**) | Thu 07-23 gap **extended**, did not reverse; Friday held the loss | A catalyst move that *holds* = genuine repricing, not an overreaction to fade | PRE-REGISTERED | PR-WT |
| IWM outperforming QQQ in a down week | −1.30% vs −2.55%, inverting the usual risk-off ordering | Factor repricing rather than broad risk-off; argues against treating it as a beta event | PRE-REGISTERED | PR-WT |

None of these earned a point and none may be sized. The macro arm accrues **nothing** from W30 — worth noting
so the pre-registration count isn't overstated later.

---

## 4. Carry-forward

**Held book — two shorts, both working, both already managed on 07-24.**

| | Lane | Entry | Mark | Gross | Excess | State |
|---|---|---|---|---|---|---|
| **ORCL** | MOM_SHORT | 131.54 (07-13) | 114.99 | **+12.58%** | +4.31% | **Trimmed 50%** on 07-24; remainder on tightened invalidation |
| **PLNT** | OI_FADE | 55.20 (07-20) | 53.48 | **+3.12%** | +1.48% | HOLD, hard exit **2026-08-05** |

- **ORCL — hold the remaining half.** Live invalidation is **`close > $123.50 with 2-day confirmation`**,
  currently **+7.40% away**. The entry-era stop (`RSI>45 AND close>$144.22`) went **vestigial** once the
  position ran >10% in its favor — held to it, the trade would have surrendered the entire gain before any
  documented exit fired. ORCL printed a fresh 52-week low ($114.75 intraday) on Friday. No adds — the
  MOM_SHORT tail cap forbids new sizing. Reassess by the 08-07 NFP boundary; own ER 09-08 is clear.
  - *Correction logged:* the Phase-B momentum lane read ORCL against the **superseded** entry-era 52w-low
    (134.57) and called the stop ~19.6pts away. The live stop is $123.50 — roughly half that distance.
- **PLNT — hold to the deadline, do not extend to the weekly horizon.** `earnings_gate.py` confirms **BLOCKED
  at h21**: the print has drifted to **08-06**, inside any 2–4 week hold. Signal itself is intact (post-entry
  call_net +830/+509/+179/+173, no unwind) and is *not* vestigial at +1.48% excess. Exit 08-05.

**Into next week:** FOMC **07-29** and Core PCE **07-30** both land inside any new 2–4wk hold, with MSFT+META
(07-29) and AAPL+AMZN (07-30) reporting into the same window — on FULLY_NEGATIVE GEX, where dealer hedging
amplifies a surprise in either direction. Vol did **not** compress into that cluster. Against a book that is
100% short and a lane set producing nothing, the posture is: manage the two held shorts to their documented
levels, add nothing pre-event.

**Watch:** ALLE re-examines only if the raised FY26 guidance is walked back, the PT raises reverse, or the
07-23 gap fills *without* the call-OI build unwinding. SSNC is done — its catalyst resolved.

---

### Verification notes
- Regime figures recomputed directly from `data/prices.parquet` (SPY ret5 −0.587%, ret10 −2.122%). The Phase-B
  momentum lane independently reported **CHOP / ret10 −1.37%**; that read was **wrong and discarded**.
- `preflight.py --date 2026-07-24` clear: 5/5 panel groups, truth set reaches the trade date.
- `oi_build.py`, `earnings_gate.py`, `liquidity.py`, `chart.py`, `held_book.py` used for all per-name figures;
  SSNC/ALLE day-by-day OI and the ALLE/SSNC price paths were re-derived rather than taken from the lane.
- `validate_decision.py --file analyses/weekly/2026-W30/decision.json` → **VALID**.

**Sources for the week's catalysts:**
[TheStreet, Jul 23](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-july-23-2026) ·
[Motley Fool, Jul 23](https://www.fool.com/coverage/stock-market-today/2026/07/23/stock-market-today-july-23-tesla-drops-15-leading-tech-stock-slide/) ·
[Mag-7 $767B](https://www.spokesman.com/stories/2026/jul/23/magnificent-7-lose-767-billion-as-ai-skeptics-dump/) ·
[CNBC, Jul 23](https://www.cnbc.com/2026/07/22/stock-market-today-live-updates.html) ·
[24/7 Wall St — memory rally](https://247wallst.com/investing/2026/07/21/sandisk-rises-8-western-digital-jumps-9-micron-adds-7-as-memory-rebound-accelerates/) ·
[24/7 Wall St — memory pricing](https://247wallst.com/investing/2026/07/22/memory-prices-are-still-skyrocketing-is-the-next-rally-for-micron-sandisk-and-sk-hynix-just-beginning/)
