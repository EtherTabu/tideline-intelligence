# =========================================================
# TIDE LINE — TRAILER MODE
# =========================================================

import streamlit as st

from components.ui.metric_card import (
    metric_card
)

from components.ui.status_banner import (
    status_banner
)


# =========================================================
# TRAILER DISPLAY MODE
# =========================================================

def show_trailer_mode(

    tactical_data,
    prediction_data,
    risk_data,
    marine_data

):

    st.markdown(
        "# 🌊 TIDE LINE LIVE"
    )

    st.markdown(
        "### MOBILE MARINE INTELLIGENCE"
    )

    # =====================================================
    # PRIMARY STATUS
    # =====================================================

    priority_state = tactical_data.get(
        "priority_state",
        {}
    )

    status_banner(

        priority_state.get(
            "color",
            "BLUE"
        ).upper(),

        priority_state.get(
            "summary",
            "Operational status unavailable."
        )

    )

    # =====================================================
    # MAIN GRID
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    # =====================================================
    # TARGET
    # =====================================================

    with col1:

        metric_card(

            "TARGET",

            tactical_data.get(
                "primary_target",
                "UNKNOWN"
            ),

            "Primary strike species"

        )

    # =====================================================
    # FEEDING
    # =====================================================

    with col2:

        metric_card(

            "FEEDING",

            f"{prediction_data.get('feeding_score', 0)}%",

            "Predator activity"

        )

    # =====================================================
    # WIND
    # =====================================================

    with col3:

        metric_card(

            "WIND",

            f"{marine_data.get('wind', {}).get('speed_mph', 0)} MPH",

            "Regional wind velocity"

        )

    # =====================================================
    # SEAS
    # =====================================================

    with col4:

        metric_card(

            "SEAS",

            f"{marine_data.get('sea_state', {}).get('wave_height_ft', 0)} FT",

            "Offshore wave conditions"

        )

    # =====================================================
    # TACTICAL SUMMARY
    # =====================================================

    status_banner(

        "TACTICAL",

        prediction_data.get(
            "recommendation",
            "No tactical recommendation available."
        )

    )

    # =====================================================
    # ALERTS
    # =====================================================

    alerts = tactical_data.get(
        "alerts",
        []
    )

    for alert in alerts[:3]:

        status_banner(

            alert.get(
                "level",
                "INFO"
            ),

            alert.get(
                "message",
                ""
            )

        )
