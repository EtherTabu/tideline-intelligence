# =========================================================
# TIDE LINE — PULSE STATUS ENGINE
# =========================================================

import streamlit as st


# =========================================================
# PULSE STATUS
# =========================================================

def show_pulse_status(

    label,
    color="#27F5A3"

):

    st.markdown(

        f"""

        <style>

        .pulse-container {{
            display:flex;
            align-items:center;
            gap:0.55rem;
            margin-bottom:0.5rem;
        }}

        .pulse-dot {{

            width:12px;
            height:12px;
            border-radius:50%;
            background:{color};

            box-shadow:
                0 0 0 rgba(39,245,163, 0.7);

            animation:pulse-animation 2s infinite;
        }}

        @keyframes pulse-animation {{

            0% {{
                box-shadow:
                    0 0 0 0 rgba(39,245,163, 0.7);
            }}

            70% {{
                box-shadow:
                    0 0 0 12px rgba(39,245,163, 0);
            }}

            100% {{
                box-shadow:
                    0 0 0 0 rgba(39,245,163, 0);
            }}

        }}

        </style>

        <div class="pulse-container">

            <div class="pulse-dot"></div>

            <div style="
                color:#E2E8F0;
                font-size:0.82rem;
                font-weight:700;
                letter-spacing:0.04em;
            ">

                {label}

            </div>

        </div>

        """,

        unsafe_allow_html=True

    )
