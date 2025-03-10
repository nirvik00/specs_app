import streamlit as st

st.set_page_config(
    page_title="Question 6"
)

st.write("Backup for exterior walls")

q1 = st.radio(
    "What is the backup for exterior walls?",
    ["Cold-Formed Metal Framing", "CMU"],
)

