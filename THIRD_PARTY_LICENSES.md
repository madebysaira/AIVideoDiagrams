# Third-party licences

This project is built with open tools and open type. The licenses below
cover the assets that are not original work.

## Typefaces (loaded at runtime from the Google Fonts CDN)

- **Fraunces** — [SIL Open Font License 1.1](https://scripts.sil.org/OFL)
  Copyright 2020 The Fraunces Project Authors
- **Poppins** — [SIL Open Font License 1.1](https://scripts.sil.org/OFL)
  Copyright 2020 The Poppins Project Authors
- **IBM Plex Mono** — [SIL Open Font License 1.1](https://scripts.sil.org/OFL)
  Copyright 2017 IBM Corp.

The fonts are not redistributed inside this repository; the diagrams load
them from `fonts.googleapis.com` in their `<head>`. If a client works
offline, self-hosting the three families under their OFL terms is allowed
and expected.

## Tooling used to produce screenshots

- **Chromium** — [BSD-3-Clause](https://chromium.googlesource.com/chromium/src/+/main/LICENSE)
  used headlessly (`--headless=new --screenshot`) to rasterise
  `docs/screenshots/*.png`. No Chromium code is distributed here.

## Project licence

The original content of this repository (diagram templates, examples,
documentation, scripts) is licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see `LICENSE`.

If anything here is missing from this file, open an issue.