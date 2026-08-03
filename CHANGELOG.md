# Changelog

All notable changes to this project are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Fixed

- `card-mod-drawer-yaml` was not a real card-mod type, so that block had never
  applied. card-mod ignores unknown keys silently, which is why it went
  unnoticed. Removed.
- `verify.py` now validates every `card-mod-*` key against card-mod's documented
  type list and fails on anything else.

### Added

- `card-mod-config` and `card-mod-panel-custom`, so the backdrop and glass reach
  Settings, Developer Tools, History and custom panels such as HACS — not just
  Lovelace dashboards.
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

[0.0.1]: https://github.com/HomeRiz/Home-Assistant-Ultimate-Theme/releases/tag/v0.0.1
