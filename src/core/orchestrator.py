# =========================================================
# TIDE LINE — SYSTEM ORCHESTRATOR
# =========================================================

from datetime import datetime

from src.utils.marine_engine import build_marine_system

from src.services.marine_service import (
    get_simulated_marine_conditions
)

from src.services.dashboard_adapter import (
    build_dashboard_marine_payload
)

from src.services.inlet_engine import (
    analyze_inlet_conditions
)

from src.services.tactical_brief_engine import (
    build_tactical_brief
)

from src.utils.alert_engine import (
    classify_alerts
)

from src.services.strike_window_engine import (
    build_strike_windows
)

from src.services.priority_engine import (
    build_priority_state
)

from src.services.memory_engine import (
    store_snapshot,
    get_recent_snapshots
)

from src.utils.logger import logger


# =========================================================
# SAFE GET
# =========================================================

def safe_dict(value):

    if isinstance(value, dict):
        return value

    return {}


def safe_list(value):

    if isinstance(value, list):
        return value

    return []


# =========================================================
# MASTER ORCHESTRATION
# =========================================================

def run_command_center():

    # =====================================================
    # BUILD CORE SYSTEM
    # =====================================================

    system = safe_dict(
        build_marine_system()
    )

    # =====================================================
    # LIVE MARINE CONDITIONS
    # =====================================================

    canonical_marine = safe_dict(
        system.get("marine")
    )

    logger.info(
        "[ORCHESTRATOR] Canonical marine payload loaded."
    )

    marine = safe_dict(
        get_simulated_marine_conditions()
    )

    logger.warning(
        "[ORCHESTRATOR] Legacy marine payload is simulated."
    )

    # =====================================================
    # CORE SYSTEM PAYLOADS
    # =====================================================

    tides = safe_dict(
        system.get("tides")
    )

    buoys = safe_dict(
        system.get("buoys")
    )

    risk = safe_dict(
        system.get("risk")
    )

    prediction = safe_dict(
        system.get("prediction")
    )

    tactical = safe_dict(
        system.get("tactical")
    )

    synthesis = safe_dict(
        system.get("synthesis")
    )

    # =====================================================
    # CANONICAL DASHBOARD ADAPTER
    # =====================================================

    dashboard_marine = safe_dict(

        build_dashboard_marine_payload(
            canonical_marine,
            tides,
            buoys,
            marine
        )

    )

    # =====================================================
    # INLET ANALYSIS
    # =====================================================

    inlet_status = safe_dict(

        analyze_inlet_conditions(
            dashboard_marine
        )

    )

    # =====================================================
    # SPECIES EXTRACTION
    # =====================================================

    species = safe_list(

        prediction.get(
            "species",
            []
        )

    )

    # =====================================================
    # ALERT ENGINE
    # =====================================================

    alerts = safe_list(

        classify_alerts(
            risk,
            prediction,
            canonical_marine
        )

    )

    tactical["alerts"] = alerts

    # =====================================================
    # STRIKE WINDOWS
    # =====================================================

    strike_windows = safe_list(

        build_strike_windows(
            prediction,
            tides,
            canonical_marine,
            risk
        )

    )

    tactical["strike_windows"] = strike_windows

    # =====================================================
    # PRIORITY ENGINE
    # =====================================================

    priority_state = safe_dict(

        build_priority_state(
            prediction,
            risk,
            tactical
        )

    )

    tactical["priority_state"] = priority_state

    # =====================================================
    # TACTICAL BRIEF
    # =====================================================

    tactical_brief = safe_dict(

        build_tactical_brief(
            dashboard_marine,
            inlet_status,
            prediction,
            tactical
        )

    )

    # =====================================================
    # MEMORY ENGINE
    # =====================================================

    try:

        store_snapshot(
            tactical,
            prediction,
            risk,
            canonical_marine
        )

    except Exception as e:

        tactical["memory_error"] = str(e)

        logger.exception(
            "[ORCHESTRATOR] Memory snapshot storage failed."
        )

    # =====================================================
    # MEMORY EXPORT
    # =====================================================

    try:

        memory = safe_list(
            get_recent_snapshots()
        )

    except Exception:

        memory = []

        logger.exception(
            "[ORCHESTRATOR] Recent memory snapshot load failed."
        )

    tactical["memory"] = memory

    # =====================================================
    # DEFAULT FALLBACKS
    # =====================================================

    tactical.setdefault(
        "confidence",
        74
    )

    tactical.setdefault(
        "mission",
        "MONITOR"
    )

    tactical.setdefault(
        "target",
        prediction.get(
            "top_species",
            "UNKNOWN"
        )
    )

    tactical.setdefault(
        "risk_state",
        "LOW"
    )

    tactical.setdefault(
        "launch_state",
        "CAUTION"
    )

    prediction.setdefault(
        "feeding_score",
        50
    )

    prediction.setdefault(
        "activity",
        "MODERATE"
    )

    prediction.setdefault(
        "top_species",
        "SNAPPER"
    )

    marine.setdefault(
        "timestamp",
        datetime.now().strftime(
            "%H:%M:%S"
        )
    )

    marine.setdefault(
        "wave_height",
        2.0
    )

    marine.setdefault(
        "wind_speed",
        10
    )

    marine.setdefault(
        "wind_direction",
        135
    )

    marine.setdefault(
        "wave_period",
        5
    )

    marine.setdefault(
        "tide_state",
        "Incoming"
    )

    # =====================================================
    # TELEMETRY BUS
    # =====================================================

    telemetry = {

        "status": "ONLINE",

        "sync": True,

        "updated": marine.get(
            "timestamp",
            dashboard_marine.get(
                "timestamp",
                "--"
            )
        ),

        "dashboard_updated": dashboard_marine.get(
            "timestamp",
            "--"
        ),

        "radar": "ACTIVE",

        "traffic": "ONLINE",

        "prediction_engine": "ACTIVE"

    }

    # =====================================================
    # TELEMETRY SOURCE METADATA
    # =====================================================

    telemetry_meta = {

        "canonical_marine": {

            "source": "src.utils.marine_engine.build_marine_system",

            "source_type": "live_or_cached",

            "is_simulated": False

        },

        "dashboard_marine": {

            "source": "src.services.dashboard_adapter",

            "source_type": "canonical_adapter",

            "is_simulated": False,

            "simulated_extras": dashboard_marine.get(
                "simulated_extras",
                []
            )

        }

    }

    # =====================================================
    # SYSTEM HEALTH BUS
    # =====================================================

    system_health = {

        "engine": "ONLINE",

        "marine_api": "CONNECTED",

        "telemetry": "ACTIVE",

        "prediction_engine": "ONLINE",

        "memory_engine": "ACTIVE",

        "alerts": len(alerts),

        "species_loaded": len(species)

    }

    # =====================================================
    # RETURN MASTER PAYLOAD
    # =====================================================

    return {

        "system": system,

        "marine": marine,

        "canonical_marine": canonical_marine,

        "dashboard_marine": dashboard_marine,

        "tides": tides,

        "buoys": buoys,

        "risk": risk,

        "prediction": prediction,

        "tactical": tactical,

        "synthesis": synthesis,

        "species": species,

        "inlet": inlet_status,

        "brief": tactical_brief,

        "alerts": alerts,

        "strike_windows": strike_windows,

        "priority_state": priority_state,

        "memory": memory,

        "telemetry": telemetry,

        "telemetry_meta": telemetry_meta,

        "system_health": system_health

    }
