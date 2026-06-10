# =========================================================
# TIDE LINE — SPECIES MATRIX ENGINE
# =========================================================

from src.config.species_profiles import (
    SPECIES_PROFILES
)


def score_species_profile(

    profile,
    marine

):

    score = 50

    water_temp = marine.get(
        "water_temp",
        75
    )

    tide_state = marine.get(
        "tide_state",
        ""
    )

    moon_phase = marine.get(
        "moon_phase",
        ""
    )

    temp_min = profile[
        "preferred_temp"
    ][0]

    temp_max = profile[
        "preferred_temp"
    ][1]

    if temp_min <= water_temp <= temp_max:

        score += 20

    if tide_state in profile[
        "preferred_tide"
    ]:

        score += 15

    if moon_phase in profile[
        "preferred_moon"
    ]:

        score += 15

    return min(
        score,
        100
    )


def build_species_matrix(

    marine

):

    matrix = []

    for name, profile in SPECIES_PROFILES.items():

        score = score_species_profile(

            profile,
            marine

        )

        matrix.append({

            "species": name,

            "group": profile[
                "group"
            ],

            "score": score

        })

    matrix.sort(

        key=lambda x: x["score"],
        reverse=True

    )

    return matrix