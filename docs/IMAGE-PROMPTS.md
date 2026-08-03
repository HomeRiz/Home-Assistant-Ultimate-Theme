# Image prompts

Every background is `STYLE + SUBJECT + CONSTRAINTS`. The **subject is identical across all three modes** — that is deliberate. It means the Kitchen still reads as the Kitchen whether you are in Glass, Velvet or Neon.

You do not have to do all 69. Anything you don't supply keeps its procedurally generated background, so you can replace them a few at a time.

## How to use

1. Generate an image.
2. Save it as `drop-in/<mode>/<area-key>.png` (e.g. `drop-in/glass/kitchen.png`). The filename **must** match the area key exactly — that is how the importer knows where it goes.
3. Run:

```bash
python3 build/import_backgrounds.py
python3 build/generate_themes.py
```

The importer centre-crops to 2560×1440, darkens slightly so glass cards stay legible, converts to WebP, and refreshes the header tints. Use `--darken 0` if your images are already dark enough.

## Constraints (append to every prompt)

```
16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**Negative prompt**, if your tool supports one:

```
text, letters, words, watermark, logo, signature, people, faces, hands, busy detail in centre, high-key bright, washed out, blown highlights, harsh edges, clutter, UI mockup, screenshot, frame, border
```

## Style blocks (prepend, one per mode)

### `glass`

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light.
```

### `velvet`

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy.
```

### `neon`

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade.
```

## Subjects

| Area key | Dashboard | Subject |
|---|---|---|
| `home` | Home | a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway |
| `living-room` | Living Room | soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow |
| `kitchen` | Kitchen | warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround |
| `bedroom` | Bedroom | a deep indigo and violet nebula haze, very still and quiet, midnight calm |
| `master-bedroom` | Master Bedroom | plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious |
| `guest` | Guest | soft teal and sage mist drifting slowly, calm, minimal, welcoming |
| `bathroom` | Bathroom | aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean |
| `office` | Office | cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake |
| `ai` | AI | electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence |
| `outside` | Outside | a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air |
| `hallway` | Hallway | warm dim light receding down a long perspective gradient, muted slate and amber, transitional |
| `garage` | Garage | brushed steel grey lit by a single orange sodium lamp, industrial, oily dark |
| `front-yard` | Front Yard | morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges |
| `back-yard` | Back Yard | late sunset green and warm orange across grass, dusk settling, relaxed |
| `electrical-room` | Electrical Room | amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light |
| `technic-room` | Technic Room | cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark |
| `garden` | Garden | verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges |
| `energy` | Energy | flowing green and yellow light currents streaming like energy in motion, kinetic, dark background |
| `security` | Security | deep crimson and dark red light sweeping across shadow, watchful and tense, alert |
| `climate` | Climate | a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance |
| `media` | Media | magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic |
| `network` | Network | blue and cyan data streams flowing through dark space, luminous nodes and connecting lines |
| `settings` | Settings | restrained graphite and silver light, neutral, minimal, quietly technical |

## Ready-to-paste full prompts

<details>
<summary><b>glass</b> — all 23 prompts</summary>

**`glass/home.png`** — Home

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/living-room.png`** — Living Room

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/kitchen.png`** — Kitchen

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/bedroom.png`** — Bedroom

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. a deep indigo and violet nebula haze, very still and quiet, midnight calm. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/master-bedroom.png`** — Master Bedroom

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/guest.png`** — Guest

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. soft teal and sage mist drifting slowly, calm, minimal, welcoming. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/bathroom.png`** — Bathroom

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/office.png`** — Office

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/ai.png`** — AI

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/outside.png`** — Outside

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/hallway.png`** — Hallway

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. warm dim light receding down a long perspective gradient, muted slate and amber, transitional. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/garage.png`** — Garage

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. brushed steel grey lit by a single orange sodium lamp, industrial, oily dark. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/front-yard.png`** — Front Yard

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/back-yard.png`** — Back Yard

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. late sunset green and warm orange across grass, dusk settling, relaxed. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/electrical-room.png`** — Electrical Room

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/technic-room.png`** — Technic Room

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/garden.png`** — Garden

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/energy.png`** — Energy

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. flowing green and yellow light currents streaming like energy in motion, kinetic, dark background. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/security.png`** — Security

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. deep crimson and dark red light sweeping across shadow, watchful and tense, alert. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/climate.png`** — Climate

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/media.png`** — Media

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/network.png`** — Network

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. blue and cyan data streams flowing through dark space, luminous nodes and connecting lines. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/settings.png`** — Settings

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. restrained graphite and silver light, neutral, minimal, quietly technical. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>velvet</b> — all 23 prompts</summary>

**`velvet/home.png`** — Home

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/living-room.png`** — Living Room

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/kitchen.png`** — Kitchen

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/bedroom.png`** — Bedroom

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. a deep indigo and violet nebula haze, very still and quiet, midnight calm. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/master-bedroom.png`** — Master Bedroom

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/guest.png`** — Guest

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. soft teal and sage mist drifting slowly, calm, minimal, welcoming. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/bathroom.png`** — Bathroom

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/office.png`** — Office

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/ai.png`** — AI

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/outside.png`** — Outside

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/hallway.png`** — Hallway

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. warm dim light receding down a long perspective gradient, muted slate and amber, transitional. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/garage.png`** — Garage

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. brushed steel grey lit by a single orange sodium lamp, industrial, oily dark. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/front-yard.png`** — Front Yard

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/back-yard.png`** — Back Yard

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. late sunset green and warm orange across grass, dusk settling, relaxed. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/electrical-room.png`** — Electrical Room

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/technic-room.png`** — Technic Room

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/garden.png`** — Garden

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/energy.png`** — Energy

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. flowing green and yellow light currents streaming like energy in motion, kinetic, dark background. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/security.png`** — Security

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. deep crimson and dark red light sweeping across shadow, watchful and tense, alert. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/climate.png`** — Climate

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/media.png`** — Media

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/network.png`** — Network

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. blue and cyan data streams flowing through dark space, luminous nodes and connecting lines. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/settings.png`** — Settings

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. restrained graphite and silver light, neutral, minimal, quietly technical. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>neon</b> — all 23 prompts</summary>

**`neon/home.png`** — Home

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/living-room.png`** — Living Room

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/kitchen.png`** — Kitchen

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/bedroom.png`** — Bedroom

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. a deep indigo and violet nebula haze, very still and quiet, midnight calm. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/master-bedroom.png`** — Master Bedroom

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/guest.png`** — Guest

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. soft teal and sage mist drifting slowly, calm, minimal, welcoming. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/bathroom.png`** — Bathroom

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/office.png`** — Office

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/ai.png`** — AI

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/outside.png`** — Outside

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/hallway.png`** — Hallway

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. warm dim light receding down a long perspective gradient, muted slate and amber, transitional. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/garage.png`** — Garage

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. brushed steel grey lit by a single orange sodium lamp, industrial, oily dark. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/front-yard.png`** — Front Yard

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/back-yard.png`** — Back Yard

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. late sunset green and warm orange across grass, dusk settling, relaxed. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/electrical-room.png`** — Electrical Room

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/technic-room.png`** — Technic Room

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/garden.png`** — Garden

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/energy.png`** — Energy

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. flowing green and yellow light currents streaming like energy in motion, kinetic, dark background. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/security.png`** — Security

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. deep crimson and dark red light sweeping across shadow, watchful and tense, alert. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/climate.png`** — Climate

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/media.png`** — Media

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/network.png`** — Network

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. blue and cyan data streams flowing through dark space, luminous nodes and connecting lines. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/settings.png`** — Settings

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. restrained graphite and silver light, neutral, minimal, quietly technical. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>
