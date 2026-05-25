# =========================================================
# TIDE LINE — MEMORY ENGINE
# =========================================================

import json
import os
from datetime import datetime


# =========================================================
# MEMORY FILE
# =========================================================

MEMORY_PATH = "data/memory.json"


# =========================================================
# ENSURE STORAGE
# =========================================================

def ensure_memory_file():

    if not os.path.exists("data"):

        os.makedirs("data")

    if not os.path.exists(MEMORY_PATH):

        with open(

            MEMORY_PATH,
            "w"

        ) as f:

            json.dump([], f)


# =========================================================
# LOAD MEMORY
# =========================================================

def load_memory():

    ensure_memory_file()

    try:

        with open(

            MEMORY_PATH,
            "r"

        ) as f:

            return json.load(f)

    except Exception:

        return []


# =========================================================
# SAVE MEMORY
# =========================================================

def save_memory(memory):

    with open(

        MEMORY_PATH,
        "w"

    ) as f:

        json.dump(

            memory,
            f,
            indent=2

        )


# =========================================================
# STORE SNAPSHOT
# =========================================================

def store_snapshot(

    tactical,
    prediction,
    risk,
    marine

):

    memory = load_memory()

    snapshot = {

        "timestamp": str(
            datetime.utcnow()
        ),

        "mission_status": tactical.get(
            "mission_status"
        ),

        "primary_target": tactical.get(
            "primary_target"
        ),

        "confidence": tactical.get(
            "confidence"
        ),

        "feeding_score": prediction.get(
            "feeding_score"
        ),

        "activity": prediction.get(
            "activity"
        ),

        "risk_state": risk.get(
            "risk_state"
        ),

        "danger_score": risk.get(
            "danger_score"
        ),

        "wave_height": marine.get(
            "sea_state",
            {}
        ).get(
            "wave_height_ft"
        ),

        "wind_speed": marine.get(
            "wind",
            {}
        ).get(
            "speed_mph"
        )

    }

    memory.append(snapshot)

    # =====================================================
    # KEEP ONLY LAST 500 RECORDS
    # =====================================================

    memory = memory[-500:]

    save_memory(memory)


# =========================================================
# RECENT SNAPSHOTS
# =========================================================

def get_recent_snapshots(

    limit=25

):

    memory = load_memory()

    return memory[-limit:]
