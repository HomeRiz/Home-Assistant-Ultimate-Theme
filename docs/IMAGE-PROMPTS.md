# Image prompts

Every background is `STYLE + SUBJECT + CONSTRAINTS`. The **subject is identical across all three modes** — that is deliberate. It means the Kitchen still reads as the Kitchen whether you are in Glass, Velvet or Neon.

You do not have to do all 140. Anything you don't supply keeps its procedurally generated background, so you can replace them a few at a time.

## How to use

1. Generate an image.
2. Save it as `drop-in/<style>/<colour-key>.png` (e.g. `drop-in/glass/amber.png`). The filename **must** match the colour key exactly — that is how the importer knows where it goes.
3. Run:

```bash
python3 build/import_backgrounds.py
python3 build/generate_themes.py
```

The importer centre-crops to 2560×1440, darkens slightly so glass cards stay legible, converts to WebP, and refreshes the header tints. Use `--darken 0` if your images are already dark enough.

## Palette arbitration

The 14 subjects are shared by every style, and several name a colour outright. This clause sits between the subject and the constraints so the style's palette wins while the composition carries over — which is what keeps a colour recognisable across aesthetics.

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

| Colour key | Name | Subject |
|---|---|---|
| `ember` | Ember | deep crimson and scarlet light sweeping across shadow, embers still glowing at the edges, tense and alive |
| `rose` | Rose | hot pink and magenta blooming outward in dark space, soft overlapping petals of light, electric and romantic |
| `amber` | Amber | warm amber and burnt orange light folding over itself, like late sun spilling through an open doorway |
| `citrine` | Citrine | golden yellow light crackling against deep dark, high-voltage brightness, sharp and charged |
| `lime` | Lime | chartreuse and yellow-green currents streaming like energy in motion, kinetic, dark background |
| `verdant` | Verdant | vivid saturated green light through dense foliage, dew catching the light, soft focus, dark edges |
| `jade` | Jade | soft jade and mint mist drifting slowly, cool and restorative, minimal, very quiet |
| `lagoon` | Lagoon | aqua and cyan caustics rippling as if seen through shallow water, soft focus, clean and weightless |
| `azure` | Azure | electric azure streams flowing through dark space, luminous nodes and connecting lines, precise |
| `cobalt` | Cobalt | deep cobalt light falling in long focused shafts through vertical structure, crisp and awake |
| `indigo` | Indigo | a deep indigo and periwinkle nebula haze, very still and quiet, midnight calm |
| `violet` | Violet | electric violet and magenta filaments branching through dark space, synthetic and luminous |
| `sand` | Sand | warm sand and taupe light receding down a long perspective gradient, muted, unhurried |
| `graphite` | Graphite | restrained graphite and silver light, neutral, minimal, quietly technical |

## Ready-to-paste full prompts

<details>
<summary><b>glass</b> — all 14 prompts</summary>

**`glass/ember.png`** — Ember

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. deep crimson and scarlet light sweeping across shadow, embers still glowing at the edges, tense and alive. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/rose.png`** — Rose

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. hot pink and magenta blooming outward in dark space, soft overlapping petals of light, electric and romantic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/amber.png`** — Amber

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. warm amber and burnt orange light folding over itself, like late sun spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/citrine.png`** — Citrine

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. golden yellow light crackling against deep dark, high-voltage brightness, sharp and charged. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/lime.png`** — Lime

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. chartreuse and yellow-green currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/verdant.png`** — Verdant

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. vivid saturated green light through dense foliage, dew catching the light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/jade.png`** — Jade

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. soft jade and mint mist drifting slowly, cool and restorative, minimal, very quiet. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/lagoon.png`** — Lagoon

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. aqua and cyan caustics rippling as if seen through shallow water, soft focus, clean and weightless. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/azure.png`** — Azure

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. electric azure streams flowing through dark space, luminous nodes and connecting lines, precise. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/cobalt.png`** — Cobalt

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. deep cobalt light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/indigo.png`** — Indigo

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. a deep indigo and periwinkle nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/violet.png`** — Violet

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. electric violet and magenta filaments branching through dark space, synthetic and luminous. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/sand.png`** — Sand

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. warm sand and taupe light receding down a long perspective gradient, muted, unhurried. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`glass/graphite.png`** — Graphite

```
Abstract wallpaper in the style of Apple's spatial glass interfaces: liquid glass, smooth volumetric colour gradients, large soft bokeh, deep saturated colour with luminous depth, gentle film grain, no hard edges, painterly light. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>velvet</b> — all 14 prompts</summary>

**`velvet/ember.png`** — Ember

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. deep crimson and scarlet light sweeping across shadow, embers still glowing at the edges, tense and alive. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/rose.png`** — Rose

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. hot pink and magenta blooming outward in dark space, soft overlapping petals of light, electric and romantic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/amber.png`** — Amber

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. warm amber and burnt orange light folding over itself, like late sun spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/citrine.png`** — Citrine

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. golden yellow light crackling against deep dark, high-voltage brightness, sharp and charged. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/lime.png`** — Lime

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. chartreuse and yellow-green currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/verdant.png`** — Verdant

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. vivid saturated green light through dense foliage, dew catching the light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/jade.png`** — Jade

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. soft jade and mint mist drifting slowly, cool and restorative, minimal, very quiet. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/lagoon.png`** — Lagoon

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. aqua and cyan caustics rippling as if seen through shallow water, soft focus, clean and weightless. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/azure.png`** — Azure

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. electric azure streams flowing through dark space, luminous nodes and connecting lines, precise. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/cobalt.png`** — Cobalt

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. deep cobalt light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/indigo.png`** — Indigo

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. a deep indigo and periwinkle nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/violet.png`** — Violet

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. electric violet and magenta filaments branching through dark space, synthetic and luminous. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/sand.png`** — Sand

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. warm sand and taupe light receding down a long perspective gradient, muted, unhurried. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`velvet/graphite.png`** — Graphite

```
Abstract wallpaper, velvet-soft and matte — deep base #1e1e2e with muted pastel accents: mauve #cba6f7, blue #89b4fa, green #a6e3a1, yellow #f9e2af, red #f38ba8. Cozy and low contrast, soft matte gradients, flat diffuse light, gentle grain, nothing garish or glossy. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>neon</b> — all 14 prompts</summary>

**`neon/ember.png`** — Ember

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. deep crimson and scarlet light sweeping across shadow, embers still glowing at the edges, tense and alive. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/rose.png`** — Rose

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. hot pink and magenta blooming outward in dark space, soft overlapping petals of light, electric and romantic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/amber.png`** — Amber

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. warm amber and burnt orange light folding over itself, like late sun spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/citrine.png`** — Citrine

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. golden yellow light crackling against deep dark, high-voltage brightness, sharp and charged. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/lime.png`** — Lime

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. chartreuse and yellow-green currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/verdant.png`** — Verdant

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. vivid saturated green light through dense foliage, dew catching the light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/jade.png`** — Jade

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. soft jade and mint mist drifting slowly, cool and restorative, minimal, very quiet. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/lagoon.png`** — Lagoon

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. aqua and cyan caustics rippling as if seen through shallow water, soft focus, clean and weightless. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/azure.png`** — Azure

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. electric azure streams flowing through dark space, luminous nodes and connecting lines, precise. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/cobalt.png`** — Cobalt

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. deep cobalt light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/indigo.png`** — Indigo

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. a deep indigo and periwinkle nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/violet.png`** — Violet

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. electric violet and magenta filaments branching through dark space, synthetic and luminous. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/sand.png`** — Sand

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. warm sand and taupe light receding down a long perspective gradient, muted, unhurried. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`neon/graphite.png`** — Graphite

```
Abstract cyberpunk wallpaper: near-black #04050a base, high-chroma neon accent light, volumetric glow and light bloom, faint horizontal scanlines, subtle chromatic aberration on bright edges, deep contrast, cinematic, Blade Runner colour grade. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>cyberprep</b> — all 14 prompts</summary>

**`cyberprep/ember.png`** — Ember

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. deep crimson and scarlet light sweeping across shadow, embers still glowing at the edges, tense and alive. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/rose.png`** — Rose

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. hot pink and magenta blooming outward in dark space, soft overlapping petals of light, electric and romantic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/amber.png`** — Amber

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. warm amber and burnt orange light folding over itself, like late sun spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/citrine.png`** — Citrine

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. golden yellow light crackling against deep dark, high-voltage brightness, sharp and charged. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/lime.png`** — Lime

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. chartreuse and yellow-green currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/verdant.png`** — Verdant

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. vivid saturated green light through dense foliage, dew catching the light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/jade.png`** — Jade

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. soft jade and mint mist drifting slowly, cool and restorative, minimal, very quiet. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/lagoon.png`** — Lagoon

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. aqua and cyan caustics rippling as if seen through shallow water, soft focus, clean and weightless. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/azure.png`** — Azure

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. electric azure streams flowing through dark space, luminous nodes and connecting lines, precise. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/cobalt.png`** — Cobalt

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. deep cobalt light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/indigo.png`** — Indigo

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. a deep indigo and periwinkle nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/violet.png`** — Violet

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. electric violet and magenta filaments branching through dark space, synthetic and luminous. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/sand.png`** — Sand

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. warm sand and taupe light receding down a long perspective gradient, muted, unhurried. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberprep/graphite.png`** — Graphite

```
Abstract wallpaper, cyberprep — the optimistic answer to cyberpunk. Dark polished graphite and slate base, brushed aluminium and pale chrome surfaces, clean sky-cyan #5AC8F5 and soft white accent light, crisp rim highlights, immaculate and unweathered, calm corporate futurism, generous negative space, no grime, no decay, no signage. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>cyberpunk</b> — all 14 prompts</summary>

**`cyberpunk/ember.png`** — Ember

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. deep crimson and scarlet light sweeping across shadow, embers still glowing at the edges, tense and alive. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/rose.png`** — Rose

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. hot pink and magenta blooming outward in dark space, soft overlapping petals of light, electric and romantic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/amber.png`** — Amber

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. warm amber and burnt orange light folding over itself, like late sun spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/citrine.png`** — Citrine

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. golden yellow light crackling against deep dark, high-voltage brightness, sharp and charged. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/lime.png`** — Lime

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. chartreuse and yellow-green currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/verdant.png`** — Verdant

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. vivid saturated green light through dense foliage, dew catching the light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/jade.png`** — Jade

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. soft jade and mint mist drifting slowly, cool and restorative, minimal, very quiet. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/lagoon.png`** — Lagoon

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. aqua and cyan caustics rippling as if seen through shallow water, soft focus, clean and weightless. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/azure.png`** — Azure

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. electric azure streams flowing through dark space, luminous nodes and connecting lines, precise. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/cobalt.png`** — Cobalt

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. deep cobalt light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/indigo.png`** — Indigo

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. a deep indigo and periwinkle nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/violet.png`** — Violet

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. electric violet and magenta filaments branching through dark space, synthetic and luminous. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/sand.png`** — Sand

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. warm sand and taupe light receding down a long perspective gradient, muted, unhurried. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cyberpunk/graphite.png`** — Graphite

```
Abstract wallpaper, street-level cyberpunk: rain-slick black asphalt reflecting smeared teal #00E5C0 and hot magenta #FF2E88 signage bokeh, dense atmospheric haze and drifting steam, wet reflections stretched into vertical streaks, grimy and lived-in, heavy contrast, sodium spill in the shadows, 35mm anamorphic flare, gritty film grain. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>solarpunk</b> — all 14 prompts</summary>

**`solarpunk/ember.png`** — Ember

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. deep crimson and scarlet light sweeping across shadow, embers still glowing at the edges, tense and alive. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/rose.png`** — Rose

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. hot pink and magenta blooming outward in dark space, soft overlapping petals of light, electric and romantic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/amber.png`** — Amber

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. warm amber and burnt orange light folding over itself, like late sun spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/citrine.png`** — Citrine

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. golden yellow light crackling against deep dark, high-voltage brightness, sharp and charged. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/lime.png`** — Lime

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. chartreuse and yellow-green currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/verdant.png`** — Verdant

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. vivid saturated green light through dense foliage, dew catching the light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/jade.png`** — Jade

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. soft jade and mint mist drifting slowly, cool and restorative, minimal, very quiet. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/lagoon.png`** — Lagoon

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. aqua and cyan caustics rippling as if seen through shallow water, soft focus, clean and weightless. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/azure.png`** — Azure

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. electric azure streams flowing through dark space, luminous nodes and connecting lines, precise. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/cobalt.png`** — Cobalt

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. deep cobalt light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/indigo.png`** — Indigo

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. a deep indigo and periwinkle nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/violet.png`** — Violet

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. electric violet and magenta filaments branching through dark space, synthetic and luminous. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/sand.png`** — Sand

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. warm sand and taupe light receding down a long perspective gradient, muted, unhurried. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`solarpunk/graphite.png`** — Graphite

```
Abstract wallpaper, solarpunk: deep forest green base with warm gold sunlight filtering through a dense living canopy, organic art-nouveau curves in the light itself, verdant #2E7D5B and honey #E3B04B, dappled shade, pollen and dust motes catching sun, hopeful and overgrown, soft focus, dark at the edges where the canopy closes in. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>art-deco</b> — all 14 prompts</summary>

**`art-deco/ember.png`** — Ember

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. deep crimson and scarlet light sweeping across shadow, embers still glowing at the edges, tense and alive. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/rose.png`** — Rose

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. hot pink and magenta blooming outward in dark space, soft overlapping petals of light, electric and romantic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/amber.png`** — Amber

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. warm amber and burnt orange light folding over itself, like late sun spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/citrine.png`** — Citrine

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. golden yellow light crackling against deep dark, high-voltage brightness, sharp and charged. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/lime.png`** — Lime

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. chartreuse and yellow-green currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/verdant.png`** — Verdant

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. vivid saturated green light through dense foliage, dew catching the light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/jade.png`** — Jade

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. soft jade and mint mist drifting slowly, cool and restorative, minimal, very quiet. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/lagoon.png`** — Lagoon

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. aqua and cyan caustics rippling as if seen through shallow water, soft focus, clean and weightless. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/azure.png`** — Azure

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. electric azure streams flowing through dark space, luminous nodes and connecting lines, precise. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/cobalt.png`** — Cobalt

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. deep cobalt light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/indigo.png`** — Indigo

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. a deep indigo and periwinkle nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/violet.png`** — Violet

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. electric violet and magenta filaments branching through dark space, synthetic and luminous. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/sand.png`** — Sand

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. warm sand and taupe light receding down a long perspective gradient, muted, unhurried. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`art-deco/graphite.png`** — Graphite

```
Abstract wallpaper, 1920s art deco: black lacquer and deep emerald #0B3D2E ground with brushed brass and champagne gold #C9A227 line work, symmetrical sunburst fans and stepped chevrons, precise geometry, polished inlay, restrained metallic sheen, elegant and architectural, no clutter, generous dark field. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>dark-academia</b> — all 14 prompts</summary>

**`dark-academia/ember.png`** — Ember

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. deep crimson and scarlet light sweeping across shadow, embers still glowing at the edges, tense and alive. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/rose.png`** — Rose

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. hot pink and magenta blooming outward in dark space, soft overlapping petals of light, electric and romantic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/amber.png`** — Amber

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. warm amber and burnt orange light folding over itself, like late sun spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/citrine.png`** — Citrine

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. golden yellow light crackling against deep dark, high-voltage brightness, sharp and charged. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/lime.png`** — Lime

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. chartreuse and yellow-green currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/verdant.png`** — Verdant

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. vivid saturated green light through dense foliage, dew catching the light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/jade.png`** — Jade

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. soft jade and mint mist drifting slowly, cool and restorative, minimal, very quiet. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/lagoon.png`** — Lagoon

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. aqua and cyan caustics rippling as if seen through shallow water, soft focus, clean and weightless. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/azure.png`** — Azure

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. electric azure streams flowing through dark space, luminous nodes and connecting lines, precise. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/cobalt.png`** — Cobalt

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. deep cobalt light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/indigo.png`** — Indigo

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. a deep indigo and periwinkle nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/violet.png`** — Violet

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. electric violet and magenta filaments branching through dark space, synthetic and luminous. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/sand.png`** — Sand

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. warm sand and taupe light receding down a long perspective gradient, muted, unhurried. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`dark-academia/graphite.png`** — Graphite

```
Abstract wallpaper, dark academia: oxblood #5C1A1B, walnut brown and aged parchment cream, single warm candle-lit source falling across deep shadow, chiaroscuro, dust suspended in the light, faint texture of old paper and leather binding, scholarly and melancholic, painterly, heavily vignetted. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>cottagecore</b> — all 14 prompts</summary>

**`cottagecore/ember.png`** — Ember

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. deep crimson and scarlet light sweeping across shadow, embers still glowing at the edges, tense and alive. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/rose.png`** — Rose

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. hot pink and magenta blooming outward in dark space, soft overlapping petals of light, electric and romantic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/amber.png`** — Amber

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. warm amber and burnt orange light folding over itself, like late sun spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/citrine.png`** — Citrine

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. golden yellow light crackling against deep dark, high-voltage brightness, sharp and charged. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/lime.png`** — Lime

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. chartreuse and yellow-green currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/verdant.png`** — Verdant

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. vivid saturated green light through dense foliage, dew catching the light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/jade.png`** — Jade

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. soft jade and mint mist drifting slowly, cool and restorative, minimal, very quiet. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/lagoon.png`** — Lagoon

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. aqua and cyan caustics rippling as if seen through shallow water, soft focus, clean and weightless. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/azure.png`** — Azure

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. electric azure streams flowing through dark space, luminous nodes and connecting lines, precise. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/cobalt.png`** — Cobalt

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. deep cobalt light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/indigo.png`** — Indigo

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. a deep indigo and periwinkle nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/violet.png`** — Violet

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. electric violet and magenta filaments branching through dark space, synthetic and luminous. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/sand.png`** — Sand

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. warm sand and taupe light receding down a long perspective gradient, muted, unhurried. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`cottagecore/graphite.png`** — Graphite

```
Abstract wallpaper, cottagecore at dusk: muted sage #7C8B6F, warm cream and dried-rose #C48B8B, soft hearth lamplight glowing from one side, hazy pastoral evening light, gentle linen and dried-flower texture, hand-made and unhurried, low contrast, matte, dark corners so the warmth reads as a single pool of light. restrained graphite and silver light, neutral, minimal, quietly technical. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

</details>

<details>
<summary><b>synthwave</b> — all 14 prompts</summary>

**`synthwave/ember.png`** — Ember

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. deep crimson and scarlet light sweeping across shadow, embers still glowing at the edges, tense and alive. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/rose.png`** — Rose

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. hot pink and magenta blooming outward in dark space, soft overlapping petals of light, electric and romantic. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/amber.png`** — Amber

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. warm amber and burnt orange light folding over itself, like late sun spilling through an open doorway. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/citrine.png`** — Citrine

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. golden yellow light crackling against deep dark, high-voltage brightness, sharp and charged. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/lime.png`** — Lime

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. chartreuse and yellow-green currents streaming like energy in motion, kinetic, dark background. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/verdant.png`** — Verdant

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. vivid saturated green light through dense foliage, dew catching the light, soft focus, dark edges. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/jade.png`** — Jade

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. soft jade and mint mist drifting slowly, cool and restorative, minimal, very quiet. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/lagoon.png`** — Lagoon

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. aqua and cyan caustics rippling as if seen through shallow water, soft focus, clean and weightless. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/azure.png`** — Azure

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. electric azure streams flowing through dark space, luminous nodes and connecting lines, precise. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/cobalt.png`** — Cobalt

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. deep cobalt light falling in long focused shafts through vertical structure, crisp and awake. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/indigo.png`** — Indigo

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. a deep indigo and periwinkle nebula haze, very still and quiet, midnight calm. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/violet.png`** — Violet

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. electric violet and magenta filaments branching through dark space, synthetic and luminous. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/sand.png`** — Sand

```
Abstract wallpaper, 1984 retro synthwave: deep indigo-to-magenta sky gradient #2B0B4E to #FF2E88, a low chrome horizon with a receding perspective grid in cyan #00E5FF, a banded scanlined sun sitting near the edge, VHS tracking artefacts and chromatic fringing, airbrushed poster finish, nostalgic and geometric, dark upper field. warm sand and taupe light receding down a long perspective gradient, muted, unhurried. Where the subject names a colour absent from this style's palette, translate it to the nearest colour that belongs to the style - the style palette always wins. Keep the subject's composition, mood and direction of light exactly. 16:9 aspect ratio, 2560x1440, desktop wallpaper. Dark overall so white UI text stays readable on top. Uncluttered centre — keep detail and interest toward the edges and corners. No text, no letters, no numbers, no watermark, no logo, no signature, no people, no faces, no hands, no recognisable products.
```

**`synthwave/graphite.png`** — Graphite

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
