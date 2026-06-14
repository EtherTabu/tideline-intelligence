# =========================================================
# TIDE LINE | COMMAND CENTER CORE
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
# LAYOUT ENGINE
# =========================================================

from components.layout.tactical_layout import (
    show_tactical_layout
)


# =========================================================
# COMPONENTS
# =========================================================

from components.tactical.tactical_header import (
    show_tactical_header
)

from components.debug.debug_panel import (
    show_debug_panel
)


# =========================================================
# SPECIES ENGINES
# =========================================================

from src.services.species_engine import (
    calculate_species_scores
)

from src.services.species_matrix_engine import (
    build_species_matrix
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

canonical_marine_data = payload.get(
    "canonical_marine",
    marine_data
)

dashboard_marine_data = payload.get(
    "dashboard_marine",
    marine_data
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

tides_data = payload.get(
    "tides",
    {}
)

buoys_data = payload.get(
    "buoys",
    {}
)

synthesis_data = payload.get(
    "synthesis",
    {}
)


# =========================================================
# LIVE SPECIES ENGINE
# =========================================================

species_data = calculate_species_scores(

    canonical_marine_data,

    tides_data,

    buoys_data,

    risk_data

)


# =========================================================
# SPECIES OPPORTUNITY MATRIX
# =========================================================

species_matrix = build_species_matrix(
    dashboard_marine_data
)


# =========================================================
# FALLBACK SPECIES RECOVERY
# =========================================================

if not species_data:

    fallback_species = {

        "species": "Mahi",

        "score": 72,

        "activity": "HIGH",

        "depth": "BLUE WATER",

        "structure": [
            "WEEDLINE"
        ]

    }

    species_data = [
        fallback_species
    ]


# =========================================================
# COMMAND STATE
# =========================================================

command_state = {

    "mode": tactical_data.get(
        "mission_status",
        "MONITOR"
    ),

    "primary_target": tactical_data.get(
        "primary_target",
        "UNKNOWN"
    ),

    "confidence": tactical_data.get(
        "confidence",
        0
    ),

    "risk": risk_data.get(
        "risk_state",
        "LOW"
    )

}


# =========================================================
# COMMAND HEADER
# =========================================================

show_tactical_header()


# =========================================================
# MAIN COMMAND GRID
# =========================================================

show_tactical_layout(

    command_state=command_state,

    marine_data=marine_data,

    dashboard_marine_data=dashboard_marine_data,

    tide_data=tides_data,

    buoy_data=buoys_data,

    risk_data=risk_data,

    prediction_data=prediction_data,

    tactical_data=tactical_data,

    species_data=species_data,

    species_matrix=species_matrix,

    inlet_data=inlet_data,

    brief_data=brief_data,

    memory_data=memory_data,

    synthesis_data=synthesis_data,

    payload=payload

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
