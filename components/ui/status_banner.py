# =========================================================
# TIDE LINE — STATUS BANNER
# =========================================================

import streamlit as st


COLOR_MAP = {

    "GREEN": "#38D996",
    "RED": "#FF5C7A",
    "YELLOW": "#FFCC15",
    "BLUE": "#3B82F6",
    "INFO": "#3B82F6",
    "TACTICAL": "#00E5FF"

}


def status_banner(

    level,
    message

):

    color = COLOR_MAP.get(

        level.upper(),

        "#3B82F6"

    )

    html = f"""
<div style="background:#081220;border:1px solid #1F293B;border-left:5px solid {color};border-radius:10px;padding:0.75rem;margin-bottom:0.45rem;">

<div style="color:{color};font-size:0.72rem;font-weight:700;letter-spacing:0.05em;text-transform:uppercase;margin-bottom:0.2rem;">
{level}
</div>

<div style="color:#E2E8F0;font-size:0.92rem;line-height:1.3;">
{message}
</div>

</div>
"""

    st.markdown(

        html,

        unsafe_allow_html=True

    )
