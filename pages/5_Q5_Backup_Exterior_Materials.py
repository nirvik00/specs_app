import streamlit as st
import pandas as pd
from os.path import join

# OUTPUT_FILE = "output_updated.csv"
OUTPUT_FILE = "output_updated_separation.csv"

st.set_page_config(
    page_title="Question 5",
    initial_sidebar_state="expanded"
)

# set state based on session state
previous_selected_index=0
if 'q5_state' in st.session_state:
    if st.session_state.q5_state == "Yes":
        previous_selected_index = 0
    elif st.session_state.q5_state == "No":
        previous_selected_index = 1
    else:
        previous_selected_index = 0

# display ui, radio buttons on screen
st.write("Is the backup for exterior walls CMU?")
opts = ["Yes", "No"]
captions = ["Use CMU as backup for opaque exterior material", "Does not use CMU as backup"]
q5 = st.radio(
    "Select one",
    opts,
    captions = captions,
    index = previous_selected_index
)

##### set the session state
button = st.button("Submit")
if button:
    st.session_state.q5_state = q5
    st.switch_page(join('pages', '6_Q6_Floor_Finish.py'))

#### get data for table 
df = pd.read_csv(OUTPUT_FILE)
if q5 == "Yes":
    df2 = df.loc[(df['q_num'] == 5) & (df['answer'] == "CMU")]
    result = df2
    result = result.sort_values(by='sec_num')
    result.reset_index(drop=True, inplace=True)
    # result.index+=1
    st.dataframe(result)

#### write the table if no error
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