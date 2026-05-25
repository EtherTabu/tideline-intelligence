# =========================================================
# TIDE LINE — PRIORITY ENGINE
# =========================================================

def build_priority_state(

    prediction,
    risk,
    tactical

):

    feeding_score = prediction.get(
        "feeding_score",
        0
    )

    danger_score = risk.get(
        "danger_score",
        0
    )

    alerts = tactical.get(
        "alerts",
        []
    )

    # =====================================================
    # CRITICAL RISK
    # =====================================================

    if danger_score >= 70:

        return {

            "state": "RISK PRIORITY",

            "color": "red",

            "summary": (
                "Operational danger dominating mission profile."
            )

        }

    # =====================================================
    # EXTREME FEEDING
    # =====================================================

    if feeding_score >= 85:

        return {

            "state": "TACTICAL OPPORTUNITY",

            "color": "green",

            "summary": (
                "Major feeding alignment detected."
            )

        }

    # =====================================================
    # MODERATE
    # =====================================================

    if feeding_score >= 60:

        return {

            "state": "ACTIVE CONDITIONS",

            "color": "orange",

            "summary": (
                "Moderate tactical opportunity developing."
            )

        }

    # =====================================================
    # DEFAULT
    # =====================================================

    return {

        "state": "MONITOR",

        "color": "blue",

        "summary": (
            "Conditions stable but limited."
        )

    }
