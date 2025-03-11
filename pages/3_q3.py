import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Question 3"
)

st.write("Does the project require demolition?")


opts=["Yes", "No"]
q3 = st.radio(
    "Select one",
    opts,
    captions=["The project requires demolition", "Project does NOT require demolition"]
)

res = opts[opts.index(q3)].strip().replace(" ", "").replace("/","_")
st.write(f"You selected {res}")

if res=="Yes":
    df = pd.read_csv("output.csv")
    df2 =df.loc[df['q_num']==3]
    df2.reset_index(drop=True, inplace=True)
    df2.index += 1
    st.table(df2)