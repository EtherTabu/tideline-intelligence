# =========================================================
# TIDE LINE — SPECIES INTELLIGENCE
# =========================================================

import streamlit as st

from components.species.species_heat_meter import (
    render_heat_meter
)

from components.tactical.tactical_chips import (
    render_tactical_chips
)


# =========================================================
# SPECIES INTEL GRID
# =========================================================

def show_species_cards(species_list):

    if not species_list:

        st.warning(
            "No species intelligence available."
        )

        return

    # =====================================================
    # PRIMARY TARGET
    # =====================================================

    primary_target = "SNAPPER"

    # =====================================================
    # SORT PRIMARY FIRST
    # =====================================================

    sorted_species = sorted(

        species_list,

        key=lambda item:

        item.get(
            "species",
            ""
        ) != primary_target

    )

    # =====================================================
    # SECTION HEADER
    # =====================================================

    st.markdown(

        """
<div style="
margin-top:1.4rem;
margin-bottom:1rem;
">

<div style="
color:#3BD6FF;
font-size:1rem;
font-weight:800;
letter-spacing:0.08em;
margin-bottom:0.25rem;
">

🎯 SPECIES INTELLIGENCE

</div>

<div style="
color:#8FA3B8;
font-size:0.78rem;
letter-spacing:0.04em;
">

TACTICAL FEEDING PROBABILITY • STRIKE WINDOWS • OFFSHORE TARGET ANALYSIS

</div>

</div>
        """,

        unsafe_allow_html=True

    )

    # =====================================================
    # GRID
    # =====================================================

    cols_per_row = 2

    for row_start in range(

        0,
        len(sorted_species),
        cols_per_row

    ):

        row_species = sorted_species[
            row_start:row_start + cols_per_row
        ]

        cols = st.columns(
            len(row_species)
        )

        # =================================================
        # CARD LOOP
        # =================================================

        for idx, data in enumerate(row_species):

            with cols[idx]:

                species_name = data.get(
                    "species",
                    "UNKNOWN"
                )

                score = int(
                    data.get(
                        "score",
                        0
                    )
                )

                activity = data.get(
                    "activity",
                    "UNKNOWN"
                )

                recommendation = data.get(
                    "recommendation",
                    "No recommendation available."
                )

                best_window = data.get(
                    "best_window",
                    "ACTIVE"
                )

                depth_zone = data.get(
                    "depth_zone",
                    "GENERAL"
                )

                techniques = data.get(
                    "techniques",
                    []
                )

                structures = data.get(
                    "known_targets",
                    []
                )

                tactical_notes = data.get(
                    "tactical_notes",
                    []
                )

                # =============================================
                # PRIMARY TARGET
                # =============================================

                is_primary = (

                    species_name.upper() == primary_target

                )

                # =============================================
                # SCORE ENGINE
                # =============================================

                if score >= 90:

                    color = "#00ff88"
                    status = "ELITE"

                elif score >= 75:

                    color = "#00d4ff"
                    status = "HIGH"

                elif score >= 55:

                    color = "#ffd166"
                    status = "MODERATE"

                else:

                    color = "#ff5c5c"
                    status = "LOW"

                # =============================================
                # PRIMARY TARGET TAG
                # =============================================

                primary_tag = ""

                glow = ""

                if is_primary:

                    primary_tag = """
<div style="
background:#00ff88;
color:black;
padding:4px 10px;
border-radius:999px;
font-size:10px;
font-weight:800;
display:inline-block;
margin-bottom:0.55rem;
">

🎯 PRIMARY TARGET

</div>
"""

                    glow = (
                        "box-shadow:0 0 18px "
                        "rgba(0,255,136,0.14);"
                    )

                # =============================================
                # CARD
                # =============================================

                card_html = f"""

<div style="
background:#07111F;
border:1px solid #13304A;
border-left:4px solid {color};
border-radius:16px;
padding:1rem;
margin-bottom:0.8rem;
{glow}
">

{primary_tag}

<div style="
display:flex;
justify-content:space-between;
align-items:flex-start;
gap:0.5rem;
margin-bottom:0.6rem;
">

<div>

<div style="
color:white;
font-size:1.7rem;
font-weight:900;
line-height:1;
margin-bottom:0.35rem;
">

{species_name}

</div>

<div style="
color:#8FA3B8;
font-size:0.82rem;
font-weight:700;
letter-spacing:0.04em;
">

{activity}

</div>

</div>

<div style="
background:{color};
color:black;
padding:6px 12px;
border-radius:999px;
font-size:0.7rem;
font-weight:900;
letter-spacing:0.04em;
white-space:nowrap;
">

{status}

</div>

</div>

<div style="
color:{color};
font-size:3rem;
font-weight:900;
line-height:1;
margin-bottom:0.6rem;
">

{score}

</div>

<div style="
background:rgba(255,255,255,0.03);
padding:0.7rem;
border-radius:12px;
margin-bottom:0.7rem;
border:1px solid rgba(255,255,255,0.04);
">

<div style="
color:white;
font-size:0.8rem;
line-height:1.5;
">

{recommendation}

</div>

</div>

<div style="
display:flex;
gap:0.45rem;
flex-wrap:wrap;
margin-bottom:0.5rem;
">

<div style="
background:#0B1727;
border:1px solid #13304A;
padding:0.35rem 0.65rem;
border-radius:999px;
color:#7DD3FC;
font-size:0.7rem;
font-weight:700;
">

🕒 {best_window}

</div>

<div style="
background:#0B1727;
border:1px solid #13304A;
padding:0.35rem 0.65rem;
border-radius:999px;
color:#7DD3FC;
font-size:0.7rem;
font-weight:700;
">

🌊 {depth_zone}

</div>

</div>

</div>

"""

                st.markdown(

                    card_html,

                    unsafe_allow_html=True

                )

                # =============================================
                # HEAT METER
                # =============================================

                render_heat_meter(

                    f"{activity} ACTIVITY",

                    score

                )

                # =============================================
                # TACTICAL CHIPS
                # =============================================

                preview_items = []

                preview_items.extend(
                    techniques[:3]
                )

                preview_items.extend(
                    structures[:3]
                )

                render_tactical_chips(

                    preview_items[:6],

                    "TACTICAL ZONES"

                )

                # =============================================
                # SIMPLE NOTES
                # =============================================

                if tactical_notes:

                    st.info(

                        " • ".join(
                            tactical_notes[:3]
                        )

                    )