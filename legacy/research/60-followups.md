# 60 — Follow-up tests (pre-migration hardening)

_Three follow-ups requested before migration: test the untested lanes (PR-1 sector flow, PR-4 signed/opening flow), harden S1 (options-carry leakage + crash guard), and scope a panel extension. Same truth set, same conditional benchmark._

## 6.1 PR-1 — Sector-rotation lane: **BETA (no durable edge)** → confirms advisory demotion
Built the lane the old `sector-rotation-strategist` implies: per (date, sector) net options flow
(`net_call_premium − net_put_premium`), trailing-5d (≤T), daily tercile rank; members of top-flow sectors
**long**, bottom-flow sectors **short**. n=58,716 signal rows.

| Leg | h | n | mean_exc | hit | base | hit−base | ic | p |
|---|---|---|---|---|---|---|---|---|
| long | 5 | 11,391 | −0.0016 | 0.46 | 0.48 | −0.018 | −0.01 | 0.06 |
| long | 10 | 9,898 | +0.0014 | 0.47 | 0.54 | −0.063 | −0.01 | 0.26 |
| short | 5 | 11,826 | −0.0132 | 0.46 | 0.39 | +0.068 | −0.06 | ~0 |
| short | 10 | 10,686 | −0.0172 | 0.48 | 0.37 | +0.110 | −0.06 | ~0 |

**Read:** the long leg has ~0 mean excess and hits *below* base (beta/noise); the short leg has *negative*
mean excess (shorting low-flow-sector names **loses** — they rise), and its sign **flips across regimes**
(A long +0.005 vs B1 long −0.004; A short ~0 vs B1 short −0.019). The positive `hit−base` on the short is
the familiar SPY-down-base-collapse illusion, not edge (mean stays negative). **Verdict: BETA.** The one
fleet lane Phase 2 had not measured, now measured, carries no durable edge — `sector-rotation-strategist`
stays cut/advisory (DESIGN §4.5). Pre-registration PR-1 is **decided: do not promote.**

## 6.2 PR-4 — Signed/opening/intraday flow: **not testable on this panel; best proxy already beta**
The Pan-Poteshman alpha lives in **signed, opening-position, intraday, account-level** flow. The panel is
**EOD-aggregate** — that granularity is destroyed by construction. The best available proxy (`OI_BUILD_ASKSIDE`,
ask-initiated OI-confirmed builds) **measured BETA in Phase 2** (`RESEARCH/20`). So on this data the answer is
definitive only in the negative: **the EOD aggregate cannot recover the opening-flow alpha; confirming it
requires intraday/account-level signed data the panel does not contain.** PR-4 remains open pending a finer
data feed — flagged, not claimed.

## 6.3 S1 hardening (1): options-carry leakage is **real but small — the edge survives rich puts**
Phase 3 flagged that near-52w-low names carry rich put skew, so the equity short edge might already be priced
into puts. Test: S1 h=10 short excess split by IV-rank (full near-low cohort, n=1,775 resolved):

| Cohort | n | mean short_exc | hit | base | hit−base | median |
|---|---|---|---|---|---|---|
| **HIGH iv_rank** (rich puts / carry priced) | 888 | **+0.0049** | 0.53 | 0.30 | **+0.232** | +0.0037 |
| **LOW iv_rank** (cheap puts) | 887 | **+0.0065** | 0.56 | 0.41 | +0.150 | +0.0086 |
| ALL S1 | 1,775 | +0.0057 | 0.55 | 0.35 | +0.191 | +0.0060 |
| IV terciles (low/mid/high) | — | +0.0070 / +0.0028 / +0.0074 | — | — | +0.120/+0.206/+0.247 | — |

**Read:** the S1 short excess **does not vanish in high-IV-rank (rich-put) names** (+0.49% mean, +23pp
excess-hit) — so it is mostly a genuine *equity/relative-weakness* phenomenon, not pre-priced put richness.
The mean and median are *modestly* larger in low-IV (cheap-put) names (+0.65%/+0.0086 vs +0.49%/+0.0037),
the direction carry-leakage predicts, but the effect is small and non-monotone.
**Hardening rule:** prefer to express S1 as an **equity/relative short or in lower-IV-rank near-low names**
(cheaper puts, slightly larger edge); do not overpay for rich puts on high-IV-rank near-low names. The
carry-leakage concern is **real but not disqualifying** — S1 keeps its HIGH-confidence status.

## 6.4 S1 hardening (2): crash guard remains **theory-based, unsampled** (PR-2 open)
The `s1_standdown` guard (suppress S1 shorts in a V-rebound/junk-rally/squeeze) fired on 6/54 days and the
lanes stayed positive — but the sampled window contains **no real momentum-crash** (the +12.8% April melt-up
is in the export gap). So the guard is calibrated to *theory* (Daniel-Moskowitz), not to a backtested
inversion. **Keep it conservative** (current `ret5>2.5%`, or `>1.5%` off a recent dip). PR-2 (validate the
guard through a real V-rebound) is the single most important open test and **needs new data (§6.5).**

## 6.5 Panel-extension scope (the #1 limitation)
Sign-stability across A/B1/B2 is *sub-windows of one 3.5-month episode* (`RESEARCH/30 §3.2`) — it rules out
local beta, not period-specific factor exposure. To make any edge claim **cross-year durable**, collect UW
exports covering, at minimum:
1. **The April 2026 gap** (2026-03-30 → 04-24) — fills the strong-rebound/melt-up regime; **directly
   backtests the S1 crash guard (PR-2)** and the long lanes in a rip. *Cheapest, highest-value add.*
2. **≥1 VIX>30 vol-shock episode** — the 0DTE-VRP / short-vol **left tail is currently unsampled**; the vol
   book cannot be promoted past advisory without it (`vol-book.md` promotion bar).
3. **≥2 prior calendar years** of contiguous exports incl. **a sustained drawdown / bear leg** — the sampled
   selloffs (A −4.3%, B2 −3.4%) are short; cross-year is the real durability test.
Until (1)–(3) exist, every edge stays labeled provisional and the half-cap sizing discipline holds.

## 6.6 Net effect on the migration
- **PR-1 decided** → `sector-rotation-strategist` cut is now evidence-backed, not just "untested." (Tightens D2.)
- **S1 carry small** → the anchor edge is sturdier than Phase 3 feared; express in equity/low-IV. (Strengthens D2/D4.)
- **PR-4/PR-2 need data** → keep the half-cap (D5) and the conservative crash guard until the panel extends (§6.5).
- Nothing here changes the staged plan; it raises confidence in the cuts and the anchor edge, and sharpens what to collect next.
