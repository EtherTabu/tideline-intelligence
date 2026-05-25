# =========================================================
# TIDE LINE — TACTICAL MEMORY PANEL
# =========================================================

import streamlit as st


# =========================================================
# PANEL
# =========================================================

def show_tactical_memory_panel(memory):

    if not memory:
        return

    st.subheader("🧠 Tactical Memory")

    st.caption(
        "Recent operational snapshots and evolving conditions"
    )

    for snapshot in reversed(memory[-8:]):

        timestamp = snapshot.get(
            "timestamp",
            "--:--"
        )

        mission = snapshot.get(
            "mission_status",
            "UNKNOWN"
        )

        confidence = snapshot.get(
            "confidence",
            0
        )

        target = snapshot.get(
            "target",
            "UNKNOWN"
        )

        with st.container(border=True):

            col1, col2 = st.columns([4, 1])

            with col1:

                st.markdown(
                    f"### {mission}"
                )

                st.caption(
                    f"TARGET: {target}"
                )

            with col2:

                st.metric(
                    "CONF",
                    f"{confidence}%"
                )

                st.caption(timestamp)