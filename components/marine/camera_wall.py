# =========================================================
# TIDE LINE — TACTICAL CAMERA GRID
# =========================================================

import streamlit as st

from datetime import datetime

from src.config.camera_registry import CAMERA_REGISTRY


# =========================================================
# GLOBAL VIDEO STYLE
# =========================================================

st.markdown(
    """
    <style>

    video {
        border-radius: 14px !important;
        overflow: hidden !important;
    }

    iframe {
        border-radius: 14px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# STATUS COLOR
# =========================================================

def get_risk_status(risk):

    risk = str(risk).upper()

    if risk == "HIGH":
        return "error"

    if risk == "MODERATE":
        return "warning"

    return "success"


# =========================================================
# HEADER BLOCK
# =========================================================

def render_header():

    st.markdown(

        """
<div style="
margin-top:0.25rem;
margin-bottom:0.45rem;
">

<div style="
color:#D7E7FF;
font-size:1.05rem;
font-weight:800;
letter-spacing:0.03em;
margin-bottom:0.15rem;
">

📹 LIVE INLET INTEL

</div>

<div style="
color:#7D8EA3;
font-size:0.72rem;
letter-spacing:0.04em;
">

REAL-TIME INLET VERIFICATION • VESSEL FLOW • LAUNCH CONDITIONS

</div>

</div>
        """,

        unsafe_allow_html=True

    )


# =========================================================
# CAMERA NODE
# =========================================================

def render_camera(camera):

    name = camera.get(
        "name",
        "UNKNOWN"
    )

    location = camera.get(
        "location",
        "UNKNOWN"
    )

    risk = camera.get(
        "risk",
        "LOW"
    )

    intel = camera.get(
        "intel",
        ""
    )

    video_url = camera.get(
        "video_url",
        ""
    )

    watch_url = camera.get(
        "watch_url",
        ""
    )

    risk_mode = get_risk_status(risk)

    clock = datetime.now().strftime("%H:%M:%S")

    # =====================================================
    # NODE
    # =====================================================

    with st.container(border=True):

        # =================================================
        # TITLE
        # =================================================

        st.markdown(

            f"""
<div style="
margin-bottom:0.35rem;
">

<div style="
color:#E6F0FF;
font-size:0.95rem;
font-weight:800;
margin-bottom:0.12rem;
">

📡 {name}

</div>

<div style="
color:#7D8EA3;
font-size:0.68rem;
letter-spacing:0.03em;
">

{location}

</div>

</div>
            """,

            unsafe_allow_html=True

        )

        # =================================================
        # LIVE CLOCK
        # =================================================

        st.caption(
            f"LIVE FEED • {clock}"
        )

        # =================================================
        # LIVE VIDEO / COMMS NODE
        # =================================================

        if video_url == "COMMS_NODE":

            st.markdown(

                """
<div style="
background:linear-gradient(135deg,#081018,#0B2239);
border:1px solid rgba(0,255,180,0.18);
border-radius:14px;
padding:1.2rem;
height:320px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:flex-start;
">

<div style="
color:#00FFC6;
font-size:1.1rem;
font-weight:800;
margin-bottom:1rem;
letter-spacing:0.05em;
">
📡 LIVE MARINE COMMS
</div>

<div style="
color:#D7E7FF;
font-size:0.88rem;
margin-bottom:0.6rem;
">
CHANNEL 16 ACTIVE
</div>

<div style="
color:#7EE7FF;
font-size:0.82rem;
margin-bottom:0.35rem;
">
• PORT MIAMI VESSEL TRAFFIC
</div>

<div style="
color:#7EE7FF;
font-size:0.82rem;
margin-bottom:0.35rem;
">
• HARBOR OPS MONITORING
</div>

<div style="
color:#7EE7FF;
font-size:0.82rem;
margin-bottom:0.35rem;
">
• COMMERCIAL MOVEMENT DETECTED
</div>

<div style="
color:#7EE7FF;
font-size:0.82rem;
margin-bottom:0.35rem;
">
• USCG COMMUNICATION BAND ACTIVE
</div>

<div style="
margin-top:1rem;
color:#00FF9C;
font-size:0.9rem;
font-weight:700;
">
● LIVE SIGNAL
</div>

</div>
                """,

                unsafe_allow_html=True

            )

            # =============================================
            # SIGNAL QUALITY
            # =============================================

            st.progress(92)

            st.caption(
                "SIGNAL QUALITY"
            )

            # =============================================
            # OPEN FEED
            # =============================================

            if watch_url:

                st.link_button(

                    "OPEN LIVE HARBOR FEED",

                    watch_url,

                    use_container_width=True

                )

        elif video_url:

            st.video(
                video_url,
                autoplay=True,
                muted=True
            )

            # =============================================
            # SIGNAL QUALITY
            # =============================================

            st.progress(96)

            st.caption(
                "SIGNAL QUALITY"
            )

        # =================================================
        # RISK BAR
        # =================================================

        if risk_mode == "error":

            st.error(
                f"{risk} RISK"
            )

        elif risk_mode == "warning":

            st.warning(
                f"{risk} RISK"
            )

        else:

            st.success(
                f"{risk} RISK"
            )

        # =================================================
        # INTEL
        # =================================================

        if intel:

            st.caption(
                intel
            )


# =========================================================
# MAIN WALL
# =========================================================

def show_camera_wall():

    render_header()

    left_col, right_col = st.columns(
        [1, 1]
    )

    for index, camera in enumerate(CAMERA_REGISTRY):

        with (
            left_col
            if index % 2 == 0
            else right_col
        ):

            render_camera(camera)