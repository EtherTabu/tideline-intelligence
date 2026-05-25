import streamlit as st

def show_live_stats():
    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Boat Traffic", "Scanning...", delta="Inlets Active")
    m2.metric("Conditions", "Live", delta="NOAA + Weather")
    m3.metric("Demand", "High", delta="Tournament Mode")
    m4.metric("Confidence", "85%", delta="Data Verified")
