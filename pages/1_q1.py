import streamlit as st
import pandas as pd
import numpy as np



st.set_page_config(
    page_title="Question 1"
)

st.write("What type of project is this?")
opts =["New Building", "Addition/Renovation", "Renovation"]
q1 = st.radio(
    "Select:",
    opts,
    captions=["A new building", "Addition or renovation to an existing building", "Renovation only"]
)

res = opts[opts.index(q1)].strip().replace(" ", "").replace("/","_")
st.write(f"You selected {res}")


df = pd.read_csv("output.csv")
df2 = df.loc[(df['q_num'] == 1) & (df['answer'] == res)]
st.table(df2)
