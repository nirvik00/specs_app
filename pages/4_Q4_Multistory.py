import streamlit as st
import pandas as pd
from os.path import join

st.set_page_config(
    page_title="Question 4"
)

# set state based on session state
previous_selected_index=0
if 'q4_state' in st.session_state:
    if st.session_state.q4_state == "Yes":
        previous_selected_index = 0
    elif st.session_state.q4_state == "No":
        previous_selected_index = 1
    else:
        previous_selected_index = 0

# display ui, radio buttons on screen
st.write("Are there multiple stories?")
opts = ["Yes", "No"]
captions = ["NewBuilding, Addition, Addition//Renovation or Renovation", "Does not have multiple stories"]
q4 = st.radio(
    "Select one",
    opts,
    captions = captions,
    index = previous_selected_index
)

#### get user selection
index = opts.index(q4)

##### set the session state
button = st.button("Submit")
user_selection = captions[opts.index(st.session_state['q4_state'])]

if button:
    res = opts[index]
    st.session_state.q4_state = res
    st.switch_page(join('pages', '5_Q5_Exterior_Materials.py'))
    
#### get data for table
if q4 == "Yes" and (st.session_state.q1_state=='NewBuilding' or st.session_state.q1_state=='Addition_Renovation'):
    df = pd.read_csv("output.csv")
    df2 = df.loc[(df["q_num"] == 4) & (df["answer"]=="Yes_NewBuilding_Addition_Addition_Renovation")]
    df2['answer'] = "Yes"
    df2 = df2.sort_values(by='sec_num')
    df2.reset_index(drop=True, inplace=True)
    df2.index +=1
    # st.table(df2) #### output table
    st.dataframe(df2)
elif q4 == "Yes" and st.session_state.q1_state=='Renovation':
    df = pd.read_csv("output.csv")
    df2 = df.loc[(df["q_num"] == 4) & (df["answer"]=="Yes_Renovation")]
    df2['answer'] = "Yes"
    df2 = df2.sort_values(by='sec_num')
    df2.reset_index(drop=True, inplace=True)
    df2.index +=1
    # st.table(df2) #### output table
    st.dataframe(df2)


### update the sidebar
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