# =========================================================
# TIDE LINE — SPECIES HEAT METER
# =========================================================

import streamlit as st


# =========================================================
# COLOR ENGINE
# =========================================================

def resolve_heat_color(score):

    if score >= 85:

        return "#27F5A3"

    if score >= 70:

        return "#7DFF7A"

    if score >= 55:

        return "#FFD166"

    if score >= 40:

        return "#FF9F43"

    return "#FF5C7A"


# =========================================================
# HEAT METER
# =========================================================

def render_heat_meter(

    label,
    score

):

    color = resolve_heat_color(
        score
    )

    meter_html = f"""

<div style="
margin-top:0.6rem;
margin-bottom:1rem;
">

<div style="
display:flex;
justify-content:space-between;
margin-bottom:0.35rem;
">

<div style="
color:#E2E8F0;
font-size:0.82rem;
font-weight:700;
">

{label}

</div>

<div style="
color:{color};
font-size:0.82rem;
font-weight:800;
">

{score}%

</div>

</div>

<div style="
width:100%;
background:#081727;
border-radius:999px;
height:12px;
overflow:hidden;
border:1px solid #13304A;
">

<div style="
width:{score}%;
background:{color};
height:100%;
border-radius:999px;
box-shadow:0 0 14px {color};
">

</div>

</div>

</div>

"""

    st.markdown(

        meter_html,

        unsafe_allow_html=True

    )
