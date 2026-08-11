# Layers

**Best for:** stacked abstractions — the post-production stack (AI base → clean-up → text → sound → grade), a prompt's layers, or a compositing chain.

## Layout conventions
- A vertical stack of full-width bars (`radius-md`), each bar one layer, `sublabel` inside carrying the tool or setting.
- Bottom layer is the foundation: `store` treatment. Top layer is the finish: `focal` treatment.
- Between bars, a thin gap with a right-aligned `eyebrow` label naming the boundary ("after clean-up", "before grade").
- Stack order is semantic: bottom = what everything sits on, top = what the viewer sees last. Don't invert for visual balance.

## Anti-patterns
- More than 7 layers. The stack stops communicating above that.
- Equal-width bars everywhere. Let the layer's importance set its thickness (base layer thicker).
- 3D extrusion or perspective. Flat, straight, aligned.
- Color-coding each layer. One accent on the top layer, muted everything else.

## Examples
- `assets/example-layers.html` — minimal light
- `assets/example-layers-dark.html` — minimal dark
