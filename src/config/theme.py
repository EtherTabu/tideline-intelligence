# =========================================================
# TIDE LINE — GLOBAL THEME ENGINE
# =========================================================

import streamlit as st


# =========================================================
# CORE COLORS
# =========================================================

BACKGROUND = "#050816"

CARD_BG = "#0B1220"

BORDER = "#1E293B"

TEXT = "#E2E8F0"

MUTED = "#94A3B8"

GREEN = "#00FF99"

YELLOW = "#FACC15"

RED = "#FF4D6D"

BLUE = "#38BDF8"

PURPLE = "#C084FC"


# =========================================================
# STATUS COLORS
# =========================================================

STATUS_COLORS = {

    "GOOD": GREEN,
    "MODERATE": YELLOW,
    "DANGER": RED,
    "CRITICAL": RED,
    "LOW": BLUE,
    "HIGH": GREEN,
    "EXTREME": RED,
    "ACTIVE": GREEN,
    "ONLINE": GREEN,
    "OFFLINE": RED

}


# =========================================================
# PAGE CONFIG
# =========================================================

def configure_page():

    st.set_page_config(

        page_title="TIDE LINE",
        layout="wide",
        initial_sidebar_state="collapsed"

    )


# =========================================================
# GLOBAL CSS
# =========================================================

def inject_global_css():

    st.markdown(

        f"""

        <style>

        /* =================================================
           GLOBAL
        ================================================= */

        html, body, [class*="css"] {{

            background-color: {BACKGROUND};
            color: {TEXT};

            font-family:
                Inter,
                system-ui,
                sans-serif;

        }}

        .block-container {{

            padding-top: 1rem;
            padding-bottom: 1rem;

            padding-left: 1.25rem;
            padding-right: 1.25rem;

            max-width: 100%;

        }}

        /* =================================================
           REMOVE STREAMLIT CLUTTER
        ================================================= */

        #MainMenu {{
            visibility: hidden;
        }}

        footer {{
            visibility: hidden;
        }}

        header {{
            visibility: hidden;
        }}

        /* =================================================
           METRICS
        ================================================= */

        div[data-testid="metric-container"] {{

            background-color: {CARD_BG};

            border:
                1px solid {BORDER};

            border-radius: 12px;

            padding: 0.65rem;

            min-height: 72px;

        }}

        /* =================================================
           ALERTS
        ================================================= */

        div.stAlert {{

            border-radius: 10px;

            border:
                1px solid {BORDER};

        }}

        /* =================================================
           EXPANDERS
        ================================================= */

        .streamlit-expanderHeader {{

            background-color: {CARD_BG};

            border-radius: 8px;

            border:
                1px solid {BORDER};

        }}

        /* =================================================
           CHART CONTAINERS
        ================================================= */

        iframe {{

            border-radius: 12px;

            border:
                1px solid {BORDER};

        }}

        /* =================================================
           TIGHTER SPACING
        ================================================= */

        section.main > div {{

            padding-top: 0rem;

        }}

        hr {{

            margin-top: 0.5rem;
            margin-bottom: 0.5rem;

            border-color: {BORDER};

        }}

        /* =================================================
           HEADERS
        ================================================= */

        h1, h2, h3, h4 {{

            color: {TEXT};

            letter-spacing: -0.02em;

        }}

        h1 {{
            font-size: 2rem;
        }}

        h2 {{
            font-size: 1.3rem;
        }}

        h3 {{
            font-size: 1rem;
        }}

        /* =================================================
           SIDEBAR
        ================================================= */

        section[data-testid="stSidebar"] {{

            background-color: {CARD_BG};

            border-right:
                1px solid {BORDER};

        }}

        </style>

        """,

        unsafe_allow_html=True

    )


# =========================================================
# STATUS COLOR HELPER
# =========================================================

def get_status_color(status):

    if not status:
        return MUTED

    return STATUS_COLORS.get(

        str(status).upper(),
        MUTED

    )
