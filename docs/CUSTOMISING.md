# Customising

Everything visible in this theme is generated from `build/`. This page covers
what the theme does, how to rebuild it, and how to replace the artwork with your
own.

For the CSS internals — how the glass engine is put together, which card-mod
block reaches which panel, and why — see [ARCHITECTURE.md](ARCHITECTURE.md).

---

## What the theme does

- **Specular sheen** — an `::after` rim gradient, so cards read as glass rather
  than frosted plastic
- **Graceful degradation** — an `@supports` fallback swaps in solid surfaces
  where `backdrop-filter` is unsupported, instead of rendering unreadable
- **iOS-safe backgrounds** — painted onto a fixed pseudo-element, because
  `background-attachment: fixed` misbehaves on iOS Safari and the companion app
- **Per-view background hook** — one dashboard, a different backdrop per tab
- **Full accent ladder** — `--ha-color-primary-05..95` computed per colour
- **Hover lift** — guarded by `prefers-reduced-motion`
- **button-card templates** — `ultimate_glass`, `ultimate_glass_icon`,
  `ultimate_glass_tile`, `ultimate_flat`, `ultimate_neon`
- **Card compatibility** — Mushroom, Bubble Card, heading, glance and text-only
  cards are excluded from the glass layer so they don't double-blur

---

## Rebuilding

**Never edit `themes/ultimate-theme.yaml`.** It is rebuilt from `build/` and your
changes will be lost.

```bash
pip install numpy Pillow jinja2 pyyaml

python3 build/generate_themes.py      # rebuild themes
python3 build/verify.py               # validates every value in every theme
```

| Want to change | Edit | Then |
|---|---|---|
| How cards look | `build/template.jinja2` | regenerate themes |
| A mode's palette or geometry | `build/modes.py` | regenerate themes |
| Add a colour | `build/areas.py` | backgrounds `--resume`, previews `--resume`, themes |
| The artwork itself | `build/generate_backgrounds.py` | re-render that mode |

Copy the rebuilt `themes/ultimate-theme.yaml` onto the instance, then
Developer Tools → **Reload themes**.

Put it *over* the existing file rather than beside it. If you installed via HACS
that means `/config/themes/ultimate-theme/ultimate-theme.yaml`; a second copy at
`/config/themes/ultimate-theme.yaml` defines all 45 theme names twice, because
the include recurses into subfolders.

**If you customise and want HACS to keep managing it:** fork this repository,
push your changes, and add *your fork* as the custom repository instead. Then
your edits survive updates. Copying files over Samba or SSH works too, but HACS
will overwrite them on the next update.

---

## Self-hosting the images

The default build loads backgrounds from jsDelivr, because HACS installs the
theme YAML and nothing else — `/local/` URLs would 404 on a fresh install.

To serve them from your own Home Assistant instead, copy `www/` to `/config/www/`
and rebuild:

```bash
python3 build/generate_themes.py --base local
```

[Why this trade-off exists →](ARCHITECTURE.md#where-backgrounds-come-from)

---

## Using your own artwork

The shipped backgrounds are generated procedurally.
[`IMAGE-PROMPTS.md`](IMAGE-PROMPTS.md) has a ready-to-paste prompt for every
image, and [`image-prompts.tsv`](image-prompts.tsv) is the same list as
`target<TAB>prompt` rows if you're driving a batch tool.

Running `python3 build/prompts.py` also writes a `prompt.txt` into each
`drop-in/<style>/` folder, so the prompts sit in the folder the images are going
into.

```bash
mkdir -p drop-in/{glass,velvet,neon}    # local workspace, not tracked by git

# save yours as drop-in/<style>/<colour-key>.png, then:
python3 build/import_backgrounds.py     # crop, darken, convert, re-tint headers
python3 build/generate_themes.py
```

The filename must match the colour key exactly — that is how the importer knows
where each image goes. Anything you don't supply keeps its generated background,
so you can replace them a few at a time.

### Styles with prompts but no theme

`glass`, `velvet` and `neon` are complete visual systems — palette, blur
character, geometry and accent language all live in `build/modes.py`.

Seven more exist as **artwork prompts only**: `cyberprep`, `cyberpunk`,
`solarpunk`, `art-deco`, `dark-academia`, `cottagecore` and `synthwave`. The
importer will process anything you drop into their folders, but no theme
references the results yet. Turning one into a real mode means choosing its
palette, blur, radii and border language in `build/modes.py` — a design
decision, not a mechanical one.
