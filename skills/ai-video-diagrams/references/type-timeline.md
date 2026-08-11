# Timeline

**Best for:** events positioned in time — production schedule, shot order, a campaign's drop dates.

## Layout conventions
- A horizontal `rule-solid` baseline across the middle of the diagram. Events sit above or below it as small markers (circles or diamonds) with `node-name` labels and `sublabel` dates/durations.
- The current point in time is a `focal` vertical line with an `arrow-label` ("now").
- Phases are soft bands (`accent-tint` at low opacity or `paper-2`) spanning their date range with `eyebrow` labels.
- Keep 5–9 events. A timeline with 20 dots is a calendar app.

## Anti-patterns
- Uneven marker spacing implying even time. Position is proportional or the axis is labeled "not to scale".
- Events stacked both above and below without reason. Pick one side per event; alternate only when above/below carries meaning.
- Phase bands that overlap without explanation (two shoots at once is a note, not a band).
- A baseline without a scale label or date ticks at the ends.

## Examples
- `assets/example-timeline.html` — minimal light
- `assets/example-timeline-dark.html` — minimal dark
