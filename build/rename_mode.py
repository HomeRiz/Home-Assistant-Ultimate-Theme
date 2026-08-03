#!/usr/bin/env python3
"""
Rename an aesthetic mode across the whole project, atomically.

A mode name appears in more places than is comfortable to change by hand:

  build/modes.py                     MODES key, label, palette constant
  build/generate_backgrounds.py      MODES key, palette snap helper
  build/render_previews.py           SPECS key, label
  build/prompts.py                   STYLES key, style prompt text
  build/verify.py                    (reads MODES, nothing hardcoded)
  drop-in/<mode>/                    your source artwork folder
  www/ultimate-theme/backgrounds/<mode>/
  docs/previews/<mode>/ and docs/previews/<mode>.webp
  www/ultimate-theme/avg-colors.json top-level key
  README.md, INSTALL.md, docs/*.md   prose and image links

Miss one and you get a half-renamed project that still builds but quietly
generates the wrong filenames. This does all of it in one pass.

NOTICE.md is deliberately excluded — third-party attribution must keep naming
the original project regardless of what the mode is called here.

Usage
  python3 build/rename_mode.py catppuccin velvet "Ultimate Velvet"
  python3 build/rename_mode.py catppuccin velvet "Ultimate Velvet" --dry-run

Afterwards
  python3 build/generate_themes.py
  python3 build/verify.py
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# Files whose text gets rewritten. NOTICE.md is absent on purpose.
TEXT_FILES = [
    "build/modes.py",
    "build/generate_backgrounds.py",
    "build/render_previews.py",
    "build/prompts.py",
    "build/import_backgrounds.py",
    "README.md",
    "INSTALL.md",
    "CONTRIBUTING.md",
    "docs/ARCHITECTURE.md",
    "docs/PER-VIEW-BACKGROUNDS.md",
    "docs/IMAGE-PROMPTS.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
]

# Directories that carry the mode name.
DIRS = [
    "drop-in/{mode}",
    "www/ultimate-theme/backgrounds/{mode}",
    "docs/previews/{mode}",
]

FILES = [
    "docs/previews/{mode}.webp",
]

AVG_COLORS = "www/ultimate-theme/avg-colors.json"


def variants(old_key: str, new_key: str, new_label: str):
    """Case variants to substitute, longest first so they don't collide."""
    old_title = old_key.title()          # catppuccin -> Catppuccin
    old_upper = old_key.upper()          # CATPPUCCIN
    new_title = new_key.title()
    new_upper = new_key.upper()
    return [
        (f"Ultimate {old_title}", new_label),
        (old_upper, new_upper),
        (old_title, new_title),
        (old_key, new_key),
    ]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("old_key")
    ap.add_argument("new_key")
    ap.add_argument("new_label", help='e.g. "Ultimate Velvet"')
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    old, new, label = args.old_key, args.new_key, args.new_label
    subs = variants(old, new, label)
    dry = args.dry_run
    tag = "[dry-run] " if dry else ""

    # ---- 1. text ----------------------------------------------------------
    for rel in TEXT_FILES:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            print(f"  skip (missing) {rel}")
            continue
        src = open(path, encoding="utf-8").read()
        out = src
        for a, b in subs:
            out = out.replace(a, b)
        if out != src:
            hits = sum(src.count(a) for a, _ in subs)
            print(f"{tag}rewrite {rel}  ({hits} occurrence(s))")
            if not dry:
                open(path, "w", encoding="utf-8").write(out)

    # ---- 2. provenance comment -------------------------------------------
    # The palette values are retained from the original project even though the
    # mode is renamed, so leave a pointer rather than an unexplained constant.
    modes_py = os.path.join(ROOT, "build/modes.py")
    if os.path.exists(modes_py) and not dry:
        s = open(modes_py, encoding="utf-8").read()
        marker = f"{new.upper()}_PALETTE = {{"
        note = ("# Palette values retained from a third-party colour scheme;\n"
                "# see NOTICE.md for attribution.\n")
        if marker in s and "see NOTICE.md for attribution" not in s:
            s = s.replace(marker, note + marker, 1)
            open(modes_py, "w", encoding="utf-8").write(s)
            print(f"{tag}annotated build/modes.py with palette provenance")

    # ---- 3. directories ---------------------------------------------------
    for pat in DIRS:
        src = os.path.join(ROOT, pat.format(mode=old))
        dst = os.path.join(ROOT, pat.format(mode=new))
        if not os.path.isdir(src):
            print(f"  skip (missing) {pat.format(mode=old)}")
            continue
        if os.path.exists(dst):
            print(f"  !! target already exists: {pat.format(mode=new)}")
            continue
        print(f"{tag}move {pat.format(mode=old)} -> {pat.format(mode=new)}")
        if not dry:
            shutil.move(src, dst)

    # ---- 4. loose files ---------------------------------------------------
    for pat in FILES:
        src = os.path.join(ROOT, pat.format(mode=old))
        dst = os.path.join(ROOT, pat.format(mode=new))
        if not os.path.exists(src):
            print(f"  skip (missing) {pat.format(mode=old)}")
            continue
        print(f"{tag}move {pat.format(mode=old)} -> {pat.format(mode=new)}")
        if not dry:
            shutil.move(src, dst)

    # ---- 5. avg-colors.json ----------------------------------------------
    avg_path = os.path.join(ROOT, AVG_COLORS)
    if os.path.exists(avg_path):
        data = json.load(open(avg_path))
        if old in data:
            print(f"{tag}rekey {AVG_COLORS}: {old!r} -> {new!r}")
            if not dry:
                data[new] = data.pop(old)
                json.dump(data, open(avg_path, "w"), indent=2, sort_keys=True)

    print("\nNext:")
    print("  python3 build/generate_themes.py")
    print("  python3 build/verify.py")
    if old in ("catppuccin",):
        print("\nNote: theme names change, so anyone who already selected")
        print(f"'Ultimate {old.title()} - <Area>' must re-pick their theme.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
