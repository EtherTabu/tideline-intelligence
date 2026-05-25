# =====================================================
# TIDE LINE — TACTICAL INTELLIGENCE ENGINE
# =====================================================

def build_tactical_intelligence(

    marine,
    tides,
    telemetry,
    risk,
    prediction

):

    # =================================================
    # NORMALIZED CONTRACTS
    # =================================================

    sea_state = marine.get(
        "sea_state",
        {}
    )

    current_tide = tides.get(
        "current",
        {}
    )

    regional = telemetry.get(
        "regional",
        {}
    )

    # =================================================
    # SEA STATE
    # =================================================

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

    # =================================================
    # TIDE STATE
    # =================================================

    tide_direction = current_tide.get(
        "direction",
        "UNKNOWN"
    )

    tide_velocity = current_tide.get(
        "velocity",
        "UNKNOWN"
    )

    # =================================================
    # REGIONAL TELEMETRY
    # =================================================

    offshore_rating = regional.get(
        "rating",
        "UNKNOWN"
    )

    # =================================================
    # RISK ENGINE
    # =================================================

    danger_score = risk.get(
        "danger_score",
        0
    )

    risk_state = risk.get(
        "risk_state",
        "UNKNOWN"
    )

    launch_viability = risk.get(
        "launch_viability",
        "UNKNOWN"
    )

    # =================================================
    # PREDICTION ENGINE
    # =================================================

    feeding_score = prediction.get(
        "feeding_score",
        0
    )

    activity = prediction.get(
        "activity",
        "LOW"
    )

    primary_target = prediction.get(
        "primary_target",
        "UNKNOWN"
    )

    primary_score = prediction.get(
        "primary_score",
        0
    )

    # =================================================
    # MISSION STATUS ENGINE
    # =================================================

    if (

        feeding_score >= 80

        and danger_score <= 25

        and launch_viability == "GOOD"

    ):

        mission_status = "PRIME"

        confidence = 92

    elif (

        feeding_score >= 60

        and danger_score <= 55

    ):

        mission_status = "MONITOR"

        confidence = 74

    else:

        mission_status = "HIGH RISK"

        confidence = 48

    # =================================================
    # TRAFFIC ENGINE
    # =================================================

    if mission_status == "PRIME":

        traffic_level = "HIGH"

    elif mission_status == "MONITOR":

        traffic_level = "MODERATE"

    else:

        traffic_level = "LOW"

    # =================================================
    # FEEDING WINDOW ENGINE
    # =================================================

    if tide_direction == "INCOMING":

        feeding_window = (
            "Incoming Tide Feeding Window"
        )

    elif tide_direction == "OUTGOING":

        feeding_window = (
            "Outgoing Tide Edge Window"
        )

    else:

        feeding_window = (
            "Slack Tide Transition"
        )

    # =================================================
    # ALERT ENGINE
    # =================================================

    alerts = []

    if danger_score >= 70:

        alerts.append(
            "Extreme marine instability detected."
        )

    elif danger_score >= 45:

        alerts.append(
            "Moderate marine operating risk detected."
        )

    if wave_height >= 5:

        alerts.append(
            "Elevated offshore wave energy present."
        )

    if swell_period >= 9:

        alerts.append(
            "Long-period swell compression risk active."
        )

    if launch_viability == "DANGEROUS":

        alerts.append(
            "Standing-wave launch conditions possible."
        )

    if offshore_rating == "DANGEROUS":

        alerts.append(
            "Regional offshore telemetry degraded."
        )

    if not alerts:

        alerts.append(
            "No major tactical threats detected."
        )

    # =================================================
    # BAIT ACTIVITY ENGINE
    # =================================================

    bait_activity = []

    if tide_direction == "INCOMING":

        bait_activity.append(
            "Incoming tide supporting bait movement."
        )

    if activity in [

        "HIGH",
        "EXTREME",
        "ACTIVE",
        "RUNNING"

    ]:

        bait_activity.append(
            "Predator staging conditions favorable."
        )

    if wave_height <= 2:

        bait_activity.append(
            "Clean nearshore visibility detected."
        )

    # =================================================
    # STRIKE WINDOW ENGINE
    # =================================================

    strike_windows = [

        {

            "window": "05:30 - 08:30",

            "confidence": primary_score

        },

        {

            "window": "11:00 - 13:00",

            "confidence": max(
                primary_score - 8,
                0
            )

        },

        {

            "window": "16:00 - 18:30",

            "confidence": max(
                primary_score - 5,
                0
            )

        }

    ]

    # =================================================
    # SUMMARY ENGINE
    # =================================================

    summary = (

        f"{activity} feeding activity detected. "
        f"{tide_direction} tidal flow interacting "
        f"with {wave_height} ft sea state. "
        f"Operational target priority favoring "
        f"{primary_target}."

    )

    # =================================================
    # SYSTEM HEALTH ENGINE
    # =================================================

    system_health = {

        "noaa": "ONLINE",

        "telemetry": "ONLINE",

        "buoys": "ONLINE",

        "prediction": "ACTIVE"

    }

    # =================================================
    # FINAL SYNTHESIS
    # =================================================

    return {

        "mission_status": mission_status,

        "confidence": confidence,

        "primary_target": primary_target,

        "primary_score": primary_score,

        "traffic_level": traffic_level,

        "launch_viability": launch_viability,

        "feeding_window": feeding_window,

        "alerts": alerts,

        "bait_activity": bait_activity,

        "strike_windows": strike_windows,

        "summary": summary,

        "system_health": system_health,

        "risk_state": risk_state

    }
