# =========================================================
# TIDE LINE — LIVE CLOCK
# =========================================================

import streamlit as st

from datetime import datetime


# =========================================================
# LIVE CLOCK
# =========================================================

def show_live_clock():

    current_time = datetime.now().strftime(
        "%A • %B %d • %H:%M:%S"
    )

    st.markdown(

        f"""

        <div style="
            background:#07111F;
            border:1px solid #13304A;
            border-radius:12px;
            padding:0.85rem 1rem;
            margin-bottom:1rem;
            text-align:center;
        ">

            <div style="
                color:#3BD6FF;
                font-size:0.78rem;
                font-weight:700;
                letter-spacing:0.08em;
                margin-bottom:0.25rem;
            ">

                TIDE LINE COMMAND TIME

            </div>

            <div style="
                color:#E2E8F0;
                font-size:1.15rem;
                font-weight:700;
                letter-spacing:0.03em;
            ">

                {current_time}

            </div>

        </div>

        """,

        unsafe_allow_html=True

    )
