import requests


# =====================================================
# JUPITER OFFSHORE COORDINATES
# =====================================================

LAT = 26.937
LON = -79.989


# =====================================================
# OPEN METEO MARINE ENGINE
# =====================================================

def get_marine_conditions():

    url = (

        "https://marine-api.open-meteo.com/v1/marine?"

        f"latitude={LAT}"
        f"&longitude={LON}"

        "&hourly="

        "wave_height,"
        "wave_direction,"
        "wave_period,"

        "swell_wave_height,"
        "swell_wave_direction,"
        "swell_wave_period"

        "&timezone=auto"

    )

    try:

        response = requests.get(
            url,
            timeout=8
        )

        data = response.json()

        hourly = data["hourly"]

        return {

            "wave_height": round(
                hourly["wave_height"][0],
                1
            ),

            "wave_direction":
                hourly["wave_direction"][0],

            "wave_period": round(
                hourly["wave_period"][0],
                1
            ),

            "swell_height": round(
                hourly["swell_wave_height"][0],
                1
            ),

            "swell_direction":
                hourly["swell_wave_direction"][0],

            "swell_period": round(
                hourly["swell_wave_period"][0],
                1
            )

        }

    except Exception as e:

        print(
            f"[MARINE API ERROR] {e}"
        )

        return None
