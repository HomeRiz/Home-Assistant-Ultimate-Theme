#!/usr/bin/env python3
"""
Generates docs/IMAGE-PROMPTS.md and docs/image-prompts.tsv.

The prompt for any given image is  STYLE + SUBJECT + CONSTRAINTS.  Keeping the
three parts separate means the 23 subjects stay identical across the 3 modes,
which is what makes a room recognisable when you switch aesthetics.
"""

from __future__ import annotations

import os
import sys

# Build scripts run in CI, where a stray build/__pycache__ would show up as
# an untracked artefact. Nothing here benefits from cached bytecode.
sys.dont_write_bytecode = True

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from areas import as_dicts  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# ---------------------------------------------------------------------------
STYLES = {
    "glass": (
        "Abstract wallpaper in the style of Apple's spatial glass interfaces: "
        "liquid glass, smooth volumetric colour gradients, large soft bokeh, "
        "deep saturated colour with luminous depth, gentle film grain, "
        "no hard edges, painterly light."
    ),
    "velvet": (
        "Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted "
        "pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, "
        "yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte "
        "gradients, flat diffuse light, gentle grain, nothing garish or glossy."
    ),
    "neon": (
        "Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma "
        "neon accent light, volumetric glow and light bloom, faint horizontal "
        "scanlines, subtle chromatic aberration on bright edges, deep contrast, "
        "cinematic, Blade Runner colour grade."
    ),
}

CONSTRAINTS = (
    "16:9 aspect ratio, 2560x1440, desktop wallpaper. "
    "Dark overall so white UI text stays readable on top. "
    "Uncluttered centre — keep detail and interest toward the edges and corners. "
    "No text, no letters, no numbers, no watermark, no logo, no signature, "
    "no people, no faces, no hands, no recognisable products."
)

NEGATIVE = (
    "text, letters, words, watermark, logo, signature, people, faces, hands, "
    "busy detail in centre, high-key bright, washed out, blown highlights, "
    "harsh edges, clutter, UI mockup, screenshot, frame, border"
)

# ---------------------------------------------------------------------------
SUBJECTS = {
    "home":            "a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway",
    "living-room":     "soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow",
    "kitchen":         "warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround",
    "bedroom":         "a deep indigo and violet nebula haze, very still and quiet, midnight calm",
    "master-bedroom":  "plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious",
    "guest":           "soft teal and sage mist drifting slowly, calm, minimal, welcoming",
    "bathroom":        "aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean",
    "office":          "cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake",
    "ai":              "electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence",
    "outside":         "a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air",
    "hallway":         "warm dim light receding down a long perspective gradient, muted slate and amber, transitional",
    "garage":          "brushed steel grey lit by a single orange sodium lamp, industrial, oily dark",
    "front-yard":      "morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges",
    "back-yard":       "late sunset green and warm orange across grass, dusk settling, relaxed",
    "electrical-room": "amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light",
    "technic-room":    "cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark",
    "garden":          "verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges",
    "energy":          "flowing green and yellow light currents streaming like energy in motion, kinetic, dark background",
    "security":        "deep crimson and dark red light sweeping across shadow, watchful and tense, alert",
    "climate":         "a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance",
    "media":           "magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic",
    "network":         "blue and cyan data streams flowing through dark space, luminous nodes and connecting lines",
    "settings":        "restrained graphite and silver light, neutral, minimal, quietly technical",
}


def full_prompt(mode: str, key: str) -> str:
    return f"{STYLES[mode]} {SUBJECTS[key]}. {CONSTRAINTS}"


def main() -> None:
    areas = as_dicts()
    docs = os.path.join(ROOT, "docs")
    drop = os.path.join(ROOT, "drop-in")
    os.makedirs(docs, exist_ok=True)
    for m in STYLES:
        os.makedirs(os.path.join(drop, m), exist_ok=True)

    # ---- flat prompt list for batch tools ---------------------------------
    # Lives in docs/, not drop-in/. drop-in/ is a local workspace and is not
    # part of the repository.
    lines = ["target\tprompt"]
    for mode in STYLES:
        for a in areas:
            lines.append(f"{mode}/{a['key']}.png\t{full_prompt(mode, a['key'])}")
    with open(os.path.join(docs, "image-prompts.tsv"), "w") as f:
        f.write("\n".join(lines) + "\n")

    # ---- human readable doc -----------------------------------------------
    md = []
    md.append("# Image prompts\n")
    md.append(
        "Every background is `STYLE + SUBJECT + CONSTRAINTS`. The **subject is "
        "identical across all three modes** — that is deliberate. It means the "
        "Kitchen still reads as the Kitchen whether you are in Glass, "
        "Velvet or Neon.\n"
    )
    md.append(
        "You do not have to do all 69. Anything you don't supply keeps its "
        "procedurally generated background, so you can replace them a few at a "
        "time.\n"
    )

    md.append("## How to use\n")
    md.append(
        "1. Generate an image.\n"
        "2. Save it as `drop-in/<mode>/<area-key>.png` "
        "(e.g. `drop-in/glass/kitchen.png`). The filename **must** match the "
        "area key exactly — that is how the importer knows where it goes.\n"
        "3. Run:\n\n"
        "```bash\n"
        "python3 build/import_backgrounds.py\n"
        "python3 build/generate_themes.py\n"
        "```\n\n"
        "The importer centre-crops to 2560×1440, darkens slightly so glass "
        "cards stay legible, converts to WebP, and refreshes the header tints. "
        "Use `--darken 0` if your images are already dark enough.\n"
    )

    md.append("## Constraints (append to every prompt)\n")
    md.append(f"```\n{CONSTRAINTS}\n```\n")
    md.append("**Negative prompt**, if your tool supports one:\n")
    md.append(f"```\n{NEGATIVE}\n```\n")

    md.append("## Style blocks (prepend, one per mode)\n")
    for mode, style in STYLES.items():
        md.append(f"### `{mode}`\n\n```\n{style}\n```\n")

    md.append("## Subjects\n")
    md.append("| Area key | Dashboard | Subject |")
    md.append("|---|---|---|")
    for a in areas:
        md.append(f"| `{a['key']}` | {a['name']} | {SUBJECTS[a['key']]} |")
    md.append("")

    md.append("## Ready-to-paste full prompts\n")
    for mode in STYLES:
        md.append(f"<details>\n<summary><b>{mode}</b> — all 23 prompts</summary>\n")
        for a in areas:
            md.append(f"**`{mode}/{a['key']}.png`** — {a['name']}\n")
            md.append(f"```\n{full_prompt(mode, a['key'])}\n```\n")
        md.append("</details>\n")

    with open(os.path.join(docs, "IMAGE-PROMPTS.md"), "w") as f:
        f.write("\n".join(md))

    print(f"docs/IMAGE-PROMPTS.md  ({len(md)} blocks)")
    print(f"docs/image-prompts.tsv ({len(lines) - 1} prompts)")


if __name__ == "__main__":
    main()
