#!/usr/bin/env bash
# review — the operator's checklist as a gate.
# Runs the same checks the human runs, so the human only checks taste.
set -u
ASSETS="$(dirname "$0")/../assets"
FAIL=0
for f in "$ASSETS"/example-*.html "$ASSETS"/template.html; do
  case "$f" in *\dark\.html) continue;; esac
  # 1. exactly one .focal node
  n=$(grep -o 'class="focal"' "$f" | wc -l)
  [ "$n" -eq 1 ] || { echo "FAIL $f: $n focal nodes (want exactly 1)"; FAIL=1; }
  # 2. every svg has an aria-label
  grep -q 'aria-label' "$f" || { echo "FAIL $f: missing aria-label"; FAIL=1; }
  # 3. dark variant exists and is newer than the light source
  dark="${f%.html}-dark.html"
  [ -f "$dark" ] || { echo "FAIL $f: no dark variant — run scripts/skin.py"; FAIL=1; }
  [ "$f" -ot "$dark" ] || { echo "FAIL $f: dark variant stale — run scripts/skin.py"; FAIL=1; }
done
[ "$FAIL" -eq 0 ] && echo "review gate passed: every diagram ships with 1 focal node, an aria-label, and a fresh dark variant."
exit "$FAIL"