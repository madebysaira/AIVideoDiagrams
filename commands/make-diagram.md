---
description: Scaffold a new diagram from the template
args: type · title (e.g. "pipeline · client spot")
allowed-tools: Bash, Write, Read
---

1. Run `commands/make.sh <type> "<title>"` — this copies `assets/template.html`
   into a new file and sets the `<title>`.
2. Read `references/type-<type>.md` for the layout conventions.
3. Build the skeleton on the 4px grid (viewBox 1200 × 720): nodes first,
   labels second, connectors last.
4. Choose exactly one focal node. If you cannot name it, the diagram is
   trying to say two things — split it.
5. Keep density at 4/10. Cut labels that repeat the obvious.
6. Generate the dark variant: `python3 scripts/skin.py`.
7. Render a PNG: `bash commands/render.sh`, then look at it as a client
   would. Only then is it a diagram.

Rules that are not optional: orthogonal connectors only; arrow labels 8px
above their line; every node gets a mono sublabel; every `<svg>` gets an
`aria-label`.