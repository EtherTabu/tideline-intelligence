import requests

from datetime import datetime, timedelta


# =========================================================
# NOAA STATION
# =========================================================

STATION_ID = "8722670"


# =========================================================
# DETERMINE TIDE DIRECTION
# =========================================================

def determine_tide_direction(

    current_height,
    next_height

):

    if next_height > current_height:

        return "INCOMING"

    elif next_height < current_height:

        return "OUTGOING"

    return "SLACK"


# =========================================================
# DETERMINE TIDE VELOCITY
# =========================================================

def determine_tide_velocity(change):

    change = abs(change)

    if change < 0.15:

        return "WEAK"

    elif change < 0.45:

        return "MODERATE"

    return "STRONG"


# =========================================================
# IDENTIFY SLACK WINDOWS
# =========================================================

def identify_slack_windows(tides):

    slack_windows = []

    for tide in tides:

        if tide["velocity"] == "WEAK":

            slack_windows.append({

                "time": tide["time"],

                "direction": tide["direction"]

            })

    return slack_windows


# =========================================================
# IDENTIFY STRONG OUTGOING WINDOWS
# =========================================================

def identify_outgoing_windows(tides):

    outgoing = []

    for tide in tides:

        if (

            tide["direction"] == "OUTGOING"

            and tide["velocity"] == "STRONG"

        ):

            outgoing.append({

                "time": tide["time"],

                "height": tide["height"]

            })

    return outgoing


# =========================================================
# IDENTIFY STRONG INCOMING WINDOWS
# =========================================================

def identify_incoming_windows(tides):

    incoming = []

    for tide in tides:

        if (

            tide["direction"] == "INCOMING"

            and tide["velocity"] == "STRONG"

        ):

            incoming.append({

                "time": tide["time"],

                "height": tide["height"]

            })

    return incoming


# =========================================================
# MAIN NOAA TIDE FETCH
# =========================================================

def get_tides():

    today = datetime.utcnow().strftime("%Y%m%d")

    tomorrow = (

        datetime.utcnow() + timedelta(days=2)

    ).strftime("%Y%m%d")

    url = (

        "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?"

        f"begin_date={today}"

        f"&end_date={tomorrow}"

        f"&station={STATION_ID}"

        "&product=predictions"

        "&datum=MLLW"

        "&interval=h"

        "&units=english"

        "&time_zone=lst_ldt"

        "&format=json"

    )

    try:

        response = requests.get(

            url,

            timeout=10

        )

        if response.status_code != 200:

            raise Exception(

                f"NOAA API failed: {response.status_code}"

            )

        data = response.json()

        predictions = data.get(

            "predictions",

            []

        )

        tides = []

        if not predictions:

            return {

                "tides": [],

                "current": {},

                "max_tide": 0,

                "min_tide": 0,

                "tidal_range": 0,

                "slack_windows": [],

                "incoming_windows": [],

                "outgoing_windows": []

            }

        # =================================================
        # BUILD TIDE SERIES
        # =================================================

        for i in range(len(predictions) - 1):

            current = predictions[i]

            nxt = predictions[i + 1]

            current_height = float(current["v"])

            next_height = float(nxt["v"])

            direction = determine_tide_direction(

                current_height,
                next_height

            )

            velocity = determine_tide_velocity(

                next_height - current_height

            )

            tides.append({

                "time": current["t"],

                "height": current_height,

                "direction": direction,

                "velocity": velocity

            })

        # =================================================
        # CURRENT TIDE
        # =================================================

        current_tide = tides[0]

        # =================================================
        # METRICS
        # =================================================

        heights = [

            t["height"]

            for t in tides

        ]

        max_tide = round(

            max(heights),

            2

        )

        min_tide = round(

            min(heights),

            2

        )

        tidal_range = round(

            max_tide - min_tide,

            2

        )

        # =================================================
        # TEMPORAL WINDOWS
        # =================================================

        slack_windows = identify_slack_windows(
            tides
        )

        outgoing_windows = identify_outgoing_windows(
            tides
        )

        incoming_windows = identify_incoming_windows(
            tides
        )

        # =================================================
        # RETURN SYNTHESIS OBJECT
        # =================================================

        return {

            "tides": tides,

            "current": current_tide,

            "max_tide": max_tide,

            "min_tide": min_tide,

            "tidal_range": tidal_range,

            "slack_windows": slack_windows,

            "incoming_windows": incoming_windows,

            "outgoing_windows": outgoing_windows

        }

    except Exception as e:

        print(f"NOAA Tide Fetch Error: {e}")

        return {

            "tides": [],

            "current": {},

            "max_tide": 0,

            "min_tide": 0,

            "tidal_range": 0,

            "slack_windows": [],

            "incoming_windows": [],

            "outgoing_windows": []

        }
