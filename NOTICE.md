# Third-party notices

The Home Assistant Ultimate Theme is an original work, but portions of its CSS
were derived from existing open-source Home Assistant themes. Those projects are
distributed under the MIT License, which requires their copyright and permission
notices to be retained in derivative works. They are reproduced below.

This file exists to satisfy that requirement. No other file in this repository
needs to carry these notices.

---

## Derived components

| Component in this project | Derived from |
|---|---|
| Card glass layer (`ha-card::before` backdrop-filter pattern), inset bevel shadow stack, sidebar and drawer blur | Project A |
| Card exclusion list (heading / glance / title / chips / bubble / text-only), data-table overrides, `--token-rgb-*` block | Project B |
| Mocha, Macchiato, Frappé and Latte colour values | Project C |
| Template-per-background generation approach, average-colour header tinting | Project D |
| `mush-*` geometry token names | Project E |

Everything else — the three-mode system, the specular sheen layer, the
`@supports` fallback, the fixed-pseudo-element background, the per-view
background hook, the accent ladder derivation, the procedural artwork generator,
the preview renderer, and the build pipeline — is original to this project.

---

## Licences

### Project A — visionOS-style glass theme
Copyright (c) Nezz
Source: https://github.com/Nezz/homeassistant-visionos-theme

### Project B — Frosted glass theme collection
Copyright (c) Wessam Lauf
Source: https://github.com/wessamlauf/homeassistant-frosted-glass-themes

### Project C — Catppuccin for Home Assistant
Copyright (c) Catppuccin
Source: https://github.com/catppuccin/home-assistant

### Project D — iOS theme collection
Copyright (c) Bas Nijholt
Source: https://github.com/basnijholt/lovelace-ios-themes

### Project E — Mushroom themes
Copyright (c) Paul Bottein
Source: https://github.com/piitaya/lovelace-mushroom-themes

---

All five are licensed under the MIT License:

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Fonts and assets

Preview renders use **Poppins**, licensed under the SIL Open Font License 1.1.

All background artwork in `www/` is generated procedurally by
`build/generate_backgrounds.py` and is original to this project.
