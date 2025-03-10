import streamlit as st

st.set_page_config(
    page_title="Question 3"
)

st.write("Demolitiion")

q3 = st.radio(
    "Does the project require demolition?",
    ["Yes", "No"],
    captions=["The project requires demolition", "Project does NOT require demolition"]
)