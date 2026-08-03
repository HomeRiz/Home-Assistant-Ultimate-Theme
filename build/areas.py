"""
Area registry for the Home Assistant Ultimate Theme.

Each area defines:
  key      -- slug used for filenames and theme names
  name     -- human readable label
  icon     -- mdi icon suggestion for the dashboard tab
  hues     -- the "story" of the room, as HSV hue anchors (0-360) with
              per-blob saturation/value bias. These get re-mapped per mode.
  accent   -- the single colour that drives --primary-color for that area
  seed     -- deterministic RNG seed so regenerating never changes the art
"""

AREAS = [
    # key                name                icon                          hues                         accent      seed
    ("home",            "Home",             "mdi:home",                   [28, 205, 44, 260],          "#FF9F0A", 1001),
    ("living-room",     "Living Room",      "mdi:sofa",                   [22, 340, 40, 12],           "#FF8A5B", 1002),
    ("kitchen",         "Kitchen",          "mdi:silverware-fork-knife",  [35, 18, 50, 8],             "#FFB340", 1003),
    ("bedroom",         "Bedroom",          "mdi:bed",                    [255, 285, 225, 310],        "#9B8CFF", 1004),
    ("master-bedroom",  "Master Bedroom",   "mdi:bed-king",               [285, 320, 260, 340],        "#C77DFF", 1005),
    ("guest",           "Guest",            "mdi:account-heart",          [165, 140, 190, 100],        "#5FD0B0", 1006),
    ("bathroom",        "Bathroom",         "mdi:shower",                 [190, 200, 165, 215],        "#5AC8F5", 1007),
    ("office",          "Office",           "mdi:desk",                   [210, 225, 195, 250],        "#0A84FF", 1008),
    ("ai",              "AI",               "mdi:brain",                  [275, 300, 320, 245],        "#BF5AF2", 1009),
    ("outside",         "Outside",          "mdi:tree",                   [200, 45, 160, 30],          "#4FC3F7", 1010),
    ("hallway",         "Hallway",          "mdi:door-open",              [30, 210, 15, 240],          "#B8A38A", 1011),
    ("garage",          "Garage",           "mdi:garage",                 [215, 25, 200, 35],          "#8FA3B8", 1012),
    ("front-yard",      "Front Yard",       "mdi:home-outline",           [95, 55, 130, 40],           "#8BC34A", 1013),
    ("back-yard",       "Back Yard",        "mdi:grill",                  [110, 25, 85, 15],           "#7CB342", 1014),
    ("electrical-room", "Electrical Room",  "mdi:flash",                  [48, 38, 25, 200],           "#FFD60A", 1015),
    ("technic-room",    "Technic Room",     "mdi:cog",                    [185, 205, 170, 220],        "#6AC4DC", 1016),
    ("garden",          "Garden",           "mdi:flower",                 [105, 85, 130, 60],          "#32D74B", 1017),
    ("energy",          "Energy",           "mdi:lightning-bolt",         [70, 45, 130, 90],           "#B4E33D", 1018),
    ("security",        "Security",         "mdi:shield-home",            [355, 15, 330, 20],          "#FF453A", 1019),
    ("climate",         "Climate",          "mdi:thermostat",             [195, 25, 210, 35],          "#64D2FF", 1020),
    ("media",           "Media",            "mdi:play-circle",            [315, 275, 340, 250],        "#FF375F", 1021),
    ("network",         "Network",          "mdi:lan",                    [205, 185, 230, 165],        "#00C2FF", 1022),
    ("settings",        "Settings",         "mdi:cog-outline",            [220, 240, 200, 260],        "#98989D", 1023),
]

AREA_KEYS = [a[0] for a in AREAS]


def as_dicts():
    keys = ("key", "name", "icon", "hues", "accent", "seed")
    return [dict(zip(keys, a)) for a in AREAS]
