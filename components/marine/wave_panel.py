# =========================================================
# TIDE LINE — WAVE INTELLIGENCE PANEL
# =========================================================

import streamlit as st


# =========================================================
# WAVE PANEL
# =========================================================

def show_wave_panel():

    st.markdown(
        "### 🌊 Wave Intelligence"
    )

    st.components.v1.iframe(

        src=(
            "https://embed.windy.com/embed2.html"
            "?lat=27.0"
            "&lon=-80.0"
            "&detailLat=26.89"
            "&detailLon=-80.05"
            "&width=650"
            "&height=450"
            "&zoom=6"
            "&level=surface"
            "&overlay=waves"
            "&product=ecmwf"
            "&menu=true"
            "&message=true"
            "&marker=true"
            "&calendar=24"
            "&pressure=true"
            "&type=map"
            "&location=coordinates"
            "&detail=true"
            "&metricWind=kt"
            "&metricWave=ft"
        ),

        height=450

    )

    st.caption(
        "Wave energy, swell direction, "
        "period intervals, and offshore conditions."
    )
