# =========================================================
# TIDE LINE — TACTICAL BRIEF ENGINE
# =========================================================

def build_tactical_brief(

    marine,
    inlet,
    prediction,
    tactical

):

    # =====================================================
    # EXTRACT
    # =====================================================

    mission_status = tactical.get(
        "mission_status",
        "MONITOR"
    )

    target = tactical.get(
        "primary_target",
        "UNKNOWN"
    )

    confidence = tactical.get(
        "confidence",
        0
    )

    active_window = prediction.get(
        "active_window",
        "UNKNOWN"
    )

    inlet_risk = inlet.get(
        "risk",
        "UNKNOWN"
    )

    recommendation = inlet.get(
        "recommendation",
        "No recommendation."
    )

    wave_height = marine.get(
        "wave_height",
        0
    )

    wind_speed = marine.get(
        "wind_speed",
        0
    )

    # =====================================================
    # DECISION ENGINE
    # =====================================================

    if inlet_risk == "HIGH":

        operational_state = (
            "DELAY LAUNCH"
        )

    elif confidence >= 80:

        operational_state = (
            "PRIME STRIKE CONDITIONS"
        )

    else:

        operational_state = (
            "MODERATE OPPORTUNITY"
        )

    # =====================================================
    # BUILD BRIEF
    # =====================================================

    brief = {

        "mission_status":
            mission_status,

        "operational_state":
            operational_state,

        "target":
            target,

        "confidence":
            confidence,

        "active_window":
            active_window,

        "inlet_risk":
            inlet_risk,

        "recommendation":
            recommendation,

        "wave_height":
            wave_height,

        "wind_speed":
            wind_speed

    }

    return brief
