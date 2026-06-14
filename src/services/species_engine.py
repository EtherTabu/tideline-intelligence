# =========================================================
# TIDE LINE | MASTER SPECIES ENGINE
# =========================================================

from src.config.species_registry import (
    run_species_engines
)


# =========================================================
# MASTER ENGINE
# =========================================================

def calculate_species_scores(

    marine,
    tides,
    buoys,
    risk

):

    registry_results = run_species_engines(

        marine,
        tides,
        buoys,
        risk

    )

    if not isinstance(
        registry_results,
        dict
    ):

        return []

    results = [

        value

        for value in registry_results.values()

        if isinstance(
            value,
            dict
        )

    ]

    # =====================================================
    # SORT
    # =====================================================

    results = sorted(

        results,

        key=lambda x: x.get(
            "score",
            0
        ),

        reverse=True

    )

    return results
