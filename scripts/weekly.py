"""The weekend block on its own (docs/OPERATING.md §0, §4; findings DESIGN/120 §10).

The nightly agent's sweep runs it once the last session of a week (a Friday, or the Thursday before a Friday holiday)
is committed, in the order of OPERATING.md §0's weekend block:

    python3 scripts/truthset/build_universe.py
    python3 scripts/truthset/build_prices.py, build_returns.py, build_features.py
    make intraday-rv DAYS=5
    make ticker-batch DATE=<the session>
    make backtest-sb REFRESH=1, make report-sb
    make backtest-sc, make report-sc
    make test
    make backtest, make report

It then checks that sb_report.md and sc_report.md were rewritten through the session (D39), commits what the block
writes (data/universe.json, the three reports, the watch names' sheets and ledger/name) as `weekly: <session>`, pushes
it beside the nightly commits and tells the owner: the sheet count, the tests, and whether a criterion of S-B's
go/no-go moved since the last weekly.

Its window runs from that night's commit to 09:00 of the next session. It starts no later than an hour before, and
reads the clock again before every step, so it never runs into a session: the window holds no market hours. It runs
nothing while the repo is off main, mid-operation, or holding uncommitted code, tests, the watch list, ledger or weekly
changes. A failed step leaves its outputs uncommitted and is held like a night: one more try two hours later (over its
own outputs), then none until HEAD moves. A week whose window closes without its weekly is told once and left to the
owner: run late, its reports would run past the session.
"""
from __future__ import annotations

import re
import sys
from collections.abc import Callable
from dataclasses import dataclass, replace
from datetime import date, datetime, timedelta
from pathlib import Path

from scripts import nightly as N
from scripts.agent_core import NY, TIMEOUT_STEP, Context, Problem, Slot, last_line, within

SLOT = Slot("weekly_held", "the weekly for {day}", "run the weekend block by hand (docs/OPERATING.md §4); no night "
                                                   "runs while its outputs sit uncommitted")
MISSED = "weekly_missed"  # the last week whose closed window was told
INPUTS = ("data/watch_names.txt", "tests")  # what decides the sheets and the tests' verdict: clean before, unmoved after
REPORTS = ("data/backtest/sb_report.md", "data/backtest/sc_report.md", "data/backtest/report.md")
SB_REPORT = REPORTS[0]
DATED = {  # D39: what each report's Inputs say once it is rewritten through the session
    "data/backtest/sb_report.md": ("'prices_through': '{day}'", "'index_vol_through': '{day}'"),
    "data/backtest/sc_report.md": ("prices_through: {day}",),
}
GO_NO_GO = "## Go / no-go"
WATCHED = ("c1_proxy", "c2_marked", "c3_month", "c4_dsr", "verdict")  # OPERATING.md §4: the one weekly check
TESTS_PASSED = re.compile(r"(\d+) passed")
START_BY = timedelta(hours=1)  # before the window's end: a later start could not finish by 09:00
LOG_TAIL = 15  # lines of a step's output kept in the log when it passes; all of it when it fails


@dataclass(frozen=True)
class Step:
    label: str
    argv: tuple[str, ...]


def steps(day: date) -> tuple[Step, ...]:
    python = sys.executable
    return (
        Step("build_universe.py", (python, "scripts/truthset/build_universe.py")),
        *(Step(Path(script).name, (python, script)) for script in N.TRUTH_SET_BUILDS),
        Step("make intraday-rv", ("make", "intraday-rv", "DAYS=5")),
        Step("make ticker-batch", ("make", "ticker-batch", f"DATE={day}")),
        Step("make backtest-sb", ("make", "backtest-sb", "REFRESH=1")),
        Step("make report-sb", ("make", "report-sb")),
        Step("make backtest-sc", ("make", "backtest-sc")),
        Step("make report-sc", ("make", "report-sc")),
        Step("make test", ("make", "test")),
        Step("make backtest", ("make", "backtest")),
        Step("make report", ("make", "report")),
    )


def expected(repo: Path, day: date) -> tuple[str, ...]:
    """Every path the block writes; a change anywhere else under the weekly paths is not its own."""
    from engine.mart.cboe_chain import read_symbols_file  # the reader `make ticker-batch` uses

    names = read_symbols_file(str(repo / "data" / "watch_names.txt"))
    return ("data/universe.json", *REPORTS, "ledger/name", *(f"analyses/ticker/{name}/{day}" for name in names))


# ---- is a week due ------------------------------------------------------------------------------


def week_of(last: date) -> date:
    """The last session of the week that `last` is in or follows: `last` itself on a Friday night."""
    from engine.daily import is_last_session_of_week

    day = last
    while not is_last_session_of_week(day):
        day = N.cal.prev_session(day)
    return day


def window_end(day: date) -> datetime:
    """09:00 of the session after `day`: until then the truth set and the reports can stop at `day`."""
    return datetime.combine(N.cal.next_session(day), N.NO_REBUILD_FROM, tzinfo=NY)


def weekly_committed(ctx: Context, day: date) -> bool | None:
    """A `weekly: <day>` commit exists, the agent's or one by hand (`weekly: <day> sheets`, `weekly: <day>; ...`
    count); None: git failed."""
    found = ctx.git("log", "-1", "--format=%h", "-E", f"--grep=^weekly: {day}([^0-9]|$)")
    return bool(found.out.strip()) if found.code == 0 else None


def due(ctx: Context, state: dict) -> tuple[date | None, Problem | None, dict]:
    """(the session whose weekly starts now, or None; what to tell; the new state). The window is judged on the
    clock, not the sweep's start: the nights before it can take an hour."""
    last = N.last_committed_night(ctx.repo, ctx.run)
    if last is None:
        return None, None, state  # the nights' own look tells the owner
    day = week_of(last)
    done = weekly_committed(ctx, day)
    if done is None:
        return None, Problem("weekly-log", "git log failed, so the weekly was not looked at"), state
    if done:
        return None, None, state
    end = window_end(day)
    if last == day and ctx.clock() < end - START_BY:
        return day, None, state
    if state.get(MISSED) == day.isoformat():
        return None, None, state
    missed = Problem(f"weekly-missed:{day}", f"the weekly for {day} did not start before {end - START_BY:%a %m-%d %H:%M}, "
                                             "so it is left to you (docs/OPERATING.md §4); run late, its reports "
                                             f"would run past {day}", failure=False)
    return None, missed, {**state, MISSED: day.isoformat()}


# ---- running it ---------------------------------------------------------------------------------


def tail(text: str, n: int) -> str:
    return "\n".join(text.rstrip().splitlines()[-n:])


def run_steps(ctx: Context, day: date) -> tuple[dict[str, str], Problem | None]:
    """Every step in order, stopping at the first that fails or that the window's end would overrun: (each step's
    output, the problem)."""
    outputs: dict[str, str] = {}
    end = window_end(day)
    for step in steps(day):
        if ctx.clock() >= end:
            return outputs, Problem(f"weekly-cut:{day}", f"the weekly for {day} stopped before {step.label}: its window "
                                                         f"closed at {end:%a %m-%d %H:%M}. Its outputs so far are left "
                                                         "uncommitted, and no night runs until you commit or clear "
                                                         "them (docs/OPERATING.md §4)")
        result = ctx.run(list(step.argv), ctx.repo, TIMEOUT_STEP)
        outputs[step.label] = result.text
        ctx.log(f"weekly {day}: {step.label} (exit {result.code})\n"
                f"{result.text if result.code != 0 else tail(result.text, LOG_TAIL)}")
        if result.code != 0:
            return outputs, Problem(f"weekly:{day}", f"the weekly for {day}: {step.label} failed (exit {result.code}): "
                                                     f"{last_line(result.text)}; nothing was committed", hold=True)
    return outputs, None


def read(path: Path) -> str:
    try:
        return path.read_text()
    except OSError:
        return ""


def inputs_section(text: str) -> str:
    start = text.find("## Inputs")
    if start < 0:
        return ""
    end = text.find("\n## ", start + 1)
    return text[start:end] if end >= 0 else text[start:]


def inputs_problem(ctx: Context, day: date) -> Problem | None:
    """D39: a report step that ran without rewriting its report would commit last week's scorecard."""
    stale = [path for path, marks in DATED.items()
             if not all(mark.format(day=day) in inputs_section(read(ctx.repo / path)) for mark in marks)]
    if not stale:
        return None
    return Problem(f"weekly-inputs:{day}", f"the weekly for {day}: the Inputs of {' and '.join(stale)} do not run "
                                           f"through {day}, so nothing was committed (D39)", hold=True)


def commit(ctx: Context, day: date) -> Problem | None:
    """What the block writes, alone, on main, and only when nothing else moved while it ran: the code, the tests, the
    watch list, a night's files, or anything under the weekly paths that the block does not write."""
    branch, underway = N.current_branch(ctx), N.operation_underway(ctx)
    if branch != "main" or underway:
        where = f"mid {underway}" if underway else f"on {branch or 'an unknown branch'}, not main"
        return Problem(f"weekly-git:{day}", f"the weekly for {day}: the repo is {where}, so its outputs are left "
                                            "uncommitted", hold=True)
    found = [N.changed(ctx, *paths) for paths in (N.CODE_PATHS, INPUTS, N.NIGHT_PATHS, N.WEEKLY_PATHS)]
    if any(paths is None for paths in found):
        return Problem(f"weekly-status:{day}", f"the weekly for {day}: git status failed; its outputs are left "
                                               "uncommitted", hold=True)
    code, inputs, nights, weekly_files = (paths or [] for paths in found)
    mine = expected(ctx.repo, day)
    moved = list(dict.fromkeys(code + inputs + [p for p in nights + weekly_files if not within(p, mine)]))
    if moved:
        return Problem(f"weekly-moved:{day}", f"the weekly for {day}: {', '.join(moved[:3])} changed while it ran, and "
                                              "the block does not write it, so nothing was committed", hold=True)
    if not weekly_files:
        return Problem(f"weekly-empty:{day}", f"the weekly for {day} changed nothing, so nothing was committed",
                       hold=True)
    for args in (("add", "--", *N.WEEKLY_PATHS), ("commit", "-q", "-m", f"weekly: {day}", "--", *N.WEEKLY_PATHS)):
        result = N.git_retrying(ctx, *args)
        if result.code != 0:
            return Problem(f"weekly-commit:{day}", f"the weekly for {day}: git {args[0]} failed "
                                                   f"({last_line(result.text)}); its outputs are left uncommitted",
                           hold=True)
    return None


# ---- what to tell -------------------------------------------------------------------------------


def go_no_go(text: str) -> dict[str, dict[str, str]]:
    """S-B's go/no-go table as {sleeve: {watched column: value}}; empty when the report has none."""
    start = text.find(GO_NO_GO)
    if start < 0:
        return {}
    rows: list[list[str]] = []
    for line in text[start:].splitlines()[1:]:
        if line.startswith("|"):
            rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
        elif rows:
            break
    if len(rows) < 3:
        return {}
    header, body = rows[0], rows[2:]
    columns = [(i, name) for i, name in enumerate(header) if name in WATCHED]
    return {cells[0]: {name: cells[i] for i, name in columns if i < len(cells)} for cells in body if cells}


def moves(before: dict[str, dict[str, str]], after: dict[str, dict[str, str]]) -> str:
    """What changed in S-B's go/no-go since the last committed weekly, for the owner's one weekly check."""
    if not after:
        return "S-B go/no-go: no table found in sb_report.md"
    if not before:
        return "S-B go/no-go: " + "; ".join(f"{sleeve} {row.get('verdict', '?')}" for sleeve, row in after.items())
    moved = [
        f"{sleeve} {name} {before[sleeve][name]}→{value}"
        for sleeve, row in after.items()
        for name, value in row.items()
        if name in before.get(sleeve, {}) and before[sleeve][name] != value
    ]
    if not moved:
        return "S-B go/no-go: no criterion moved since the last weekly"
    return "S-B go/no-go moved: " + ", ".join(moved) + " (see sb_report.md)"


def sheets(repo: Path, day: date) -> int:
    return sum(1 for _ in (repo / "analyses" / "ticker").glob(f"*/{day}/report.md"))


def tests_passed(output: str) -> str:
    found = TESTS_PASSED.findall(output)
    return f"make test: {int(found[-1]):,} passed" if found else "make test passed"


# ---- the block ----------------------------------------------------------------------------------


def failures_only(ping: Callable[[str], None]) -> Callable[[str], None]:
    """The healthcheck watches the nights: the block reports its failures to it, never a success that could cover a
    failure the same sweep's night phase just reported."""
    return lambda suffix: ping(suffix) if suffix else None


def run_week(ctx: Context, state: dict) -> tuple[int, dict]:
    """The sweep's last part (nightly.sweep): the weekend block when a week's last session is committed. It tells the
    owner itself; returns (exit code, new state)."""
    ctx = replace(ctx, ping=failures_only(ctx.ping))
    day, problem, state = due(ctx, state)
    if day is None:
        return N.tell(ctx, state, [], "", [problem] if problem is not None else [])
    skip, held = N.hold_status(ctx, state, day, SLOT)
    if skip:
        return N.tell(ctx, state, [], "", [held] if held is not None else [])
    retrying = (state.get(SLOT.key) or {}).get("session") == day.isoformat()  # its own outputs, whether HEAD moved
    groups = (N.NIGHT_PATHS, N.CODE_PATHS, N.WEEKLY_PATHS, INPUTS)
    blocked = N.refusal(ctx, groups, allow=expected(ctx.repo, day) if retrying else ())
    if blocked is not None:
        return N.tell(ctx, state, [], "", [blocked])
    if ctx.dry_run:
        return N.tell(ctx, state, [f"would run the weekly for {day} ({len(steps(day))} steps), then commit it"], "",
                      [])
    before = go_no_go(ctx.git("show", f"HEAD:{SB_REPORT}").out)
    outputs, problem = run_steps(ctx, day)
    problem = problem or inputs_problem(ctx, day) or commit(ctx, day)
    if problem is not None:
        if problem.hold:
            state = N.hold(ctx, state, day, problem, SLOT)
        elif problem.key == f"weekly-cut:{day}":
            state = {**state, MISSED: day.isoformat()}  # told now; the closed window is not told again
        return N.tell(ctx, state, [], "", [problem])
    state = N.release(state, day, SLOT)
    line = (f"weekly: {day} committed: {sheets(ctx.repo, day)} ticker sheets; "
            f"{tests_passed(outputs.get('make test', ''))}; {moves(before, go_no_go(read(ctx.repo / SB_REPORT)))}")
    pushed, push_problem = N.push(ctx, probe=False)
    return N.tell(ctx, state, [line], pushed, [push_problem] if push_problem is not None else [])
