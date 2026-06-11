# =========================================================
# TIDE LINE — FISH PREDICTION ENGINE
# =========================================================

from src.config.species_registry import (
    run_species_engines
)

from src.config.debug import DEBUG_MODE


# =========================================================
# MASTER PREDICTION ENGINE
# =========================================================

def generate_fish_prediction(

    marine,
    tides,
    buoys,
    risk

):

    # =====================================================
    # NORMALIZED CONTRACT ACCESS
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
    # SAFE INPUT PARSING
    # =====================================================

    wave_height = safe_float(

        sea_state.get(
            "wave_height_ft",
            0
        )

    )

    swell_period = safe_float(

        sea_state.get(
            "swell_period_sec",
            0
        )

    )

    tide_direction = str(

        current_tide.get(
            "direction",
            "UNKNOWN"
        )

    ).upper()

    tidal_velocity = str(

        current_tide.get(
            "velocity",
            "LOW"
        )

    ).upper()

    offshore_rating = str(

        regional.get(
            "rating",
            "UNKNOWN"
        )

    ).upper()

    danger_score = safe_int(

        risk.get(
            "danger_score",
            0
        )

    )

    # =====================================================
    # BASE FEEDING SCORE
    # =====================================================

    feeding_score = 50

    tactical_reasons = []

    # =====================================================
    # SWELL ENERGY
    # =====================================================

    if swell_period >= 7:

        feeding_score += 15

        tactical_reasons.append(
            "Long-period swell increasing feeding energy."
        )

    elif swell_period >= 5:

        feeding_score += 10

        tactical_reasons.append(
            "Moderate swell interval supporting bait movement."
        )

    # =====================================================
    # WAVE HEIGHT
    # =====================================================

    if 1 <= wave_height <= 3:

        feeding_score += 15

        tactical_reasons.append(
            "Clean manageable sea state detected."
        )

    elif wave_height > 5:

        feeding_score -= 15

        tactical_reasons.append(
            "Elevated wave state reducing fishability."
        )

    # =====================================================
    # TIDE FLOW
    # =====================================================

    if tide_direction == "INCOMING":

        feeding_score += 15

        tactical_reasons.append(
            "Incoming tide concentrating bait."
        )

    elif tide_direction == "OUTGOING":

        feeding_score += 10

        tactical_reasons.append(
            "Outgoing tide creating ambush lanes."
        )

    # =====================================================
    # CURRENT VELOCITY
    # =====================================================

    if tidal_velocity == "MODERATE":

        feeding_score += 15

        tactical_reasons.append(
            "Moderate current optimizing feeding windows."
        )

    elif tidal_velocity == "STRONG":

        feeding_score += 10

        tactical_reasons.append(
            "Strong current improving predator staging."
        )

    # =====================================================
    # OFFSHORE CONDITIONS
    # =====================================================

    if offshore_rating == "GOOD":

        feeding_score += 10

        tactical_reasons.append(
            "Regional offshore telemetry favorable."
        )

    elif offshore_rating == "DANGEROUS":

        feeding_score -= 20

        tactical_reasons.append(
            "Regional offshore conditions elevated risk."
        )

    # =====================================================
    # RISK PENALTY
    # =====================================================

    if danger_score > 70:

        feeding_score -= 25

        tactical_reasons.append(
            "Extreme marine risk reducing viability."
        )

    elif danger_score > 40:

        feeding_score -= 10

        tactical_reasons.append(
            "Moderate marine risk detected."
        )

    # =====================================================
    # SCORE CLAMP
    # =====================================================

    feeding_score = max(
        0,
        min(
            100,
            feeding_score
        )
    )

    # =====================================================
    # ACTIVITY CLASSIFICATION
    # =====================================================

    activity, bite_window, recommendation = (

        classify_activity(
            feeding_score
        )

    )

    # =====================================================
    # SPECIES REGISTRY
    # =====================================================

    raw_species_registry = run_species_engines(

        marine,
        tides,
        buoys,
        risk

    ) or {}

    species_registry = {}

    if isinstance(
        raw_species_registry,
        dict
    ):

        for key, value in raw_species_registry.items():

            if not isinstance(value, dict):

                continue

            if "score" not in value:

                continue

            species_registry[key] = value

    # =====================================================
    # PRIMARY TARGET ENGINE
    # =====================================================

    primary_target = "UNKNOWN"

    primary_score = 0

    if species_registry:

        sorted_species = sorted(

            species_registry.items(),

            key=lambda item:

            int(
                item[1].get(
                    "score",
                    0
                )
            ),

            reverse=True

        )

        top_species = sorted_species[0][1]

        primary_target = top_species.get(
            "species",
            "UNKNOWN"
        )

        primary_score = int(

            top_species.get(
                "score",
                0
            )

        )

    # =====================================================
    # STRIKE WINDOWS
    # =====================================================

    strike_windows = build_strike_windows(
        activity
    )

    # =====================================================
    # DEBUG
    # =====================================================

    if DEBUG_MODE:

        print(
            f"[PREDICTION] "
            f"{activity} | "
            f"{feeding_score}"
        )

    # =====================================================
    # RETURN ENGINE
    # =====================================================

    return {

        "feeding_score": feeding_score,

        "activity": activity,

        "bite_window": bite_window,

        "recommendation": recommendation,

        "tactical_reasons": tactical_reasons,

        "species": species_registry,

        "primary_target": primary_target,

        "primary_score": primary_score,

        "strike_windows": strike_windows

    }


# =========================================================
# ACTIVITY CLASSIFIER
# =========================================================

def classify_activity(score):

    if score >= 85:

        return (

            "EXTREME",

            "MAJOR FEEDING WINDOW",

            (
                "Aggressive predator activity expected "
                "near tidal transitions and structure."
            )

        )

    elif score >= 70:

        return (

            "HIGH",

            "ACTIVE FEEDING",

            (
                "Strong feeding probability detected."
            )

        )

    elif score >= 50:

        return (

            "MODERATE",

            "TRANSITION WINDOW",

            (
                "Moderate fish activity expected."
            )

        )

    return (

        "LOW",

        "LOW ACTIVITY",

        (
            "Weak feeding conditions detected."
        )

    )


# =========================================================
# STRIKE WINDOWS
# =========================================================

def build_strike_windows(activity):

    if activity == "EXTREME":

        return [

            {
                "window": "SUNRISE",
                "confidence": 96
            },

            {
                "window": "TIDE SWITCH",
                "confidence": 93
            },

            {
                "window": "LATE AFTERNOON",
                "confidence": 88
            }

        ]

    elif activity == "HIGH":

        return [

            {
                "window": "EARLY MORNING",
                "confidence": 82
            },

            {
                "window": "MOVING WATER",
                "confidence": 79
            }

        ]

    return [

        {
            "window": "OPPORTUNISTIC",
            "confidence": 55
        }

    ]


# =========================================================
# SAFE HELPERS
# =========================================================

def safe_float(value):

    try:

        return float(value or 0)

    except:

        return 0.0


def safe_int(value):

    try:

        return int(value or 0)

    except:

        return 0