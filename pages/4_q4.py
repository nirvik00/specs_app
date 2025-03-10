import streamlit as st

st.set_page_config(
    page_title="Question 4"
)

q4 = st.radio(
    "Are there multiple stories?",
    ["Yes", "No"],
    #captions=["school building", "hospital building"]
)