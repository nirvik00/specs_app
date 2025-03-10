import streamlit as st

st.set_page_config(
    page_title="Question 7"
)

st.write("Anticipated floor finishes")


st.write("What are the anticipated floor finishes? (select all that apply)")


res_7 = ["Carpet", "Resilient Floor Finishes", "Tile", "Wood"]
q7=[]
for e in res_7:
    x =st.checkbox(e)
    q7.append(x)

