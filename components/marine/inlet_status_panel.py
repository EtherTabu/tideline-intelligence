# =========================================================
# TIDE LINE — INLET STATUS PANEL
# =========================================================

import streamlit as st


# =========================================================
# PANEL
# =========================================================

def show_inlet_status_panel(inlet):

    if not inlet:
        return

    risk = inlet.get(
        "risk",
        "UNKNOWN"
    )

    recommendation = inlet.get(
        "recommendation",
        "No recommendation available."
    )

    stacking = inlet.get(
        "stacking",
        False
    )

    small_craft_safe = inlet.get(
        "small_craft_safe",
        True
    )

    wave_height = inlet.get(
        "wave_height",
        "--"
    )

    wave_period = inlet.get(
        "wave_period",
        "--"
    )

    wind_speed = inlet.get(
        "wind_speed",
        "--"
    )

    wind_direction = inlet.get(
        "wind_direction",
        "--"
    )

    tide_state = inlet.get(
        "tide_state",
        "--"
    )

    st.subheader("🌊 Inlet Status Engine")

    st.warning(
        f"{risk} RISK"
    )

    st.caption(recommendation)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("SEAS", f"{wave_height} FT")

    with col2:
        st.metric("PERIOD", f"{wave_period} S")

    with col3:
        st.metric("WIND", f"{wind_speed} KT")

    with col4:
        st.metric("DIR", f"{wind_direction}°")

    with col5:
        st.metric("TIDE", tide_state)

    if stacking:

        st.error(
            "⚠️ Swell stacking / wind-against-current conditions detected."
        )

    else:

        st.success(
            "✅ No major inlet stacking detected."
        )

    if small_craft_safe:

        st.success(
            "SAFE TO RUN"
        )

    else:

        st.warning(
            "SMALL CRAFT CAUTION"
        )