#!/bin/zsh
# Local daily Binance Square short posts for ccprivacy ZH news.
# Uses ~/.config/binance-square/openapi-key (or BINANCE_SQUARE_OPENAPI_KEY).
set -euo pipefail

REPO="/Volumes/BTC/Home/cursor AI/canton-edu"
LOG_DIR="${HOME}/Library/Logs/canton-edu"
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/square-digest.log"

{
  echo "==== $(date '+%Y-%m-%d %H:%M:%S %z') ===="
  cd "$REPO"
  git fetch origin main >/dev/null 2>&1 || true
  git checkout main >/dev/null 2>&1 || true
  git pull --ff-only origin main >/dev/null 2>&1 || true
  /usr/bin/env node scripts/binance-square-daily-digest.mjs --publish
  echo "done"
} >>"$LOG" 2>&1
