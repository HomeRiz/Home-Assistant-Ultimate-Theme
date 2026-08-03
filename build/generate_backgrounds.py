#!/usr/bin/env python3
"""
Procedural background generator for the Home Assistant Ultimate Theme.

Renders one backdrop per area per aesthetic mode. The composition for a given
area is identical across modes (same seed -> same blob layout), only the palette
and post-processing change. That is what keeps a room recognisable when you
switch between Liquid Glass, Velvet and Neon.

Technique:
  1. fBm value noise (cheap: low-res random upsampled bicubically, octave-summed)
  2. Domain warping of the coordinate field by that noise -> organic, non-circular blobs
  3. Radial-falloff colour blobs summed with weight normalisation -> mesh gradient
  4. Per-mode grade: base blend, saturation curve, bloom, vignette, grain
  5. Neon mode additionally gets scanlines and a chromatic edge lift

Output: WebP, 2560x1440, quality tuned so each file lands well under 400 KB.
"""

from __future__ import annotations

import colorsys
import math
import os
import sys

# Build scripts run in CI, where a stray build/__pycache__ would show up as
# an untracked artefact. Nothing here benefits from cached bytecode.
sys.dont_write_bytecode = True

import numpy as np
from PIL import Image, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from areas import as_dicts  # noqa: E402

W, H = 2560, 1440
OUT_ROOT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "www", "ultimate-theme", "backgrounds",
)

# --------------------------------------------------------------------------
# Mode definitions
# --------------------------------------------------------------------------
# base        : the colour the whole field sits on top of
# sat         : saturation multiplier applied to blob colours
# val         : value (brightness) multiplier applied to blob colours
# mix         : how strongly the mesh gradient overrides the base (0-1)
# bloom       : radius/strength of the additive glow pass
# vignette    : strength of the corner darkening
# grain       : film grain amplitude (0-255 scale)
# scanlines   : neon-only horizontal line modulation
MODES = {
    "glass": dict(
        base="#0B0D14", sat=0.95, val=1.00, mix=0.94,
        bloom=(120, 0.30), vignette=0.42, grain=3.0, scanlines=0.0,
        velvet_snap=False,
    ),
    "velvet": dict(
        base="#181825", sat=0.58, val=0.80, mix=0.90, sat_boost=2.1,
        bloom=(150, 0.20), vignette=0.34, grain=2.5, scanlines=0.0,
        velvet_snap=True,
    ),
    "neon": dict(
        base="#04050A", sat=1.35, val=1.05, mix=0.95,
        bloom=(90, 0.55), vignette=0.55, grain=4.0, scanlines=0.030,
        velvet_snap=False,
    ),
}

# The Velvet accent ring. Blob hues are snapped onto it so the mode never
# drifts off-palette. Values retained from a third-party colour scheme;
# see NOTICE.md.
VELVET_ACCENTS = [
    "#f5e0dc", "#f2cdcd", "#f5c2e7", "#cba6f7", "#f38ba8", "#eba0ac",
    "#fab387", "#f9e2af", "#a6e3a1", "#94e2d5", "#89dceb", "#74c7ec",
    "#89b4fa", "#b4befe",
]


# --------------------------------------------------------------------------
# Colour helpers
# --------------------------------------------------------------------------
def hex_to_rgb(h: str) -> tuple[float, float, float]:
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def rgb_to_hex(rgb) -> str:
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(round(c * 255)))) for c in rgb)


def hue_to_rgb(hue_deg: float, sat: float, val: float) -> tuple[float, float, float]:
    return colorsys.hsv_to_rgb((hue_deg % 360) / 360.0, sat, val)


def snap_to_velvet(rgb, sat_boost: float = 1.0) -> tuple[float, float, float]:
    """Snap a colour to the nearest Velvet accent by hue distance.

    Velvet accents are pastel (S ~0.3), so snapping straight to them drains
    the image to grey once the blobs blend. sat_boost pushes chroma back up
    while keeping the on-spec hues.
    """
    h, s, v = colorsys.rgb_to_hsv(*rgb)
    best, best_d = None, 1e9
    for cand in VELVET_ACCENTS:
        ch, cs, cv = colorsys.rgb_to_hsv(*hex_to_rgb(cand))
        d = min(abs(ch - h), 1 - abs(ch - h))
        if d < best_d:
            best_d, best = d, (ch, cs, cv)
    sat = min(1.0, best[1] * sat_boost)
    # keep the candidate hue, but retain some of the original value
    return colorsys.hsv_to_rgb(best[0], sat, best[2] * 0.55 + v * 0.45)


# --------------------------------------------------------------------------
# Noise
# --------------------------------------------------------------------------
def value_noise(rng: np.random.Generator, w: int, h: int, cells: int) -> np.ndarray:
    """Smooth noise via bicubic upsampling of a small random grid."""
    small = rng.random((cells, cells)).astype(np.float32)
    img = Image.fromarray((small * 255).astype(np.uint8), mode="L")
    img = img.resize((w, h), Image.BICUBIC)
    return np.asarray(img, dtype=np.float32) / 255.0


FBM_DOWNSCALE = 4  # noise is smooth by construction, so build it small and upscale


def fbm(rng: np.random.Generator, w: int, h: int, octaves: int = 5,
        base_cells: int = 3, gain: float = 0.5) -> np.ndarray:
    """Fractal Brownian motion: octave-summed value noise, normalised to 0-1.

    Computed at 1/FBM_DOWNSCALE resolution and upscaled once. The result is
    visually identical because every octave is already band-limited well below
    Nyquist at full res, but it is about 5x faster (measured, 6 octaves at
    2560x1440).
    """
    lw, lh = max(8, w // FBM_DOWNSCALE), max(8, h // FBM_DOWNSCALE)
    total = np.zeros((lh, lw), dtype=np.float32)
    amp, norm, cells = 1.0, 0.0, base_cells
    for _ in range(octaves):
        total += amp * value_noise(rng, lw, lh, cells)
        norm += amp
        amp *= gain
        cells = max(2, int(cells * 2.15))
    total /= norm
    lo, hi = float(total.min()), float(total.max())
    total = (total - lo) / max(1e-6, hi - lo)

    if (lw, lh) != (w, h):
        img = Image.fromarray((total * 255).astype(np.uint8), mode="L")
        total = np.asarray(img.resize((w, h), Image.BICUBIC),
                           dtype=np.float32) / 255.0
    return total


# --------------------------------------------------------------------------
# Core render
# --------------------------------------------------------------------------
def render_area(area: dict, mode_name: str, mode: dict,
                w: int = W, h: int = H) -> Image.Image:
    rng = np.random.default_rng(area["seed"])

    # --- 1. coordinate field, aspect corrected -----------------------------
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    xx /= w
    yy /= h
    aspect = w / h

    # --- 2. domain warp ----------------------------------------------------
    warp_x = fbm(rng, w, h, octaves=4, base_cells=3) - 0.5
    warp_y = fbm(rng, w, h, octaves=4, base_cells=3) - 0.5
    warp_amount = 0.16 if mode_name != "neon" else 0.22
    wx = xx + warp_x * warp_amount
    wy = yy + warp_y * warp_amount

    # --- 3. mesh gradient from hue anchors ---------------------------------
    hues = area["hues"]
    n_blobs = len(hues) + 2  # a couple of extra blobs for depth

    accum = np.zeros((h, w, 3), dtype=np.float32)
    weight = np.zeros((h, w), dtype=np.float32)

    for i in range(n_blobs):
        hue = hues[i % len(hues)] + rng.uniform(-14, 14)

        # deterministic-ish placement biased toward a pleasing golden-angle spiral
        ang = i * 2.39996 + rng.uniform(-0.4, 0.4)
        rad = 0.20 + 0.34 * math.sqrt((i + 0.6) / n_blobs)
        cx = 0.5 + math.cos(ang) * rad * 1.15
        cy = 0.5 + math.sin(ang) * rad * 0.92
        cx = float(np.clip(cx, -0.12, 1.12))
        cy = float(np.clip(cy, -0.12, 1.12))

        sigma = rng.uniform(0.22, 0.42)

        sat = float(np.clip(rng.uniform(0.55, 0.88) * mode["sat"], 0, 1))
        val = float(np.clip(rng.uniform(0.62, 0.98) * mode["val"], 0, 1))
        col = hue_to_rgb(hue, sat, val)
        if mode["velvet_snap"]:
            col = snap_to_velvet(col, mode.get("sat_boost", 1.0))

        dx = (wx - cx) * aspect
        dy = wy - cy
        d2 = dx * dx + dy * dy
        wgt = np.exp(-d2 / (2.0 * sigma * sigma)).astype(np.float32)
        # Power weighting: pushes the blend toward a winner-takes-most mix so
        # neighbouring hues stay distinct instead of averaging into mud.
        wgt = wgt ** 2.6

        accum += wgt[..., None] * np.array(col, dtype=np.float32)
        weight += wgt

    mesh = accum / np.maximum(weight, 1e-6)[..., None]

    # Re-saturate: the blend still pulls toward grey, so push chroma back out
    # around the per-pixel luminance.
    lum = mesh.mean(axis=2, keepdims=True)
    mesh = np.clip(lum + (mesh - lum) * 1.45, 0.0, 1.0)

    # --- 4. composite over base -------------------------------------------
    base = np.array(hex_to_rgb(mode["base"]), dtype=np.float32)
    # weight falls off at the edges -> base shows through, giving natural vignette
    cover = np.clip(weight / max(1e-6, float(weight.max())), 0, 1) ** 0.55
    alpha = (cover * mode["mix"])[..., None]
    img = base[None, None, :] * (1 - alpha) + mesh * alpha

    # --- 5. large-scale luminance variation for depth ----------------------
    depth = fbm(rng, w, h, octaves=6, base_cells=2)
    img *= (0.88 + 0.26 * depth)[..., None]

    # --- 6. directional light sweep ---------------------------------------
    sweep = np.clip(1.0 - ((xx * 0.7 + yy * 0.3) - 0.28) * 0.85, 0.72, 1.28)
    img *= sweep[..., None]

    # --- 6b. hero light source: one bright core so the frame has a focal point
    hx, hy = rng.uniform(0.18, 0.42), rng.uniform(0.12, 0.38)
    hd = ((xx - hx) * aspect) ** 2 + (yy - hy) ** 2
    core = np.exp(-hd / (2 * 0.30 ** 2)).astype(np.float32)
    img += core[..., None] * 0.16

    img = np.clip(img, 0.0, 1.0)

    # --- 7. neon extras ----------------------------------------------------
    if mode["scanlines"] > 0:
        lines = (np.sin(yy * h * math.pi / 1.5) * 0.5 + 0.5).astype(np.float32)
        img *= (1.0 - mode["scanlines"] * lines)[..., None]
        # chromatic edge lift: push R and B apart slightly in bright regions
        lum = img.mean(axis=2, keepdims=True)
        img[..., 0] = np.clip(img[..., 0] + lum[..., 0] * 0.05, 0, 1)
        img[..., 2] = np.clip(img[..., 2] + lum[..., 0] * 0.07, 0, 1)

    pil = Image.fromarray((np.clip(img, 0, 1) * 255).astype(np.uint8), mode="RGB")

    # --- 8. bloom ----------------------------------------------------------
    radius, strength = mode["bloom"]
    blurred = pil.filter(ImageFilter.GaussianBlur(radius=radius))
    a = np.asarray(pil, dtype=np.float32)
    b = np.asarray(blurred, dtype=np.float32)
    screen = 255.0 - (255.0 - a) * (255.0 - b) / 255.0     # screen blend
    out = a * (1 - strength) + screen * strength

    # --- 9. vignette -------------------------------------------------------
    vx = (xx - 0.5) * 2.0
    vy = (yy - 0.5) * 2.0
    vig = 1.0 - mode["vignette"] * np.clip((vx * vx * 0.85 + vy * vy), 0, 1.6) * 0.72
    out *= vig[..., None]

    # --- 10. grain ---------------------------------------------------------
    if mode["grain"] > 0:
        noise = rng.normal(0.0, mode["grain"], size=(h, w, 1)).astype(np.float32)
        out += noise

    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), mode="RGB")


def average_color(img: Image.Image) -> str:
    """Average colour of an image - used to tint the HA header per background."""
    px = img.resize((1, 1), Image.BOX).getpixel((0, 0))
    return "#%02x%02x%02x" % px


def main() -> None:
    args = [a for a in sys.argv[1:]]
    resume = "--resume" in args
    args = [a for a in args if not a.startswith("--")]
    only_mode = args[0] if args else None
    areas = as_dicts()
    manifest: dict[str, dict[str, str]] = {}

    for mode_name, mode in MODES.items():
        if only_mode and mode_name != only_mode:
            continue
        outdir = os.path.join(OUT_ROOT, mode_name)
        os.makedirs(outdir, exist_ok=True)
        for area in areas:
            path = os.path.join(outdir, f"{area['key']}.webp")
            if resume and os.path.exists(path):
                manifest.setdefault(mode_name, {})[area["key"]] = \
                    average_color(Image.open(path))
                print(f"{mode_name:11s} {area['key']:17s} (kept)")
                continue
            img = render_area(area, mode_name, mode)
            img.save(path, "WEBP", quality=88, method=5)
            size_kb = os.path.getsize(path) / 1024
            manifest.setdefault(mode_name, {})[area["key"]] = average_color(img)
            print(f"{mode_name:11s} {area['key']:17s} {size_kb:7.1f} KB  "
                  f"avg {manifest[mode_name][area['key']]}")

    # Persist average colours so the theme generator can tint headers.
    # Merge rather than overwrite: this script can be run one mode at a time.
    import json
    path = os.path.join(os.path.dirname(OUT_ROOT), "avg-colors.json")
    existing = {}
    if os.path.exists(path):
        try:
            with open(path) as f:
                existing = json.load(f)
        except (ValueError, OSError):
            existing = {}
    existing.update(manifest)
    with open(path, "w") as f:
        json.dump(existing, f, indent=2, sort_keys=True)
    print(f"\nwrote avg-colors.json ({', '.join(sorted(existing))})")


if __name__ == "__main__":
    main()
