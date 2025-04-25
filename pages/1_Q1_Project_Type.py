import streamlit as st
import pandas as pd
import numpy as np
from os.path import join

INPUT_FILE=""
# OUTPUT_FILE = "output_updated.csv"
OUTPUT_FILE = "output_updated_separation.csv"

st.set_page_config(
    page_title="Question 1",
    initial_sidebar_state="expanded"
)

#
st.write("What type of project is this?")

# set state based on session state
previous_selected_index=0
if 'q1_state' in st.session_state:
    if st.session_state.q1_state == "NewBuilding":
        previous_selected_index = 0
    elif st.session_state.q1_state == "Addition_Renovation":
        previous_selected_index = 1
    elif st.session_state.q1_state == "Renovation":
        previous_selected_index = 2
    else:
        previous_selected_index = 0

#
# display radio buttons
opts =["New Building", "Addition/Renovation", "Renovation"]
q1 = st.radio(
    "Select:",
    opts,
    captions=["A new building", 
              "Addition or renovation to an existing building", 
              "Renovation only"],
    index=previous_selected_index
)

#### get user selection
res = opts[opts.index(q1)].strip().replace(" ", "").replace("/","_")

#### update session state
submit = st.button("Submit")
if submit:
    st.session_state['q1_state']= res
    st.switch_page(join('pages', '2_Q2_Demolition.py'))

#### get data for table
df = pd.read_csv(OUTPUT_FILE)
df2 = df.loc[(df['q_num'] == 1) & (df['answer'] == res)]
df2 = df2.sort_values(by='sec_num')
df2.reset_index(drop=True, inplace=True)
# df2.index += 1
st.dataframe(df2)#### output table

### update the sidebar
if st.session_state.show_states == True:
    with st.sidebar:
        st.write(f"project name is {st.session_state.proj_name_state}")
        st.write(f"project number is {st.session_state.proj_num_state}")
        st.write(f"q1 - Project type is set to {st.session_state.q1_state}")
        st.write(f"q2 - Demolition is set to {st.session_state.q2_state}")
        st.write(f"q3 - Mulitple stories is set to {st.session_state.q3_state}")
        st.write(f"q4 - Exterior opaque Materials is set to {st.session_state.q4_state}")
        st.write(f"q5 - Backup for CMU {st.session_state.q5_state}")
        st.write(f"q6 - Anticipated floor finishes {st.session_state.q6_state}")
        st.write(f"q7 - Ceiling materials is set to {st.session_state.q7_state}")


