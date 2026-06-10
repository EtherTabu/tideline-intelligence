# =========================================================
# TIDE LINE | MASTER SPECIES ENGINE
# =========================================================

from src.species_engines.snapper_engine import (
    calculate_snapper_score
)

from src.species_engines.mahi_engine import (
    calculate_mahi_score
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

    results = []

    # =====================================================
    # SNAPPER
    # =====================================================

    try:

        snapper = calculate_snapper_score(

            marine,
            tides,
            buoys,
            risk

        )

        results.append(
            snapper
        )

    except Exception as e:

        print(
            f"[SPECIES ENGINE] SNAPPER FAILED: {e}"
        )

    # =====================================================
    # MAHI
    # =====================================================

    try:

        mahi = calculate_mahi_score(

            marine,
            tides,
            buoys,
            risk

        )

        results.append(
            mahi
        )

    except Exception as e:

        print(
            f"[SPECIES ENGINE] MAHI FAILED: {e}"
        )

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