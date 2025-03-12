import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import numpy as np

import plotly.express as px
data = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

fig = px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
)

# Plot!
st.plotly_chart(fig)


#### update the sidebar
with st.sidebar:
    st.write(f"project name is {st.session_state.proj_name_state}")
    st.write(f"project number is {st.session_state.proj_num_state}")
    st.write(f"q1 - Project type is set to {st.session_state.q1_state}")
    st.write(f"q2 - Typology is set to {st.session_state.q2_state}")
    st.write(f"q3 - Demolition is set to {st.session_state.q3_state}")
    st.write(f"q4 - Mulitple stories is set to {st.session_state.q4_state}")
    st.write(f"q5 - Exterior opaque Materials is set to {st.session_state.q5_state}")
    st.write(f"q6 - Backup for q5 is set to {st.session_state.q6_state}")
    st.write(f"q7 - Anticipated floor finishes {st.session_state.q7_state}")
    st.write(f"q8 - Ceiling materials is set to {st.session_state.q8_state}")

q1_state = st.session_state.q1_state
res = q1_state.strip().replace(" ", "").replace("/","_")

result = None
df = pd.read_csv("output.csv")

#### get data for table
df = pd.read_csv("output.csv")
df2 = df.loc[(df['q_num'] == 1) & (df['answer'] == res)]
df2.reset_index(drop=True, inplace=True)
df2.index += 1
st.table(df2)####       output table

def get_q8_state(q8):
    for i, e in enumerate(q8):
        if e == True:
            if i == 1:
                df2 = df.loc[(df['q_num'] == 8) & (df["answer"] == "AcousticalBaffles")]
            else:
                df2 = df.loc[(df['q_num'] == 8) & (df["answer"] == res2[i])]
            result= pd.concat([result, df2])

