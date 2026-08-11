# Onboarding

**The flow that makes every diagram look like *your* studio, not a template.**

Out of the box, diagrams render in the default skin (bone paper, deep ink, indigo accent). It is deliberately neutral and good enough to screenshot. But the skill exists so your client-facing diagrams carry your brand, so run onboarding once per studio: paste your website URL (or your brand hexes) and the skill rewrites `style-guide.md`. Every diagram from then on inherits the new tokens.

---

## § URL

1. Fetch the homepage of the URL the user gives you.
2. Extract the dominant palette:
   - `<body>` background → `paper`
   - primary text color → `ink`
   - secondary / caption text → `muted`
   - card / container backgrounds → `paper-2` and `card`
   - the most-used brand color (CTA, link, heading) → `accent`
3. Extract the font stack:
   - `<h1>` family → `title` (serif preferred; if the brand has no serif, keep Fraunces)
   - `<body>` family → `node-name`
   - `<code>` / `<pre>` family → `sublabel` (mono)
4. Map detected values to semantic roles and **show the user a proposed diff** before writing anything.
5. On approval, write the tokens into `references/style-guide.md` under "Custom tokens" and mark the guide as customized (see first-run gate below).

## § Manual hexes

The user pastes hex values. Map them the same way: brightest warm neutral → `paper`, darkest → `ink`, loudest brand color → `accent`. Verify contrast before writing.

## § Brand handoff

The user pastes a design token JSON (from their design system). Map its keys to semantic roles and add a mapping table in `style-guide.md`.

---

## Contrast checks (automatic)

Before writing tokens, verify WCAG AA contrast for `ink` over `paper` and `muted` over `paper` at 11px. If a brand color fails at diagram sizes (9–12px), propose an adjusted value and explain why, then apply only with the user's OK.

## First-run gate

On first use in a new project, before generating the first diagram, check whether `style-guide.md` still holds the shipped defaults (accent `#4f46e5`). If it does, **pause and ask**:

> "This is your first diagram in this project. The style guide is still at the default (bone + indigo). Want to customize it first? (a) pull from your website URL, (b) paste brand hexes, (c) paste design tokens, (d) proceed with the default for now."

Branch (a)–(c) → run the matching flow above. (d) → proceed; remind them onboarding can run later.

The gate exists because shipping default-skinned diagrams into a branded project is the exact failure mode this skill was built to prevent. Don't skip it.
