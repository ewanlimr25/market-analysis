# Regression gate — baseline history & isolation-check protocol

Full detail behind `CLAUDE.md` invariant #6 (**regression gate is law**). Keep this file in sync whenever
the baseline moves; `CLAUDE.md` should only ever carry the *current* baseline numbers and a pointer here.

## Current baseline

Adopted **2026-08-22** on the **FULL liquid universe** (panel→08-21, 93 days, 2,471-ticker spine),
**post-OI_FADE-full-window fix**:

| Lane | Mean excess | n | Move vs 08-17 baseline | Attribution |
|---|---|---|---|---|
| MOM_LONG | −0.0118 | 1213 | +0.0009 | panel growth only (code identical) |
| MOM_SHORT | −0.0138 | 830 | −0.0001 | panel growth only |
| **OI_FADE** | **+0.0013** | **1177** | **−0.0025** | **CODE — full-window fix, see below** |
| S2 | +0.0018 | 1269 | +0.0004 | panel growth only |
| S4 | +0.0024 | 1304 | −0.0001 | panel growth only |

`python3 scripts/retro_harness.py --all` must show no lane below its recorded baseline after any
lane/threshold change. **Every baseline is only meaningful against the universe it was measured on — state
the spine size whenever you record one.**

**Why the table was re-pointed at all.** The 08-22 audit deliberately did *not* re-baseline on panel
growth (see the unwind worked example below) — but a **code** change forces it, because post-fix code
cannot be graded against a pre-fix baseline. Only OI_FADE moved by code. The other four are the 89→93-day
panel increment and nothing else, proven by the old-code/new-data control on the identical 93-day panel
*before* the patch: MOM_LONG −0.0118 (1213) · MOM_SHORT −0.0138 (830) · **OI_FADE +0.0029 (1237)** ·
S2 +0.0018 (1269) · S4 +0.0024 (1304). All four non-OI_FADE lanes are **bit-identical pre- and
post-patch** — isolation check (c) passing.

> ⚠️ **Carried forward: this panel increment is a 4-exit-day correlated draw, the mirror of the two
> before it.** MOM_LONG's +0.0009 and S2's +0.0004 are that draw unwinding, **not** lanes improving —
> see [the worked example](#worked-example-2026-08-22-the-pre-registered-unwind-arrived). Do not credit
> any change with them, and do not read OI_FADE's −0.0025 as decay: it is
> [artifact removal](#solid-the-baseline-carried-a-panel-edge-artifact-fixed-re-baselined).

> ⚠️ **OI_FADE no longer sizes** (demoted to advisory 2026-08-22; stood down to diary-only 08-29;
> **restored to advisory 2026-09-05** when its re-check fired on outcome 2). Its corrected +0.0013 is
> indistinguishable from zero (79 `lane-exit-day`, p=0.767), so **no lane in the book currently sizes.**

> ⚠️ **The spine this baseline was measured on (2,471) is retired.** The live priced spine is 2,443 as
> of 2026-09-02. The baseline is deliberately not re-pointed; see [the spine
> move](#the-spine-moved-again-2471--2443-priced-2026-09-05) for the attribution and for why check (c)
> must be re-run before citing any pre-09-02 lane *or gate* figure.

### Prior baseline (2,471-ticker spine, panel→08-17, 89 days, superseded 2026-08-22)

MOM_LONG −0.0127 (1154) · MOM_SHORT −0.0137 (830) · OI_FADE +0.0038 (1176) · S2 +0.0014 (1210) ·
S4 +0.0025 (1241) — post-`S4_MIN_CALL_VOLUME` fix.

### S4 re-baseline: +0.0041 → +0.0025 (2026-08-17) — artifact removal, not decay

S4's drop is **code-attributable and intentional**, and it is the one baseline move in this file's history
that is a lane getting *more honest* rather than a lane getting worse.

The old option-liquidity filter was `call_volume > 0 AND put_volume > 0 AND call_volume+put_volume >= 1000`.
The combined floor puts **no constraint on the call leg**: NWG cleared it on 2026-08-17 with **3 call
contracts against 2,046 puts**, printing **PCR 682** and ranking #1 in the lane. TNGX (32 calls), SAN (66),
AMRZ (68), HST (90), JAZZ (63) were the same failure. This was never a marginal contamination — across the
panel the **median S4 selection carried 154 call contracts** (p25 = 66, p10 = 20; 64% under 250).

`S4_MIN_CALL_VOLUME = 250` was chosen on **ratio-stability** grounds — below it a single contract moves PCR
by >0.5%, and at call_volume = 3 one contract moves it by 200+. It was explicitly **not** chosen to maximise
measured excess. The sensitivity runs monotonically *against* the fix:

| call-volume floor | mean excess | hit − base | median |
|---|---|---|---|
| 1 (old) | +0.0048 | −0.041 | +0.0034 |
| 100 | +0.0030 | −0.046 | +0.0025 |
| **250 (shipped)** | **+0.0025** | **−0.056** | **+0.0009** |
| 500 | +0.0027 | −0.062 | −0.0000 |
| 1000 | +0.0009 | −0.081 | −0.0021 |

Two things this makes explicit, both of which should shape how S4 is read from now on:

1. **The artifact names were carrying the lane's apparent edge.** Removing them lowers the mean. The
   +0.0041 was not a measurement of "fading an over-hedged crowd" — for most picks PCR was numerically
   meaningless.
2. **`hit − base` was already negative before the fix** (−0.041) and gets more negative after (−0.056).
   S4 has never had a hit-rate edge on this panel; its positive mean is a right tail. That is consistent
   with the lane's own documented status (advisory, never sizes) and is a reason to keep it there.

Note the floor **swaps** selections rather than removing them — selection is top-15-by-PCR, so raising the
floor backfills with the next-highest passing names and `n` *rises* (1225 → 1241). Do not read the n change
as added coverage.

**Paired-site requirement.** `retro_harness.py` re-implements the lane gates inline and imports nothing, so
this fix had to land in **both** `scripts/retro_harness.py` (`S4_MIN_CALL_VOLUME`) and
`.claude/agents/sentiment-contrarian.md`. Patching only the lane would have left the live engine more
permissive than the instrument grading it.

### Prior baseline (2,471-ticker spine, panel→08-14, 88 days, superseded 2026-08-17)

MOM_LONG −0.0122 (1121) · MOM_SHORT −0.0140 (828) · OI_FADE +0.0037 (1159) · S2 +0.0011 (1185) ·
S4 +0.0041 (1202)

### Earlier baseline (2,471-ticker spine, panel→08-07, superseded 2026-08-15)

MOM_LONG −0.0108 (1066) · MOM_SHORT −0.0128 (803) · OI_FADE +0.0059 (1087) · S2 +0.0009 (1123) ·
S4 +0.0035 (1145)

Same spine, same code (`git diff 711adb7 HEAD` over `retro_harness.py`, `_regime.py`, `_calendar.py`,
`_env.py`, `truthset/` is **empty**), so this move is pure panel growth. Isolation check (b) reproduces it:
rows matured by the 08-07 edge print −0.0107 / −0.0131 / **+0.0059** / +0.0008 / +0.0027. **OI_FADE — the
only lane that sizes — reproduces exactly**, so its headline drop (+0.0059 → +0.0037) is entirely the
5-exit-day increment (−0.0286 over 74 rows, base 0.00) and not decay.

**Two consecutive baselines have now been set inside the same rally.** When it unwinds all five lanes will
rise together; that is the artifact releasing, not a fix landing. Do not credit any change with it.

## Prior baseline (785-ticker spine, superseded 2026-08-08)

MOM_LONG +0.0008 · MOM_SHORT −0.0043 · OI_FADE +0.0054 · S2 +0.0007 · S4 +0.0039
(n = 506 / 351 / 1050 / 559 / 396)

Measured on `universe.json` hand-frozen at **785** tickers on 2026-06-28 — an activity-ranked subset, not
the tradeable universe — while `build_features.py` used the live screener spine, leaving **1,688 feature
tickers with no price row at all** (`build_prices.py` read the frozen list; the correlation-cluster gate
went blind on absentees and returned an empty result that read as a pass). Refreshing the spine to the
full liquid screener universe (`scripts/truthset/build_universe.py`,
2,471 tickers, prices 783→2,449) roughly doubled every lane's n and is the entire cause of the change.

**This was a third kind of baseline move** — not a code regression, not panel growth, but a universe
expansion — and it was isolated the same way: the same new code re-run against the old 785 reproduced all
five lanes to the last digit (isolation check (c) below).

## What the 2026-08-08 universe expansion revealed, and what it did not

- **OI_FADE — the only lane that sizes — is unmoved** (+0.0054 → +0.0059) on +37 rows. Heavy call-OI build
  concentrates in names already inside the old 785, so tripling the universe barely touched it. That is a
  genuine robustness result and the strongest evidence the lane is not a subset artifact.
- **S2 and S4 held their means while n doubled** (+0.0007→+0.0009, +0.0039→+0.0035). Both advisory-only.
- **Both momentum legs carry the entire drop**, and both were already unsized — so *no live sizing
  changed*. MOM_LONG +0.0008 → −0.0108 is corroborating evidence for what the forward book already said
  (BH(0.10) negative, −4.65%, p=0.008). MOM_SHORT's mean deepened −0.0043 → −0.0128, and more importantly
  its **hit−base collapsed +0.162 → +0.029**: the "wins often, loses big" consolation was itself a subset
  artifact. On the full universe the lane barely beats its own base rate. Treat the +16.2pp hit−base figure
  wherever it still appears in prose (including older `analyses/` entries) as superseded.

## Isolation-check protocol

**The baseline is panel-dependent — re-verify it before reading a dip as a regression.** The pooled mean
moves on its own as the panel grows, because a signal day only enters the aggregate once its h-window
matures. Three checks, run from `analyses/audit/<date>/harness_split.py` (all three ran 2026-08-08):

**(a) old code, new data** — `git show <baseline-commit>:scripts/retro_harness.py` run against the current
panel must reproduce all five lanes. At 2026-08-08 this was stronger than behavior-preserving: `git diff
de91fe9 HEAD` over `retro_harness.py`, `_regime.py`, `_calendar.py`, `_env.py` was **empty**, so there was
no refactor to clear at all (the `_regime.py` extraction in `374b20d` and the `hz_end()` →
`scripts/_calendar.py` move at `4ec89dc` were each cleared this way when they landed).

**(b) cohort split by maturity edge** — rows that had matured at the old 07-31 edge still reproduce the
prior baseline to the last digit:

| Commit | MOM_LONG | MOM_SHORT | OI_FADE | S2 | S4 |
|---|---|---|---|---|---|
| `2b32bad` (first recorded) | +0.0018 | −0.0003 | +0.0070 | +0.0006 | +0.0044 |
| `4ec89dc` | +0.0018 | −0.0003 | +0.0070 | +0.0006 | +0.0044 |
| `de91fe9` | +0.0023 | −0.0008 | +0.0071 | +0.0021 | +0.0051 |

**(c) same code, old universe** — added 2026-08-08 after the spine refresh. When `universe.json` (and so
`prices.parquet`) changes, re-run the current code against the PREVIOUS ticker list; it must reproduce the
previous baseline to the last digit, which proves the delta is the added names and not the rebuild. Cheap
to do without refetching: filter the new `prices.parquet` to the old spine, rebuild returns, run the gate.

Only after the applicable checks is a below-baseline lane a real regression. **Check the spine size
first** — a baseline compared across two different universes is not a comparison at all.

## Worked example: 2026-08-08, all five lanes fell at once

This is the reference case for why the protocol exists. Both checks (a) and (b) passed, and the 190-row
increment had its `base` column **pinned at 1.00 for every long lane and 0.00 for every short** — SPY rose
in 100% of the new windows, because signal days 07-20→07-31 all exit into 08-03→08-07. Five lanes did not
independently decay; one rally out-ran all five.

**Diagnostic:** when an increment's `base` column is 0.00/1.00 rather than mid-range, it is a single
correlated draw and its true N is the count of distinct **exit-days**, not rows.

**Corollary — do not read the recovery as a fix:** when this artifact unwinds next cycle the lanes will
rise on their own, which is not evidence that any change worked.

**Sequel, 2026-08-15:** the artifact did not unwind — it *extended*. The next increment was 317 rows across
only **5 exit-days** (08-10→08-14) with the same pinned base, so two consecutive baselines are now set
inside one rally. A cycle that expected the first non-overlapping cohort got a second one-way window and
15 resolved rows instead.

## Worked example: 2026-08-15, a GATE result that was a spine artifact

The protocol's checks are usually run on lanes. This is the case that proves they must also be run on any
**gate-effectiveness** number.

The crash guard is graded by forcing it off and re-firing the lane query on the days it fired (see
`/calibration-audit` Step 4). That counterfactual was recorded at **−1.73%, p=0.010 [DURABLE]** (day-clustered
−1.86%, p=0.070) and was the strongest gate evidence in the repo — the whole of PR-2's progress. Re-run on
2026-08-15 against the *same 15 guard-days with byte-identical code*, it returned **−0.60%, p=0.237**
(day-clustered −0.68%, p=0.401).

Isolation check (c) explains it exactly:

| spine | name-days | mean | p | day-clustered | p |
|---|---|---|---|---|---|
| full 2,471 (today) | 220 | −0.60% | 0.237 | −0.68% | 0.401 |
| old 785 (what was recorded) | 164 | −1.64% | **0.002** | −1.56% | 0.057 |

Restricting to the old spine reproduces the original figure. The lane query's `LIMIT 15` now binds on days
the 785-name subset could barely fill, and **12 of 15 guard-days move less-negative** on the full universe.

**What to take from it:** the guard is not invalidated — it is still a net save (negative on both spines,
10/15 days) — but it is no longer DURABLE evidence, and the retired figure must not be re-cited. The failure
mode was procedural: the 2026-08-08 universe refresh re-measured every *lane* and no *gate*, so a subset
artifact stood as the repo's headline gate result for a full cycle. **Any measured number carries the spine
it was measured on.**

## Worked example: 2026-08-22, the pre-registered unwind arrived

The 08-08 entry closed with a **corollary written in advance**: *"when this artifact unwinds next cycle the
lanes will rise on their own, which is not evidence that any change worked."* It unwound on 2026-08-22, and
the pre-registration is what made the cycle readable. This is the reference case for **trusting a
pre-registered caveat over the fresh number**.

The 93-day panel prints MOM_LONG −0.0118 · MOM_SHORT −0.0138 · OI_FADE **+0.0029** · S2 +0.0018 ·
S4 +0.0024 — two lanes up, three flat-to-down, OI_FADE the only material mover (−9bp). All three isolation
checks pass, and decisively:

- **(a)** `git diff a4278af HEAD` over `retro_harness.py`, `_regime.py`, `_calendar.py`, `_env.py` and
  `truthset/` is **empty** — all five commits in the interval are scan/weekly journal docs. Zero code.
- **(b)** The cohort matured by the 08-17 edge reproduces the recorded baseline to **≤0.4bp on every lane**;
  **OI_FADE +0.0038 and S4 +0.0025 reproduce exactly**.
- **(c)** Spine unchanged (`universe.json` = 2,471).

The increment is ~60 rows per lane across **4 exit-days**, and its `base` column is pinned the *other way*:
**0.00 for MOM_LONG, 1.00 for both short lanes** — SPY fell in 100% of the new windows, the mirror image of
the 08-08 and 08-15 increments. Mechanically it was a narrow squeeze in high-beta call-OI names (SPCX +29%,
MSTR, PLTR, CELH, NOK, DKNG) against a flat-to-down index — which is precisely the population OI_FADE
shorts, so the lane that moved is the lane the draw was aimed at.

**What to take from it, in both directions:**

1. **MOM_LONG's and S2's rise is not a lane improving**, and no change may be credited with it.
2. **OI_FADE's −9bp is not decay** — its baseline cohort reproduces exactly, so the entire move is those
   4 exit-days.
3. A pre-registered corollary did real work here. When an increment's `base` is pinned, **write down what
   the unwind will look like** so the next cycle cannot mistake it for signal.

## MOM_SHORT: a knowingly-negative recorded exception

`2b32bad` fixed the **measuring instrument** (calendar→trading-day earnings window on all lanes; OI_FADE
had no ETP/earnings hygiene at all), exposing a lane that was always negative behind a polluted universe.
The mean moved in three real steps, each time the measuring universe got *less* flattering:

1. −0.0003 → −0.0008 on 36 mid-July rows (signal days 07-13→17, mean −0.0041) whose 52-week lows were
   Yahoo-verified genuine.
2. −0.0008 → −0.0043 on the 08-03→07 rally — a short lane measured across windows where SPY rose every
   time.
3. **−0.0043 → −0.0128 on the 2026-08-08 universe refresh**, which more than doubled its n and collapsed
   its hit−base to +0.029.

All three moves are real signal, not instrument error. **A red MOM_SHORT is the expected baseline, not a
new regression** — it is capped watch-only for new starters, so no live sizing depends on it. This is the
**ONE** recorded exception to "no lane negative-excess" in `CLAUDE.md`; do not add another lane to that
list without the same written rationale (three independent, dated, universe/instrument-driven moves, all
in the same direction).

## Which clustering unit governs a STOP flag

Added 2026-08-22, because for the first time the units **disagreed on the whole-book verdict** and nothing
in the repo said which one decides. The same 323-row forward book reads:

| unit | N | mean excess | p |
|---|---|---|---|
| naive per-name | 323 | −0.97% | 0.051 |
| declared `cluster_id`, else the name | 265 | **−0.60%** | 0.278 |
| **exit-session** (distinct exit sessions, pooled across lanes) | 35 | −2.20% | 0.054 |
| **lane-exit-day** (lane × exit-day, summed over lanes) | 95 | −1.69% | 0.022 |

⚠️ **The last two are DIFFERENT units and the repo used to call both of them "exit-day".** Named apart
2026-08-29, after an audit spent a cycle treating the 35-unit and 95-unit figures as a contradiction in
the record. They are not: re-running the 08-22 cohort reproduces **both** exactly (35 units / −2.20% /
p=0.054 pooled; 95 units / −1.69% / p=0.022 lane-wise). Definitions, binding from now on:

- **`exit-session`** — one calendar exit session is one observation, pooled across every lane. The
  strictest unit; ~3× fewer observations than the lane-wise view on the same rows. **This is the
  whole-book figure** quoted in CLAUDE.md invariant #6.
- **`lane-exit-day`** — one (lane, exit-day) pair is one observation. **This is the per-lane column**
  in every audit's `robustness.md` §(C), and it is the unit rule 3 below means by "distinct exit-day
  count", because that bar is applied per lane.

Use the names, not the phrase "exit-day", in any table or claim. Two units that share a name are two
numbers that can be swapped after the fact.

Prior cycles leaned on `cluster_id` to dissolve the naive per-name negative — correctly, but the repo's
*own* companion rule (exit-days, below) points the other way, and an undeclared choice means the reading
can be selected after seeing it. The rule, from now on:

1. **`cluster_id` (else the name) is the governing unit for a Step-3 STOP flag and for the confidence
   label.** It is the only unit consistent with how `risk-sizer.md` would actually have held the book —
   a STOP exists to stop losing money, so the unit must be the unit of risk.
2. **The `lane-exit-day` view must be reported alongside it, every cycle, for every lane** (and the
   whole-book `exit-session` figure alongside the whole-book cluster-unit figure). It is the
   independent-draw count, and it is what tells you whether the cluster-unit N is real evidence or one
   macro window wearing many names.
3. **A lane whose `lane-exit-day` count is below 30 carries an explicit correlated-draw caveat and
   cannot graduate to sizing on that evidence alone**, however many cluster-units it has. As of 2026-08-22
   *every* lane is in this state (MOM_LONG 14 · MOM_SHORT 21 · OI_FADE 22 · S2 20 · S4 18 exit-days), which
   is the honest description of the forward book: it is roughly 20 independent windows, not 265.
4. **Never report one unit alone.** A single-unit number is not wrong, it is unfalsifiable.

This does not change any lane's current status: no lane clears BH(0.10) under *any* of the three units, so
the 2026-08-22 verdict is "no STOP" on all of them. It fixes the case where they diverge.

## Exit-day counting (companion rule)

Applies whenever grading a cohort, not just the 2026-08-08 event: **a cohort's N is its count of distinct
exit-days, not its count of rows.** Rows whose h-windows overlap share one macro draw. On 2026-08-08 the
long-awaited post-fix h10 cohort turned out to span **3 exit-days** (08-04/05/06, SPY up in all three), so
its 19 rows could not grade the engine at durable N — and it dissolved a false positive: MOM_SHORT's
per-name p=0.039 became p=0.134 once clustered by exit-day. Report exit-day counts next to every cohort N,
and never let a single-window print — in either direction — change a lane's size or status.

## Re-signal dedup caps a lane's forward N (structural, not bad luck)

Added 2026-08-22, after the third consecutive cycle in which "the first genuinely non-overlapping OI_FADE
cohort" was scheduled and did not arrive. It was never going to arrive by waiting, and the reason is
mechanical rather than meteorological.

The audit resolver collapses a `(ticker, lane, direction)` re-signal that lands **inside a live prior
window** — correctly: a name re-signalled on consecutive scan days is one ongoing position with overlapping
h-windows, not N independent trades. But OI_FADE fires on *persistent multi-day call-OI building*, so its
strongest candidates re-signal **every session for as long as the build continues**. PLNT signalled on 12
consecutive sessions (2026-07-20 → 08-03); dedup keeps the first of each chain, so those 12 rows became
**2 cluster-units**.

The consequence, measured on 2026-08-22: five OI_FADE rows matured during the cycle (PLNT +11.94%,
INFY +7.12%, PLNT +4.16%, AVTR +3.22%, HRI −3.63%; mean **+4.6%**) and **all five were deduped away**.
OI_FADE's forward book was frozen at ~80 cluster-units across a full cycle, and its 11 OPEN rows are only
7 distinct names. **A runner contributes ~2 units however long and however profitably it runs.**

Three things follow:

1. **Do not schedule "the non-overlapping OI_FADE cohort" as a matter of waiting.** Its unit growth is
   capped by its own signal shape, and the cap tightens the better the lane's thesis works.
2. **The dedup is not biased** — it keeps the *first* signal of a chain, not the best or worst (PLNT's kept
   rows were −4.30% and +9.68%, while the dropped ones ran +11.9% to +20.0%). It is lossy, not skewed.
   Do not "fix" it by keeping the best row.
3. **The honest alternative is to measure the lane at the POSITION level** — entry→exit as the book
   actually held it — rather than at the signal level. That is a different measurement, not a bug fix, and
   it is what `PR-9` already pre-registers for S4 entry timing. Until then, read OI_FADE's forward N as
   "~2 units per runner" and size nothing on its growth rate.

## OI_FADE: the baseline carried an artifact, and the rules are NOT distinguishable (2026-08-22)

`retro_harness.py --all --oi-variant both` exists because the only lane that **sized** was being
graded by a rule the engine does not run. Two conclusions, one solid and one a retraction.

### Solid: the baseline carried a panel-edge artifact (FIXED, re-baselined)

`oi_net_5d` is `avg(oi_net_cp) OVER (ROWS BETWEEN 4 PRECEDING AND CURRENT ROW)`, and `avg()` does
**not** require five observations: a partial window divides by k<5 and inflates the name into the
top-15. On the 93-day panel **75 of 1,237 resolved rows (6.1%) had a partial window and carried
mean +0.0277**, against **+0.0013** for full-window rows. **60 of those 75 are the panel's FIRST
FOUR DAYS** (2026-03-13→03-18), where the feature is not yet defined at all — 15 names × 4 days,
one correlated draw at the left edge. Paired by exit-day the artifact is worth **+0.0021,
p=0.018**.

The lane now joins the full-window panel. **OI_FADE re-baselines +0.0029 → +0.0013** on the
93-day panel. This is **artifact removal, not decay** — the same category as the S4 call-volume
floor, and like it, the removed rows were supplying the right tail. `hit − base` is *unharmed*
(+0.155 → +0.184) and the lane stays positive in all three regimes (CHOP +0.0023 / PULLBACK
+0.0014 / UPTREND +0.0001), so what was removed was mean, not hit-rate.

### Retraction: the "live rule grades worse" finding was measured on a misspecified pool

The first cut of this comparison reported the live rule at **−0.0076, p=0.014 on 79 exit-days**
and concluded the live lane's ranking was measurably harmful. **That counterfactual omitted the
live lane's own fail-closed floors** (`.claude/agents/oi-flow-fade.md`: net build ≥ 1,000
contracts, `avg_30_day_call_oi` ≥ 1,000, exclude listings younger than ~60 trading days). It
required only `acoi > 0`, re-admitting the precise tiny-base artifact the lane exists to exclude.
Faithfully floored:

| selection (all on the live lane's own floored pool) | n | exit-days | mean | p |
|---|---|---|---|---|
| `oi_rel_build` + persistence gate (**the LIVE lane**) | 360 | 24 | **−0.0081** | 0.080 |
| raw `oi_net_5d` rank, same pool | 360 | 24 | **−0.0093** | — |
| `oi_rel_build`, persistence gate OFF | 360 | 24 | −0.0125 | 0.005 |

Three corrections follow, and they reverse the original reading:

1. **Raw ranking is not better than `oi_rel_build`** — on the live lane's own pool it is *worse*
   (−0.0093 vs −0.0081). **No rule switch is warranted**, and none was made.
2. **The persistence gate HELPS**, it does not hurt (−0.0125 → −0.0081). The earlier "the gate
   costs 24bp" reading was an artifact of the unfloored pool.
3. **The live rule's negative is PROVISIONAL, not DURABLE** — 24 exit-days at p=0.080, not 79 at
   p=0.014. Under this file's own rules that is not actionable evidence.

What actually differs between the +0.0013 baseline and the −0.0081 live measurement is **the
pool, not the ranking**: the live lane's floors cut 1,177 rows to 360, and that floored subset
measures negative. Whether those floors help or hurt is now the open question — they were adopted
to remove a real artifact (JPST's "6.67× build" off 12 contracts), so they cannot simply be
dropped, and 24 exit-days cannot settle it.

**Procedural lesson, and it is the same one as 2026-08-15:** a counterfactual must re-implement
the gate's *actual* floors. Grading a rule you did not faithfully reproduce measures nothing, and
it took a near-miss lane change to catch. Re-read the lane spec before writing the counterfactual,
not after.

### Where this leaves the lane

**No OI_FADE variant has a validated positive edge.** Corrected baseline +0.0013 (79 `lane-exit-day`,
p=0.767) is indistinguishable from zero; the live lane's floored measurement is −0.0081 at
PROVISIONAL N. OI_FADE is therefore **demoted from sizing to advisory** (2026-08-22) — see
[`lanes.md`](lanes.md). That is a consequence of "no validated edge", not of the retracted
finding.

> **Superseded 2026-08-29.** One cycle later `OI_FADE_LIVE` reads −0.0093 at 29 `lane-exit-day`,
> **p=0.028, surviving BH(0.10)** — no longer "indistinguishable from zero" but significantly
> negative, and robust to dropping the crypto names that moved the pooled baseline. The lane is
> **stood down to diary-only**; see
> [OI_FADE_LIVE is significantly NEGATIVE](#oi_fade_live-is-significantly-negative--lane-stood-down-to-diary-only-2026-08-29).

### PR-10 — the rank band (pre-registered 2026-08-22, NOT scored)

The signal is not in the extreme top of the ranking. On the full-window pool, raw rank:

| band | n | mean | exit-day mean | p |
|---|---|---|---|---|
| ranks 1–15 (the shipped cut) | 1177 | −0.0004 | −0.0003 | 0.948 |
| ranks 16–30 | 1184 | +0.0044 | +0.0044 | 0.376 |
| **ranks 31–60** | 2359 | **+0.0093** | +0.0094 | **0.054** |
| ranks 1–50 | 3936 | +0.0052 | +0.0052 | 0.212 |

This matches both documented artifacts at once — raw's extreme top is a mega-cap beta short,
`rel_build`'s extreme top is tiny-base noise, and the signal sits below both. **It is NOT scored:**
p=0.054 **fails BH(0.10) across the five bands tested** (cut = 0.02), and the band was chosen after
seeing the result, so it is in-sample by construction. It graduates only on data postdating
2026-08-22. Do not size it, and do not re-cut the live lane to it.

**Accrual, 2026-08-29: 0 out-of-sample rows, and none was possible yet.** A signal dated after
2026-08-22 needs 10 trading sessions to mature and the panel edge is 08-28, so the earliest PR-10
evidence exits ~2026-09-08. Recorded so the next cycle does not re-derive it: **PR-10 cannot advance
before then, and the absence of evidence is arithmetic, not a null result.**


## OI_FADE_LIVE is significantly NEGATIVE — lane stood down to diary-only (2026-08-29)

> **SUPERSEDED 2026-09-05.** The re-check below fired on **outcome 2**: at 34 `lane-exit-day`
> `OI_FADE_LIVE` reads −0.0065, p=0.0929, and **fails BH(0.10)**. The lane is back to **advisory**.
> Two things here did not survive and must not be re-cited: the p=0.028 headline (it was an
> **uncorrected** statistic — Newey-West reads 0.143 on this very cohort), and the ex-trio robustness
> claim (−0.0070 → −0.0045, p=0.218). Kept for the diagnosis of the *raw pool*, which still holds.
> → [the re-check](#the-oi_fade_live-re-check-fired-on-outcome-2--lane-restored-to-advisory-2026-09-05)

The 2026-08-22 cycle demoted OI_FADE from sizing to advisory on "no variant has a validated positive
edge". One cycle later the finding is stronger and its sign is no longer ambiguous: **the rule the
engine actually runs is significantly negative.**

98-day panel (2026-03-13 → 08-28), `retro_harness.py --all --oi-variant both`:

| variant | n | pooled | `lane-exit-day` | p | ex-MSTR/CELH/MARA | baseline cohort (exit ≤ 08-21) |
|---|---|---|---|---|---|---|
| `OI_FADE` (raw rank, full pool) | 1252 | −0.0018 | 84 | 0.707 | **+0.0011 — sign flips** | +0.0013 / 79 / p 0.767 ✅ exact |
| **`OI_FADE_LIVE`** (`oi_rel_build` + persistence) | 435 | **−0.0093** | **29** | **0.028** | −0.0070 — holds | −0.0081 / 24 / p 0.080 ✅ exact |
| `OI_FADE_RAWPOOL` (raw rank, live pool) | 435 | −0.0166 | 29 | 0.008 | −0.0074 — holds | −0.0093 / 24 |

**`LIVE` and `RAWPOOL` both survive BH(0.10)** across the three variants. Every recorded post-fix
figure reproduces **bit-exactly** on the baseline cohort, so the move from p=0.080 to p=0.028 is new
rows, not code — isolation checks (a), (b) and (c) all pass (`git diff 6cceae8 HEAD -- scripts/
.claude/agents/` is empty; spine unchanged at 2,471).

**Why this is not the same finding as the pooled baseline crossing zero.** `OI_FADE`'s pooled figure
went +0.0013 → −0.0018 this cycle, but that is **three tickers**: MSTR, MARA and CELH signalled on five
consecutive sessions (08-10 → 08-14) into one crypto squeeze, contributing 14 of the increment's 75
rows. Drop those three names from the whole 98-day panel and OI_FADE returns to **+0.0011**. The pooled
baseline is therefore *not* evidence of decay and **must not be re-baselined**. `OI_FADE_LIVE` is
different: removing the same three names leaves it at −0.0070. Its negative sign does not depend on any
small set of names.

**Consequence — the lane is STOOD DOWN to diary-only.** It no longer emits a watch list. Prior status
("advisory, emits watch-only candidates") presented a ranked list of shorts every night from a rule now
measured as significantly negative; a watch list is an implicit suggestion, and invariant #1 does not
have a category for "suggest a name from a rule we have measured as losing". The lane still **runs and
is still documented** in the nightly journal — the numbers, the gates and the cuts are diary material.

**This does not starve the test.** `retro_harness.py` fires its own lane query independent of the agent,
so the historical evidence keeps accruing at ~5 `lane-exit-day` per week whether or not the lane emits
candidates. That is the opposite of the crash-guard problem (a gate that suppresses its own evidence).

**Re-check bar.** `OI_FADE_LIVE` is at **29 `lane-exit-day`, one short of the 30 that makes it DURABLE.**
At the next audit it will cross. Two outcomes are pre-registered here:

- **Still negative and BH-significant at ≥30 `lane-exit-day`** → this becomes a formal Step-3 STOP and
  the second recorded exception alongside MOM_SHORT, with the same written rationale.
- **Reverts to indistinguishable-from-zero** → the p=0.028 was the 5-exit-day pinned-base increment
  leaking in, and the lane returns to advisory. Note the increment's `base` was pinned 1.00 for shorts
  (SPY down in 100% of the new windows), so a short lane losing in it is the harder read, not the easier.

Do not re-cut the ranking in the meantime; see PR-10 below.

## The 2026-08-22 suppression result did not replicate (2026-08-29)

> **Extended 2026-09-05:** it failed a *second* re-test — 49 lane-periods, −0.53%, **p=0.194**. The
> trajectory is monotone toward zero. → [the MOM_LONG
> leg](#the-mom_long-suppression-leg--pre-registered-re-check-at-25-baskets-2026-09-05)

Recorded 08-22: gate discipline was "**significantly** negative for the first time" at **21 lane-periods,
−1.74%, p=0.008 [PROVISIONAL]**. At 57% more baskets it is **33 lane-periods, −0.89%, p=0.054**, and no
lane survives BH: MOM_LONG 11 baskets −1.62% (p=0.124), MOM_SHORT 12, −0.67% (p=0.338), OI_FADE 10,
−0.36% (p=0.597). Resolved candidate-rows went 121 → 195; 102/195 correct.

The 08-22 write-up already flagged the same shape one level down — "the earlier 19/22 (86%) hit-rate was
flattering — it is 59% at 5× the sample" — and then leaned on the pooled p=0.008 anyway. **A gate-
effectiveness result at PROVISIONAL N is a hypothesis, and this one did not survive its first re-test.**
Gate discipline remains directionally right (negative at every N measured so far) and no gate should be
removed on it; it is simply not significant, and the 08-22 figure must not be re-cited.

## The `OI_FADE_LIVE` re-check fired on OUTCOME 2 — lane restored to advisory (2026-09-05)

The 2026-08-29 stand-down pre-registered a re-check at **30 `lane-exit-day`** with two outcomes. The
2026-09-05 audit adjudicated it. **Outcome 2 fired: `OI_FADE_LIVE` is no longer BH-significant, and the
lane returns to advisory** (watch-list only — advisory has never sized, and no lane sizes).

**Partial-window check first**, because this lane has already had a `lane-exit-day` count move its p
across the pre-registered line once (2026-09-01). `OI_FADE_LIVE` and `OI_FADE_RAWPOOL` are at **34
complete units, ZERO partial** — every unit resolved 15/15, verified fired-vs-resolved. (Raw `OI_FADE`
carries 8 partial units at 14/15; all are historic — May and late June — not the maturity edge.)

103-day panel (2026-03-13 → 09-04), `retro_harness.py --all --oi-variant both`:

| variant | n | pooled | `lane-exit-day` | p | **NW p (L=9)** | ex-trio | ex-trio p | baseline cohort (exit ≤ 08-21) |
|---|---|---|---|---|---|---|---|---|
| `OI_FADE` (raw rank, full pool) | 1327 | −0.0014 | 81 | 0.506 | 0.714 | **+0.0005 — flips** | 0.916 | −0.0003 / 71 |
| **`OI_FADE_LIVE`** (shipped) | 510 | **−0.0065** | **34** | **0.0929** | **0.290** | −0.0045 | 0.218 | **−0.0081 / 24 / p 0.080 ✅ bit-exact** |
| `OI_FADE_RAWPOOL` | 510 | −0.0133 | 34 | 0.0148 | 0.025 | −0.0042 | 0.342 | −0.0093 / 24 |

**BH(0.10) across the three variants: only `RAWPOOL` survives** (0.0148 ≤ 0.0333). `OI_FADE_LIVE` fails
at rank 2 (0.0929 > 0.0667) — the exact test the stand-down cited. `RAWPOOL` is **not** the shipped rule
and does not govern.

Three supports for outcome 2:

1. **Monotone decay across seven consecutive units**, recomputed from the panel rather than quoted from
   the nightlies: k=28 p=0.0202 · **k=29 (stand-down) p=0.0280** · k=30 p=0.0227 · k=31 0.0290 ·
   k=32 0.0402 · k=33 0.0457 · **k=34 (now) 0.0929**. Five of the last ten complete units are positive;
   09-04 alone (+0.0315) moved p from 0.0457 to 0.0929.
2. **The crypto-robustness argument has eroded.** The 08-29 record's key claim was that `LIVE`, unlike
   the raw pool, did not depend on a few names (ex-MSTR/CELH/MARA −0.0070). It now reads **−0.0045,
   p=0.218**. The 08-29 diagnosis of the *raw pool* still holds and still must not be re-baselined:
   dropping the trio returns pooled `OI_FADE` to **+0.0017**, and those three carry 92% / 77% / 54% of
   the pooled sum on 19 increment rows.
3. **The mechanism matches the pre-registration.** Outcome 2 predicted p=0.028 was the pinned-base
   increment leaking in. The increment's short `base` has unpinned 1.00 → 0.80, and `LIVE`'s
   post-baseline mean is −0.0024 against −0.0081 on the baseline cohort.

**The sign is unchanged and stays visible.** Every cut is still negative. Outcome 2 says the lane is not
*significantly* negative; it does not say the lane is good. Advisory = watch list, never sizing.

### `OI_FADE_LIVE` never survived the h10 overlap correction — at any k

The stand-down rested on "significantly negative and survives BH(0.10)" at p=0.028. That p is
**uncorrected**. h10 windows share 9/10 of their days, and `lane-exit-day` clustering does not fix window
overlap — only the unit. Newey-West (L=9) on the exit-day mean series gives:

| k | uncorrected p | **NW p** |
|---|---|---|
| 29 (the stand-down) | 0.0280 | **0.143** |
| 30 (the bar) | 0.0227 | **0.128** |
| 34 (now) | 0.0929 | **0.290** |

`OI_FADE_LIVE` was **never** BH-significant under the correction this repo already documents — not at the
stand-down, not at the bar, not now. **The evidence the lane was stood down on did not survive it.**
Report NW alongside the clustered p for every h10 lane figure from here; the clustered t is an upper
bound on significance, not the answer.

### The re-check's form was the defect, not the lane

The bar was a **count** (30 `lane-exit-day`) but the evaluation was a **date** ("at the next audit"),
which arrived four units later. At k=30 — exit-day 08-31, the session the bar was actually crossed — the
same test read **p=0.0227 and outcome 1 would have fired.** A fixed-k bar adjudicated on a drifting
calendar lets the tape between the bar and the audit pick the answer, and it is optional stopping in
whichever direction that tape moved.

**Standing rule (2026-09-05): a pre-registration whose bar is a COUNT must name a count trigger.** Write
the evaluation point as *"the first cycle at which k ≥ N"*, or state an explicit window (*"evaluated on
the first 30 units, later units excluded"*), or state that the test is re-run at every cycle past the bar
and requires the result to hold at all of them. Never *"re-check at N units, at the next audit"* — those
are two different events and they disagreed here by a factor of four in p. Applies to every open PR-* item.

Outcome 2 is nevertheless the right call, because the NW reading above is **independent of where you
stop**: the lane fails at k=29, k=30 and k=34 alike.

## The MOM_LONG suppression leg — pre-registered re-check at 25 baskets (2026-09-05)

Pooled suppression discipline has now weakened at **two consecutive re-tests**:

| cycle | lane-periods | mean avoided exc | p |
|---|---|---|---|
| 2026-08-22 | 21 | −1.74% | **0.008** |
| 2026-08-29 | 33 | −0.89% | 0.054 |
| **2026-09-05** | **49** | **−0.53%** | **0.194** |

Monotone toward zero at 2.3× the original sample; 158/335 rows correct (47%, from 52%). The 08-22 figure
is now twice-failed and must not be re-cited in any form.

**One leg moved the other way, and it is a hypothesis, not a finding.** Per lane at 2026-09-05:

| lane | baskets | mean avoided exc | p | BH(0.10) |
|---|---|---|---|---|
| **MOM_LONG** | 15 | **−1.78%** | **0.028** | **SIGNIF** |
| MOM_SHORT | 18 | −0.53% | 0.269 | ns |
| **OI_FADE** | 16 | **+0.65%** | 0.433 | ns — suppression has **COST edge** |

MOM_LONG went 11 baskets/−1.62%/p=0.124 → 15 baskets/−1.78%/p=0.028. It is **PROVISIONAL at 15 baskets**
and falls under exactly the rule that has now killed the pooled result twice.

**Pre-registered: re-check MOM_LONG suppression at 25 baskets, evaluated at the FIRST cycle at which the
basket count reaches 25** (the count trigger required above — not "at some later audit"). Outcomes:

- **Still negative and BH-significant at ≥25 baskets** → the first replicated gate-effectiveness result in
  the repo; record it as evidence the MOM_LONG basket suppression is doing real work.
- **Reverts to non-significant** → the same PROVISIONAL-N mirage as the 08-22 pooled result, twice over,
  and the pooled trajectory is the honest read.

Either way, **no gate is removed on this** — a gate's value is insurance against the regime not yet in the
data, and OI_FADE's +0.65% is the reason to keep reporting the legs separately rather than pooling them.

## The spine moved again: 2,471 → 2,443 priced (2026-09-05)

Isolation check (c) was **not** required at 08-29 (spine unchanged) and **was** required this cycle:

- **priced spine 2,471 → 2,443** (`prices.parquet` / `returns.parquet`)
- **features spine 2,471 → 2,499** (`features.parquet`)
- **56 tickers are in `features` but not in `prices`** — they are selected into a lane's top-15 off
  features, then fail to resolve against returns, so they silently drop out of the aggregate.

Cause is the documented non-idempotent vendor feed, not a screener/universe decision. Selection-level
attribution reconciles the baseline-cohort deficit **exactly**, which is what makes it attrition rather
than decay:

| lane | selected in baseline window | − lost to the 56 unpriced | − other unresolved | = resolved now | recorded baseline |
|---|---|---|---|---|---|
| MOM_LONG | 1245 | 24 | 13 | **1208** | 1213 |
| MOM_SHORT | 832 | 2 | 4 | **826** | 830 |
| OI_FADE | 1185 | 8 | 0 | **1177** | **1177 ✅ bit-exact** |
| S2 | 1315 | 14 | 44 | **1257** | 1269 |
| S4 | 1320 | 9 | 8 | **1303** | 1304 |

Means moved ≤4bp; OI_FADE and S4 reproduce exactly. **Not a regression, and the baseline is NOT
re-pointed** — the recorded baseline keeps its own 2,471 spine, which is precisely why the spine must be
stated next to it.

⚠️ **Any lane or gate figure measured before 2026-09-02 carries the retired 2,471 spine.** Re-run check
(c) before citing one, exactly as the [2026-08-15 gate-vs-spine worked
example](#worked-example-2026-08-15-a-gate-result-that-was-a-spine-artifact) requires. Spine changes are
now recurring rather than one-off, so treat "the spine is unchanged" as something to verify each cycle,
not to assume.
