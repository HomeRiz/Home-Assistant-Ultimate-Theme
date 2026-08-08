<div align="center">

# Home Assistant Ultimate Theme

**72 themes. 3 aesthetics. 23 areas. A background for every dashboard and every tab.**

[![Latest release](https://img.shields.io/github/v/release/HomeRiz/Home-Assistant-Ultimate-Theme?style=flat-square&label=release)](https://github.com/HomeRiz/Home-Assistant-Ultimate-Theme/releases/latest)
[![HACS Custom](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://hacs.xyz)
[![Validate](https://img.shields.io/github/actions/workflow/status/HomeRiz/Home-Assistant-Ultimate-Theme/validate.yml?branch=main&style=flat-square&label=validate)](https://github.com/HomeRiz/Home-Assistant-Ultimate-Theme/actions/workflows/validate.yml)
[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/HomeRiz/Home-Assistant-Ultimate-Theme/blob/main/LICENSE)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2024.11%2B-41BDF5.svg?style=flat-square)](https://www.home-assistant.io)

[![Ultimate Glass, AI dashboard](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/glass/ai.webp)](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/glass/ai.webp)

</div>

---

Three complete visual systems — **Glass**, **Velvet** and **Neon** — each rendered
across 23 areas of the home. Every area gets its own artwork, its own accent
colour and its own theme entry, so a dashboard can look like the room it controls.

```
3 modes  ×  (1 base + 23 areas)  =  72 themes
3 modes  ×  23 areas             =  69 backgrounds
```

---

## Install

### Step 1 — install card-mod

**This theme does not work without it.** card-mod is what draws the glass and the
backgrounds; without it you get the colours and nothing else, and no error
explaining why.

[![Open card-mod in HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=thomasloven&repository=lovelace-card-mod&category=plugin)

Or in HACS, search for **card-mod** and download it.

### Step 2 — install this theme

[![Open this theme in HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=HomeRiz&repository=Home-Assistant-Ultimate-Theme&category=theme)

The button adds it as a custom repository. If you would rather do it by hand:
**HACS → ⋮ (top right) → Custom repositories**, paste
`https://github.com/HomeRiz/Home-Assistant-Ultimate-Theme`, type **Theme**, **Add**.

Then search HACS for **Home Assistant Ultimate Theme** and **Download**.

### Step 3 — find your card-mod URL

Go to **Settings → Dashboards → ⋮ (top right) → Resources**.

Find the row for card-mod. It has this shape, ending in a 12-digit number:

```
/hacsfiles/lovelace-card-mod/card-mod.js?hacstag=############
```

**Copy the real line from your own screen, number included.** Do not copy the
one above — `hacstag` is the version stamp HACS puts on the file, so it differs
per instance and changes whenever card-mod updates. A number taken from
somewhere else gives you a 404 that only shows up on Settings, while dashboards
keep working — which makes it look like a theme bug rather than a wrong URL.

### Step 4 — add one line to `configuration.yaml`

You most likely already have this block:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

Add `extra_module_url` to it, with the line you just copied:

```yaml
frontend:
  themes: !include_dir_merge_named themes
  extra_module_url:
    - /hacsfiles/lovelace-card-mod/card-mod.js?hacstag=XXXXXXXXXXXX
```

Replace `XXXXXXXXXXXX` with your own number from Step 3.

> **Why this line is needed:** dashboard resources are only loaded on Lovelace
> dashboards. Without `extra_module_url`, card-mod never runs on Settings,
> Developer Tools or HACS — those pages get the colours but no background and no
> glass. Keep the Resources entry as it is; you need both.

### Step 5 — restart and pick a theme

**Restart Home Assistant.** A theme reload is not enough — `extra_module_url` is
only read at startup.

Then: your username, bottom left → **Theme** → pick one. Start with
`Ultimate Glass - Home`, and set the dropdown beside it to **Dark**.

> **Give it a few seconds on the first load.** The module is fetched separately
> from the rest of the frontend, so Settings can render plain and then pick up the
> background a moment later. That is not a broken install.

> **Why dark?** All backgrounds are dark so white card text stays readable. Light
> mode works and uses lighter card surfaces, but keeps light text.

**Something not working?** → [Troubleshooting](INSTALL.md#troubleshooting)

---

## A theme per tab

Every area exists as a full theme, so a single dashboard can change backdrop as
you move between tabs. In the dashboard's **Raw configuration editor**:

```yaml
theme: Ultimate Glass - Home        # the whole dashboard

views:
  - title: Kitchen
    path: kitchen
    theme: Ultimate Glass - Kitchen  # just this tab

  - title: Energy
    path: energy
    theme: Ultimate Neon - Electrical Room
```

Each tab gets that theme's colours *and* its backdrop. Mixing modes across tabs
works — Glass on one, Neon on the next.

[Full guide, including image-only overrides →](docs/PER-VIEW-BACKGROUNDS.md)

---

## Gallery

### Ultimate Glass

Heavy blur, 30px radii, no borders, bright specular rim.

[![All 23 areas in Ultimate Glass](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/glass.webp)](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/glass.webp)

<sub>Click to view full size.</sub>

### Ultimate Velvet

Softer blur, 18px radii, hairline borders, muted pastel accents.

[![All 23 areas in Ultimate Velvet](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/velvet.webp)](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/velvet.webp)

<sub>Click to view full size.</sub>

### Ultimate Neon

Near-black, 12px radii, accent borders with outer glow, scanlined backdrops.

[![All 23 areas in Ultimate Neon](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/neon.webp)](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/neon.webp)

<sub>Click to view full size.</sub>

<details>
<summary><b>The same area across all three modes</b></summary>

| Glass | Velvet | Neon |
|---|---|---|
| [![](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/glass/kitchen.webp)](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/glass/kitchen.webp) | [![](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/velvet/kitchen.webp)](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/velvet/kitchen.webp) | [![](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/neon/kitchen.webp)](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/neon/kitchen.webp) |
| [![](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/glass/security.webp)](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/glass/security.webp) | [![](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/velvet/security.webp)](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/velvet/security.webp) | [![](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/neon/security.webp)](https://raw.githubusercontent.com/HomeRiz/Home-Assistant-Ultimate-Theme/main/docs/previews/neon/security.webp) |

The composition is deliberately identical across modes — only palette and grade
change, so a room stays recognisable when you switch aesthetic.

</details>

---

## The three modes

| | Glass | Velvet | Neon |
|---|---|---|---|
| Blur | `blur(16px) saturate(1.45)` | `blur(12px) saturate(1.15)` | `blur(10px) saturate(1.8)` |
| Radius | 30px | 18px | 12px |
| Borders | none | 1px hairline | 1px accent, glowing |
| Character | rich, luminous, soft | muted, cozy, matte | high-chroma, scanlined |

## The 23 areas

| Rooms | Outdoors | Systems |
|---|---|---|
| `home` | `outside` | `ai` |
| `living-room` | `front-yard` | `electrical-room` |
| `kitchen` | `back-yard` | `technic-room` |
| `bedroom` | `garden` | `energy` |
| `master-bedroom` | `garage` | `security` |
| `guest` | | `climate` |
| `bathroom` | | `media` |
| `office` | | `network` |
| `hallway` | | `settings` |

Adding one is a single line in `build/areas.py`.

---

## Documentation

| | |
|---|---|
| [Install guide](INSTALL.md) | Every route, in detail, plus troubleshooting |
| [Per-tab backgrounds](docs/PER-VIEW-BACKGROUNDS.md) | Profile, dashboard and view level |
| [Customising](docs/CUSTOMISING.md) | Feature list, rebuilding, your own artwork |
| [Architecture](docs/ARCHITECTURE.md) | How the glass engine and build pipeline work |
| [Image prompts](docs/IMAGE-PROMPTS.md) | Every prompt behind the artwork |
| [Changelog](CHANGELOG.md) | What changed, and what turned out to be wrong |

## Contributing

Issues and pull requests welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).
Screenshots are the review for anything visual.

## Licence

[MIT](LICENSE). Portions of the CSS derive from other MIT-licensed themes; those
notices are in [NOTICE.md](NOTICE.md).
