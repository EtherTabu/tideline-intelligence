# =========================================================
# TIDE LINE — LIVE CAMERA WALL
# =========================================================

import streamlit as st

from src.config.camera_registry import CAMERA_REGISTRY


# =========================================================
# RISK COLOR
# =========================================================

def get_risk_status(risk):

    risk = str(risk).upper()

    if risk == "HIGH":
        return "error"

    if risk == "MODERATE":
        return "warning"

    return "success"


# =========================================================
# CAMERA CARD
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

    provider = camera.get(
        "provider",
        "UNKNOWN"
    )

    embed_mode = camera.get(
        "embed_mode",
        "search_only"
    )

    embed_url = camera.get(
        "embed_url",
        ""
    )

    watch_url = camera.get(
        "watch_url",
        ""
    )

    # =====================================================
    # CARD
    # =====================================================

    with st.container(border=True):

        st.markdown(
            f"### 📡 {name}"
        )

        st.caption(
            f"{location} • {provider}"
        )

        # =================================================
        # RISK
        # =================================================

        risk_mode = get_risk_status(risk)

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
        # VIDEO
        # =================================================

        if embed_mode == "youtube_embed":

            st.video(embed_url)

        else:

            st.info(
                "External tactical feed"
            )

        # =================================================
        # INTEL
        # =================================================

        if intel:

            st.caption(intel)

        # =================================================
        # BUTTON
        # =================================================

        if watch_url:

            st.link_button(
                "OPEN LIVE FEED",
                watch_url,
                use_container_width=True
            )


# =========================================================
# MAIN WALL
# =========================================================

def show_camera_wall():

    st.subheader(
        "📹 LIVE INLET INTEL"
    )

    st.caption(
        "Real-time inlet verification • traffic • tide flow • launch conditions"
    )

    cols = st.columns(2)

    for index, camera in enumerate(CAMERA_REGISTRY):

        with cols[index % 2]:

            render_camera(camera)