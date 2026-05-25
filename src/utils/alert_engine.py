# =========================================================
# TIDE LINE — ALERT ENGINE
# =========================================================

def classify_alerts(

    risk,
    prediction,
    marine

):

    alerts = []

    # =====================================================
    # SAFE CONTRACT ACCESS
    # =====================================================

    sea_state = marine.get(
        "sea_state",
        {}
    )

    danger_score = risk.get(
        "danger_score",
        0
    )

    wave_height = sea_state.get(
        "wave_height_ft",
        0
    )

    feeding_score = prediction.get(
        "feeding_score",
        0
    )

    activity = prediction.get(
        "activity",
        "UNKNOWN"
    )

    # =====================================================
    # CRITICAL RISK
    # =====================================================

    if danger_score >= 70:

        alerts.append({

            "level": "CRITICAL",

            "message": (
                "High marine danger detected."
            )

        })

    # =====================================================
    # MODERATE RISK
    # =====================================================

    elif danger_score >= 40:

        alerts.append({

            "level": "WARNING",

            "message": (
                "Moderate operational risk detected."
            )

        })

    # =====================================================
    # ELEVATED SEA STATE
    # =====================================================

    if wave_height >= 5:

        alerts.append({

            "level": "WARNING",

            "message": (
                "Elevated sea state reducing operational efficiency."
            )

        })

    # =====================================================
    # MAJOR FEEDING WINDOW
    # =====================================================

    if feeding_score >= 85:

        alerts.append({

            "level": "TACTICAL",

            "message": (
                "Major feeding window active."
            )

        })

    # =====================================================
    # HIGH ACTIVITY
    # =====================================================

    if activity == "HIGH":

        alerts.append({

            "level": "TACTICAL",

            "message": (
                "Strong predator activity detected."
            )

        })

    # =====================================================
    # EXTREME ACTIVITY
    # =====================================================

    if activity == "EXTREME":

        alerts.append({

            "level": "TACTICAL",

            "message": (
                "Extreme feeding conditions developing."
            )

        })

    # =====================================================
    # FALLBACK
    # =====================================================

    if not alerts:

        alerts.append({

            "level": "CLEAR",

            "message": (
                "Operational conditions stable."
            )

        })

    return alerts
