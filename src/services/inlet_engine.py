# =========================================================
# TIDE LINE — INLET ENGINE
# =========================================================

# =========================================================
# INLET STATUS ENGINE
# =========================================================

def analyze_inlet_conditions(marine):

    wind_speed = marine.get(
        "wind_speed",
        0
    )

    wind_direction = marine.get(
        "wind_direction",
        0
    )

    wave_height = marine.get(
        "wave_height",
        0
    )

    wave_period = marine.get(
        "wave_period",
        0
    )

    tide_state = marine.get(
        "tide_state",
        "UNKNOWN"
    )

    # =====================================================
    # BASELINE
    # =====================================================

    risk = "LOW"

    recommendation = (
        "Safe operational conditions."
    )

    stacking = False

    small_craft_safe = True

    # =====================================================
    # WAVE HEIGHT
    # =====================================================

    if wave_height >= 5:

        risk = "HIGH"

        recommendation = (
            "Heavy swell activity detected."
        )

        small_craft_safe = False

    elif wave_height >= 3:

        risk = "MODERATE"

        recommendation = (
            "Moderate swell conditions."
        )

    # =====================================================
    # OUTGOING TIDE CONFLICT
    # =====================================================

    if (

        tide_state == "Outgoing"

        and wave_height >= 3

    ):

        stacking = True

        risk = "HIGH"

        recommendation = (
            "Outgoing tide swell stacking risk."
        )

        small_craft_safe = False

    # =====================================================
    # WIND AGAINST CURRENT
    # =====================================================

    east_wind = (

        wind_direction >= 45

        and wind_direction <= 135

    )

    if east_wind and tide_state == "Outgoing":

        stacking = True

        risk = "HIGH"

        recommendation = (
            "Wind-against-current inlet hazard."
        )

        small_craft_safe = False

    # =====================================================
    # SHORT PERIOD
    # =====================================================

    if wave_period <= 5 and wave_height >= 3:

        risk = "HIGH"

        recommendation = (
            "Short interval breaking wave risk."
        )

    # =====================================================
    # RETURN
    # =====================================================

    return {

        "risk": risk,

        "stacking": stacking,

        "small_craft_safe":
            small_craft_safe,

        "recommendation":
            recommendation,

        "wave_height":
            wave_height,

        "wave_period":
            wave_period,

        "wind_speed":
            wind_speed,

        "wind_direction":
            wind_direction,

        "tide_state":
            tide_state

    }
