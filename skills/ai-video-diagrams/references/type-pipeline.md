# Pipeline

**Best for:** the generation pipeline of an AI video project. Script → image → video → post → delivery. The hero type of this skill.

## Layout conventions
- Flow runs left → right in stage groups, each group a soft container (`paper-2` fill, `rule` border, radius 8).
- Stage groups hold 1–3 nodes. Group labels are `eyebrow` text at the top-left inside the container.
- Connectors between stages are orthogonal elbows (right-angle paths, rounded joins). No diagonal lines.
- The one node that turns raw material into the client deliverable is `focal`. Everything else is `primary`.
- Under each node, a `sublabel` carries the concrete thing: model ID, resolution, or file format.
- Arrow labels sit 8px above their line on a masked background, never on the line itself.

## Anti-patterns
- More than 6 stages. If the pipeline has more, split into an overview diagram + one detail per stage.
- Mixing stages vertically when the flow is horizontal. Keep one axis.
- Focal on every stage. One accent node per diagram; two if the diagram is long, never more.
- Emoji or clip-art robot icons as stage markers. Text labels carry the meaning.

## Examples
- `assets/example-pipeline.html` — minimal light
- `assets/example-pipeline-dark.html` — minimal dark
- `assets/example-pipeline-full.html` — full editorial with header card
