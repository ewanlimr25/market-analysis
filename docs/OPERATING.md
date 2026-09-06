# Operating guide — the nightly routine

_For the person running the engine. What to type, what the report means, what to do when something is
off, and the dates that matter. Design and evidence live in `~/Development/findings/market-analysis/`
(`DESIGN/70` for S-A, `DESIGN/80` for S-B, `RESEARCH/45` and `46` for the backtests). Module map:
`engine/README.md`._

## 0. The routine at a glance

**Every trading day (Mon to Fri), after the 8 PM export**

```
cd ~/Development/market-analysis
make daily DATE=YYYY-MM-DD                       # the session that just closed; ~2 s
git add analyses/daily ledger && git commit -m "daily: YYYY-MM-DD" && git push
```

Then read `analyses/daily/YYYY-MM-DD/report.md` (one page). On most nights the two lines that matter
are `no event tonight clears the filters` and the S-B gate verdict. Two nights carry extra meaning:
**Thursday**, where the `Next session` line previews Friday's gate; **Friday**, the entry night, where
a gate ON lists the SPY/QQQ put spreads and condors and the ledger gains rows, and a gate OFF lists the
four sleeves as skipped. The command is the same either way. Skip weekends and holidays; if the export
has not landed, wait.

**Every weekend**

```
make backtest-sb REFRESH=1 && make report-sb     # extend the proxy, re-run the marked backtest -> data/backtest/sb_report.md (read §8)
make test                                        # 269 unit tests; also proves no frozen parameter moved
make backtest && make report                     # S-A, from October once Season 3 events exist
git add data/backtest && git commit -m "weekly: YYYY-MM-DD" && git push
```

**Dates where the routine changes**

| Date | Change |
|---|---|
| Mon 2026-09-08 | Routine starts |
| Fri 2026-09-11 | S-B ledger opens; first possible paper entry |
| Thu 2026-10-01 | S-A ledger opens (automatic) |
| Fri 2026-10-02 | First S-B expiry; first graded rows |
| Fri 2026-11-06 | Last S-B entry that counts toward the read |
| Tue 2026-12-01 | The read: run both backtest pairs, then a Claude session with the prompt in `findings/.../NEXT-SESSION.md` writes the verdict |

**Commands you never run on your own:** `make mart` (full rebuild, only for a corrupted partition),
`make index-vol` (only if the nightly says the CBOE refresh failed two sessions running),
`--force-ledger` (testing only). `/market-scan`, `/weekly-review` and `/calibration-audit` stay frozen.

That is the entire job: one command and a commit on trading nights, three commands on weekends, and
nothing touches real money before 2026-12-01. Sections 1 to 7 below are the detail.

## 1. Every trading day, after the 8 PM export lands

```
cd ~/Development/market-analysis
make daily DATE=YYYY-MM-DD          # the session that just closed; about 2 seconds
git add analyses/daily ledger && git commit -m "daily: YYYY-MM-DD"
```

Then open `analyses/daily/YYYY-MM-DD/report.md`. Read it top to bottom; it is under a page. The
machine copy is `signals.json` in the same folder.

Do not run for a date with no export (weekends, holidays). If the export has not landed, wait; do
not run the previous date twice (it is harmless, the ledger writes are idempotent, but it wastes a
commit).

## 2. Reading the report

**Header:** `S-A daily — <date> (<season>)`. Seasons: S1 Apr–Jun 2026, S2 Jul–Sep, **S3 Oct–Nov (the
out-of-sample test)**.

**Preflight:** must say `clear`. If it does not, see §5 before anything else.

**Tonight's candidates:** earnings events that clear every S-A filter tonight. Each row gives the name,
structure (SS short straddle, IC iron condor), strikes and expiry, credit at the late-window market,
spread cost, max or stress loss, and contracts sized to the risk limit. On most nights outside earnings
season it reads `no event tonight clears the filters`. **S-A is a measurement only:** its backtest
failed the bar on Seasons 1 and 2 (`RESEARCH/45`), so these rows are never traded; they are graded
into the ledger to see whether Season 3 agrees.

**Suppressed:** events that failed, with the first failing filter (F1 price/issue type through F8
timing). This is the gate-effectiveness cohort; it accrues on its own.

**Graded today:** S-A rows whose exit was this morning, with the net P&L from real marks.

**Season to date:** running S-A ledger stats. `ledger CLOSED (before 2026-10-01)` is correct until then.

**S-B state** (the strategy that can launch):

- `Gate (<date>, from <prior date> closes)`: one verdict per underlying, read at the prior close.
  `ON` or `OFF:G1` / `OFF:G2`.
  - **G1 = contango condition**: VIX must be below VIX3M. `OFF:G1` means the term structure is
    inverted, a stress reading.
  - **G2 = level condition**: the underlying's vol index (`X`: VIX for SPY, VXN for QQQ) must be
    above its own 20-session median. `OFF:G2` means vol is cheap relative to its recent past, so the
    premium is not worth selling. This is the usual reason the gate is off; expect it about 60% of
    Fridays.
  - `UNKNOWN` (a missing CBOE value) fails closed: no entry.
- `Next session (...)`: the same gate for the next session, so Thursday's report previews Friday.
- `CBOE refresh: ok through <date>`: if it says the refresh failed, the file on disk was used; the
  gate is still valid if `index-vol through` equals yesterday's date. Two stale days in a row: see §5.
- `Entry day: yes/no`: entries happen only on the last session of the ISO week (Friday, or Thursday
  before a Friday holiday).
- **S-B positions tonight:** on an entry day with the gate ON, the SPY and QQQ put spreads (PS) and
  iron condors (IC): strikes, expiry (nearest Friday to 21 days out), credit, cost, max loss, and
  contracts. Before 2026-12-01 these are **paper positions**; the sizing line shows what one contract
  would risk. Nothing is traded.
- **S-B skipped:** the four sleeves and why (usually `OFF:G2`, or `not entry day`).
- **S-B graded at expiry today:** positions settled today at intrinsic against the official close.
  `settle_source` shows whether the close came from `prices.parquet` or fell back to the last print.
- **Open positions / forward ledger to date:** what is on, and the running record.

## 3. The calendar

| Date | What |
|---|---|
| 2026-09-08 (Mon) | Routine starts |
| **2026-09-11 (Fri)** | S-B ledger opens. First entry night if the gate is ON |
| 2026-10-01 | S-A Season 3 ledger opens (automatic) |
| 2026-10-02 | First S-B positions expire and are graded |
| 2026-11-06 | Last S-B entry that counts toward the read |
| **2026-12-01** | **The read.** Run the two backtests, write `findings/.../RESEARCH/47-read-2026-12-01.md`, record verdicts in `DECISIONS.md`. If SPY-PS clears all four criteria of `DESIGN/80 §6.7`, one contract goes live on the first gate-on Friday after |
| after | Scale above one contract only at the first cycle with ≥ 40 graded forward positions and positive mean (per sleeve) |

## 4. Weekly (weekend)

```
make backtest-sb REFRESH=1 && make report-sb     # S-B: proxy + marked run, then the bar tables -> data/backtest/sb_report.md
make backtest && make report                     # S-A: once Season 3 events exist (from October)
make test                                        # 269 unit tests; must stay green
```

Read `data/backtest/sb_report.md` §8 (go/no-go as of today). A criterion that flips from pass to fail
is information, not a reason to change anything before the read.

## 5. When something is off

| Symptom | Cause | What to do |
|---|---|---|
| Preflight not clear: a panel export missing or empty | the export did not finish | do not run; re-export, then run |
| Preflight not clear: truth set stale (`prices`/`returns` behind the trade date) | the truth-set build has not run | `python3 scripts/truthset/build_prices.py && python3 scripts/truthset/build_returns.py`, then rerun `make daily`. S-B settlement falls back to the last print's underlying price when `prices.parquet` is stale and records `settle_source` |
| `CBOE refresh: failed` two sessions running | CBOE site or network | run `make index-vol` by hand; if still failing the gate reads `UNKNOWN` and fails closed, which is safe |
| A report shows a `model` tier on an entry leg | no print in the late window | the engine already refuses the entry; nothing to do |
| `make daily` for a date already run | re-run | safe; ledger keys are unique and nothing is duplicated |
| A number in an old report looks wrong | do not edit the report or the ledger | record it in `findings/.../DECISIONS.md`; ledger rows are never re-derived |

## 6. Rules that are not optional

- **No parameter changes before 2026-12-01.** `tests/test_frozen_params.py` and
  `tests/test_sb_frozen_params.py` fail if one moves. New ideas go to the idea ledgers
  (`DESIGN/70 §7.4`, `DESIGN/80 §8`) and are tested the season after the read.
- **The ledger is append-only.** A graded row is the record of what the marks were that day; vendor
  data can retract later and must not overwrite it.
- **Nothing trades real money before the read.** The report's sizing lines are what one contract
  would risk, so the dollars are visible, not so they are traded.
- **The old `/market-scan`, `/weekly-review` Layer 2 and `/calibration-audit` stay frozen.** The
  journal under `analyses/scan` and `analyses/weekly` is read-only history.
- **Commit every night** (`analyses/daily`, `ledger`). Do not push without deciding to; the repo is
  public.

## 7. Where things live

| Path | What |
|---|---|
| `analyses/daily/<date>/report.md`, `signals.json` | the nightly output |
| `ledger/sb/` | S-B forward ledger (parquet, committed) |
| `ledger/` (S-A files) | S-A forward ledger, opens 2026-10-01 |
| `data/mart/daily_contract/date=*/` | per-contract daily marks, appended nightly |
| `data/mart/earnings_events/` | the earnings event table |
| `data/mart/index_vol/`, `data/mart/vix/` | CBOE and VIX series |
| `data/backtest/` | the two backtests' outputs and reports |
| `engine/config.py` | every frozen parameter, with the section of the spec it comes from |
| `~/Development/findings/market-analysis/` | why all of this exists, and the hand-off note `NEXT-SESSION.md` |
