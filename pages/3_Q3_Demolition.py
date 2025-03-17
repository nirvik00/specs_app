import streamlit as st
import pandas as pd
import numpy as np

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
st.write("Does the project require demolition?")
opts=["Yes", "No"]
q3 = st.radio(
    "Select one",
    opts,
    captions=["The project requires demolition", "Project does NOT require demolition"],
    index = previous_selected_index
)


#### get user selection
res = opts[opts.index(q3)].strip().replace(" ", "").replace("/","_")
st.write(f"You selected {res}")

##### set the session state
button = st.button("Submit")
if button:
    st.session_state.q3_state = res


#### get data for table
if res=="Yes":
    df = pd.read_csv("output.csv")
    df2 =df.loc[df['q_num']==3]
    df2.reset_index(drop=True, inplace=True)
    df2.index += 1
    # st.table(df2)#### output table
    st.dataframe(df2)#### output table


#### update the sidebar
# with st.sidebar:
#     st.write(f"project name is {st.session_state.proj_name_state}")
#     st.write(f"project number is {st.session_state.proj_num_state}")
#     st.write(f"q1 - Project type is set to {st.session_state.q1_state}")
#     st.write(f"q2 - Typology is set to {st.session_state.q2_state}")
#     st.write(f"q3 - Demolition is set to {st.session_state.q3_state}")
#     st.write(f"q4 - Mulitple stories is set to {st.session_state.q4_state}")
#     st.write(f"q5 - Exterior opaque Materials is set to {st.session_state.q5_state}")
#     st.write(f"q6 - Backup for q5 is set to {st.session_state.q6_state}")
#     st.write(f"q7 - Anticipated floor finishes {st.session_state.q7_state}")
#     st.write(f"q8 - Ceiling materials is set to {st.session_state.q8_state}")