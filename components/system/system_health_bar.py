import streamlit as st


# =========================================================
# TIDE LINE — SYSTEM HEALTH BAR
# =========================================================

def show_system_health_bar(

    tactical

):

    health = tactical.get(
        "system_health",
        {}
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "NOAA",
            health.get(
                "noaa",
                "UNKNOWN"
            )
        )

    with col2:

        st.metric(
            "Telemetry",
            health.get(
                "telemetry",
                "UNKNOWN"
            )
        )

    with col3:

        st.metric(
            "Buoys",
            health.get(
                "buoys",
                "UNKNOWN"
            )
        )

    with col4:

        st.metric(
            "Prediction",
            health.get(
                "prediction",
                "UNKNOWN"
            )
        )
