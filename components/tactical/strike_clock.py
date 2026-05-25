# =========================================================
# TIDE LINE — STRIKE CLOCK
# =========================================================

import streamlit as st


# =========================================================
# STRIKE CLOCK
# =========================================================

def show_strike_clock(

    prediction_data,
    tactical_data

):

    active_window = prediction_data.get(
        "active_window",
        "PRIME WINDOW"
    )

    target = tactical_data.get(
        "primary_target",
        "SNAPPER"
    )

    clock_html = f"""
<div style="
background:linear-gradient(
135deg,
#08131F 0%,
#0B1727 100%
);
border:1px solid #16324A;
border-radius:18px;
padding:1.2rem;
margin-top:1rem;
margin-bottom:1rem;
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
flex-wrap:wrap;
gap:1rem;
">

<div>

<div style="
color:#9FDBFF;
font-size:0.78rem;
font-weight:700;
letter-spacing:0.06em;
margin-bottom:0.35rem;
">
STRIKE CLOCK
</div>

<div style="
color:white;
font-size:1.5rem;
font-weight:800;
line-height:1;
">
{active_window}
</div>

<div style="
color:#27F5A3;
margin-top:0.45rem;
font-size:0.95rem;
font-weight:700;
">
TARGET: {target}
</div>

</div>

<div style="
width:140px;
height:140px;
border-radius:50%;
border:6px solid #27F5A3;
display:flex;
align-items:center;
justify-content:center;
background:rgba(39,245,163,0.08);
box-shadow:0 0 25px rgba(39,245,163,0.18);
">

<div style="
text-align:center;
">

<div style="
color:#27F5A3;
font-size:2rem;
font-weight:900;
line-height:1;
">
92%
</div>

<div style="
color:#8FA8C0;
font-size:0.75rem;
margin-top:0.3rem;
">
STRIKE ODDS
</div>

</div>

</div>

</div>

</div>
"""

    st.markdown(
        clock_html,
        unsafe_allow_html=True
    )
