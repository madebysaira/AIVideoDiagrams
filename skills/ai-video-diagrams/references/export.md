# Export

**Turn a diagram HTML file into standalone `.svg` and `.png` for decks, Figma, and social posts.**

Diagrams are self-contained HTML (that's what makes them edit-anywhere). Export is a separate step for when you need the raw vector or a raster image.

## SVG

Extract the `<svg>` node from the HTML and save it as `<name>.svg`. Inject the Google Fonts `<link>` tag into the SVG so text renders standalone in browsers, Figma, and Illustrator.

Simple, no dependencies. Do this first; most decks and Figma flows only need the SVG.

## PNG

Rasterize the HTML with headless Chromium at 2× by default. No Playwright, no node packages; Chromium is already on most machines (it ships with VS Code, Chrome, and Electron apps).

```bash
# macOS (Chrome installed)
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
  --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --screenshot=diagram.png --window-size=1360,900 file:///path/to/diagram.html

# Linux
chromium --headless=new --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=2 --screenshot=diagram.png \
  --window-size=1360,900 file:///path/to/diagram.html
```

The `scripts/screenshot.sh` in this repo wraps the same command and is safe to copy into any project.

## What's included

- **SVG** — diagram only (the `<svg>` element, fonts injected).
- **PNG** — full rendered page: diagram plus any editorial header cards from `-full` variants.

For a full-page capture of an editorial layout, use your browser's print-to-PDF or full-page screenshot instead.

## Edge cases

- **No source path given** → ask the user which `.html` file to export. Don't guess.
- **Source is the gallery (`index.html`)** → refuse; it holds many SVGs. Ask for a specific example file.
- **Source has no `<svg>` block** → refuse and tell the user.
- **PNG requested but no Chromium found** → surface the install instruction above and stop. Don't auto-install.
