#!/usr/bin/env python3
"""
Import externally generated backgrounds.

Drop your own images into  drop-in/<mode>/<area-key>.<ext>  and run this.
It will:
  1. resize/crop to 2560x1440 (centre crop, no squashing)
  2. optionally darken so glass cards stay readable on top
  3. convert to WebP and write into www/ultimate-theme/backgrounds/<mode>/
  4. refresh avg-colors.json so the HA header tint matches the new art

Any area you do not supply keeps its procedurally generated background, so you
can replace them a few at a time.

Usage
  python3 build/import_backgrounds.py                 # import everything found
  python3 build/import_backgrounds.py glass           # one mode only
  python3 build/import_backgrounds.py --darken 0.35   # stronger darkening
  python3 build/import_backgrounds.py --darken 0      # no darkening at all
"""

from __future__ import annotations

import argparse
import json
import os
import sys

# Build scripts run in CI, where a stray build/__pycache__ would show up as
# an untracked artefact. Nothing here benefits from cached bytecode.
sys.dont_write_bytecode = True

from PIL import Image, ImageEnhance

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from areas import AREA_KEYS  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DROP = os.path.join(ROOT, "drop-in")
OUT = os.path.join(ROOT, "www", "ultimate-theme", "backgrounds")
AVG = os.path.join(ROOT, "www", "ultimate-theme", "avg-colors.json")
MODES = ("glass", "velvet", "neon")
W, H = 2560, 1440
EXTS = (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff")


def cover_resize(img: Image.Image, w: int, h: int) -> Image.Image:
    """Scale to fill then centre-crop - same behaviour as CSS `cover`."""
    src_ratio = img.width / img.height
    dst_ratio = w / h
    if src_ratio > dst_ratio:                     # too wide -> crop sides
        new_h = h
        new_w = max(w, int(round(h * src_ratio)))
    else:                                          # too tall -> crop top/bottom
        new_w = w
        new_h = max(h, int(round(w / src_ratio)))
    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - w) // 2
    top = (new_h - h) // 2
    return img.crop((left, top, left + w, top + h))


def average_color(img: Image.Image) -> str:
    px = img.resize((1, 1), Image.BOX).getpixel((0, 0))[:3]
    return "#%02x%02x%02x" % px


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", nargs="?", choices=MODES, help="only import this mode")
    ap.add_argument("--darken", type=float, default=0.22,
                    help="0 = untouched, 0.5 = very dark. Default 0.22. "
                         "Glass cards need a reasonably dark backdrop to stay legible.")
    ap.add_argument("--quality", type=int, default=88)
    args = ap.parse_args()

    if not os.path.isdir(DROP):
        print(f"No drop-in folder at {DROP} - nothing to import.")
        return

    try:
        with open(AVG) as f:
            avg = json.load(f)
    except (OSError, ValueError):
        avg = {}

    imported = 0
    unknown = []
    for mode in MODES:
        if args.mode and mode != args.mode:
            continue
        src_dir = os.path.join(DROP, mode)
        if not os.path.isdir(src_dir):
            continue
        os.makedirs(os.path.join(OUT, mode), exist_ok=True)

        for fn in sorted(os.listdir(src_dir)):
            stem, ext = os.path.splitext(fn)
            if ext.lower() not in EXTS:
                continue
            if stem not in AREA_KEYS:
                unknown.append(f"{mode}/{fn}")
                continue

            img = Image.open(os.path.join(src_dir, fn)).convert("RGB")
            img = cover_resize(img, W, H)
            if args.darken > 0:
                img = ImageEnhance.Brightness(img).enhance(1.0 - args.darken)

            dst = os.path.join(OUT, mode, f"{stem}.webp")
            img.save(dst, "WEBP", quality=args.quality, method=5)
            avg.setdefault(mode, {})[stem] = average_color(img)
            imported += 1
            print(f"imported {mode}/{stem}  "
                  f"({os.path.getsize(dst) / 1024:.0f} KB, avg {avg[mode][stem]})")

    with open(AVG, "w") as f:
        json.dump(avg, f, indent=2, sort_keys=True)

    if unknown:
        print("\nSkipped - filename does not match an area key:")
        for u in unknown:
            print(f"  {u}")
        print(f"\nValid keys: {', '.join(AREA_KEYS)}")

    print(f"\n{imported} image(s) imported.")
    if imported:
        print("Now re-run:  python3 build/generate_themes.py")
        print("(so the header tints pick up the new artwork)")


if __name__ == "__main__":
    main()
