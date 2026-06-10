# =========================================================
# TIDE LINE — TACTICAL INTELLIGENCE PANEL
# =========================================================

import streamlit as st

from components.ui.tactical_card import (

    tactical_title,
    tactical_metric,

    tactical_status,
    tactical_divider,

    tactical_label

)


# =========================================================
# PANEL
# =========================================================

def show_tactical_panel(tactical_data):

    # =====================================================
    # SAFE EXTRACTION
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
    # MAIN HEADER
    # =====================================================

    tactical_title(

        "🛡 Tactical Intelligence",

        "LIVE OPERATIONAL SYNTHESIS"

    )

    # =====================================================
    # STATUS
    # =====================================================

    if mission_status == "PRIME":

        tactical_status(

            f"PRIME CONDITIONS • TARGET: {primary_target}",

            "normal"

        )

    elif mission_status == "MONITOR":

        tactical_status(

            f"MONITOR CONDITIONS • TARGET: {primary_target}",

            "warning"

        )

    else:

        tactical_status(

            f"HIGH RISK CONDITIONS • TARGET: {primary_target}",

            "danger"

        )

    st.caption(summary)

    tactical_divider()

    # =====================================================
    # GRID
    # =====================================================

    left_col, right_col = st.columns([1, 1])

    # =====================================================
    # LEFT SIDE
    # =====================================================

    with left_col:

        tactical_label(
            "MISSION INTELLIGENCE"
        )

        r1c1, r1c2 = st.columns(2)

        with r1c1:

            tactical_metric(
                "CONFIDENCE",
                f"{confidence}%",
                "#00FF99"
            )

            tactical_metric(
                "RISK",
                risk_state,
                "#FFD24A"
            )

        with r1c2:

            tactical_metric(
                "TARGET",
                primary_target,
                "#38BDF8"
            )

            tactical_metric(
                "SCORE",
                primary_score,
                "#C084FC"
            )

        tactical_divider()

        tactical_metric(
            "LAUNCH",
            launch_viability,
            "#00D1FF"
        )

        tactical_metric(
            "TRAFFIC",
            traffic_level,
            "#FFFFFF"
        )

        # =================================================
        # FEEDING WINDOW
        # =================================================

        tactical_label(
            "FEEDING WINDOW"
        )

        tactical_status(
            feeding_window,
            "normal"
        )

        st.caption(
            "Peak projected feeding activity."
        )

        tactical_divider()

        # =================================================
        # STRIKE WINDOWS
        # =================================================

        tactical_label(
            "STRIKE WINDOWS"
        )

        if strike_windows:

            for window in strike_windows:

                tactical_status(

                    f"{window.get('window')} • "
                    f"{window.get('confidence')}% CONFIDENCE",

                    "normal"

                )

        else:

            tactical_status(
                "NO STRIKE WINDOWS DETECTED",
                "warning"
            )

        tactical_divider()

        # =================================================
        # BAIT MIGRATION
        # =================================================

        tactical_label(
            "BAIT MIGRATION"
        )

        if bait_activity:

            for item in bait_activity:

                st.markdown(
                    f"• {item}"
                )

        else:

            st.caption(
                "No bait migration signals detected."
            )

    # =====================================================
    # RIGHT SIDE
    # =====================================================

    with right_col:

        tactical_label(
            "OPERATIONAL ALERTS"
        )

        # =================================================
        # SAFE ALERT HANDLER
        # =================================================

        if alerts:

            for alert in alerts:

                # =========================================
                # DICT ALERTS
                # =========================================

                if isinstance(alert, dict):

                    message = alert.get(
                        "message",
                        "Operational alert detected."
                    )

                    level = str(
                        alert.get(
                            "level",
                            "TACTICAL"
                        )
                    ).upper()

                    if level in ["DANGER", "CRITICAL"]:

                        ui_level = "danger"

                    elif level in ["WARNING", "CAUTION"]:

                        ui_level = "warning"

                    else:

                        ui_level = "normal"

                    tactical_status(
                        message,
                        ui_level
                    )

                # =========================================
                # STRING ALERTS
                # =========================================

                else:

                    tactical_status(
                        str(alert),
                        "warning"
                    )

        else:

            tactical_status(
                "NO OPERATIONAL ALERTS",
                "normal"
            )

        tactical_divider()

        # =================================================
        # SYSTEM HEALTH
        # =================================================

        tactical_label(
            "SYSTEM HEALTH"
        )

        h1, h2 = st.columns(2)

        with h1:

            tactical_metric(
                "NOAA",
                system_health.get(
                    "noaa",
                    "UNKNOWN"
                ),
                "#00FF99"
            )

            tactical_metric(
                "TELEMETRY",
                system_health.get(
                    "telemetry",
                    "UNKNOWN"
                ),
                "#38BDF8"
            )

        with h2:

            tactical_metric(
                "BUOYS",
                system_health.get(
                    "buoys",
                    "UNKNOWN"
                ),
                "#C084FC"
            )

            tactical_metric(
                "ENGINE",
                system_health.get(
                    "prediction",
                    "UNKNOWN"
                ),
                "#FFD24A"
            )

    # =====================================================
    # STRATEGIC EVOLUTION
    # =====================================================

    tactical_divider()

    tactical_title(

        "🚀 Strategic System Evolution",

        "NEXT-GENERATION MARINE INTELLIGENCE"

    )

    e1, e2, e3 = st.columns(3)

    with e1:

        tactical_label(
            "SENSOR LAYER"
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

    with e2:

        tactical_label(
            "INTERPRETATION LAYER"
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

    with e3:

        tactical_label(
            "AI STRATEGIC LAYER"
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