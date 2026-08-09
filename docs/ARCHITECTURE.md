# Architecture

How the theme works, and how to change it.

- [The two mechanisms](#the-two-mechanisms)
- [The glass sandwich](#the-glass-sandwich)
- [The background layers](#the-background-layers)
- [Accent propagation](#accent-propagation)
- [Graceful degradation](#graceful-degradation)
- [The exclusion list](#the-exclusion-list)
- [Why one theme file](#why-one-theme-file)
- [Where backgrounds come from](#where-backgrounds-come-from)
- [The build pipeline](#the-build-pipeline)
- [How the artwork is made](#how-the-artwork-is-made)
- [How the previews are made](#how-the-previews-are-made)

---

## The two mechanisms

A Home Assistant theme can only do two things, and this project uses both.

**1. CSS custom properties.** A theme is fundamentally a flat dictionary of CSS
variables that Home Assistant sets on the document root. `primary-color: "#FF9F0A"`
becomes `--primary-color: #FF9F0A`, and every component reading that variable
changes. Native, no dependencies — but it can only change values Home Assistant
chose to expose.

**2. card-mod injection.** Anything not exposed — pseudo-elements, blur layers,
per-component overrides — needs real CSS. card-mod reads magic keys from the
theme and injects their contents into the right shadow roots:

| Key | Injected into |
|---|---|
| `card-mod-root` | `hui-root` — the **Lovelace** root, not the app root |
| `card-mod-card` | every `ha-card` on every dashboard |
| `card-mod-sidebar` | the sidebar |
| `card-mod-view` | each view (tab) |
| `card-mod-config` | built-in panels: Settings, Developer Tools, History |
| `card-mod-panel-custom` | custom panels — but only those *not* embedded in an iframe |

### Why this needs a line in `configuration.yaml`

A recurring question: can the theme not just load card-mod itself?

No. A theme is inert YAML — Home Assistant reads it into CSS custom properties
and nothing more. It cannot execute JavaScript or register a module, and
`extra_module_url` belongs to the `frontend` integration, which reads it once at
startup. There is no hook from one to the other.

A **custom integration** could, and that is the honest alternative:

- `add_extra_js_url(hass, url)` registers the module programmatically — no
  manual line, and no wrong `hacstag`, because the integration can read the
  path that is actually installed rather than one you copied by hand
- `await hass.http.async_register_static_paths([StaticPathConfig(...)])` serves
  the artwork from the integration's own folder, removing the CDN entirely
- it could install the theme file and reload themes on its own

The reasons this project is still a theme:

- converting breaks every existing install — HACS treats Theme and Integration
  as different categories, so everyone would have to remove and re-add it
- a broken theme is ugly; a broken integration can stop Home Assistant starting
- it would not remove the card-mod dependency, only the configuration step
- those APIs churn: the synchronous `register_static_path` was removed in
  2025.7, so an integration is a standing maintenance commitment

One line in `configuration.yaml`, once, is the cheaper trade.

**Iframe panels cannot be themed, by anyone.** Add-on panels (File editor,
Terminal, Studio Code Server) and any custom panel registered with
`embed_iframe: true` — HACS is one — render in a separate document. Neither the
theme's CSS variables nor card-mod cross that boundary; inside, Home Assistant's
default palette applies. This is a browser guarantee, not a limitation worth
working around. To check a panel, open the console and read
`document.querySelector('home-assistant').hass.panels`.

One critical gotcha: **`card-mod-theme` must equal the theme's own name**, exactly.
If it doesn't match, card-mod silently does nothing — no error, just a flat theme.
The generator sets it automatically and `verify.py` checks all 45.

---

## The glass sandwich

Each card is three stacked layers. This is the heart of the whole thing.

```
        ┌─────────────────────────────────┐
 z: 1   │  card content (text, icons)     │  ← never blurred
        ├─────────────────────────────────┤
 z: 0   │  ::after — specular sheen       │  ← bright top rim
        ├─────────────────────────────────┤
 z: -1  │  ::before — backdrop-filter     │  ← the actual blur
        └─────────────────────────────────┘
                    ↓ sees through to
        ┌─────────────────────────────────┐
 z: -1  │  :host::after — scrim           │  ← darkens for legibility
        ├─────────────────────────────────┤
 z: -2  │  :host::before — background img │  ← position: fixed
        └─────────────────────────────────┘
```

Why not put `backdrop-filter` on `ha-card` directly? Two reasons. In some engines
it also blurs the element's own children, and it forces the card into its own
stacking context, which traps overflowing menus. Pushing the blur down to a
`::before` at `z-index: -1` keeps text crisp and lets menus escape.

The `::after` sheen is what makes it read as *glass* rather than *frosted
plastic*. It's a `linear-gradient(160deg, ...)` that's bright at the top-left and
gone by 45% — a light source above and to the left, which is what your eye
expects from a physical pane.

---

## The background layers

The obvious approach is:

```yaml
background-image: "center / cover no-repeat fixed url(...)"
```

`fixed` is ignored or janky on iOS Safari and inside the companion app — the
background jumps during scroll and scales wrong on rubber-band overscroll. The
theme keeps that declaration for compatibility, but the *real* backdrop is
painted in `card-mod-root` onto a genuinely fixed pseudo-element:

```css
:host::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: var(--ultimate-background);
  background-size: cover;
  z-index: -2;
}
```

A second pseudo-element at `z-index: -1` lays a scrim over it. That scrim is what
guarantees legibility — it's why a bright patch in the artwork never makes a card
unreadable.

**`card-mod-root` is the Lovelace root, not the application root.** It is
injected into `hui-root`, which only exists inside a dashboard — so its fixed
backdrop can never reach Settings or Developer Tools. Those panels get their own copy of the
same pseudo-element pair through `card-mod-config` and `card-mod-panel-custom`.

And card-mod itself is only loaded on dashboards unless you register it via
`frontend: extra_module_url` — see [INSTALL.md](../INSTALL.md).

`card-mod-view` declares the same pattern but reads `--ultimate-view-background`.
Views sit inside the root, so a view setting that variable paints over the
theme's own backdrop. That's the per-tab mechanism — see
[PER-VIEW-BACKGROUNDS.md](PER-VIEW-BACKGROUNDS.md).

---

## Accent propagation

Each colour has one accent hex. From that single value the generator derives:

```
colour accent (#FF9F0A)
   ├─ --primary-color
   ├─ --accent-color
   ├─ --state-icon-active-color        active entities
   ├─ --ultimate-glow-color            hover glow, neon borders
   └─ --ha-color-primary-05 … 95       11-stop ladder
         05-30  = accent mixed toward black
         40     = the accent itself
         50-95  = accent mixed toward white
```

That ladder is what Home Assistant 2025+ uses for its newer components.
Hardcoding it per theme would be 792 values; computing it is four lines.

**The accent is not used verbatim in every mode.** An accent is chosen
against the Glass palette, so `accent_for_mode()` in `build/modes.py`
re-expresses it:

| Mode | Transform | Garden `#32D74B` becomes |
|---|---|---|
| Glass | unchanged | `#32D74B` |
| Velvet | snapped to the nearest Velvet accent by hue | `#A6E3A1` |
| Neon | saturation and value pushed to maximum | `#00FF27` |

This is what keeps Velvet genuinely on-palette instead of wearing borrowed
colours, and Neon genuinely luminous. In Neon the accent also flows into
`color-mix()` for borders and glows, so switching colours re-tints the whole
chrome, not just icons.

---

## Graceful degradation

```css
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  ha-card::before { background: rgba(40, 42, 52, 0.86); }
}
```

Without this, a browser that can't blur renders the card's `::before` as a
near-transparent tint over a photograph — every card becomes an unreadable smear.
This is the failure people hit on older Android WebViews.

---

## The exclusion list

Some cards draw their own surface, so glass on top gives doubled blur and a
visible seam. These are opted out:

`hui-heading-card` · `hui-glance-card` · `mushroom-title-card` ·
`mushroom-chips-card` · `.type-custom-bubble-card` · `ha-card.text-only`

If you add a custom card that looks wrong, adding its element name to this list
in `build/template.jinja2` is almost always the fix.

---

## Why one theme file

HACS manages **exactly one** theme configuration file per repository — if
`themes/` holds more than one, only the first is installed. Splitting by mode
would silently ship a third of the project to anyone installing via HACS.

So all 45 themes live in `themes/ultimate-theme.yaml` (~25,000 lines, ~1.1 MB).
Home Assistant parses it once at startup. `verify.py` fails the build if a second
`.yaml` ever appears in `themes/`, and so does CI.

---

## Where backgrounds come from

HACS copies the theme YAML and **nothing else** — it never touches
`/config/www`. A HACS install therefore can't rely on `/local/` URLs, or every
background would 404 on a fresh setup.

The generator supports both:

```bash
python3 build/generate_themes.py --base cdn     # default
python3 build/generate_themes.py --base local
```

| | `cdn` | `local` |
|---|---|---|
| URL | `https://cdn.jsdelivr.net/gh/<repo>@<ref>/www/…` | `/local/ultimate-theme/backgrounds/…` |
| HACS install | works with no extra steps | backgrounds 404 until you copy `www/` |
| Works offline | no | yes |
| Updating art | needs a CDN cache cycle | instant |

The shipped file uses `cdn`. Anyone who wants everything self-hosted copies
`www/` to `/config/www/` and rebuilds with `--base local`.

> jsDelivr caches `@main` for up to seven days. Once you cut a release, change
> `CDN_REF` in `build/generate_themes.py` to that tag so background updates are
> predictable.

---

## The build pipeline

```
build/areas.py     ─┐
                    ├─→ generate_backgrounds.py ─→ www/…/*.webp
build/modes.py     ─┤                                    │
                    │                              avg-colors.json
                    │                                    │
                    ├─→ render_previews.py ─→ docs/previews/*
                    │                                    │
build/template.jinja2 ──→ generate_themes.py ←───────────┘
                                  │
                                  ├─→ themes/ultimate-theme.yaml      (45 themes)
                                  └─→ dashboards/per-view-backgrounds.yaml

build/prompts.py  ──→ docs/IMAGE-PROMPTS.md, docs/image-prompts.tsv
build/verify.py   ──→ validates every value in every theme
```

`avg-colors.json` is the interesting link. After rendering each background the
generator averages the image down to a single pixel and stores that colour. The
theme generator darkens it 25% and uses it as `app-theme-color` — what browsers
use to tint the address bar and Android uses for the task switcher. So each
dashboard's browser chrome matches its own artwork.

---

## How the artwork is made

`build/generate_backgrounds.py` is a small renderer, not an AI model:

1. **fBm noise** — octave-summed value noise, built at quarter resolution and
   upscaled. Every octave is already band-limited well below Nyquist at full
   resolution, so the detail would be discarded anyway. Measured at about
   5× faster for the noise pass.
2. **Domain warping** — the coordinate grid is displaced by that noise, turning
   circular blobs into organic shapes.
3. **Mesh gradient** — colour blobs on a golden-angle spiral, blended with power
   weighting (`w ** 2.6`) so the nearest blob dominates. Plain averaging produces
   mud; this keeps hues distinct.
4. **Grade** — base blend, chroma boost, depth modulation, light sweep, hero
   glow, screen-blended gaussian bloom, vignette, film grain.
5. **Mode extras** — Neon adds scanlines and chromatic edge lift. Velvet
   snaps every blob hue to the nearest Velvet accent, with a saturation boost so
   the pastel palette doesn't drain to grey once blobs blend.

Each colour has a fixed seed, so **the composition is identical across all three
modes** — only palette and grade change. That is what makes Amber still read as
Amber when you switch aesthetics.

---

## How the previews are made

`build/render_previews.py` composites a mock dashboard over each background.

The blur is real. For every panel the renderer crops the region of the backdrop
underneath it, runs a Gaussian blur at that mode's radius, tints it, and
composites it back through a rounded-rectangle mask — the same operation
`backdrop-filter` performs in the browser. Sheen, bevel, border and outer glow
are then drawn from the same values the CSS uses.

That makes the previews representative rather than illustrative, which matters:
they are the only way to see the theme without installing it.

`SPECS` in that file mirrors `MODES` in `build/modes.py`. If you change blur,
radius or tint in one, change it in the other or the previews will quietly drift
away from reality.
