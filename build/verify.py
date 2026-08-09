#!/usr/bin/env python3
"""
Verification pass. Run before every commit; CI runs it on every push.

Catches the failures that would otherwise only show up as a broken dashboard:
  1. the theme file parses as YAML
  2. exactly one theme file exists (HACS manages only the first one it finds)
  3. no duplicate theme names
  4. every card-mod-theme value matches the theme it sits in
     (card-mod silently does nothing if this is wrong - the classic failure)
  5. every background URL resolves to a file that exists in this repository
  6. every CSS block has balanced braces
  7. no unresolved template syntax leaked into the output
  8. every area has artwork and a preview in every mode
  9. documentation and dashboard helper files are present
"""

from __future__ import annotations

import os
import re
import sys

# Set before importing anything local: this script checks that no __pycache__ is
# committed, and would otherwise fail on the bytecode its own imports create.
sys.dont_write_bytecode = True

import yaml  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from areas import AREA_KEYS   # noqa: E402
from modes import MODES       # noqa: E402

THEMES = os.path.join(ROOT, "themes")
WWW = os.path.join(ROOT, "www")

CDN_PREFIX = "https://cdn.jsdelivr.net/gh/"
LOCAL_PREFIX = "/local/"

# The complete set of card-mod theme types, from card-mod's README-themes.md.
# "theme" is the name-matching key, not a type. Anything outside this set is
# accepted by YAML, ignored by card-mod, and impossible to notice by eye.
CARD_MOD_TYPES = {
    "theme",
    "card", "row", "glance", "badge", "heading-badge", "assist-chip", "element",
    "root", "view", "more-info", "sidebar", "config", "panel-custom",
    "top-app-bar-fixed", "dialog",
}

errors: list[str] = []
warnings: list[str] = []
checks = 0


def check(cond: bool, msg: str) -> None:
    global checks
    checks += 1
    if not cond:
        errors.append(msg)


def url_to_disk(url: str) -> str | None:
    """Map a theme background URL back to its path inside this repository."""
    if url.startswith(LOCAL_PREFIX):
        return os.path.join(WWW, url[len(LOCAL_PREFIX):])
    if url.startswith(CDN_PREFIX):
        # https://cdn.jsdelivr.net/gh/<owner>/<repo>@<ref>/<path>
        tail = url[len(CDN_PREFIX):]
        if "/" not in tail:
            return None
        parts = tail.split("/", 2)
        if len(parts) < 3:
            return None
        return os.path.join(ROOT, parts[2])
    return None


def main() -> int:
    global checks

    files = sorted(f for f in os.listdir(THEMES) if f.endswith((".yaml", ".yml")))
    check(len(files) == 1,
          f"themes/ must contain exactly one theme file (HACS installs only the "
          f"first); found {len(files)}: {files}")
    if not files:
        print("FAILED - no theme file")
        return 1

    fn = files[0]
    raw = open(os.path.join(THEMES, fn)).read()

    for tok in ("{{", "{%", "}}"):
        check(tok not in raw, f"{fn}: unresolved template token {tok!r}")

    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        print(f"FAILED - {fn}: YAML parse error: {e}")
        return 1
    checks += 1

    expected = len(MODES) * (1 + len(AREA_KEYS))
    check(len(data) == expected,
          f"expected {expected} themes, found {len(data)}")

    seen: set[str] = set()
    for name, theme in data.items():
        check(name not in seen, f"duplicate theme name {name!r}")
        seen.add(name)

        cmt = theme.get("card-mod-theme")
        check(cmt == name,
              f"{name!r}: card-mod-theme={cmt!r} must equal its own name")

        # A `backdrop-filter` on a dialog surface turns that surface into a
        # containing block for every `position: fixed` descendant, so any
        # dropdown opened inside the dialog anchors to the dialog instead of
        # the viewport and renders outside it. Home Assistant also copies theme
        # variables onto the body of custom-panel iframes, so this escapes into
        # HACS and every other embedded panel. Nothing errors - the menu just
        # lands in the wrong place, which is easy to blame on the panel.
        checks += 1
        dlg = str(theme.get("ha-dialog-surface-backdrop-filter", "none")).strip()
        if dlg and dlg != "none":
            errors.append(
                f"{name!r}: ha-dialog-surface-backdrop-filter must be 'none' - "
                f"got {dlg!r}. It makes dialogs a containing block and throws "
                f"dropdowns opened inside them out of position.")

        bg = str(theme.get("ultimate-background", ""))

        # --ultimate-background is consumed by `background-image`, so it must be
        # an <image>, never a `background:` shorthand. A shorthand here parses
        # as an invalid background-image, the whole declaration is dropped, and
        # the backdrop just silently fails to paint - no console error, nothing.
        checks += 1
        first = bg.split("(", 1)[0].strip().lower()
        if first and not first.startswith(("url", "linear-gradient",
                                           "radial-gradient", "conic-gradient",
                                           "image-set", "none")):
            errors.append(
                f"{name!r}: ultimate-background must be a bare <image>, not a "
                f"background shorthand - got {bg[:60]!r}")

        m = re.search(r"url\('([^']+)'\)", bg)
        if m:
            url = m.group(1)
            disk = url_to_disk(url)
            check(disk is not None, f"{name!r}: unrecognised background URL {url}")
            if disk:
                check(os.path.exists(disk),
                      f"{name!r}: background missing from repo -> {url}")
                if os.path.exists(disk):
                    check(os.path.getsize(disk) > 1024,
                          f"{name!r}: background looks truncated -> {url}")

        for key, val in theme.items():
            if key.startswith("card-mod") and isinstance(val, str):
                checks += 1
                if val.count("{") != val.count("}"):
                    errors.append(
                        f"{name!r} -> {key}: unbalanced braces "
                        f"({val.count('{')} open, {val.count('}')} close)")

            # card-mod ignores unknown keys without a word of warning, so a typo
            # or an invented type is dead CSS you will never be told about.
            # Types are from card-mod's README-themes.md.
            if key.startswith("card-mod-"):
                checks += 1
                base = key[len("card-mod-"):]
                if base.endswith("-yaml"):
                    base = base[:-len("-yaml")]
                if base.endswith("-debug"):
                    base = base[:-len("-debug")]
                if base not in CARD_MOD_TYPES:
                    errors.append(
                        f"{name!r}: {key!r} is not a card-mod type - it will be "
                        f"silently ignored. Valid: {', '.join(sorted(CARD_MOD_TYPES))}")

        for req in ("modes", "primary-color", "ha-card-backdrop-filter",
                    "card-mod-card", "card-mod-root", "card-mod-view"):
            check(req in theme, f"{name!r}: missing required key {req!r}")

        # Home Assistant rejects the whole themes file if `modes` is malformed,
        # and the error it logs does not name the offending theme.
        m = theme.get("modes")
        check(isinstance(m, dict), f"{name!r}: 'modes' must be a mapping")
        if isinstance(m, dict):
            check(set(m) == {"light", "dark"},
                  f"{name!r}: 'modes' must contain exactly light and dark, "
                  f"got {sorted(m)}")
            for variant, body in m.items():
                check(isinstance(body, dict),
                      f"{name!r}: modes.{variant} must be a mapping")

        # Every value must be a scalar or block string. A nested mapping outside
        # `modes` silently breaks HA's theme loader.
        for key, val in theme.items():
            if key == "modes":
                continue
            check(not isinstance(val, (dict, list)),
                  f"{name!r}: key {key!r} has a nested "
                  f"{type(val).__name__}, which HA cannot load")

        # No null or empty values, anywhere, including inside `modes`.
        #
        # This is the check that matters most. An unquoted hex colour such as
        #     primary-background-color: #1e1e2e
        # is a *comment* in YAML, so the value parses as null. Home Assistant
        # then rejects the whole themes file and not a single theme loads - and
        # nothing in the log points at the offending line. Structure checks pass
        # happily, because the key is present and `modes` is still a mapping.
        def scan(node, path: str) -> None:
            if isinstance(node, dict):
                for k, v in node.items():
                    scan(v, f"{path}.{k}" if path else str(k))
                return
            if isinstance(node, list):
                for i, v in enumerate(node):
                    scan(v, f"{path}[{i}]")
                return
            checks_local.append(1)
            if node is None:
                errors.append(
                    f"{name!r}: {path} is null - most likely an unquoted value "
                    f"starting with '#', which YAML reads as a comment")
            elif isinstance(node, str) and not node.strip():
                errors.append(f"{name!r}: {path} is empty")

        checks_local: list[int] = []
        scan(theme, "")
        checks += len(checks_local)

    # -- artwork + previews --------------------------------------------------
    for mode in MODES:
        for key in AREA_KEYS:
            check(os.path.exists(
                os.path.join(WWW, "ultimate-theme", "backgrounds", mode, f"{key}.webp")),
                f"missing artwork: {mode}/{key}.webp")
            check(os.path.exists(
                os.path.join(ROOT, "docs", "previews", mode, f"{key}.webp")),
                f"missing preview: {mode}/{key}.webp")
        check(os.path.exists(os.path.join(ROOT, "docs", "previews", f"{mode}.webp")),
              f"missing contact sheet: {mode}.webp")

    # -- repository files ----------------------------------------------------
    for doc in ("README.md", "INSTALL.md", "NOTICE.md", "LICENSE",
                "CONTRIBUTING.md", "hacs.json", ".gitignore",
                "docs/ARCHITECTURE.md", "docs/PER-VIEW-BACKGROUNDS.md",
                "docs/IMAGE-PROMPTS.md", "CHANGELOG.md",
                "dashboards/button-card-templates.yaml",
                "dashboards/per-view-backgrounds.yaml",
                ".github/workflows/validate.yml"):
        check(os.path.exists(os.path.join(ROOT, doc)), f"missing file: {doc}")

    # -- hygiene: nothing that should not be published -----------------------
    # What matters is whether a file would be *committed*, not whether it exists
    # on disk. macOS recreates .DS_Store every time Finder opens a folder, so
    # failing on mere presence would make the build red for no reason. Ask git
    # instead, and only fall back to presence when git isn't available.
    import subprocess

    def git_ignores(path: str) -> bool | None:
        """True/False if git can answer, None if there is no usable git."""
        try:
            r = subprocess.run(["git", "check-ignore", "-q", path],
                               cwd=ROOT, capture_output=True, timeout=10)
        except (OSError, subprocess.SubprocessError):
            return None
        if r.returncode in (0, 1):
            return r.returncode == 0
        return None                      # 128 = not a git repo

    junk_found: list[str] = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for name in list(filenames) + [d for d in dirnames if d == "__pycache__"]:
            if name in (".DS_Store", "Thumbs.db", ".env", "__pycache__"):
                junk_found.append(os.path.join(dirpath, name))

    for path in junk_found:
        rel = os.path.relpath(path, ROOT)
        ignored = git_ignores(path)
        if ignored is True:
            warnings.append(f"{rel} exists but is git-ignored, so it will not "
                            f"be published (delete it if you want a tidy tree)")
        else:
            # git says it would be committed, or there is no git to ask
            check(False, f"{rel} would be committed - add it to .gitignore "
                         f"or delete it")

    # -- hacs.json -----------------------------------------------------------
    # HACS validates this with voluptuous using extra=PREVENT_EXTRA, so a single
    # unrecognised key fails the whole manifest check. Mirror the real schema
    # (custom_components/hacs/utils/validate.py) rather than trusting the docs
    # table, which is missing at least render_readme.
    HACS_KEYS = {
        "content_in_root": bool, "country": (str, list), "filename": str,
        "hacs": str, "hide_default_branch": bool, "homeassistant": str,
        "persistent_directory": str, "render_readme": bool,
        "zip_release": bool, "name": str,
    }
    import json
    try:
        hacs = json.load(open(os.path.join(ROOT, "hacs.json")))
        check("name" in hacs, "hacs.json missing required key 'name'")
        check(hacs.get("filename") == fn,
              f"hacs.json filename={hacs.get('filename')!r} but theme file is {fn!r}")
        for key, val in hacs.items():
            check(key in HACS_KEYS,
                  f"hacs.json: unknown key {key!r} - HACS rejects the whole "
                  f"manifest on any extra key")
            if key in HACS_KEYS:
                check(isinstance(val, HACS_KEYS[key]),
                      f"hacs.json: {key!r} should be "
                      f"{HACS_KEYS[key]}, got {type(val).__name__}")
    except (OSError, ValueError) as e:
        errors.append(f"hacs.json unreadable: {e}")

    # -- README must contain an image HACS will render ------------------------
    # HACS scans the readme for a line with '<img' or '![' that is not a shield
    # or a buymeacoffee link. Badges alone do not count.
    try:
        readme = open(os.path.join(ROOT, "README.md")).read()
        ignored = ("-shield", "img.shields.io", "buymeacoffee.com")
        has_image = any(
            ("<img" in line or "![" in line)
            and not any(i in line for i in ignored)
            for line in readme.splitlines())
        check(has_image,
              "README.md has no image that HACS will count - badges are "
              "ignored, so at least one real screenshot is required")
    except OSError as e:
        errors.append(f"README.md unreadable: {e}")

    print(f"theme file : {fn}")
    print(f"themes     : {len(seen)}")
    print(f"checks run : {checks}")
    if warnings:
        print(f"\nwarnings ({len(warnings)}) - not blocking:")
        for w in warnings:
            print(f"  ! {w}")
    # A real hacstag in the docs is not a secret - it is just the version stamp
    # HACS puts on the file - but it is per-instance and changes on every
    # card-mod update, and people copy examples. A copied one 404s only on
    # non-Lovelace panels while dashboards keep working, which reads as a theme
    # bug rather than a wrong URL. Keep the docs unpastable.
    for doc in ("README.md", "INSTALL.md"):
        path = os.path.join(ROOT, doc)
        if os.path.exists(path):
            checks += 1
            for m in re.finditer(r"hacstag=(\d{6,})", open(path).read()):
                errors.append(
                    f"{doc}: contains a literal hacstag {m.group(1)!r}. Use a "
                    f"placeholder - a copied hacstag 404s on Settings only.")

    # Two things HACS's markdown renderer does that GitHub does not, both
    # measured on a live instance:
    #
    #  1. It strips `src` from raw HTML <img> tags. Only markdown-syntax images
    #     survive. On the repository page everything looks perfect; in HACS the
    #     gallery is a column of empty boxes.
    #  2. It resolves image URLs against the repository, and gets confused when
    #     a markdown image sits inside a *relative* link - it prefixes the
    #     absolute image URL with raw.githubusercontent.com/<owner>/<repo>/<tag>/
    #     and the badge 404s.
    #
    # So: markdown images only, and never inside a relative link.
    readme = os.path.join(ROOT, "README.md")
    if os.path.exists(readme):
        text = open(readme).read()

        checks += 1
        n_html_img = len(re.findall(r"<img\b", text))
        if n_html_img:
            errors.append(
                f"README.md: {n_html_img} raw <img> tag(s). HACS strips their "
                f"src - use markdown ![alt](url) instead.")

        for m in re.finditer(r"\[!\[[^\]]*\]\(([^)]+)\)\]\(([^)]+)\)", text):
            checks += 1
            img, link = m.group(1), m.group(2)
            if not img.startswith(("http://", "https://")):
                errors.append(
                    f"README.md: image {img!r} is relative - it 404s inside HACS.")
            if not link.startswith(("http://", "https://")):
                errors.append(
                    f"README.md: image linked to relative target {link!r}. HACS "
                    f"rewrites the image URL when it sees this and the image breaks.")

        for m in re.finditer(r"(?<!\[)!\[[^\]]*\]\(([^)]+)\)", text):
            checks += 1
            if not m.group(1).startswith(("http://", "https://")):
                errors.append(
                    f"README.md: image {m.group(1)!r} is relative - it 404s "
                    f"inside HACS. Use an absolute URL.")

    # The README references preview images by name. When the colour registry
    # was renamed, those references silently kept pointing at rooms that no
    # longer existed - and one of them, kitchen, had been deleted outright. The
    # repository page just showed a broken image. Check they resolve.
    if os.path.exists(readme):
        for m in re.finditer(r"docs/previews/([A-Za-z0-9/_-]+\.webp)", open(readme).read()):
            checks += 1
            rel = os.path.join("docs", "previews", m.group(1))
            if not os.path.exists(os.path.join(ROOT, rel)):
                errors.append(
                    f"README.md references {rel} which does not exist - a "
                    f"renamed or retired colour left the link behind.")

    if errors:
        print(f"\nFAILED - {len(errors)} error(s):")
        for e in errors[:40]:
            print(f"  x {e}")
        if len(errors) > 40:
            print(f"  ... and {len(errors) - 40} more")
        return 1
    print("\nOK - all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
