import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Question 1"
)

st.write("What type of project is this?")
update_table=False
# display radio buttons
st.write("Are there multiple stories?")
opts = ["Yes - 1", "Yes - 2",  "No"]
captions = ["NewBuilding, Addition, Addition//Renovation", "Renovation", "Does not have multiple stories"]
q4 = st.radio(
    "Select one",
    opts,
    captions = captions,
    key = 'q4_state',
)


st.write(f"new state: {st.session_state['q4_state']}")
st.write(f"option q4: {q4}")

#### get data for table
q4 = st.session_state.q4_state
if q4 == "Yes - 1":
    df = pd.read_csv("output.csv")
    df2 = df.loc[(df["q_num"] == 4) & (df["answer"]=="Yes_NewBuilding_Addition_Addition_Renovation")]
    df2['answer'] = "Yes"
    df2.reset_index(drop=True, inplace=True)
    df2.index +=1
    # st.table(df2) #### output table
    st.dataframe(df2)

elif q4 == "Yes - 2":
    df = pd.read_csv("output.csv")
    df2 = df.loc[(df["q_num"] == 4) & (df["answer"]=="Yes_Renovation")]
    df2['answer'] = "Yes"
    df2.reset_index(drop=True, inplace=True)
    df2.index +=1
    # st.table(df2) #### output table
    st.dataframe(df2)

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


