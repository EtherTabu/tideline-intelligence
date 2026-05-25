# =========================================================
# TIDE LINE — MEMORY PANEL
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px


# =========================================================
# MEMORY PANEL
# =========================================================

def show_memory_panel(tactical_data):

    memory = tactical_data.get(
        "memory",
        []
    )

    st.markdown(
        "## 🧠 Tactical Memory"
    )

    # =====================================================
    # NO MEMORY
    # =====================================================

    if not memory:

        st.warning(
            "No tactical memory available."
        )

        return

    # =====================================================
    # DATAFRAME
    # =====================================================

    df = pd.DataFrame(memory)

    # =====================================================
    # TIMESTAMP
    # =====================================================

    if "timestamp" in df.columns:

        df["timestamp"] = pd.to_datetime(
            df["timestamp"],
            errors="coerce"
        )

    # =====================================================
    # FEEDING TREND
    # =====================================================

    if "feeding_score" in df.columns:

        st.markdown(
            "### Feeding Trend"
        )

        fig = px.line(
            df,
            x="timestamp",
            y="feeding_score",
            markers=True
        )

        fig.update_layout(
            template="plotly_dark",
            height=260,
            margin=dict(
                l=10,
                r=10,
                t=10,
                b=10
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # =====================================================
    # RISK TREND
    # =====================================================

    if "danger_score" in df.columns:

        st.markdown(
            "### Risk Trend"
        )

        fig2 = px.area(
            df,
            x="timestamp",
            y="danger_score"
        )

        fig2.update_layout(
            template="plotly_dark",
            height=240,
            margin=dict(
                l=10,
                r=10,
                t=10,
                b=10
            )
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # =====================================================
    # RAW SNAPSHOTS
    # =====================================================

    with st.expander(
        "Memory Snapshots"
    ):

        st.dataframe(
            df,
            use_container_width=True
        )