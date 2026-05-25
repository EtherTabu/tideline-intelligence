# =========================================================
# TIDE LINE — TACTICAL BRIEF PANEL
# =========================================================

import streamlit as st


# =========================================================
# PANEL
# =========================================================

def show_tactical_brief_panel(brief):

    if not brief:
        return

    operational_state = brief.get(
        "operational_state",
        "UNKNOWN"
    )

    mission_status = brief.get(
        "mission_status",
        "MONITOR"
    )

    target = brief.get(
        "target",
        "UNKNOWN"
    )

    confidence = brief.get(
        "confidence",
        0
    )

    active_window = brief.get(
        "active_window",
        "UNKNOWN"
    )

    inlet_risk = brief.get(
        "inlet_risk",
        "UNKNOWN"
    )

    recommendation = brief.get(
        "recommendation",
        "No recommendation available."
    )

    wave_height = brief.get(
        "wave_height",
        0
    )

    wind_speed = brief.get(
        "wind_speed",
        0
    )

    st.subheader("🎯 Tactical Briefing")

    st.info(recommendation)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("TARGET", target)

    with col2:
        st.metric("CONFIDENCE", f"{confidence}%")

    with col3:
        st.metric("WINDOW", active_window)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric("INLET", inlet_risk)

    with col5:
        st.metric("SEAS", f"{wave_height} FT")

    with col6:
        st.metric("WIND", f"{wind_speed} KT")

    st.success(
        f"MISSION STATUS: {mission_status}"
    )