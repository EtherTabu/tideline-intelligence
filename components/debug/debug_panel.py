# =========================================================
# TIDE LINE — DEBUG PANEL
# =========================================================

import streamlit as st
import json


def show_debug_panel(payload):

    with st.expander("⚠️ DEBUG CONSOLE", expanded=False):

        st.subheader("PAYLOAD")

        st.json(payload)

        st.subheader("TOP LEVEL TYPES")

        debug_types = {}

        for key, value in payload.items():

            debug_types[key] = str(type(value))

        st.json(debug_types)

        st.subheader("PREDICTION")

        st.write(payload.get("prediction"))

        st.subheader("TACTICAL")

        st.write(payload.get("tactical"))

        st.subheader("INLET")

        st.write(payload.get("inlet"))

        st.subheader("MARINE")

        st.write(payload.get("marine"))
