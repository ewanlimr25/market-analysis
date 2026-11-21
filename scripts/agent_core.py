"""What the nightly agent's parts share (scripts/nightly.py, scripts/weekly.py; findings DESIGN/120 §8, §10): a
command's result, a problem to tell, a held run's slot, the sweep's context, and the one way commands are run."""
from __future__ import annotations

import subprocess
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

NY = ZoneInfo("America/New_York")
TIMEOUT_GIT = 300
TIMEOUT_STEP = 3600
TIMED_OUT = 124  # run()'s code for a step stopped at its timeout, as timeout(1) exits
TITLE = "market-analysis nightly"
EXIT_OK, EXIT_FAILED = 0, 1


@dataclass(frozen=True)
class Result:
    code: int
    out: str  # stdout: what is parsed
    err: str = ""  # stderr

    @property
    def text(self) -> str:
        return self.out + self.err


Runner = Callable[[Sequence[str], Path, int], Result]


@dataclass(frozen=True)
class Problem:
    key: str  # the same key on two sweeps the same day is told once
    message: str
    failure: bool = True  # False: a wait, told but never a healthcheck failure
    hold: bool = False  # True: the session's own night failed, so it is held (not retried every sweep)


@dataclass(frozen=True)
class Slot:
    """Where a failed run is held in the state, and how the owner is told about it: a night, or a week's block."""
    key: str
    name: str  # "{day}" is the session
    by_hand: str


@dataclass(frozen=True)
class Context:
    repo: Path
    stocks: Path
    uw_mcp: Path
    downloads: Path
    state_file: Path
    now: datetime  # the sweep's start: its day decides what is due and what was told
    dry_run: bool
    run: Runner
    notify: Callable[[str, str], None]
    ping: Callable[[str], None]
    log: Callable[[str], None]
    clock: Callable[[], datetime]  # read again right before each truth-set build
    sleep: Callable[[float], None]
    posted: Callable[[date], str] | None = None  # "" once Yahoo has the session's close, else why; raises; None: no look
    week: Callable[[Context, dict], tuple[int, dict]] | None = None  # the weekend block after the nights, if any

    @property
    def today(self) -> date:
        return self.now.astimezone(NY).date()

    def git(self, *args: str) -> Result:
        return self.run(["git", *args], self.repo, TIMEOUT_GIT)


def _text(value: object) -> str:
    if isinstance(value, bytes):
        return value.decode("utf-8", "replace")
    return value if isinstance(value, str) else ""


def run(argv: Sequence[str], cwd: Path, timeout: int) -> Result:
    """Run a command. A timeout or a missing program comes back as a result, never an exception."""
    try:
        done = subprocess.run(list(argv), cwd=cwd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as e:
        return Result(TIMED_OUT, _text(e.stdout), f"timed out after {timeout}s\n{_text(e.stderr)}")
    except OSError as e:
        return Result(127, "", str(e))
    return Result(done.returncode, done.stdout, done.stderr)


def last_line(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip() and not line.startswith("make: ***")]
    return lines[-1][:200] if lines else "no output"


def within(path: str, paths: Sequence[str]) -> bool:
    """`path` is one of `paths` or under one of them (git's paths: no trailing slash)."""
    return any(path == p or path.startswith(p + "/") for p in paths)
