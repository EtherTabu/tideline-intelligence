import streamlit as st

def show():
    c1, c2 = st.columns([3, 1])
    with c1:
        st.title("🌊 TIDE LINE | STRATEGIC COMMAND")
        st.subheader("Juno Beach / Jupiter Operational Hub")
    with c2:
        st.write("") # Alignment spacer
        st.success("🟢 SYSTEM ONLINE")
