# =========================================================
# TIDE LINE — TACTICAL RADAR GRID
# =========================================================

import streamlit as st


# =========================================================
# PANEL HEADER
# =========================================================

def render_panel_header(title, subtitle):

    st.markdown(

        f"""
<div style="
background:#07111F;
border:1px solid #13304A;
border-radius:14px;
padding:0.65rem 0.85rem;
margin-bottom:0.45rem;
">

<div style="
color:#7DD3FC;
font-size:0.82rem;
font-weight:800;
letter-spacing:0.08em;
margin-bottom:0.18rem;
">

{title}

</div>

<div style="
color:#6B7C93;
font-size:0.70rem;
letter-spacing:0.04em;
">

{subtitle}

</div>

</div>
        """,

        unsafe_allow_html=True

    )


# =========================================================
# MAIN RADAR GRID
# =========================================================

def show_radar_panel():

    # =====================================================
    # SECTION HEADER
    # =====================================================

    st.markdown(

        """
<div style="
margin-top:0.4rem;
margin-bottom:0.55rem;
">

<div style="
color:#3BD6FF;
font-size:0.95rem;
font-weight:800;
letter-spacing:0.08em;
margin-bottom:0.20rem;
">

🌩️ TACTICAL WEATHER RADAR

</div>

<div style="
color:#8FA3B8;
font-size:0.72rem;
letter-spacing:0.05em;
">

LIVE NOAA RADAR • WAVE ENERGY • OFFSHORE TELEMETRY

</div>

</div>
        """,

        unsafe_allow_html=True

    )

    # =====================================================
    # COMMAND GRID
    # =====================================================

    left_panel, right_panel = st.columns(
        [1, 1]
    )

    # =====================================================
    # LEFT — RADAR
    # =====================================================

    with left_panel:

        render_panel_header(

            "📡 NOAA RADAR",

            "PRECIPITATION • WIND • STORM MOVEMENT"

        )

        st.iframe(

            "https://embed.windy.com/embed2.html"
            "?lat=27.0"
            "&lon=-80.0"
            "&detailLat=26.89"
            "&detailLon=-80.05"
            "&width=900"
            "&height=460"
            "&zoom=6"
            "&level=surface"
            "&overlay=radar"
            "&product=ecmwf"
            "&menu=false"
            "&message=false"
            "&marker=true"
            "&calendar=24"
            "&pressure=true"
            "&type=map"
            "&location=coordinates"
            "&detail=true"
            "&metricWind=kt"
            "&metricTemp=%C",

            height=460

        )

        st.caption(
            "Storm movement • precipitation • offshore wind flow"
        )

    # =====================================================
    # RIGHT — WAVE FIELD
    # =====================================================

    with right_panel:

        render_panel_header(

            "🌊 WAVE INTELLIGENCE",

            "SEA STATE • SWELL ENERGY • PERIOD FLOW"

        )

        st.iframe(

            "https://embed.windy.com/embed2.html"
            "?lat=27.0"
            "&lon=-80.0"
            "&detailLat=26.89"
            "&detailLon=-80.05"
            "&width=900"
            "&height=460"
            "&zoom=6"
            "&level=surface"
            "&overlay=waves"
            "&product=ecmwf"
            "&menu=false"
            "&message=false"
            "&marker=true"
            "&calendar=24"
            "&pressure=true"
            "&type=map"
            "&location=coordinates"
            "&detail=true"
            "&metricWind=kt"
            "&metricWave=ft",

            height=460

        )

        st.caption(
            "Wave height • swell intervals • offshore energy transfer"
        )