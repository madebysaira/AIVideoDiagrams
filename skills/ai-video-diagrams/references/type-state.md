# State Machine

**Best for:** the lifecycle of a render job, an approval, or a pipeline run. States + transitions, with guards.

## Layout conventions
- States are rounded rects (`rx=6`), start is an oval, terminal states get a double border (`stroke-width` 1.2 outer + thin inner, or a ring).
- Transitions are `edge` arrows with `arrow-label`s stating the trigger ("review passed", "model returned error", "timeout").
- Guards sit in brackets on the transition label: `[seeded]`, `[cost < budget]`, `[client approved]`.
- The state the job spends the most time in is `store`; the terminal state you want is `ok`; the failure state is `danger`.
- Keep to 5–8 states. State machines beyond that are two machines.

## Anti-patterns
- Transitions that return to the same state (self-loops) unless they carry a real trigger (retry).
- Every state with an error exit. Consolidate failure into one `danger` terminal.
- Guard text that restates the trigger ("if approved" on a transition labeled "approved").
- Missing start or terminal states. Every machine has both.

## Examples
- `assets/example-state.html` — minimal light
- `assets/example-state-dark.html` — minimal dark
