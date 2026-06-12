# =========================================================
# TIDE LINE — REFRESH ENGINE
# =========================================================

import streamlit as st

from datetime import datetime

from components.telemetry.pulse_status import (
    show_pulse_status
)


# =========================================================
# REFRESH STATUS
# =========================================================

def show_refresh_status():

    current_time = datetime.now().strftime(
        "%H:%M:%S"
    )

    # =====================================================
    # LIVE PULSE GRID
    # =====================================================

    p1, p2, p3, p4 = st.columns(4)

    with p1:

        show_pulse_status(
            "NOAA ONLINE",
            "#27F5A3"
        )

    with p2:

        show_pulse_status(
            "BUOY SYNC",
            "#00D4FF"
        )

    with p3:

        show_pulse_status(
            "RADAR ACTIVE",
            "#FFD166"
        )

    with p4:

        show_pulse_status(
            "STRIKE WINDOWS",
            "#FF9F43"
        )

    # =====================================================
    # STATUS BAR
    # =====================================================

    st.markdown(

        f"""

        <div style="
            background:#07111F;
            border:1px solid #13304A;
            border-radius:12px;
            padding:0.75rem 1rem;
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
                    color:#27F5A3;
                    font-weight:700;
                    font-size:0.82rem;
                    letter-spacing:0.05em;
                ">

                    ● LIVE TELEMETRY ACTIVE

                </div>

                <div style="
                    color:#3BD6FF;
                    font-size:0.82rem;
                    font-weight:600;
                ">

                    MARINE INTELLIGENCE NETWORK ACTIVE

                </div>

                <div style="
                    color:#9FB3C8;
                    font-size:0.8rem;
                ">

                    LAST SYNC: {current_time}

                </div>

            </div>

        </div>

        """,

        unsafe_allow_html=True

    )


# =========================================================
# AUTO REFRESH
# =========================================================

def auto_refresh(

    seconds=300

):

    st.markdown(

        f"""

        <script>

            setTimeout(function(){{
                window.location.reload();
            }}, {seconds * 1000});

        </script>

        """,

        unsafe_allow_html=True

    )