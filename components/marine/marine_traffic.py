# =========================================================
# TIDE LINE — MARINE TRAFFIC PANEL
# =========================================================

import streamlit as st


# =========================================================
# MARINE TRAFFIC
# =========================================================

def show_marine_traffic():

    st.markdown(
        """
        <div style="
        color:#9FDBFF;
        font-size:0.82rem;
        font-weight:800;
        margin-bottom:0.4rem;
        letter-spacing:0.06em;
        ">
        🚢 LIVE MARINE TRAFFIC
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        "AIS vessel telemetry • fleet movement • offshore traffic"
    )

    st.iframe(

        "https://www.marinetraffic.com/en/ais/embed/zoom:7/centery:26.7/centerx:-79.9/maptype:1/shownames:true/mmsi:0/shipid:0/fleet:/fleet_id:/vtypes:/showmenu:false/remember:false",

        height=500

    )
