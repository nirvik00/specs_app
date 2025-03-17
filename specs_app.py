import streamlit as st



st.set_page_config(
    page_title="Home"
)

#
st.title("Specs Form")

if 'proj_name_state' not in st.session_state:
    st.session_state['proj_name_state'] = "no name"
if 'proj_num_state' not in st.session_state:
    st.session_state['proj_num_state'] = "no num"
if 'q1_state' not in st.session_state:
    st.session_state['q1_state'] = "New Building"
if 'q2_state' not in st.session_state:
    st.session_state['q2_state'] = "General"
if 'q3_state' not in st.session_state:
    st.session_state['q3_state'] = "Yes"
if 'q4_state' not in st.session_state:
    st.session_state['q4_state'] = "Yes-1"
if 'q5_state' not in st.session_state:
    st.session_state['q5_state'] = "[]"
if 'q6_state' not in st.session_state:
    st.session_state['q6_state'] = "Cold-Formed metal framing"
if 'q7_state' not in st.session_state:
    st.session_state['q7_state'] = "[]"
if 'q8_state' not in st.session_state:
    st.session_state['q8_state'] = "[]"

my_name=st.text_input("enter project name", st.session_state['proj_name_state'])
my_num=st.text_input("enter project number", st.session_state['proj_num_state'])
submit = st.button("Submit")
if submit:
    st.session_state['proj_name_state']= my_name
    st.session_state['proj_num_state']= my_num


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

# streamlit run specs_app.py