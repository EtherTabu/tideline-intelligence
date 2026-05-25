import streamlit as st


# =========================================================
# SYNTHESIS ENGINE
# =========================================================

def generate_operational_summary(data):

    risk = data.get(
        "risk",
        "LOW"
    )

    tide_direction = data.get(
        "tide_direction",
        "UNKNOWN"
    )

    swell_direction = data.get(
        "swell_direction",
        "UNKNOWN"
    )

    wave_data = data.get(
        "wave_data",
        {}
    )

    wave_height = wave_data.get(
        "average",
        0
    )

    # =====================================================
    # STANDING WAVE LOGIC
    # =====================================================

    if (
        tide_direction == "OUTGOING"
        and swell_direction in ["E", "SE", "ENE"]
        and wave_height >= 3
    ):

        return (
            "Outgoing tide opposing easterly swell. "
            "Standing-wave formation possible "
            "near inlet mouth and jetty zones."
        )

    # =====================================================
    # HIGH RISK
    # =====================================================

    if risk == "HIGH":

        return (
            "Elevated marine turbulence expected. "
            "Exercise caution during outbound transit."
        )

    # =====================================================
    # MODERATE
    # =====================================================

    if risk == "MODERATE":

        return (
            "Moderate inlet movement detected. "
            "Cross-current activity possible near "
            "peak tidal exchange."
        )

    # =====================================================
    # LOW
    # =====================================================

    return (
        "Marine systems nominal. "
        "Minimal inlet turbulence currently detected."
    )


# =========================================================
# MAIN PANEL
# =========================================================

def show_marine_panel(data):

    st.markdown("## NOAA Marine Forecast")

    if not data:

        st.error(
            "NOAA marine systems unavailable."
        )

        return

    risk = data.get(
        "risk",
        "LOW"
    )

    score = data.get(
        "danger_score",
        0
    )

    # =====================================================
    # RISK HEADER
    # =====================================================

    if risk == "LOW":

        st.success(
            f"Operational Risk: {risk}"
        )

    elif risk == "MODERATE":

        st.warning(
            f"Operational Risk: {risk}"
        )

    else:

        st.error(
            f"Operational Risk: {risk}"
        )

    # =====================================================
    # GRID
    # =====================================================

    left, center, right = st.columns(
        [1, 2.2, 1]
    )

    # =====================================================
    # LEFT COLUMN
    # =====================================================

    with left:

        st.metric(
            "Wind",
            data.get(
                "wind",
                "0 mph"
            )
        )

        st.metric(
            "Direction",
            data.get(
                "direction",
                "UNKNOWN"
            )
        )

        wave_data = data.get(
            "wave_data",
            {}
        )

        if wave_data:

            st.metric(
                "Wave Height",
                f"{wave_data.get('average', 0)} ft"
            )

        else:

            st.metric(
                "Wave Height",
                "0 ft"
            )

        st.metric(
            "Tide Flow",
            data.get(
                "tide_direction",
                "UNKNOWN"
            )
        )

    # =====================================================
    # CENTER COLUMN
    # =====================================================

    with center:

        st.markdown(
            f"### {data.get('forecast', 'Unknown')}"
        )

        st.write(
            data.get(
                "details",
                "No marine details available."
            )
        )

        # =================================================
        # SYNTHESIS OUTPUT
        # =================================================

        summary = generate_operational_summary(
            data
        )

        if risk == "LOW":

            st.success(summary)

        elif risk == "MODERATE":

            st.warning(summary)

        else:

            st.error(summary)

        # =================================================
        # ADVISORIES
        # =================================================

        advisories = data.get(
            "advisories",
            []
        )

        if advisories:

            st.error(
                " | ".join(advisories)
            )

    # =====================================================
    # RIGHT COLUMN
    # =====================================================

    with right:

        swell_period = data.get(
            "swell_period",
            "Unknown"
        )

        st.metric(
            "Swell Period",
            (
                f"{swell_period} sec"
                if swell_period != "Unknown"
                else "Unknown"
            )
        )

        st.metric(
            "Swell Direction",
            data.get(
                "swell_direction",
                "UNKNOWN"
            )
        )

        st.metric(
            "Danger Score",
            f"{score}/100"
        )

        st.metric(
            "Risk State",
            risk
        )

    # =====================================================
    # FOOTER
    # =====================================================

    st.caption(
        "Environmental synthesis engine using "
        "NOAA marine forecast interpretation, "
        "tide flow analysis, and inlet conflict modeling."
    )
