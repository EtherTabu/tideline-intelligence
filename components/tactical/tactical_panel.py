import streamlit as st


# =========================================================
# TIDE LINE — TACTICAL PANEL
# =========================================================

def show_tactical_panel(tactical_data):

    # =====================================================
    # SAFE DATA EXTRACTION
    # =====================================================

    mission_status = tactical_data.get(
        "mission_status",
        "MONITOR"
    )

    confidence = tactical_data.get(
        "confidence",
        0
    )

    primary_target = tactical_data.get(
        "primary_target",
        "UNKNOWN"
    )

    primary_score = tactical_data.get(
        "primary_score",
        0
    )

    traffic_level = tactical_data.get(
        "traffic_level",
        "UNKNOWN"
    )

    launch_viability = tactical_data.get(
        "launch_viability",
        "UNKNOWN"
    )

    feeding_window = tactical_data.get(
        "feeding_window",
        "UNKNOWN"
    )

    risk_state = tactical_data.get(
        "risk_state",
        "UNKNOWN"
    )

    summary = tactical_data.get(
        "summary",
        "No tactical synthesis available."
    )

    alerts = tactical_data.get(
        "alerts",
        []
    )

    bait_activity = tactical_data.get(
        "bait_activity",
        []
    )

    strike_windows = tactical_data.get(
        "strike_windows",
        []
    )

    system_health = tactical_data.get(
        "system_health",
        {}
    )

    # =====================================================
    # HEADER
    # =====================================================

    st.header(
        "🛡️ Tactical Intelligence"
    )

    # =====================================================
    # TOP STATUS BAR
    # =====================================================

    if mission_status == "PRIME":

        st.success(
            f"🟢 PRIME CONDITIONS | "
            f"Primary Target: {primary_target}"
        )

    elif mission_status == "MONITOR":

        st.warning(
            f"🟡 MONITOR CONDITIONS | "
            f"Primary Target: {primary_target}"
        )

    else:

        st.error(
            f"🔴 HIGH RISK CONDITIONS | "
            f"Primary Target: {primary_target}"
        )

    st.info(summary)

    st.divider()

    # =====================================================
    # MAIN GRID
    # =====================================================

    left_col, right_col = st.columns([1, 1])

    # =====================================================
    # LEFT COLUMN
    # =====================================================

    with left_col:

        # =================================================
        # MISSION STATUS
        # =================================================

        st.markdown(
            "### 🎯 Mission Intelligence"
        )

        m1, m2, m3 = st.columns(3)

        with m1:

            st.metric(
                "Confidence",
                f"{confidence}%"
            )

            st.metric(
                "Risk State",
                risk_state
            )

        with m2:

            st.metric(
                "Primary Target",
                primary_target
            )

            st.metric(
                "Target Score",
                primary_score
            )

        with m3:

            st.metric(
                "Launch Status",
                launch_viability
            )

            st.metric(
                "Traffic Level",
                traffic_level
            )

        st.caption(
            "Real-time tactical synthesis engine."
        )

        st.divider()

        # =================================================
        # FEEDING WINDOW
        # =================================================

        st.markdown(
            "### 🌊 Feeding Window"
        )

        st.success(
            feeding_window
        )

        st.caption(
            "Peak projected feeding activity."
        )

        st.divider()

        # =================================================
        # STRIKE WINDOWS
        # =================================================

        st.markdown(
            "### ⏰ Strike Windows"
        )

        if strike_windows:

            for window in strike_windows:

                st.info(

                    f"{window.get('window')} "
                    f"| Confidence: "
                    f"{window.get('confidence')}%"

                )

        else:

            st.warning(
                "No strike windows available."
            )

        st.caption(
            "Projected optimal engagement periods."
        )

        st.divider()

        # =================================================
        # BAIT ACTIVITY
        # =================================================

        st.markdown(
            "### 🐟 Bait Migration"
        )

        if bait_activity:

            for item in bait_activity:

                st.write(f"• {item}")

        else:

            st.info(
                "No bait migration signals detected."
            )

        st.caption(
            "Bait movement strongly impacts "
            "predator positioning."
        )

    # =====================================================
    # RIGHT COLUMN
    # =====================================================

    with right_col:

        # =================================================
        # OPERATIONAL ALERTS
        # =====================================================

        st.markdown(
            "### ⚠️ Operational Alerts"
        )

        if alerts:

            for alert in alerts:

                st.warning(alert)

        else:

            st.success(
                "No operational alerts detected."
            )

        st.caption(
            "Environmental + tactical alert fusion."
        )

        st.divider()

        # =================================================
        # SYSTEM HEALTH
        # =====================================================

        st.markdown(
            "### 📡 System Health"
        )

        s1, s2 = st.columns(2)

        with s1:

            st.metric(
                "NOAA Sync",
                system_health.get(
                    "noaa",
                    "UNKNOWN"
                )
            )

            st.metric(
                "Telemetry",
                system_health.get(
                    "telemetry",
                    "UNKNOWN"
                )
            )

        with s2:

            st.metric(
                "Buoy Network",
                system_health.get(
                    "buoys",
                    "UNKNOWN"
                )
            )

            st.metric(
                "Prediction Engine",
                system_health.get(
                    "prediction",
                    "UNKNOWN"
                )
            )

        st.caption(
            "Operational subsystem integrity."
        )

    # =====================================================
    # COMPACT ROADMAP
    # =====================================================

    st.divider()

    st.markdown(
        "## 🚀 Strategic System Evolution"
    )

    roadmap1, roadmap2, roadmap3 = st.columns(3)

    with roadmap1:

        st.markdown(
            "### 📡 Sensor Layer"
        )

        st.caption(
            """
NOAA tides  
Marine forecast  
Buoy telemetry  
AIS tracking  
Live cameras  
Bathymetric intelligence
"""
        )

    with roadmap2:

        st.markdown(
            "### 🌊 Interpretation Layer"
        )

        st.caption(
            """
Sea-state engine  
Risk synthesis  
Feeding windows  
Standing-wave logic  
Launch viability  
Traffic analysis
"""
        )

    with roadmap3:

        st.markdown(
            "### 🤖 AI Strategic Layer"
        )

        st.caption(
            """
Strike prediction  
Historical memory  
Moon synthesis  
Tournament detection  
Fuel forecasting  
Mission analysis
"""
        )
