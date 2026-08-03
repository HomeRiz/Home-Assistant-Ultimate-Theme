# Per-dashboard and per-tab backgrounds

There are three levels at which you can set a background. They stack — the most
specific one wins.

| Level | What it sets | How |
|---|---|---|
| **Profile** | Your default everywhere | Profile → Theme |
| **Dashboard** | One whole dashboard | Assign an area theme to that dashboard |
| **View (tab)** | A single tab | `theme:` on the view, or `card_mod` for the image alone |

---

## 1. Profile level — pick your baseline

Click your username (bottom left) → **Theme** → pick one:

- `Ultimate Glass` / `Ultimate Velvet` / `Ultimate Neon` — the base themes,
  no area background, just the mode's own gradient.
- Or jump straight to an area theme like `Ultimate Glass - Home`.

Set the mode dropdown next to it to **Dark**. All backgrounds are dark by
design so that white card text stays legible; light mode uses lighter card
surfaces but keeps light text.

---

## 2. Dashboard level — a theme per dashboard

Every area exists as a full theme, so you can hand a whole dashboard its own
identity.

**Storage mode** (dashboards you edit in the UI):

1. Open the dashboard → pencil icon → three dots → **Raw configuration editor**
2. Add a top-level `theme:` key:

```yaml
theme: Ultimate Glass - Kitchen
views:
  - title: Overview
    ...
```

**YAML mode** (`lovelace:` in `configuration.yaml`): same key, same place.

---

## 3. View level — a background per tab

This is the one people usually want, and there are two ways to do it.

### The short way — `theme:` on the view

Home Assistant lets a view carry its own theme, and as of 0.0.3 that changes
the backdrop as well as the colours:

```yaml
theme: Ultimate Glass - Home          # dashboard default

views:
  - title: Kitchen
    path: kitchen
    icon: mdi:silverware-fork-knife
    theme: Ultimate Glass - Kitchen

  - title: Energy
    path: energy
    icon: mdi:lightning-bolt
    theme: Ultimate Neon - Electrical Room
```

Modes can be mixed freely across tabs of one dashboard.

> **Before 0.0.3 this only changed the colours.** Home Assistant applies a
> view's theme to `hui-view-container`, which sits below `hui-root` — and the
> backdrop was painted on the root, so it always resolved to the profile theme.
> If your tabs recolour but keep one image, you are on an older build: update
> and reload themes.
>
> The sidebar and header stay on the profile theme by design. They are outside
> the view, and repainting them on every tab switch reads as a flicker rather
> than a feature.

### The precise way — image only, colours untouched

Use this when you want a different backdrop but the *same* palette and card
styling across tabs. It is what `--ultimate-view-background` exists for.

Add a `card_mod` block to the **view** (not to a card inside it):

```yaml
views:
  - title: Kitchen
    path: kitchen
    icon: mdi:silverware-fork-knife
    card_mod:
      style: |
        :host {
          --ultimate-view-background: url('/local/ultimate-theme/backgrounds/glass/kitchen.webp');
        }

  - title: Garden
    path: garden
    icon: mdi:flower
    card_mod:
      style: |
        :host {
          --ultimate-view-background: url('/local/ultimate-theme/backgrounds/glass/garden.webp');
        }
```

Both tabs now have their own backdrop while sharing one theme, one sidebar and
one set of card styling.

> **Storage-mode dashboards:** you can absolutely do this. The UI editor has no
> field for `card_mod`, but the **Raw configuration editor** (pencil → ⋮ → Raw
> configuration editor) gives you the full YAML for the dashboard. Edit there
> and it persists normally.

`dashboards/per-view-backgrounds.yaml` has a ready-made commented block for
every area × every mode — copy the ones you need.

### Fading the view background

```yaml
card_mod:
  style: |
    :host {
      --ultimate-view-background: url('/local/ultimate-theme/backgrounds/neon/ai.webp');
      --ultimate-view-background-opacity: 0.55;
    }
```

At `1` (the default) the view background completely replaces the theme's. Lower
values let the theme background show through, which is a nice way to keep a
family resemblance across tabs.

---

## Why not `background-attachment: fixed`?

The source themes all use:

```yaml
background-image: "center / cover no-repeat fixed url(...)"
```

`fixed` is ignored or renders janky on iOS Safari and inside the Home Assistant
companion app — the background jumps as you scroll, or scales wrong on rubber-band
overscroll. This theme keeps that declaration for compatibility but *also*
paints the real backdrop onto a `position: fixed` pseudo-element in
`card-mod-root`:

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

Same visual result, no scroll artefacts, works identically on desktop, iOS and
Android.

---

## Native HA view backgrounds (2024.11+)

Recent Home Assistant versions let you set a background image per view from the
UI: edit view → **Background**. That works too and needs no `card_mod`.

Use it if you prefer clicking to YAML. The `card_mod` route is still worth
knowing because it also gives you the opacity control and works on older HA
versions.

---

## Troubleshooting

**Background doesn't change**
Hard refresh (`Ctrl/Cmd + Shift + R`). Home Assistant caches themes aggressively.
Then Developer Tools → **Reload themes** (or call `frontend.reload_themes`).

**Cards are fully transparent and unreadable**
Your browser doesn't support `backdrop-filter`. The theme has an `@supports`
fallback that swaps in a solid card colour — if you're still seeing this, you're
likely on a very old Android WebView. Update the companion app.

**Images 404**
Check the path. Files must be at
`/config/www/ultimate-theme/backgrounds/<mode>/<area>.webp`, which Home
Assistant serves at `/local/ultimate-theme/backgrounds/<mode>/<area>.webp`.
`/config/www` maps to `/local`, not `/www`.
