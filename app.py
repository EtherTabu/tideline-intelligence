# =========================================================
# TIDE LINE | STRATEGIC COMMAND
# FULL RESTORED BUILD
# =========================================================

import streamlit as st


# =========================================================
# CORE CONFIG
# =========================================================

from src.config.theme import (
    configure_page,
    inject_global_css
)

from src.core.orchestrator import (
    run_command_center
)


# =========================================================
# COMPONENTS
# =========================================================

from components.tactical.tactical_header import (
    show_tactical_header
)

from components.ui.weather_command_bar import (
    show_weather_command_bar
)

from components.marine.inlet_status_panel import (
    show_inlet_status_panel
)

from components.tactical.tactical_brief_panel import (
    show_tactical_brief_panel
)

from components.tactical.tactical_memory_panel import (
    show_tactical_memory_panel
)

from components.ui.status_banner import (
    status_banner
)

from components.ui.metric_card import (
    metric_card
)

from components.tactical.strike_clock import (
    show_strike_clock
)

from components.telemetry.telemetry_ticker import (
    show_telemetry_ticker
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

from components.species.species_cards import (
    show_species_cards
)

from components.tactical.tactical_panel import (
    show_tactical_panel
)

from components.tactical.recommendations import (
    show_recommendations
)

from components.debug.debug_panel import (
    show_debug_panel
)


# =========================================================
# PAGE CONFIG
# =========================================================

configure_page()

inject_global_css()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("# 🌊 TIDE LINE")

    st.markdown(
        "### TACTICAL COMMAND MODE"
    )

    st.caption(
        "Marine intelligence infrastructure online."
    )

    st.divider()

    debug_mode = st.toggle(
        "DEBUG MODE",
        value=False
    )


# =========================================================
# SAFE ORCHESTRATION
# =========================================================

try:

    payload = run_command_center()

except Exception as e:

    st.error(
        f"ORCHESTRATOR FAILURE: {e}"
    )

    payload = {}


# =========================================================
# SAFE PAYLOAD EXTRACTION
# =========================================================

marine_data = payload.get(
    "marine",
    {}
)

risk_data = payload.get(
    "risk",
    {}
)

prediction_data = payload.get(
    "prediction",
    {}
)

tactical_data = payload.get(
    "tactical",
    {}
)

species_data = payload.get(
    "species",
    []
)

inlet_data = payload.get(
    "inlet",
    {}
)

brief_data = payload.get(
    "brief",
    {}
)

memory_data = tactical_data.get(
    "memory",
    []
)


# =========================================================
# FALLBACK SPECIES RECOVERY
# =========================================================

if not species_data:

    if prediction_data:

        fallback_species = {

            "species": tactical_data.get(
                "primary_target",
                "SNAPPER"
            ),

            "score": prediction_data.get(
                "feeding_score",
                0
            ),

            "activity": prediction_data.get(
                "activity",
                "MODERATE"
            ),

            "recommendation": prediction_data.get(
                "recommendation",
                "Monitor marine conditions."
            ),

            "best_window": prediction_data.get(
                "bite_window",
                "ACTIVE"
            ),

            "depth_zone": "OFFSHORE",

            "techniques": [
                "Live bait",
                "Drift line",
                "Vertical jig"
            ],

            "known_targets": [
                "Reef edge",
                "Artificial structure"
            ],

            "tactical_notes": [
                "Fallback tactical synthesis active."
            ]

        }

        species_data = [fallback_species]


# =========================================================
# HEADER
# =========================================================

show_tactical_header()


# =========================================================
# WEATHER TELEMETRY
# =========================================================

show_weather_command_bar(
    marine_data
)


# =========================================================
# INLET STATUS
# =========================================================

show_inlet_status_panel(
    inlet_data
)


# =========================================================
# TACTICAL BRIEF
# =========================================================

show_tactical_brief_panel(
    brief_data
)


# =========================================================
# SYSTEM STATUS
# =========================================================

status_banner(

    "TACTICAL",

    "SYSTEMS SYNCHRONIZED • COMMAND LINK ACTIVE"

)


# =========================================================
# COMMAND METRICS
# =========================================================

cmd1, cmd2, cmd3, cmd4, cmd5 = st.columns(5)

with cmd1:

    metric_card(

        "MISSION",

        tactical_data.get(
            "mission_status",
            "MONITOR"
        ),

        "Operational posture"

    )

with cmd2:

    metric_card(

        "TARGET",

        tactical_data.get(
            "primary_target",
            "UNKNOWN"
        ),

        "Primary species focus"

    )

with cmd3:

    metric_card(

        "CONFIDENCE",

        f"{tactical_data.get('confidence', 0)}%",

        "System confidence"

    )

with cmd4:

    metric_card(

        "RISK",

        risk_data.get(
            "risk_state",
            "LOW"
        ),

        "Marine operational risk"

    )

with cmd5:

    metric_card(

        "LAUNCH",

        risk_data.get(
            "launch_viability",
            "UNKNOWN"
        ),

        "Go / no-go assessment"

    )


# =========================================================
# STRIKE CLOCK
# =========================================================

show_strike_clock(

    prediction_data,
    tactical_data

)


# =========================================================
# TELEMETRY TICKER
# =========================================================

show_telemetry_ticker(

    marine_data,
    risk_data,
    prediction_data,
    tactical_data

)


# =========================================================
# RADAR PANEL
# =========================================================

show_radar_panel()


# =========================================================
# MARINE TRAFFIC
# =========================================================

show_marine_traffic()


# =========================================================
# CAMERA WALL
# =========================================================

show_camera_wall()


# =========================================================
# SPECIES INTEL
# =========================================================

show_species_cards(
    species_data
)


# =========================================================
# TACTICAL PANEL
# =========================================================

show_tactical_panel(
    tactical_data
)


# =========================================================
# RECOMMENDATION ENGINE
# =========================================================

show_recommendations(
    payload
)


# =========================================================
# MEMORY PANEL
# =========================================================

show_tactical_memory_panel(
    memory_data
)


# =========================================================
# DEBUG PANEL
# =========================================================

if debug_mode:

    show_debug_panel(
        payload
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "TIDE LINE • Tactical Marine Intelligence Infrastructure"
)