---
description: Run the review gate over every diagram
allowed-tools: Bash
---

Run `bash commands/review.sh` from the skill root. The gate checks, for
every example and the template:

- exactly one `class="focal"` node per diagram
- an `aria-label` on every `<svg>`
- a dark variant that exists and is newer than its light source (`skin.py`)

The gate is the machine half of the review. The human half is taste: open
the PNGs, and ask — one focal node and it is the right one; every label
clear of every line; density low enough to breathe. If the gate passes but
the taste test fails, fix the taste and re-render. Both pass before
anything ships to a client.