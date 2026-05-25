import streamlit as st


# =========================================================
# TIDE LINE — STRIKE TIMELINE
# =========================================================

def show_strike_timeline(

    tactical

):

    # =====================================================
    # STRIKE WINDOWS
    # =====================================================

    strike_windows = tactical.get(
        "strike_windows",
        []
    )

    st.markdown(
        "## ⏱️ Strike Timeline"
    )

    # =====================================================
    # NO DATA FAILSAFE
    # =====================================================

    if not strike_windows:

        st.warning(
            "No strike intelligence available."
        )

        return

    # =====================================================
    # PRIMARY WINDOW
    # =====================================================

    primary = strike_windows[0]

    score = primary.get(
        "score",
        0
    )

    state = primary.get(
        "state",
        "UNKNOWN"
    )

    summary = primary.get(
        "summary",
        "No tactical summary."
    )

    tide_direction = primary.get(
        "tide_direction",
        "UNKNOWN"
    )

    tide_velocity = primary.get(
        "tide_velocity",
        "UNKNOWN"
    )

    # =====================================================
    # LAYOUT
    # =====================================================

    col1, col2, col3 = st.columns(3)

    # =====================================================
    # COLUMN 1
    # =====================================================

    with col1:

        st.metric(
            "Strike State",
            state
        )

        st.progress(
            min(score / 100, 1.0)
        )

    # =====================================================
    # COLUMN 2
    # =====================================================

    with col2:

        st.metric(
            "Tide Direction",
            tide_direction
        )

        st.metric(
            "Tide Velocity",
            tide_velocity
        )

    # =====================================================
    # COLUMN 3
    # =====================================================

    with col3:

        st.metric(
            "Strike Score",
            f"{score}%"
        )

        # ================================================
        # STATE COLORING
        # ================================================

        if state == "EXTREME":

            st.success(summary)

        elif state == "HIGH":

            st.info(summary)

        elif state == "MODERATE":

            st.warning(summary)

        else:

            st.error(summary)
