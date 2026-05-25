# =========================================================
# TIDE LINE — SPECIES REGISTRY
# =========================================================

import traceback

from src.config.debug import DEBUG_MODE

from src.utils.logger import logger

from src.species_engines.snapper_engine import (
    calculate_snapper_score
)

from src.species_engines.mahi_engine import (
    calculate_mahi_score
)

# =========================================================
# ENGINE REGISTRY
# =========================================================

SPECIES_ENGINES = [

    {
        "name": "SNAPPER",
        "engine": calculate_snapper_score
    },

    {
        "name": "MAHI",
        "engine": calculate_mahi_score
    }

]

# =========================================================
# RUN ALL SPECIES ENGINES
# =========================================================

def run_species_engines(

    marine,
    tides,
    buoys,
    risk

):

    species_results = {}

    # =====================================================
    # ENGINE LOOP
    # =====================================================

    for item in SPECIES_ENGINES:

        engine_name = item.get(
            "name",
            "UNKNOWN"
        )

        engine = item.get(
            "engine"
        )

        try:

            # =============================================
            # ENGINE SAFETY
            # =============================================

            if not callable(engine):

                if DEBUG_MODE:

                    logger.warning(
                        f"[INVALID ENGINE] {engine_name}"
                    )

                continue

            # =============================================
            # EXECUTE ENGINE
            # =============================================

            result = engine(

                marine,
                tides,
                buoys,
                risk

            )

            # =============================================
            # VALIDATE RESULT
            # =============================================

            if not isinstance(result, dict):

                if DEBUG_MODE:

                    logger.warning(

                        f"[BAD ENGINE RETURN - {engine_name}] "
                        f"Expected dict, got {type(result)}"

                    )

                continue

            # =============================================
            # VALIDATE SPECIES FIELD
            # =============================================

            species_name = result.get(
                "species"
            )

            if not species_name:

                if DEBUG_MODE:

                    logger.warning(

                        f"[BAD ENGINE DATA - {engine_name}] "
                        f"Missing species field."

                    )

                continue

            # =============================================
            # STORE RESULT
            # =============================================

            species_results[
                species_name
            ] = result

            # =============================================
            # DEBUG SUCCESS
            # =============================================

            if DEBUG_MODE:

                logger.info(

                    f"[ENGINE SUCCESS] "
                    f"{species_name} | "
                    f"Score: {result.get('score', 0)}"

                )

        except Exception as e:

            logger.exception(

                f"[SPECIES ENGINE FAILURE - {engine_name}] "
                f"{str(e)}"

            )

            if DEBUG_MODE:

                traceback.print_exc()

    return species_results


# =========================================================
# LOCAL TEST
# =========================================================

if __name__ == "__main__":

    test_marine = {

        "sea_state": {

            "wave_height_ft": 2.5,
            "swell_period_sec": 7,
            "swell_direction": "E"

        },

        "wind": {

            "speed_mph": 10

        }

    }

    test_tides = {

        "current": {

            "direction": "INCOMING",
            "velocity": "MODERATE"

        }

    }

    test_buoys = {

        "regional": {

            "rating": "GOOD",
            "wave_height_ft": 2.5,
            "wave_period_sec": 6

        }

    }

    test_risk = {

        "danger_score": 20

    }

    results = run_species_engines(

        test_marine,
        test_tides,
        test_buoys,
        test_risk

    )

    if DEBUG_MODE:

        logger.info(
            "========== SPECIES REGISTRY =========="
        )

        logger.info(results)

        logger.info(
            "======================================"
        )
