#!/usr/bin/env bash
# Resumable screenshot loop: renders every example HTML to docs/screenshots/*.png (2x).
set -u
cd "$(dirname "$0")/../skills/ai-video-diagrams/assets"
SC="$(dirname "$0")/../docs/screenshots"
mkdir -p "$SC"
for f in example-*.html; do
  png="$SC/${f%.html}.png"
  [ -f "$png" ] && continue
  chromium --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --screenshot="$png" --window-size=1296,816 "file://$PWD/$f" 2>/dev/null
  echo "done: $f"
done
echo "ALL DONE: $(ls "$SC" | wc -l) screenshots"