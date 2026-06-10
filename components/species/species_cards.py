import streamlit as st

from components.species.species_heat_meter import (
    render_heat_meter
)

from components.tactical.tactical_chips import (
    render_tactical_chips
)


def resolve_species_color(score):

    if score >= 85:
        return "🟢"

    if score >= 70:
        return "🟡"

    if score >= 50:
        return "🟠"

    return "🔴"


def render_species_cards(species_data):

    if not species_data:
        return

    species_columns = st.columns(
        len(species_data)
    )

    for col, species in zip(
        species_columns,
        species_data
    ):

        with col:

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
                "UNKNOWN"
            )

            recommendation = species.get(
                "recommendation",
                "No recommendation available."
            )

            best_window = species.get(
                "best_window",
                "UNKNOWN"
            )

            depth_zone = species.get(
                "depth_zone",
                "UNKNOWN"
            )

            techniques = species.get(
                "techniques",
                []
            )

            structures = species.get(
                "known_structure",
                species.get(
                    "known_targets",
                    []
                )
            )

            tactical_drivers = species.get(
                "tactical_drivers",
                []
            )

            primary_target = species.get(
                "primary_target",
                False
            )

            icon = resolve_species_color(
                score
            )

            with st.container(border=True):

                if primary_target:

                    st.success(
                        "🎯 PRIMARY TARGET"
                    )

                st.subheader(
                    f"{icon} {species_name}"
                )

                left, right = st.columns(2)

                with left:

                    st.metric(
                        "Score",
                        score
                    )

                with right:

                    st.metric(
                        "Activity",
                        activity
                    )

                st.caption(
                    recommendation
                )

                st.markdown(
                    f"**🕒 Window:** {best_window}"
                )

                st.markdown(
                    f"**🌊 Zone:** {depth_zone}"
                )

                render_heat_meter(
                    "BITE PROBABILITY",
                    score
                )

                if tactical_drivers:

                    st.markdown(
                        "##### 🎯 WHY NOW"
                    )

                    for driver in tactical_drivers[:2]:

                        st.markdown(
                            f"• {driver}"
                        )

                preview_items = []

                preview_items.extend(
                    techniques[:3]
                )

                preview_items.extend(
                    structures[:3]
                )

                if preview_items:

                    render_tactical_chips(
                        preview_items,
                        "TACTICAL PLAYBOOK"
                    )