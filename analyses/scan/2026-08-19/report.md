# Market Scan — 2026-08-19

## Regime & Verdict
- **Regime: CHOP** · ret5 **−0.440%** · ret10 **−0.090%** · dd15 **−3.650%** · vol-state **LOW** (VIX **14.89**, down from 15.84)
- `directional_tradable` = **True** (structural: all four lanes have non-empty candidate pools tonight)
- `s1_standdown` = **False**
- Regime arbitrated: `regime_check.py --date 2026-08-19 --claim-label CHOP --claim-ret10 -0.0009` → **exit 0, claim checks out**. Phase A also hand-recomputed all three metrics off live Yahoo closes (SPY 769.06) and matched the panel bar-for-bar — this is a live read, not the stale-parquet fallback.
- Preflight **clear**: 5/5 UW groups present for 08-19; truth set **rebuilt tonight** (prices 353,405 rows / 2,446 tickers; features 176,100 rows / 2,486 tickers / 91 dates) and now reaches the trade date.

**Bottom line: no directional edge today. Zero new starters — the book stays flat for an 8th consecutive session.** One name (AS) cleared every hygiene gate and the OI_FADE lane's own selection rule, and was still withheld — for a reason worth reading, below.

## Directional Book (excess-scored)

**Empty.** No name reached a sizing band in any lane.

| Ticker | Lane | Dir | Horizon | validated_excess | regime_fit | size | invalidation | gates |
|---|---|---|---|---|---|---|---|---|
| AS | OI_FADE | short | h10 | **UNESTABLISHED** | 1.0 | **watch** | n/a — not sized | all PASS; withheld on the excess question |

### Why AS did not size — the central adjudication
AS (Amer Sports) is the only name tonight clearing the live OI_FADE lane's actual selection rule *and* every hygiene gate:

- `oi_rel_build` **1.562**, persistence **0.736**, 5d net **+75,011** (call +112,733 / put +37,722)
- Liquidity **PASS**: $34.02, 20d $-ADV **$178.1M** (script-sourced, not hand-multiplied)
- Earnings gate **PASS**: reports 2026-11-17, clear of the h10 window (ends 09-03)
- Catalyst-split **LIVE_BUILD on both boundary conventions** — 51.3% with the script's default `>=`, **41.2% under the strict `>`** that excludes the print day. The two agree here (unlike the EWTX case, where they inverted), and the largest single post-print day is 08-19 itself (+38,742 call). The build genuinely survived its own 08-18 catalyst.
- Not deal-pinned (5d realized vol 1.69%/day, an order of magnitude above the deal-pin signature). AS–SPY corr 0.550, below the 0.70 cluster threshold.

**It is still watch-only, because its `validated_excess` is unestablished — not positive, and not measured-zero.** The only measured OI_FADE prior (**+0.0038, n=1176**) is computed on the **raw top-15 by `oi_net_5d`**. I independently ranked tonight's panel: **AS sits at rank ~26–30 of 1,174**, roughly 2x outside that population. Under Phase C, `score = validated_excess × regime_fit × (1 − fundamental_contradiction)` — an unestablished prior cannot inherit a positive score by borrowing the lane's general reputation. That extrapolation ("hygiene-pass + a big number ⇒ edge") is precisely the additive-confluence error the gate stack exists to prevent. **Score floors at zero, so size floors at zero.**

This is an epistemic gate, not a claim that AS's edge is negative.

### The standing structural gap, now in its 10th session
The raw top-15 — the population the +0.0038 baseline actually grades — decomposes tonight as:

- **5 ETPs cut**: GLD, TLT, SLV, DRAM, SQQQ
- **2 earnings-blocked**: NVDA (reports **08-26**, inside h10), IREN (**08-27**, inside h10)
- **1 mechanically invalidated**: NOK (last call_net −11,101)
- **1 exclusion carried forward**: RKT — ValueAct 9.9% activist stake, build accelerated 2.3x behind the 08-14/08-17 disclosures. Re-checked tonight and **still live**: 08-18 was the single biggest day of the window (+54,280 call). Catalyst-informed positioning is not a crowd to fade.
- **4 mega-cap beta traps**: META, GOOGL, AAPL, WULF pass every mechanical gate but carry `oi_rel_build` **0.045–0.121**, an order of magnitude below the lane's own threshold. These are large numbers on enormous books — the QQQ-beta-short failure mode — collapsed into one conceptual non-position rather than sized individually.

So the population the prior measures is, tonight, entirely ETPs, mega-cap beta, earnings-blocked names, and one activist situation. Meanwhile the rule the live engine actually runs (rel_build/persistence) has **never been graded against a harness baseline**. That gap is the single most important open item in this repo and is now a live agenda item for the **2026-08-22 calibration audit**.

## Vol Book (non-directional, delta-neutral, quoted net-of-cost)

**0DTE-VRP: STAND ASIDE on both SPY and QQQ.**
- **SPY** — the pooled headline reads `sell_premium=true`, and spot-vs-flip reads LONG gamma, both of which would green-light selling. Both are overridden by the **VIX-tercile pooling trap**: VIX 14.89 is in the **LOW** tercile (bound 16.1), where conditional gross is **+0.02%/day** against a **0.10%** round-trip cost → **−0.08%/day net. Negative.** Gamma reads kept deliberately distinct per the 08-05 fix: *aggregate sign* (net GEX 0–45d = −3,944M) drives wing width (1.21%, the short-γ bucket); *spot-vs-flip* drives the sell decision. Not deployed.
- **QQQ** — fails twice independently: dealers net **SHORT** gamma (spot below flip — the left tail this sleeve cannot survive and never sampled), and LOW-tercile net is **−0.033%/day** even ignoring the gamma veto.

**Earnings IV-crush: ROST flagged, not sized.**
- Prints **2026-08-20 (tomorrow)**; bracketing expiry **08-21 confirmed after the print** — the bracketing-expiry trap was checked, not assumed.
- Deep backwardation: front avg IV 110.9% vs 30-DTE 37.1% (2.99x).
- ATM straddle 15.20 on 234.9 spot → **6.47% implied move**, treated as a **floor, not an estimate** (the CLI's own `implied_move_perc` read 5.59%, softer still).
- Not sized: no net-of-cost quote was computed, so the vol-short tail cap cannot be satisfied tonight.
- **OKTA and HPQ** are workable only after overriding the tool's wrong-expiry `implied_move_perc` (**3.06%** and **2.62%** — badly understated; correct bracket for both is **08-28**, giving ~14.4% and ~10.3%). Logged as the trap recurring, not as trades.

## Watch / Stood-down
- **AS** (OI_FADE) — the night's central name; watch pending the raw-rank/rel_build population question, not a hygiene failure.
- **CUT — BSY**: OI_FADE **mechanical invalidation FIRED**, last call_net **−124** on 08-19; `oi_build.py` prints *"last call_net NEGATIVE — calls genuinely closing."* Persistence 0.594. *(Phase D had carried BSY as "still building organically, persistence 0.578" — that contradicted both the lane's own CUT and the tool's explicit invalidation print, and was corrected here after direct verification.)*
- **CUT — FDX**: discretionary, no mechanical trigger (last call_net still +440). Persistence **1.205** trips the tool's own *">0.85 = likely a single-day block, not organic"* flag; daily net alternates sign (08-13 −803, 08-18 −546); rel_build 0.188; raw rank 354/1174 — never inherited the prior across its entire watch tenure.
- **MOM_SHORT basket (never sizes)** — baseline **−0.0137** (n=830), the one recorded exception to the no-negative-lane invariant, plus the **PROVISIONAL cap** from the 2026-07-18 audit (sized book was 0-for-9, −5.3% excess). 9 names, each Yahoo-verified near its 52w low: ALHC (0.6%), GME (1.1%), ROL (1.4%), CPRI (1.6%), ESAB (2.0%), JBTM (2.4%), AGCO (2.9%), CRH (4.2%), PEG (8.4%).
  - The lane correctly excluded **VMRK** and **MIDD** as stale-`w52h` false shorts (both mid-range ~39–49%).
  - **FDXF dropped by the orchestrator** — a *third* failure class, not previously recorded: only **57 bars of history** (first bar 2026-05-27, a spinoff), so its "52-week" range is a ~3-month window. Internally consistent, but not the validated factor. Its 52w low (05-27) and high (05-28) are one day apart, which is what surfaced it.
- **MOM_LONG basket (never sizes)** — baseline **−0.0127** (n=1154), plus a DURABLE-N bar. MRNA, TWST, MRK, IOVA, AMLX verified at **98.3–99.6%** pct_range on Yahoo (+10 more unverified). **Data-quality flag:** the lane reported these as "MRNA 203.7%" etc. — a stale-panel `w52h` artifact. Name *selection* verifies; the *ranking metric* does not, so the ordering is unreliable.
- **S2 advisory (never sizes)** — +0.0014. SLF ($141.3M DP, 100% sell-side), YUMC ($21.9M, 90% buy), FRPT ($15.3M, 94.7% buy), ABG ($11.6M, 100% buy). All liquidity-PASS and earnings-clear. Note the DP complex was **thin**: 39 tickers cleared the bar vs ~171 on 08-18.
- **S4 advisory (never sizes)** — +0.0025, and `hit − base` is **negative (−0.056)**: right-tail-only, **no hit-rate edge**. ZION (PCR 5.40 on **307 calls** — clears the post-fix 250 call floor, so a real crowd, not the NWG-style denominator artifact), VICI, GD, TROW, DX. VSXY and BAH excluded on prior blocking VETOs.

## Risk
- **Event stack inside the h10 window (08-20 → 09-03):** **08-26** July PCE + **NVDA earnings** (after close) · **08-27** Jackson Hole opens · **08-28 Warsh's first keynote as Fed Chair** (Tier-1 policy risk) · 09-01 ISM · NFP 09-04, just outside. Anything opened tonight resolves straight into that gauntlet — this alone would have cut a starter to watch even had the excess question resolved favorably.
- **Mechanical regime pinch confirmed at 08-27.** Holding SPY flat at 769.06, the ret10 anchor rolls onto the 08-13 local high (777.88) that day, driving ret10 to **−1.13%**; PULLBACK triggers on a **766.21** close — only ~0.4% below flat. Re-derived off tonight's rebuilt truth set, and it reproduces the 766.21 figure the 08-18 scan projected. The pinch resolves by 09-02 when the anchor rolls onto today's close.
- **The crash guard is one print from firing.** dd15 −3.65% **already satisfies** the `dd15 < −2%` leg of guard-arm (a); it needs only `ret5 > +1.5%` — a close above ~**780.65** — to flip `s1_standdown` True and suppress MOM_SHORT. With PCE and NVDA both on 08-26, that is a live path, not a hypothetical.
- **Breadth divergence:** price breadth healthy (**56.66%** green) while options-flow breadth is weak (**36.5%** bullish tickers) and sector rotation is defensive — out of Technology (−$59.1M) and Comm Services (−$73.5M), into Healthcare/Consumer Defensive. A mild distribution tell in mega-cap growth leadership; not a gate trigger.
- **Vol-state asymmetry:** SPY's near-the-money gamma flips sign right at spot — negative from 760–768, positive above 769 — so a move down through ~765–768 walks into a dealer-short-gamma pocket (vol-amplifying) while upside stays pinned. QQQ is `FULLY_NEGATIVE` (−$560M, no flip in range), i.e. structurally vol-amplifying in tech. Convexity note only; **no direction is read from GEX/DEX**.
- **Correlation clusters:** none binding — nothing sized. AS–SPY 0.550.
- **Hedge note:** no book, no hedge required.
- **Fundamentals-gate: correctly NOT spawned.** Standing rule is that it runs only on names about to be sized; nothing reached a sizing tier.

## Process notes
- **Regression gate not triggered** — no lane or threshold code changed tonight. The panel grew by one session, which is data drift, not a code change (`docs/regression-gate.md`).
- **Next calibration audit: 2026-08-22** (3 sessions out). It inherits the cohort that has now been deferred twice, plus a new standing agenda item: *grade the live lane's rel_build/persistence rule, or accept that the +0.0038 OI_FADE prior describes a rule the engine no longer runs.* Ten consecutive sessions of total raw-rank/live-rank divergence have now accumulated.
