import streamlit as st

st.set_page_config(
    page_title="Question 4"
)

st.write("Are there multiple stories?")

opts = ["Yes", "No"]
q4 = st.radio(
    "Select",
    opts,
)

res = opts[opts.index(q4)].strip().replace(" ", "").replace("/","_")
st.write(f"You selected {res}")


