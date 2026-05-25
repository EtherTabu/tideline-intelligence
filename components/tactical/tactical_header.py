# =========================================================
# TIDE LINE — TACTICAL HEADER
# =========================================================

import streamlit as st

from datetime import datetime


# =========================================================
# HEADER
# =========================================================

def show_tactical_header():

    current_time = datetime.now().strftime(
        "%A • %H:%M:%S"
    )

    header_html = f"""
<div style="
background:linear-gradient(
135deg,
#07111F 0%,
#0B1727 55%,
#102033 100%
);
border:1px solid #13304A;
border-radius:20px;
padding:1.5rem 1.75rem;
margin-bottom:1.25rem;
box-shadow:0 0 24px rgba(0,212,255,0.08);
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
color:#3BD6FF;
font-size:0.82rem;
font-weight:800;
letter-spacing:0.12em;
margin-bottom:0.35rem;
">
TACTICAL MARINE INTELLIGENCE
</div>

<div style="
color:white;
font-size:2.5rem;
font-weight:900;
line-height:1;
margin-top:0.3rem;
">
🌊 TIDE LINE
</div>

<div style="
color:#9FB3C8;
font-size:0.95rem;
margin-top:0.25rem;
">
JUNO BEACH SECTOR • MOBILE COMMAND PLATFORM
</div>

</div>

<div style="text-align:right;">

<div style="
color:#27F5A3;
font-size:0.8rem;
font-weight:800;
letter-spacing:0.08em;
">
● SYSTEM OPERATIONAL
</div>

<div style="
color:white;
font-size:1rem;
margin-top:0.35rem;
">
{current_time}
</div>

<div style="
color:#3BD6FF;
font-size:0.82rem;
margin-top:0.25rem;
">
NOAA • RADAR • BUOYS • STRIKE ENGINE
</div>

</div>

</div>

</div>
"""

    st.markdown(
        header_html,
        unsafe_allow_html=True
    )
