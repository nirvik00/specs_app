import streamlit as st

st.set_page_config(
    page_title="Question 8"
)

st.write("Special ceiling materials")

st.write("What are the special ceiling materials? (select all that apply)")

res_8 = ["Acoustical Gypsum Board", "Acoustical Gypsum Baffles", "Linear Wood", "Metal"]
q8=[]
for e in res_8:
    x =st.checkbox(e)
    q8.append(x)

