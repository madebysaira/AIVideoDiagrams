# Style Board

**Best for:** locking a look across shots — palette, type, grain, motion feel. The visual contract between you and the model, and between you and the client.

## Layout conventions
- Left column: the palette as a row of swatches (each a `rect` with its hex as a `sublabel` underneath). One swatch is `focal` — the brand color that anchors the look.
- Middle column: type specimens — a large Fraunces wordmark, a Poppins body line, an IBM Plex Mono caption. Label each with its role.
- Right column: "motion feel" rows: grain on/off, speed words ("slow push", "locked-off"), grade notes.
- Bottom strip: a 2-3 word style block ready to paste into a prompt (e.g. "soft daylight, 35mm, muted grade").
- Keep every swatch value exact. A style board with approximate hexes is a lie.

## Anti-patterns
- More than 6 swatches. The model can't hold 12 colors, and neither can the client.
- Type specimens in weights the fonts don't ship (Fraunces 700 doesn't exist in the stack; use 400/600).
- Style words that contradict each other ("warm grade" next to "clinical cool").
- A palette swatch set that fails contrast against the paper color. Check it.

## Examples
- `assets/example-style-board.html` — minimal light
- `assets/example-style-board-dark.html` — minimal dark
