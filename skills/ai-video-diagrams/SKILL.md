---
name: ai-video-diagrams
description: Use when providing diagrams to madebysaira automation clients. 14 SVG diagram types, one design system — pipeline, decision tree, character sheet, style board, swimlane, sequence, quadrant, layers, state, loop, architecture, timeline, tree, funnel.
---

# AI Video Diagrams

Every madebysaira automation delivery comes with a diagram. This skill is
how that happens without the diagrams looking like they were made by
three different people.

The rules are few and they are strict:

1. **One design system.** Every diagram uses the same three typefaces, the
   same eleven colour tokens, the same radius, the same arrowheads. A
   pipeline and a character sheet share DNA.
2. **Typography does the work.** Label placement is a layout decision, not
   a leftover. If a label touches a line, the label moves.
3. **Density around 4/10.** A diagram that shows everything shows nothing.
   Two arrows per relationship, one accent per diagram, dead space is
   load-bearing.
4. **The focal node is chosen, not inherited.** Exactly one node per
   diagram gets the accent treatment. It is the thing the client must look
   at first. If you cannot name it, the diagram is not done.

## When to use

Any time a client needs to understand:

- how the (pipeline, studio, automation) works — **pipeline**, **architecture**, **swimlane**
- which model/route to pick — **decision tree**, **quadrant**
- who a character is — **character sheet**
- what the footage should feel like — **style board** (pairs with a character sheet; one per spot)
- how an event unfolds — **sequence**, **timeline**
- what a render job goes through — **state**
- how the side of the business gets better — **loop**
- what is on top of what — **layers**, **tree**
- what survives the edit — **funnel**

## The 14 types

| Type | Best for | Example file |
|---|---|---|
| Pipeline | stage flow, left → right | `assets/example-pipeline.html` |
| Decision tree | model/route choice, diamond branches | `assets/example-decision-tree.html` |
| Character sheet | locked character attributes | `assets/example-character-sheet.html` |
| Style board | palette · type · motion specs | `assets/example-style-board.html` |
| Swimlane | who does what across roles | `assets/example-swimlane.html` |
| Sequence | message exchanges over time | `assets/example-sequence.html` |
| Quadrant | position by two axes | `assets/example-quadrant.html` |
| Layers | stacked render pipeline | `assets/example-layers.html` |
| State | job lifecycle, states + guards | `assets/example-state.html` |
| Loop | reinforcing cycle around a hub | `assets/example-loop.html` |
| Architecture | automation + APIs + delivery | `assets/example-architecture.html` |
| Timeline | events pinned to a calendar | `assets/example-timeline.html` |
| Tree | parent → children breakdown | `assets/example-tree.html` |
| Funnel | 30 ideas → 1 delivered | `assets/example-funnel.html` |

Per-type layout conventions live in `references/type-*.md`. Read the
relevant one before drawing. The full editorial variant (header + stat
cards) is `assets/example-pipeline-full.html` — use it when the diagram is
the hero of a case study.

## Workflow

1. **Pick the type** — re-read the table above. If two types fit, pick the
   one with fewer nodes.
2. **Copy the template** — start from `assets/template.html`. Never start
   from a previous diagram; templates keep the system honest.
3. **Draft the skeleton** — nodes and their labels first, on the 4px grid
   (viewBox 1200 × 720). Orthogonal connectors only; no diagonal lines.
4. **Draw the flow with elbows** — connectors leave node centres or edges,
   bend at right angles, arrive at edges. Arrow labels sit 8px above the
   line they describe.
5. **Choose the focal node** — `class="focal"`. One. If the choice is
   hard, the diagram is trying to say two things; split it.
6. **Set density** — cut every label that repeats the obvious, every node
   that is not on the path. Aim for 4/10.
7. **Render and review** — open the file, look at it as a client would,
   and only then generate the dark variant with `scripts/skin.py`.
8. **Export** — PNG at 2× via `scripts/screenshots.sh` (headless
   chromium), or SVG as-is for embed.

## Checklist (before it leaves the studio)

- [ ] One focal node, and it is the right one
- [ ] Every connector is orthogonal; every arrowhead lands on an edge
- [ ] No label touches a line or another label — 8px clearance minimum
- [ ] Sublabels are mono, node names are Poppins, eyebrow is Fraunces-free (mono uppercase)
- [ ] Accent used sparingly: focal node + at most one callout
- [ ] Density: if the diagram has more than ~20 shapes, cut it
- [ ] Dark variant generated, not hand-tuned (`python3 scripts/skin.py`)
- [ ] `aria-label` on the `<svg>` describes the diagram for a blind client
- [ ] Fonts load from the Google Fonts CDN link in the head (do not self-host)

## Escape hatches

- **Client asks for a different colour.** The tokens in `:root` are the
  whole system. Change the token, every diagram changes with it. That is
  the point of the system.
- **Diagram feels heavy.** Delete one level of detail and make the
  remaining labels bigger. Sparse beats dense every time.
- **Client wants a style we do not have.** Say no politely, deliver the
  closest type, offer the missing one as a request — do not invent a new
  style on the spot.
- **Type does not fit the story.** The table is a menu, not a cage. If a
  spot needs a "before / after" split, draw it as two panels of the same
  story — but do it once, document it in `references/`, and give it a
  template.

## Colophon

- Typefaces: Fraunces (display), Poppins (UI), IBM Plex Mono (data)
- Palette tokens: bone `#f6f4ee`, ink `#20242f`, accent `#4f46e5`
  (dark: `#181b24` / `#e8eaf1` / `#7b73f0`)
- Grid: 4px, viewBox 1200 × 720, radius 6 on nodes, 8 on containers
- Built with plain SVG + CSS variables. No runtime, no build step, opens
  by double-click. That is a feature, not a shortcut.