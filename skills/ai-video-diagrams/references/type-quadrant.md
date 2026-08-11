# Quadrant

**Best for:** two-axis positioning — cost vs quality of models, effort vs impact of client requests, "worth it" vs "skip".

## Layout conventions
- A square plot area (`paper-2` fill, `rule-solid` border). Axes are `muted` lines with `eyebrow` labels: bottom axis left → right, left axis bottom → top.
- Axis labels state the scale ends ("cheap" → "expensive", "rough" → "client-ready"). Never leave axes unlabeled.
- Each item is a small `rect` (`radius-sm`) or `circle` with a `node-name` label beside it, placed at its coordinates.
- The quadrant that contains the recommended zone is `focal` (a large tinted rect behind the items, `accent` dashed border).
- Second series (e.g. "last year's tools") uses `series-1` at 0.18 fill. The focal rule still holds: accent stays on the recommendation, not on the data.
- Target 4–9 items. More becomes a scatter plot.

## Anti-patterns
- Items overlapping the axis labels. Leave margin.
- Quadrant cells without labels ("top-right is good"). Name each cell.
- Both axes saying the same thing ("quality" and "quality"). If axes correlate, the diagram is a line.
- Focal on the whole grid instead of one cell.

## Examples
- `assets/example-quadrant.html` — minimal light
- `assets/example-quadrant-dark.html` — minimal dark
