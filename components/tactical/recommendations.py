import streamlit as st


# =========================================================
# STANDING WAVE DETECTION
# =========================================================

def detect_standing_wave_risk(
    tide_direction,
    swell_direction,
    swell_period,
    wave_height
):

    return (
        tide_direction == "OUTGOING"
        and swell_direction in ["E", "SE", "NE"]
        and swell_period >= 8
        and wave_height >= 3
    )


# =========================================================
# DETERMINE LAUNCH WINDOW
# =========================================================

def determine_launch_window(
    risk,
    tide_velocity,
    standing_wave
):

    if standing_wave:
        return (
            "Delay outbound transit until "
            "tidal exchange weakens."
        )

    if risk == "EXTREME":
        return (
            "No safe launch window currently detected."
        )

    if risk == "HIGH":
        return (
            "Use caution during peak tidal movement."
        )

    if tide_velocity == "STRONG":
        return (
            "Prefer launch near slack tide transition."
        )

    return (
        "Current launch conditions appear favorable."
    )


# =========================================================
# STATUS COLOR
# =========================================================

def render_status_banner(risk, standing_wave):

    if standing_wave:
        st.error(
            "Standing-wave probability elevated."
        )

    elif risk == "EXTREME":
        st.error(
            "Unsafe marine operating conditions."
        )

    elif risk == "HIGH":
        st.warning(
            "Elevated inlet turbulence detected."
        )

    else:
        st.success(
            "Marine conditions currently stable."
        )


# =========================================================
# MAIN ENGINE
# =========================================================

def show_recommendations(system):

    st.markdown(
        "## Operational Recommendation Engine"
    )

    if not system:

        st.error(
            "Marine synthesis engine unavailable."
        )

        return

    # =====================================================
    # MASTER OBJECTS
    # =====================================================

    marine = system.get("marine", {})
    tides = system.get("tides", {})
    risk_engine = system.get("risk", {})
    prediction = system.get("prediction", {})

    # =====================================================
    # INPUTS
    # =====================================================

    risk = risk_engine.get(
        "risk",
        "LOW"
    )

    danger_score = risk_engine.get(
        "danger_score",
        0
    )

    tide_direction = tides.get(
        "tide_flow",
        "UNKNOWN"
    )

    tide_velocity = tides.get(
        "velocity",
        "UNKNOWN"
    )

    swell_direction = marine.get(
        "swell_direction",
        "UNKNOWN"
    )

    swell_period = marine.get(
        "swell_period",
        0
    )

    wave_height = marine.get(
        "wave_height",
        0
    )

    feeding_score = prediction.get(
        "feeding_score",
        0
    )

    activity = prediction.get(
        "activity",
        "LOW"
    )

    bite_window = prediction.get(
        "bite_window",
        "UNKNOWN"
    )

    recommendation = prediction.get(
        "recommendation",
        "No tactical recommendation available."
    )

    # =====================================================
    # DETECTION
    # =====================================================

    standing_wave = detect_standing_wave_risk(
        tide_direction,
        swell_direction,
        swell_period,
        wave_height
    )

    launch_window = determine_launch_window(
        risk,
        tide_velocity,
        standing_wave
    )

    # =====================================================
    # STATUS
    # =====================================================

    render_status_banner(
        risk,
        standing_wave
    )

    st.divider()

    # =====================================================
    # MAIN GRID
    # =====================================================

    left, center, right = st.columns([1, 2, 1])

    # =====================================================
    # LEFT
    # =====================================================

    with left:

        st.metric(
            "Risk",
            risk
        )

        st.metric(
            "Danger Score",
            f"{danger_score}/100"
        )

        st.metric(
            "Wave Height",
            f"{wave_height} ft"
        )

        st.metric(
            "Feeding Score",
            f"{feeding_score}/100"
        )

    # =====================================================
    # CENTER
    # =====================================================

    with center:

        st.subheader(
            "Tactical Synthesis"
        )

        synthesis = []

        if tide_direction == "OUTGOING":
            synthesis.append(
                "Outbound tidal pressure active."
            )

        if tide_direction == "INCOMING":
            synthesis.append(
                "Incoming tidal energy pushing bait toward structure."
            )

        if swell_direction in ["E", "SE", "NE"]:
            synthesis.append(
                "Atlantic swell impacting inlet."
            )

        if standing_wave:
            synthesis.append(
                "Standing-wave formation possible near jetty zones."
            )

        if tide_velocity == "STRONG":
            synthesis.append(
                "Peak tidal exchange currently active."
            )

        if feeding_score >= 80:
            synthesis.append(
                "Predatory feeding probability elevated."
            )

        elif feeding_score >= 60:
            synthesis.append(
                "Moderate bait movement detected."
            )

        if not synthesis:
            synthesis.append(
                "Marine systems nominal."
            )

        for item in synthesis:
            st.write(f"• {item}")

        st.divider()

        # =================================================
        # PREDICTION
        # =================================================

        st.subheader(
            "Fish Prediction Engine"
        )

        if feeding_score >= 85:
            st.success(recommendation)

        elif feeding_score >= 65:
            st.info(recommendation)

        else:
            st.warning(recommendation)

        st.markdown(
            f"**Bite Timing:** {bite_window}"
        )

        st.divider()

        # =================================================
        # LAUNCH
        # =================================================

        st.subheader(
            "Launch Guidance"
        )

        st.info(
            launch_window
        )

    # =====================================================
    # RIGHT
    # =====================================================

    with right:

        st.metric(
            "Tide Flow",
            tide_direction
        )

        st.metric(
            "Tidal Velocity",
            tide_velocity
        )

        st.metric(
            "Swell Period",
            f"{swell_period} sec"
        )

        st.metric(
            "Fish Activity",
            activity
        )

    st.divider()

    # =====================================================
    # ALERTS
    # =====================================================

    st.subheader(
        "Operational Alerts"
    )

    alerts = []

    if standing_wave:
        alerts.append(
            "Standing-wave hazard elevated during outbound flow."
        )

    if danger_score >= 60:
        alerts.append(
            "Operational danger score elevated."
        )

    if feeding_score >= 80:
        alerts.append(
            "Major feeding window detected near tidal exchange zones."
        )

    if tide_velocity == "STRONG":
        alerts.append(
            "Strong tidal velocity impacting navigation timing."
        )

    if not alerts:
        alerts.append(
            "No critical marine alerts detected."
        )

    for alert in alerts:
        st.warning(alert)

    st.divider()

    st.caption(
        "Predictive operational synthesis using tides, "
        "swell interaction, wave energy, feeding probability, "
        "and inlet hazard modeling."
    )