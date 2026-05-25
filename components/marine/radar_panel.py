# =========================================================
# TIDE LINE — TACTICAL RADAR WALL
# =========================================================

import streamlit as st


# =========================================================
# RADAR WALL
# =========================================================

def show_radar_panel():

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown(

        """
<div style="
margin-top:1rem;
margin-bottom:1rem;
">

<div style="
color:#3BD6FF;
font-size:1rem;
font-weight:800;
letter-spacing:0.08em;
margin-bottom:0.4rem;
">

🌩️ TACTICAL WEATHER RADAR

</div>

<div style="
color:#8FA3B8;
font-size:0.9rem;
">

LIVE NOAA RADAR • WAVE INTELLIGENCE • OFFSHORE TELEMETRY

</div>

</div>
        """,

        unsafe_allow_html=True

    )

    # =====================================================
    # RADAR GRID
    # =====================================================

    radar_left, radar_right = st.columns(2)

    # =====================================================
    # LEFT — NOAA RADAR
    # =====================================================

    with radar_left:

        st.markdown(

            """
<div style="
background:#07111F;
border:1px solid #13304A;
border-radius:16px;
padding:0.75rem;
margin-bottom:0.75rem;
">

<div style="
color:#7DD3FC;
font-size:0.9rem;
font-weight:700;
letter-spacing:0.05em;
">

📡 NOAA TACTICAL RADAR

</div>

</div>
            """,

            unsafe_allow_html=True

        )

        st.iframe(

            "https://embed.windy.com/embed2.html"
            "?lat=27.0"
            "&lon=-80.0"
            "&detailLat=26.89"
            "&detailLon=-80.05"
            "&width=900"
            "&height=620"
            "&zoom=6"
            "&level=surface"
            "&overlay=radar"
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
            "&metricTemp=%C",

            height=620

        )

        st.caption(
            "Live radar, precipitation, offshore wind, and marine telemetry."
        )

    # =====================================================
    # RIGHT — WAVE INTELLIGENCE
    # =====================================================

    with radar_right:

        st.markdown(

            """
<div style="
background:#07111F;
border:1px solid #13304A;
border-radius:16px;
padding:0.75rem;
margin-bottom:0.75rem;
">

<div style="
color:#7DD3FC;
font-size:0.9rem;
font-weight:700;
letter-spacing:0.05em;
">

🌊 WAVE INTELLIGENCE

</div>

</div>
            """,

            unsafe_allow_html=True

        )

        st.iframe(

            "https://embed.windy.com/embed2.html"
            "?lat=27.0"
            "&lon=-80.0"
            "&detailLat=26.89"
            "&detailLon=-80.05"
            "&width=900"
            "&height=620"
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
            "&metricWave=ft",

            height=620

        )

        st.caption(
            "Wave height, swell intervals, offshore energy, and sea-state flow."
        )
