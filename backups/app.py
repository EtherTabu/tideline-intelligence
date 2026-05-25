# =========================================================
# TIDE LINE | STRATEGIC COMMAND
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

from src.utils.marine_engine import (
    build_marine_system
)

from components.species.species_cards import (
    render_species_cards
)

from components.cameras import (
    show_inlet_feeds
)

from components.ui.mission_hero import (
    show_mission_hero
)

from components.radar_panel import (
    show_radar_panel
)

from components.strike_timeline import (
    show_strike_timeline
)

from components.system_health_bar import (
    show_system_health_bar
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(

    page_title="TIDE LINE | STRATEGIC COMMAND",

    layout="wide"

)


# =========================================================
# BUILD SYSTEM
# =========================================================

system = build_marine_system()

marine_data = system.get(
    "marine",
    {}
)

tide_data = system.get(
    "tides",
    {}
)

buoy_data = system.get(
    "buoys",
    {}
)

risk_data = system.get(
    "risk",
    {}
)

prediction_data = system.get(
    "prediction",
    {}
)

synthesis_data = system.get(
    "synthesis",
    {}
)

tactical_data = system.get(
    "tactical",
    {}
)


# =========================================================
# NORMALIZED CONTRACTS
# =========================================================

forecast = marine_data.get(
    "forecast",
    {}
)

wind = marine_data.get(
    "wind",
    {}
)

sea_state = marine_data.get(
    "sea_state",
    {}
)

current_tide = tide_data.get(
    "current",
    {}
)

regional = buoy_data.get(
    "regional",
    {}
)

stations = buoy_data.get(
    "stations",
    {}
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
# 🌊 TIDE LINE | STRATEGIC COMMAND

### Juno Beach / Jupiter Operational Hub
"""
)


# =========================================================
# STATUS BAR
# =========================================================

status1, status2, status3, status4 = st.columns(4)

with status1:

    st.caption("Boat Traffic")

    st.markdown("## SCANNING")

    st.success(
        "⚡ Inlets Active"
    )

with status2:

    st.caption("Marine Systems")

    st.markdown("## ONLINE")

    st.success(
        "🌊 NOAA + Telemetry"
    )

with status3:

    st.caption("Prediction Engine")

    st.markdown("## ACTIVE")

    st.success(
        "🎣 Species Tracking"
    )

with status4:

    st.caption("System Confidence")

    st.markdown("## LIVE")

    st.success(
        "🧠 Tactical Synthesis"
    )

st.divider()


# =========================================================
# COMMAND CENTER HERO GRID
# =========================================================

hero_left, hero_right = st.columns(
    [1.5, 1]
)

with hero_left:

    show_mission_hero(

        prediction_data,
        synthesis_data,
        risk_data

    )

with hero_right:

    st.markdown(
        "## 🛠️ System Health"
    )

    show_system_health_bar(
        tactical_data
    )

    st.divider()

    st.markdown(
        "## 🚨 Tactical Alerts"
    )

    alerts = tactical_data.get(
        "alerts",
        []
    )

    if alerts:

        for alert in alerts:

            st.warning(alert)

    else:

        st.success(
            "No tactical alerts detected."
        )

st.divider()


# =========================================================
# RADAR / WEATHER INTELLIGENCE
# =========================================================

show_radar_panel()

st.divider()


# =========================================================
# CAMERA / VISUAL INTELLIGENCE
# =========================================================

show_inlet_feeds()

st.divider()


# =========================================================
# STRIKE TIMELINE
# =========================================================

show_strike_timeline(

    prediction_data,
    tide_data

)

st.divider()


# =========================================================
# PRIMARY TELEMETRY GRID
# =========================================================

left, center, right = st.columns(
    [1.1, 2.2, 1]
)


# =========================================================
# LEFT COLUMN
# =========================================================

with left:

    st.markdown(
        "## 🌬️ Wind Intelligence"
    )

    st.metric(
        "Wind Speed",
        f"{wind.get('speed_mph', 0)} mph"
    )

    st.metric(
        "Direction",
        wind.get(
            "direction",
            "UNKNOWN"
        )
    )

    st.metric(
        "Swell Direction",
        sea_state.get(
            "swell_direction",
            "UNKNOWN"
        )
    )

    st.caption(
        "NOAA atmospheric intelligence."
    )


# =========================================================
# CENTER COLUMN
# =========================================================

with center:

    st.markdown(
        "## 🌊 Sea State Intelligence"
    )

    risk_state = risk_data.get(
        "risk_state",
        "LOW"
    )

    if risk_state == "LOW":

        st.success(
            "Marine systems nominal."
        )

    elif risk_state == "MODERATE":

        st.warning(
            "Moderate marine instability detected."
        )

    else:

        st.error(
            "Elevated marine operating risk."
        )

    c1, c2, c3 = st.columns(3)

    # =====================================================
    # SEA STATE
    # =====================================================

    with c1:

        st.metric(
            "Wave Height",
            f"{sea_state.get('wave_height_ft', 0)} ft"
        )

        st.metric(
            "Wave Period",
            f"{sea_state.get('wave_period_sec', 0)} sec"
        )

        st.metric(
            "Swell Period",
            f"{sea_state.get('swell_period_sec', 0)} sec"
        )

    # =====================================================
    # TIDE INTEL
    # =====================================================

    with c2:

        st.metric(
            "Tide Direction",
            current_tide.get(
                "direction",
                "UNKNOWN"
            )
        )

        st.metric(
            "Tide Velocity",
            current_tide.get(
                "velocity",
                "UNKNOWN"
            )
        )

        st.metric(
            "Launch Viability",
            risk_data.get(
                "launch_viability",
                "UNKNOWN"
            )
        )

    # =====================================================
    # FEEDING ENGINE
    # =====================================================

    with c3:

        st.metric(
            "Feeding Score",
            prediction_data.get(
                "feeding_score",
                0
            )
        )

        st.metric(
            "Activity",
            prediction_data.get(
                "activity",
                "UNKNOWN"
            )
        )

        st.metric(
            "Danger Score",
            risk_data.get(
                "danger_score",
                0
            )
        )

    st.divider()

    st.markdown(
        "### 📡 Tactical Signal Engine"
    )

    st.info(

        prediction_data.get(
            "recommendation",
            "No recommendation available."
        )

    )


# =========================================================
# RIGHT COLUMN
# =========================================================

with right:

    st.markdown(
        "## 📡 Telemetry"
    )

    st.metric(
        "Stations Active",
        stations.get(
            "active",
            0
        )
    )

    st.metric(
        "Regional Rating",
        regional.get(
            "rating",
            "UNKNOWN"
        )
    )

    st.metric(
        "Regional Wind",
        f"{regional.get('wind_speed_kt', 0)} kt"
    )

    st.metric(
        "Wave Height",
        f"{regional.get('wave_height_ft', 0)} ft"
    )

    st.caption(
        "Regional offshore buoy network."
    )

st.divider()


# =========================================================
# STRATEGIC TIDE VISUALIZATION
# =========================================================

st.markdown(
    "## 🌊 Strategic Tide Intelligence"
)

tide_points = tide_data.get(
    "tides",
    []
)

if tide_points:

    df = pd.DataFrame(
        tide_points
    )

    fig = px.area(

        df,

        x="time",

        y="height"

    )

    fig.update_layout(

        template="plotly_dark",

        height=360,

        margin=dict(
            l=10,
            r=10,
            t=30,
            b=10
        )

    )

    st.plotly_chart(

        fig,

        width="stretch"

    )

st.divider()


# =========================================================
# SPECIES INTELLIGENCE
# =========================================================

render_species_cards(
    prediction_data
)

st.divider()


# =========================================================
# NOAA FORECAST
# =========================================================

st.markdown(
    "## NOAA Marine Forecast"
)

st.markdown(
    f"### {forecast.get('headline', 'Unavailable')}"
)

st.write(

    forecast.get(
        "details",
        "No forecast details available."
    )

)

st.divider()


# =========================================================
# DEBUG PANEL
# =========================================================

with st.expander(

    "SYSTEM DEBUG DATA",

    expanded=False

):

    st.json(system)

    st.write(
        "SPECIES PAYLOAD:",
        prediction_data.get("species")
    )


# =========================================================
# FOOTER
# =========================================================

st.caption(
    "TIDE LINE Strategic Command • Tactical Marine Intelligence Platform"
)
