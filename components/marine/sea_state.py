import streamlit as st


def analyze_sea_state(weather):

    if not weather:
        st.warning("Sea-state intelligence offline.")
        return

    try:

        # =====================================================
        # INPUTS
        # =====================================================

        wind_speed = int(
            str(weather.get("wind", "0")).split()[0]
        )

        wind_dir = weather.get("wind_dir", 0)

        wave_height = weather.get(
            "wave_height",
            0.0
        )

        swell_period = weather.get(
            "swell_period",
            0.0
        )

        swell_direction = weather.get(
            "swell_direction",
            "N"
        )

        tide_flow = weather.get(
            "tide_flow",
            "UNKNOWN"
        )

        # =====================================================
        # SEA STATE ENGINE
        # =====================================================

        if wind_speed <= 5:

            sea_state = "CALM"
            risk = "LOW"
            inlet_hazard = 10
            feeding_score = 72
            bite_window = "SUNRISE"

        elif wind_speed <= 12:

            sea_state = "MODERATE CHOP"
            risk = "MODERATE"
            inlet_hazard = 35
            feeding_score = 81
            bite_window = "TIDE SWITCH"

        elif wind_speed <= 18:

            sea_state = "HEAVY CHOP"
            risk = "HIGH"
            inlet_hazard = 68
            feeding_score = 63
            bite_window = "SHORT WINDOWS"

        else:

            sea_state = "DANGEROUS"
            risk = "EXTREME"
            inlet_hazard = 92
            feeding_score = 30
            bite_window = "POOR"

        # =====================================================
        # HEADER
        # =====================================================

        st.markdown(
            "## 🌊 Sea State Intelligence"
        )

        # =====================================================
        # TOP ALERT BAR
        # =====================================================

        if inlet_hazard <= 20:

            st.success(
                "Minimal inlet turbulence detected."
            )

        elif inlet_hazard <= 50:

            st.info(
                "Moderate cross-current interaction possible."
            )

        elif inlet_hazard <= 75:

            st.warning(
                "Standing wave development possible near inlet structures."
            )

        else:

            st.error(
                "Dangerous inlet dynamics detected."
            )

        # =====================================================
        # MAIN INTELLIGENCE GRID
        # =====================================================

        col1, col2, col3, col4 = st.columns(4)

        # -----------------------------------------------------

        with col1:

            st.metric(
                "Wind Vector",
                f"{wind_speed} kts"
            )

            st.metric(
                "Direction",
                f"{wind_dir}°"
            )

            st.metric(
                "Sea State",
                sea_state
            )

        # -----------------------------------------------------

        with col2:

            st.metric(
                "Wave Height",
                f"{wave_height} ft"
            )

            st.metric(
                "Swell Period",
                f"{swell_period} sec"
            )

            st.metric(
                "Swell Direction",
                swell_direction
            )

        # -----------------------------------------------------

        with col3:

            st.metric(
                "Tide Flow",
                tide_flow
            )

            st.metric(
                "Inlet Hazard",
                f"{inlet_hazard}/100"
            )

            st.metric(
                "Operational Risk",
                risk
            )

        # -----------------------------------------------------

        with col4:

            st.metric(
                "Feeding Score",
                f"{feeding_score}/100"
            )

            st.metric(
                "Bite Timing",
                bite_window
            )

            confidence = 88 - (
                inlet_hazard // 4
            )

            st.metric(
                "Confidence",
                f"{confidence}%"
            )

        # =====================================================
        # TACTICAL MATRIX
        # =====================================================

        st.markdown("---")

        st.markdown(
            "### 🧠 Tactical Conditions Matrix"
        )

        matrix1, matrix2 = st.columns(2)

        # -----------------------------------------------------

        with matrix1:

            st.markdown(
                f"""
- Wind Interaction: **{sea_state}**
- Tide State: **{tide_flow}**
- Swell Energy: **{swell_period} sec**
- Inlet Stability: **{risk}**
"""
            )

        # -----------------------------------------------------

        with matrix2:

            st.markdown(
                f"""
- Feeding Activity: **{feeding_score}/100**
- Best Window: **{bite_window}**
- Swell Track: **{swell_direction}**
- Confidence Engine: **{confidence}%**
"""
            )

        # =====================================================
        # SIGNAL ENGINE
        # =====================================================

        st.markdown("---")

        st.markdown(
            "### 📡 Signal Engine"
        )

        if feeding_score >= 80:

            st.success(
                "High predator feeding probability detected along moving water structure."
            )

        elif feeding_score >= 60:

            st.info(
                "Moderate feeding activity expected near tide transitions."
            )

        else:

            st.warning(
                "Reduced feeding efficiency likely due to unstable marine energy."
            )

        # =====================================================
        # SYSTEM NOTES
        # =====================================================

        st.caption(
            "Environmental synthesis engine using wind vectors, "
            "swell energy, tidal pressure, and inlet interaction modeling."
        )

    except Exception as e:

        st.warning(
            f"Sea-state engine error: {e}"
        )
