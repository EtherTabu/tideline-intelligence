# =========================================================
# TIDE LINE — TELEMETRY TICKER
# =========================================================

import streamlit as st

from datetime import datetime


# =========================================================
# BUILD FEED
# =========================================================

def build_tactical_feed(

    marine_data,
    risk_data,
    prediction_data,
    tactical_data

):

    wind_speed = marine_data.get(
        "wind_speed",
        0
    )

    wave_height = marine_data.get(
        "wave_height",
        0
    )

    target = tactical_data.get(
        "primary_target",
        "UNKNOWN"
    )

    mission = tactical_data.get(
        "mission_status",
        "MONITOR"
    )

    feeding_score = prediction_data.get(
        "feeding_score",
        0
    )

    timestamp = datetime.now().strftime(
        "%H:%M:%S"
    )

    return [

        f"🌊 Seas running {wave_height} FT",

        f"🎯 Target species {target}",

        f"⚡ Mission state {mission}",

        f"🌬️ Wind velocity {wind_speed} MPH",

        f"🐟 Feeding probability {feeding_score}%",

        f"📡 NOAA telemetry synchronized",

        f"🛰️ Tactical systems operational",

        f"🕒 Updated {timestamp}"

    ]


# =========================================================
# SHOW TICKER
# =========================================================

def show_telemetry_ticker(

    marine_data,
    risk_data,
    prediction_data,
    tactical_data

):

    feed_items = build_tactical_feed(

        marine_data,
        risk_data,
        prediction_data,
        tactical_data

    )

    ticker_text = " ✦ ".join(
        feed_items
    )

    ticker_html = f"""
<div style="
background:#07111F;
border:1px solid #13304A;
border-radius:12px;
padding:0.75rem;
overflow:hidden;
margin-top:1rem;
margin-bottom:1rem;
white-space:nowrap;
">

<div style="
display:inline-block;
padding-left:100%;
animation:tickerMove 40s linear infinite;
color:#7DD3FC;
font-size:0.92rem;
font-weight:600;
">

{ticker_text}

</div>

</div>

<style>

@keyframes tickerMove {{

0% {{
transform:translateX(0%);
}}

100% {{
transform:translateX(-100%);
}}

}}

</style>
"""

    st.markdown(
        ticker_html,
        unsafe_allow_html=True
    )
