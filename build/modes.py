"""
The three aesthetic identities of the Ultimate Theme.

Each mode is a complete visual system. They share one engine (the card-mod glass
layer in template.jinja2) but differ in palette, geometry, blur character and
post-processing.

  glass      -- Heavy blur, large radii, Apple-style system colours, bright
                specular rim. The flagship look.
  velvet -- Muted pastel accents on a deep base, rendered as matte glass. Softer
                blur, muted pastel accents, medium radii.
  neon       -- Near-black cyberpunk. Tight radii, hard accent borders, strong
                outer glow, scanlined backdrop.
"""

# ---------------------------------------------------------------------------
# Shared token block
# ---------------------------------------------------------------------------
def tokens(p: dict) -> dict:
    """HA's --token-rgb-* palette, derived from a mode's colour set."""
    def rgb(h):
        h = h.lstrip("#")
        return ", ".join(str(int(h[i:i + 2], 16)) for i in (0, 2, 4))

    return {
        "--token-rgb-primary": rgb(p["blue-color"]),
        "--token-rgb-black": "0, 0, 0",
        "--token-rgb-white": "255, 255, 255",
        "--token-rgb-purple": rgb(p["purple-color"]),
        "--token-rgb-pink": rgb(p["pink-color"]),
        "--token-rgb-red": rgb(p["red-color"]),
        "--token-rgb-deep-purple": rgb(p["purple-color"]),
        "--token-rgb-indigo": rgb(p["indigo-color"]),
        "--token-rgb-blue": rgb(p["blue-color"]),
        "--token-rgb-light-blue": rgb(p["light-blue-color"]),
        "--token-rgb-cyan": rgb(p["cyan-color"]),
        "--token-rgb-teal": rgb(p["teal-color"]),
        "--token-rgb-green": rgb(p["green-color"]),
        "--token-rgb-light-green": rgb(p["green-color"]),
        "--token-rgb-lime": rgb(p["green-color"]),
        "--token-rgb-yellow": rgb(p["yellow-color"]),
        "--token-rgb-amber": rgb(p["yellow-color"]),
        "--token-rgb-orange": rgb(p["orange-color"]),
        "--token-rgb-deep-orange": rgb(p["orange-color"]),
        "--token-rgb-brown": rgb(p["brown-color"]),
        "--token-rgb-grey": "142, 142, 147",
        "--token-rgb-blue-grey": "120, 130, 145",
        "--token-rgb-state-icon": "255, 255, 255",
        "--token-size-radius-card": "var(--ha-card-border-radius)",
    }


GLASS_PALETTE = {
    "red-color": "#FF453A", "pink-color": "#FF375F", "purple-color": "#BF5AF2",
    "indigo-color": "#5E5CE6", "blue-color": "#0A84FF", "light-blue-color": "#66D4CF",
    "cyan-color": "#5AC8F5", "teal-color": "#6AC4DC", "green-color": "#32D74B",
    "yellow-color": "#FFD60A", "orange-color": "#FF9F0A", "brown-color": "#AC8E68",
    "grey-color": "#8E8E93",
}

# Palette values retained from a third-party colour scheme;
# see NOTICE.md for attribution.
VELVET_PALETTE = {
    "red-color": "#f38ba8", "pink-color": "#f5c2e7", "purple-color": "#cba6f7",
    "indigo-color": "#b4befe", "blue-color": "#89b4fa", "light-blue-color": "#89dceb",
    "cyan-color": "#94e2d5", "teal-color": "#94e2d5", "green-color": "#a6e3a1",
    "yellow-color": "#f9e2af", "orange-color": "#fab387", "brown-color": "#dc8a78",
    "grey-color": "#9399b2",
}

NEON_PALETTE = {
    "red-color": "#FF2D55", "pink-color": "#FF2D9B", "purple-color": "#A855F7",
    "indigo-color": "#6366F1", "blue-color": "#00A3FF", "light-blue-color": "#22D3EE",
    "cyan-color": "#00F0FF", "teal-color": "#14F1C8", "green-color": "#39FF14",
    "yellow-color": "#FFE600", "orange-color": "#FF8A00", "brown-color": "#C08552",
    "grey-color": "#7A8290",
}


MODES = {
    # =====================================================================
    "glass": dict(
        label="Ultimate Glass",
        blur="blur(16px) saturate(1.45)",
        radius="30px",
        badge_radius="24px",
        mush_radius="24px",
        mush_spacing="12px",
        border_width="0px",
        border_color="rgba(255, 255, 255, 0.18)",
        glass_tint="rgba(255, 255, 255, 0.06)",
        sheen=("linear-gradient(160deg, rgba(255,255,255,0.22) 0%, "
               "rgba(255,255,255,0.06) 22%, rgba(255,255,255,0) 45%)"),
        sheen_blend="normal",
        inset_shadow=("3px 3px 0.5px -3.5px rgba(255,255,255,0.35) inset, "
                      "-2px -2px 0.5px -2px rgba(255,255,255,0.30) inset, "
                      "0 0 10px 1px rgba(255,255,255,0.10) inset, "
                      "0 8px 24px -12px rgba(0,0,0,0.55)"),
        hover_glow="0 0 24px -6px var(--ultimate-glow-color)",
        transition="box-shadow 220ms ease, transform 220ms ease",
        background_scrim=("linear-gradient(180deg, rgba(0,0,0,0.12) 0%, "
                          "rgba(0,0,0,0.30) 100%)"),
        fallback_gradient=("center / cover no-repeat fixed "
                           "linear-gradient(140deg, #1b1030 0%, #0b0d14 55%, #12202e 100%)"),
        fallback_card_bg="rgba(40, 42, 52, 0.86)",
        light_primary="rgb(241, 241, 241)",
        divider="rgba(152, 152, 157, 0.28)",
        text_primary="rgba(255, 255, 255, 0.96)",
        text_secondary="rgba(228, 228, 232, 0.78)",
        text_disabled="rgba(208, 208, 208, 0.45)",
        sidebar_bg="rgba(18, 18, 24, 0.55)",
        sidebar_selected_bg="rgba(255, 255, 255, 0.10)",
        header_bg="rgba(18, 18, 24, 0.30)",
        header_edit_bg="rgba(0, 0, 0, 0.35)",
        surface="rgba(32, 32, 40, 0.88)",
        surface_alt="rgba(44, 44, 54, 0.88)",
        surface_rgb="rgb(20, 20, 26)",
        dialog_bg="rgba(30, 30, 38, 0.72)",
        scrim="rgba(0, 0, 0, 0.55)",
        code_bg="rgba(0, 0, 0, 0.45)",
        slider_track="rgba(255, 255, 255, 0.22)",
        hover_fill="rgba(255, 255, 255, 0.12)",
        hover_fill_strong="rgba(255, 255, 255, 0.20)",
        scrollbar="rgba(255, 255, 255, 0.22)",
        palette=GLASS_PALETTE,
        light={
            "primary-background-color": "rgb(70, 74, 80)",
            "secondary-background-color": "rgb(70, 74, 80)",
            "ha-card-background": "rgba(190, 195, 205, 0.26)",
        },
        dark={
            "primary-background-color": "rgb(14, 14, 20)",
            "secondary-background-color": "rgb(14, 14, 20)",
            "ha-card-background": "rgba(0, 0, 0, 0.26)",
        },
    ),
    # =====================================================================
    "velvet": dict(
        label="Ultimate Velvet",
        blur="blur(12px) saturate(1.15)",
        radius="18px",
        badge_radius="14px",
        mush_radius="14px",
        mush_spacing="10px",
        border_width="1px",
        border_color="rgba(205, 214, 244, 0.10)",
        glass_tint="rgba(49, 50, 68, 0.42)",
        sheen=("linear-gradient(160deg, rgba(205,214,244,0.12) 0%, "
               "rgba(205,214,244,0.03) 26%, rgba(205,214,244,0) 50%)"),
        sheen_blend="normal",
        inset_shadow=("0 1px 0 0 rgba(205,214,244,0.10) inset, "
                      "0 0 0 1px rgba(17,17,27,0.35), "
                      "0 10px 26px -14px rgba(0,0,0,0.70)"),
        hover_glow="0 0 20px -8px var(--ultimate-glow-color)",
        transition="box-shadow 200ms ease, transform 200ms ease",
        background_scrim=("linear-gradient(180deg, rgba(17,17,27,0.28) 0%, "
                          "rgba(17,17,27,0.48) 100%)"),
        fallback_gradient=("center / cover no-repeat fixed "
                           "linear-gradient(140deg, #313244 0%, #1e1e2e 55%, #181825 100%)"),
        fallback_card_bg="rgba(49, 50, 68, 0.92)",
        light_primary="#cdd6f4",
        divider="rgba(147, 153, 178, 0.24)",
        text_primary="#cdd6f4",
        text_secondary="#a6adc8",
        text_disabled="rgba(127, 132, 156, 0.65)",
        sidebar_bg="rgba(24, 24, 37, 0.62)",
        sidebar_selected_bg="rgba(49, 50, 68, 0.85)",
        header_bg="rgba(24, 24, 37, 0.38)",
        header_edit_bg="rgba(17, 17, 27, 0.70)",
        surface="rgba(49, 50, 68, 0.92)",
        surface_alt="rgba(69, 71, 90, 0.92)",
        surface_rgb="rgb(30, 30, 46)",
        dialog_bg="rgba(30, 30, 46, 0.80)",
        scrim="rgba(17, 17, 27, 0.62)",
        code_bg="rgba(17, 17, 27, 0.70)",
        slider_track="rgba(205, 214, 244, 0.20)",
        hover_fill="rgba(205, 214, 244, 0.10)",
        hover_fill_strong="rgba(205, 214, 244, 0.18)",
        scrollbar="rgba(147, 153, 178, 0.35)",
        palette=VELVET_PALETTE,
        light={
            "primary-background-color": "#585b70",
            "secondary-background-color": "#585b70",
            "ha-card-background": "rgba(88, 91, 112, 0.42)",
        },
        dark={
            "primary-background-color": "#1e1e2e",
            "secondary-background-color": "#181825",
            "ha-card-background": "rgba(30, 30, 46, 0.42)",
        },
    ),
    # =====================================================================
    "neon": dict(
        label="Ultimate Neon",
        blur="blur(10px) saturate(1.8) brightness(0.92)",
        radius="12px",
        badge_radius="8px",
        mush_radius="8px",
        mush_spacing="8px",
        border_width="1px",
        border_color="color-mix(in srgb, var(--ultimate-glow-color) 45%, transparent)",
        glass_tint="rgba(6, 8, 16, 0.55)",
        sheen=("linear-gradient(180deg, "
               "color-mix(in srgb, var(--ultimate-glow-color) 22%, transparent) 0%, "
               "rgba(255,255,255,0.02) 2px, rgba(255,255,255,0) 40%)"),
        sheen_blend="screen",
        inset_shadow=("0 0 0 1px color-mix(in srgb, var(--ultimate-glow-color) 30%, transparent), "
                      "0 0 18px -6px color-mix(in srgb, var(--ultimate-glow-color) 55%, transparent), "
                      "0 0 40px -20px color-mix(in srgb, var(--ultimate-glow-color) 80%, transparent) inset, "
                      "0 10px 30px -16px rgba(0,0,0,0.90)"),
        hover_glow="0 0 30px -4px var(--ultimate-glow-color)",
        transition="box-shadow 160ms ease, transform 160ms ease, border-color 160ms ease",
        background_scrim=("radial-gradient(120% 90% at 50% 0%, rgba(0,0,0,0.10) 0%, "
                          "rgba(0,0,0,0.55) 70%, rgba(0,0,0,0.78) 100%)"),
        fallback_gradient=("center / cover no-repeat fixed "
                           "linear-gradient(140deg, #12002b 0%, #04050a 55%, #001a2b 100%)"),
        fallback_card_bg="rgba(10, 12, 22, 0.94)",
        light_primary="#E6F1FF",
        divider="color-mix(in srgb, var(--ultimate-glow-color) 28%, transparent)",
        text_primary="rgba(233, 243, 255, 0.97)",
        text_secondary="rgba(160, 176, 200, 0.85)",
        text_disabled="rgba(110, 122, 142, 0.55)",
        sidebar_bg="rgba(4, 5, 10, 0.72)",
        sidebar_selected_bg="color-mix(in srgb, var(--ultimate-glow-color) 18%, transparent)",
        header_bg="rgba(4, 5, 10, 0.42)",
        header_edit_bg="rgba(0, 0, 0, 0.80)",
        surface="rgba(10, 12, 22, 0.94)",
        surface_alt="rgba(18, 21, 34, 0.94)",
        surface_rgb="rgb(6, 8, 16)",
        dialog_bg="rgba(8, 10, 20, 0.86)",
        scrim="rgba(0, 0, 0, 0.78)",
        code_bg="rgba(0, 0, 0, 0.70)",
        slider_track="rgba(160, 176, 200, 0.20)",
        hover_fill="color-mix(in srgb, var(--ultimate-glow-color) 14%, transparent)",
        hover_fill_strong="color-mix(in srgb, var(--ultimate-glow-color) 26%, transparent)",
        scrollbar="color-mix(in srgb, var(--ultimate-glow-color) 40%, transparent)",
        palette=NEON_PALETTE,
        light={
            "primary-background-color": "rgb(24, 27, 38)",
            "secondary-background-color": "rgb(24, 27, 38)",
            "ha-card-background": "rgba(24, 27, 38, 0.55)",
        },
        dark={
            "primary-background-color": "rgb(4, 5, 10)",
            "secondary-background-color": "rgb(4, 5, 10)",
            "ha-card-background": "rgba(6, 8, 16, 0.52)",
        },
    ),
}

# ---------------------------------------------------------------------------
# Additional aesthetics
# ---------------------------------------------------------------------------
# These are worlds, not engines. Glass, Velvet and Neon each define a way cards
# behave - blur character, radii, border language. An anime or Art Deco theme
# does not need its own answer to "how round is a card"; it needs its own
# artwork. So each of these borrows the engine that suits its material and
# brings only a label and a folder of backgrounds.
#
# The pairing is about surface, not subject:
#   Glass   - clean, luminous, heavy blur
#   Velvet  - matte, soft, low contrast
#   Neon    - hard contrast, tight radii, accent borders
ENGINE_OF = {
    "ionut":         "glass",    # flat graphic artwork, luminous card treatment
    "cyberprep":     "glass",    # chrome and clean light
    "solarpunk":     "velvet",   # organic, diffuse, warm
    "dark-academia": "velvet",   # candlelit, matte, chiaroscuro
    "cottagecore":   "velvet",   # soft, unhurried, nothing glossy
    "cyberpunk":     "neon",     # signage, glow, hard contrast
    "synthwave":     "neon",     # grid, banded sun, chromatic fringe
    "art-deco":      "neon",     # precise geometry - but see below
}

LABELS = {
    "ionut":         "Ultimate Ionut",
    "cyberprep":     "Ultimate Cyberprep",
    "cyberpunk":     "Ultimate Cyberpunk",
    "solarpunk":     "Ultimate Solarpunk",
    "art-deco":      "Ultimate Art Deco",
    "dark-academia": "Ultimate Dark Academia",
    "cottagecore":   "Ultimate Cottagecore",
    "synthwave":     "Ultimate Synthwave",
}

for _key, _engine in ENGINE_OF.items():
    _m = dict(MODES[_engine])
    _m["label"] = LABELS[_key]

    if _key == "art-deco":
        # Deco wants Neon's geometry and none of its glow. Brass reflects, it
        # does not emit - a glowing border reads as neon signage, which is the
        # one thing this aesthetic is not. Hairline metal instead, and a
        # shadow-only hover.
        _m["border_color"] = "rgba(201, 162, 39, 0.55)"
        _m["hover_glow"] = "0 10px 28px -14px rgba(0, 0, 0, 0.75)"
        _m["sheen"] = ("linear-gradient(160deg, rgba(201,162,39,0.20) 0%, "
                       "rgba(201,162,39,0.05) 24%, rgba(201,162,39,0) 46%)")

    MODES[_key] = _m


_BG_SHORTHAND_PREFIX = "center / cover no-repeat fixed "

for _m in MODES.values():
    _m["tokens"] = tokens(_m["palette"])

    # `fallback_gradient` is a `background:` shorthand, so it cannot be used as
    # a `background-image` value - the declaration would simply be dropped.
    # Several card-mod blocks paint the backdrop via `background-image`, so keep
    # an image-only form of the same gradient alongside it.
    _fg = _m["fallback_gradient"]
    assert _fg.startswith(_BG_SHORTHAND_PREFIX), _fg
    _m["fallback_image"] = _fg[len(_BG_SHORTHAND_PREFIX):]


# ---------------------------------------------------------------------------
# Accent adaptation
# ---------------------------------------------------------------------------
# Each area carries one accent colour, chosen against the Glass palette. Using
# it verbatim in the other two modes is wrong: a bright Apple green is off-spec
# in Velvet and too dull for Neon. Each mode re-expresses the area's hue in
# its own colour language, so the area stays recognisable while the mode stays
# internally consistent.

_VELVET_ACCENTS = [
    "#f5e0dc", "#f2cdcd", "#f5c2e7", "#cba6f7", "#f38ba8", "#eba0ac",
    "#fab387", "#f9e2af", "#a6e3a1", "#94e2d5", "#89dceb", "#74c7ec",
    "#89b4fa", "#b4befe",
]


def _hex_to_rgb01(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def _rgb01_to_hex(rgb):
    return "#%02X%02X%02X" % tuple(
        max(0, min(255, int(round(c * 255)))) for c in rgb)


def accent_for_mode(accent_hex: str, mode_name: str) -> str:
    """Re-express a colour accent in the target mode's colour language."""
    import colorsys

    # An aesthetic that borrows an engine borrows its accent treatment too.
    mode_name = ENGINE_OF.get(mode_name, mode_name)

    if mode_name == "glass":
        return accent_hex

    h, s, v = colorsys.rgb_to_hsv(*_hex_to_rgb01(accent_hex))

    if mode_name == "velvet":
        # snap to the nearest on-palette Velvet accent by hue distance
        best, best_d = accent_hex, 1e9
        for cand in _VELVET_ACCENTS:
            ch = colorsys.rgb_to_hsv(*_hex_to_rgb01(cand))[0]
            d = min(abs(ch - h), 1 - abs(ch - h))
            if d < best_d:
                best_d, best = d, cand
        return best.upper()

    if mode_name == "neon":
        # push to high chroma and full value — neon accents must glow
        return _rgb01_to_hex(colorsys.hsv_to_rgb(h, max(0.78, min(1.0, s * 1.35)), 1.0))

    return accent_hex
