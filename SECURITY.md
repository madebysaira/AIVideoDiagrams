# Security

This repository ships static HTML, SVG, and Python tooling. There are no
secrets, no credentials, and no network-facing services in the code.

If you build on top of the diagrams or scripts:

- Never commit tokens, API keys, or client material into a diagram or a
  script. The examples in this repo are fictions built from public
  knowledge about model APIs.
- The `skin.py`, `gallery.py`, and `screenshots.sh` scripts only touch
  files inside this repository. If you extend them, keep that property.
- Diagrams load typefaces from the Google Fonts CDN. If a deployment
  blocks third-party requests, self-host the fonts (OFL permits it); do
  not silently substitute a different font in a client deliverable.

## Reporting

If you find a security issue in the tooling or a way the templates could
be abused (for example, an injection path through a filename into
`scripts/gallery.py`), report it privately to the repository owner
rather than opening a public issue.