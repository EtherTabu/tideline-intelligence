# =========================================================
# TIDE LINE — TACTICAL LAYOUT ENGINE
# =========================================================

import streamlit as st

from components.telemetry.live_clock import (
    show_live_clock
)

from components.telemetry.refresh_engine import (
    show_refresh_status
)

from components.telemetry.telemetry_ticker import (
    show_telemetry_ticker
)

from components.marine.radar_panel import (
    show_radar_panel
)

from components.marine.wave_panel import (
    show_wave_panel
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

from components.tactical.strike_clock import (
    show_strike_clock
)

from components.tactical.strike_timeline import (
    show_strike_timeline
)

from components.tactical.tactical_memory_panel import (
    show_tactical_memory_panel
)

from components.species.species_cards import (
    show_species_cards
)

from components.ui.memory_panel import (
    show_memory_panel
)

from components.ui.weather_command_bar import (
    show_weather_command_bar
)

from components.ui.mission_hero import (
    show_mission_hero
)

from components.system.system_health_bar import (
    show_system_health_bar
)

from components.tactical.confidence_ring import (
    render_confidence_ring
)


# =========================================================
# MAIN LAYOUT
# =========================================================

def show_tactical_layout(

    mode,

    marine_data,
    tide_data,
    buoy_data,
    risk_data,
    prediction_data,
    tactical_data,
    synthesis_data

):

    # =====================================================
    # TELEMETRY
    # =====================================================

    show_live_clock()

    show_refresh_status()

    show_telemetry_ticker(

        marine_data,
        risk_data,
        prediction_data,
        tactical_data

    )

    # =====================================================
    # HERO
    # =====================================================

    show_mission_hero()

    # =====================================================
    # STATUS PANELS
    # =====================================================

    show_inlet_status_panel(
        risk_data
    )

    show_tactical_brief_panel(
        tactical_data
    )

    show_system_health_bar(
        synthesis_data
    )

    # =====================================================
    # CONFIDENCE RINGS
    # =====================================================

    r1, r2, r3 = st.columns(3)

    with r1:

        render_confidence_ring(

            "MISSION",

            tactical_data.get(
                "confidence",
                0
            )

        )

    with r2:

        render_confidence_ring(

            "FEEDING",

            prediction_data.get(
                "feeding_score",
                0
            )

        )

    with r3:

        render_confidence_ring(

            "SAFE",

            max(

                0,

                100 - risk_data.get(
                    "danger_score",
                    0
                )

            )

        )

    # =====================================================
    # COMMAND BAR
    # =====================================================

    show_weather_command_bar(
        marine_data
    )

    # =====================================================
    # STRIKE SYSTEMS
    # =====================================================

    show_strike_clock(
        tactical_data
    )

    show_strike_timeline(
        tactical_data
    )

    # =====================================================
    # TACTICAL PANEL
    # =====================================================

    show_tactical_panel(
        tactical_data
    )

    # =====================================================
    # RADAR + WAVES
    # =====================================================

    show_radar_panel()

    show_wave_panel()

    # =====================================================
    # MARINE TRAFFIC
    # =====================================================

    show_marine_traffic()

    # =====================================================
    # CAMERA WALL
    # =====================================================

    show_camera_wall()

    # =====================================================
    # SPECIES
    # =====================================================

    show_species_cards(
        prediction_data
    )

    # =====================================================
    # RECOMMENDATIONS
    # =====================================================

    show_recommendations(
        tactical_data
    )

    # =====================================================
    # MEMORY
    # =====================================================

    show_tactical_memory_panel(

        tactical_data.get(
            "memory",
            []
        )

    )

    show_memory_panel(
        tactical_data
    )