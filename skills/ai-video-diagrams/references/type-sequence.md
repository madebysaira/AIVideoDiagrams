# Sequence

**Best for:** time-ordered messages between actors — an n8n workflow's HTTP calls, an agent loop talking to a model API, retry logic with backoff.

## Layout conventions
- Actors as thin boxes across the top (`external` for services, `primary` for your pipeline). Lifelines drop vertically from each.
- Messages are horizontal `edge-link` arrows with `arrow-label`s carrying the payload summary ("POST /v1/videos", "callback: ready").
- Time flows top → down. Each message is 24px below the previous; groups of messages are 48px apart.
- Responses and callbacks return right → left. The pair (request + response) reads as one exchange.
- The single exchange that matters (the generation call) is `focal` on both boxes.
- If the sequence is more than ~10 messages, split at a natural boundary.

## Anti-patterns
- Activation bars (the UML blocks) — they add noise at this density.
- Vertical text on lifelines. Rotate nothing; keep labels horizontal.
- Messages at uneven spacing. The grid is 4; message rows are 24.
- Repeating the same request pattern three times for retries. Show one exchange and a labeled loop fragment.

## Examples
- `assets/example-sequence.html` — minimal light
- `assets/example-sequence-dark.html` — minimal dark
