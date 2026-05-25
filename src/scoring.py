# =========================================================
# TIDE LINE — CANONICAL RISK ENGINE
# =========================================================


def calculate_marine_risk(

    marine,
    tides

):

    # =====================================================
    # FAILSAFE
    # =====================================================

    if not marine:

        return {

            "risk_state": "UNKNOWN",

            "danger_score": 0,

            "summary": [

                "Marine intelligence offline."

            ],

            "standing_wave_risk": False,

            "launch_viability": "UNKNOWN",

            "tide_direction": "UNKNOWN",

            "tide_velocity": "UNKNOWN"

        }

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

    advisories = marine.get(
        "advisories",
        []
    )

    # =====================================================
    # EXTRACT VARIABLES
    # =====================================================

    wave_height = sea_state.get(
        "wave_height_ft",
        0
    )

    swell_period = sea_state.get(
        "swell_period_sec",
        0
    )

    swell_direction = sea_state.get(
        "swell_direction",
        "UNKNOWN"
    )

    wind_speed = wind.get(
        "speed_mph",
        0
    )

    wind_direction = wind.get(
        "direction",
        "UNKNOWN"
    )

    tide_direction = current_tide.get(
        "direction",
        "UNKNOWN"
    )

    tide_velocity = current_tide.get(
        "velocity",
        "UNKNOWN"
    )

    # =====================================================
    # INITIALIZE
    # =====================================================

    score = 10

    synthesis = []

    standing_wave_risk = False

    # =====================================================
    # WAVE ENERGY
    # =====================================================

    if wave_height >= 6:

        score += 40

        synthesis.append(
            "Large offshore wave energy detected."
        )

    elif wave_height >= 4:

        score += 25

        synthesis.append(
            "Elevated swell energy impacting inlet."
        )

    elif wave_height >= 2:

        score += 10

        synthesis.append(
            "Moderate wave activity present."
        )

    # =====================================================
    # SWELL PERIOD
    # =====================================================

    if swell_period >= 9:

        score += 20

        synthesis.append(
            "Long-period swell increasing inlet force."
        )

    elif swell_period >= 6:

        score += 10

    # =====================================================
    # TIDE VELOCITY
    # =====================================================

    if (

        tide_direction == "OUTGOING"

        and tide_velocity == "STRONG"

    ):

        score += 20

        synthesis.append(
            "Strong outgoing tidal exchange detected."
        )

    elif tide_velocity == "MODERATE":

        score += 5

    # =====================================================
    # WIND AGAINST TIDE
    # =====================================================

    opposing_wind = wind_direction in [

        "E",
        "SE",
        "NE",
        "ENE",
        "ESE"

    ]

    if (

        tide_direction == "OUTGOING"

        and opposing_wind
        and wind_speed >= 12

    ):

        score += 30

        standing_wave_risk = True

        synthesis.append(
            "Wind-against-tide standing-wave conditions likely."
        )

    # =====================================================
    # SWELL CONFLICT
    # =====================================================

    if (

        tide_direction == "OUTGOING"

        and swell_direction in [

            "E",
            "SE",
            "NE"

        ]

        and swell_period >= 6

    ):

        score += 20

        standing_wave_risk = True

        synthesis.append(
            "Incoming swell conflict detected near inlet mouth."
        )

    # =====================================================
    # NOAA ADVISORIES
    # =====================================================

    if advisories:

        score += 20

        synthesis.append(
            "NOAA marine advisories active."
        )

    # =====================================================
    # FINAL RISK STATE
    # =====================================================

    if score <= 20:

        risk_state = "LOW"

    elif score <= 45:

        risk_state = "MODERATE"

    elif score <= 70:

        risk_state = "HIGH"

    else:

        risk_state = "EXTREME"

    # =====================================================
    # LAUNCH VIABILITY
    # =====================================================

    if standing_wave_risk:

        launch_viability = "DANGEROUS"

    elif (

        tide_direction == "OUTGOING"

        and tide_velocity == "STRONG"

    ):

        launch_viability = "LIMITED"

    elif wind_speed >= 15:

        launch_viability = "CAUTION"

    else:

        launch_viability = "GOOD"

    # =====================================================
    # EMPTY SYNTHESIS
    # =====================================================

    if not synthesis:

        synthesis.append(
            "Marine systems nominal."
        )

    # =====================================================
    # RETURN CANONICAL OBJECT
    # =====================================================

    return {

        "risk_state": risk_state,

        "danger_score": min(
            score,
            100
        ),

        "summary": synthesis,

        "standing_wave_risk": standing_wave_risk,

        "launch_viability": launch_viability,

        "tide_direction": tide_direction,

        "tide_velocity": tide_velocity

    }
