#!/usr/bin/env python3
"""
Theme generator for the Home Assistant Ultimate Theme.

One Jinja template, many rendered themes - one per (aesthetic mode x area).
Each mode is a full visual system, not just a background swap: palette, blur
character, geometry and accent language all change together.

Outputs
  themes/ultimate-theme.yaml             all 72 themes in one file
  dashboards/per-view-backgrounds.yaml   copy-paste card_mod snippets

Why one file: HACS manages exactly one theme configuration file per repository -
if there is more than one under themes/, only the first is installed. Splitting
by mode would silently ship a third of the project.

Background URL modes
  --base cdn     (default) absolute jsDelivr URLs. A HACS install is then
                 self-contained, because HACS copies only the theme YAML and
                 never touches /config/www.
  --base local   /local/... URLs, for anyone who copies www/ to /config/www
                 themselves and would rather not depend on a CDN.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

# Build scripts run in CI, where a stray build/__pycache__ would show up as
# an untracked artefact. Nothing here benefits from cached bytecode.
sys.dont_write_bytecode = True

import jinja2
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from areas import as_dicts          # noqa: E402
from modes import MODES, accent_for_mode   # noqa: E402

THEMES_DIR = os.path.join(ROOT, "themes")
DASH_DIR = os.path.join(ROOT, "dashboards")
AVG_COLORS = os.path.join(ROOT, "www", "ultimate-theme", "avg-colors.json")

# Served from /config/www, which Home Assistant exposes at /local
LOCAL_BASE = "/local/ultimate-theme/backgrounds"

# Served straight from the repository via jsDelivr. Pin to a release tag rather
# than @main once you cut one — jsDelivr caches @main for up to seven days, so a
# tag makes background updates predictable.
REPO = "HomeRiz/Home-Assistant-Ultimate-Theme"

# Pin to the release tag, not to a branch. jsDelivr caches a branch for up to
# seven days, and worse, a branch keeps moving - so re-rendering the artwork
# would silently change the backgrounds of every already-installed theme. A tag
# is immutable and cached permanently.
#
# The reference is self-consistent: the theme file committed under tag X.Y.Z
# points at X.Y.Z, which is the same commit that carries those images. Bump
# this, regenerate and commit *before* creating the tag.
#
# Must match the git tag exactly. jsDelivr happens to resolve 'v0.0.1' to tag
# '0.0.1' via semver, but relying on that is a trap - keep them identical.
CDN_REF = "0.0.6"
CDN_BASE = f"https://cdn.jsdelivr.net/gh/{REPO}@{CDN_REF}/www/ultimate-theme/backgrounds"


# ---------------------------------------------------------------------------
def _hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _rgb_to_hex(rgb):
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(round(c)))) for c in rgb)


def _mix(a, b, t):
    ra, rb = _hex_to_rgb(a), _hex_to_rgb(b)
    return _rgb_to_hex(tuple(ra[i] + (rb[i] - ra[i]) * t for i in range(3)))


def primary_ramp(accent: str):
    """Build HA's --ha-color-primary-05..95 ladder around the area accent."""
    out = []
    for i in (5, 10, 20, 30):
        out.append((f"{i:02d}", _mix("#000000", accent, i / 40.0)))
    out.append(("40", accent))
    for i in (50, 60, 70, 80, 90, 95):
        out.append((str(i), _mix(accent, "#ffffff", (i - 40) / 60.0)))
    return out


def darken_for_header(hexcol: str, amount: float = 0.35) -> str:
    """Header tint: the background's average colour, darkened so it reads as chrome."""
    return _mix(hexcol, "#000000", amount)


# ---------------------------------------------------------------------------
def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", choices=("cdn", "local"), default="cdn",
                    help="where the theme should load background images from")
    args = ap.parse_args()
    base_url = CDN_BASE if args.base == "cdn" else LOCAL_BASE

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(HERE),
        keep_trailing_newline=True,
        trim_blocks=False,
        lstrip_blocks=False,
    )
    tpl = env.get_template("template.jinja2")

    avg = {}
    if os.path.exists(AVG_COLORS):
        with open(AVG_COLORS) as f:
            avg = json.load(f)
    else:
        print("! avg-colors.json missing - run generate_backgrounds.py first. "
              "Falling back to accent-derived header tints.")

    areas = as_dicts()
    os.makedirs(THEMES_DIR, exist_ok=True)
    os.makedirs(DASH_DIR, exist_ok=True)

    total = 0
    chunks = []
    for mode_name, m in MODES.items():

        # ---- base theme (no area background) ------------------------------
        chunks.append(tpl.render(
            theme_name=m["label"],
            m=m, area=None, bg_url=None,
            accent=m["palette"]["blue-color"],
            header_tint=darken_for_header(m["palette"]["blue-color"], 0.65),
            ramp=primary_ramp(m["palette"]["blue-color"]),
        ))
        total += 1

        # ---- one theme per area -------------------------------------------
        for area in areas:
            bg_url = f"{base_url}/{mode_name}/{area['key']}.webp"
            # the area's hue, re-expressed in this mode's colour language
            accent = accent_for_mode(area["accent"], mode_name)
            tint = avg.get(mode_name, {}).get(area["key"])
            header_tint = (darken_for_header(tint, 0.25) if tint
                           else darken_for_header(accent, 0.65))
            chunks.append(tpl.render(
                theme_name=f"{m['label']} - {area['name']}",
                m=m, area=area, bg_url=bg_url,
                accent=accent,
                header_tint=header_tint,
                ramp=primary_ramp(accent),
            ))
            total += 1

    # ---- one file, because HACS only manages the first one it finds --------
    path = os.path.join(THEMES_DIR, "ultimate-theme.yaml")
    header = (
        "---\n"
        "# Home Assistant Ultimate Theme\n"
        "# GENERATED FILE - edit build/modes.py + build/template.jinja2 and\n"
        "# re-run build/generate_themes.py instead.\n"
        f"# {total} themes: {len(MODES)} modes x (1 base + {len(areas)} areas).\n"
        f"# Backgrounds: {args.base}\n"
    )
    body = header + "\n".join(chunks)
    with open(path, "w") as f:
        f.write(body)

    parsed = yaml.safe_load(body)
    print(f"{path}\n  {len(parsed)} themes, {len(body.splitlines())} lines, "
          f"{len(body)/1024:.0f} KB, valid YAML")

    # ---- per-view snippets -------------------------------------------------
    snippets = ["---",
                "# Per-view background snippets.",
                "# Paste the card_mod block into a view in your dashboard's",
                "# Raw Configuration Editor. See docs/PER-VIEW-BACKGROUNDS.md.",
                ""]
    for mode_name in MODES:
        snippets.append(f"# ===== {MODES[mode_name]['label']} " + "=" * 30)
        for area in areas:
            snippets.append(
                f"# {area['name']}\n"
                f"# - title: {area['name']}\n"
                f"#   path: {area['key']}\n"
                f"#   icon: {area['icon']}\n"
                f"#   card_mod:\n"
                f"#     style: |\n"
                f"#       :host {{\n"
                f"#         --ultimate-view-background: "
                f"url('{base_url}/{mode_name}/{area['key']}.webp');\n"
                f"#       }}\n"
            )
    with open(os.path.join(DASH_DIR, "per-view-backgrounds.yaml"), "w") as f:
        f.write("\n".join(snippets))

    print(f"\n{total} themes generated across {len(MODES)} modes.")


if __name__ == "__main__":
    main()
