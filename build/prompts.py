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

    # ---- Additional aesthetics -------------------------------------------
    # These have artwork prompts but no theme palette yet: see the note at the
    # bottom of docs/IMAGE-PROMPTS.md. Each one is written to read differently
    # from every other at a glance - the two easiest to collapse into each
    # other are `neon`, `cyberpunk` and `synthwave`, so those three are pushed
    # deliberately apart: neon is clean and scanlined, cyberpunk is wet and
    # dirty, synthwave is geometric and nostalgic.

    "cyberprep": (
        "Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. "
        "Dark polished graphite and slate base, brushed aluminium and pale "
        "chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, "
        "crisp rim highlights, immaculate and unweathered, calm corporate "
        "futurism, generous negative space, no grime, no decay, no signage."
    ),
    "cyberpunk": (
        "Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt "
        "reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, "
        "dense atmospheric haze and drifting steam, wet reflections stretched "
        "into vertical streaks, grimy and lived-in, heavy contrast, sodium "
        "spill in the shadows, 35mm anamorphic flare, gritty film grain."
    ),
    "solarpunk": (
        "Abstract wallpaper, solarpunk: deep forest green base with warm gold "
        "sunlight filtering through a dense living canopy, organic art-nouveau "
        "curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled "
        "shade, pollen and dust motes catching sun, hopeful and overgrown, "
        "soft focus, dark at the edges where the canopy closes in."
    ),
    "art-deco": (
        "Abstract wallpaper, 1920s art deco: black lacquer and deep emerald "
        "#0B3D2E ground with brushed brass and champagne gold #C9A227 line "
        "work, symmetrical sunburst fans and stepped chevrons, precise "
        "geometry, polished inlay, restrained metallic sheen, elegant and "
        "architectural, no clutter, generous dark field."
    ),
    "dark-academia": (
        "Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and "
        "aged parchment cream, single warm candle-lit source falling across "
        "deep shadow, chiaroscuro, dust suspended in the light, faint texture "
        "of old paper and leather binding, scholarly and melancholic, "
        "painterly, heavily vignetted."
    ),
    "cottagecore": (
        "Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm "
        "cream and dried-rose #C48B8B, soft hearth lamplight glowing from one "
        "side, hazy pastoral evening light, gentle linen and dried-flower "
        "texture, hand-made and unhurried, low contrast, matte, dark corners "
        "so the warmth reads as a single pool of light."
    ),
    "synthwave": (
        "Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky "
        "gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding "
        "perspective grid in cyan #00E5FF, a banded scanlined sun sitting near "
        "the edge, VHS tracking artefacts and chromatic fringing, airbrushed "
        "poster finish, nostalgic and geometric, dark upper field."
    ),
}

# The 23 subjects are shared by every style, and several of them name a colour
# outright ("amber and deep blue"). That was harmless while all three styles
# were abstract light, but Art Deco in amber or Cottagecore in electric violet
# is not the brief. This clause settles the conflict without giving up the
# shared subject, which is the whole reason a room stays recognisable when you
# switch aesthetic: composition and mood carry over, palette does not.
PALETTE_RULE = (
    "Where the subject names a colour absent from this style's palette, "
    "translate it to the nearest colour that belongs to the style - the style "
    "palette always wins. Keep the subject's composition, mood and direction "
    "of light exactly."
)

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
    return f"{STYLES[mode]} {SUBJECTS[key]}. {PALETTE_RULE} {CONSTRAINTS}"


def main() -> None:
    areas = as_dicts()
    docs = os.path.join(ROOT, "docs")
    drop = os.path.join(ROOT, "drop-in")
    os.makedirs(docs, exist_ok=True)
    for m in STYLES:
        os.makedirs(os.path.join(drop, m), exist_ok=True)

    # ---- per-style prompt.txt, right where the images get dropped ---------
    # docs/ has everything, but nobody generating 23 images wants to keep a
    # doc open in another window. This puts the exact prompts in the folder
    # the files are going into. drop-in/ is gitignored, so these are local.
    for mode in STYLES:
        out = [
            f"{mode.upper()} - {len(areas)} background prompts",
            "=" * 60,
            "",
            "Save each image in THIS folder as <area-key>.png - the filename",
            "must match the key exactly, that is how the importer places it.",
            "",
            "  python3 build/import_backgrounds.py",
            "  python3 build/generate_themes.py",
            "",
            "Anything you do not supply keeps its existing background, so you",
            "can do these a few at a time.",
            "",
            "NEGATIVE PROMPT (if your tool has one):",
            NEGATIVE,
            "",
            "=" * 60,
            "",
        ]
        for a in areas:
            out.append(f"--- {a['key']}.png  ({a['name']}) " + "-" * 20)
            out.append(full_prompt(mode, a["key"]))
            out.append("")
        with open(os.path.join(drop, mode, "prompt.txt"), "w") as f:
            f.write("\n".join(out))

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

    md.append("## Palette arbitration\n")
    md.append(
        "The 23 subjects are shared by every style, and several name a colour "
        "outright. This clause sits between the subject and the constraints so "
        "the style's palette wins while the composition carries over — which is "
        "what keeps a room recognisable across aesthetics.\n"
    )
    md.append(f"```\n{PALETTE_RULE}\n```\n")

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

    md.append("## Styles without a theme yet\n")
    md.append(
        "`glass`, `velvet` and `neon` are complete visual systems — palette, "
        "blur character, geometry and accent language all live in "
        "`build/modes.py`, and each renders 24 themes.\n"
    )
    md.append(
        "The seven below currently exist as **artwork only**. The prompts are "
        "here, `build/import_backgrounds.py` will process anything you drop in, "
        "and the images land in `www/ultimate-theme/backgrounds/<style>/` — but "
        "no theme references them yet. Turning one into a real mode means "
        "choosing its palette, blur, radii and border language in "
        "`build/modes.py`; that is a design decision, not a mechanical one.\n"
    )
    md.append("| Style | Reads as |")
    md.append("|---|---|")
    md.append("| `cyberprep` | clean, chrome, optimistic high-tech |")
    md.append("| `cyberpunk` | wet asphalt, signage bokeh, grimy |")
    md.append("| `solarpunk` | canopy light, gold and green, overgrown |")
    md.append("| `art-deco` | black lacquer, brass geometry, symmetrical |")
    md.append("| `dark-academia` | candlelight, oxblood, chiaroscuro |")
    md.append("| `cottagecore` | dusk hearth light, sage and cream, matte |")
    md.append("| `synthwave` | grid horizon, banded sun, VHS artefacts |")
    md.append("")
    md.append(
        "`neon`, `cyberpunk` and `synthwave` are the three most likely to "
        "collapse into each other, so their style blocks are pushed apart "
        "deliberately: neon is clean and scanlined, cyberpunk is wet and dirty, "
        "synthwave is geometric and nostalgic.\n"
    )

    with open(os.path.join(docs, "IMAGE-PROMPTS.md"), "w") as f:
        f.write("\n".join(md))

    print(f"drop-in/<style>/prompt.txt for {len(STYLES)} styles")
    print(f"docs/IMAGE-PROMPTS.md  ({len(md)} blocks)")
    print(f"docs/image-prompts.tsv ({len(lines) - 1} prompts)")


if __name__ == "__main__":
    main()
