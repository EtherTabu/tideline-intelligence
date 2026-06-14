# =========================================================
# TIDE LINE — MARINE SERVICE
# =========================================================

import random
from datetime import datetime

from src.utils.logger import logger


# =========================================================
# LIVE MARINE PAYLOAD
# =========================================================

def get_simulated_marine_conditions():

    now = datetime.now()

    logger.info(
        "[MARINE SERVICE] Simulated marine telemetry generated."
    )

    payload = {

        # =============================================
        # SOURCE
        # =============================================

        "source": "SIMULATED",

        "source_type": "simulated",

        "is_simulated": True,

        "_meta": {

            "source": "src.services.marine_service",

            "source_type": "simulated",

            "is_simulated": True

        },

        # =============================================
        # WIND
        # =============================================

        "wind_speed": round(
            random.uniform(8, 22),
            1
        ),

        "wind_direction": random.choice(
            [45, 90, 135, 180, 225]
        ),

        # =============================================
        # WAVES
        # =============================================

        "wave_height": round(
            random.uniform(1.5, 5.5),
            1
        ),

        "wave_period": random.randint(
            4,
            11
        ),

        # =============================================
        # WATER
        # =============================================

        "water_temp": random.randint(
            76,
            84
        ),

        "pressure": random.randint(
            1008,
            1020
        ),

        # =============================================
        # TACTICAL
        # =============================================

        "moon_phase": random.choice(

            [
                "New Moon",
                "Waxing Crescent",
                "First Quarter",
                "Full Moon"
            ]

        ),

        "tide_state": random.choice(

            [
                "Incoming",
                "Outgoing",
                "Slack"
            ]

        ),

        "visibility": random.randint(
            4,
            10
        ),

        # =============================================
        # SOLAR
        # =============================================

        "sunrise": "06:28",

        "sunset": "20:04",

        # =============================================
        # TIMESTAMP
        # =============================================

        "timestamp": now.strftime(
            "%H:%M:%S"
        )

    }

    return payload


# =========================================================
# LEGACY ALIAS
# =========================================================

def get_marine_conditions():

    return get_simulated_marine_conditions()
