# =========================================================
# TIDE LINE — MISSION HERO
# =========================================================

import streamlit as st


def show_mission_hero():

    st.markdown("""

    <div style="
        padding:1.2rem;
        border-radius:16px;
        background:linear-gradient(
            90deg,
            rgba(0,20,40,0.95),
            rgba(0,40,80,0.95)
        );
        border:1px solid rgba(0,255,200,0.18);
        margin-bottom:1rem;
    ">

        <div style="
            color:#00FFD1;
            font-size:0.75rem;
            letter-spacing:0.18rem;
            font-weight:700;
            margin-bottom:0.5rem;
        ">
            TACTICAL MARINE INTELLIGENCE
        </div>

        <div style="
            color:white;
            font-size:2rem;
            font-weight:900;
        ">
            TIDE LINE
        </div>

        <div style="
            color:#7C93B6;
            margin-top:0.5rem;
            font-size:0.95rem;
        ">
            Offshore strike coordination • inlet intelligence • species prediction
        </div>

    </div>

    """, unsafe_allow_html=True)
