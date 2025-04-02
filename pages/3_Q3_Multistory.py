import streamlit as st
import pandas as pd
from os.path import join

# OUTPUT_FILE = "output_updated.csv"
OUTPUT_FILE = "output_updated_separation.csv"


st.set_page_config(
    page_title="Question 3"
)

# set state based on session state
previous_selected_index=0
if 'q3_state' in st.session_state:
    if st.session_state.q3_state == "Yes":
        previous_selected_index = 0
    elif st.session_state.q3_state == "No":
        previous_selected_index = 1
    else:
        previous_selected_index = 0

# display ui, radio buttons on screen
st.write("Are there multiple stories?")
opts = ["Yes", "No"]
captions = ["NewBuilding, Addition, Addition//Renovation or Renovation", "Does not have multiple stories"]
q3 = st.radio(
    "Select one",
    opts,
    captions = captions,
    index = previous_selected_index
)

#### get user selection
# index = opts.index(q3)

##### set the session state
button = st.button("Submit")
# user_selection = captions[opts.index(st.session_state['q3_state'])]

if button:
    # res = opts[index]
    st.session_state.q3_state = q3
    st.switch_page(join('pages', '4_Q4_Exterior_Materials.py'))

# st.write(st.session_state.q1_state, st.session_state.q3_state)

#### get data for table
if q3 == "Yes" and (st.session_state.q1_state=='NewBuilding' or st.session_state.q1_state=='Addition_Renovation'):
    df = pd.read_csv(OUTPUT_FILE)
    df2 = df.loc[(df["q_num"] == 3) & (df["answer"]=="Yes_NewBuilding_Addition_Addition_Renovation")]
    df2['answer'] = "Yes"
    df2 = df2.sort_values(by='sec_num')
    df2.reset_index(drop=True, inplace=True)
    # df2.index +=1
    st.dataframe(df2)
elif q3 == "Yes" and st.session_state.q1_state=='Renovation':
    df = pd.read_csv(OUTPUT_FILE)
    df2 = df.loc[(df["q_num"] == 3) & (df["answer"]=="Yes_Renovation")]
    df2['answer'] = "Yes"
    df2 = df2.sort_values(by='sec_num')
    df2.reset_index(drop=True, inplace=True)
    # df2.index +=1
    st.dataframe(df2)

 
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