# =====================================================
# TIDE LINE — MARINE FORECAST ENGINE
# =====================================================

import requests
import json
import os
import re

from src.marine_api import (
    get_marine_conditions
)


# =====================================================
# CACHE FILE
# =====================================================

CACHE_FILE = "data/marine_cache.json"


# =====================================================
# LOAD CACHE
# =====================================================

def load_cache():

    if not os.path.exists(CACHE_FILE):

        return None

    try:

        with open(CACHE_FILE, "r") as f:

            return json.load(f)

    except:

        return None


# =====================================================
# SAVE CACHE
# =====================================================

def save_cache(data):

    try:

        with open(CACHE_FILE, "w") as f:

            json.dump(data, f)

    except:

        pass


# =====================================================
# ADVISORY DETECTION
# =====================================================

def detect_advisories(text):

    advisories = []

    text = text.lower()

    if "small craft advisory" in text:

        advisories.append(
            "Small Craft Advisory"
        )

    if "hazardous seas" in text:

        advisories.append(
            "Hazardous Seas"
        )

    if "gale warning" in text:

        advisories.append(
            "Gale Warning"
        )

    if "thunderstorm" in text:

        advisories.append(
            "Thunderstorm Activity"
        )

    return advisories


# =====================================================
# DEGREE TO CARDINAL
# =====================================================

def degrees_to_cardinal(deg):

    try:

        deg = float(deg)

    except:

        return "UNKNOWN"

    directions = [

        "N",
        "NE",
        "E",
        "SE",
        "S",
        "SW",
        "W",
        "NW"

    ]

    index = round(deg / 45) % 8

    return directions[index]


# =====================================================
# NORMALIZE WIND SPEED
# =====================================================

def normalize_wind_speed(value):

    try:

        numbers = re.findall(

            r"\d+",

            str(value)

        )

        if not numbers:

            return 0

        numbers = [

            int(n)

            for n in numbers

        ]

        return round(

            sum(numbers) / len(numbers),

            1

        )

    except:

        return 0


# =====================================================
# FALLBACK RESPONSE
# =====================================================

def fallback_response(

    message="Marine systems unavailable."

):

    cache = load_cache()

    if cache:

        cache["forecast"]["details"] = (

            f"CACHED MARINE STATE | {message}"

        )

        return cache

    return {

        "forecast": {

            "headline": "Marine Offline",

            "details": message

        },

        "wind": {

            "speed_mph": 0,

            "direction": "UNKNOWN"

        },

        "sea_state": {

            "wave_height_ft": 0,

            "wave_period_sec": 0,

            "swell_height_ft": 0,

            "swell_period_sec": 0,

            "swell_direction": "UNKNOWN"

        },

        "advisories": []

    }


# =====================================================
# MAIN MARINE SYNTHESIS ENGINE
# =====================================================

def get_marine_forecast():

    lat = 26.9342
    lon = -80.0942

    point_url = (

        f"https://api.weather.gov/points/"
        f"{lat},{lon}"

    )

    try:

        # =================================================
        # NOAA POINT API
        # =================================================

        point_response = requests.get(

            point_url,

            timeout=6,

            headers={
                "User-Agent":
                "TideLineMarineIntel/1.0"
            }

        )

        if point_response.status_code != 200:

            return fallback_response(

                f"NOAA Point API "
                f"{point_response.status_code}"

            )

        point_data = point_response.json()

        forecast_url = point_data[
            "properties"
        ].get(
            "forecast"
        )

        # =================================================
        # NOAA FORECAST
        # =================================================

        response = requests.get(

            forecast_url,

            timeout=6,

            headers={
                "User-Agent":
                "TideLineMarineIntel/1.0"
            }

        )

        if response.status_code != 200:

            return fallback_response(

                f"NOAA Forecast "
                f"{response.status_code}"

            )

        data = response.json()

        periods = data[
            "properties"
        ].get(
            "periods",
            []
        )

        if not periods:

            return fallback_response(
                "No NOAA forecast periods."
            )

        current = periods[0]

        details = current.get(
            "detailedForecast",
            ""
        )

        short = current.get(
            "shortForecast",
            ""
        )

        raw_wind_speed = current.get(
            "windSpeed",
            "0 mph"
        )

        wind_speed = normalize_wind_speed(
            raw_wind_speed
        )

        wind_direction = current.get(
            "windDirection",
            "UNKNOWN"
        )

        # =================================================
        # OPEN METEO / SWELL ENGINE
        # =================================================

        marine = get_marine_conditions()

        if not marine:

            return fallback_response(
                "Marine swell engine failed."
            )

        wave_height = marine.get(
            "wave_height",
            0
        )

        wave_period = marine.get(
            "wave_period",
            0
        )

        swell_height = marine.get(
            "swell_height",
            0
        )

        swell_period = marine.get(
            "swell_period",
            0
        )

        swell_direction = degrees_to_cardinal(

            marine.get(
                "swell_direction",
                0
            )

        )

        # =================================================
        # ADVISORIES
        # =================================================

        advisories = detect_advisories(
            details
        )

        # =================================================
        # FINAL MARINE STATE
        # =================================================

        marine_state = {

            "forecast": {

                "headline": short,

                "details": details

            },

            "wind": {

                "speed_mph": wind_speed,

                "direction": wind_direction

            },

            "sea_state": {

                "wave_height_ft": wave_height,

                "wave_period_sec": wave_period,

                "swell_height_ft": swell_height,

                "swell_period_sec": swell_period,

                "swell_direction": swell_direction

            },

            "advisories": advisories

        }

        # =================================================
        # CACHE STATE
        # =================================================

        save_cache(marine_state)

        return marine_state

    except Exception as e:

        return fallback_response(
            str(e)
        )


# =====================================================
# LOCAL TEST
# =====================================================

if __name__ == "__main__":

    result = get_marine_forecast()

    print(

        json.dumps(

            result,

            indent=2

        )

    )
