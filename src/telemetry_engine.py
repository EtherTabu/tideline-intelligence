# =========================================================
# TIDE LINE — CANONICAL TELEMETRY ENGINE
# =========================================================

from src.marine_api import (
    get_marine_conditions
)

from src.buoy import (
    get_regional_marine_data
)


# =========================================================
# MASTER TELEMETRY ENGINE
# =========================================================

def build_telemetry():

    # =====================================================
    # INGEST RAW SOURCES
    # =====================================================

    marine_api = get_marine_conditions() or {}

    buoy_data = get_regional_marine_data() or {}

    # =====================================================
    # NORMALIZED REGIONAL CONTRACT
    # =====================================================

    telemetry = {

        # =================================================
        # REGIONAL BUOY NETWORK
        # =================================================

        "regional": {

            "wave_height_ft": buoy_data.get(
                "regional_wave_height_ft",
                marine_api.get(
                    "wave_height",
                    0
                )
            ),

            "wave_period_sec": buoy_data.get(
                "regional_swell_period_sec",
                marine_api.get(
                    "wave_period",
                    0
                )
            ),

            "wind_speed_kt": buoy_data.get(
                "regional_wind_speed_kt",
                0
            ),

            "rating": buoy_data.get(
                "regional_rating",
                "UNKNOWN"
            )

        },

        # =================================================
        # STATION NETWORK
        # =================================================

        "stations": {

            "active": buoy_data.get(
                "stations_active",
                0
            ),

            "offline": buoy_data.get(
                "stations_offline",
                0
            ),

            "health": buoy_data.get(
                "network_health",
                "ONLINE"
            )

        }

    }

    return telemetry


# =========================================================
# LOCAL TEST
# =========================================================

if __name__ == "__main__":

    telemetry = build_telemetry()

    print("\n========== TELEMETRY ==========\n")

    print(telemetry)

    print("\n================================\n")
