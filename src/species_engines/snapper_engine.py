# =========================================================
# TIDE LINE — SNAPPER TACTICAL ENGINE
# =========================================================

def calculate_snapper_score(

    marine,
    tides,
    buoys,
    risk

):

    # =====================================================
    # NORMALIZED CONTRACTS
    # =====================================================

    sea_state = marine.get(
        "sea_state",
        {}
    )

    current_tide = tides.get(
        "current",
        {}
    )

    regional = buoys.get(
        "regional",
        {}
    )

    # =====================================================
    # INPUTS
    # =====================================================

    swell_period = sea_state.get(
        "swell_period_sec",
        0
    )

    wave_height = sea_state.get(
        "wave_height_ft",
        0
    )

    tide_direction = current_tide.get(
        "direction",
        "UNKNOWN"
    )

    tidal_velocity = current_tide.get(
        "velocity",
        "LOW"
    )

    offshore_rating = regional.get(
        "rating",
        "UNKNOWN"
    )

    danger_score = risk.get(
        "danger_score",
        0
    )

    # =====================================================
    # BASE SCORE
    # =====================================================

    score = 50

    tactical_drivers = []

    # =====================================================
    # SWELL ENERGY
    # =====================================================

    if swell_period >= 6:

        score += 15

        tactical_drivers.append(
            "Long-period swell improving reef feeding behavior."
        )

    # =====================================================
    # WAVE HEIGHT
    # =====================================================

    if 1 <= wave_height <= 3:

        score += 10

        tactical_drivers.append(
            "Moderate sea-state supporting stable reef positioning."
        )

    # =====================================================
    # TIDAL FLOW
    # =====================================================

    if tide_direction == "INCOMING":

        score += 20

        tactical_drivers.append(
            "Incoming tide improving reef feeding windows."
        )

    elif tide_direction == "OUTGOING":

        score += 10

    # =====================================================
    # TIDAL VELOCITY
    # =====================================================

    if tidal_velocity == "STRONG":

        score += 15

        tactical_drivers.append(
            "Strong current increasing predator positioning."
        )

    elif tidal_velocity == "MODERATE":

        score += 10

    # =====================================================
    # OFFSHORE CONDITIONS
    # =====================================================

    if offshore_rating == "GOOD":

        score += 10

    elif offshore_rating == "DANGEROUS":

        score -= 15

    # =====================================================
    # RISK PENALTY
    # =====================================================

    if danger_score > 60:

        score -= 25

    elif danger_score > 40:

        score -= 10

    # =====================================================
    # CLAMP SCORE
    # =====================================================

    score = max(
        0,
        min(
            100,
            score
        )
    )

    # =====================================================
    # ACTIVITY STATE
    # =====================================================

    if score >= 85:

        activity = "PRIME"

    elif score >= 70:

        activity = "ACTIVE"

    elif score >= 50:

        activity = "MODERATE"

    else:

        activity = "LOW"

    # =====================================================
    # SPECIES SPECIALIZATION
    # =====================================================

    snapper_profiles = {

        "Mutton Snapper": {

            "peak": "Late Spring - Summer Spawn",

            "depth": "80FT - 220FT",

            "technique": "Live Bait + Slow Drift"

        },

        "Mangrove Snapper": {

            "peak": "Summer Structure Bite",

            "depth": "20FT - 120FT",

            "technique": "Chunking + Vertical Jigging"

        },

        "Yellowtail Snapper": {

            "peak": "Warm Water Current Pushes",

            "depth": "40FT - 180FT",

            "technique": "Chumming + Light Fluorocarbon"

        },

        "Cubera Snapper": {

            "peak": "Heavy Current Feeding Windows",

            "depth": "90FT - 300FT",

            "technique": "Large Live Baits Near Structure"

        }

    }

    # =====================================================
    # RETURN ENGINE
    # =====================================================

    return {

        "species": "SNAPPER",

        "score": score,

        "activity": activity,

        "recommendation": (
            "Target reef edges, wrecks, ledges, "
            "hard bottom transitions, and current seams."
        ),

        "depth_zone": "60FT - 240FT REEF STRUCTURE",

        "best_window": "MOVING WATER",

        "peak_season": "SPRING - FALL",

        "water_temp": "68F - 80F",

        # =================================================
        # TARGET SNAPPPER SPECIES
        # =================================================

        "target_species": [

            "Mutton Snapper",
            "Mangrove Snapper",
            "Yellowtail Snapper",
            "Cubera Snapper"

        ],

        # =================================================
        # SPECIES PROFILES
        # =================================================

        "species_profiles": snapper_profiles,

        # =================================================
        # FISHING METHODS
        # =================================================

        "techniques": [

            "Slow Pitch Jigging",
            "Knocker Rig Live Baiting",
            "Vertical Jigging",
            "Chunking",
            "Deep Drop Bait Fishing"

        ],

        # =================================================
        # BAITS
        # =================================================

        "recommended_baits": [

            "Pilchards",
            "Ballyhoo",
            "Threadfin Herring",
            "Squid",
            "Live Blue Runners"

        ],

        # =================================================
        # ARTIFICIALS
        # =================================================

        "artificials": [

            "Slow Pitch Jigs",
            "Flutter Jigs",
            "Bucktail Jigs",
            "Soft Plastics"

        ],

        # =================================================
        # STRUCTURE TARGETING
        # =================================================

        "known_structure": [

            "Reef Lines",
            "Ledges",
            "Deep Wrecks",
            "Artificial Reefs",
            "Current Breaks"

        ],

        # =================================================
        # TACTICAL NOTES
        # =================================================

        "tactical_drivers": tactical_drivers,

        # =================================================
        # OPERATIONAL NOTES
        # =================================================

        "tactical_notes": [

            "Low-light periods often improve larger snapper activity.",

            "Strong current edges typically improve feeding aggression.",

            "Long fluorocarbon leaders improve pressured reef bites.",

            "Anchoring uptide of structure increases bait presentation quality."

        ]

    }
