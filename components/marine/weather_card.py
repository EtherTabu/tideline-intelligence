import streamlit as st


def show_weather(data):

    if not data:
        st.warning("Weather Sync Offline")
        return

    degree = data.get("wind_dir", 180)
    wind_speed = data.get("wind_speed", 0)

    # ==========================================
    # WIND DIRECTION CONVERSION
    # ==========================================

    directions = [
        "N", "NE", "E", "SE",
        "S", "SW", "W", "NW"
    ]

    direction_index = round(degree / 45) % 8
    cardinal = directions[direction_index]

    # ==========================================
    # MAIN WEATHER CARD
    # ==========================================

    st.markdown(
        """
        <style>
        .weather-card {
            background: #1a1c24;
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 12px;
            padding: 20px;
        }

        .weather-title {
            color: #00d4ff;
            font-size: 26px;
            font-weight: 700;
            margin-bottom: 18px;
        }

        .metric-label {
            color: #808495;
            font-size: 12px;
            margin-bottom: 4px;
        }

        .metric-value {
            color: white;
            font-size: 30px;
            font-weight: 700;
        }

        .weather-footer {
            margin-top: 18px;
            color: #808495;
            font-size: 13px;
        }

        .compass {
            font-size: 54px;
            text-align: center;
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.container():

        st.markdown(
            '<div class="weather-card">',
            unsafe_allow_html=True
        )

        cols = st.columns([1, 2, 2])

        # ======================================
        # COMPASS
        # ======================================

        with cols[0]:

            compass_map = {
                "N": "↑",
                "NE": "↗",
                "E": "→",
                "SE": "↘",
                "S": "↓",
                "SW": "↙",
                "W": "←",
                "NW": "↖"
            }

            arrow = compass_map.get(cardinal, "↑")

            st.markdown(
                f"""
                <div class="compass">
                    {arrow}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption(f"{cardinal} Wind Flow")

        # ======================================
        # WIND DIRECTION
        # ======================================

        with cols[1]:

            st.markdown(
                '<div class="weather-title">Wind Intelligence</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="metric-label">DIRECTION</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="metric-value">{degree}°</div>',
                unsafe_allow_html=True
            )

        # ======================================
        # WIND SPEED
        # ======================================

        with cols[2]:

            st.markdown(
                '<div class="metric-label">WIND SPEED</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="metric-value">{wind_speed} kts</div>',
                unsafe_allow_html=True
            )

        st.markdown(
            """
            <div class="weather-footer">
                Real-time NOAA/Open-Meteo directional analysis
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)
