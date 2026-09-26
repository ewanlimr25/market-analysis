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
python3 scripts/truthset/build_prices.py && python3 scripts/truthset/build_returns.py && python3 scripts/truthset/build_features.py
make intraday-rv DAYS=5                          # the truth set and intraday_rv are NOT nightly: refresh them first (see note)
make backtest-sb REFRESH=1 && make report-sb     # extend the proxy, re-run the marked backtest -> data/backtest/sb_report.md (read §8)
make backtest-sc && make report-sc               # S-C panel run + §6 harness -> data/backtest/sc_report.md (NOT DUE until 40 forward weeks)
make test                                        # every unit test (1,279 at 2026-09-26); also proves no frozen parameter moved
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

Every ledger row carries `policy_id`, `role` (`champion` / `challenger` / `exploration`) and `gate_verdict`
(`DESIGN/100 §3`, adopted 2026-09-06). `signals.json` is `d1.1` from 2026-09-08; `d1.0` files stay valid.

That is the entire job: one command and a commit on trading nights, the block above on weekends, and
nothing touches real money before 2026-12-01. Sections 1 to 7 below are the detail.

### What one week of the routine produces

| Artifact | When | What it holds |
|---|---|---|
| `analyses/daily/<date>/report.md` + `signals.json` ×5 | each night | preflight, S-A candidates and suppressions, S-B gate tonight and next session, positions entered / skipped / graded, running ledger stats |
| `data/mart/daily_contract/date=<date>/` ×5 | each night | ~330,000 per-contract marks per day, the priced history the strategies read |
| `data/mart/index_vol/`, `data/mart/vix/` | each night | CBOE and VIX series extended through the day |
| `ledger/sb/` new rows | Friday, only if the gate is ON | up to four paper positions (SPY and QQQ, put spread and condor): strikes, expiry, credit, cost, max loss, one-contract sizing |
| `ledger/sb/` graded rows | the Friday a position expires (~3 weeks after entry) | net P&L per position from the official close, with `settle_source` |
| S-A ledger rows | from 2026-10-01, any night with a qualifying print | earnings candidates emitted and graded next morning; measurement only |
| `data/backtest/sb_report.md`, `sb_*.parquet` | weekend | proxy extended by one week, marked run re-done, the §8 go/no-go table as of that date (the `.md` reports are committed; the parquet stays local) |
| `data/backtest/report.md` | weekend, from October | S-A Season 3 tables accruing |
| `make test` result | weekend | all green, which also certifies no frozen parameter moved |
| six commits, pushed | five nightly, one weekly | the public, append-only record |

**What accumulates.** At most four S-B positions a week, and the gate has been ON about 40% of
Fridays, so expect one to two new positions a week and a graded result for each about three weeks
later. Between 09-11 and the last counting entry on 11-06 there are nine Fridays, so the 12-01 read
will rest on roughly three or four gate-on weeks (about fourteen paper positions across four sleeves):
enough to check that live marks match the backtest, not enough to prove the premium, which is why the
verdict is on the three-year proxy with the forward ledger beside it. The scale-up trigger (40 graded
positions per sleeve) is about two years away at that rate.

**What a week does not produce:** a trade instruction, a realized dollar, or a change to any
parameter. The one weekly judgment is whether the go/no-go table's four criteria still read as they
did the week before.

## 1. Every trading day, after the 8 PM export lands

```
cd ~/Development/market-analysis
make daily DATE=YYYY-MM-DD          # the session that just closed; about 2 seconds
git add analyses/daily ledger && git commit -m "daily: YYYY-MM-DD"
```

Then open `analyses/daily/YYYY-MM-DD/report.md`. Read it top to bottom; it is under a page. The
machine copy is `signals.json` in the same folder; its shape is pinned by `schemas/signals.schema.json`
(`schema_version d1.0`, `report_kind engine-daily`), and the command's last line reads
`signals.json: VALID`. A `WARN ... does not match` line means a key drifted: the file is still the
record, but tell the next session so the schema (not the ledger) is fixed.

### The loaders run from launchd, not from `make daily` (D23, 2026-09-07; moved from cron 2026-09-18)

The G7 to G10 mart tables (`cboe_chain`, `regsho`, `borrow`, `index_vol_ext`, `short_interest`) are
refreshed by two `make` targets that launchd runs on this machine; `make daily` never calls them and no
schema changed for them. The two LaunchAgents live in the repo under `ops/launchd/` and are installed as
copies in `~/Library/LaunchAgents/`:

```
com.market-analysis.loaders          weekdays 16:30 local   make -s loaders          >> data/logs/loaders.log
com.market-analysis.loaders-weekly   Saturday  09:00 local   make -s loaders-weekly   >> data/logs/loaders.log
```

Install or reinstall (after editing a plist, copy it again and repeat):

```
cp ops/launchd/com.market-analysis.*.plist ~/Library/LaunchAgents/
launchctl bootout gui/$(id -u)/com.market-analysis.loaders 2>/dev/null; launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.market-analysis.loaders.plist
launchctl bootout gui/$(id -u)/com.market-analysis.loaders-weekly 2>/dev/null; launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.market-analysis.loaders-weekly.plist
launchctl list | grep market-analysis          # both rows present, last exit 0
launchctl kickstart gui/$(id -u)/com.market-analysis.loaders   # fire it now (idempotent; a stored day logs "already stored")
```

16:30 local is after CBOE's 15-minute delay on the close; the weekly FINRA pull (about 2,500 requests)
runs Saturday morning. **Why launchd:** a `StartCalendarInterval` job that was missed because the Mac was
asleep runs when the Mac wakes; cron never caught up, and in the week of 09-14 it fired on one day of five.
A job missed because the Mac was shut down (not asleep) still does not run; then `make loaders` by hand
the same evening stores the chain under the payload's own date, and the CBOE payload holds a session's
close until the next open. A holiday logs one `already exists` / `no file` line per loader and nothing
else. `data/logs/` is gitignored; glance at `loaders.log` weekly and at `launchd-loaders*.err` if a row in
`launchctl list` shows a non-zero exit. The Reg SHO line catches up on its own: FINRA posts a session's
file in the evening, after the 16:30 run, and its CDN answers a missing file with HTTP 403, so each run
stores the prior session and lists today as `not published`; a run after a sleep gap refills the trailing
two weeks.

Do not run for a date with no export (weekends, holidays). If the export has not landed, wait; do
not run the previous date twice (it is harmless, the ledger writes are idempotent, but it wastes a
commit).

Optionally, `make cboe-chain` fetches the full SPY/QQQ option chain from CBOE's free delayed API
(RESEARCH/47 G8) into `data/mart/cboe_chain/`; it is a standalone target, not part of `make daily`,
and touches no S-A/S-B number.

`make daily` also runs the watch-basket step after S-B (DESIGN/110 R2, report.md's "Watch basket"
section, `ledger/wb/`) -- a pre-registered, exploration-only paper book of 20 stacked technical/flow
conditions, adding roughly 20-25 s to the run; it is **not** a signal, a filter on S-A/S-B, or
anything traded before its own 2026-12-01-or-100-episode read (`DESIGN/110` §6).

## 2. Reading the report

**Header:** `S-A daily — <date> (<season>)`. Seasons: S1 Apr–Jun 2026, S2 Jul–Sep, **S3 Oct–Nov (the
out-of-sample test)**.

**Preflight:** must say `clear`. If it does not, see §5 before anything else.

**Tonight's candidates:** earnings events that clear every S-A filter tonight. Each row gives the name,
structure (SS short straddle, IC iron condor), strikes and expiry, credit at the late-window market,
spread cost, max or stress loss, and `contracts` sized to the risk limit (the column is named
`contracts` everywhere; `n` in the running tables is a count of positions). On most nights outside earnings
season it reads `no event tonight clears the filters`. **S-A is a measurement only:** its backtest
failed the bar on Seasons 1 and 2 (`RESEARCH/45`), so these rows are never traded; they are graded
into the ledger to see whether Season 3 agrees.

**Suppressed:** events that failed, with the first failing filter (F1 price/issue type through F8
timing). This is the gate-effectiveness cohort; it accrues on its own.

**Graded today:** S-A rows whose exit was this morning, with the net P&L from real marks.

**Exploration book tonight (S-A):** from 10-01, both structures at one contract for every earnings event
the engine can price (a markable ATM pair in the 1B to 100B load band), whatever F1..F8 and the caps
said, with the first failing filter (or `PASS`) as `gate_verdict`. Same purpose as the S-B exploration
book: the filter chain is graded against what it refused at the season read.

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
- **S-B exploration book tonight:** on every entry day, one paper contract per sleeve entered under the
  champion's rules **whether or not the gate is ON**, with the gate's verdict stored on the row
  (`gate_verdict`). This is the improvement process's exploration floor (`findings/market-analysis/DESIGN/100 §6`):
  it lets the 12-01 read grade the gate itself (gate-ON rows against gate-OFF rows) and means the book can
  never go silent. Exploration rows carry `role = exploration`, are never mixed into the champion's tables,
  never count toward the open-position cap, and are graded at expiry like any other row.
- **S-B graded at expiry today:** positions settled today at intrinsic against the official close.
  `settle_source` shows whether the close came from `prices.parquet` or fell back to the last print.
- **Open positions / forward ledger to date:** what is on (champion rows only), and the running record per
  `(policy_id, role, sleeve)`. Champion (`sb-1.0`) and exploration lines are separate by construction.

**S-C state (from 2026-10-02):** on Fridays, where the week's universe stopped (one count per filter), the
positions tonight per variant (C1, C2 without Technology; SS and IB, one row each, with `cap_pass`: every selection
is a ledger row, the caps are the portfolio view), and the exploration book as counts by first failing filter (one
contract for every name with a priceable pair; the rows are in `ledger/sc/`). Every night: positions graded at
expiry (a row whose close is missing is retried the next night), the open book per pair against the 40% budget
(which binds only while S-B has positions open), and `graded entry-weeks: n of 40` per pair. Nothing here is a trade
before the read.

## 3. The calendar

| Date | What |
|---|---|
| 2026-09-08 (Mon) | Routine starts |
| **2026-09-11 (Fri)** | S-B ledger opens. First entry night if the gate is ON |
| 2026-10-01 | S-A Season 3 ledger opens (automatic) |
| 2026-10-02 | First S-B positions expire and are graded |
| **2026-10-02 (Fri)** | S-C ledger opens (`ledger/sc/`): first entry Friday, C1 and C2, SS and IB, plus the exploration book (findings DESIGN/90 §7) |
| 2026-11-06 | Last S-B entry that counts toward the read |
| **2026-12-01** | **The read.** Run the two backtests, write `findings/.../RESEARCH/47-read-2026-12-01.md`, record verdicts in `DECISIONS.md`. If SPY-PS clears all four criteria of `DESIGN/80 §6.7`, one contract goes live on the first gate-on Friday after |
| after | Scale above one contract only at the first cycle with ≥ 40 graded forward positions and positive mean (per sleeve) |
| about 2027-10 | S-C read: the first week a (variant, structure) pair holds 40 graded forward entry-weeks (the panel selected in 20 of 25 weeks, so about 50 calendar weeks plus the four-week hold) (`make report-sc` prints the count; NOT DUE until then) |

## 4. Weekly (weekend)

```
python3 scripts/truthset/build_prices.py && python3 scripts/truthset/build_returns.py && python3 scripts/truthset/build_features.py
make intraday-rv DAYS=5                          # the truth set and intraday_rv are NOT nightly: refresh them first (see note)
make backtest-sb REFRESH=1 && make report-sb     # S-B: proxy + marked run, then the bar tables -> data/backtest/sb_report.md
make backtest && make report                     # S-A: once Season 3 events exist (from October)
make backtest-sc && make report-sc               # S-C: panel run, then the §6 harness -> data/backtest/sc_report.md (NOT DUE until 40 forward weeks)
make test                                        # every unit test; must stay green
```

**Why the refresh comes first.** `prices.parquet`, `returns` and `features` (`scripts/truthset/`) and
`data/mart/intraday_rv` are manual rebuilds; no loader or `make daily` touches them. Left alone they go stale
silently until preflight trips: they sat at 2026-09-04 for three weeks in September, which made `rv5_21` and
the regime label on every ticker sheet 10+ sessions old and would have pushed S-B and S-C settlement onto the
last-print fallback. Run the two refresh lines every weekend, and again before any `make daily` or
`make ticker` whose date is past the truth set's last session.

Read `data/backtest/sb_report.md` §8 (go/no-go as of today). The report ends with an appendix that defines every column, symbol and
verdict it prints (`engine/validation/sb_glossary.py`). Between the sensitivities and the marked tables it also carries
"Other structures on the proxy": single legs, naked shorts and the call spread re-priced on the same rows
(`engine/validation/sb_alt_structures.py`). Descriptive only; the go/no-go never reads it. A criterion that flips from pass to fail
is information, not a reason to change anything before the read.

**The weekly report has no strikes; that is by design.** `sb_report.md` is the scorecard for the *rule*: about 60
proxy positions per sleeve reduced to statistics, answering one question, whether each sleeve still clears the bar
for the 12-01 read. It never lists a trade. The positions themselves live in two places:

| What | Where |
|---|---|
| positions entered on a Friday | `analyses/daily/<Friday>/report.md`, section "S-B positions tonight" |
| every position, open and graded | `ledger/sb/forward_signals.parquet` (`E`, `expiry`, `k_p1 k_p2 k_c1 k_c2`, `credit_entry`, `max_loss_usd`, `role`) |

Reading a position row: SPY PS `744 / 717`, credit `1.33`, expiry 10-16 (entered 2026-09-25, spot 771.40) is short
the 744 put and long the 717 put, about 1σ and 2σ below spot. Max loss is `(width − credit) × 100` =
`(27 − 1.33) × 100` = $2,567. An IC adds the short `c1` and long `c2` calls above spot. Every row is one paper
contract until the read. The next time a position is graded is the Friday of its expiry.

Reading `sb_report.md`, bottom up:

1. **Go / no-go** (the last table before the appendix). The only table that matters week to week: `verdict` per
   sleeve, with `note` naming the failed criteria. The weekly check is whether any of `c1_proxy`, `c2_marked`,
   `c3_month` or `c4_dsr` flipped since last week.
2. **The three evidence layers behind it.** The *proxy* tables (three years of positions priced from CBOE vol
   indices, the source of the t-stats). The *marked* tables (the same rule on real option prints since March; they
   check that the proxy does not flatter itself, through `gap_ror`). The *forward* ledger (`forward_n`, 0 until the
   first positions are graded on 2026-10-02).
3. **The risk checks.** The month rule (worst expiry month against the median month, ≤ 3×), the tail report (the
   single worst positions, for example SPY-PS −61% entered 2024-07-12), and the deflated Sharpe and PBO, which charge
   for having tested several variants.
4. **Descriptive sections** (gate modes and sensitivities, "Other structures on the proxy"). Context only; they
   never enter a verdict.
5. **Appendix.** Defines every column.

Rule of thumb: the daily report says what the book would be holding; the weekly report says whether the rule that
picked it is still good enough. Neither is a verdict before 2026-12-01.

## 5. When something is off

| Symptom | Cause | What to do |
|---|---|---|
| Preflight not clear: a panel export missing or empty | the export did not finish | do not run; re-export, then run |
| Preflight not clear: truth set stale (`prices`/`returns` behind the trade date) | the truth-set build has not run | `python3 scripts/truthset/build_prices.py && python3 scripts/truthset/build_returns.py`, then rerun `make daily`. S-B settlement falls back to the last print's underlying price when `prices.parquet` is stale and records `settle_source` |
| `CBOE refresh: failed` two sessions running | CBOE site or network | run `make index-vol` by hand; if still failing the gate reads `UNKNOWN` and fails closed, which is safe |
| A report shows a `model` tier on an entry leg | no print in the late window | the engine already refuses the entry; nothing to do |
| `make daily` for a date already run | re-run | safe; ledger keys are unique and nothing is duplicated |
| A number in an old report looks wrong | do not edit the report or the ledger | record it in `findings/.../DECISIONS.md`; ledger rows are never re-derived |
| `[watch.bars] Yahoo fetch failed for <T>: HTTP Error 404` | a share class the panel writes concatenated (`BRKB`) and Yahoo hyphenates (`BRK-B`) | add the pair to `YAHOO_ALIASES` in `scripts/chart.py`, the single Yahoo boundary. The name is not dropped loudly: its bar conditions simply go null |
| The watch basket's report says `Borrow snapshot: ... (fallback, N days old)` | no IBKR borrow file for the session (the 16:30 loader did not run, or the FTP failed) | nothing: `C-SHORT` read the latest earlier snapshot within 7 days (`engine.mart.borrow.BORROW_FALLBACK_MAX_DAYS`), never a later one, and `signals.json` records which (`watch_basket.borrow`, d1.5). `none within the fallback window` means borrow was null that night; note it, do not re-run |
| The watch basket's bar-derived conditions (`C-DIV`, `C-AVWAP`, `C-POC`, `C-SWING`, `C-RSI`) all read `?` | the bars cache does not reach the night being evaluated | expected only if the fetch failed; `bars.py` refreshes to the as-of session on its own, recovering the current session from `chart.session_bar` when Yahoo's multi-day array still lags. A whole column of `?` means the network pass failed, not that the conditions are false |

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

## 6a. Changing a strategy (the improvement process, DESIGN/100)

The weekly audit loops of the two retired fleets re-tuned prompts on n < 30 and converged on silence
(`findings/uw-daily-analysis/RESEARCH/93`). Here a strategy changes in exactly one way:

1. **Measure weekly, in code, and change nothing.** `make report-sb`, `make report`, the desk tables. No
   parameter, cap, gate or status moves outside step 4.
2. **Register one challenger** from the strategy's idea ledger (`DESIGN/80 §8`, `70 §7.4`), one parameter,
   after the champion's season read (the first is 2026-12-01). `make sb-challengers DRAFTS=1` backtests the
   CBOE vol-index family (VIX floor, VIX9D/VIX, VVIX, SKEW, VIX/VIX3M) on the S-B proxy and writes
   registration drafts under `ledger/challengers/drafts/` (`registered: "PENDING-2026-12-01"`, invisible to
   `open_challengers`) to carry into the real registration:
   `make adjudicate ARGS="register --strategy sb --policy-id sb-c-vixfloor-abs --idea 'VIX floor, absolute (VIX>=14 SPY / VXN>=17.5 QQQ)' --param vix_floor_abs=SPY:14,QQQ:17.5 --min-effect 0.01"`
   (the first registration, decided 2026-09-07 as D23/O1: the draft `ledger/challengers/drafts/sb-c-vixfloor-abs.json`,
   `n_required 15`, adjudication about 2026-12-25; register it on 2026-12-01 after the champion read, then build its
   shadow runner).
   `n_required` comes from `make power` (the champion's realised sd, inflated for the Newey-West lag) and
   fixes the adjudication date; the file lands in `ledger/challengers/` with a hash of the adjudication
   script. Commit it before the first shadow night. One open challenger per strategy.
3. **Run the challenger in shadow** under `role = challenger` with its own `policy_id`. The runner for a
   given parameter is built with the first registration; it writes rows beside the champion's on the same
   nights and never touches the champion's book.
4. **Adjudicate once, on the date:** `make adjudicate ARGS="run --policy sb-c1"`. Before the date it prints
   NOT_DUE and writes nothing; on the date it writes `ledger/adjudications/sb-c1.json` with PROMOTE or FAIL and
   appends to `LOG.md` (INSUFFICIENT prints the count and writes nothing, so it can run again once the units
   have accrued). It refuses to run twice and refuses an edited script. An early
   FAIL fires at half `n_required` if the paired mean is below `-min_effect`. PROMOTE prints the two edits
   to make by hand (the policy id in `engine/config.py` and the frozen-params test) and is recorded in
   `DECISIONS.md`.
5. **Grade the champion and its gate at every season read:** `make adjudicate ARGS="champion --strategy sb
   --n-required 26"` (the t part of the bar; the month rule, DSR and tail stay in `make report-sb`) and
   `make adjudicate ARGS="gate --strategy sb --min-effect 0.01 --n-required 20"`, which compares the
   exploration book's gate-ON units to its gate-OFF units. A gate that does not earn its keep becomes a
   challenger candidate for removal; it is never removed by the read itself.
6. **Kill rules** (`DESIGN/100 §8`): three consecutive FAILs close a strategy's idea ledger for a season;
   four season reads without a launched champion make the engine a measurement tool, and that is written
   down too.

**The watch-basket read** (`DESIGN/110 §6`, its own book, not the champion/challenger loop above): once
per basket, `make adjudicate ARGS="basket --policy wb-1.0 [--basket LONG|SHORT|VOL]"` counts independent
episodes (`episode = true` rows, `DESIGN/110 §4`) with `excess_h21` resolved. Before the later of
2026-12-01 and 100 episodes it prints `NOT_DUE` (the count and, at the trailing-30-session accrual rate, a
projected date) and writes nothing. On the date it computes the hit rate at h21 against the universe base
of the *same nights* (live from the screener spine, never the ledger), a two-sided binomial p, and the
mean SPY excess with a name-clustered t; `CLEARS` needs the hit rate at least 10 points above the base
(p < 0.05) and a positive mean excess (t >= 2), else `FAILS`. The verdict is written once to
`ledger/adjudications/wb-1.0-<basket>.json` and appended to `LOG.md`, exactly like the other verdicts; a
basket that clears becomes a registered challenger candidate for a sleeve, and one that fails twice in a
row is retired (rows stay as history).

Every ledger row carries `policy_id`, `role` and `gate_verdict`; rows are never pooled across them. The
exploration books (S-B from 09-11, S-A from 10-01) are what make step 5 possible: one paper contract per
sleeve or per priceable event, entered whatever the gate or the filters said, with the verdict on the row.

## 6b. One name: the ticker sheet (`make ticker`, findings/stock-deep-dive DESIGN/70; from 2026-09-21)

When you want to look at one stock, run the sheet, not a research skill:

```
make ticker T=NVDA                      # today's sheet -> analyses/ticker/NVDA/<date>/{ticker.json, report.md}
make ticker T=NVDA DATE=2026-09-18      # an earlier session (its inputs/ are kept beside it; a rerun is offline and identical)
make ticker T=NVDA DIRECTION=long       # your call, priced as shares + two verticals and written to the disc-1.0 book
make narrate T=NVDA                     # optional: headlines, analyst, Form 4, the disconfirming-facts checklist (changes no number)
make ticker-batch DATE=...              # one sheet per data/watch_names.txt name (the exploration book)
                                        # weekly, after the section 4 truth-set refresh, for the Friday session
```

The sheet answers, in order: **A** can this name be priced at all (L1..L6; the first failing floor is
named and a `CANNOT_PRICE` sheet still writes B, E, F); **B** the next print from three sources, `confirmed`
only when they agree on the session (a disagreement is X1 for 45 days -- the UW screener's
`next_earnings_date` is often a week off Finnhub, which is the point); **C** the premium label beside its
numbers (`spread_rv5` / `spread_c2c` in vol points, S-C's first failing filter, F6 at the value); **D** the
1σ boxes, ATR14, chain GEX and the zero-gamma strike nearest spot (never `uw gex`'s first crossing);
**E** borrow, short interest, beta, analyst, Form 4, VIX term, regime, with X2/X5 flagged; **F** the fixed
sentence -- the engine emits no direction -- and three context numbers; **G** the structure menu at S-C's
expiry with live-chain or tier-1/2 marks, cost, `P(inside)`/`P(touch)` and `n` at 0.5% of `E`; **H** what
went to `ledger/name/`.

What to expect from week to week: many names come back `CANNOT_PRICE` at L6 on some Fridays, and that is the
calendar, not a fault. The sheet prices premium at S-C's expiry, the listed expiry 20 to 40 days out nearest
`t + 28` (D26). When that lands on a monthly, most liquid names print an at-the-money pair with 5+ lots on
each leg; when it lands on a weekly, many do not (2026-09-18, 10-16 monthly: 23 of 34 watch names priced;
2026-09-25, 10-23 weekly: 12 of 34, MU failing with 4,460 contracts traded on the day). L6 reads the day's
flagged `daily_contract` prints, not the live CBOE quote, and stays frozen (owner default, 2026-09-26). A
`CANNOT_PRICE` sheet still writes sections B, E and F, and it adds no `sheet-1.0` row. S-C's own funnel thins
the same way on those weeks.

What to expect at the frozen `E = $100,000`: a 2σ-wing butterfly on a $200+ stock has a max loss above
$500, so `n = 0` with the note; the line still prints its numbers. `E=` on the command line is a reporting
parameter, not a permission.

The ledger: one `sheet-1.0` IB row per `CAN_PRICE` sheet (`champion` on `PASS`, else `exploration` with
the failing S-C filter or `X1` as `gate_verdict`), two `disc-1.0` rows per `DIRECTION=` call (shares at
the next open with the X4 stop, and the debit vertical) carrying `context_read` from file mtimes. `make
daily` grades whatever is due (`name ledger:` line on stderr). Reads: `make adjudicate ARGS="gate
--strategy sheet"` at 40 rows per stratum; `make adjudicate ARGS="champion --strategy disc --n-required
70"` at 70 rows and not before 2027-03-01; both print NOT_DUE until then. The 62-decision corpus of the
old skill sits in the same file as `sdd-llm-1.0` (graded, never re-derived). Kill rules are in DESIGN/70 §6.

The CBOE chain loader reads `data/watch_names.txt` every weekday (SPY/QQQ always); add a name there the
day you start looking at it -- its chain history starts then, not before. A weekend or after-close
snapshot carries 0/0 quotes on strikes the market makers pulled; such a leg falls back to the day's
`daily_contract` tier-1/2 mark, else the line is `unpriced`.

## 7. Where things live

| Path | What |
|---|---|
| `analyses/daily/<date>/report.md`, `signals.json` | the nightly output |
| `ledger/sb/` | S-B forward ledger (parquet, committed) |
| `ledger/` (S-A files) | S-A forward ledger, opens 2026-10-01 |
| `ledger/name/` | the ticker sheet's book: `sheet-1.0`, `disc-1.0` and the `sdd-llm-1.0` seed in one file (§6b) |
| `analyses/ticker/<SYMBOL>/<date>/` | one sheet: `ticker.json`, `report.md`, optional `narrate.md`; `inputs/` beside them is gitignored |
| `data/watch_names.txt` | the names the CBOE chain loader fetches nightly |
| `data/mart/daily_contract/date=*/` | per-contract daily marks, appended nightly |
| `data/mart/earnings_events/` | the earnings event table |
| `data/mart/index_vol/`, `data/mart/vix/` | CBOE and VIX series |
| `data/backtest/` | the two backtests' outputs and reports |
| `engine/config.py` | every frozen parameter, with the section of the spec it comes from |
| `schemas/signals.schema.json` | the contract for `signals.json`; `make validate DATE=...` checks one night by hand |
| `~/Development/findings/market-analysis/` | why all of this exists, and the hand-off note `NEXT-SESSION.md` |
