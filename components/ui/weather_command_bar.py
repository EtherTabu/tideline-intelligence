# =========================================================
# TIDE LINE — WEATHER COMMAND BAR
# =========================================================

import streamlit as st


# =========================================================
# WEATHER COMMAND BAR
# =========================================================

def show_weather_command_bar(marine):

    if not marine:

        return

    wind_speed = marine.get(
        "wind_speed",
        "--"
    )

    wind_direction = marine.get(
        "wind_direction",
        "--"
    )

    wave_height = marine.get(
        "wave_height",
        "--"
    )

    wave_period = marine.get(
        "wave_period",
        "--"
    )

    water_temp = marine.get(
        "water_temp",
        "--"
    )

    pressure = marine.get(
        "pressure",
        "--"
    )

    moon_phase = marine.get(
        "moon_phase",
        "--"
    )

    tide_state = marine.get(
        "tide_state",
        "--"
    )

    visibility = marine.get(
        "visibility",
        "--"
    )

    timestamp = marine.get(
        "timestamp",
        "--"
    )

    # =====================================================
    # BAR
    # =====================================================

    st.markdown(

        f"""
<div style="
background:linear-gradient(
90deg,
#07111F 0%,
#0A1626 100%
);
border:1px solid #13304A;
border-radius:14px;
padding:0.85rem 1rem;
margin-top:0.8rem;
margin-bottom:1rem;
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
flex-wrap:wrap;
gap:1rem;
">

<div style="
display:flex;
gap:1.2rem;
flex-wrap:wrap;
align-items:center;
">

<div>
<div style="
color:#8FA3B8;
font-size:0.62rem;
letter-spacing:0.08em;
">
WIND
</div>

<div style="
color:#27F5A3;
font-size:1rem;
font-weight:800;
">
{wind_speed} KT
</div>
</div>

<div>
<div style="
color:#8FA3B8;
font-size:0.62rem;
letter-spacing:0.08em;
">
DIR
</div>

<div style="
color:white;
font-size:1rem;
font-weight:800;
">
{wind_direction}°
</div>
</div>

<div>
<div style="
color:#8FA3B8;
font-size:0.62rem;
letter-spacing:0.08em;
">
SEAS
</div>

<div style="
color:#3BD6FF;
font-size:1rem;
font-weight:800;
">
{wave_height} FT
</div>
</div>

<div>
<div style="
color:#8FA3B8;
font-size:0.62rem;
letter-spacing:0.08em;
">
PERIOD
</div>

<div style="
color:white;
font-size:1rem;
font-weight:800;
">
{wave_period} S
</div>
</div>

<div>
<div style="
color:#8FA3B8;
font-size:0.62rem;
letter-spacing:0.08em;
">
WATER
</div>

<div style="
color:#FFD166;
font-size:1rem;
font-weight:800;
">
{water_temp}°
</div>
</div>

<div>
<div style="
color:#8FA3B8;
font-size:0.62rem;
letter-spacing:0.08em;
">
PRESSURE
</div>

<div style="
color:white;
font-size:1rem;
font-weight:800;
">
{pressure}
</div>
</div>

<div>
<div style="
color:#8FA3B8;
font-size:0.62rem;
letter-spacing:0.08em;
">
TIDE
</div>

<div style="
color:#27F5A3;
font-size:1rem;
font-weight:800;
">
{tide_state}
</div>
</div>

<div>
<div style="
color:#8FA3B8;
font-size:0.62rem;
letter-spacing:0.08em;
">
MOON
</div>

<div style="
color:white;
font-size:1rem;
font-weight:800;
">
{moon_phase}
</div>
</div>

<div>
<div style="
color:#8FA3B8;
font-size:0.62rem;
letter-spacing:0.08em;
">
VIS
</div>

<div style="
color:#3BD6FF;
font-size:1rem;
font-weight:800;
">
{visibility} NM
</div>
</div>

</div>

<div style="
text-align:right;
">

<div style="
color:#8FA3B8;
font-size:0.62rem;
letter-spacing:0.08em;
">
LIVE TELEMETRY
</div>

<div style="
color:#27F5A3;
font-size:0.95rem;
font-weight:800;
">
{timestamp}
</div>

</div>

</div>

</div>
        """,

        unsafe_allow_html=True

    )
