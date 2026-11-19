"""The nightly on its own: from tonight's Unusual Whales zips to the pushed `daily:` commit.

Run by the LaunchAgent `com.market-analysis.nightly` (install with `ops/launchd/install-nightly.sh`), never by
`make daily` (findings market-analysis DESIGN/120 §4(2), §8; D41, D42). Each sweep:

1. moves the downloaded zips into the panel (`convert.py --ingest` in unusual-whales-mcp);
2. for each session after the last committed `analyses/daily/<date>/` whose five files are in the panel, oldest
   first and stopping at the first that is not, runs the truth-set rebuild (last session of the week only), then
   `make daily DATE=<session>`, then commits that session's outputs under `analyses/daily` and `ledger` alone as
   `daily: <session>`;
3. pushes the checked tip of `main` when every commit ahead of `origin/main` is such a commit; it never pulls;
4. tells the owner: a macOS notification, and a healthchecks.io ping when the keychain holds the check's URL.

Before each session it looks again, and runs nothing, if `analyses/daily` or `ledger` hold uncommitted changes (a hand
run), if the code does (`engine/`, `scripts/`, `schemas/`, `Makefile`), if a git operation is underway, or off
`main`. A session whose night fails is held: one more try two hours later, then none until HEAD moves. Each
problem is told once a day. At 20:05 on a session day with tonight's files neither in the panel nor downloading,
it posts a reminder and opens the download page. The download itself stays a hand job (Unusual Whales' terms §4(D)).

    python3 scripts/nightly.py             # what the agent runs (MA_NIGHTLY_DRY_RUN=1 makes it a dry run)
    python3 scripts/nightly.py --dry-run   # the ingest, then only what it would run: no make daily, commit or push
"""
from __future__ import annotations

import argparse
import fcntl
import json
import os
import re
import subprocess
import sys
import traceback
import urllib.request
from collections.abc import Callable, Iterator, Sequence
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from pathlib import Path
from time import sleep
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))  # run as a script, `engine` must still import

try:  # a broken engine must still reach the owner: main() tells them instead of dying in a log
    from engine import calendar as cal
    from engine import config
except Exception as _error:  # noqa: BLE001
    IMPORT_ERROR: str | None = f"{type(_error).__name__}: {_error}"
else:
    IMPORT_ERROR = None

NY = ZoneInfo("America/New_York")
STOCKS = Path(config.STOCKS) if IMPORT_ERROR is None else Path.home() / "Documents" / "Stocks"
UW_MCP = Path(os.path.expanduser(os.environ.get("UW_MCP_DIR", "~/Development/unusual-whales-mcp")))
DOWNLOADS = Path.home() / "Downloads"
LOGS = REPO / "data" / "logs"

PANEL_FILES = {
    "All Options": "bot-eod-report",
    "Dark pool": "dp-eod-report",
    "Hot Option Chains": "hot-chains",
    "OI changes": "chain-oi-changes",
    "Stock Screener": "stock-screener",
}
NIGHT_PATHS = ("analyses/daily", "ledger")  # all a night commits
CODE_PATHS = ("engine", "scripts", "schemas", "Makefile")  # a night never runs on uncommitted code
NIGHT_SUBJECT = re.compile(r"daily: \d{4}-\d{2}-\d{2}")
NIGHT_DIR = re.compile(r"analyses/daily/(\d{4}-\d{2}-\d{2})")
IN_PROGRESS = ("MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD", "rebase-merge", "rebase-apply", "BISECT_LOG")
TRUTH_SET_BUILDS = (
    "scripts/truthset/build_prices.py",
    "scripts/truthset/build_returns.py",
    "scripts/truthset/build_features.py",
)
STALE_TRUTH_MARK = "the truth set does not reach it"  # engine/daily.py's STOP line (D40)
SCHEMA_WARNING_MARK = "WARN signals.json does not match"
NOTHING_INGESTED = re.compile(r"^0 ingested, 0 skipped, 0 failed\.$", re.M)
HEALTHCHECK_URL = re.compile(r"https://\S+")
DOWNLOAD_PAGE = "https://unusualwhales.com/data/download"
REMIND_FROM = time(20, 5)  # New York; the export lands around 8 PM
NO_REBUILD_FROM = time(9, 0)  # to the session's close (16:15): a rebuild would file the unfinished bar (D35, D36)
STALLED_AFTER = timedelta(minutes=30)  # a .crdownload untouched this long no longer counts as downloading
RETRY_AFTER = timedelta(hours=2)
MAX_ATTEMPTS = 2  # a failed session is tried at most twice before HEAD moves
LOCK_RETRIES, LOCK_PAUSE = 5, 2.0  # git add/commit against another process's index.lock (an editor's git status)
CALENDAR_WARNING = timedelta(days=30)
HEALTHCHECK_ITEM = "market-analysis-nightly-healthcheck"  # the keychain item holding the check's ping URL
INGEST_BUSY = 3  # convert.py --ingest: another ingest holds its lock
TIMEOUT_GIT = 300
TIMEOUT_STEP = 3600
TIMED_OUT = 124  # run()'s code for a step stopped at its timeout, as timeout(1) exits
INGEST_TIMED_OUT = (  # the likeliest cause: macOS's privacy prompt with nobody there to answer it (D42)
    f"the ingest was stopped after {TIMEOUT_STEP // 60} min. If macOS is asking whether Python may use Downloads or "
    f"Documents, click Allow (or add {sys.executable} under Privacy & Security → Full Disk Access)"
)
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


def _last_line(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip() and not line.startswith("make: ***")]
    return lines[-1][:200] if lines else "no output"


# ---- git ----------------------------------------------------------------------------------------


def changed(ctx: Context, *paths: str) -> list[str] | None:
    """Changed paths under `paths`, untracked ones included whatever the git config says; None if git fails."""
    result = ctx.git("status", "--porcelain", "--untracked-files=all", "--", *paths)
    if result.code != 0:
        return None
    return [line[3:] for line in result.out.splitlines() if line.strip()]


def current_branch(ctx: Context) -> str:
    return ctx.git("rev-parse", "--abbrev-ref", "HEAD").out.strip()


def head(ctx: Context) -> str:
    return ctx.git("rev-parse", "HEAD").out.strip()


def operation_underway(ctx: Context) -> str:
    """A merge, cherry-pick, revert, rebase or bisect in progress, by the file git keeps for it."""
    found = ctx.git("rev-parse", "--git-dir").out.strip() or ".git"
    git_dir = Path(found) if Path(found).is_absolute() else ctx.repo / found
    return next((name for name in IN_PROGRESS if (git_dir / name).exists()), "")


def shas(ctx: Context, spec: str) -> list[str] | None:
    result = ctx.git("rev-list", "--reverse", spec)
    return result.out.split() if result.code == 0 else None


def git_retrying(ctx: Context, *args: str) -> Result:
    """git, retried a few times while another process holds the index lock."""
    result = ctx.git(*args)
    for _ in range(LOCK_RETRIES):
        if result.code == 0 or "index.lock" not in result.text:
            break
        ctx.sleep(LOCK_PAUSE)
        result = ctx.git(*args)
    return result


# ---- what is due --------------------------------------------------------------------------------


def missing_files(stocks: Path, day: date) -> list[str]:
    return [
        folder
        for folder, prefix in PANEL_FILES.items()
        if not (stocks / folder / f"{prefix}-{day.isoformat()}.parquet").exists()
    ]


def last_committed_night(repo: Path, runner: Runner) -> date | None:
    """The latest session with a committed `analyses/daily/<date>/`; an untracked folder does not count."""
    listing = runner(["git", "ls-tree", "--name-only", "HEAD", "analyses/daily/"], repo, TIMEOUT_GIT)
    if listing.code != 0:
        return None
    days = []
    for line in listing.out.splitlines():
        match = NIGHT_DIR.fullmatch(line.strip())
        if match is None:
            continue
        try:
            days.append(date.fromisoformat(match[1]))
        except ValueError:
            continue
    return max(days, default=None)


def sessions_due(ctx: Context) -> tuple[list[date], Problem | None]:
    """The sessions after the last committed night whose five files are in the panel, oldest first, up to the
    first that is not. A missing session is a problem only when a later one is complete; tonight's is normal."""
    last = last_committed_night(ctx.repo, ctx.run)
    if last is None:
        return [], Problem("no-night", "no committed analyses/daily/<date>/ found, so nothing was run")
    days = cal.trading_days(cal.next_session(last), ctx.today)
    due: list[date] = []
    for i, day in enumerate(days):
        missing = missing_files(ctx.stocks, day)
        if not missing:
            due.append(day)
            continue
        if any(not missing_files(ctx.stocks, later) for later in days[i + 1 :]):
            return due, Problem(
                f"gap:{day}",
                f"{day} is not in the panel (missing {', '.join(missing)}), so the sessions after it wait",
            )
        break
    return due, None


def calendar_problem(ctx: Context) -> Problem | None:
    """The engine's holiday list ends; past it every holiday would look like a missing session."""
    end = cal.CALENDAR_END
    if ctx.today > end:
        return Problem("calendar", f"the engine's holiday calendar ends {end}; no night runs until "
                                   "engine/calendar.py is extended")
    if ctx.today >= end - CALENDAR_WARNING:
        return Problem("calendar-soon", f"the engine's holiday calendar ends {end}; extend engine/calendar.py "
                                        "before then, or the agent stops", failure=False)
    return None


def refusal(ctx: Context) -> Problem | None:
    """Why no night may run now: another branch, a git operation underway, a hand run, or uncommitted code."""
    branch = current_branch(ctx)
    if branch != "main":
        return Problem(f"branch:{branch}", f"the repo is on {branch or 'an unknown branch'}, not main; nothing was run")
    underway = operation_underway(ctx)
    if underway:
        return Problem(f"underway:{underway}", f"a git operation is underway ({underway}); nothing was run")
    for paths in (NIGHT_PATHS, CODE_PATHS):
        found = changed(ctx, *paths)
        if found is None:
            return Problem("status", "git status failed; nothing was run")
        if found:
            shown = ", ".join(found[:4]) + (" ..." if len(found) > 4 else "")
            return Problem(f"dirty:{shown}", f"uncommitted changes in {shown}; nothing was run")
    return None


# ---- one session --------------------------------------------------------------------------------


def no_rebuild_now(now: datetime) -> bool:
    local = now.astimezone(NY)
    session = local.date()
    return cal.is_trading_day(session) and local.time() >= NO_REBUILD_FROM and not cal.session_closed(session, now)


def rebuild_truth_set(ctx: Context, day: date) -> Problem | None:
    """The last session of the week settles on the official close, so the truth set must reach it (D39, D40).
    It is never rebuilt from 09:00 to a session's close: that would file the unfinished bar. The clock is read
    before each build, since a sweep can start before 09:00 or resume after a sleep."""
    for script in TRUTH_SET_BUILDS:
        if no_rebuild_now(ctx.clock()):
            return Problem(
                f"truth-wait:{day}",
                f"{day} is the last session of its week, and the truth set is rebuilt only after today's close "
                "(16:15), so it waits",
                failure=False,
            )
        if ctx.dry_run:
            return None
        result = ctx.run([sys.executable, script], ctx.repo, TIMEOUT_STEP)
        ctx.log(result.text)
        if result.code != 0:
            return Problem(
                f"truth:{day}",
                f"{day}: {script} failed (exit {result.code}): {_last_line(result.text)}; nothing was committed",
                hold=True,
            )
    return None


def summary(repo: Path, day: date) -> str:
    """The S-B gate and S-A's candidate count from the session's signals.json."""
    try:
        signals = json.loads((repo / "analyses" / "daily" / day.isoformat() / "signals.json").read_text())
        gate = signals.get("sb_state", {}).get("gate", {})
        gates = ", ".join(f"{ticker} {'ON' if g.get('on') else 'OFF'}" for ticker, g in gate.items())
        return f"S-B gate {gates or 'unknown'}; {len(signals.get('candidates', []))} S-A candidates"
    except (OSError, ValueError, AttributeError, TypeError) as e:
        return f"summary unavailable ({type(e).__name__})"


def daily_problem(day: date, result: Result) -> Problem:
    if STALE_TRUTH_MARK in result.text:
        return Problem(
            f"daily:{day}",
            f"{day}: the truth set does not reach it, so nothing was committed. Rebuild and rerun by hand, or run "
            f"make daily DATE={day} ALLOW_STALE_TRUTH=1 and note it in findings (D40)",
            hold=True,
        )
    return Problem(
        f"daily:{day}",
        f"{day}: make daily failed (exit {result.code}): {_last_line(result.text)}; nothing was committed",
        hold=True,
    )


def commit(ctx: Context, day: date) -> Problem | None:
    """Commit the session's outputs alone, and only when nothing else changed while its night ran. The pathspec
    keeps anything else that is staged out of the commit, and git refuses it during a merge."""
    code = changed(ctx, *CODE_PATHS)
    if code is None or code:
        shown = ", ".join((code or ["git status failed"])[:3])
        return Problem(f"code-moved:{day}", f"{day}: the code changed while the night ran ({shown}), so its "
                                            "outputs are left uncommitted for you to look at", hold=True)
    mine = f"analyses/daily/{day.isoformat()}/"
    foreign = [p for p in changed(ctx, *NIGHT_PATHS) or [] if p.startswith("analyses/daily/") and not p.startswith(mine)]
    if foreign:
        return Problem(f"foreign:{day}", f"{day}: another night's files appeared while it ran "
                                         f"({', '.join(foreign[:3])}), so nothing was committed", hold=True)
    for args in (("add", "--", *NIGHT_PATHS), ("commit", "-q", "-m", f"daily: {day}", "--", *NIGHT_PATHS)):
        result = git_retrying(ctx, *args)
        if result.code != 0:
            return Problem(f"commit:{day}", f"{day}: git {args[0]} failed ({_last_line(result.text)}); the "
                                            "outputs are left uncommitted", hold=True)
    return None


def run_session(ctx: Context, day: date) -> tuple[str, Problem | None]:
    """One session's nightly and its commit: (the line to tell, a problem that stops the night)."""
    from engine.daily import is_last_session_of_week  # about a second of imports, paid only when a session is due

    rebuild = is_last_session_of_week(day)
    if rebuild:
        problem = rebuild_truth_set(ctx, day) or refusal(ctx)  # the rebuild takes minutes: look again after it
        if problem is not None:
            return "", problem
    if ctx.dry_run:
        first = "rebuild the truth set, then " if rebuild else ""
        return f"{day}: would {first}run make daily DATE={day}, then commit it", None
    result = ctx.run(["make", "daily", f"DATE={day}"], ctx.repo, TIMEOUT_STEP)
    ctx.log(result.text)
    if result.code != 0:
        return "", daily_problem(day, result)
    problem = commit(ctx, day)
    if problem is not None:
        return "", problem
    warning = "; WARN: signals.json does not match its schema" if SCHEMA_WARNING_MARK in result.text else ""
    return f"{day} committed: {summary(ctx.repo, day)}{warning}", None


# ---- holding a failed session -------------------------------------------------------------------


def hold_status(ctx: Context, state: dict, day: date) -> tuple[bool, Problem | None]:
    """(skip it, what to tell) for a session whose night failed before. It gets one more try after RETRY_AFTER,
    then none until HEAD moves (the owner committed a fix, or the night by hand)."""
    held = state.get("held") or {}
    if held.get("session") != day.isoformat() or held.get("head") != head(ctx):
        return False, None
    attempts = int(held.get("attempts", 0))
    if attempts >= MAX_ATTEMPTS:
        return True, Problem(
            f"held:{day}",
            f"{day} is held after {attempts} failed tries ({held.get('reason', 'see the log')}). Commit a fix or "
            "run the night by hand; the agent tries again once HEAD moves",
        )
    return ctx.now < datetime.fromisoformat(held["retry_after"]), None


def hold(ctx: Context, state: dict, day: date, problem: Problem) -> dict:
    held = state.get("held") or {}
    same = held.get("session") == day.isoformat() and held.get("head") == head(ctx)
    attempts = int(held.get("attempts", 0)) + 1 if same else 1
    entry = {"session": day.isoformat(), "head": head(ctx), "attempts": attempts,
             "retry_after": (ctx.now + RETRY_AFTER).isoformat(), "reason": problem.message[:200]}
    return {**state, "held": entry}


def release(state: dict, day: date) -> dict:
    held = state.get("held") or {}
    return {k: v for k, v in state.items() if k != "held"} if held.get("session") == day.isoformat() else state


def run_nights(ctx: Context, state: dict) -> tuple[list[str], list[Problem], dict]:
    """Every due session in order, each behind a fresh look at the repo, stopping at the first that cannot run."""
    due, gap = sessions_due(ctx)
    lines: list[str] = []
    problems: list[Problem] = []
    for day in due:
        skip, told = hold_status(ctx, state, day)
        if skip:
            problems += [told] if told is not None else []
            break
        blocked = refusal(ctx)
        if blocked is not None:
            problems.append(blocked)
            break
        line, problem = run_session(ctx, day)
        lines += [line] if line else []
        if problem is None:
            state = release(state, day)
            continue
        problems.append(problem)
        state = hold(ctx, state, day, problem) if problem.hold else state
        break
    return lines, problems + ([gap] if gap is not None else []), state


# ---- the push -----------------------------------------------------------------------------------


def stranger(ctx: Context, shas_ahead: Sequence[str]) -> str:
    """The first commit that is not a nightly one: a merge, another subject, or a file outside the night's paths."""
    for sha in shas_ahead:
        subject = ctx.git("log", "-1", "--format=%s", sha).out.strip()
        if len(ctx.git("log", "-1", "--format=%P", sha).out.split()) > 1:
            return f"{sha[:7]} '{subject}' (a merge commit)"
        files = ctx.git("diff-tree", "--no-commit-id", "--name-only", "-r", sha).out.splitlines()
        outside = [f for f in files if f and not f.startswith(("analyses/daily/", "ledger/"))]
        if not NIGHT_SUBJECT.fullmatch(subject) or outside:
            touches = f" (it touches {', '.join(outside[:3])})" if outside else ""
            return f"{sha[:7]} '{subject}'{touches}"
    return ""


def push(ctx: Context, probe: bool) -> tuple[str, Problem | None]:
    """Push the checked tip of `main` when every commit ahead of `origin/main` is a nightly one; never pull.
    `probe` (a dry run, once a day) checks the credentials even with nothing to push. (line, problem)."""
    if shas(ctx, "origin/main..main") == [] and not probe:
        return "", None  # nothing ahead of what origin last showed: no network
    if current_branch(ctx) != "main" or operation_underway(ctx):
        return "", None  # the owner is mid-operation; nothing is pushed until it is done
    fetch = ctx.git("fetch", "-q", "origin", "main")
    if fetch.code != 0:
        return "", Problem("fetch", f"git fetch failed ({_last_line(fetch.text)}); the push waits for the next sweep")
    behind = ctx.git("rev-list", "--count", "main..origin/main")
    if behind.code != 0 or behind.out.strip() != "0":
        count = behind.out.strip() if behind.code == 0 else "an unknown number of"
        return "", Problem("behind", f"origin/main has {count} commit(s) this Mac lacks; the agent never pulls, "
                                     "so push by hand")
    ahead = shas(ctx, "origin/main..main")
    if ahead is None:
        return "", Problem("compare", "could not compare main with origin/main; nothing was pushed")
    odd = stranger(ctx, ahead)
    if odd:
        return "", Problem(f"stranger:{odd}", f"not pushed: {odd} is not a nightly commit; push by hand")
    target = f"{ahead[-1]}:refs/heads/main" if ahead else "main"
    if ctx.dry_run:
        check = ctx.git("push", "--dry-run", "origin", target)
        if check.code != 0:
            return "", Problem("push-check", f"git push --dry-run failed ({_last_line(check.text)}), so a live "
                                             "night could not push")
        ctx.log("git push --dry-run works")
        return (f"would push {len(ahead)} commit(s)" if ahead else ""), None
    if not ahead:
        return "", None
    result = ctx.git("push", "-q", "origin", target)
    if result.code != 0:
        return "", Problem("push", f"git push failed ({_last_line(result.text)}); the next sweep retries")
    return f"pushed {len(ahead)} commit(s)", None


# ---- the ingest, the evening, the telling -------------------------------------------------------


def ingest_key(failed: Sequence[str]) -> str:
    """The same failure on two sweeps gets the same key, even when its message carries changing numbers."""
    zips = sorted({name for line in failed for name in re.findall(r"[\w.-]+\.zip", line)})
    return "ingest:" + (",".join(zips) if zips else re.sub(r"\d+", "#", "; ".join(failed)))


def ingest(ctx: Context) -> Problem | None:
    venv = ctx.uw_mcp / ".venv" / "bin" / "python"
    python = str(venv) if venv.exists() else sys.executable
    result = ctx.run([python, "convert.py", "--ingest", str(ctx.downloads)], ctx.uw_mcp, TIMEOUT_STEP)
    if result.code != 0 or "[" in result.text or not NOTHING_INGESTED.search(result.text):
        ctx.log(result.text)  # a sweep with nothing to ingest leaves no lines
    if result.code in (0, INGEST_BUSY):
        return None
    if result.code == TIMED_OUT:
        return Problem("ingest:timed out", INGEST_TIMED_OUT)
    failed = [line.strip() for line in result.text.splitlines() if "FAILED" in line]
    detail = "; ".join(failed[:3]) or _last_line(result.text)
    return Problem(ingest_key(failed or [detail]), f"the ingest kept something back: {detail}")


def tonights_downloads(ctx: Context, session: date) -> tuple[bool, bool]:
    """(any of tonight's files in Downloads, any of them fresh). A .crdownload untouched for STALLED_AFTER is stale."""
    try:
        entries = [entry for entry in os.scandir(ctx.downloads)
                   if entry.name.startswith(tuple(PANEL_FILES.values())) and session.isoformat() in entry.name]
        ages = [(entry.name, ctx.now.timestamp() - entry.stat().st_mtime) for entry in entries]
    except OSError:
        return True, True  # unreadable: the ingest says so; no reminder on top
    fresh = [n for n, age in ages if not n.endswith(".crdownload") or age < STALLED_AFTER.total_seconds()]
    return bool(ages), bool(fresh)


def reminder(ctx: Context) -> str:
    """The reminder to post now, if any: a session evening from 20:05 with tonight's files neither in the panel nor
    downloading (a stalled download does not count)."""
    local = ctx.now.astimezone(NY)
    session = local.date()
    if not cal.is_trading_day(session) or local.time() < REMIND_FROM or not missing_files(ctx.stocks, session):
        return ""
    present, fresh = tonights_downloads(ctx, session)
    if fresh:
        return ""
    stalled = "; one seems to have stalled in Downloads" if present else ""
    return f"Unusual Whales: tonight's five files are ready to download{stalled}; the rest runs by itself"


def holiday_evening(ctx: Context) -> bool:
    local = ctx.now.astimezone(NY)
    return local.weekday() < 5 and not cal.is_trading_day(local.date()) and local.time() >= REMIND_FROM


def evening(ctx: Context, state: dict, ok: bool) -> dict:
    """The reminder, and the holiday's healthcheck ping (the check expects one every weekday evening); a sweep that
    failed never pings success."""
    today = ctx.today.isoformat()
    message = reminder(ctx) if state.get("reminded") != today and ctx.today <= cal.CALENDAR_END else ""
    if message:
        ctx.notify(TITLE, message)
        ctx.run(["open", DOWNLOAD_PAGE], ctx.repo, TIMEOUT_GIT)
        state = {**state, "reminded": today}
    if ok and state.get("holiday_ping") != today and holiday_evening(ctx) and not ctx.dry_run:
        ctx.log("a market holiday: the healthcheck is told all is well")
        ctx.ping("")
        state = {**state, "holiday_ping": today}
    return state


def tell(ctx: Context, state: dict, lines: list[str], pushed: str, problems: list[Problem]) -> tuple[int, dict]:
    """Notify what happened, each problem once a day, and ping the healthcheck. Returns (exit code, new state)."""
    today = ctx.today.isoformat()
    told = set(state.get("told", [])) if state.get("day") == today else set()
    news = "; ".join([*lines, pushed] if pushed else lines)
    keys: set[str] = set()
    if news and not ctx.dry_run:
        ctx.notify(TITLE, news)
    elif news and f"dry:{news}" not in told:  # a dry run commits nothing, so the same news would recur every sweep
        ctx.notify(TITLE, f"dry run: {news}")
        keys.add(f"dry:{news}")
    fresh = [p for p in problems if p.key not in told]
    for problem in fresh:
        ctx.notify(f"{TITLE}: needs a look" if problem.failure else TITLE, problem.message)
    if not ctx.dry_run and any(p.failure for p in fresh):
        ctx.ping("/fail")
    elif not ctx.dry_run and news and not problems:
        ctx.ping("")
    code = EXIT_FAILED if any(p.failure for p in problems) else EXIT_OK
    return code, {**state, "day": today, "told": sorted(told | keys | {p.key for p in fresh})}


def sweep(ctx: Context, state: dict) -> tuple[int, dict]:
    problems = [p for p in (ingest(ctx), calendar_problem(ctx)) if p is not None]
    lines: list[str] = []
    if not any(p.key == "calendar" for p in problems):
        lines, found, state = run_nights(ctx, state)
        problems += found
    probe = ctx.dry_run and state.get("push_check") != ctx.today.isoformat()
    pushed, push_problem = push(ctx, probe)
    problems += [push_problem] if push_problem is not None else []
    state = {**state, "push_check": ctx.today.isoformat()} if probe else state
    code, state = tell(ctx, state, lines, pushed, problems)
    return code, evening(ctx, state, ok=code == EXIT_OK)


def load_state(path: Path) -> dict:
    try:
        state = json.loads(path.read_text())
    except (OSError, ValueError):
        return {}
    return state if isinstance(state, dict) else {}


def save_state(path: Path, state: dict) -> None:
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(state, indent=1))
    os.replace(tmp, path)


def run_agent(ctx: Context) -> int:
    """One sweep that always tells the owner what went wrong, a crash included."""
    state = load_state(ctx.state_file)
    try:
        code, state = sweep(ctx, state)
    except Exception as e:  # unattended: a crash must reach the owner, not only the log
        ctx.log(traceback.format_exc())
        crash = Problem(f"crash:{type(e).__name__}: {e}", f"the nightly crashed: {type(e).__name__}: {e}")
        code, state = tell(ctx, state, [], "", [crash])
    save_state(ctx.state_file, state)
    return code


def last_resort(message: str, notify: Callable[[str, str], None], state_file: Path, today: date) -> int:
    """Tell the owner, once a day, when a sweep cannot even start (an engine that does not import, an unwritable
    log folder). launchd's own log, data/logs/launchd-nightly.err, keeps the traceback."""
    state = load_state(state_file)
    told = set(state.get("told", [])) if state.get("day") == today.isoformat() else set()
    key = f"start:{message}"
    if key not in told:
        notify(f"{TITLE}: needs a look", f"the nightly could not start: {message}")
        try:
            save_state(state_file, {**state, "day": today.isoformat(), "told": sorted(told | {key})})
        except OSError as e:  # the owner was told already; the next sweep tells them again
            print(f"could not save {state_file}: {e}", file=sys.stderr)
    return EXIT_FAILED


# ---- the real world -----------------------------------------------------------------------------


@contextmanager
def exclusive(path: Path) -> Iterator[bool]:
    """True while this process holds the sweep lock; False when another sweep holds it."""
    fd = os.open(path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            yield False
            return
        yield True
    finally:
        os.close(fd)


def healthcheck_url(runner: Runner) -> str | None:
    """The check's ping URL from the login keychain (stdout only); it is never written to a file or a log."""
    found = runner(["security", "find-generic-password", "-s", HEALTHCHECK_ITEM, "-w"], Path.home(), TIMEOUT_GIT)
    url = found.out.strip()
    return url if found.code == 0 and HEALTHCHECK_URL.fullmatch(url) else None


def file_logger(path: Path) -> Callable[[str], None]:
    def log(message: str) -> None:
        if not message.strip():
            return
        stamp = datetime.now(NY).strftime("%Y-%m-%d %H:%M:%S")
        with path.open("a", encoding="utf-8") as fh:
            fh.writelines(f"{stamp}  {line}\n" for line in message.rstrip().splitlines())

    return log


def mac_notifier(log: Callable[[str], None]) -> Callable[[str, str], None]:
    def notify(title: str, message: str) -> None:
        log(f"told: {title}: {message}")
        script = ("-e", "on run argv", "-e", "display notification (item 2 of argv) with title (item 1 of argv)",
                  "-e", "end run")
        result = run(["osascript", *script, title, message[:900]], Path.home(), TIMEOUT_GIT)
        if result.code != 0:
            log(f"the notification failed: {_last_line(result.text)}")

    return notify


def pinger(url: str | None, log: Callable[[str], None]) -> Callable[[str], None]:
    def ping(suffix: str) -> None:
        if url is None:
            log(f"healthcheck not configured (keychain item {HEALTHCHECK_ITEM}); no ping")
            return
        for attempt in (1, 2, 3):
            try:
                with urllib.request.urlopen(url + suffix, timeout=10) as response:
                    log(f"healthcheck {suffix or 'success'}: HTTP {response.status}")
                    return
            except Exception as e:  # noqa: BLE001  never raise, and never log the URL (it is in some messages)
                log(f"healthcheck {suffix or 'success'}, attempt {attempt}: {type(e).__name__}")

    return ping


def stay_awake(log: Callable[[str], None]) -> None:
    """Hold off idle sleep until this process exits (caffeinate -w), as com.desk.export-odte does."""
    try:
        subprocess.Popen(["caffeinate", "-i", "-w", str(os.getpid())],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except OSError as e:
        log(f"caffeinate unavailable: {e}")


def sweep_once(dry_run: bool) -> int:
    LOGS.mkdir(parents=True, exist_ok=True)
    log = file_logger(LOGS / "nightly.log")
    with exclusive(LOGS / "nightly.lock") as held:
        if not held:
            return EXIT_OK  # a sweep is already running; launchd fires again soon
        stay_awake(log)
        ctx = Context(
            repo=REPO, stocks=STOCKS, uw_mcp=UW_MCP, downloads=DOWNLOADS, state_file=LOGS / "nightly-state.json",
            now=datetime.now(NY), dry_run=dry_run, run=run, notify=mac_notifier(log),
            ping=pinger(healthcheck_url(run), log), log=log, clock=lambda: datetime.now(NY), sleep=sleep,
        )
        code = run_agent(ctx)
        if code != EXIT_OK:
            log(f"sweep exit {code}{' (dry run)' if dry_run else ''}")
        return code


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="market-analysis's nightly on its own (DESIGN/120)")
    parser.add_argument("--dry-run", action="store_true",
                        help="ingest, then only say what would run: no make daily, commit or push")
    args = parser.parse_args(argv)
    dry_run = args.dry_run or os.environ.get("MA_NIGHTLY_DRY_RUN") == "1"
    today, notify, state_file = datetime.now(NY).date(), mac_notifier(lambda _message: None), LOGS / "nightly-state.json"
    if IMPORT_ERROR is not None:
        return last_resort(f"the engine does not import ({IMPORT_ERROR})", notify, state_file, today)
    try:
        return sweep_once(dry_run)
    except Exception as e:  # noqa: BLE001  before run_agent's own guard: the log or the lock could not open
        traceback.print_exc()
        return last_resort(f"{type(e).__name__}: {e}", notify, state_file, today)


if __name__ == "__main__":
    raise SystemExit(main())
