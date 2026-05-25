# =====================================================
# TIDE LINE — MASTER MARINE ENGINE
# =====================================================

from src.marine_forecast import (
    get_marine_forecast
)

from src.tides import (
    get_tides
)

from src.scoring import (
    calculate_marine_risk
)

from src.services.fish_prediction import (
    generate_fish_prediction
)

from src.telemetry_engine import (
    build_telemetry
)

from src.tactical_intelligence import (
    build_tactical_intelligence
)

from src.system_validator import (
    validate_contract
)

# =====================================================
# CANONICAL CONTRACT IMPORTS
# =====================================================

from src.contracts import (

    MARINE_CONTRACT,
    TIDE_CONTRACT,
    BUOY_CONTRACT,
    RISK_CONTRACT,
    PREDICTION_CONTRACT,
    TACTICAL_CONTRACT,
    SYNTHESIS_CONTRACT

)

# =====================================================
# MASTER MARINE INTELLIGENCE ENGINE
# =====================================================

def build_marine_system():

    # =================================================
    # CORE FORECAST INGESTION
    # =================================================

    marine = get_marine_forecast()

    marine = validate_contract(
        marine,
        MARINE_CONTRACT
    )

    # =================================================
    # TIDE ENGINE
    # =================================================

    tides = get_tides()

    tides = validate_contract(
        tides,
        TIDE_CONTRACT
    )

    # =================================================
    # TELEMETRY ENGINE
    # =================================================

    telemetry = build_telemetry()

    telemetry = validate_contract(
        telemetry,
        BUOY_CONTRACT
    )

    # =================================================
    # CANONICAL RISK ENGINE
    # =================================================

    risk = calculate_marine_risk(
        marine,
        tides
    )

    risk = validate_contract(
        risk,
        RISK_CONTRACT
    )

    # =================================================
    # SPECIES / PREDICTION ENGINE
    # =================================================

    prediction = generate_fish_prediction(
        marine,
        tides,
        telemetry,
        risk
    )

    prediction = validate_contract(
        prediction,
        PREDICTION_CONTRACT
    )

    # =================================================
    # TACTICAL INTELLIGENCE ENGINE
    # =================================================

    tactical = build_tactical_intelligence(
        marine,
        tides,
        telemetry,
        risk,
        prediction
    )

    tactical = validate_contract(
        tactical,
        TACTICAL_CONTRACT
    )

    # =================================================
    # SYNTHESIS ENGINE
    # =================================================

    synthesis = {

        "mission_status": tactical.get(
            "mission_status",
            "MONITOR"
        ),

        "primary_target": tactical.get(
            "primary_target",
            "UNKNOWN"
        ),

        "confidence": tactical.get(
            "confidence",
            0
        ),

        "summary": tactical.get(
            "summary",
            "No synthesis available."
        )

    }

    synthesis = validate_contract(
        synthesis,
        SYNTHESIS_CONTRACT
    )

    # =================================================
    # MASTER SYSTEM OBJECT
    # =================================================

    system = {

        "marine": marine,

        "tides": tides,

        "buoys": telemetry,

        "risk": risk,

        "prediction": prediction,

        "tactical": tactical,

        "synthesis": synthesis

    }

    return system


# =====================================================
# LOCAL TEST
# =====================================================

if __name__ == "__main__":

    system = build_marine_system()

    print("\n========== MARINE SYSTEM ==========\n")

    for key, value in system.items():

        print(f"{key.upper()}:\n")

        print(value)

        print("\n")
