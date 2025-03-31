import streamlit as st
import pandas as pd
from os.path import join

st.set_page_config(
    page_title="Question 5"
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
st.write("What is the backup for exterior walls?")
opts = ["Yes", "No"]
captions = ["Use CMU as backup", "Does not use CMU as backup"]
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
df = pd.read_csv('output.csv')
if q5 == "Cold-Formed Metal Framing":
    df2= df.loc[(df['q_num'] == 5) & (df['answer'] == "ColdFormedMetalFraming")]
else:
    df2= df.loc[(df['q_num'] == 5) & (df['answer'] == "CMU")]

#### write the table if no error
# st.table(df2)
result=df2
result = result.sort_values(by='sec_num')
result.reset_index(drop=True, inplace=True)
result.index+=1
st.dataframe(result)

if st.session_state.show_states == True:
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