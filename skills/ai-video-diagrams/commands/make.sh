#!/usr/bin/env bash
# make — scaffold a new diagram from the template.
# Usage: ./commands/make.sh pipeline "client spot · 15s"
# Creates assets/<slug>.html by copying template.html and setting the title.
set -eu
TYPE="${1:?usage: make.sh <type> <title>}"
TITLE="${2:-untitled}"
SLUG="${TYPE}-$(echo "$TITLE" | tr '[:upper:] ·' '[:lower:]---' | tr -cs 'a-z0-9-' '-')"
ASSETS="$(dirname "$0")/../assets"
sed -e "s|<title>Template — AIVideoDiagrams</title>|<title>${TITLE} — AIVideoDiagrams</title>|" \
    "$ASSETS/template.html" > "$ASSETS/$SLUG.html"
echo "created $ASSETS/$SLUG.html — copy nodes from references/type-${TYPE}.md"
echo "after editing: python3 $(dirname "$0")/../../scripts/skin.py"