# Install

Two routes. Pick one.

| | [HACS](#route-a--hacs) | [Manual](#route-b--manual) |
|---|---|---|
| Effort | 4 steps, no file copying | copy two folders |
| Updates | one click | manual |
| Backgrounds | served from CDN | served from your own instance |
| Works offline | no | yes |
| Best for | almost everyone | air-gapped setups, or if you're modifying the theme |

Modifying the theme? Read [Customising and keeping updates](#customising-and-keeping-updates)
before you start — the wrong route means HACS silently overwrites your work.

---

## Step 0 — install card-mod (both routes)

**[card-mod](https://github.com/thomasloven/lovelace-card-mod) is required.** It
is the mechanism that injects the glass CSS. Without it you get the colours but
no blur, no sheen, no rounded sidebar — the theme will look flat and wrong, with
no error to tell you why.

HACS → **Frontend** → search **card-mod** → **Download**.

### Then register it as a frontend module — this part is not optional

Dashboard resources are loaded **only on Lovelace dashboards**. On Settings,
HACS, Developer Tools and every add-on panel, card-mod is never loaded at all —
so those pages get the theme's colours but no backdrop and no glass.

card-mod's own documentation is explicit about this: installing it as a frontend
module *"is required if you are using card-mod to style panels of Home Assistant
which are not Lovelace dashboards"*.

Find your exact resource URL first — Settings → Dashboards → ⋮ → **Resources**.
It looks like the line below, but **the number is unique to your install** —
copy yours, don't retype this one:

```
/hacsfiles/lovelace-card-mod/card-mod.js?hacstag=XXXXXXXXXXXX
```

Add it to `configuration.yaml`, alongside the themes line:

```yaml
frontend:
  themes: !include_dir_merge_named themes
  extra_module_url:
    - /hacsfiles/lovelace-card-mod/card-mod.js?hacstag=XXXXXXXXXXXX
```

**Restart Home Assistant.** A theme reload is not enough — `extra_module_url` is
only read at startup.

> Keep the HACS resource entry as it is. You need both: the resource for
> dashboards and CAST devices, the module for everything else. And when HACS
> updates card-mod, the `hacstag` changes — update `extra_module_url` to match,
> or card-mod loads twice and warns about duplicate patching.

Verify it worked: open **Settings**. You should see the theme's background behind
the page. If the page is flat dark, the module is not loading.

Mushroom, Bubble Card and button-card are supported but not required.

---

## Route A — HACS

### 1. Add the custom repository

1. **HACS** → **⋮** (top right) → **Custom repositories**
2. Repository: `https://github.com/HomeRiz/Home-Assistant-Ultimate-Theme`
3. Type: **Theme**
4. **Add**

### 2. Download

Search HACS for **Home Assistant Ultimate Theme** → **Download**.

HACS creates its own subfolder and puts the file inside it:

```
/config/themes/ultimate-theme/ultimate-theme.yaml
```

That one file contains all 72 themes. **Leave it where HACS put it.** The
`!include_dir_merge_named` include recurses into subdirectories, so Home
Assistant finds it there. Moving it to `/config/themes/` directly will work
until the next HACS update recreates the subfolder — and then you have two
copies of all 72 theme names fighting each other.

> HACS installs **only** the theme YAML — it never touches `/config/www`. That is
> why the default build loads backgrounds from a CDN, so a HACS install needs no
> further copying. If you'd rather self-host the images, use Route B.

### 3. Enable themes

In `configuration.yaml`:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

Already have a `frontend:` block? Add the `themes:` line to it. A second
`frontend:` key is a YAML error.

### 4. Restart and pick a theme

**Settings → System → ⋮ → Restart Home Assistant.**

A full restart is needed the first time — `!include_dir_merge_named` is only
evaluated at startup. Afterwards, Developer Tools → **Reload themes** is enough.

Then click your username (bottom left) → **Theme**. Start with:

- `Ultimate Glass` — base, no area background
- `Ultimate Glass - Home` — with the Home backdrop

Set the mode dropdown beside it to **Dark**.

Hard refresh (`Ctrl/Cmd + Shift + R`) if nothing changes.

---

## Route B — manual

Use this if you want the backgrounds served from your own instance, need it to
work without internet, or are modifying the theme locally.

> **Shortcut: use the release assets.** Every release attaches two files, so you
> don't need to clone anything or install Python:
>
> 1. Download **`ultimate-theme-backgrounds-<version>.zip`** (~8 MB) and unzip it
>    into `/config/www/`. You should end up with
>    `/config/www/ultimate-theme/backgrounds/…`.
> 2. Download **`ultimate-theme-local-<version>.yaml`**, rename it to
>    `ultimate-theme.yaml`, and put it in `/config/themes/` — replacing any copy
>    HACS installed (see the note below).
> 3. Skip to step 3, enable themes and restart.
>
> The steps below are the from-source route, for when you're changing the theme
> rather than just self-hosting it.

### 1. Build with local URLs

```bash
git clone https://github.com/HomeRiz/Home-Assistant-Ultimate-Theme.git
cd Home-Assistant-Ultimate-Theme
pip install numpy Pillow jinja2 pyyaml

python3 build/generate_themes.py --base local
```

This rewrites every background URL to `/local/ultimate-theme/backgrounds/...`.

### 2. Copy two folders

```
themes/  →  /config/themes/
www/     →  /config/www/
```

Afterwards:

```
/config/themes/ultimate-theme.yaml

/config/www/ultimate-theme/backgrounds/glass/*.webp
/config/www/ultimate-theme/backgrounds/velvet/*.webp
/config/www/ultimate-theme/backgrounds/neon/*.webp
```

> **Already installed via HACS? Pick one, not both.**
>
> HACS keeps its copy at `/config/themes/ultimate-theme/ultimate-theme.yaml`.
> Adding a second copy at `/config/themes/ultimate-theme.yaml` means Home
> Assistant loads all 72 theme names **twice** — the include recurses, so it
> merges both files. Which one wins is not something you want to rely on, and
> the symptom is confusing: backgrounds that come from the CDN when you expected
> local ones.
>
> Either remove the theme from HACS first (HACS → the theme → ⋮ → **Remove**) and
> use only your manual copy, or overwrite HACS's file in place at
> `/config/themes/ultimate-theme/ultimate-theme.yaml` and accept that the next
> HACS update reverts it to the CDN build.
>
> To keep local URLs *and* HACS updates, use the fork route below.

Whichever transfer method you already use:

- **Samba share** — drag both folders into `\\homeassistant\config\`
- **File editor** or **Studio Code Server** add-on — upload directly
- **SSH / Terminal add-on**

  ```bash
  scp -r themes/*  root@homeassistant:/config/themes/
  scp -r www/*     root@homeassistant:/config/www/
  ```

> **The `/config/www` → `/local` mapping matters.** Home Assistant serves
> `/config/www/` at the URL `/local/`. So
> `/config/www/ultimate-theme/backgrounds/glass/kitchen.webp` is fetched as
> `/local/ultimate-theme/backgrounds/glass/kitchen.webp` — exactly what the theme
> references. **Don't rename `ultimate-theme`** or every background 404s.

Backgrounds total about 8 MB (glass 2.6, velvet 2.2, neon 3.3).

### 3–4. Same as Route A

Enable themes in `configuration.yaml`, restart, pick a theme.

---

## Why dark mode

Every background is dark by design, so white card text stays readable over it.
Light mode works and uses lighter card surfaces, but keeps light text.

A true light mode needs a light background set — see
[Using your own artwork](README.md#using-your-own-artwork).

---

## Per-dashboard and per-tab backgrounds

The part you probably came for. Quick version — in your dashboard's **Raw
configuration editor**:

```yaml
theme: Ultimate Glass - Home        # whole-dashboard default

views:
  - title: Kitchen
    path: kitchen
    icon: mdi:silverware-fork-knife
    card_mod:
      style: |
        :host {
          --ultimate-view-background: url('https://cdn.jsdelivr.net/gh/HomeRiz/Home-Assistant-Ultimate-Theme@main/www/ultimate-theme/backgrounds/glass/kitchen.webp');
        }
```

`dashboards/per-view-backgrounds.yaml` has a ready-made block for every area in
every mode. Full detail in
**[docs/PER-VIEW-BACKGROUNDS.md](docs/PER-VIEW-BACKGROUNDS.md)**.

---

## Optional — button-card templates

`custom:button-card` draws its own surface, so by default it ignores the glass
engine and sits on top as a flat rectangle. To fix that, copy
`dashboards/button-card-templates.yaml` to `/config/` and add this as the **first
line** of your dashboard's raw config:

```yaml
button_card_templates: !include button-card-templates.yaml
```

Then:

```yaml
type: custom:button-card
template: ultimate_glass_tile
entity: light.kitchen
```

Available: `ultimate_glass`, `ultimate_glass_icon`, `ultimate_glass_tile`,
`ultimate_flat`, `ultimate_neon`.

---

## Customising and keeping updates

If you edit the theme, **how you installed it decides whether your work
survives**.

| Approach | Result |
|---|---|
| Edit files in `/config/themes/` after a HACS install | Overwritten on the next HACS update |
| Copy modified files over Samba/SSH after a HACS install | Same — overwritten |
| **Fork this repo, push changes, add your fork as the custom repository** | Your edits are what HACS installs, and you still get one-click updates |
| Manual install, never add to HACS | Fully under your control, no automatic updates |

**The fork route, in short:**

1. Fork this repository on GitHub
2. Clone your fork, edit `build/`, run `python3 build/generate_themes.py` and
   `python3 build/verify.py`
3. If you changed background URLs, update `REPO` and `CDN_REF` in
   `build/generate_themes.py` to point at *your* fork
4. Commit and push
5. In HACS, remove this repository and add your fork as a **Theme** custom
   repository instead

Never edit `themes/ultimate-theme.yaml` by hand — it is generated, and the next
build overwrites it. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Troubleshooting

**Themes don't appear in the picker.**
The `frontend: themes:` include is missing, or you haven't restarted since
installing. Check Settings → System → **Logs** for YAML errors.

**Config check fails with `string value is None`.**

```
Invalid config for 'frontend' at configuration.yaml
  string value is None for dictionary value
  'frontend->themes->modes->dark->primary-background-color', got None
```

A theme value parsed as `null`, which makes Home Assistant reject the entire
themes file — so *no* theme loads, not just the affected one. The usual cause is
an unquoted colour: in YAML a `#` after `key: ` starts a comment, so
`primary-background-color: #1e1e2e` becomes null.

This was a real bug in versions before the fix; update to the latest release.
If you hit it in your own build, quote the value and re-run
`python3 build/verify.py`, which now fails on any null or empty value.

**Everything is flat — no blur, no rounded sidebar.**
card-mod isn't loading. Check Settings → Dashboards → Resources for
`/hacsfiles/lovelace-card-mod/card-mod.js`. If it is listed, reload the browser —
resources are only fetched when the frontend boots, so a tab you had open before
installing card-mod will not have it.

**The theme works on dashboards but Settings is plain.**
You skipped `extra_module_url` in Step 0. Dashboard resources are not loaded on
non-Lovelace panels, so card-mod simply is not present there. Add the module,
restart, and the backdrop will follow you across the whole UI.

**Add-on panels (File editor, Terminal, Studio Code Server) and HACS have no
theme.**
Expected, and not fixable by any theme. These are shown in an iframe — a
separate document with its own CSS that neither Home Assistant nor card-mod can
reach. HACS registers itself with `embed_iframe: true`, so it falls in this
group even though it is a custom panel rather than an add-on. You can confirm
what a panel is by opening the browser console on it and running
`document.querySelector('home-assistant').hass.panels`.

> **If a HACS dialog opens with its contents spilling outside the box** and the
> version dropdown floating loose, you are on 0.0.2 or earlier. `backdrop-filter`
> on the sidebar corrupts the layout of an iframe rendered next to it — a
> compositing quirk in Chrome that this theme was triggering. Fixed in 0.0.3,
> which drops the sidebar blur while an iframe panel is open. As a stopgap on an
> older build, switch to a non-Ultimate theme while you use HACS.

**Cards are fully transparent and unreadable.**
`backdrop-filter` unsupported. There is an `@supports` fallback for exactly this;
if you still see it, you're on a very old Android WebView — update the companion
app.

**Backgrounds don't load.**
On a HACS install they come from jsDelivr — if your network blocks it, or you're
offline, switch to Route B. On a manual install it's a path problem: it's
`/config/www/...` on disk but `/local/...` in the URL, and the `ultimate-theme`
folder can't be renamed.

**Only some themes appear.**
The repository's `themes/` folder must contain exactly one `.yaml` file. HACS
installs only the first one it finds, so a stray second file in the *repo* means
two thirds of the project goes missing.

**Backgrounds load from the CDN when I built with `--base local`.**
You almost certainly have two copies of the theme on the instance: HACS's at
`/config/themes/ultimate-theme/ultimate-theme.yaml` and yours at
`/config/themes/ultimate-theme.yaml`. The include recurses, so both are loaded
and the same 72 theme names are defined twice. Delete whichever one you did not
intend to keep, then Developer Tools → **Reload themes**.

To check which file a background actually came from, open the browser's Network
tab and look at the request for the `.webp` — `cdn.jsdelivr.net` means the CDN
build is winning, `/local/…` means yours is.

**Changed a theme file, nothing happened.**
Developer Tools → **Reload themes**, then hard refresh (`Ctrl/Cmd + Shift + R`).

**A custom card looks wrong — doubled blur or a visible seam.**
It draws its own surface. Add its element name to the exclusion list in
`build/template.jinja2` (search for `EXCLUSIONS`) and regenerate.

**Text is hard to read over a bright patch of artwork.**
Raise the alpha values in `background_scrim` for that mode in `build/modes.py`,
then regenerate.
