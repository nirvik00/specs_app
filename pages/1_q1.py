import streamlit as st
import pandas as pd
import numpy as np



st.set_page_config(
    page_title="Question 1"
)

st.write("What type of project is this?")

q1 = st.radio(
    "Is this project a",
    ["new building", "addition//renovation", "renovation"],
    captions=["A new building", "Addition or renovation to an existing building", "Renovation only"]
)

df = pd.read_csv("output.csv")
df2 = df.loc[(df['q_num'] == 1) & (df['answer'] == "NewBuilding")]
st.table(df2)
