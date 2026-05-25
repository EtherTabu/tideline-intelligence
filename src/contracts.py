# =========================================================
# TIDE LINE — CANONICAL SYSTEM CONTRACTS
# =========================================================


# =========================================================
# MARINE CONTRACT
# =========================================================

MARINE_CONTRACT = {

    "sea_state": {

        "wave_height_ft": 0.0,

        "wave_period_sec": 0.0,

        "swell_height_ft": 0.0,

        "swell_period_sec": 0.0,

        "swell_direction": "UNKNOWN"

    },

    "wind": {

        "speed_mph": 0,

        "direction": "UNKNOWN"

    },

    "forecast": {

        "headline": "UNKNOWN",

        "details": "UNKNOWN"

    },

    "advisories": []

}


# =========================================================
# TIDE CONTRACT
# =========================================================

TIDE_CONTRACT = {

    "current": {

        "direction": "UNKNOWN",

        "velocity": "UNKNOWN",

        "height_ft": 0.0

    },

    "tidal_range_ft": 0.0,

    "slack_windows": [],

    "tides": []

}


# =========================================================
# BUOY CONTRACT
# =========================================================

BUOY_CONTRACT = {

    "regional": {

        "wave_height_ft": 0.0,

        "wave_period_sec": 0.0,

        "wind_speed_kt": 0,

        "rating": "UNKNOWN"

    },

    "stations": {

        "active": 0

    }

}


# =========================================================
# RISK CONTRACT
# =========================================================

RISK_CONTRACT = {

    "danger_score": 0,

    "risk_state": "UNKNOWN",

    "launch_viability": "UNKNOWN",

    "standing_wave_risk": "UNKNOWN",

    "summary": []

}


# =========================================================
# PREDICTION CONTRACT
# =========================================================

PREDICTION_CONTRACT = {

    "feeding_score": 0,

    "activity": "UNKNOWN",

    "bite_window": "UNKNOWN",

    "recommendation": "UNKNOWN",

    "species": {},

    "primary_target": "UNKNOWN",

    "primary_score": 0

}


# =========================================================
# TACTICAL CONTRACT
# =========================================================

TACTICAL_CONTRACT = {

    "mission_status": "MONITOR",

    "confidence": 0,

    "primary_target": "UNKNOWN",

    "primary_score": 0,

    "traffic_level": "UNKNOWN",

    "launch_viability": "UNKNOWN",

    "feeding_window": "UNKNOWN",

    "alerts": [],

    "bait_activity": [],

    "strike_windows": [],

    "summary": "UNKNOWN",

    "risk_state": "UNKNOWN",

    "system_health": {

        "noaa": "UNKNOWN",

        "telemetry": "UNKNOWN",

        "buoys": "UNKNOWN",

        "prediction": "UNKNOWN"

    }

}


# =========================================================
# SYNTHESIS CONTRACT
# =========================================================

SYNTHESIS_CONTRACT = {

    "mission_status": "UNKNOWN",

    "primary_target": "UNKNOWN",

    "confidence": 0,

    "summary": "UNKNOWN"

}
