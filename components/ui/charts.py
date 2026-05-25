import streamlit as st
import plotly.graph_objects as go


# =========================================================
# TIDE CHART ENGINE
# =========================================================

def show_tides_chart(tides_data):

    st.markdown("## Strategic Deployment Map")

    if not tides_data:

        st.error("Tide intelligence unavailable.")
        return

    tides = tides_data.get("tides", [])

    if not tides:

        st.error("No tide series available.")
        return

    # =====================================================
    # EXTRACT DATA
    # =====================================================

    times = [
        t["time"] for t in tides
    ]

    heights = [
        t["height"] for t in tides
    ]

    # =====================================================
    # BUILD CHART
    # =====================================================

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=times,

            y=heights,

            fill="tozeroy",

            mode="lines",

            name="Tide",

            line=dict(
                width=2
            )

        )

    )

    # =====================================================
    # LAYOUT
    # =====================================================

    fig.update_layout(

        height=260,

        margin=dict(
            l=10,
            r=10,
            t=30,
            b=20
        ),

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        xaxis=dict(
            showgrid=False
        ),

        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(255,255,255,0.08)"
        ),

        font=dict(
            color="white"
        )

    )

    # =====================================================
    # RENDER
    # =====================================================

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # =====================================================
    # METRICS
    # =====================================================

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Max Tide",
            f"{tides_data.get('max_tide', 0)} ft"
        )

    with c2:

        st.metric(
            "Min Tide",
            f"{tides_data.get('min_tide', 0)} ft"
        )

    with c3:

        st.metric(
            "Tidal Range",
            f"{tides_data.get('tidal_range', 0)} ft"
        )

    # =====================================================
    # CURRENT TIDE STATE
    # =====================================================

    current = tides_data.get(
        "current",
        {}
    )

    direction = current.get(
        "direction",
        "UNKNOWN"
    )

    velocity = current.get(
        "velocity",
        "UNKNOWN"
    )

    st.caption(

        f"Tide Flow: {direction} | "
        f"Velocity: {velocity}"

    )
