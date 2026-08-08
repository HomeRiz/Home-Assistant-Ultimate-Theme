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

## Palette arbitration

The 23 subjects are shared by every style, and several name a colour outright. This clause sits between the subject and the constraints so the style's palette wins while the composition carries over — which is what keeps a room recognisable across aesthetics.

```
Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly.
```

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

### `cyberprep`

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage.
```

### `cyberpunk`

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain.
```

### `solarpunk`

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in.
```

### `art-deco`

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field.
```

### `dark-academia`

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted.
```

### `cottagecore`

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light.
```

### `synthwave`

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field.
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
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/living-room.png`** — Living Room

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/kitchen.png`** — Kitchen

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/bedroom.png`** — Bedroom

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. a deep indigo and violet nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/master-bedroom.png`** — Master Bedroom

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/guest.png`** — Guest

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. soft teal and sage mist drifting slowly, calm, minimal, welcoming. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/bathroom.png`** — Bathroom

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/office.png`** — Office

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/ai.png`** — AI

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/outside.png`** — Outside

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/hallway.png`** — Hallway

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. warm dim light receding down a long perspective gradient, muted slate and amber, transitional. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/garage.png`** — Garage

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. brushed steel grey lit by a single orange sodium lamp, industrial, oily dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/front-yard.png`** — Front Yard

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/back-yard.png`** — Back Yard

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. late sunset green and warm orange across grass, dusk settling, relaxed. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/electrical-room.png`** — Electrical Room

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/technic-room.png`** — Technic Room

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/garden.png`** — Garden

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/energy.png`** — Energy

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. flowing green and yellow light currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/security.png`** — Security

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. deep crimson and dark red light sweeping across shadow, watchful and tense, alert. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/climate.png`** — Climate

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/media.png`** — Media

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/network.png`** — Network

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. blue and cyan data streams flowing through dark space, luminous nodes and connecting lines. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/settings.png`** — Settings

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>velvet</b> — all 23 prompts</summary>

**`velvet/home.png`** — Home

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/living-room.png`** — Living Room

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/kitchen.png`** — Kitchen

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/bedroom.png`** — Bedroom

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. a deep indigo and violet nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/master-bedroom.png`** — Master Bedroom

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/guest.png`** — Guest

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. soft teal and sage mist drifting slowly, calm, minimal, welcoming. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/bathroom.png`** — Bathroom

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/office.png`** — Office

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/ai.png`** — AI

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/outside.png`** — Outside

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/hallway.png`** — Hallway

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. warm dim light receding down a long perspective gradient, muted slate and amber, transitional. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/garage.png`** — Garage

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. brushed steel grey lit by a single orange sodium lamp, industrial, oily dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/front-yard.png`** — Front Yard

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/back-yard.png`** — Back Yard

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. late sunset green and warm orange across grass, dusk settling, relaxed. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/electrical-room.png`** — Electrical Room

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/technic-room.png`** — Technic Room

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/garden.png`** — Garden

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/energy.png`** — Energy

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. flowing green and yellow light currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/security.png`** — Security

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. deep crimson and dark red light sweeping across shadow, watchful and tense, alert. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/climate.png`** — Climate

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/media.png`** — Media

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/network.png`** — Network

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. blue and cyan data streams flowing through dark space, luminous nodes and connecting lines. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/settings.png`** — Settings

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>neon</b> — all 23 prompts</summary>

**`neon/home.png`** — Home

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/living-room.png`** — Living Room

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/kitchen.png`** — Kitchen

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/bedroom.png`** — Bedroom

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. a deep indigo and violet nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/master-bedroom.png`** — Master Bedroom

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/guest.png`** — Guest

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. soft teal and sage mist drifting slowly, calm, minimal, welcoming. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/bathroom.png`** — Bathroom

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/office.png`** — Office

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/ai.png`** — AI

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/outside.png`** — Outside

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/hallway.png`** — Hallway

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. warm dim light receding down a long perspective gradient, muted slate and amber, transitional. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/garage.png`** — Garage

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. brushed steel grey lit by a single orange sodium lamp, industrial, oily dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/front-yard.png`** — Front Yard

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/back-yard.png`** — Back Yard

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. late sunset green and warm orange across grass, dusk settling, relaxed. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/electrical-room.png`** — Electrical Room

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/technic-room.png`** — Technic Room

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/garden.png`** — Garden

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/energy.png`** — Energy

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. flowing green and yellow light currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/security.png`** — Security

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. deep crimson and dark red light sweeping across shadow, watchful and tense, alert. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/climate.png`** — Climate

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/media.png`** — Media

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/network.png`** — Network

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. blue and cyan data streams flowing through dark space, luminous nodes and connecting lines. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/settings.png`** — Settings

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>cyberprep</b> — all 23 prompts</summary>

**`cyberprep/home.png`** — Home

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/living-room.png`** — Living Room

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/kitchen.png`** — Kitchen

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/bedroom.png`** — Bedroom

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. a deep indigo and violet nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/master-bedroom.png`** — Master Bedroom

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/guest.png`** — Guest

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. soft teal and sage mist drifting slowly, calm, minimal, welcoming. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/bathroom.png`** — Bathroom

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/office.png`** — Office

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/ai.png`** — AI

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/outside.png`** — Outside

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/hallway.png`** — Hallway

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. warm dim light receding down a long perspective gradient, muted slate and amber, transitional. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/garage.png`** — Garage

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. brushed steel grey lit by a single orange sodium lamp, industrial, oily dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/front-yard.png`** — Front Yard

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/back-yard.png`** — Back Yard

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. late sunset green and warm orange across grass, dusk settling, relaxed. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/electrical-room.png`** — Electrical Room

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/technic-room.png`** — Technic Room

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/garden.png`** — Garden

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/energy.png`** — Energy

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. flowing green and yellow light currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/security.png`** — Security

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. deep crimson and dark red light sweeping across shadow, watchful and tense, alert. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/climate.png`** — Climate

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/media.png`** — Media

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/network.png`** — Network

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. blue and cyan data streams flowing through dark space, luminous nodes and connecting lines. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/settings.png`** — Settings

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>cyberpunk</b> — all 23 prompts</summary>

**`cyberpunk/home.png`** — Home

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/living-room.png`** — Living Room

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/kitchen.png`** — Kitchen

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/bedroom.png`** — Bedroom

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. a deep indigo and violet nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/master-bedroom.png`** — Master Bedroom

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/guest.png`** — Guest

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. soft teal and sage mist drifting slowly, calm, minimal, welcoming. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/bathroom.png`** — Bathroom

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/office.png`** — Office

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/ai.png`** — AI

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/outside.png`** — Outside

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/hallway.png`** — Hallway

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. warm dim light receding down a long perspective gradient, muted slate and amber, transitional. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/garage.png`** — Garage

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. brushed steel grey lit by a single orange sodium lamp, industrial, oily dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/front-yard.png`** — Front Yard

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/back-yard.png`** — Back Yard

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. late sunset green and warm orange across grass, dusk settling, relaxed. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/electrical-room.png`** — Electrical Room

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/technic-room.png`** — Technic Room

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/garden.png`** — Garden

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/energy.png`** — Energy

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. flowing green and yellow light currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/security.png`** — Security

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. deep crimson and dark red light sweeping across shadow, watchful and tense, alert. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/climate.png`** — Climate

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/media.png`** — Media

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/network.png`** — Network

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. blue and cyan data streams flowing through dark space, luminous nodes and connecting lines. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/settings.png`** — Settings

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>solarpunk</b> — all 23 prompts</summary>

**`solarpunk/home.png`** — Home

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/living-room.png`** — Living Room

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/kitchen.png`** — Kitchen

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/bedroom.png`** — Bedroom

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. a deep indigo and violet nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/master-bedroom.png`** — Master Bedroom

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/guest.png`** — Guest

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. soft teal and sage mist drifting slowly, calm, minimal, welcoming. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/bathroom.png`** — Bathroom

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/office.png`** — Office

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/ai.png`** — AI

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/outside.png`** — Outside

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/hallway.png`** — Hallway

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. warm dim light receding down a long perspective gradient, muted slate and amber, transitional. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/garage.png`** — Garage

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. brushed steel grey lit by a single orange sodium lamp, industrial, oily dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/front-yard.png`** — Front Yard

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/back-yard.png`** — Back Yard

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. late sunset green and warm orange across grass, dusk settling, relaxed. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/electrical-room.png`** — Electrical Room

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/technic-room.png`** — Technic Room

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/garden.png`** — Garden

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/energy.png`** — Energy

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. flowing green and yellow light currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/security.png`** — Security

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. deep crimson and dark red light sweeping across shadow, watchful and tense, alert. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/climate.png`** — Climate

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/media.png`** — Media

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/network.png`** — Network

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. blue and cyan data streams flowing through dark space, luminous nodes and connecting lines. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/settings.png`** — Settings

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>art-deco</b> — all 23 prompts</summary>

**`art-deco/home.png`** — Home

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/living-room.png`** — Living Room

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/kitchen.png`** — Kitchen

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/bedroom.png`** — Bedroom

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. a deep indigo and violet nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/master-bedroom.png`** — Master Bedroom

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/guest.png`** — Guest

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. soft teal and sage mist drifting slowly, calm, minimal, welcoming. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/bathroom.png`** — Bathroom

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/office.png`** — Office

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/ai.png`** — AI

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/outside.png`** — Outside

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/hallway.png`** — Hallway

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. warm dim light receding down a long perspective gradient, muted slate and amber, transitional. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/garage.png`** — Garage

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. brushed steel grey lit by a single orange sodium lamp, industrial, oily dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/front-yard.png`** — Front Yard

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/back-yard.png`** — Back Yard

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. late sunset green and warm orange across grass, dusk settling, relaxed. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/electrical-room.png`** — Electrical Room

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/technic-room.png`** — Technic Room

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/garden.png`** — Garden

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/energy.png`** — Energy

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. flowing green and yellow light currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/security.png`** — Security

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. deep crimson and dark red light sweeping across shadow, watchful and tense, alert. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/climate.png`** — Climate

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/media.png`** — Media

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/network.png`** — Network

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. blue and cyan data streams flowing through dark space, luminous nodes and connecting lines. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/settings.png`** — Settings

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>dark-academia</b> — all 23 prompts</summary>

**`dark-academia/home.png`** — Home

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/living-room.png`** — Living Room

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/kitchen.png`** — Kitchen

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/bedroom.png`** — Bedroom

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. a deep indigo and violet nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/master-bedroom.png`** — Master Bedroom

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/guest.png`** — Guest

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. soft teal and sage mist drifting slowly, calm, minimal, welcoming. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/bathroom.png`** — Bathroom

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/office.png`** — Office

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/ai.png`** — AI

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/outside.png`** — Outside

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/hallway.png`** — Hallway

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. warm dim light receding down a long perspective gradient, muted slate and amber, transitional. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/garage.png`** — Garage

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. brushed steel grey lit by a single orange sodium lamp, industrial, oily dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/front-yard.png`** — Front Yard

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/back-yard.png`** — Back Yard

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. late sunset green and warm orange across grass, dusk settling, relaxed. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/electrical-room.png`** — Electrical Room

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/technic-room.png`** — Technic Room

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/garden.png`** — Garden

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/energy.png`** — Energy

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. flowing green and yellow light currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/security.png`** — Security

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. deep crimson and dark red light sweeping across shadow, watchful and tense, alert. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/climate.png`** — Climate

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/media.png`** — Media

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/network.png`** — Network

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. blue and cyan data streams flowing through dark space, luminous nodes and connecting lines. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/settings.png`** — Settings

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>cottagecore</b> — all 23 prompts</summary>

**`cottagecore/home.png`** — Home

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/living-room.png`** — Living Room

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/kitchen.png`** — Kitchen

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/bedroom.png`** — Bedroom

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. a deep indigo and violet nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/master-bedroom.png`** — Master Bedroom

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/guest.png`** — Guest

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. soft teal and sage mist drifting slowly, calm, minimal, welcoming. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/bathroom.png`** — Bathroom

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/office.png`** — Office

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/ai.png`** — AI

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/outside.png`** — Outside

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/hallway.png`** — Hallway

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. warm dim light receding down a long perspective gradient, muted slate and amber, transitional. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/garage.png`** — Garage

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. brushed steel grey lit by a single orange sodium lamp, industrial, oily dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/front-yard.png`** — Front Yard

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/back-yard.png`** — Back Yard

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. late sunset green and warm orange across grass, dusk settling, relaxed. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/electrical-room.png`** — Electrical Room

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/technic-room.png`** — Technic Room

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/garden.png`** — Garden

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/energy.png`** — Energy

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. flowing green and yellow light currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/security.png`** — Security

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. deep crimson and dark red light sweeping across shadow, watchful and tense, alert. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/climate.png`** — Climate

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/media.png`** — Media

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/network.png`** — Network

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. blue and cyan data streams flowing through dark space, luminous nodes and connecting lines. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/settings.png`** — Settings

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>synthwave</b> — all 23 prompts</summary>

**`synthwave/home.png`** — Home

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. a warm aurora of amber and deep blue light folding over itself, like evening light spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/living-room.png`** — Living Room

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. soft amber and rose light pooling across a dark surface, warm lamplight bokeh, deep comfortable shadow. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/kitchen.png`** — Kitchen

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. warm copper, butter and cream light bleeding through drifting steam, appetising warmth, dark surround. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/bedroom.png`** — Bedroom

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. a deep indigo and violet nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/master-bedroom.png`** — Master Bedroom

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. plum and deep magenta silk folds lit from within, velvet depth, quietly luxurious. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/guest.png`** — Guest

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. soft teal and sage mist drifting slowly, calm, minimal, welcoming. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/bathroom.png`** — Bathroom

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. aqua and cyan caustics rippling as if seen through water, soft focus, cool and clean. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/office.png`** — Office

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. cool steel-blue light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/ai.png`** — AI

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. electric violet and magenta neural filaments glowing in dark space, branching data pathways, synthetic intelligence. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/outside.png`** — Outside

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. a dawn sky gradient of pale blue and gold above a dark blurred treeline, open air. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/hallway.png`** — Hallway

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. warm dim light receding down a long perspective gradient, muted slate and amber, transitional. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/garage.png`** — Garage

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. brushed steel grey lit by a single orange sodium lamp, industrial, oily dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/front-yard.png`** — Front Yard

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. morning green and gold light filtering through leaves, soft bokeh, dark vignetted edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/back-yard.png`** — Back Yard

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. late sunset green and warm orange across grass, dusk settling, relaxed. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/electrical-room.png`** — Electrical Room

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. amber and yellow energy arcs crackling in a dark industrial space, sparks of high voltage light. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/technic-room.png`** — Technic Room

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. cyan and steel-blue technical glow, faint circuit and schematic geometry dissolving into dark. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/garden.png`** — Garden

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. verdant green and lime light through dense foliage, dew catching light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/energy.png`** — Energy

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. flowing green and yellow light currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/security.png`** — Security

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. deep crimson and dark red light sweeping across shadow, watchful and tense, alert. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/climate.png`** — Climate

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. a cool cyan current and a warm orange current meeting and swirling together, hot and cold in balance. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/media.png`** — Media

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. magenta and purple cinematic light streaks across a dark theatre, projector haze, dramatic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/network.png`** — Network

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. blue and cyan data streams flowing through dark space, luminous nodes and connecting lines. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/settings.png`** — Settings

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

## Styles without a theme yet

`glass`, `velvet` and `neon` are complete visual systems — palette, blur character, geometry and accent language all live in `build/modes.py`, and each renders 24 themes.

The seven below currently exist as **artwork only**. The prompts are here, `build/import_backgrounds.py` will process anything you drop in, and the images land in `www/ultimate-theme/backgrounds/<style>/` — but no theme references them yet. Turning one into a real mode means choosing its palette, blur, radii and border language in `build/modes.py`; that is a design decision, not a mechanical one.

| Style | Reads as |
|---|---|
| `cyberprep` | clean, chrome, optimistic high-tech |
| `cyberpunk` | wet asphalt, signage bokeh, grimy |
| `solarpunk` | canopy light, gold and green, overgrown |
| `art-deco` | black lacquer, brass geometry, symmetrical |
| `dark-academia` | candlelight, oxblood, chiaroscuro |
| `cottagecore` | dusk hearth light, sage and cream, matte |
| `synthwave` | grid horizon, banded sun, VHS artefacts |

`neon`, `cyberpunk` and `synthwave` are the three most likely to collapse into each other, so their style blocks are pushed apart deliberately: neon is clean and scanlined, cyberpunk is wet and dirty, synthwave is geometric and nostalgic.
