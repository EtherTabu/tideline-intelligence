# =========================================================
# TIDE LINE — COMMAND GRID ENGINE
# =========================================================

import streamlit as st


# =========================================================
# COMPONENT IMPORTS
# =========================================================

from components.ui.weather_command_bar import (
    show_weather_command_bar
)

from components.ui.status_banner import (
    status_banner
)

from components.ui.metric_card import (
    metric_card
)

from components.telemetry.telemetry_ticker import (
    show_telemetry_ticker
)

from components.tactical.strike_clock import (
    show_strike_clock
)

from components.marine.radar_panel import (
    show_radar_panel
)

from components.marine.marine_traffic import (
    show_marine_traffic
)

from components.marine.camera_wall import (
    show_camera_wall
)

from components.marine.inlet_status_panel import (
    show_inlet_status_panel
)

from components.tactical.tactical_brief_panel import (
    show_tactical_brief_panel
)

from components.tactical.tactical_panel import (
    show_tactical_panel
)

from components.tactical.recommendations import (
    show_recommendations
)

from components.tactical.tactical_memory_panel import (
    show_tactical_memory_panel
)

from components.species.species_cards import (
    render_species_cards
)

from components.species.species_matrix import (
    render_species_matrix
)


# =========================================================
# MAIN COMMAND GRID
# =========================================================

def show_tactical_layout(

    command_state,

    marine_data,
    tide_data,
    buoy_data,
    risk_data,
    prediction_data,
    tactical_data,

    species_data,
    species_matrix,

    inlet_data,
    brief_data,
    memory_data,
    synthesis_data,
    payload

):

    # =====================================================
    # TOP TELEMETRY
    # =====================================================

    show_weather_command_bar(
        marine_data
    )

    show_inlet_status_panel(
        inlet_data
    )

    show_tactical_brief_panel(
        brief_data
    )

    status_banner(

        "TACTICAL",

        "SYSTEMS SYNCHRONIZED • COMMAND GRID ACTIVE"

    )

    # =====================================================
    # COMMAND METRICS
    # =====================================================

    cmd1, cmd2, cmd3, cmd4, cmd5 = st.columns(5)

    with cmd1:

        metric_card(

            "MISSION",

            command_state.get(
                "mode",
                "MONITOR"
            ),

            "Operational posture"

        )

    with cmd2:

        metric_card(

            "TARGET",

            command_state.get(
                "primary_target",
                "UNKNOWN"
            ),

            "Primary species focus"

        )

    with cmd3:

        metric_card(

            "CONFIDENCE",

            f"{command_state.get('confidence', 0)}%",

            "System confidence"

        )

    with cmd4:

        metric_card(

            "RISK",

            command_state.get(
                "risk",
                "LOW"
            ),

            "Marine operational risk"

        )

    with cmd5:

        metric_card(

            "STATE",

            "ONLINE",

            "Command grid status"

        )

    # =====================================================
    # STRIKE TELEMETRY
    # =====================================================

    show_strike_clock(

        prediction_data,
        tactical_data

    )

    show_telemetry_ticker(

        marine_data,
        risk_data,
        prediction_data,
        tactical_data

    )

    # =====================================================
    # RADAR STACK
    # =====================================================

    show_radar_panel()

    show_marine_traffic()

    # =====================================================
    # SPECIES OPPORTUNITY MATRIX
    # =====================================================

    status_banner(

        "SPECIES OPPORTUNITY MATRIX",

        "LIVE SPECIES RANKINGS • CONDITIONS • OPPORTUNITIES"

    )

    render_species_matrix(
        species_matrix
    )

    # =====================================================
    # SPECIES INTEL
    # =====================================================

    status_banner(

        "SPECIES INTEL",

        "LIVE TARGET ANALYSIS"

    )

    render_species_cards(
        species_data
    )

    # =====================================================
    # LIVE CAMERA GRID
    # =====================================================

    show_camera_wall()

    # =====================================================
    # LOWER TACTICAL GRID
    # =====================================================

    lower_left, lower_right = st.columns(
        [1.2, 1]
    )

    with lower_left:

        show_tactical_panel(
            tactical_data
        )

    with lower_right:

        show_recommendations(
            payload
        )

    # =====================================================
    # MEMORY BUS
    # =====================================================

    show_tactical_memory_panel(
        memory_data
    )