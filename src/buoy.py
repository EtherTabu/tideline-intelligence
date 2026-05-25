import requests
import re


# =====================================================
# REGIONAL OFFSHORE SENSOR NETWORK
# =====================================================

BUOY_IDS = [

    "41009",   # Canaveral Offshore
    "LKWF1"    # Lake Worth Pier

]


# =====================================================
# DEGREE → 16 POINT CARDINAL
# =====================================================

def degrees_to_cardinal(deg):

    try:

        deg = float(deg)

    except:

        return "UNKNOWN"

    directions = [

        "N",
        "NNE",
        "NE",
        "ENE",
        "E",
        "ESE",
        "SE",
        "SSE",
        "S",
        "SSW",
        "SW",
        "WSW",
        "W",
        "WNW",
        "NW",
        "NNW"

    ]

    index = round(deg / 22.5) % 16

    return directions[index]


# =====================================================
# SAFE FLOAT PARSER
# =====================================================

def safe_float(value, default=0.0):

    try:

        if value in [

            "MM",
            "999",
            "999.0",
            "99.0",
            None,
            ""

        ]:

            return default

        return float(value)

    except:

        return default


# =====================================================
# CONDITIONS ENGINE
# =====================================================

def calculate_conditions(

    wave_height,
    wind_speed,
    swell_period

):

    if (

        wave_height <= 2
        and wind_speed <= 10
        and swell_period >= 8

    ):

        return "EXCELLENT"

    elif (

        wave_height <= 4
        and wind_speed <= 15

    ):

        return "GOOD"

    elif (

        wave_height <= 6

    ):

        return "CAUTION"

    else:

        return "DANGEROUS"


# =====================================================
# FETCH SINGLE BUOY
# =====================================================

def fetch_single_buoy(buoy_id):

    url = (
        f"https://www.ndbc.noaa.gov/data/realtime2/"
        f"{buoy_id}.txt"
    )

    try:

        response = requests.get(
            url,
            timeout=8
        )

        response.raise_for_status()

        lines = response.text.splitlines()

        if len(lines) < 3:

            return None

        headers = re.split(
            r"\s+",
            lines[0].replace("#", "").strip()
        )

        values = None

        for line in lines[2:]:

            row = re.split(
                r"\s+",
                line.strip()
            )

            if len(row) == len(headers):

                values = row
                break

        if not values:

            return None

        data = dict(zip(headers, values))

        timestamp = (

            f"{data.get('YY')}-"
            f"{data.get('MM')}-"
            f"{data.get('DD')} "
            f"{data.get('hh')}:"
            f"{data.get('mm')}"

        )

        wave_height = safe_float(
            data.get("WVHT")
        )

        swell_period = safe_float(
            data.get("DPD")
        )

        average_period = safe_float(
            data.get("APD")
        )

        swell_direction_deg = safe_float(
            data.get("MWD")
        )

        wind_direction_deg = safe_float(
            data.get("WDIR")
        )

        wind_speed = safe_float(
            data.get("WSPD")
        )

        gust = safe_float(
            data.get("GST")
        )

        pressure = safe_float(
            data.get("PRES")
        )

        water_temp = safe_float(
            data.get("WTMP")
        )

        air_temp = safe_float(
            data.get("ATMP")
        )

        swell_direction = degrees_to_cardinal(
            swell_direction_deg
        )

        wind_direction = degrees_to_cardinal(
            wind_direction_deg
        )

        marine_rating = calculate_conditions(

            wave_height,
            wind_speed,
            swell_period

        )

        return {

            "station": buoy_id,

            "timestamp_utc": timestamp,

            "marine_rating": marine_rating,

            "wave_height_ft": round(
                wave_height,
                1
            ),

            "dominant_period_sec": round(
                swell_period,
                1
            ),

            "average_period_sec": round(
                average_period,
                1
            ),

            "swell_direction": swell_direction,

            "wind_direction": wind_direction,

            "wind_speed_kt": round(
                wind_speed
            ),

            "gust_kt": round(
                gust
            ),

            "water_temp_f": round(
                water_temp
            ),

            "air_temp_f": round(
                air_temp
            ),

            "pressure_mb": round(
                pressure,
                1
            )

        }

    except Exception as e:

        print(
            f"[BUOY ERROR - {buoy_id}] {e}"
        )

        return None


# =====================================================
# REGIONAL SYNTHESIS ENGINE
# =====================================================

def get_regional_marine_data():

    buoy_results = []

    for buoy_id in BUOY_IDS:

        result = fetch_single_buoy(
            buoy_id
        )

        if result:

            buoy_results.append(
                result
            )

    if not buoy_results:

        return {

            "regional_wave_height_ft": 0,

            "regional_swell_period_sec": 0,

            "dominant_swell_direction": "N",

            "regional_wind_speed_kt": 0,

            "regional_rating": "UNKNOWN",

            "stations_active": 0,

            "stations": []

        }

    valid_wave_heights = [

        b["wave_height_ft"]

        for b in buoy_results

        if b["wave_height_ft"] > 0

    ]

    valid_periods = [

        b["dominant_period_sec"]

        for b in buoy_results

        if b["dominant_period_sec"] > 0

    ]

    valid_winds = [

        b["wind_speed_kt"]

        for b in buoy_results

    ]

    regional_wave_height = round(

        sum(valid_wave_heights)
        / max(len(valid_wave_heights), 1),

        1

    )

    regional_swell_period = round(

        sum(valid_periods)
        / max(len(valid_periods), 1),

        1

    )

    regional_wind_speed = round(

        sum(valid_winds)
        / len(valid_winds)

    )

    dominant_station = max(

        buoy_results,

        key=lambda x: x["wave_height_ft"]

    )

    dominant_swell_direction = dominant_station[
        "swell_direction"
    ]

    regional_rating = calculate_conditions(

        regional_wave_height,
        regional_wind_speed,
        regional_swell_period

    )

    return {

        "regional_wave_height_ft":
            regional_wave_height,

        "regional_swell_period_sec":
            regional_swell_period,

        "dominant_swell_direction":
            dominant_swell_direction,

        "regional_wind_speed_kt":
            regional_wind_speed,

        "regional_rating":
            regional_rating,

        "stations_active":
            len(buoy_results),

        "stations":
            buoy_results

    }


# =====================================================
# LOCAL TEST
# =====================================================

if __name__ == "__main__":

    data = get_regional_marine_data()

    print("\n========== REGIONAL MARINE ENGINE ==========\n")

    for k, v in data.items():

        print(f"{k}: {v}")

    print("\n============================================\n")
