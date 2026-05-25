# =========================================================
# TIDE LINE — METRIC CARD
# =========================================================

import streamlit as st


def metric_card(

    label,
    value,
    description="",
    accent="#3B82F6"

):

    html = f"""
<div style="background:#081220;border:1px solid #1F293B;border-left:4px solid {accent};border-radius:12px;padding:0.75rem;min-height:95px;">

<div style="color:#94A3B8;font-size:0.72rem;font-weight:600;margin-bottom:0.3rem;">
{label}
</div>

<div style="color:white;font-size:1.05rem;font-weight:700;margin-bottom:0.2rem;">
{value}
</div>

<div style="color:#64748B;font-size:0.72rem;">
{description}
</div>

</div>
"""

    st.markdown(

        html,

        unsafe_allow_html=True

    )
