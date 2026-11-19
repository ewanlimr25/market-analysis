"""The nightly agent (scripts/nightly.py; findings market-analysis DESIGN/120 §4(2)).

Each test builds a throwaway git repository with a bare `origin`, a panel folder and a Downloads folder. `make daily`,
the ingest, the truth-set builds and `open` are faked; git runs for real, so commits and pushes are the real thing."""
from __future__ import annotations

import http.client
import json
import os
import plistlib
import subprocess
import sys
from collections.abc import Callable
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

from scripts import nightly

pytestmark = pytest.mark.unit

NY = ZoneInfo("America/New_York")
FOLDERS = {
    "All Options": "bot-eod-report",
    "Dark pool": "dp-eod-report",
    "Hot Option Chains": "hot-chains",
    "OI changes": "chain-oi-changes",
    "Stock Screener": "stock-screener",
}
VALID = "signals.json: VALID (engine-daily d1.2)"
STALE = "STOP 2026-11-20 is the last session of the week and the truth set does not reach it, so expiries ..."


def at(day: str, hour: int, minute: int = 0) -> datetime:
    return datetime.fromisoformat(day).replace(hour=hour, minute=minute, tzinfo=NY)


def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True, text=True).stdout.strip()


def complete(stocks: Path, day: str) -> None:
    for folder, prefix in FOLDERS.items():
        (stocks / folder / f"{prefix}-{day}.parquet").write_bytes(b"PAR1")


class FakeRunner:
    """Fakes the ingest, the truth-set builds, `make daily` and `open`; everything else (git) runs for real."""

    def __init__(self, repo: Path) -> None:
        self.repo = repo
        self.calls: list[list[str]] = []
        self.ingest = nightly.Result(0, "0 ingested, 0 skipped, 0 failed.")
        self.daily: dict[str, nightly.Result] = {}
        self.builds: dict[str, nightly.Result] = {}  # by script name; a failing truth-set build
        self.push_check: nightly.Result | None = None
        self.during_build: Callable[[], None] | None = None  # what the owner does while a build runs
        self.during_daily: Callable[[str], None] | None = None  # ... or while make daily runs

    def __call__(self, argv: list[str], cwd: Path, timeout: int) -> nightly.Result:
        argv = [str(a) for a in argv]
        self.calls.append(argv)
        if "convert.py" in " ".join(argv):
            return self.ingest
        script = next((s for s in nightly.TRUTH_SET_BUILDS if argv[-1].endswith(s)), None)
        if script is not None:
            if self.during_build is not None:
                self.during_build()
            return self.builds.get(script, nightly.Result(0, "built"))
        if argv[:2] == ["make", "daily"]:
            day = argv[2].removeprefix("DATE=")
            result = self._make_daily(day)
            if self.during_daily is not None:
                self.during_daily(day)
            return result
        if argv[0] == "open":
            return nightly.Result(0, "")
        if argv[:3] == ["git", "push", "--dry-run"] and self.push_check is not None:
            return self.push_check
        return nightly.run(argv, cwd, timeout)

    def _make_daily(self, day: str) -> nightly.Result:
        result = self.daily.get(day, nightly.Result(0, f"{day}: 0 candidates, 3 suppressed, 1 graded\n{VALID}"))
        if result.code == 0:
            out = self.repo / "analyses" / "daily" / day
            out.mkdir(parents=True)
            gate = {"SPY": {"reason": "ON", "on": True}, "QQQ": {"reason": "OFF: vix below median", "on": False}}
            (out / "signals.json").write_text(json.dumps({"date": day, "candidates": [{}, {}], "sb_state": {"gate": gate}}))
            (out / "report.md").write_text(f"# {day}\n")
            with open(self.repo / "ledger" / "forward_ledger.parquet", "a") as ledger:
                ledger.write(f"{day}\n")
        return result

    def made(self) -> list[str]:
        return [c[2].removeprefix("DATE=") for c in self.calls if c[:2] == ["make", "daily"]]

    def built(self) -> list[str]:
        return [c[-1] for c in self.calls if any(c[-1].endswith(s) for s in nightly.TRUTH_SET_BUILDS)]


class World:
    def __init__(self, tmp: Path) -> None:
        self.repo, self.origin = tmp / "repo", tmp / "origin.git"
        self.stocks, self.uw, self.downloads = tmp / "Stocks", tmp / "uw", tmp / "Downloads"
        self.state = tmp / "state.json"
        for folder in FOLDERS:
            (self.stocks / folder).mkdir(parents=True)
        self.uw.mkdir()
        self.downloads.mkdir()
        self._init_repo()
        self.runner = FakeRunner(self.repo)
        self.notes: list[tuple[str, str]] = []
        self.pings: list[str] = []
        self.logs: list[str] = []
        self.pauses: list[float] = []
        self.sleep: Callable[[float], None] = self.pauses.append

    def _init_repo(self) -> None:
        subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(self.origin)], check=True)
        self.repo.mkdir()
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "config", "user.name", "Test")
        git(self.repo, "config", "user.email", "test@example.invalid")
        git(self.repo, "config", "commit.gpgsign", "false")
        for path in ("analyses/daily/2026-11-17/signals.json", "analyses/daily/2026-11-17/report.md",
                     "ledger/forward_ledger.parquet", "engine/daily.py", "scripts/nightly.py", "schemas/x.json"):
            (self.repo / path).parent.mkdir(parents=True, exist_ok=True)
            (self.repo / path).write_text("x\n")
        (self.repo / "Makefile").write_text("daily:\n")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "daily: 2026-11-17")
        git(self.repo, "remote", "add", "origin", str(self.origin))
        git(self.repo, "push", "-q", "-u", "origin", "main")

    def sweep(self, now: datetime, dry_run: bool = False, clock: datetime | None = None) -> int:
        ctx = nightly.Context(
            repo=self.repo, stocks=self.stocks, uw_mcp=self.uw, downloads=self.downloads, state_file=self.state,
            now=now, dry_run=dry_run, run=self.runner,
            notify=lambda title, message: self.notes.append((title, message)),
            ping=self.pings.append, log=self.logs.append,
            clock=lambda: clock or now, sleep=self.sleep,
        )
        return nightly.run_agent(ctx)

    def subjects(self) -> list[str]:
        return git(self.repo, "log", "--format=%s").splitlines()

    def pushed(self) -> bool:
        return git(self.repo, "rev-parse", "main") == git(self.origin, "rev-parse", "main")

    def told(self) -> str:
        return "\n".join(f"{t}: {m}" for t, m in self.notes)


@pytest.fixture
def world(tmp_path: Path) -> World:
    return World(tmp_path)


# ---- the normal night ---------------------------------------------------------------------------


def test_a_complete_session_is_run_committed_and_pushed(world: World) -> None:
    complete(world.stocks, "2026-11-18")

    code = world.sweep(at("2026-11-18", 21, 30))

    assert code == 0
    assert world.runner.made() == ["2026-11-18"]
    assert world.subjects()[0] == "daily: 2026-11-18"
    assert git(world.repo, "status", "--porcelain") == ""
    assert world.pushed()
    assert "2026-11-18" in world.told() and "pushed" in world.told()
    assert "SPY ON" in world.told() and "QQQ OFF" in world.told() and "2 S-A candidates" in world.told()
    assert world.pings == [""]


def test_the_commit_holds_only_the_nightly_outputs(world: World) -> None:
    complete(world.stocks, "2026-11-18")
    (world.repo / "notes.txt").write_text("the owner's scratch file")
    (world.repo / "docs").mkdir()
    (world.repo / "docs" / "OPERATING.md").write_text("an edit staged by hand, not yet committed\n")
    git(world.repo, "add", "docs/OPERATING.md")

    world.sweep(at("2026-11-18", 21, 30))

    files = git(world.repo, "show", "--name-only", "--format=", "HEAD").splitlines()
    assert sorted(files) == ["analyses/daily/2026-11-18/report.md", "analyses/daily/2026-11-18/signals.json",
                             "ledger/forward_ledger.parquet"]
    assert (world.repo / "notes.txt").exists()
    assert git(world.repo, "diff", "--cached", "--name-only") == "docs/OPERATING.md"  # still staged, never committed
    assert world.pushed()


def test_nothing_due_is_silent(world: World) -> None:
    code = world.sweep(at("2026-11-18", 19, 0))

    assert code == 0
    assert world.runner.made() == []
    assert world.notes == []
    assert world.pings == []


def test_two_sessions_are_committed_oldest_first_and_pushed_once(world: World) -> None:
    complete(world.stocks, "2026-11-18")
    complete(world.stocks, "2026-11-19")

    world.sweep(at("2026-11-19", 21, 0))

    assert world.runner.made() == ["2026-11-18", "2026-11-19"]
    assert world.subjects()[:2] == ["daily: 2026-11-19", "daily: 2026-11-18"]
    assert world.pushed()
    assert [c[:2] for c in world.runner.calls].count(["git", "push"]) == 1


def test_a_gap_stops_the_night_and_is_told(world: World) -> None:
    complete(world.stocks, "2026-11-19")  # 11-18 never downloaded

    code = world.sweep(at("2026-11-19", 21, 0))

    assert code == 1
    assert world.runner.made() == []
    assert "2026-11-18" in world.told() and "Dark pool" in world.told()
    assert world.pings == ["/fail"]


def test_the_last_session_of_the_week_rebuilds_the_truth_set_first(world: World) -> None:
    for day in ("2026-11-18", "2026-11-19", "2026-11-20"):
        complete(world.stocks, day)

    world.sweep(at("2026-11-20", 21, 0))

    assert world.runner.made() == ["2026-11-18", "2026-11-19", "2026-11-20"]
    builds = [i for i, c in enumerate(world.runner.calls) if any(c[-1].endswith(s) for s in nightly.TRUTH_SET_BUILDS)]
    friday = world.runner.calls.index(["make", "daily", "DATE=2026-11-20"])
    thursday = world.runner.calls.index(["make", "daily", "DATE=2026-11-19"])
    assert len(builds) == 3 and all(thursday < i < friday for i in builds)


def test_the_truth_set_rebuild_waits_for_the_close(world: World) -> None:
    for day in ("2026-11-18", "2026-11-19", "2026-11-20"):
        complete(world.stocks, day)

    code = world.sweep(at("2026-11-23", 10, 0))  # Monday, market open

    assert code == 0
    assert world.runner.made() == ["2026-11-18", "2026-11-19"]
    assert world.runner.built() == []
    assert "16:15" in world.told()
    assert world.pings == []


# ---- what stops a night -------------------------------------------------------------------------


def test_a_failed_make_daily_commits_nothing_and_stops(world: World) -> None:
    complete(world.stocks, "2026-11-18")
    complete(world.stocks, "2026-11-19")
    world.runner.daily["2026-11-18"] = nightly.Result(2, "Traceback ...\nKeyError: 'premium'\nmake: *** [daily] Error 1")

    code = world.sweep(at("2026-11-19", 21, 0))

    assert code == 1
    assert world.runner.made() == ["2026-11-18"]
    assert world.subjects()[0] == "daily: 2026-11-17"
    assert "make daily failed" in world.told() and "KeyError" in world.told()
    assert world.pings == ["/fail"]


def test_a_stale_truth_set_is_left_to_the_owner(world: World) -> None:
    for day in ("2026-11-18", "2026-11-19", "2026-11-20"):
        complete(world.stocks, day)
    world.runner.daily["2026-11-20"] = nightly.Result(2, STALE)

    code = world.sweep(at("2026-11-20", 21, 0))

    assert code == 1
    assert world.subjects()[0] == "daily: 2026-11-19"
    assert "ALLOW_STALE_TRUTH" in world.told()
    assert world.pushed()  # the two good nights still went


def test_a_schema_warning_still_commits_and_says_so(world: World) -> None:
    complete(world.stocks, "2026-11-18")
    world.runner.daily["2026-11-18"] = nightly.Result(0, "WARN signals.json does not match schemas/signals.schema.json (1):")

    code = world.sweep(at("2026-11-18", 21, 0))

    assert code == 0
    assert world.subjects()[0] == "daily: 2026-11-18"
    assert "WARN" in world.told()


@pytest.mark.parametrize("dirty", ["ledger/forward_ledger.parquet", "engine/daily.py", "Makefile"])
def test_uncommitted_changes_refuse_the_night(world: World, dirty: str) -> None:
    complete(world.stocks, "2026-11-18")
    (world.repo / dirty).write_text("edited by hand\n")

    code = world.sweep(at("2026-11-18", 21, 0))

    assert code == 1
    assert world.runner.made() == []
    assert dirty.split("/")[0] in world.told()


def test_an_untracked_hand_run_refuses_the_night(world: World) -> None:
    complete(world.stocks, "2026-11-18")
    (world.repo / "analyses" / "daily" / "2026-11-18").mkdir()
    (world.repo / "analyses" / "daily" / "2026-11-18" / "report.md").write_text("by hand\n")

    code = world.sweep(at("2026-11-18", 21, 0))

    assert code == 1
    assert world.runner.made() == []


def test_another_branch_refuses_the_night(world: World) -> None:
    complete(world.stocks, "2026-11-18")
    git(world.repo, "checkout", "-q", "-b", "experiment")

    code = world.sweep(at("2026-11-18", 21, 0))

    assert code == 1
    assert world.runner.made() == []
    assert "experiment" in world.told()


# ---- the push -----------------------------------------------------------------------------------


def test_a_code_commit_ahead_of_origin_is_never_pushed(world: World) -> None:
    (world.repo / "engine" / "daily.py").write_text("a change committed at the owner's word, not pushed\n")
    git(world.repo, "commit", "-q", "-am", "feat: something")
    complete(world.stocks, "2026-11-18")

    code = world.sweep(at("2026-11-18", 21, 0))

    assert code == 1
    assert world.subjects()[0] == "daily: 2026-11-18"
    assert git(world.origin, "log", "-1", "--format=%s", "main") == "daily: 2026-11-17"
    assert "feat: something" in world.told()


def test_a_nightly_subject_on_a_code_change_is_never_pushed(world: World) -> None:
    (world.repo / "engine" / "daily.py").write_text("changed\n")
    git(world.repo, "commit", "-q", "-am", "daily: 2026-11-18")

    world.sweep(at("2026-11-18", 21, 0))

    assert not world.pushed()
    assert "engine/daily.py" in world.told()


def test_origin_ahead_blocks_the_push_and_nothing_is_pulled(world: World, tmp_path: Path) -> None:
    other = tmp_path / "other"
    subprocess.run(["git", "clone", "-q", str(world.origin), str(other)], check=True)
    git(other, "config", "user.name", "T")
    git(other, "config", "user.email", "t@example.invalid")
    (other / "README.md").write_text("from elsewhere\n")
    git(other, "add", "README.md")
    git(other, "commit", "-q", "-m", "docs: elsewhere")
    git(other, "push", "-q", "origin", "main")
    complete(world.stocks, "2026-11-18")
    before = git(world.repo, "rev-parse", "HEAD~0")

    code = world.sweep(at("2026-11-18", 21, 0))

    assert code == 1
    assert git(world.repo, "log", "-1", "--format=%s") == "daily: 2026-11-18"
    assert git(world.repo, "rev-parse", "HEAD~1") == before
    assert not (world.repo / "README.md").exists()
    assert "origin" in world.told()


def test_an_unreachable_origin_holds_the_push_for_the_next_sweep(world: World, tmp_path: Path) -> None:
    complete(world.stocks, "2026-11-18")
    git(world.repo, "remote", "set-url", "origin", str(tmp_path / "unreachable.git"))

    first = world.sweep(at("2026-11-18", 21, 0))
    git(world.repo, "remote", "set-url", "origin", str(world.origin))
    second = world.sweep(at("2026-11-18", 21, 15))

    assert (first, second) == (1, 0)
    assert world.runner.made() == ["2026-11-18"]
    assert world.pushed()


def test_a_refused_push_is_retried_by_the_next_sweep(world: World) -> None:
    complete(world.stocks, "2026-11-18")
    hook = world.origin / "hooks" / "pre-receive"
    hook.write_text("#!/bin/sh\necho 'remote: refused for the test' >&2\nexit 1\n")
    hook.chmod(0o755)

    first = world.sweep(at("2026-11-18", 21, 0))
    hook.unlink()
    second = world.sweep(at("2026-11-18", 21, 15))

    assert (first, second) == (1, 0)
    assert "git push failed" in world.told()
    assert world.runner.made() == ["2026-11-18"]
    assert world.pushed()


def test_the_push_sends_the_commit_it_checked(world: World) -> None:
    complete(world.stocks, "2026-11-18")

    world.sweep(at("2026-11-18", 21, 0))

    tip = git(world.repo, "rev-parse", "main")
    assert ["git", "push", "-q", "origin", f"{tip}:refs/heads/main"] in world.runner.calls


def test_a_merge_commit_is_never_pushed_even_with_a_nightly_subject(world: World) -> None:
    # Arrange: the side commit is a proper nightly one, so only the merge itself can stop the push
    git(world.repo, "checkout", "-q", "-b", "side")
    (world.repo / "analyses" / "daily" / "2026-11-18").mkdir()
    (world.repo / "analyses" / "daily" / "2026-11-18" / "report.md").write_text("x\n")
    git(world.repo, "add", "-A")
    git(world.repo, "commit", "-q", "-m", "daily: 2026-11-18")
    git(world.repo, "checkout", "-q", "main")
    git(world.repo, "merge", "-q", "--no-ff", "-m", "daily: 2026-11-19", "side")

    code = world.sweep(at("2026-11-18", 19, 0))

    assert code == 1
    assert not world.pushed()
    assert "merge commit" in world.told()


def test_no_push_while_a_merge_is_underway(world: World) -> None:
    (world.repo / "analyses" / "daily" / "2026-11-18").mkdir()
    (world.repo / "analyses" / "daily" / "2026-11-18" / "report.md").write_text("by hand\n")
    git(world.repo, "add", "-A")
    git(world.repo, "commit", "-q", "-m", "daily: 2026-11-18")
    (world.repo / ".git" / "MERGE_HEAD").write_text(git(world.repo, "rev-parse", "HEAD") + "\n")

    world.sweep(at("2026-11-18", 21, 0))

    assert [c for c in world.runner.calls if c[:2] == ["git", "push"]] == []
    assert not world.pushed()


# ---- the dry run, the ingest, the reminder ------------------------------------------------------


def test_the_dry_run_ingests_but_runs_and_commits_nothing(world: World) -> None:
    complete(world.stocks, "2026-11-18")

    code = world.sweep(at("2026-11-18", 21, 0), dry_run=True)

    assert code == 0
    assert any("convert.py" in " ".join(c) for c in world.runner.calls)
    assert world.runner.made() == []
    assert world.subjects()[0] == "daily: 2026-11-17"
    assert ["git", "push", "--dry-run", "origin", "main"] in world.runner.calls
    assert "would run make daily DATE=2026-11-18" in world.told()
    assert world.pings == []


def test_a_dry_run_tells_what_it_would_do_once_a_day(world: World) -> None:
    complete(world.stocks, "2026-11-18")

    world.sweep(at("2026-11-18", 21, 0), dry_run=True)
    world.sweep(at("2026-11-18", 21, 15), dry_run=True)

    assert len(world.notes) == 1
    assert world.notes[0][1].startswith("dry run:")


def test_a_dry_run_with_nothing_due_is_silent(world: World) -> None:
    code = world.sweep(at("2026-11-18", 19, 0), dry_run=True)

    assert code == 0
    assert world.notes == []


def test_a_dry_run_whose_push_check_fails_says_so(world: World) -> None:
    world.runner.push_check = nightly.Result(128, "fatal: Authentication failed for the remote")

    code = world.sweep(at("2026-11-18", 19, 0), dry_run=True)

    assert code == 1
    assert "Authentication failed" in world.told()
    assert world.pings == []


def test_an_ingest_failure_is_told_and_complete_sessions_still_run(world: World) -> None:
    complete(world.stocks, "2026-11-18")
    world.runner.ingest = nightly.Result(1, "  hot-chains-2026-11-19.zip ... FAILED: the zip is damaged; the zip is kept\n")

    code = world.sweep(at("2026-11-19", 21, 0))

    assert code == 1
    assert world.runner.made() == ["2026-11-18"]
    assert "hot-chains-2026-11-19.zip" in world.told()


def test_a_busy_ingest_is_not_a_problem(world: World) -> None:
    world.runner.ingest = nightly.Result(3, "  [busy] another ingest is running; nothing was touched")

    code = world.sweep(at("2026-11-18", 19, 0))

    assert code == 0
    assert world.notes == []


def test_a_step_past_its_timeout_comes_back_as_timed_out(tmp_path: Path) -> None:
    result = nightly.run([sys.executable, "-c", "import time; time.sleep(30)"], tmp_path, 1)

    assert result.code == nightly.TIMED_OUT
    assert "timed out after 1s" in result.text


def test_an_ingest_timeout_points_at_the_macos_prompt_once_a_day(world: World) -> None:
    world.runner.ingest = nightly.Result(nightly.TIMED_OUT, "", "timed out after 3600s\n")

    world.sweep(at("2026-11-18", 19, 0))
    code = world.sweep(at("2026-11-18", 19, 15))

    assert code == 1
    assert len(world.notes) == 1
    title, message = world.notes[0]
    assert title == f"{nightly.TITLE}: needs a look"
    assert "click Allow" in message and "Full Disk Access" in message and sys.executable in message
    assert "kept something back" not in message
    assert world.pings == ["/fail"]


def test_the_reminder_comes_once_on_a_session_evening(world: World) -> None:
    world.sweep(at("2026-11-18", 20, 5))
    world.sweep(at("2026-11-18", 20, 20))

    opens = [c for c in world.runner.calls if c[0] == "open"]
    assert opens == [["open", nightly.DOWNLOAD_PAGE]]
    assert len(world.notes) == 1 and "five" in world.notes[0][1]


@pytest.mark.parametrize("name", ["hot-chains-2026-11-18.zip", "bot-eod-report-2026-11-18.zip.crdownload"])
def test_no_reminder_once_tonights_downloads_have_started(world: World, name: str) -> None:
    (world.downloads / name).write_bytes(b"")

    world.sweep(at("2026-11-18", 20, 10))

    assert [c for c in world.runner.calls if c[0] == "open"] == []


@pytest.mark.parametrize("now", [at("2026-11-18", 19, 59), at("2026-11-19", 0, 30), at("2026-11-21", 20, 10)])
def test_no_reminder_before_2005_after_midnight_or_on_a_weekend(world: World, now: datetime) -> None:
    world.sweep(now)

    assert [c for c in world.runner.calls if c[0] == "open"] == []


def test_a_holiday_evening_pings_the_healthcheck_once(world: World) -> None:
    for day in ("2026-11-18", "2026-11-19", "2026-11-20", "2026-11-23", "2026-11-24", "2026-11-25"):
        (world.repo / "analyses" / "daily" / day).mkdir(parents=True)
        (world.repo / "analyses" / "daily" / day / "report.md").write_text("x\n")
    git(world.repo, "add", "-A")
    git(world.repo, "commit", "-q", "-m", "daily: 2026-11-25")
    git(world.repo, "push", "-q", "origin", "main")

    world.sweep(at("2026-11-26", 20, 10))  # Thanksgiving
    world.sweep(at("2026-11-26", 20, 25))

    assert world.pings == [""]
    assert [c for c in world.runner.calls if c[0] == "open"] == []


def test_a_problem_is_told_once_a_day(world: World) -> None:
    complete(world.stocks, "2026-11-19")  # the 11-18 gap

    world.sweep(at("2026-11-19", 21, 0))
    world.sweep(at("2026-11-19", 21, 15))
    world.sweep(at("2026-11-20", 9, 0))

    assert len(world.notes) == 2
    assert world.pings == ["/fail", "/fail"]


def test_a_crash_still_tells_the_owner(world: World) -> None:
    def broken(argv: list[str], cwd: Path, timeout: int) -> nightly.Result:
        raise RuntimeError("disk on fire")

    world.runner = broken  # type: ignore[assignment]

    code = world.sweep(at("2026-11-18", 21, 0))

    assert code == 1
    assert "disk on fire" in world.told()
    assert world.pings == ["/fail"]


# ---- small parts --------------------------------------------------------------------------------


def test_the_last_committed_night_ignores_untracked_folders(world: World) -> None:
    (world.repo / "analyses" / "daily" / "2026-11-18").mkdir()

    assert nightly.last_committed_night(world.repo, world.runner) == date(2026, 11, 17)


@pytest.mark.parametrize("stored, expected", [
    ("https://hc-ping.com/0f7c-uuid\n", "https://hc-ping.com/0f7c-uuid"),
    ("http://insecure.example/ping", None),
    ("", None),
])
def test_the_healthcheck_url_comes_from_the_keychain_and_must_be_https(stored: str, expected: str | None) -> None:
    def keychain(argv: list[str], cwd: Path, timeout: int) -> nightly.Result:
        assert argv[:2] == ["security", "find-generic-password"]
        return nightly.Result(0 if stored else 44, stored)

    assert nightly.healthcheck_url(keychain) == expected


def test_the_lock_admits_one_sweep_at_a_time(tmp_path: Path) -> None:
    lock = tmp_path / "nightly.lock"
    with nightly.exclusive(lock) as first:
        with nightly.exclusive(lock) as second:
            assert (first, second) == (True, False)


def test_the_launch_agent_template_renders_to_a_valid_plist() -> None:
    template = (Path(nightly.REPO) / "ops" / "launchd" / "com.market-analysis.nightly.plist").read_text()
    assert "/Users/" not in template
    rendered = (template.replace("__HOME__", "/h").replace("__REPO__", "/h/repo")
                .replace("__PYTHON__", "/h/py").replace("__DRY_RUN__", "0"))
    plist = plistlib.loads(rendered.encode())
    assert plist["Label"] == "com.market-analysis.nightly"
    assert plist["ProgramArguments"] == ["/h/py", "/h/repo/scripts/nightly.py"]
    assert plist["WatchPaths"] == ["/h/Downloads"]
    assert plist["StartInterval"] == 900
    assert sorted(c["Weekday"] for c in plist["StartCalendarInterval"]) == [1, 2, 3, 4, 5]
    assert {(c["Hour"], c["Minute"]) for c in plist["StartCalendarInterval"]} == {(20, 5)}
    assert plist["EnvironmentVariables"]["MA_NIGHTLY_DRY_RUN"] == "0"
    assert plist["RunAtLoad"] is False


# ---- the independent review's cases (findings DESIGN/120 §8) ------------------------------------


def test_a_merge_underway_refuses_the_night_and_commits_nothing(world: World, tmp_path: Path) -> None:
    other = tmp_path / "other"
    subprocess.run(["git", "clone", "-q", str(world.origin), str(other)], check=True)
    git(other, "config", "user.name", "T")
    git(other, "config", "user.email", "t@example.invalid")
    (other / "README.md").write_text("from elsewhere\n")
    git(other, "add", "README.md")
    git(other, "commit", "-q", "-m", "docs: elsewhere")
    git(other, "push", "-q", "origin", "main")
    git(world.repo, "fetch", "-q", "origin")
    git(world.repo, "merge", "--no-commit", "--no-ff", "origin/main")  # resolved, staged, not committed
    complete(world.stocks, "2026-11-18")

    code = world.sweep(at("2026-11-18", 21, 0))

    assert code == 1
    assert world.runner.made() == []
    assert world.subjects()[0] == "daily: 2026-11-17"
    assert (world.repo / ".git" / "MERGE_HEAD").exists()
    assert "MERGE_HEAD" in world.told()


def test_a_hand_run_during_the_rebuild_stops_the_session(world: World) -> None:
    for day in ("2026-11-18", "2026-11-19", "2026-11-20"):
        complete(world.stocks, day)

    def hand_run() -> None:
        out = world.repo / "analyses" / "daily" / "2026-11-20"
        out.mkdir(parents=True, exist_ok=True)
        (out / "report.md").write_text("make daily DATE=2026-11-20 ALLOW_STALE_TRUTH=1, by hand\n")

    world.runner.during_build = hand_run

    code = world.sweep(at("2026-11-20", 21, 0))

    assert code == 1
    assert world.runner.made() == ["2026-11-18", "2026-11-19"]
    assert world.subjects()[0] == "daily: 2026-11-19"
    assert "analyses/daily/2026-11-20/report.md" in world.told()


def test_the_code_changing_during_the_night_leaves_it_uncommitted(world: World) -> None:
    complete(world.stocks, "2026-11-18")
    world.runner.during_daily = lambda day: (world.repo / "engine" / "daily.py").write_text("edited mid-run\n")

    code = world.sweep(at("2026-11-18", 21, 0))

    assert code == 1
    assert world.subjects()[0] == "daily: 2026-11-17"
    assert (world.repo / "analyses" / "daily" / "2026-11-18" / "report.md").exists()  # left for the owner
    assert "the code changed" in world.told()


def test_another_nights_files_appearing_are_never_committed(world: World) -> None:
    complete(world.stocks, "2026-11-18")

    def another_night(day: str) -> None:
        out = world.repo / "analyses" / "daily" / "2026-11-19"
        out.mkdir(parents=True)
        (out / "report.md").write_text("another night, by hand\n")

    world.runner.during_daily = another_night

    code = world.sweep(at("2026-11-18", 21, 0))

    assert code == 1
    assert world.subjects()[0] == "daily: 2026-11-17"
    assert "another night's files" in world.told()


def test_a_failed_session_is_held_not_retried_every_sweep(world: World) -> None:
    for day in ("2026-11-18", "2026-11-19", "2026-11-20"):
        complete(world.stocks, day)
    world.runner.daily["2026-11-20"] = nightly.Result(2, "", STALE)

    for minute in (0, 15, 30, 45):
        world.sweep(at("2026-11-20", 21, minute))
    after_first = (world.runner.made().count("2026-11-20"), len(world.runner.built()))
    world.sweep(at("2026-11-20", 23, 5))  # past RETRY_AFTER: one more try
    for minute in (20, 35, 50):
        world.sweep(at("2026-11-20", 23, minute))
    after_second = (world.runner.made().count("2026-11-20"), len(world.runner.built()))
    git(world.repo, "commit", "-q", "--allow-empty", "-m", "fix: something")  # HEAD moves: tried again
    world.sweep(at("2026-11-20", 23, 55))

    assert after_first == (1, 3)
    assert after_second == (2, 6)
    assert world.runner.made().count("2026-11-20") == 3
    assert "is held after 2 failed tries" in world.told()


def test_the_rebuild_reads_the_clock_when_it_starts(world: World) -> None:
    for day in ("2026-11-18", "2026-11-19", "2026-11-20"):
        complete(world.stocks, day)

    world.sweep(at("2026-11-23", 8, 59), clock=at("2026-11-23", 9, 1))  # a Monday sweep reaching Friday after 09:00

    assert world.runner.made() == ["2026-11-18", "2026-11-19"]
    assert world.runner.built() == []
    assert "16:15" in world.told()


def test_a_failed_truth_set_build_commits_nothing(world: World) -> None:
    for day in ("2026-11-18", "2026-11-19", "2026-11-20"):
        complete(world.stocks, day)
    world.runner.builds["scripts/truthset/build_returns.py"] = nightly.Result(1, "", "HTTPError: 429 Too Many Requests")

    code = world.sweep(at("2026-11-20", 21, 0))

    assert code == 1
    assert world.runner.made() == ["2026-11-18", "2026-11-19"]
    assert "build_returns.py failed" in world.told() and "429" in world.told()


def test_a_brief_index_lock_is_waited_out(world: World) -> None:
    complete(world.stocks, "2026-11-18")
    lock = world.repo / ".git" / "index.lock"
    world.runner.during_daily = lambda day: lock.write_text("")

    def pause(seconds: float) -> None:
        world.pauses.append(seconds)
        lock.unlink(missing_ok=True)  # the editor's git status finishes

    world.sleep = pause

    code = world.sweep(at("2026-11-18", 21, 0))

    assert code == 0
    assert world.subjects()[0] == "daily: 2026-11-18"
    assert world.pauses == [nightly.LOCK_PAUSE]


def test_a_lasting_index_lock_leaves_the_night_uncommitted_and_says_so(world: World) -> None:
    complete(world.stocks, "2026-11-18")
    world.runner.during_daily = lambda day: (world.repo / ".git" / "index.lock").write_text("")

    code = world.sweep(at("2026-11-18", 21, 0))

    assert code == 1
    assert world.subjects()[0] == "daily: 2026-11-17"
    assert len(world.pauses) == nightly.LOCK_RETRIES
    assert "git add failed" in world.told()


def test_untracked_files_are_seen_whatever_the_git_config(world: World) -> None:
    git(world.repo, "config", "status.showUntrackedFiles", "no")
    complete(world.stocks, "2026-11-18")
    (world.repo / "analyses" / "daily" / "2026-11-18").mkdir()
    (world.repo / "analyses" / "daily" / "2026-11-18" / "report.md").write_text("by hand\n")

    code = world.sweep(at("2026-11-18", 21, 0))

    assert code == 1
    assert world.runner.made() == []


def test_past_the_calendar_no_night_runs(world: World) -> None:
    code = world.sweep(at("2028-01-04", 21, 0))

    assert code == 1
    assert world.runner.made() == []
    assert "holiday calendar ends 2027-12-31" in world.told()


def test_the_calendar_end_is_told_a_month_ahead(world: World) -> None:
    git(world.repo, "commit", "-q", "--allow-empty", "-m", "placeholder")
    (world.repo / "analyses" / "daily" / "2027-12-09").mkdir(parents=True)
    (world.repo / "analyses" / "daily" / "2027-12-09" / "report.md").write_text("x\n")
    git(world.repo, "add", "-A")
    git(world.repo, "commit", "-q", "-m", "daily: 2027-12-09")
    git(world.repo, "push", "-q", "origin", "main")

    code = world.sweep(at("2027-12-10", 19, 0))

    assert code == 0
    assert "extend engine/calendar.py" in world.told()


def test_an_ingest_problem_with_changing_numbers_is_told_once(world: World) -> None:
    for free, minute in (("1.2", 0), ("0.9", 15), ("0.7", 30)):
        world.runner.ingest = nightly.Result(
            1, f"  bot-eod-report-2026-11-18.zip ... FAILED: needs 9.1 GB free to unpack, {free} GB available\n")
        world.sweep(at("2026-11-18", 19, minute))

    assert len(world.notes) == 1
    assert world.pings == ["/fail"]


def test_a_holiday_evening_with_a_failure_stays_failed(world: World) -> None:
    for day in ("2026-11-18", "2026-11-19", "2026-11-20", "2026-11-23", "2026-11-24", "2026-11-25"):
        (world.repo / "analyses" / "daily" / day).mkdir(parents=True)
        (world.repo / "analyses" / "daily" / day / "report.md").write_text("x\n")
    git(world.repo, "add", "-A")
    git(world.repo, "commit", "-q", "-m", "daily: 2026-11-25")
    git(world.repo, "push", "-q", "origin", "main")
    world.runner.ingest = nightly.Result(1, "  hot-chains-2026-11-25.zip ... FAILED: the zip is damaged; the zip is kept")

    world.sweep(at("2026-11-26", 20, 10))  # Thanksgiving

    assert world.pings == ["/fail"]


def test_idle_dry_runs_check_the_push_once_a_day(world: World) -> None:
    for minute in (0, 15, 30):
        world.sweep(at("2026-11-18", 3, minute), dry_run=True)

    fetches = [c for c in world.runner.calls if c[:2] == ["git", "fetch"]]
    checks = [c for c in world.runner.calls if c[:3] == ["git", "push", "--dry-run"]]
    assert (len(fetches), len(checks)) == (1, 1)


def test_a_stalled_download_does_not_silence_the_reminder(world: World) -> None:
    stalled = world.downloads / "bot-eod-report-2026-11-18.zip.crdownload"
    stalled.write_bytes(b"part")
    two_hours_ago = at("2026-11-18", 18, 30).timestamp()
    os.utime(stalled, (two_hours_ago, two_hours_ago))

    world.sweep(at("2026-11-18", 20, 30))

    assert [c for c in world.runner.calls if c[0] == "open"] == [["open", nightly.DOWNLOAD_PAGE]]
    assert "stalled" in world.told()


def test_an_ingest_of_several_files_is_logged(world: World) -> None:
    world.runner.ingest = nightly.Result(0, "  bot-eod-report-2026-11-18.zip ... ingested\n\n10 ingested, 0 skipped, 0 failed.")

    world.sweep(at("2026-11-18", 19, 0))

    assert any("10 ingested" in line for line in world.logs)


def test_a_sweep_that_cannot_start_is_told_once_a_day(tmp_path: Path) -> None:
    notes: list[tuple[str, str]] = []
    state = tmp_path / "state.json"

    first = nightly.last_resort("ImportError: engine.calendar", lambda t, m: notes.append((t, m)), state, date(2026, 11, 18))
    nightly.last_resort("ImportError: engine.calendar", lambda t, m: notes.append((t, m)), state, date(2026, 11, 18))
    nightly.last_resort("ImportError: engine.calendar", lambda t, m: notes.append((t, m)), state, date(2026, 11, 19))

    assert first == 1
    assert len(notes) == 2
    assert "could not start" in notes[0][1]


def test_a_failing_ping_never_raises_or_logs_the_url(monkeypatch: pytest.MonkeyPatch) -> None:
    logs: list[str] = []
    secret = "https://hc-ping.com/very-secret-uuid"

    def broken(url: str, timeout: int) -> None:
        raise http.client.InvalidURL(f"URL can't contain control characters. {url!r}")

    monkeypatch.setattr(nightly.urllib.request, "urlopen", broken)

    nightly.pinger(secret, logs.append)("/fail")

    assert len(logs) == 3
    assert all("very-secret" not in line and "InvalidURL" in line for line in logs)


@pytest.mark.parametrize("out, err, expected", [
    ("https://hc-ping.com/abc\n", "security: a warning on stderr", "https://hc-ping.com/abc"),
    ("https://hc-ping.com/a b\n", "", None),
    ("https://hc-ping.com/abc\nsecond line\n", "", None),
])
def test_the_healthcheck_url_ignores_stderr_and_rejects_whitespace(out: str, err: str, expected: str | None) -> None:
    def keychain(argv: list[str], cwd: Path, timeout: int) -> nightly.Result:
        return nightly.Result(0, out, err)

    assert nightly.healthcheck_url(keychain) == expected
