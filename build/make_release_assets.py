#!/usr/bin/env python3
"""
Build the files to attach to a GitHub release.

HACS downloads the theme YAML and nothing else - for the `theme` category there
is no way to make it fetch `www/` as well (`zip_release` exists, but HACS
supports it for integrations only). So the CDN build is the one HACS installs.

For anyone who wants the images served from their own instance, cloning the repo
and running Python is a lot of ceremony. These assets remove it: two downloads,
drop them in, done.

Produces, in dist/:

  ultimate-theme-backgrounds-<version>.zip
      the whole www/ tree, ready to unzip into /config/www/

  ultimate-theme-local-<version>.yaml
      the theme built with /local/ URLs, ready to drop into /config/themes/

Usage
  python3 build/make_release_assets.py v0.0.1
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import zipfile

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DIST = os.path.join(ROOT, "dist")
THEME = os.path.join(ROOT, "themes", "ultimate-theme.yaml")


def run(*args: str) -> None:
    subprocess.run([sys.executable, *args], cwd=ROOT, check=True,
                   stdout=subprocess.DEVNULL)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("version", help="release tag, e.g. v0.0.1")
    args = ap.parse_args()
    ver = args.version

    os.makedirs(DIST, exist_ok=True)

    # ---- 1. backgrounds archive -------------------------------------------
    zip_path = os.path.join(DIST, f"ultimate-theme-backgrounds-{ver}.zip")
    src_root = os.path.join(ROOT, "www")
    count = 0
    # WebP is already compressed, so storing beats deflating on both size and time.
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_STORED) as z:
        for dirpath, _, filenames in os.walk(src_root):
            for fn in sorted(filenames):
                if fn.startswith("."):
                    continue
                full = os.path.join(dirpath, fn)
                z.write(full, os.path.relpath(full, src_root))
                count += 1
    print(f"{os.path.relpath(zip_path, ROOT)}"
          f"  ({count} files, {os.path.getsize(zip_path) / 1024 / 1024:.1f} MB)")
    print("  unzip into /config/www/ -> /config/www/ultimate-theme/...")

    # ---- 2. the /local/ build ---------------------------------------------
    # Generate it, copy it aside, then restore the CDN build so the working tree
    # is never left holding the wrong variant.
    run(os.path.join("build", "generate_themes.py"), "--base", "local")
    local_path = os.path.join(DIST, f"ultimate-theme-local-{ver}.yaml")
    shutil.copyfile(THEME, local_path)
    run(os.path.join("build", "generate_themes.py"))          # back to cdn

    with open(THEME) as f:
        head = f.read(400)
    if "Backgrounds: cdn" not in head:
        print("ERROR: working tree is not back on the CDN build", file=sys.stderr)
        return 1

    print(f"{os.path.relpath(local_path, ROOT)}"
          f"  ({os.path.getsize(local_path) / 1024:.0f} KB)")
    print("  drop into /config/themes/ (replacing any existing copy)")
    print("\nWorking tree restored to the CDN build.")
    print(f"Attach both files to the {ver} release.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
