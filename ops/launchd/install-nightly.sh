#!/bin/bash
# Install, reinstall or remove the nightly LaunchAgent (scripts/nightly.py; docs/OPERATING.md §1).
#   ops/launchd/install-nightly.sh            install the live agent
#   ops/launchd/install-nightly.sh --dry-run  install it as a dry run: the ingest, then only what it would run
#   ops/launchd/install-nightly.sh --remove   stop it and remove the installed copy
# The committed plist is a template with no local path in it; this fills in this Mac's paths.
set -euo pipefail

LABEL=com.market-analysis.nightly
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"
DOMAIN="gui/$(id -u)"

case "${1:-}" in
  --remove)
    launchctl bootout "$DOMAIN/$LABEL" 2>/dev/null || true
    rm -f "$DEST"
    echo "removed $LABEL"
    exit 0 ;;
  --dry-run) DRY=1 ;;
  "") DRY=0 ;;
  *) echo "usage: $0 [--dry-run | --remove]" >&2; exit 2 ;;
esac

PYTHON="$(cd "$REPO" && { pyenv which python3 2>/dev/null || command -v python3; })"
mkdir -p "$REPO/data/logs" "$HOME/Library/LaunchAgents"
sed -e "s#__HOME__#$HOME#g" -e "s#__REPO__#$REPO#g" -e "s#__PYTHON__#$PYTHON#g" -e "s#__DRY_RUN__#$DRY#g" \
  "$REPO/ops/launchd/$LABEL.plist" > "$DEST"
plutil -lint -s "$DEST"
launchctl bootout "$DOMAIN/$LABEL" 2>/dev/null || true
launchctl bootstrap "$DOMAIN" "$DEST" 2>/dev/null || { sleep 2; launchctl bootstrap "$DOMAIN" "$DEST"; }
echo "installed $LABEL (dry run: $DRY), running $PYTHON"
echo "a first sweep now:  launchctl kickstart $DOMAIN/$LABEL"
echo "what it did:        tail -n 40 $REPO/data/logs/nightly.log"
