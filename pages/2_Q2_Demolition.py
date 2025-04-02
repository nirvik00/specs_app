import streamlit as st
import pandas as pd
import numpy as np
from os.path import join 

OUTPUT_FILE = "output_updated.csv"

st.set_page_config(
    page_title="Question 2"
)

# set state based on session state
previous_selected_index=0
if 'q2_state' in st.session_state:
    if st.session_state.q2_state == "Yes":
        previous_selected_index = 0
    elif st.session_state.q2_state == "No":
        previous_selected_index = 1
    else:
        previous_selected_index = 0

# display ui, radio buttons on screen
st.write("Does the project require demolition?")
opts=["Yes", "No"]
q2 = st.radio(
    "Select one",
    opts,
    captions=["The project requires demolition", "Project does not require demolition"],
    index = previous_selected_index
)


#### get user selection
res = opts[opts.index(q2)].strip().replace(" ", "").replace("/","_")

##### set the session state
button = st.button("Submit")
if button:
    st.session_state.q2_state = res
    st.switch_page(join('pages', '3_Q3_Multistory.py'))
    
if res=="Yes":
    df = pd.read_csv(OUTPUT_FILE)
    df2 =df.loc[df['q_num']==2]
    df2 = df2.sort_values(by='sec_num')
    df2.reset_index(drop=True, inplace=True)
    df2.index += 1
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