# =========================================================
# TIDE LINE — CONFIDENCE RING
# =========================================================

import streamlit as st


# =========================================================
# COLOR ENGINE
# =========================================================

def resolve_ring_color(value):

    if value >= 85:

        return "#27F5A3"

    if value >= 70:

        return "#00D4FF"

    if value >= 55:

        return "#FFD166"

    return "#FF5C7A"


# =========================================================
# RENDER RING
# =========================================================

def render_confidence_ring(

    label,
    value

):

    color = resolve_ring_color(
        value
    )

    st.markdown(

        f"""

        <div style="
            display:flex;
            flex-direction:column;
            align-items:center;
            justify-content:center;
            margin-bottom:1rem;
        ">

            <div style="
                width:120px;
                height:120px;
                border-radius:50%;
                background:
                    radial-gradient(
                        closest-side,
                        #07111F 78%,
                        transparent 80% 100%
                    ),
                    conic-gradient(
                        {color} {value}%,
                        #1F2937 0
                    );
                display:flex;
                align-items:center;
                justify-content:center;
                box-shadow:0 0 18px {color}55;
                border:1px solid #13304A;
            ">

                <div style="
                    color:{color};
                    font-size:1.4rem;
                    font-weight:800;
                ">

                    {value}%

                </div>

            </div>

            <div style="
                color:#9FB3C8;
                margin-top:0.6rem;
                font-size:0.82rem;
                font-weight:700;
                letter-spacing:0.05em;
            ">

                {label}

            </div>

        </div>

        """,

        unsafe_allow_html=True

    )
