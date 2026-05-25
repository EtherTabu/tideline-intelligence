# =========================================================
# TIDE LINE — TACTICAL CHIPS
# =========================================================

import streamlit as st


# =========================================================
# CHIP COLOR ENGINE
# =========================================================

def resolve_chip_color(text):

    text = str(text).lower()

    positive_terms = [

        "incoming",
        "prime",
        "good",
        "active",
        "stable",
        "favorable",
        "feeding",
        "running",
        "reef",
        "weedline",
        "structure"

    ]

    warning_terms = [

        "risk",
        "rough",
        "danger",
        "storm",
        "lightning",
        "caution"

    ]

    for term in positive_terms:

        if term in text:

            return "#27F5A3"

    for term in warning_terms:

        if term in text:

            return "#FF7B72"

    return "#3BD6FF"


# =========================================================
# CHIP RENDERER
# =========================================================

def render_tactical_chips(

    items,
    title=None

):

    if not items:

        return

    # =====================================================
    # TITLE
    # =====================================================

    if title:

        st.markdown(

            f"""
<div style="
margin-top:0.7rem;
margin-bottom:0.5rem;
color:white;
font-size:0.95rem;
font-weight:700;
">

{title}

</div>
            """,

            unsafe_allow_html=True

        )

    # =====================================================
    # BUILD CHIPS
    # =====================================================

    chip_html = '<div style="margin-bottom:0.7rem;">'

    for item in items:

        color = resolve_chip_color(
            item
        )

        chip_html += f"""

<span style="
display:inline-flex;
align-items:center;
background:#07111F;
border:1px solid {color};
color:{color};
border-radius:999px;
padding:0.28rem 0.65rem;
margin-right:0.45rem;
margin-bottom:0.45rem;
font-size:0.72rem;
font-weight:700;
letter-spacing:0.02em;
white-space:nowrap;
">

{item}

</span>

"""

    chip_html += "</div>"

    # =====================================================
    # RENDER
    # =====================================================

    st.markdown(

        chip_html,

        unsafe_allow_html=True

    )
