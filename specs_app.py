import streamlit as st
from os.path import join

st.set_page_config(
    page_title="Home"
)

#
st.title("Specs Form")

if 'proj_name_state' not in st.session_state:
    st.session_state['proj_name_state'] = "no name"
if 'proj_num_state' not in st.session_state:
    st.session_state['proj_num_state'] = "no num"
# project type
if 'q1_state' not in st.session_state: 
    st.session_state['q1_state'] = "NewBuilding"
# demolition
if 'q2_state' not in st.session_state:
    st.session_state['q2_state'] = "Yes"
# multistory
if 'q3_state' not in st.session_state:
    st.session_state['q3_state'] = "Yes_NewBuilding_Addition_Addition/Renovation"
# opaque exterior materials
if 'q4_state' not in st.session_state:
    st.session_state['q4_state'] = "[]"
# is cmu back up
if 'q5_state' not in st.session_state:
    st.session_state['q5_state'] = "Yes"
# floor finish
if 'q6_state' not in st.session_state:# 
    st.session_state['q6_state'] = "[]"
# ceiling materials
if 'q7_state' not in st.session_state:
    st.session_state['q7_state'] = "[]"
#
if 'result_sec_nums' not in st.session_state:
    st.session_state['result_sec_nums'] = []
if 'result_sec_names' not in st.session_state:
    st.session_state['result_sec_names'] = []    
if 'show_states' not in st.session_state:
    st.session_state['show_states'] = False
#
my_name=st.text_input("enter project name", st.session_state['proj_name_state'])
my_num=st.text_input("enter project number", st.session_state['proj_num_state'])
submit = st.button("Submit")
if submit:
    st.session_state['proj_name_state']= my_name
    st.session_state['proj_num_state']= my_num
    st.switch_page(join('pages', '1_Q1_Project_Type.py'))
#
# set state based on session state
previous_selected_index=0
if 'show_states' in st.session_state:
    if st.session_state.show_states == True:
        previous_selected_index = 0
    elif st.session_state.show_states == False:
        previous_selected_index = 1
    else:
        previous_selected_index = 0

st.write("Show states in sidebar?")
opts=["Yes", "No"]
q00 = st.radio(
    "Select one",
    opts,
    captions=["Show states", "Do not show states"],
    index = previous_selected_index
)

if q00 == 'Yes': 
    st.session_state.show_states = True
else:
    st.session_state.show_states = False


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

# streamlit run specs_app.py