"""Resolve API keys for the enrichment scripts.

Keys are resolved, in priority order, from:
  1. the process environment
  2. this repo's ``.env`` (``REPO_ROOT/.env``)
  3. documented sibling fallbacks — only for keys we deliberately do NOT
     duplicate into this repo's ``.env`` (so a secret is never copied across
     credential stores).

No third-party dependency (``python-dotenv``) is required — ``.env`` is parsed
with a tiny stdlib reader so the scripts run on a bare Python 3.12 install.
"""

from __future__ import annotations

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# The Finnhub key lives in the sibling ``claude-trading-agents`` repo's .env.
# We point the loader at it rather than copying the secret here.
_SIBLING_ENV_FALLBACKS: dict[str, list[Path]] = {
    "FINNHUB_API_KEY": [
        Path.home() / "Development" / "claude-trading-agents" / ".env",
    ],
}


def _parse_env_file(path: Path) -> dict[str, str]:
    """Return ``{KEY: VALUE}`` for a simple ``KEY=VALUE`` .env file.

    Missing/unreadable files yield an empty dict. Comments (``#``) and blank
    lines are skipped; surrounding quotes on values are stripped.
    """
    out: dict[str, str] = {}
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return out
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key:
            out[key] = val
    return out


def get_key(name: str) -> str:
    """Resolve an API key by name. Returns ``""`` when not found anywhere."""
    env_val = os.environ.get(name, "").strip()
    if env_val:
        return env_val

    repo_val = _parse_env_file(REPO_ROOT / ".env").get(name, "").strip()
    if repo_val:
        return repo_val

    for candidate in _SIBLING_ENV_FALLBACKS.get(name, []):
        sib_val = _parse_env_file(candidate).get(name, "").strip()
        if sib_val:
            return sib_val

    return ""


def has_key(name: str) -> bool:
    """True iff ``name`` resolves to a non-empty value."""
    return bool(get_key(name))
