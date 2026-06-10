import streamlit as st


# =========================================================
# TITLE
# =========================================================

def tactical_title(title, subtitle):

    st.markdown(
        f"""
<div style="
padding:1rem 0 0.5rem 0;
">

<div style="
color:#F4F8FF;
font-size:1.55rem;
font-weight:800;
letter-spacing:0.02em;
line-height:1.1;
">
{title}
</div>

<div style="
color:#6F88A5;
font-size:0.72rem;
text-transform:uppercase;
letter-spacing:0.08em;
margin-top:0.25rem;
">
{subtitle}
</div>

</div>
""",
        unsafe_allow_html=True
    )


# =========================================================
# LABEL
# =========================================================

def tactical_label(text):

    st.markdown(
        f"""
<div style="
color:#00D1FF;
font-size:0.68rem;
font-weight:800;
text-transform:uppercase;
letter-spacing:0.08em;
margin-bottom:0.55rem;
margin-top:0.5rem;
">
{text}
</div>
""",
        unsafe_allow_html=True
    )


# =========================================================
# STATUS
# =========================================================

def tactical_status(message, level="normal"):

    colors = {

        "normal": "#00FF99",
        "warning": "#FFD24A",
        "danger": "#FF5C7A"

    }

    color = colors.get(level, "#00FF99")

    st.markdown(
        f"""
<div style="
border-left:4px solid {color};
background:rgba(255,255,255,0.03);
padding:0.85rem;
border-radius:12px;
margin-top:0.4rem;
margin-bottom:1rem;
color:#F4F8FF;
font-weight:700;
letter-spacing:0.01em;
">
{message}
</div>
""",
        unsafe_allow_html=True
    )


# =========================================================
# METRIC
# =========================================================

def tactical_metric(label, value, color="#00FF99"):

    st.markdown(
        f"""
<div style="
border:1px solid rgba(0,180,255,0.16);
border-radius:16px;
padding:1rem;
margin-bottom:0.8rem;
background:rgba(255,255,255,0.02);
">

<div style="
color:#6D829C;
font-size:0.68rem;
text-transform:uppercase;
letter-spacing:0.08em;
margin-bottom:0.2rem;
">
{label}
</div>

<div style="
color:{color};
font-size:2.2rem;
font-weight:800;
line-height:1;
">
{value}
</div>

</div>
""",
        unsafe_allow_html=True
    )


# =========================================================
# DIVIDER
# =========================================================

def tactical_divider():

    st.markdown(
        """
<div style="
height:1px;
background:rgba(255,255,255,0.08);
margin:1rem 0 1rem 0;
">
</div>
""",
        unsafe_allow_html=True
    )