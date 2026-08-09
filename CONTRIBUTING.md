# Contributing

Thanks for considering it. This project is generated, so the most important rule
is short:

> **Never edit `themes/ultimate-theme.yaml`.** It is built from `build/` and any
> manual change is overwritten on the next build. CI will catch it.

---

## Setup

```bash
git clone https://github.com/HomeRiz/Home-Assistant-Ultimate-Themes.git
cd Home-Assistant-Ultimate-Themes
pip install numpy Pillow jinja2 pyyaml
```

## The build

```bash
python3 build/generate_themes.py        # themes/ultimate-theme.yaml
python3 build/verify.py                 # must pass before you open a PR
```

Slower ones, only needed when areas or artwork change:

```bash
python3 build/generate_backgrounds.py --resume   # artwork
python3 build/render_previews.py --resume        # docs/previews
python3 build/prompts.py                         # docs/IMAGE-PROMPTS.md
```

`--resume` skips anything that already exists, which turns a two-minute job into
a six-second one.

---

## Common contributions

### Add an area

One line in `build/areas.py`:

```python
("laundry", "Laundry", "mdi:washing-machine", [200, 45, 175, 30], "#4DD0E1", 1024),
#  key       name       icon                   hue anchors          accent     seed
```

- **key** — lowercase, hyphenated. Becomes the filename and the URL. Never change
  an existing one; it breaks everyone's dashboards.
- **hue anchors** — 3–5 HSV hues (0–360) that tell the story of the room.
- **accent** — drives `--primary-color`. Pick against the Glass palette; the
  other two modes re-derive it automatically.
- **seed** — any unused integer. Fixes the composition forever.

Then run backgrounds, previews, themes, verify.

### Change how cards look

`build/template.jinja2` holds all the CSS. Regenerate and verify.

### Change a mode

`build/modes.py` holds palettes, blur, radii, surfaces and tokens. If you touch
anything the artwork reads (`sat`, `val`, `mix`, `bloom`), re-render that mode's
backgrounds too.

### Add support for a custom card

If a card looks wrong — doubled blur, a visible seam, a flat rectangle — it
almost certainly draws its own surface. Add its element name to the exclusion
list in `build/template.jinja2` (search for `EXCLUSIONS`).

Please say which card and version you tested against.

---

## Style

- Comments explain **why**, not what. The what is readable from the code.
- Keep Python to the standard library plus numpy, Pillow, jinja2 and pyyaml.
- British or American spelling, just be consistent within a file.
- No trailing whitespace, LF line endings.

## Pull requests

Small and focused beats large and sweeping. Include before/after screenshots for
anything visual — this is a theme, so screenshots are the review.

CI runs the build, checks the committed output matches, runs `verify.py`, and
validates the repository against HACS. All four must pass.

## Third-party code

Portions of the CSS derive from other MIT-licensed themes; see
[NOTICE.md](NOTICE.md). If you contribute code adapted from another project,
say so in the PR so the notice can be updated.
