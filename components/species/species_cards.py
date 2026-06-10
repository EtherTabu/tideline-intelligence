import streamlit as st

from components.species.species_heat_meter import (
    render_heat_meter
)

from components.tactical.tactical_chips import (
    render_tactical_chips
)


# =========================================================
# SPECIES CARDS
# =========================================================

def render_species_cards(species_data):

    if not species_data:
        return

    for species in species_data:

        species_name = species.get(
            "species",
            "UNKNOWN"
        )

        score = int(
            species.get(
                "score",
                0
            )
        )

        activity = species.get(
            "activity",
            "LOW"
        )

        recommendation = species.get(
            "recommendation",
            "No tactical recommendation available."
        )

        best_window = species.get(
            "best_window",
            "UNKNOWN"
        )

        depth_zone = species.get(
            "depth_zone",
            "UNKNOWN"
        )

        structures = species.get(
            "known_structure",
            species.get(
                "known_targets",
                species.get(
                    "structures",
                    []
                )
            )
        )

        techniques = species.get(
            "techniques",
            []
        )

        status = species.get(
            "status",
            "ACTIVE"
        )

        primary_target = species.get(
            "primary_target",
            False
        )

        # =================================================
        # COLOR LOGIC
        # =================================================

        if score >= 85:

            color = "#00FF99"

        elif score >= 70:

            color = "#7CFFB2"

        elif score >= 50:

            color = "#FFD24A"

        else:

            color = "#FF5C5C"

        glow = ""

        primary_tag = ""

        if primary_target:

            primary_tag = """
            <div style="
                background:rgba(0,255,136,0.12);
                color:#00FF99;
                border:1px solid rgba(0,255,136,0.22);
                padding:6px 10px;
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

        # =================================================
        # CARD HTML
        # =================================================

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

        # =================================================
        # HEAT METER
        # =================================================

        render_heat_meter(
            f"{activity} ACTIVITY",
            score
        )

        # =================================================
        # TACTICAL CHIPS
        # =================================================

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