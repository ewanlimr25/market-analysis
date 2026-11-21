"""The weekend block (scripts/weekly.py; findings market-analysis DESIGN/120 §10), run by the nightly agent's sweep
after the last session of a week is committed.

The nightly's harness (tests/test_nightly.py) with every step of the block faked: each fake writes what the real step
would for the week's session. git runs for real, so commits and pushes are the real thing."""
from __future__ import annotations

import json
from collections.abc import Callable
from datetime import datetime, timedelta
from pathlib import Path

import pytest
from test_nightly import FakeRunner, World, at, complete, git

from scripts import nightly, weekly

pytestmark = pytest.mark.unit

FRIDAY, LAST_FRIDAY = "2026-11-20", "2026-11-13"
NO_GO = {"SPY-PS": ("yes", "no", "yes", "yes", "NO-GO"), "QQQ-PS": ("no", "no", "no", "no", "NO-GO")}
ORDER = ["build_universe.py", "build_prices.py", "build_returns.py", "build_features.py", "make intraday-rv",
         "make ticker-batch", "make backtest-sb", "make report-sb", "make backtest-sc", "make report-sc", "make test",
         "make backtest", "make report"]


def sb_report(day: str, verdicts: dict[str, tuple[str, ...]], index_vol: str | None = None) -> str:
    rows = "\n".join(f"| {sleeve} | 64 | {' | '.join(cells)} | note |" for sleeve, cells in verdicts.items())
    return ("# S-B backtest report (generated)\n\n\n## Inputs\n\n"
            f"- refreshed: {{'index_vol_through': '{index_vol or day}', 'prices_through': '{day}'}}\n\n"
            "## Go / no-go (DESIGN/80 §6.7; t >= 2.0; read 2026-12-01)\n\n"
            "| sleeve | n_proxy | c1_proxy | c2_marked | c3_month | c4_dsr | verdict | note |\n"
            f"|---|---|---|---|---|---|---|---|\n{rows}\n\n\n## Appendix: columns and symbols\n")


def sc_report(day: str) -> str:
    return f"# S-C backtest report (generated)\n\n\n## Inputs\n\n- n_weeks: 32\n- prices_through: {day}\n\n## More\n"


class Clock:
    """The time a sweep reads as it runs; a test moves it while the steps run."""

    def __init__(self, start: datetime) -> None:
        self.now = start

    def __call__(self) -> datetime:
        return self.now

    def advance(self, minutes: int) -> None:
        self.now += timedelta(minutes=minutes)


class WeekRunner(FakeRunner):
    """The nightly's fakes, plus the weekend block's steps (the truth-set builds stay the nightly's fakes)."""

    def __init__(self, repo: Path) -> None:
        super().__init__(repo)
        self.failing: dict[str, nightly.Result] = {}  # by the step's label in weekly.steps
        self.verdicts = dict(NO_GO)
        self.reports_name: str | None = None  # the day report-sb and report-sc write; None: the batch's DATE
        self.index_vol: str | None = None  # the day sb_report's index vols run to; None: as its prices
        self.batch_day = ""
        self.during_step: Callable[[str], None] | None = None  # what happens while a step runs

    @staticmethod
    def label(argv: list[str]) -> str | None:
        if argv[-1].endswith("scripts/truthset/build_universe.py"):
            return "build_universe.py"
        if argv[0] == "make" and argv[1] != "daily":
            return f"make {argv[1]}"
        return None

    def __call__(self, argv: list[str], cwd: Path, timeout: int) -> nightly.Result:
        argv = [str(a) for a in argv]
        label = self.label(argv)
        if label is None:
            return super().__call__(argv, cwd, timeout)
        self.calls.append(argv)
        if self.during_step is not None:
            self.during_step(label)
        if label in self.failing:
            return self.failing[label]
        self._write(label, argv)
        return nightly.Result(0, "1374 passed, 11 deselected in 41.17s" if label == "make test" else "done")

    def _write(self, label: str, argv: list[str]) -> None:
        backtest = self.repo / "data" / "backtest"
        named = self.reports_name or self.batch_day
        if label == "build_universe.py":
            (self.repo / "data" / "universe.json").write_text('["AAA", "BBB"]\n')
        elif label == "make ticker-batch":
            self.batch_day = argv[2].removeprefix("DATE=")
            sheet = self.repo / "analyses" / "ticker" / "AAA" / self.batch_day
            sheet.mkdir(parents=True, exist_ok=True)
            (sheet / "report.md").write_text(f"# AAA {self.batch_day}\n")
            (sheet / "ticker.json").write_text("{}\n")
            with open(self.repo / "ledger" / "name" / "forward_signals.parquet", "a") as ledger:
                ledger.write(f"{self.batch_day}\n")
        elif label == "make report-sb":
            (backtest / "sb_report.md").write_text(sb_report(named, self.verdicts, self.index_vol))
        elif label == "make report-sc":
            (backtest / "sc_report.md").write_text(sc_report(named))
        elif label == "make report":
            (backtest / "report.md").write_text(f"# S-A backtest report {self.batch_day}\n")

    def steps_run(self) -> list[str]:
        """The block's steps in the order they ran, the truth-set builds included (from the first universe build)."""
        labels = [self.label(c) or Path(c[-1]).name for c in self.calls]
        start = labels.index("build_universe.py") if "build_universe.py" in labels else len(labels)
        return [name for name in labels[start:] if name in ORDER]


class WeekWorld(World):
    def __init__(self, tmp: Path) -> None:
        super().__init__(tmp)
        self.runner = WeekRunner(self.repo)
        self.week: Callable[..., tuple[int, dict]] | None = weekly.run_week
        files = {
            "data/universe.json": '["AAA"]\n',
            "data/watch_names.txt": "# the watch list\nAAA\n",
            "data/backtest/sb_report.md": sb_report(LAST_FRIDAY, NO_GO),
            "data/backtest/sc_report.md": sc_report(LAST_FRIDAY),
            "data/backtest/report.md": "# S-A backtest report\n",
            "data/backtest/g3_report.md": "# a report the block does not write\n",
            f"analyses/ticker/AAA/{LAST_FRIDAY}/report.md": "# AAA\n",
            "ledger/name/forward_signals.parquet": f"{LAST_FRIDAY}\n",
        }
        for path, text in files.items():
            (self.repo / path).parent.mkdir(parents=True, exist_ok=True)
            (self.repo / path).write_text(text)
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", f"weekly: {LAST_FRIDAY}")
        git(self.repo, "push", "-q", "origin", "main")

    def sweep(self, now: datetime, dry_run: bool = False, clock: datetime | Callable[[], datetime] | None = None,
              **_: object) -> int:
        return super().sweep(now, dry_run, clock, posted=lambda day: "", week=self.week)

    def friday_night(self) -> None:
        for day in ("2026-11-18", "2026-11-19", FRIDAY):
            complete(self.stocks, day)

    def friday_committed(self) -> None:
        """Friday's night in, by a sweep without the block (as if it ran before the block was there)."""
        self.friday_night()
        self.week, week = None, self.week
        self.sweep(at(FRIDAY, 21, 40))
        self.week = week

    def weekly_files(self) -> list[str]:
        return git(self.repo, "show", "--name-only", "--format=", "HEAD").splitlines()

    def saved(self) -> dict:
        return json.loads(self.state.read_text())

    def commit_by_hand(self, path: str, subject: str) -> None:
        """The owner commits one file and pushes it; whatever else is uncommitted stays so."""
        (self.repo / path).parent.mkdir(parents=True, exist_ok=True)
        (self.repo / path).write_text("by hand\n")
        git(self.repo, "add", "--", path)
        git(self.repo, "commit", "-q", "-m", subject, "--", path)
        git(self.repo, "push", "-q", "origin", "main")


@pytest.fixture
def world(tmp_path: Path) -> WeekWorld:
    return WeekWorld(tmp_path)


# ---- the normal week ----------------------------------------------------------------------------


def test_after_the_weeks_last_night_the_block_runs_in_order_commits_and_pushes(world: WeekWorld) -> None:
    world.friday_night()

    code = world.sweep(at(FRIDAY, 21, 40))

    assert code == 0
    assert world.subjects()[:2] == [f"weekly: {FRIDAY}", f"daily: {FRIDAY}"]
    assert world.runner.steps_run() == ORDER
    assert ["make", "ticker-batch", f"DATE={FRIDAY}"] in world.runner.calls
    assert ["make", "backtest-sb", "REFRESH=1"] in world.runner.calls
    assert all(nightly.within(path, nightly.WEEKLY_PATHS) for path in world.weekly_files())
    assert f"analyses/ticker/AAA/{FRIDAY}/report.md" in world.weekly_files()
    assert git(world.repo, "status", "--porcelain") == ""
    assert world.pushed()
    night, week = world.notes[-2][1], world.notes[-1][1]
    assert f"{FRIDAY} committed" in night  # the night is told before the block starts
    assert week == (f"weekly: {FRIDAY} committed: 1 ticker sheets; make test: 1,374 passed; "
                    "S-B go/no-go: no criterion moved since the last weekly; pushed 1 commit(s)")
    assert world.pings == [""]  # the night's; the block never pings success


def test_the_block_waits_for_the_weeks_last_night(world: WeekWorld) -> None:
    complete(world.stocks, "2026-11-18")

    world.sweep(at("2026-11-18", 21, 40))

    assert world.subjects()[0] == "daily: 2026-11-18"
    assert world.runner.steps_run() == []


@pytest.mark.parametrize("subject", [f"weekly: {FRIDAY}", f"weekly: {FRIDAY} sheets", f"weekly: {FRIDAY}; by hand"])
def test_a_week_done_by_hand_is_left_alone(world: WeekWorld, subject: str) -> None:
    world.friday_night()
    world.commit_by_hand(f"analyses/ticker/AAA/{FRIDAY}/report.md", subject)

    world.sweep(at(FRIDAY, 21, 40))

    assert world.subjects()[0] == f"daily: {FRIDAY}"
    assert world.runner.steps_run() == []


def test_a_moved_go_no_go_criterion_is_told(world: WeekWorld) -> None:
    world.friday_night()
    world.runner.verdicts = {"SPY-PS": ("yes", "yes", "yes", "yes", "GO"), "QQQ-PS": NO_GO["QQQ-PS"]}

    world.sweep(at(FRIDAY, 21, 40))

    assert "S-B go/no-go moved: SPY-PS c2_marked no→yes, SPY-PS verdict NO-GO→GO (see sb_report.md)" in world.told()


def test_the_block_runs_on_the_weekend(world: WeekWorld) -> None:
    world.friday_committed()

    world.sweep(at("2026-11-22", 10, 0))

    assert world.subjects()[0] == f"weekly: {FRIDAY}"


# ---- failures -----------------------------------------------------------------------------------


def test_a_failed_step_commits_nothing_and_is_retried_once_over_its_own_outputs(world: WeekWorld) -> None:
    world.friday_night()
    world.runner.failing["make backtest-sb"] = nightly.Result(1, "fetching CBOE\nHTTP Error 503: Service Unavailable")

    first = world.sweep(at(FRIDAY, 21, 40))

    assert first == 1
    assert world.subjects()[0] == f"daily: {FRIDAY}"
    assert (f"the weekly for {FRIDAY}: make backtest-sb failed (exit 1): HTTP Error 503: Service Unavailable; "
            "nothing was committed") in world.told()
    assert git(world.repo, "status", "--porcelain") != ""  # its outputs are left for the retry, or for the owner
    assert world.pings[-1] == "/fail"

    world.sweep(at(FRIDAY, 22, 30))  # before the retry is due
    assert world.runner.steps_run().count("build_universe.py") == 1

    del world.runner.failing["make backtest-sb"]
    world.sweep(at(FRIDAY, 23, 45))

    assert world.subjects()[0] == f"weekly: {FRIDAY}"
    assert git(world.repo, "status", "--porcelain") == ""
    assert world.pushed()
    assert "weekly_held" not in world.saved()


def test_the_retry_is_two_hours_after_the_failure_not_after_the_sweeps_start(world: WeekWorld) -> None:
    world.friday_committed()
    clock = Clock(at(FRIDAY, 21, 50))
    world.runner.during_step = lambda label: clock.advance(10)  # nine faked steps: the failure lands at 23:20
    world.runner.failing["make backtest"] = nightly.Result(1, "MemoryError")

    world.sweep(at(FRIDAY, 21, 50), clock=clock)
    world.runner.during_step = None
    world.sweep(at(FRIDAY, 23, 55))  # two hours after the sweep's start, not after the failure

    assert world.runner.steps_run().count("build_universe.py") == 1
    assert world.saved()["weekly_held"]["retry_after"].startswith("2026-11-21T01:20")


def test_a_week_that_fails_twice_is_held_then_retried_once_head_moves(world: WeekWorld) -> None:
    world.friday_night()
    world.runner.failing["make test"] = nightly.Result(1, "1 failed, 1373 passed")

    for hour, minute in ((21, 40), (23, 45), (23, 55)):
        world.sweep(at(FRIDAY, hour, minute))
    world.sweep(at("2026-11-21", 9, 0))

    assert world.runner.steps_run().count("build_universe.py") == 2
    held = [m for _, m in world.notes if "is held after 2 failed tries" in m]
    assert len(held) == 2  # once a day: Friday night, then Saturday
    assert held[0].startswith(f"the weekly for {FRIDAY} is held") and "no night runs while" in held[0]
    assert world.subjects()[0] == f"daily: {FRIDAY}"

    world.commit_by_hand("engine/fix.py", "fix: the failing test")  # HEAD moves
    del world.runner.failing["make test"]
    world.sweep(at("2026-11-21", 10, 0))

    assert world.subjects()[0] == f"weekly: {FRIDAY}"  # over its own leftover outputs
    assert git(world.repo, "status", "--porcelain") == ""


@pytest.mark.parametrize("index_vol, reports", [(LAST_FRIDAY, None), (None, LAST_FRIDAY)])
def test_reports_not_rewritten_through_the_session_are_not_committed(
    world: WeekWorld, index_vol: str | None, reports: str | None,
) -> None:
    world.friday_night()
    world.runner.index_vol, world.runner.reports_name = index_vol, reports  # one stale input, or last week's (D39)

    world.sweep(at(FRIDAY, 21, 40))

    assert world.subjects()[0] == f"daily: {FRIDAY}"
    assert f"do not run through {FRIDAY}, so nothing was committed (D39)" in world.told()


def test_code_that_changes_while_the_block_runs_keeps_it_uncommitted(world: WeekWorld) -> None:
    world.friday_night()
    world.runner.during_step = lambda label: (
        (world.repo / "engine" / "daily.py").write_text("an edit mid-block\n") if label == "make backtest" else None)

    world.sweep(at(FRIDAY, 21, 40))

    assert world.subjects()[0] == f"daily: {FRIDAY}"
    assert "engine/daily.py changed while it ran" in world.told()


def test_a_hand_edit_under_the_weekly_paths_during_the_block_is_not_committed(world: WeekWorld) -> None:
    world.friday_night()
    world.runner.during_step = lambda label: (
        (world.repo / "data" / "backtest" / "g3_report.md").write_text("edited by hand\n")
        if label == "make backtest" else None)

    world.sweep(at(FRIDAY, 21, 40))

    assert world.subjects()[0] == f"daily: {FRIDAY}"
    assert "data/backtest/g3_report.md changed while it ran, and the block does not write it" in world.told()


def test_a_sheet_made_by_hand_between_tries_is_never_swept_into_the_retry(world: WeekWorld) -> None:
    world.friday_night()
    world.runner.failing["make backtest-sb"] = nightly.Result(1, "HTTP Error 503")
    world.sweep(at(FRIDAY, 21, 40))
    hand = world.repo / "analyses" / "ticker" / "NVDA" / FRIDAY
    hand.mkdir(parents=True)
    (hand / "report.md").write_text("make ticker T=NVDA DIRECTION=long, by hand\n")
    del world.runner.failing["make backtest-sb"]

    world.sweep(at(FRIDAY, 23, 45))

    assert world.subjects()[0] == f"daily: {FRIDAY}"
    assert f"uncommitted changes in analyses/ticker/NVDA/{FRIDAY}/report.md; nothing was run" in world.told()


def test_a_branch_switched_mid_block_gets_no_weekly_commit(world: WeekWorld) -> None:
    world.friday_night()
    world.runner.during_step = lambda label: (
        git(world.repo, "checkout", "-q", "-b", "experiment") if label == "make backtest" else None)

    world.sweep(at(FRIDAY, 21, 40))

    assert git(world.repo, "log", "-1", "--format=%s", "experiment") == f"daily: {FRIDAY}"
    assert "the repo is on experiment, not main, so its outputs are left uncommitted" in world.told()


def test_a_crash_in_the_block_is_told_and_what_the_night_saved_is_kept(world: WeekWorld) -> None:
    world.friday_night()
    world.runner.ingest = nightly.Result(1, "  hot-chains-2026-11-23.zip ... FAILED: the zip is damaged; the zip is kept\n")

    def crash(ctx: nightly.Context, state: dict) -> tuple[int, dict]:
        raise RuntimeError("boom")

    world.week = crash

    code = world.sweep(at(FRIDAY, 21, 40))

    assert code == 1
    assert world.subjects()[0] == f"daily: {FRIDAY}"
    assert "the weekly crashed: RuntimeError: boom" in world.told()
    told = world.saved()["told"]
    assert any(key.startswith("ingest:") for key in told)  # the night's told key survived the crash
    assert any(key.startswith("crash:weekly:") for key in told)


def test_a_failed_last_night_keeps_the_block_back(world: WeekWorld) -> None:
    world.friday_night()
    world.runner.daily[FRIDAY] = nightly.Result(1, "Traceback: KeyError")

    world.sweep(at(FRIDAY, 21, 40))

    assert world.runner.steps_run() == []


def test_an_unrelated_failure_in_the_sweep_does_not_keep_a_due_block_back(world: WeekWorld) -> None:
    world.friday_committed()
    world.runner.ingest = nightly.Result(1, "  hot-chains-2026-11-23.zip ... FAILED: the zip is damaged; the zip is kept\n")

    code = world.sweep(at("2026-11-21", 10, 0))

    assert code == 1  # the sweep still reports the ingest's failure
    assert world.subjects()[0] == f"weekly: {FRIDAY}"
    assert world.pings == ["", "/fail"]  # and the block's success does not cover it


# ---- when it may run ----------------------------------------------------------------------------


def test_a_week_whose_window_closed_is_told_once_and_never_run_late(world: WeekWorld) -> None:
    world.friday_night()

    world.sweep(at("2026-11-23", 17, 0))  # Friday's night lands on Monday evening, after the window
    world.sweep(at("2026-11-23", 17, 15))
    world.sweep(at("2026-11-24", 17, 0))

    assert world.subjects()[0] == f"daily: {FRIDAY}"
    assert world.runner.steps_run() == []
    missed = [(t, m) for t, m in world.notes if "did not start before" in m]
    assert len(missed) == 1
    assert missed[0][0] == nightly.TITLE and "Mon 11-23 08:00" in missed[0][1]


def test_the_block_does_not_start_in_the_hour_before_the_window_closes(world: WeekWorld) -> None:
    world.friday_night()

    world.sweep(at("2026-11-23", 8, 30))

    assert world.subjects()[0] == f"daily: {FRIDAY}"
    assert world.runner.steps_run() == []
    assert "did not start before Mon 11-23 08:00" in world.told()


def test_the_start_is_judged_on_the_clock_after_the_nights_not_the_sweeps_start(world: WeekWorld) -> None:
    world.friday_night()
    clock = Clock(at("2026-11-23", 7, 50))
    world.runner.during_daily = lambda day: clock.advance(15)  # three nights: the block would start at 08:35

    world.sweep(at("2026-11-23", 7, 50), clock=clock)

    assert world.subjects()[0] == f"daily: {FRIDAY}"
    assert world.runner.steps_run() == []
    assert "did not start before Mon 11-23 08:00" in world.told()


def test_a_block_that_reaches_the_window_end_stops_there_and_says_so_once(world: WeekWorld) -> None:
    world.friday_committed()
    clock = Clock(at("2026-11-23", 7, 30))
    world.runner.during_step = lambda label: clock.advance(10)  # ten faked steps: 09:00 before the last

    code = world.sweep(at("2026-11-23", 7, 30), clock=clock)
    world.sweep(at("2026-11-23", 9, 15))

    assert code == 1
    assert world.runner.steps_run()[-1] == "make backtest"
    stopped = [(t, m) for t, m in world.notes if "stopped before make report" in m]
    assert len(stopped) == 1 and stopped[0][0].endswith("needs a look")
    assert "no night runs until you commit or clear them" in stopped[0][1]
    assert "did not start before" not in world.told()  # the closed window is told once, by the stop
    assert world.subjects()[0] == f"daily: {FRIDAY}"


def test_uncommitted_weekly_files_or_inputs_stop_the_block(world: WeekWorld) -> None:
    world.friday_night()
    (world.repo / "data" / "backtest" / "sb_report.md").write_text("an edit by hand\n")

    world.sweep(at(FRIDAY, 21, 40))

    assert world.runner.steps_run() == []
    assert "uncommitted changes in data/backtest/sb_report.md; nothing was run" in world.told()

    git(world.repo, "checkout", "--", "data/backtest/sb_report.md")
    (world.repo / "data" / "watch_names.txt").write_text("AAA\nNVDA\n")
    world.sweep(at(FRIDAY, 22, 0))

    assert world.runner.steps_run() == []
    assert "uncommitted changes in data/watch_names.txt; nothing was run" in world.told()


def test_a_dry_run_says_what_the_block_would_do(world: WeekWorld) -> None:
    world.friday_committed()

    world.sweep(at(FRIDAY, 21, 55), dry_run=True)

    assert world.runner.steps_run() == []
    assert f"dry run: would run the weekly for {FRIDAY} (13 steps), then commit it" in world.told()
    assert world.subjects()[0] == f"daily: {FRIDAY}"


# ---- the push guard and the report parsing ------------------------------------------------------


def test_a_weekly_subject_on_other_files_is_not_pushed(world: WeekWorld) -> None:
    (world.repo / "engine" / "daily.py").write_text("changed\n")
    git(world.repo, "commit", "-q", "-am", f"weekly: {FRIDAY}")

    world.sweep(at("2026-11-18", 12, 0))

    assert not world.pushed()
    assert "is not a nightly or weekly commit" in world.told() and "engine/daily.py" in world.told()


def test_the_go_no_go_table_is_read_by_column_name() -> None:
    table = weekly.go_no_go(sb_report(FRIDAY, NO_GO))

    assert table == {
        "SPY-PS": {"c1_proxy": "yes", "c2_marked": "no", "c3_month": "yes", "c4_dsr": "yes", "verdict": "NO-GO"},
        "QQQ-PS": {"c1_proxy": "no", "c2_marked": "no", "c3_month": "no", "c4_dsr": "no", "verdict": "NO-GO"},
    }
    assert weekly.go_no_go("# no table here\n") == {}
    assert weekly.moves({}, table) == "S-B go/no-go: SPY-PS NO-GO; QQQ-PS NO-GO"
    assert weekly.moves(table, {}) == "S-B go/no-go: no table found in sb_report.md"
