# Decision Tree

**Best for:** "which model / tool / setting do I use for this job" — the diagram madebysaira readers keep asking for. Model choice (Kling vs Veo vs Runway vs Luma), upscale-or-regenerate, style choice.

## Layout conventions
- Flow runs top → down. Start / end are ovals (`rx=20`), steps are rectangles (`rx=6`), decisions are diamonds.
- From a diamond: label every outgoing arrow ("high motion", "brand-safe", "under 10s"…). Conventional exits: Yes right, No below; keep them consistent across the tree.
- Each terminal leaf states the concrete pick: model name in `node-name`, and a `sublabel` with why (cost, motion, license) or a direct link to the workflow.
- The single most consequential decision or the recommended path is `focal`. Never every diamond.
- If two arrows must cross, arc one line over the other with a small bridge.

## Anti-patterns
- Fill color signaling node type. Shape does that.
- Diamonds with 4+ exits. Refactor into nested decisions.
- Unlabeled branches. A tree without branch labels is a guess.
- More than ~12 leaves. Split into a top-level tree + detail trees.

## Examples
- `assets/example-decision-tree.html` — minimal light
- `assets/example-decision-tree-dark.html` — minimal dark
