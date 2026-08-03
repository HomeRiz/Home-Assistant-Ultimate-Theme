#!/usr/bin/env python3
"""
Preview renderer.

Composites a mock Home Assistant dashboard over each generated background so the
repository can show what every theme actually looks like without needing a live
instance to screenshot.

The blur is real: for each card the renderer crops the region of the backdrop
underneath it, runs a Gaussian blur at the mode's own radius, tints it, and
composites it back through a rounded-rectangle mask. That is the same operation
`backdrop-filter` performs in the browser, so the result is representative
rather than illustrative.

Outputs
  docs/previews/<mode>/<area>.webp   1600x900, one per theme
  docs/previews/<mode>.webp          contact sheet, all 23 areas

Usage
  python3 build/render_previews.py              # everything
  python3 build/render_previews.py neon         # one mode
  python3 build/render_previews.py --resume     # skip what already exists
  python3 build/render_previews.py --sheets     # contact sheets only
"""

from __future__ import annotations

import os
import sys

# Build scripts run in CI, where a stray build/__pycache__ would show up as
# an untracked artefact. Nothing here benefits from cached bytecode.
sys.dont_write_bytecode = True

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from areas import as_dicts  # noqa: E402
from modes import accent_for_mode  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BG = os.path.join(ROOT, "www", "ultimate-theme", "backgrounds")
OUT = os.path.join(ROOT, "docs", "previews")

W, H = 1600, 900
FONTS = "/usr/share/fonts/truetype/google-fonts"


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(os.path.join(FONTS, name), size)


F_TITLE = lambda: font("Poppins-Medium.ttf", 27)          # noqa: E731
F_LABEL = lambda: font("Poppins-Regular.ttf", 17)         # noqa: E731
F_VALUE = lambda: font("Poppins-Medium.ttf", 25)          # noqa: E731
F_CHIP = lambda: font("Poppins-Regular.ttf", 15)          # noqa: E731

# ---------------------------------------------------------------------------
# Per-mode render spec. Mirrors build/modes.py — keep the two in step.
# ---------------------------------------------------------------------------
SPECS = {
    "glass": dict(
        radius=30, blur=26, tint=(255, 255, 255, 16),
        text=(255, 255, 255, 245), sub=(228, 228, 232, 200),
        border=None, bevel=(255, 255, 255, 70),
        sheen=(255, 255, 255, 46), glow=0.0,
        chrome_tint=(18, 18, 24, 96), scrim=(0, 0, 0, 46),
        label="Ultimate Glass",
    ),
    "velvet": dict(
        radius=18, blur=20, tint=(49, 50, 68, 118),
        text=(205, 214, 244, 245), sub=(166, 173, 200, 210),
        border=(205, 214, 244, 30), bevel=(205, 214, 244, 32),
        sheen=(205, 214, 244, 26), glow=0.0,
        chrome_tint=(24, 24, 37, 110), scrim=(17, 17, 27, 66),
        label="Ultimate Velvet",
    ),
    "neon": dict(
        radius=12, blur=16, tint=(6, 8, 16, 150),
        text=(233, 243, 255, 248), sub=(160, 176, 200, 215),
        border="accent", bevel=None,
        sheen="accent", glow=0.85,
        chrome_tint=(4, 5, 10, 130), scrim=(0, 0, 0, 92),
        label="Ultimate Neon",
    ),
}

# Card content per area — plausible entities so the previews read as real
# dashboards rather than lorem ipsum.
CARDS = {
    "home":            [("Front door", "Locked", "lock"), ("Living room", "22.4 °C", "thermo"), ("Everything", "6 on", "bulb"), ("Power now", "1.4 kW", "bolt")],
    "living-room":     [("Ceiling", "On · 60%", "bulb"), ("Temperature", "22.4 °C", "thermo"), ("TV", "Playing", "wave"), ("Blinds", "Open", "bolt")],
    "kitchen":         [("Worktop", "On · 80%", "bulb"), ("Oven", "180 °C", "thermo"), ("Dishwasher", "42 min", "wave"), ("Kettle", "Idle", "bolt")],
    "bedroom":         [("Bedside", "Off", "bulb"), ("Temperature", "19.8 °C", "thermo"), ("Humidity", "48%", "drop"), ("Alarm", "07:00", "wave")],
    "master-bedroom":  [("Ceiling", "On · 25%", "bulb"), ("Temperature", "20.1 °C", "thermo"), ("Window", "Closed", "lock"), ("Fan", "Low", "wave")],
    "guest":           [("Lights", "Off", "bulb"), ("Temperature", "21.0 °C", "thermo"), ("Occupancy", "Clear", "shield"), ("Heating", "Eco", "bolt")],
    "bathroom":        [("Mirror", "On", "bulb"), ("Humidity", "72%", "drop"), ("Floor heat", "24 °C", "thermo"), ("Extractor", "Running", "wave")],
    "office":          [("Desk lamp", "On · 70%", "bulb"), ("Monitor", "Active", "wave"), ("CO²", "612 ppm", "drop"), ("Power", "180 W", "bolt")],
    "ai":              [("Inference", "42 ms", "wave"), ("Queue", "3", "bolt"), ("Model", "Loaded", "shield"), ("GPU", "61 °C", "thermo")],
    "outside":         [("Porch", "On", "bulb"), ("Temperature", "14.2 °C", "thermo"), ("Wind", "11 km/h", "wave"), ("Rain", "None", "drop")],
    "hallway":         [("Lights", "Motion", "bulb"), ("Front door", "Locked", "lock"), ("Motion", "Clear", "shield"), ("Temperature", "20.5 °C", "thermo")],
    "garage":          [("Door", "Closed", "lock"), ("Car", "Charging", "bolt"), ("Temperature", "12.8 °C", "thermo"), ("Lights", "Off", "bulb")],
    "front-yard":      [("Path lights", "Auto", "bulb"), ("Gate", "Closed", "lock"), ("Sprinkler", "Off", "drop"), ("Camera", "Recording", "shield")],
    "back-yard":       [("Patio", "On · 40%", "bulb"), ("Temperature", "15.6 °C", "thermo"), ("Pool", "24 °C", "drop"), ("Grill", "Off", "bolt")],
    "electrical-room": [("Main load", "3.2 kW", "bolt"), ("Voltage", "231 V", "wave"), ("Breaker", "Nominal", "shield"), ("Temperature", "26 °C", "thermo")],
    "technic-room":    [("Boiler", "Running", "bolt"), ("Pressure", "1.8 bar", "wave"), ("Flow temp", "54 °C", "thermo"), ("Filter", "OK", "shield")],
    "garden":          [("Irrigation", "Zone 2", "drop"), ("Soil", "38%", "wave"), ("Lights", "Off", "bulb"), ("Temperature", "16.1 °C", "thermo")],
    "energy":          [("Solar now", "2.8 kW", "bolt"), ("Grid", "Exporting", "wave"), ("Battery", "84%", "shield"), ("Today", "18.4 kWh", "drop")],
    "security":        [("Alarm", "Armed", "shield"), ("Front door", "Locked", "lock"), ("Cameras", "4 online", "wave"), ("Motion", "Clear", "bolt")],
    "climate":         [("Thermostat", "21.5 °C", "thermo"), ("Mode", "Heating", "bolt"), ("Humidity", "45%", "drop"), ("Air quality", "Good", "wave")],
    "media":           [("Living room", "Playing", "wave"), ("Volume", "34%", "bolt"), ("Source", "Spotify", "bulb"), ("Cinema", "Off", "shield")],
    "network":         [("Down", "412 Mb/s", "wave"), ("Up", "38 Mb/s", "bolt"), ("Devices", "47", "shield"), ("Ping", "8 ms", "drop")],
    "settings":        [("Backups", "Daily", "shield"), ("Updates", "2 pending", "bolt"), ("Uptime", "18 days", "wave"), ("Storage", "62%", "drop")],
}


# ---------------------------------------------------------------------------
# Drawing helpers
# ---------------------------------------------------------------------------
# Filler entities, rotated per area so no two previews show the same eight cards.
SECONDARY = [
    ("Motion", "Clear", "shield"), ("Battery", "92%", "bolt"),
    ("Wi-Fi", "Strong", "wave"), ("Humidity", "46%", "drop"),
    ("Window", "Closed", "lock"), ("Brightness", "62%", "bulb"),
    ("Air quality", "Good", "drop"), ("Presence", "Home", "shield"),
]


def hex_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lift(rgb: tuple[int, int, int], t: float = 0.55) -> tuple[int, int, int]:
    """Mix a colour toward white — used so accent glyphs read on accent chips."""
    return tuple(int(c + (255 - c) * t) for c in rgb)


def rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, size[0] - 1, size[1] - 1],
                                        radius=radius, fill=255)
    return m


def glass_panel(base: Image.Image, box: tuple[int, int, int, int],
                spec: dict, accent: tuple[int, int, int],
                radius: int | None = None) -> None:
    """Composite one blurred, tinted, rounded panel onto `base` in place.

    This is the operation that makes the previews faithful: the backdrop is
    genuinely sampled and blurred, not faked with a flat fill.
    """
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    r = spec["radius"] if radius is None else radius

    # 1. sample the backdrop and blur it -> this IS backdrop-filter
    region = base.crop(box).filter(ImageFilter.GaussianBlur(spec["blur"]))

    # 2. tint
    tint = Image.new("RGBA", (w, h), tuple(spec["tint"]))
    region = Image.alpha_composite(region.convert("RGBA"), tint)

    # 3. specular sheen — bright top-left corner fading out by ~45%
    sheen_col = accent if spec["sheen"] == "accent" else tuple(spec["sheen"][:3])
    sheen_a = 60 if spec["sheen"] == "accent" else spec["sheen"][3]
    sheen = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sheen)
    span = max(1, int((w + h) * 0.45))
    for i in range(span):
        a = int(sheen_a * (1 - i / span) ** 2.2)
        if a <= 0:
            continue
        sd.line([(0, i), (i, 0)], fill=(*sheen_col, a))
    region = Image.alpha_composite(region, sheen)

    # 4. outer glow (neon)
    if spec["glow"] > 0:
        glow = Image.new("RGBA", base.size, (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        gd.rounded_rectangle([x0 - 2, y0 - 2, x1 + 2, y1 + 2], radius=r + 2,
                             fill=(*accent, int(150 * spec["glow"])))
        glow = glow.filter(ImageFilter.GaussianBlur(14))
        base.alpha_composite(glow)

    # 5. paste through rounded mask
    base.paste(region, (x0, y0), rounded_mask((w, h), r))

    # 6. edges: hairline border and/or inner bevel
    d = ImageDraw.Draw(base, "RGBA")
    if spec["border"] is not None:
        col = (*accent, 150) if spec["border"] == "accent" else tuple(spec["border"])
        d.rounded_rectangle([x0, y0, x1 - 1, y1 - 1], radius=r, outline=col, width=1)
    if spec["bevel"]:
        # Soft rim only — a hard full-width line reads as a stroke, not as glass.
        bv = spec["bevel"]
        edge = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        ImageDraw.Draw(edge).rounded_rectangle(
            [0, 0, w - 1, h - 1], radius=r, outline=(*bv[:3], bv[3]), width=1)
        # Fade the rim out toward the bottom so the light reads as coming from
        # above, the way the CSS sheen gradient does.
        fade = Image.linear_gradient("L").resize((w, h)).point(
            lambda v: max(0, 255 - int(v * 1.35)))
        edge.putalpha(ImageChops.multiply(edge.getchannel("A"), fade))
        base.alpha_composite(edge, (x0, y0))


def glyph(d: ImageDraw.ImageDraw, kind: str, cx: int, cy: int,
          s: int, col: tuple) -> None:
    """Small vector pictograms — no icon font dependency."""
    if kind == "bulb":
        d.ellipse([cx - s * .42, cy - s * .55, cx + s * .42, cy + s * .28], outline=col, width=2)
        d.line([(cx - s * .22, cy + s * .38), (cx + s * .22, cy + s * .38)], fill=col, width=2)
        d.line([(cx - s * .16, cy + s * .55), (cx + s * .16, cy + s * .55)], fill=col, width=2)
    elif kind == "bolt":
        d.polygon([(cx + s * .18, cy - s * .6), (cx - s * .3, cy + s * .08),
                   (cx - s * .02, cy + s * .08), (cx - s * .18, cy + s * .6),
                   (cx + s * .3, cy - s * .1), (cx + s * .02, cy - s * .1)], fill=col)
    elif kind == "thermo":
        d.rounded_rectangle([cx - s * .13, cy - s * .6, cx + s * .13, cy + s * .22],
                            radius=int(s * .13), outline=col, width=2)
        d.ellipse([cx - s * .27, cy + s * .12, cx + s * .27, cy + s * .62], fill=col)
    elif kind == "drop":
        d.polygon([(cx, cy - s * .62), (cx + s * .42, cy + s * .12),
                   (cx, cy + s * .58), (cx - s * .42, cy + s * .12)], outline=col, width=2)
        d.ellipse([cx - s * .34, cy - s * .12, cx + s * .34, cy + s * .56], outline=col, width=2)
    elif kind == "lock":
        d.rounded_rectangle([cx - s * .38, cy - s * .1, cx + s * .38, cy + s * .55],
                            radius=int(s * .1), outline=col, width=2)
        d.arc([cx - s * .26, cy - s * .62, cx + s * .26, cy + s * .18], 180, 360,
              fill=col, width=2)
    elif kind == "shield":
        d.polygon([(cx, cy - s * .62), (cx + s * .44, cy - s * .38),
                   (cx + s * .34, cy + s * .3), (cx, cy + s * .62),
                   (cx - s * .34, cy + s * .3), (cx - s * .44, cy - s * .38)],
                  outline=col, width=2)
    elif kind == "wave":
        for i, rr in enumerate((.24, .44, .64)):
            d.arc([cx - s * rr, cy - s * rr + s * .18, cx + s * rr, cy + s * rr + s * .18],
                  205, 335, fill=col, width=2)
        d.ellipse([cx - s * .07, cy + s * .34, cx + s * .07, cy + s * .48], fill=col)


# ---------------------------------------------------------------------------
def render(area: dict, mode: str) -> Image.Image:
    spec = SPECS[mode]
    accent = hex_rgb(accent_for_mode(area["accent"], mode))

    base = Image.open(os.path.join(BG, mode, f"{area['key']}.webp")).convert("RGBA")
    base = base.resize((W, H), Image.LANCZOS)

    # scrim — mirrors the theme's :host::after legibility layer
    base.alpha_composite(Image.new("RGBA", (W, H), tuple(spec["scrim"])))

    d = ImageDraw.Draw(base, "RGBA")

    # ---- sidebar -----------------------------------------------------------
    glass_panel(base, (0, 0, 76, H), spec, accent, radius=0)
    d = ImageDraw.Draw(base, "RGBA")
    for i in range(6):
        y = 38 + i * 58
        sel = i == 0
        if sel:
            d.rounded_rectangle([16, y - 4, 60, y + 40], radius=12, fill=(*accent, 55))
        glyph(d, ["bulb", "thermo", "bolt", "shield", "wave", "drop"][i],
              38, y + 18, 22,
              (*lift(accent), 255) if sel else (*spec["sub"][:3], 170))

    # ---- header ------------------------------------------------------------
    glass_panel(base, (108, 34, 108 + 470, 34 + 62), spec, accent,
                radius=min(spec["radius"], 31))
    d = ImageDraw.Draw(base, "RGBA")
    glyph(d, "bulb", 146, 65, 22, (*accent, 240))
    d.text((178, 51), area["name"], font=F_TITLE(), fill=tuple(spec["text"]))

    # mode label, right aligned
    lbl = spec["label"]
    lw = d.textlength(lbl, font=F_CHIP())
    glass_panel(base, (int(W - 52 - lw - 36), 44, W - 52, 86), spec, accent,
                radius=min(spec["radius"], 21))
    d = ImageDraw.Draw(base, "RGBA")
    d.text((W - 52 - lw - 18, 56), lbl, font=F_CHIP(), fill=tuple(spec["sub"]))

    # ---- badges ------------------------------------------------------------
    bx = 108
    for txt in ("All areas", "Active 6", "22.4 °C", "1.4 kW"):
        tw = int(d.textlength(txt, font=F_CHIP()))
        glass_panel(base, (bx, 118, bx + tw + 46, 158), spec, accent,
                    radius=min(spec["radius"], 20))
        d = ImageDraw.Draw(base, "RGBA")
        d.ellipse([bx + 15, 132, bx + 27, 144], fill=(*accent, 230))
        d.text((bx + 34, 129), txt, font=F_CHIP(), fill=tuple(spec["sub"]))
        bx += tw + 46 + 12

    # ---- card grid ---------------------------------------------------------
    # four area-specific cards, then four rotated fillers so no preview repeats
    off = area["seed"] % len(SECONDARY)
    cards = list(CARDS.get(area["key"], CARDS["home"]))[:4]
    cards += [SECONDARY[(off + i) % len(SECONDARY)] for i in range(4)]

    gx, gy, gap = 108, 186, 22
    cw = (W - gx - 52 - gap * 3) // 4
    ch = 222

    for row in range(2):
        for col in range(4):
            name, value, ic = cards[row * 4 + col]
            x0 = gx + col * (cw + gap)
            y0 = gy + row * (ch + gap)
            glass_panel(base, (x0, y0, x0 + cw, y0 + ch), spec, accent)
            d = ImageDraw.Draw(base, "RGBA")

            # icon chip — accent fill, glyph lifted toward white so it reads
            cxr = 30
            d.ellipse([x0 + 26, y0 + 26, x0 + 26 + cxr * 2, y0 + 26 + cxr * 2],
                      fill=(*accent, 60))
            glyph(d, ic, x0 + 26 + cxr, y0 + 26 + cxr, 30, (*lift(accent), 255))

            d.text((x0 + 26, y0 + 120), name.strip(), font=F_LABEL(),
                   fill=tuple(spec["sub"]))
            d.text((x0 + 26, y0 + 148), value, font=F_VALUE(),
                   fill=tuple(spec["text"]))

    # ---- footer strip ------------------------------------------------------
    fy = gy + 2 * (ch + gap)
    fh = 132
    glass_panel(base, (108, fy, W - 52, fy + fh), spec, accent)
    d = ImageDraw.Draw(base, "RGBA")
    d.text((132, fy + 20), "Today", font=F_LABEL(), fill=tuple(spec["sub"]))

    # Bar chart rather than an area fill — reads far better at thumbnail size,
    # where a filled sparkline collapses into a solid slab.
    import math
    x_lo, x_hi = 132, W - 76
    y_base, amp = fy + fh - 24, 62
    n = 34
    bw = (x_hi - x_lo) / n
    for i in range(n):
        t = i / (n - 1)
        v = (math.sin(t * 6.2 + area["seed"] % 7) * .42
             + math.sin(t * 2.3 + 1.2) * .30
             + math.sin(t * 11.0 + 0.5) * .16)
        v = max(0.10, v * .5 + .55)
        bx0 = x_lo + i * bw
        bh = v * amp
        peak = v > 0.78
        d.rounded_rectangle([bx0, y_base - bh, bx0 + bw - 6, y_base],
                            radius=3,
                            fill=(*accent, 235) if peak else (*accent, 120))

    return base.convert("RGB")


def contact_sheet(mode: str, areas: list[dict]) -> Image.Image:
    cols, tw, th, pad = 4, 380, 214, 14
    rows = (len(areas) + cols - 1) // cols
    sheet = Image.new("RGB",
                      (cols * tw + pad * (cols + 1), rows * (th + 30) + pad * (rows + 1)),
                      (12, 12, 16))
    d = ImageDraw.Draw(sheet)
    f = font("Poppins-Regular.ttf", 15)
    for i, a in enumerate(areas):
        r, c = divmod(i, cols)
        x = pad + c * (tw + pad)
        y = pad + r * (th + 30 + pad)
        im = Image.open(os.path.join(OUT, mode, f"{a['key']}.webp"))
        im = im.resize((tw, th), Image.LANCZOS)
        sheet.paste(im, (x, y))
        d.text((x + 2, y + th + 7), a["name"], font=f, fill=(190, 190, 200))
    return sheet


def main() -> None:
    args = sys.argv[1:]
    sheets_only = "--sheets" in args
    args = [a for a in args if not a.startswith("--")]
    only = args[0] if args else None

    resume = "--resume" in sys.argv
    areas = as_dicts()
    for mode in SPECS:
        if only and mode != only:
            continue
        os.makedirs(os.path.join(OUT, mode), exist_ok=True)
        if not sheets_only:
            for a in areas:
                p = os.path.join(OUT, mode, f"{a['key']}.webp")
                if resume and os.path.exists(p):
                    print(f"{mode:11s} {a['key']:17s} (kept)")
                    continue
                render(a, mode).save(p, "WEBP", quality=84, method=4)
                print(f"{mode:11s} {a['key']:17s} {os.path.getsize(p)/1024:6.0f} KB")
        sheet = contact_sheet(mode, areas)
        sp = os.path.join(OUT, f"{mode}.webp")
        sheet.save(sp, "WEBP", quality=82, method=4)
        print(f"{mode:11s} contact sheet     {os.path.getsize(sp)/1024:6.0f} KB")


if __name__ == "__main__":
    main()
