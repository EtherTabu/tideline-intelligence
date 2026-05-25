import requests

def get_weather():

    # Jupiter Inlet Coordinates
    lat, lon = 26.9342, -80.0942

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}"
        f"&longitude={lon}"
        f"&current="
        "temperature_2m,"
        "relative_humidity_2m,"
        "apparent_temperature,"
        "is_day,"
        "precipitation,"
        "weather_code,"
        "wind_speed_10m,"
        "wind_direction_10m"
        "&wind_speed_unit=kn"
        "&timezone=auto"
    )

    try:

        response = requests.get(url, timeout=10)

        data = response.json()["current"]

        # WEATHER CONDITIONS
        code = data["weather_code"]

        if code == 0:
            condition = "Clear Skies"
            icon = "☀️"

        elif code in [1, 2, 3]:
            condition = "Partially Cloudy"
            icon = "⛅"

        elif code >= 51:
            condition = "Rain / Squall"
            icon = "🌧️"

        else:
            condition = "Overcast"
            icon = "☁️"

        # RAW VALUES
        wind_speed = round(data["wind_speed_10m"])
        wind_dir = data["wind_direction_10m"]

        return {

            # DISPLAY VALUES
            "temp": f"{round(data['temperature_2m'])}°F",
            "wind": f"{wind_speed} kts",
            "humidity": f"{data['relative_humidity_2m']}%",

            # RAW VALUES FOR LOGIC ENGINE
            "wind_speed": wind_speed,
            "wind_dir": wind_dir,

            # CONDITIONS
            "condition": condition,
            "icon": icon
        }

    except Exception as e:

        print(f"Weather API Error: {e}")

        return None
