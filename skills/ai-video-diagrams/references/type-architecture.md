# Architecture

**Best for:** the studio stack behind a pipeline — automation (n8n), model APIs, storage, delivery. The "how does this actually run" diagram.

## Layout conventions
- A large container (`paper-2`, `rule` border, radius 8) holds the internal systems; external services sit outside the container as `external` nodes.
- Top row: inputs (client brief, source footage) as `input` nodes. Middle: the automation core (`focal` — this is what the diagram is about). Bottom: delivery (CDN, client drive, social).
- Connectors use `edge-link` with `sublabel`s carrying the protocol ("HTTPS", "webhook", "rclone sync").
- Data stores (`store` treatment) hang off the automation core, not in the main flow.
- Density 4/10: max ~10 nodes in a single architecture diagram. Beyond that, split into subsystems.

## Anti-patterns
- Vendors' official logos. Text labels in Poppins, technical details in mono. Logos turn the diagram into a banner ad.
- Cloud shapes (the puffy ellipse) for every service. A rounded rect is honest.
- Showing every microservice. Show the ones that carry the flow.
- A legend inside the diagram area. Labels are legible or the diagram is wrong.

## Examples
- `assets/example-architecture.html` — minimal light
- `assets/example-architecture-dark.html` — minimal dark
