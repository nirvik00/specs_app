import streamlit as st

st.set_page_config(
    page_title="Question 2"
)

st.write("Type of building is not accounted for at present")

q2 = st.radio(
    "What is the building type?",
    ["general", "k-12", "hospital"],
    captions=["general", "school building", "hospital building"]
)