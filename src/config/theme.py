# =========================================================
# TIDE LINE — GLOBAL THEME ENGINE
# =========================================================

import streamlit as st


# =========================================================
# CORE COLORS
# =========================================================

BACKGROUND = "#050816"

CARD_BG = "#09111F"

CARD_BG_ALT = "#0D1728"

BORDER = "#1E293B"

TEXT = "#E2E8F0"

MUTED = "#7C93B0"

GREEN = "#00FF99"

CYAN = "#38BDF8"

BLUE = "#3B82F6"

YELLOW = "#D4C21A"

ORANGE = "#FF9F43"

RED = "#FF4D6D"

PURPLE = "#C084FC"


# =========================================================
# TACTICAL GRADIENTS
# =========================================================

PANEL_GRADIENT = """

linear-gradient(
135deg,
rgba(8,15,30,0.96),
rgba(3,8,20,0.98)
)

"""

COMMAND_GRADIENT = """

linear-gradient(
90deg,
rgba(0,255,170,0.14),
rgba(0,120,255,0.04)
)

"""

DANGER_GRADIENT = """

linear-gradient(
90deg,
rgba(255,80,80,0.18),
rgba(255,0,0,0.05)
)

"""

SUCCESS_GRADIENT = """

linear-gradient(
90deg,
rgba(0,255,140,0.14),
rgba(0,255,200,0.05)
)

"""


# =========================================================
# STATUS COLORS
# =========================================================

STATUS_COLORS = {

    "GOOD": GREEN,

    "MODERATE": YELLOW,

    "DANGER": RED,

    "CRITICAL": RED,

    "LOW": CYAN,

    "HIGH": GREEN,

    "EXTREME": RED,

    "ACTIVE": GREEN,

    "ONLINE": GREEN,

    "OFFLINE": RED,

    "WARNING": ORANGE

}


# =========================================================
# PAGE CONFIG
# =========================================================

def configure_page():

    st.set_page_config(

        page_title="TIDE LINE",

        page_icon="🌊",

        layout="wide",

        initial_sidebar_state="collapsed"

    )


# =========================================================
# GLOBAL CSS ENGINE
# =========================================================

def inject_global_css():

    st.markdown(

        f"""

<style>

/* =====================================================
   GLOBAL
===================================================== */

html,
body,
[class*="css"] {{

    background-color: {BACKGROUND};

    color: {TEXT};

    font-family:

        Inter,
        system-ui,
        sans-serif;

}}

/* =====================================================
   MAIN LAYOUT
===================================================== */

.block-container {{

    padding-top: 0.8rem;

    padding-bottom: 1rem;

    padding-left: 1rem;

    padding-right: 1rem;

    max-width: 100%;

}}

/* =====================================================
   REMOVE STREAMLIT CLUTTER
===================================================== */

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

/* =====================================================
   CARDS
===================================================== */

div[data-testid="stVerticalBlockBorderWrapper"] {{

    background: {PANEL_GRADIENT};

    border:

        1px solid rgba(56,189,248,0.14);

    border-radius: 14px;

    box-shadow:

        0 0 0 rgba(0,0,0,0);

    transition: 0.25s ease;

}}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {{

    border:

        1px solid rgba(0,255,180,0.24);

}}

/* =====================================================
   METRICS
===================================================== */

div[data-testid="metric-container"] {{

    background: {PANEL_GRADIENT};

    border:

        1px solid rgba(56,189,248,0.12);

    border-radius: 12px;

    padding: 0.75rem;

}}

/* =====================================================
   ALERTS
===================================================== */

div.stAlert {{

    border-radius: 10px;

    border:

        1px solid rgba(56,189,248,0.14);

}}

/* =====================================================
   BUTTONS
===================================================== */

.stButton > button {{

    background:

        rgba(0,0,0,0);

    border:

        1px solid rgba(56,189,248,0.22);

    color: {TEXT};

    border-radius: 10px;

    transition: 0.25s ease;

}}

.stButton > button:hover {{

    border:

        1px solid rgba(0,255,180,0.38);

    color: white;

}}

/* =====================================================
   VIDEO / IFRAMES
===================================================== */

iframe,
video {{

    border-radius: 14px !important;

    overflow: hidden !important;

}}

/* =====================================================
   SIDEBAR
===================================================== */

section[data-testid="stSidebar"] {{

    background:

        {CARD_BG};

    border-right:

        1px solid rgba(56,189,248,0.12);

}}

/* =====================================================
   TYPOGRAPHY
===================================================== */

h1,
h2,
h3,
h4 {{

    color: {TEXT};

    letter-spacing: -0.02em;

}}

h1 {{
    font-size: 2rem;
}}

h2 {{
    font-size: 1.35rem;
}}

h3 {{
    font-size: 1rem;
}}

/* =====================================================
   DIVIDERS
===================================================== */

hr {{

    border-color:

        rgba(56,189,248,0.08);

}}

/* =====================================================
   SCROLLBAR
===================================================== */

::-webkit-scrollbar {{

    width: 10px;

}}

::-webkit-scrollbar-track {{

    background: #040B16;

}}

::-webkit-scrollbar-thumb {{

    background: #12304D;

    border-radius: 12px;

}}

::-webkit-scrollbar-thumb:hover {{

    background: #1D4F7A;

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