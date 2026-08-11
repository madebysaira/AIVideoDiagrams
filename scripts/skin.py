#!/usr/bin/env python3
"""Generate dark variants of every example HTML by swapping :root tokens.

The design system's single source of truth is style-guide.md; this script is
the mechanical part of the rule "dark variants are generated, never hand-tuned".
Swatches in example-style-board.html carry inline hex fills that are CONTENT
(palette being presented), so they are deliberately left untouched.

Usage: python3 skin.py
"""
import pathlib

ASSETS = pathlib.Path(__file__).resolve().parent.parent / "skills" / "ai-video-diagrams" / "assets"

# token:value (light) -> token:value (dark)
DARK = {
    "--paper:#f6f4ee": "--paper:#181b24",
    "--paper-2:#efede5": "--paper-2:#20242f",
    "--card:#ffffff": "--card:#232836",
    "--ink:#20242f": "--ink:#e8eaf1",
    "--muted:#5b6472": "--muted:#9da5b8",
    "--soft:#8d94a3": "--soft:#757d92",
    "--rule:rgba(32,36,47,0.14)": "--rule:rgba(232,234,241,0.13)",
    "--rule-solid:#c8c5b8": "--rule-solid:rgba(157,165,184,0.30)",
    "--accent:#4f46e5": "--accent:#7b73f0",
    "--accent-tint:rgba(79,70,229,0.09)": "--accent-tint:rgba(123,115,240,0.14)",
    "--link:#0e7490": "--link:#3aa3c6",
    "--ok:#3d7a4e": "--ok:#5fae74",
    "--danger:#b23a3a": "--danger:#d06363",
    "--ink-05:rgba(32,36,47,0.05)": "--ink-05:rgba(232,234,241,0.05)",
    "--ink-03:rgba(32,36,47,0.03)": "--ink-03:rgba(232,234,241,0.03)",
    "--ink-02:rgba(32,36,47,0.02)": "--ink-02:rgba(232,234,241,0.02)",
    "--ink-30:rgba(32,36,47,0.30)": "--ink-30:rgba(232,234,241,0.30)",
    "--ink-20:rgba(32,36,47,0.20)": "--ink-20:rgba(232,234,241,0.20)",
    "--muted-10:rgba(91,100,114,0.10)": "--muted-10:rgba(157,165,184,0.10)",
    "--ok-08:rgba(61,122,78,0.08)": "--ok-08:rgba(95,174,116,0.08)",
    "--danger-08:rgba(178,58,58,0.08)": "--danger-08:rgba(208,99,99,0.08)",
}


def darken(text: str) -> str:
    for src, dst in DARK.items():
        text = text.replace(src, dst)
    return text


def main() -> None:
    targets = sorted(p for p in ASSETS.glob("example-*.html") if "-dark." not in p.name)
    targets.append(ASSETS / "template.html")
    for f in targets:
        out = ASSETS / f.name.replace(".html", "-dark.html")
        out.write_text(darken(f.read_text()), encoding="utf-8")
        print(f"{f.name} -> {out.name} ({out.stat().st_size} B)")


if __name__ == "__main__":
    main()
