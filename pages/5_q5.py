import streamlit as st

st.set_page_config(
    page_title="Question 5"
)

st.write("What are the opaque Exterior materials? (select all that apply)")

res = ["Masonry", "Stone", "Metal Panel", "Floor Cement Panel", "Terra Cota", "Phenolic Panel", "EIFS", "Precast Concrete", "Cast Stone", "Architectural Concrete"]
q5=[]
for e in res:
    x =st.checkbox(e)
    q5.append(x)