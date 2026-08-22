# Regression gate — baseline history & isolation-check protocol

Full detail behind `CLAUDE.md` invariant #6 (**regression gate is law**). Keep this file in sync whenever
the baseline moves; `CLAUDE.md` should only ever carry the *current* baseline numbers and a pointer here.

## Current baseline

Adopted **2026-08-17** on the **FULL liquid universe** (panel→08-17, 89 days, 2,471-ticker spine),
**post-`S4_MIN_CALL_VOLUME` fix**:

| Lane | Mean excess | n | Move vs 08-15 baseline | Attribution |
|---|---|---|---|---|
| MOM_LONG | −0.0127 | 1154 | −0.0005 | panel growth only (code identical) |
| MOM_SHORT | −0.0137 | 830 | +0.0003 | panel growth only |
| OI_FADE | +0.0038 | 1176 | +0.0001 | panel growth only |
| S2 | +0.0014 | 1210 | +0.0003 | panel growth only |
| **S4** | **+0.0025** | **1241** | **−0.0016** | **CODE — S4 call-volume floor, see below** |

`python3 scripts/retro_harness.py --all` must show no lane below its recorded baseline after any
lane/threshold change. **Every baseline is only meaningful against the universe it was measured on — state
the spine size whenever you record one.**

**Why the whole table moved together.** Only S4 changed by code. The other four are the 88→89-day panel
increment and nothing else — proven by an old-code/new-data control run on the identical 89-day panel
*before* the patch: MOM_LONG −0.0127 (1154) · MOM_SHORT −0.0137 (830) · OI_FADE +0.0038 (1176) ·
S2 +0.0014 (1210) · S4 **+0.0048** (1225). All four non-S4 lanes are **bit-identical pre- and post-patch**,
which is isolation check (c) passing. Recording only S4's new figure against the old 88-day numbers would
have mixed two spines inside one baseline line — the exact error this file exists to prevent.

> ⚠️ **This baseline was depressed by a correlated draw, and that draw UNWOUND on 2026-08-22 exactly as
> pre-registered.** The 08-15 increment was 317 rows spanning only **5 exit-days** (08-10→08-14), with
> `base` pinned at 1.00 for MOM_LONG and 0.00 for both short lanes; 08-17 added a single further exit-day.
> The 08-22 increment is its **mirror** — see
> [the worked example](#worked-example-2026-08-22-the-pre-registered-unwind-arrived). **The baseline below
> is deliberately NOT re-pointed to the 93-day panel**: re-baselining on a 4-exit-day reversal would bake
> one draw into the reference the next cycle compares against, which is the failure this file exists to
> prevent. The baseline stays at `a4278af` until a genuinely multi-window increment arrives.

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
| distinct exit-day (across lanes) | 35 | −2.20% | 0.054 |

Prior cycles leaned on `cluster_id` to dissolve the naive per-name negative — correctly, but the repo's
*own* companion rule (exit-days, below) points the other way, and an undeclared choice means the reading
can be selected after seeing it. The rule, from now on:

1. **`cluster_id` (else the name) is the governing unit for a Step-3 STOP flag and for the confidence
   label.** It is the only unit consistent with how `risk-sizer.md` would actually have held the book —
   a STOP exists to stop losing money, so the unit must be the unit of risk.
2. **The exit-day view must be reported alongside it, every cycle, for every lane.** It is the
   independent-draw count, and it is what tells you whether the cluster-unit N is real evidence or one
   macro window wearing many names.
3. **A lane whose distinct exit-day count is below 30 carries an explicit correlated-draw caveat and
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

## OI_FADE: the baseline and the live lane grade different rules (2026-08-22)

`retro_harness.py --all --oi-variant both` exists because the only lane that **sizes** was being
graded by a rule the engine does not run. The baseline ranks by raw `oi_net_5d`; the live lane
(`.claude/agents/oi-flow-fade.md`, `scripts/oi_build.py`) ranks by `oi_rel_build` and drops
single-day blocks on `persistence_ratio`. On the same 93-day panel:

| lane | selection | n | mean excess | hit−base | median |
|---|---|---|---|---|---|
| `OI_FADE` | raw `oi_net_5d`, full pool (**the baseline**) | 1237 | **+0.0029** | +0.155 | +0.0077 |
| `OI_FADE_RAWPOOL` | raw rank, live-eligible pool | 1177 | **−0.0004** | +0.179 | +0.0065 |
| `OI_FADE_LIVE` | `oi_rel_build` + persistence gate | 1171 | **−0.0076** | +0.130 | −0.0023 |

Read as two separate effects — conflating them is why the flag emits all three:

**1. Roughly half the baseline's edge is a partial-window artifact.** `oi_net_5d` is
`avg(oi_net_cp) OVER (ROWS BETWEEN 4 PRECEDING AND CURRENT ROW)`, and `avg` does **not** require
five observations: a ticker with a partial window is divided by k<5, inflating it into the
top-15. Of the baseline's 1,237 resolved rows, **75 (6.1%) have a partial window and carry mean
+0.0277**, against **+0.0013** for the 1,162 full-window rows. This is the same shape as the S4
PCR-denominator artifact — a metric whose denominator is not floored — and it was found the same
way, by asking what the ranking actually selects.

**2. On an identical pool, the LIVE rule grades WORSE than the raw rule, not better.** Ranking by
`oi_rel_build` costs ~48bp (−0.0004 → −0.0052 with the persistence gate off) and the persistence
gate a further ~24bp (→ −0.0076). The 2026-08-18 scan set out two possibilities — that the live
gates add edge and the baseline understates the live lane, or the reverse. **On this panel it is
the reverse**, for the ranking and persistence components.

**What this does and does not license:**

- It does **not** condemn the live lane. Its news/catalyst gates are **still ungraded** — the panel
  carries no news tape — and those gates have caught real defects (COKE 08-17, GEN, AZN). The
  measured comparison covers selection, not gating.
- It **does** mean the **+0.0038 prior may not be cited as validation of the lane the engine runs**.
  It grades a different selection, and on a pool whose top decile is partly an artifact.
- OI_FADE is the **only lane that sizes**, so this is the highest-priority open question in the
  repo. Neither number is currently fit to size on: the prior grades the wrong rule, and the
  forward book is frozen at ~80 cluster-units by [re-signal
  dedup](#re-signal-dedup-caps-a-lanes-forward-n-structural-not-bad-luck).
- **Do not "fix" the artifact by re-baselining to +0.0013 or to any of these figures.** They are
  one panel, and the pool restriction changes which names backfill the top-15. The next step is a
  decision about which rule the repo intends to run, not a new number.

