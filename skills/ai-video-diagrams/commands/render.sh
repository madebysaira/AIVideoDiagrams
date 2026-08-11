#!/usr/bin/env bash
# render — produce PNGs (light + dark) for every diagram in assets/.
# Needs a headless chromium. Output lands in docs/screenshots/.
set -eu
SCRIPT_DIR="$(dirname "$0")"
bash "$SCRIPT_DIR/../../scripts/screenshots.sh"
echo "rendered. Preview: open docs/screenshots/*.png"