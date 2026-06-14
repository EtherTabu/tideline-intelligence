# =========================================================
# TIDE LINE - DASHBOARD TELEMETRY ADAPTER
# =========================================================

from datetime import datetime


CARDINAL_TO_DEGREES = {
    "N": 0,
    "NNE": 23,
    "NE": 45,
    "ENE": 68,
    "E": 90,
    "ESE": 113,
    "SE": 135,
    "SSE": 158,
    "S": 180,
    "SSW": 203,
    "SW": 225,
    "WSW": 248,
    "W": 270,
    "WNW": 293,
    "NW": 315,
    "NNW": 338,
}


def safe_number(value, default=0):

    try:

        return float(value)

    except (TypeError, ValueError):

        return default


def direction_to_degrees(value):

    if isinstance(value, (int, float)):

        return value

    return CARDINAL_TO_DEGREES.get(
        str(value).upper(),
        0
    )


def title_tide_state(value):

    value = str(
        value or "UNKNOWN"
    ).upper()

    if value == "INCOMING":

        return "Incoming"

    if value == "OUTGOING":

        return "Outgoing"

    if value == "SLACK":

        return "Slack"

    return value


def build_dashboard_marine_payload(

    canonical_marine,
    tides,
    buoys,
    simulated_extras=None

):

    canonical_marine = (
        canonical_marine
        if isinstance(canonical_marine, dict)
        else {}
    )
    tides = tides if isinstance(tides, dict) else {}
    buoys = buoys if isinstance(buoys, dict) else {}
    simulated_extras = (
        simulated_extras
        if isinstance(simulated_extras, dict)
        else {}
    )

    sea_state = canonical_marine.get(
        "sea_state",
        {}
    )
    wind = canonical_marine.get(
        "wind",
        {}
    )
    current_tide = tides.get(
        "current",
        {}
    )
    regional = buoys.get(
        "regional",
        {}
    )

    tide_flow = current_tide.get(
        "direction",
        "UNKNOWN"
    )
    tide_velocity = current_tide.get(
        "velocity",
        "UNKNOWN"
    )

    payload = {

        "source": "CANONICAL_DASHBOARD_ADAPTER",

        "source_type": "canonical_adapter",

        "is_simulated": False,

        "simulated_extras": [],

        "timestamp": simulated_extras.get(
            "timestamp",
            datetime.now().strftime("%H:%M:%S")
        ),

        "wave_height": safe_number(
            sea_state.get(
                "wave_height_ft",
                regional.get(
                    "wave_height_ft",
                    0
                )
            )
        ),

        "wave_period": safe_number(
            sea_state.get(
                "wave_period_sec",
                regional.get(
                    "wave_period_sec",
                    0
                )
            )
        ),

        "swell_height": safe_number(
            sea_state.get(
                "swell_height_ft",
                0
            )
        ),

        "swell_period": safe_number(
            sea_state.get(
                "swell_period_sec",
                0
            )
        ),

        "swell_direction": sea_state.get(
            "swell_direction",
            "UNKNOWN"
        ),

        "wind_speed": safe_number(
            wind.get(
                "speed_mph",
                0
            )
        ),

        "wind_direction": direction_to_degrees(
            wind.get(
                "direction",
                "UNKNOWN"
            )
        ),

        "wind_direction_cardinal": wind.get(
            "direction",
            "UNKNOWN"
        ),

        "tide_state": title_tide_state(
            tide_flow
        ),

        "tide_flow": tide_flow,

        "tidal_velocity": tide_velocity,

        "velocity": tide_velocity,

        "tidal_range": tides.get(
            "tidal_range_ft",
            tides.get(
                "tidal_range",
                0
            )
        ),

        "tidal_range_ft": tides.get(
            "tidal_range_ft",
            tides.get(
                "tidal_range",
                0
            )
        ),

        "offshore_rating": regional.get(
            "rating",
            "UNKNOWN"
        ),

        "_meta": {

            "source": "src.services.dashboard_adapter",

            "source_type": "canonical_adapter",

            "is_simulated": False,

            "simulated_extras": []

        }

    }

    for key in [
        "water_temp",
        "pressure",
        "moon_phase",
        "visibility",
        "sunrise",
        "sunset",
    ]:

        if key in simulated_extras:

            payload[key] = simulated_extras[key]

            payload["simulated_extras"].append(
                key
            )

    payload["_meta"]["simulated_extras"] = list(
        payload["simulated_extras"]
    )

    return payload
