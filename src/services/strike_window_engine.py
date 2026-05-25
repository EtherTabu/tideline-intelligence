# =========================================================
# TIDE LINE — STRIKE WINDOW ENGINE
# =========================================================

from datetime import datetime


# =========================================================
# BUILD STRIKE WINDOWS
# =========================================================

def build_strike_windows(

    prediction,
    tides,
    marine,
    risk

):

    windows = []

    # =====================================================
    # SAFE CONTRACT ACCESS
    # =====================================================

    current = tides.get(
        "current",
        {}
    )

    sea_state = marine.get(
        "sea_state",
        {}
    )

    feeding_score = prediction.get(
        "feeding_score",
        0
    )

    danger_score = risk.get(
        "danger_score",
        0
    )

    tide_direction = current.get(
        "direction",
        "UNKNOWN"
    )

    tide_velocity = current.get(
        "velocity",
        "UNKNOWN"
    )

    wave_height = sea_state.get(
        "wave_height_ft",
        0
    )

    wave_period = sea_state.get(
        "wave_period_sec",
        0
    )

    # =====================================================
    # SCORE ENGINE
    # =====================================================

    strike_score = 0

    # Feeding pressure
    strike_score += feeding_score * 0.45

    # Tide positioning
    if tide_direction == "INCOMING":

        strike_score += 20

    # Velocity bonus
    if tide_velocity == "STRONG":

        strike_score += 15

    elif tide_velocity == "MODERATE":

        strike_score += 8

    # Wave quality
    if wave_height <= 3:

        strike_score += 10

    if wave_period >= 5:

        strike_score += 10

    # Danger suppression
    strike_score -= danger_score * 0.35

    # Clamp
    strike_score = max(
        0,
        min(
            int(strike_score),
            100
        )
    )

    # =====================================================
    # WINDOW CLASSIFICATION
    # =====================================================

    if strike_score >= 85:

        state = "EXTREME"

        summary = (
            "Major predator activation window."
        )

    elif strike_score >= 70:

        state = "HIGH"

        summary = (
            "Strong feeding opportunity."
        )

    elif strike_score >= 50:

        state = "MODERATE"

        summary = (
            "Viable tactical conditions."
        )

    else:

        state = "LOW"

        summary = (
            "Weak strike alignment."
        )

    # =====================================================
    # BUILD WINDOW
    # =====================================================

    windows.append({

        "timestamp": datetime.utcnow().isoformat(),

        "score": strike_score,

        "state": state,

        "summary": summary,

        "tide_direction": tide_direction,

        "tide_velocity": tide_velocity

    })

    return windows
