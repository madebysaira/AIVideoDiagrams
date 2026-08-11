# Swimlane

**Best for:** a production flow with handoffs between roles — client, studio, and AI tools. Who waits on whom is the point.

## Layout conventions
- One horizontal lane per actor, actor label as `eyebrow` text on the left, lane separated by `rule` hairlines.
- Steps flow left → right inside lanes. Every handoff crosses a lane boundary with a vertical connector.
- Handoff nodes are where work changes hands: give the crossing arrow an `arrow-label` ("brief", "review", "approve").
- The approval gate (the step everything waits on) is `focal`. Client steps are `external`, AI steps are `primary`, studio steps are `card`.
- Keep each lane to 1–4 steps. A lane with 6 steps is two diagrams.

## Anti-patterns
- Lanes for actors who appear once. If a role does one thing, that step belongs in another lane with a label.
- Diagonal connectors between lanes. Handoffs go straight down, then straight across.
- More than 4 lanes. Beyond that, group actors.
- The focal gate on the wrong node: it must be the step that actually blocks the flow, not the most interesting one.

## Examples
- `assets/example-swimlane.html` — minimal light
- `assets/example-swimlane-dark.html` — minimal dark
