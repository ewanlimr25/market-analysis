# CLAUDE.md — market-analysis

> **2026-09-05: `/market-scan` and weekly Layer 2 are FROZEN** (see the banners in `.claude/commands/`). The
> decision tool is now `make daily` from `engine/` (`engine/README.md`); its S-A parameters are frozen by
> `tests/test_frozen_params.py` and its S-B parameters (DESIGN/80, added 2026-09-05 evening) by
> `tests/test_sb_frozen_params.py`, both until the read on 2026-12-01. The invariants below describe the
> frozen engine and remain the record of why it stopped.

Excess-scored, regime-first market analysis. Built from the hindsight-validated clean-room research in
`research/` (panel 2026-03-13→06-26) — **read `research/00-orientation.md` before changing any lane's
logic or gates.** Full doc index, including the history behind every rule below: [`docs/README.md`](docs/README.md).

## What this repo is (and is NOT)
- **IS:** a lean engine that scores only the handful of signals that beat SPY out-of-sample, on a conditional
  benchmark, regime-stratified. Price-structure (momentum) + one OI-fade + mean-reversion/sentiment + a
  non-directional vol book. Daily `/market-scan`, weekly `/weekly-review`, forward `/calibration-audit`.
- **IS NOT:** a microstructure flow engine. Raw options flow measured as **beta** here (`research/20`, `70`);
  it is cut, not scored. (That product is `~/Development/uw-daily-analysis`.)

## Non-negotiable invariants

1. **Excess-vs-SPY (conditional same-day benchmark) is the only scoring currency.** Never raw win-rate — the
   tape is long-biased (SPY up 58/63/68/71% at h1/3/5/10), so raw WR is beta in disguise.
2. **No additive confluence.** A name scores on ONE lane's measured excess × regime-fit. Orthogonal lanes that
   agree are noted, never summed (additive confluence produced a −8.2% / 0-for-6 book — `research/50`).
3. **Most days have no directional edge — say so.** The modal output is regime + vol book + watch list.
4. **Half-cap, no auto-full, and as of 2026-08-22 NO lane sizes at all.** No call sizes full until a
   cross-year edge validates. OI_FADE — the last lane that sized — went to advisory on 08-22 when no
   variant showed a validated positive edge. **A book that sizes nothing is the correct output of
   invariant #1 when nothing clears; it is not a defect to be worked around.**
5. **Pre-registered ≠ scored.** Weekly technicals and all PR-* items are documented, never sized, until their
   bar clears on data that postdates registration. **A bar stated as a COUNT must name a count trigger**
   ("the first cycle at which k ≥ N"), never "at the next audit" — the two are different events, and on
   `OI_FADE_LIVE` they disagreed by 4× in p ([`docs/regression-gate.md`](docs/regression-gate.md#the-re-checks-form-was-the-defect-not-the-lane)).
6. **Regression gate is law.** See below.
7. **Path-aware outcomes from the Yahoo chart API**, never the close-only `mcp__yahoo-finance__*` tools.

## Invariant #6 — the regression gate

`python3 scripts/retro_harness.py --all` must show no lane **below its recorded baseline** after any
lane/threshold change.

**Current baseline** — adopted 2026-08-22, FULL liquid universe, panel→08-21, 93 days, **2,471-ticker
spine** (retired; see the spine rule below), post-OI_FADE-full-window fix:

| MOM_LONG | MOM_SHORT | OI_FADE | S2 | S4 |
|---|---|---|---|---|
| −0.0118 (n=1213) | −0.0138 (n=830) | +0.0013 (n=1177) | +0.0018 (n=1269) | +0.0024 (n=1304) |

The standing rules this baseline carries. Each links to its worked example — read the doc before
overriding one, and do not re-derive the history here:

- **A below-baseline lane is not automatically a regression.** The panel grows and the pooled mean drifts
  on its own. Run the three isolation checks — (a) baseline cohort still reproduces, (b) engine code
  provably unchanged, (c) previous ticker list still reproduces the previous baseline — and only a lane
  that fails them is a real regression. [protocol](docs/regression-gate.md#isolation-check-protocol) ·
  [2026-08-08: all five lanes fell at once](docs/regression-gate.md#worked-example-2026-08-08-all-five-lanes-fell-at-once)
- **Every measured number carries the spine it was measured on — state the spine whenever you record one,
  and re-run check (c) before citing one across a universe change.** This binds **gate-effectiveness
  figures exactly as much as lanes**: the crash guard's DURABLE p=0.010 was a 785-spine artifact and reads
  p=0.237 on the full spine. **The spine now moves most cycles** — 2,471 → **2,443** priced on 2026-09-02
  (56 tickers sit in `features` but not `prices`), so verify it each cycle rather than assuming.
  [gate-vs-spine](docs/regression-gate.md#worked-example-2026-08-15-a-gate-result-that-was-a-spine-artifact) ·
  [the 09-02 move](docs/regression-gate.md#the-spine-moved-again-2471--2443-priced-2026-09-05)
- **Artifact removal is not decay.** Both OI_FADE's and S4's re-baselines were artifact removal; S4's
  `hit − base` was *already* negative beforehand, so it has never had a hit-rate edge on this panel — the
  removed names were supplying the right tail. [S4](docs/regression-gate.md#s4-re-baseline-00041--00025-2026-08-17--artifact-removal-not-decay)
- **When an increment's `base` is pinned (1.00 long / 0.00 short), the whole cohort is one observation —
  write down what the unwind will look like before it arrives.** The 08-08/08-15 rally and its 08-22
  mirror are the worked pair, and the pre-registration is what made the cycle
  readable. [unwind](docs/regression-gate.md#worked-example-2026-08-22-the-pre-registered-unwind-arrived)
- **A STOP flag is governed by the `cluster_id` unit** (else the name) — the risk-sizer's own unit — with
  the **`lane-exit-day`** view reported alongside it every cycle. A lane under **30 `lane-exit-day`**
  carries a correlated-draw caveat and cannot graduate to sizing on that evidence
  alone. [which unit](docs/regression-gate.md#which-clustering-unit-governs-a-stop-flag)
- **There are TWO exit-day units. Use their names, never the bare phrase "exit-day".** `exit-session` =
  distinct exit sessions pooled across lanes (the whole-book figure); `lane-exit-day` = one lane × exit-day
  pair (the per-lane column, ~3× more units on the same rows). Both reproduce; conflating them cost a full
  audit cycle. **Never report one unit alone.** [counting rule](docs/regression-gate.md#exit-day-counting-companion-rule)
- **At h10, clustering is not enough — report Newey-West alongside the clustered p.** h10 windows share
  9/10 of their days, which `lane-exit-day` clustering fixes only in the unit, not the overlap. The
  clustered t is an upper bound on significance. This is what dissolved the `OI_FADE_LIVE` stand-down: it
  was never significant under NW at any
  k. [NW](docs/regression-gate.md#oi_fade_live-never-survived-the-h10-overlap-correction--at-any-k)
- **MOM_SHORT is the ONE recorded exception** to "no lane negative-excess" (knowingly negative, watch-only
  capped). Don't add another without the same written
  rationale. [why](docs/regression-gate.md#mom_short-a-knowingly-negative-recorded-exception)

## The validated lanes (priors from research/20, 50, 70)

Historical-panel priors, harness-measured (**2026-08-15 baseline, full 2,471-ticker universe** — except
OI_FADE, re-pointed 2026-09-05). The forward book is graded separately by `/calibration-audit` and can
disagree — **no lane has cleared BH(0.10) forward yet.** **Where a lane's shipped rule differs from the
rule its prior was measured on, quote the SHIPPED rule's number** — OI_FADE forced this rule; its two
figures carry opposite signs. ⚠️ **These are priors, not a live read: do not re-point them on panel
growth** (invariant #6). Full per-lane notes: [`docs/lanes.md`](docs/lanes.md).

| Lane | Dir | Horizon | Realized (harness) | Status |
|---|---|---|---|---|
| `oi-flow-fade` (OI_FADE) | short | h10 | **−0.65%, n=510, 34 `lane-exit-day`, p=0.093** — `OI_FADE_LIVE`, the rule the engine runs. NW(L=9) p=0.290 | **ADVISORY — watch-only, never sizes.** Restored from diary-only 2026-09-05 when the pre-registered 30-unit re-check fired on **outcome 2**: no longer BH-significant. ⚠️ **Still negative on every cut** — advisory means the sign is watched, not endorsed. Two 08-29 claims are retracted: the p=0.028 headline was **uncorrected** (NW reads 0.143 on that same cohort), and ex-MSTR/CELH/MARA robustness decayed −0.70% → −0.45% (p=0.218). The raw-rank pool (+0.13% → −0.14%) grades a rule the engine does not run and its sign is three crypto names — **do not re-baseline it in either direction.** Ranking UNCHANGED (`oi_rel_build` + persistence). [`docs/regression-gate.md`](docs/regression-gate.md#the-oi_fade_live-re-check-fired-on-outcome-2--lane-restored-to-advisory-2026-09-05) |
| `momentum` MOM_SHORT (near-52w-low) | short | h10 | −1.37% mean, n=830 | Watch-only, crash-gated, never sizes |
| `momentum` MOM_LONG (near-52w-high) | long | h10 | −1.27% mean, n=1154 | Basket/watch only, never sizes. ⚠️ BH-significant negative under `lane-exit-day` (−4.65%, 14 units, p=0.008) — a correlated-draw caveat, not a STOP |
| `liquidity-reversion` (S2) | long | h3–5 | +0.14%, n=1210 | Advisory-only |
| `sentiment-contrarian` (S4) | long | h5–10 | +0.25%, n=1241 (post call-volume-floor fix) | Advisory-only; **hit − base negative (−0.056) — no hit-rate edge, right-tail only** |
| `vol-book` | non-dir | event/0DTE | VOL-ONLY | Net-of-cost, delta-neutral |
| `fundamentals-gate` | veto | — | risk filter | Finnhub = veto, not alpha (`research/80`) |

## Data & tools
- Panel: `~/Documents/Stocks/{All Options, Dark pool, Hot Option Chains, OI changes, Stock Screener}` (read via `uw` CLI / DuckDB).
- Truth set: `data/{prices,returns,features,weekly_features}.parquet` (built by `scripts/truthset/*`). `edge.py` = the conditional-benchmark resolver.
- `retro_harness.py` = the standing regression gate (`--oi-variant both` grades the raw vs the live OI_FADE rule). `factor_scan.py` = the cross-sectional factor zoo.
- `resolved_ledger.py` = the durable record of matured measurements, for **calls AND suppressions**. Re-deriving realized excess from the live vendor feed is **not idempotent** — EQR lost 11 sessions after the 08-15 audit, and CRNX lost **25 contiguous sessions** before the 09-05 one — so the audit book is not append-only unless the ledger restores it. `chart.py` exposes `gaps()`/`bars_grid()` for the same reason; never index a lookback by position.
- **A missing bar is a delisting only if it is a TRAILING stop with no interior hole.** An interior hole is a vendor retraction, and it recovers. `suppression_resolve.py` classifies the two apart (`inconclusive_kind`); never let a retraction be booked as a delisting.
- `fz` (Finviz) advisory; `mcp__yahoo-finance__*` NOT for path-aware outcomes.

## Cadence
Nightly `/market-scan` (post-8PM-EST export). Weekend `/weekly-review`. Weekly/per-~10-resolved
`/calibration-audit`. **Next audit due 2026-09-12.** **0 open call-rows** and **367 open suppressed
candidates** (26 lane-periods, 76 PENDING). The suppressions are the only cohort that actually grows: the
sized book gained **zero rows for the third cycle running**, and the whole call book gained 5.

- **Do not re-cite the 08-22 suppression result** — "gate discipline is significantly negative"
  (21 lane-periods, −1.74%, p=0.008) has now failed **two** re-tests: −0.89%/p=0.054 at 33, and
  **−0.53%/p=0.194 at 49**. Monotone toward zero. A gate-effectiveness result at PROVISIONAL N is a
  hypothesis until it survives a re-test — which is why **MOM_LONG's new −1.78%/p=0.028 at 15 baskets is
  pre-registered, not banked**, and why OI_FADE's suppression leg reading **+0.65% (cost edge)** must be
  reported rather than pooled away
  ([`docs/regression-gate.md`](docs/regression-gate.md#the-mom_long-suppression-leg--pre-registered-re-check-at-25-baskets-2026-09-05)).
- **Stop scheduling "the first non-overlapping OI_FADE cohort" as a matter of waiting** — re-signal dedup
  caps that lane at ~2 cluster-units per runner, however long it runs
  ([`docs/regression-gate.md`](docs/regression-gate.md#re-signal-dedup-caps-a-lanes-forward-n-structural-not-bad-luck)).
- **Report DORMANT gates in one line; do not re-derive them.** A gate produces evidence only when it
  **fires**, which is a regime event with no schedule. Crash guard: 20 guard-days, −0.58%, p=0.212 —
  the guard-day *set* is unchanged since 08-22 and none has fired since 08-07. Fundamentals veto: VETO
  n=15 / −2.28%, CONFIRM n=23 / −1.21% — unchanged since 08-15. Check the decided-N against last cycle
  **first**; if it has not moved, say "dormant, unchanged since <date>" and spend the cycle elsewhere.
- Count distinct **`lane-exit-day`** (per lane) / **`exit-session`** (whole book), not rows, when judging
  any cohort — and use the names
  ([`docs/regression-gate.md`](docs/regression-gate.md#exit-day-counting-companion-rule)).

## Git
- Name: Ewan · Email: liyuxuan66@hotmail.com. Branch before non-trivial changes; never commit `data/*.parquet`, `analyses/audit/`, or `.env`. **`analyses/weekly/` IS tracked** — the weekly-review journal is versioned (policy changed 2026-07-04). **`analyses/scan/` IS tracked** — the nightly scan journal is versioned and public (policy changed 2026-08-08); commit each night's `report.md` / `decision.json` / `conviction_*.json` with the scan. `analyses/audit/` stays local-only (working files, not a journal).
- **The repo is public** (`github.com/ewanlimr25/market-analysis`). `README.md` is the public-facing entry point — keep the required-data-layout section true if panel paths, filename patterns, or truth-set build order change. Nothing written into `analyses/` should contain a credential or an absolute local path.
