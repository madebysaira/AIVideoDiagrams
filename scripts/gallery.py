#!/usr/bin/env python3
"""Regenerate docs/gallery.html — the visual index of every diagram.

Reads the assets directory, renders one card per light/dark pair.
Usage: python3 scripts/gallery.py
"""
import pathlib
import html

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "skills" / "ai-video-diagrams" / "assets"
SHOTS = ROOT / "docs" / "screenshots"
OUT = ROOT / "docs" / "gallery.html"

NAME_MAP = {
    "pipeline-full": "Pipeline — full editorial",
    "pipeline": "Pipeline",
    "decision-tree": "Decision tree",
    "character-sheet": "Character sheet",
    "style-board": "Style board",
    "swimlane": "Swimlane",
    "sequence": "Sequence",
    "quadrant": "Quadrant",
    "layers": "Layers",
    "state": "State machine",
    "loop": "Loop",
    "architecture": "Architecture",
    "timeline": "Timeline",
    "tree": "Tree",
    "funnel": "Funnel",
}

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gallery — AIVideoDiagrams</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=Poppins:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{
  --paper:#f6f4ee; --paper-2:#efede5; --card:#ffffff;
  --ink:#20242f; --muted:#5b6472; --soft:#8d94a3;
  --rule:rgba(32,36,47,0.14);
  --accent:#4f46e5; --accent-tint:rgba(79,70,229,0.09);
  --title:'Fraunces',Georgia,serif; --sans:'Poppins',system-ui,sans-serif; --mono:'IBM Plex Mono',ui-monospace,monospace;
}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);-webkit-font-smoothing:antialiased;padding:56px;max-width:1200px;margin:0 auto}
header{padding-bottom:36px;border-bottom:1px solid var(--rule);margin-bottom:36px}
.kicker{font-family:var(--mono);font-size:10px;font-weight:500;letter-spacing:0.18em;text-transform:uppercase;color:var(--accent);margin-bottom:12px}
h1{font-family:var(--title);font-weight:600;font-size:38px;line-height:1.1}
.sub{font-family:var(--sans);font-size:14px;color:var(--muted);margin-top:12px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:20px}
.card{background:var(--card);border:1px solid var(--rule);border-radius:10px;overflow:hidden}
.card:hover{box-shadow:0 6px 24px rgba(32,36,47,0.08)}
.card img{display:block;width:100%;height:auto;border-bottom:1px solid var(--rule)}
.card figcaption{padding:12px 16px;font-family:var(--mono);font-size:11px;letter-spacing:0.06em;color:var(--muted)}
.card figcaption b{color:var(--ink);font-weight:500}
.card a{color:inherit;text-decoration:none}
</style>
</head>
<body>
<header>
  <div class="kicker">AIVideoDiagrams · gallery</div>
  <h1>Fourteen types. One design system.</h1>
  <p class="sub">Every diagram ships in light and dark. Each is a single self-contained HTML file — no runtime, no build step, opens by double-click.</p>
</header>
<div class="grid">
"""

FOOT = """</div>
</body>
</html>
"""


def slug_of(name: str) -> str:
    return name.removeprefix("example-").removesuffix(".html")


def main() -> None:
    files = sorted(p for p in ASSETS.glob("example-*.html"))
    cards = []
    for f in files:
        slug = slug_of(f.name)
        title = NAME_MAP.get(slug, slug.replace("-", " ").title())
        dark = "-dark" in f.name
        shot = SHOTS / f"{f.stem}.png"
        if not shot.exists():
            print(f"WARN: no screenshot for {f.name}")
            shot = None
        variant = "dark" if dark else "light"
        src = f"../skills/ai-video-diagrams/assets/{f.name}"
        label = html.escape(f"{title} · {variant}")
        img = (
            f'<a href="{html.escape(src)}"><img src="../docs/screenshots/{slug}.png" alt="{label}" loading="lazy"></a>'
            if shot
            else f'<a href="{html.escape(src)}">{html.escape(title)}</a>'
        )
        cards.append(
            f'<figure class="card">{img}<figcaption><b>{html.escape(title)}</b> · {variant}</figcaption></figure>'
        )
    OUT.write_text(HEAD + "\n".join(cards) + "\n" + FOOT, encoding="utf-8")
    print(f"wrote {OUT} with {len(cards)} cards")


if __name__ == "__main__":
    main()