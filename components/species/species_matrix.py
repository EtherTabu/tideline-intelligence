import streamlit as st


def render_species_matrix(matrix):

    st.markdown(
        "## 🎯 Species Opportunity Matrix"
    )

    cols = st.columns(
        len(matrix)
    )

    for col, item in zip(
        cols,
        matrix
    ):

        with col:

            st.metric(

                item["species"],

                f"{item['score']}%",

                item["group"]

            )