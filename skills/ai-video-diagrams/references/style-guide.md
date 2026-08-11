# Style Guide

**The single source of truth for colors, typography, and tokens.** Every diagram draws from this file, never from hex values inlined elsewhere. Change a token here and every new diagram inherits it without touching type logic.

The default skin is a warm editorial palette: bone paper, deep ink, one indigo accent. It reads well on screens, in client decks, and in print. Swap the values (or run [`onboarding.md`](onboarding.md)) and every diagram follows.

---

## Tokens

### Semantic roles

Every token is referred to by **semantic role**, never by hex value. Type references say `accent`, not `#4f46e5`.

| Role | Purpose | Default (light) | Default (dark) |
|---|---|---|---|
| `paper` | Page background, default node fill | `#f6f4ee` (bone) | `#181b24` (deep ink) |
| `paper-2` | Raised surface, secondary fill | `#efede5` | `#20242f` |
| `card` | Primary node fill | `#ffffff` | `#232836` |
| `ink` | Primary text, primary stroke | `#20242f` (deep ink) | `#e8eaf1` (bone) |
| `muted` | Secondary text, default arrow stroke | `#5b6472` (slate) | `#9da5b8` (slate) |
| `soft` | Sublabels, boundary labels | `#8d94a3` | `#757d92` |
| `rule` | Hairline borders | `rgba(32,36,47,0.14)` | `rgba(232,234,241,0.13)` |
| `rule-solid` | Stronger borders, baselines | `#c8c5b8` | `rgba(157,165,184,0.30)` |
| `accent` | Focal. 1–2 nodes max per diagram | `#4f46e5` (indigo) | `#7b73f0` (bright indigo) |
| `accent-tint` | Fill for focal boxes | `rgba(79,70,229,0.09)` | `rgba(123,115,240,0.14)` |
| `link` | API calls, external arrows | `#0e7490` (teal) | `#3aa3c6` |
| `ok` | Success / approved (semantic types only) | `#3d7a4e` | `#5fae74` |
| `danger` | Failed / rejected (semantic types only) | `#b23a3a` | `#d06363` |

> `ok` and `danger` are opt-in for semantic types (state machine, funnel). They are not a license to add color elsewhere. Everything outside those types stays paper, ink, muted, and one accent.

### Inversion rule (light → dark)

Any `rgba(32,36,47, X)` in light becomes `rgba(232,234,241, X)` in dark. Same opacities, RGB flipped. The accent shifts brighter to hold contrast on dark paper.

### Series palette (multi-series chart types only)

For chart types that must distinguish several overlapping entities. Currently only **quadrant** needs a second series color.

| Token | Light | Dark | Notes |
|---|---|---|---|
| `series-1` | `#8a7f3d` (olive) | `#b0a45a` | Non-focal series |
| `series-2` | `#5e7a9b` (dusty blue) | `#82a0c0` | Non-focal series |

Fills sit at `0.18` opacity light, `0.22` dark. Don't backfill these to non-chart types.

---

## Typography

| Role | Family | Size | Weight | Usage |
|---|---|---|---|---|
| `title` | Fraunces (serif) | 1.6rem | 400 | Page H1 |
| `node-name` | Poppins (sans) | 12px | 600 | Human-readable labels |
| `sublabel` | IBM Plex Mono | 9px | 400 | Model name, API, URL, field |
| `eyebrow` | IBM Plex Mono | 7–8px | 500, tracked 0.16em, uppercase | Type tags, axis labels |
| `arrow-label` | IBM Plex Mono | 8px | 400, tracked 0.04em | Arrow annotations |
| `callout` | Fraunces *italic* | 14px | 400 | Editorial asides only |

### Font stack

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=Poppins:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
```

**Load-bearing rule:** Mono is for *technical* content (model IDs, API endpoints, resolutions, file types). Human-readable names go in Poppins. Page title and editorial callouts are Fraunces (italic for callouts only). Never use a mono font as a blanket "dev" font.

---

## Stroke, radius, spacing

| Token | Value | Use |
|---|---|---|
| `stroke-thin` | `0.8` | Tag outlines, leaf nodes |
| `stroke-default` | `1` | Most strokes |
| `stroke-strong` | `1.2` | Emphasis strokes |
| `radius-sm` | `4` | Small tags |
| `radius-md` | `6` | Node boxes |
| `radius-lg` | `8` | Containers, rings |
| `grid` | `4` | Every coord, size, and gap is divisible by 4 (hard rule) |

---

## Node type → treatment

| Type | Fill | Stroke |
|---|---|---|
| `focal` (1–2 max) | `accent-tint` | `accent` |
| `primary` | `card` | `ink` |
| `store` | `ink @ 0.05` | `muted` |
| `external` | `ink @ 0.03` | `ink @ 0.30` |
| `input` | `muted @ 0.10` | `soft` |
| `optional` | `ink @ 0.02` | `ink @ 0.20` dashed `4,3` |
| `ok` | `ok @ 0.08` | `ok` |
| `danger` | `danger @ 0.08` | `danger` |

---

## Customizing the skin

1. **Run onboarding** — see [`onboarding.md`](onboarding.md). Drop a URL; the skill extracts palette + fonts and rewrites this file.
2. **Edit by hand** — change hex values in the tables above, then run the taste gate (§0 of SKILL.md) to confirm the accent still reads as focal on the new paper.
3. **Brand handoff** — paste your design token JSON in a new section and map tokens to semantic roles.

### Constraints (don't break these)

- **Contrast**: `ink` must hit WCAG AA on `paper`. `muted` must hit AA on `paper` at 11px+.
- **One accent**: two accents erase the focal signal.
- **No rainbow**: if the brand ships 8 colors, keep 3 (paper, ink, accent). The rest become `muted` variants.
- **Three families max**: serif + sans + mono. If the brand is all sans, keep Fraunces for `title` and `callout` anyway; the contrast is load-bearing.
- **Paper is warm, not pure white**: pure white reads sterile. Bone, cream, or a warm light grey.
- **No shadows, ever**: borders are the hierarchy tool. No gradients, no glow, no blur.
- **Radius ceiling**: 8px containers, 6px nodes, 4px tags. `rounded-2xl` is right out.
