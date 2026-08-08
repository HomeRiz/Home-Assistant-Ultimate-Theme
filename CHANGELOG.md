# Changelog

All notable changes to this project are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.0.6] — 2026-08-08

Ships the README fix that 0.0.5 could not: it landed one commit after the tag,
and **HACS renders the README from the installed release's tag, not from
`main`.** The repository page showed the corrected version the whole time while
HACS kept serving the old one — which is why the gallery looked fixed and the
licence badge did not.

### Fixed

- Images in the README are markdown, not raw HTML. HACS's markdown renderer
  strips `src` from `<img>` tags; measured on a live instance, 13 of 19 images
  had no `src` at all.
- The licence badge no longer sits inside a relative link. HACS reacted to
  `](LICENSE)` by prefixing the badge's absolute URL with
  `raw.githubusercontent.com/<owner>/<repo>/<tag>/`, and by sending the click to
  the HACS panel instead of the repository.
- `verify.py` rejects raw `<img>` tags, relative image URLs, and images wrapped
  in relative links.

No theme CSS changed. `CDN_REF` moves to `0.0.6` so the artwork URLs stay
self-consistent with their tag.

---

## [0.0.5] — 2026-08-08

No theme changes. Documentation, packaging and the artwork pipeline.

### Fixed

- **Every image in the README was broken inside HACS.** The paths were relative,
  which works on GitHub but not in HACS — it renders the README inside Home
  Assistant, so `docs/previews/glass.webp` resolved against
  `http://<your-instance>:8123/` and 404'd. The repository page looked perfect
  while the HACS page showed broken icons with the user's own IP in the URL.
  All images are now absolute `raw.githubusercontent.com` URLs.

  **That alone was not enough**, found after 0.0.5 was tagged. Measured on a
  live instance: of 19 images on the HACS page, 13 had no `src` attribute at
  all. HACS's markdown renderer strips `src` from raw HTML `<img>` tags —
  only markdown-syntax images survive. The gallery was written as HTML for the
  `width` control, so it rendered as a column of empty boxes.

  Separately, the licence badge was the only image wrapped in a *relative*
  link (`](LICENSE)`), and HACS responded by prefixing its absolute URL with
  `raw.githubusercontent.com/<owner>/<repo>/<tag>/` — producing a URL with two
  schemes in it.

  Every image is markdown now, every link target is absolute, and the `width`
  attributes are gone with them. `verify.py` rejects raw `<img>` tags, relative
  image URLs, and images inside relative links.
- The licence badge depended on GitHub's licence detection and rendered broken.
  It is a static MIT badge now.
- The README carried a real `hacstag` as an example. Not a secret — it is the
  version stamp HACS puts on the file — but it invited copy-paste, and a copied
  `hacstag` 404s *only* on Settings while dashboards keep working, which reads
  as a theme bug rather than a wrong URL. Replaced with a placeholder.

### Added

- **One-click install buttons** for card-mod and for this theme, via
  My Home Assistant.
- Install is now five explicit steps, including where to find your own card-mod
  URL (Settings → Dashboards → ⋮ → Resources) and the fact that the module is
  fetched asynchronously — Settings can render plain for a few seconds after a
  restart and then pick up the background. That is not a broken install.
- Gallery images are click-to-enlarge and smaller inline; the 23 areas are a
  grouped table rather than a run-on line.
- [`docs/CUSTOMISING.md`](docs/CUSTOMISING.md) — the feature list, rebuild
  instructions and own-artwork workflow, moved out of the README.
- `docs/ARCHITECTURE.md` explains why the theme cannot load card-mod itself,
  what a custom integration would change, and why this is still a theme.
- **Artwork prompts for seven more aesthetics:** `cyberprep`, `cyberpunk`,
  `solarpunk`, `art-deco`, `dark-academia`, `cottagecore` and `synthwave`.
  Prompts only — no palettes yet, so no new themes. `build/prompts.py` writes a
  `prompt.txt` into each `drop-in/<style>/` folder, so the prompts sit where the
  images go.
- A palette arbitration clause in every prompt. The 23 subjects are shared
  across styles and several name a colour outright, which was harmless while all
  three modes were abstract light — but Art Deco in amber is not the brief. The
  style palette now wins while composition and light direction carry over.

### Changed

- `build/import_backgrounds.py` takes its style list from `build/prompts.py`
  instead of hardcoding three names, so a new `drop-in/<style>/` folder is no
  longer skipped in silence.
- `verify.py` gained two guards: it fails on a relative image path in the README,
  and on a literal `hacstag` in the README or install guide.

---

## [0.0.4] — 2026-08-04

### Fixed

- **Dropdowns opened inside a dialog no longer land outside it.** This is the
  HACS bug 0.0.3 claimed to fix and did not. The real cause was a single theme
  variable:

  ```yaml
  ha-dialog-surface-backdrop-filter: var(--ha-card-backdrop-filter)
  ```

  `backdrop-filter` makes an element a containing block for every
  `position: fixed` descendant. MDC renders select menus as
  `.mdc-menu-surface--fixed`, so with a blurred dialog surface the menu anchored
  to the dialog instead of the viewport — and rendered outside it, with the
  dialog's own contents dragged along.

  It reached HACS because **Home Assistant copies theme variables onto the body
  of custom-panel iframes.** card-mod never enters that frame, and neither does
  any of this theme's CSS — but the variables do. That is what made the bug so
  hard to place: every inspection of the frame's `documentElement` showed
  Home Assistant's defaults, while its `<body>` carried 315 theme variables.

  Dialog surfaces are no longer blurred. They keep their tint from
  `ha-dialog-surface-background`, and the scrim behind them stays blurred — a
  scrim is a sibling of the dialog, so it has no fixed descendants to displace.
  `card-mod-dialog` no longer applies `backdrop-filter` either, for the same
  reason: it would have done this to every dialog in the main document too.

- `verify.py` fails if `ha-dialog-surface-backdrop-filter` is ever set to
  anything but `none`.

### Correction to 0.0.3

The 0.0.3 notes blamed `backdrop-filter` on the `ha-sidebar` host and presented
a table of measurements to support it. That diagnosis was wrong. The bug is
intermittent, the trials were too few to tell a fix from a lucky run, and the
"4/4 correct" result did not survive retesting. The sidebar change shipped in
0.0.3 is harmless and stays, but it never fixed anything.

The other three fixes in 0.0.3 — per-view backdrops, the Settings backdrop, and
the base themes' missing background — are unaffected and remain correct.

---

## [0.0.3] — 2026-08-03

Most of this release is one lesson twice over: `:host` only means what you think
it means if the element card-mod is styling actually has a shadow root.
`ha-panel-config` and `hui-view` do not, so card-mod falls back to the enclosing
shadow root and `:host` silently resolves to the wrong element. Nothing errors;
the CSS just lands somewhere useless.

The last entry is the opposite failure — CSS that landed exactly where it was
aimed, on the `ha-sidebar` host, and broke something in a different document.

### Fixed

- **A per-view `theme:` now changes the backdrop, not just the colours.** Home
  Assistant applies a view's theme to `hui-view-container`, which sits *below*
  `hui-root` — so the backdrop painted by `card-mod-root` always resolved to
  the profile theme however the tab was set. The backdrop is now painted at
  view level, inside the scope the view theme reaches. Set `theme:` on a view
  and the image follows.
- **Settings, Developer Tools and History** paint their backdrop on `ha-drawer`
  rather than on the panel. The drawer spans the whole viewport, so the
  sidebar's blur has an image behind it — no more themed content area sitting
  next to a flat grey sidebar.
- The negative-`z-index` pseudo-elements those blocks used could not render
  anyway: with no stacking context to sit behind, `z-index: -2` puts the layer
  behind the document background.
- `--ultimate-background` was a `background:` shorthand in the three base
  themes, which is not a valid `background-image` value — so the declaration
  was dropped and their backdrop never painted. It is now always a bare image,
  and `verify.py` fails if that ever regresses.
- **Dialogs inside iframe panels no longer break, and the sidebar keeps its
  blur.** `backdrop-filter` on the `ha-sidebar` *host* corrupts the layout of an
  iframe rendered next to it: Chrome composites the blurred host onto its own
  layer and the iframe's document resolves positions against a stale coordinate
  space, so elements are painted at an origin their own parent disagrees with.
  In HACS this showed up as a download dialog with its contents spilling outside
  the box and the version dropdown floating loose.

  The blur now goes on the sidebar's inner elements instead of its host. The
  visual result is identical — they cover the whole sidebar — but the host is no
  longer a backdrop root sitting beside the frame. Measured on that dialog; the
  surface is always `[525, 197]`, the numbers are where its children land:

  | | children | result |
  |---|---|---|
  | blur on `:host` | `[136, 33]` | broken, 3/3 |
  | `will-change: transform` on the iframe | `[136, 33]` | broken |
  | `translateZ(0)` on `ha-panel-custom` | `[136, 33]` | broken |
  | `translateZ(0)` on the iframe | — | flaky: passed once, failed once |
  | `contain: paint` on the sidebar | `[136, 33]` | broken, 2/2 |
  | blur on `.menu` / `.panels-list` | `[525, 250]` | correct, 4/4 |

  This only became reachable in 0.0.2, which introduced `extra_module_url` —
  that is what makes card-mod run outside Lovelace, so before it the sidebar was
  never blurred on a panel like HACS to begin with.

---

## [0.0.2] — 2026-08-03

### Fixed

- `card-mod-drawer-yaml` was not a real card-mod type, so that block had never
  applied. card-mod ignores unknown keys silently, which is why it went
  unnoticed. Removed.
- `verify.py` now validates every `card-mod-*` key against card-mod's documented
  type list and fails on anything else.

### Added

- `card-mod-config` and `card-mod-panel-custom`, so the backdrop and glass reach
  Settings, Developer Tools, History and custom panels — not just Lovelace
  dashboards. (Panels registered with `embed_iframe: true`, HACS among them,
  are a separate document and stay unthemed; see ARCHITECTURE.md.)
- `card-mod-dialog` and `card-mod-top-app-bar-fixed` for dialogs and the header.
- Install docs now cover `frontend: extra_module_url`, which card-mod requires
  in order to run on anything other than a Lovelace dashboard. Without it the
  theme only ever applies to dashboards.

---

## [0.0.1] — 2026-08-03

First public release.

### Highlights

**72 themes.** Three complete visual systems — Glass, Velvet and Neon — each
rendered across 23 areas of the home, so a dashboard can look like the room it
controls.

**69 backgrounds.** Original artwork, one per area per mode, at 2560×1440. The
composition is deliberately identical across modes: only palette and grade
change, so the Kitchen stays recognisably the Kitchen when you switch aesthetic.

**A background per dashboard *and* per tab.** Assign a theme to a whole
dashboard, or give a single view its own backdrop with one `card_mod` block.

### The three modes

| | Glass | Velvet | Neon |
|---|---|---|---|
| Blur | `blur(16px) saturate(1.45)` | `blur(12px) saturate(1.15)` | `blur(10px) saturate(1.8)` |
| Radius | 30px | 18px | 12px |
| Borders | none | 1px hairline | 1px accent, glowing |
| Character | rich, luminous, soft | muted, cozy, matte | high-chroma, scanlined |

Accents adapt per mode rather than being reused verbatim — Garden's `#32D74B`
becomes `#A6E3A1` in Velvet and `#00FF27` in Neon.

### Added

- Glass card engine: `::before` backdrop-filter layer with a four-part inset
  bevel, blurred sidebar and drawer
- **Specular sheen** — an `::after` rim gradient, so cards read as glass rather
  than frosted plastic
- **`@supports` fallback** — solid card surfaces where `backdrop-filter` is
  unsupported, instead of rendering transparent and unreadable
- **iOS-safe backgrounds** — painted onto a fixed pseudo-element, because
  `background-attachment: fixed` misbehaves on iOS Safari and the companion app
- **Per-view background hook** (`--ultimate-view-background`), with optional
  opacity blending
- Full `--ha-color-primary-05..95` accent ladder, computed per area
- Hover lift, guarded by `prefers-reduced-motion`
- button-card templates: `ultimate_glass`, `ultimate_glass_icon`,
  `ultimate_glass_tile`, `ultimate_flat`, `ultimate_neon`
- Compatibility exclusions for Mushroom, Bubble Card, heading, glance and
  text-only cards, so they don't double-blur
- Copy-paste `card_mod` snippets for every area in every mode
- Build pipeline: `areas.py`, `modes.py`, one Jinja template, plus generators for
  artwork, themes, previews and prompts
- `verify.py` — validates every value in every theme before anything ships
- CI: rebuilds the themes, fails if the committed output is stale, runs the
  validator, and checks the repository against HACS
- Release assets for self-hosting without cloning the repository:
  `ultimate-theme-backgrounds-<version>.zip` (unzip into `/config/www/`) and
  `ultimate-theme-local-<version>.yaml` (the `/local/` build)

### Requirements

- Home Assistant 2024.11 or newer
- [card-mod](https://github.com/thomasloven/lovelace-card-mod) — **required**;
  without it you get the colours but no glass, and no error explaining why
- Mushroom, Bubble Card and button-card are supported but optional

### Known limitations

- **Dark by design.** Every background is dark so white card text stays
  readable. Light mode works and uses lighter card surfaces, but keeps light
  text. A true light mode needs a light background set.
- **Backgrounds come from a CDN by default.** HACS installs the theme YAML and
  nothing else, so `/local/` URLs would 404 on a fresh install. Rebuild with
  `--base local` and copy `www/` if you want everything self-hosted — see
  [INSTALL.md](INSTALL.md).
- **One theme file, deliberately.** HACS manages exactly one theme file per
  repository, so all 72 themes live in `themes/ultimate-theme.yaml` (~1.3 MB).

### Install

See [INSTALL.md](INSTALL.md). Short version: HACS → ⋮ → Custom repositories →
add this repo as type **Theme** → Download → add `frontend: themes:` to
`configuration.yaml` → restart → pick a theme and set the mode to **Dark**.

[0.0.6]: https://github.com/HomeRiz/Home-Assistant-Ultimate-Theme/releases/tag/0.0.6
[0.0.5]: https://github.com/HomeRiz/Home-Assistant-Ultimate-Theme/releases/tag/0.0.5
[0.0.4]: https://github.com/HomeRiz/Home-Assistant-Ultimate-Theme/releases/tag/0.0.4
[0.0.3]: https://github.com/HomeRiz/Home-Assistant-Ultimate-Theme/releases/tag/0.0.3
[0.0.2]: https://github.com/HomeRiz/Home-Assistant-Ultimate-Theme/releases/tag/0.0.2
[0.0.1]: https://github.com/HomeRiz/Home-Assistant-Ultimate-Theme/releases/tag/0.0.1
