# =========================================================
# TIDE LINE — MAHI TACTICAL ENGINE
# =========================================================

def calculate_mahi_score(

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

    wind = marine.get(
        "wind",
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

    swell_direction = sea_state.get(
        "swell_direction",
        "UNKNOWN"
    )

    wave_height = regional.get(
        "wave_height_ft",
        0
    )

    wave_period = regional.get(
        "wave_period_sec",
        0
    )

    wind_speed = wind.get(
        "speed_mph",
        0
    )

    tide_direction = current_tide.get(
        "direction",
        "UNKNOWN"
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

    mahi_score = 50

    tactical_drivers = []

    # =====================================================
    # SWELL ENERGY
    # =====================================================

    if swell_period >= 6:

        mahi_score += 15

        tactical_drivers.append(
            "Long interval swell improving offshore movement."
        )

    # =====================================================
    # WAVE STRUCTURE
    # =====================================================

    if 1 <= wave_height <= 4:

        mahi_score += 15

        tactical_drivers.append(
            "Moderate offshore sea state favorable."
        )

    elif wave_height > 6:

        mahi_score -= 20

        tactical_drivers.append(
            "Elevated offshore wave energy reducing stability."
        )

    # =====================================================
    # WIND STRUCTURE
    # =====================================================

    if wind_speed <= 12:

        mahi_score += 10

        tactical_drivers.append(
            "Controlled wind supporting weedline formation."
        )

    elif wind_speed > 20:

        mahi_score -= 20

        tactical_drivers.append(
            "Excessive wind disrupting offshore structure."
        )

    # =====================================================
    # SWELL DIRECTION
    # =====================================================

    if swell_direction in [

        "E",
        "SE",
        "SSE",
        "NE"

    ]:

        mahi_score += 10

        tactical_drivers.append(
            "Atlantic current interaction favorable."
        )

    # =====================================================
    # TIDAL MOVEMENT
    # =====================================================

    if tide_direction == "INCOMING":

        mahi_score += 10

        tactical_drivers.append(
            "Incoming tide assisting bait migration."
        )

    # =====================================================
    # OFFSHORE CONDITIONS
    # =====================================================

    if offshore_rating == "GOOD":

        mahi_score += 15

        tactical_drivers.append(
            "Regional offshore conditions stable."
        )

    elif offshore_rating == "DANGEROUS":

        mahi_score -= 25

    # =====================================================
    # RISK PENALTY
    # =====================================================

    if danger_score > 70:

        mahi_score -= 30

    elif danger_score > 40:

        mahi_score -= 10

    # =====================================================
    # WAVE PERIOD BONUS
    # =====================================================

    if wave_period >= 6:

        mahi_score += 5

        tactical_drivers.append(
            "Wave interval spacing improving offshore comfort."
        )

    # =====================================================
    # CLAMP SCORE
    # =====================================================

    mahi_score = max(
        0,
        min(
            100,
            mahi_score
        )
    )

    # =====================================================
    # ACTIVITY CLASSIFICATION
    # =====================================================

    if mahi_score >= 85:

        activity = "RUNNING"

        school_type = "SCHOOLIES + GAFFERS"

    elif mahi_score >= 70:

        activity = "ACTIVE"

        school_type = "SCATTERED PODS"

    else:

        activity = "LOW"

        school_type = "SPARSE"

    # =====================================================
    # RETURN ENGINE
    # =====================================================

    return {

        "species": "MAHI",

        "score": mahi_score,

        "activity": activity,

        "school_type": school_type,

        "recommendation": (
            "Target weedlines, floating debris, "
            "temperature breaks, and current edges."
        ),

        "depth_zone": "OFFSHORE BLUEWATER",

        "best_window": "CURRENT EDGES",

        "peak_season": "APRIL - SEPTEMBER",

        "water_temp": "72F - 82F",

        "techniques": [

            "Trolling",
            "Pitch Baits",
            "Vertical Jigging",
            "Fast Retrieve Presentations"

        ],

        "recommended_baits": [

            "Ballyhoo",
            "Pilchards",
            "Squid",
            "Topwater Poppers"

        ],

        "known_targets": [

            "Weedlines",
            "Floating Debris",
            "Temperature Breaks",
            "Current Rips"

        ],

        "tactical_drivers": tactical_drivers

    }
