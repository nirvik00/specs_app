import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Question 1"
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
    captions=["A new building", "Addition or renovation to an existing building", "Renovation only"],
    index=previous_selected_index
)

#### get user selection
res = opts[opts.index(q1)].strip().replace(" ", "").replace("/","_")
st.write(f"You selected {res}")


#### update session state
submit = st.button("Submit")
if submit:
    st.session_state['q1_state']= res


#### get data for table
df = pd.read_csv("output.csv")
df2 = df.loc[(df['q_num'] == 1) & (df['answer'] == res)]
df2.reset_index(drop=True, inplace=True)
df2.index += 1
st.table(df2)####       output table 


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



