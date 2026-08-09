"""
Colour registry for the Home Assistant Ultimate Theme.

Each entry defines:
  key      -- slug used for filenames and theme names
  name     -- human readable label
  icon     -- mdi icon suggestion for the dashboard tab
  hues     -- the palette's "story", as HSV hue anchors (0-360) with
              per-blob saturation/value bias. These get re-mapped per mode.
  accent   -- the single colour that drives --primary-color
  seed     -- deterministic RNG seed so regenerating never changes the art

These used to be rooms - Kitchen, Office, Security. That reads oddly in a
theme picker: nobody has exactly these rooms, and the thing that actually
distinguishes one entry from another is its colour, not its label. Naming them
by colour also exposed a problem the room names had been hiding - the set had
six blues and five greens, because that is how the rooms happened to fall.

So this list is the spectrum instead: fourteen anchors roughly 25-30 degrees
apart, plus two neutrals. The nine that went are the ones that sat within about
20 degrees of a survivor. Their artwork is still in drop-in/ if any of them ever
earns its place back.

Order is spectral, not alphabetical, so the theme picker reads as a gradient.
"""

AREAS = [
    # key         name         icon                         hues                     accent      seed
    ("ember",    "Ember",     "mdi:fire",                  [355, 15, 330, 20],      "#FF453A", 1019),
    ("rose",     "Rose",      "mdi:flower",                [315, 275, 340, 250],    "#FF375F", 1021),
    ("amber",    "Amber",     "mdi:weather-sunset",        [28, 205, 44, 260],      "#FF9F0A", 1001),
    ("citrine",  "Citrine",   "mdi:white-balance-sunny",   [48, 38, 25, 200],       "#FFD60A", 1015),
    ("lime",     "Lime",      "mdi:leaf",                  [70, 45, 130, 90],       "#B4E33D", 1018),
    ("verdant",  "Verdant",   "mdi:sprout",                [105, 85, 130, 60],      "#32D74B", 1017),
    ("jade",     "Jade",      "mdi:diamond-stone",         [165, 140, 190, 100],    "#5FD0B0", 1006),
    ("lagoon",   "Lagoon",    "mdi:waves",                 [190, 200, 165, 215],    "#5AC8F5", 1007),
    ("azure",    "Azure",     "mdi:water",                 [205, 185, 230, 165],    "#00C2FF", 1022),
    ("cobalt",   "Cobalt",    "mdi:hexagon",               [210, 225, 195, 250],    "#0A84FF", 1008),
    ("indigo",   "Indigo",    "mdi:weather-night",         [255, 285, 225, 310],    "#9B8CFF", 1004),
    ("violet",   "Violet",    "mdi:shimmer",               [275, 300, 320, 245],    "#BF5AF2", 1009),
    ("sand",     "Sand",      "mdi:beach",                 [30, 210, 15, 240],      "#B8A38A", 1011),
    ("graphite", "Graphite",  "mdi:circle-slice-8",        [220, 240, 200, 260],    "#98989D", 1023),
]

# Where each colour came from, when this was still a list of rooms. Kept because
# the artwork on disk was generated under the old key and the migration script
# needs the mapping - and because it explains the seeds above, which are
# deliberately unchanged so regenerating produces the same art.
RENAMED_FROM = {
    "ember": "security",
    "rose": "media",
    "amber": "home",
    "citrine": "electrical-room",
    "lime": "energy",
    "verdant": "garden",
    "jade": "guest",
    "lagoon": "bathroom",
    "azure": "network",
    "cobalt": "office",
    "indigo": "bedroom",
    "violet": "ai",
    "sand": "hallway",
    "graphite": "settings",
}

# Dropped in the same pass, each within ~20 degrees of a survivor. Listed so the
# reason is recoverable later, and so nobody wonders where the files went.
RETIRED = {
    "living-room":    "within 15 degrees of amber",
    "kitchen":        "within 15 degrees of amber",
    "master-bedroom": "within 20 degrees of violet",
    "outside":        "between lagoon and azure",
    "front-yard":     "within 20 degrees of verdant",
    "back-yard":      "within 20 degrees of verdant",
    "technic-room":   "between jade and lagoon",
    "climate":        "within 15 degrees of lagoon",
    "garage":         "cool neutral, covered by graphite",
}

AREA_KEYS = [a[0] for a in AREAS]


def as_dicts():
    keys = ("key", "name", "icon", "hues", "accent", "seed")
    return [dict(zip(keys, a)) for a in AREAS]
