import streamlit as st

st.set_page_config(
    page_title="Question 2"
)

if 'q2_state' not in st.session_state:
    st.session_state['q2_state'] = "not set"


# note this is not used in calcs
st.write("Type of building is not accounted for at present")

# display radio buttons
opts = ["General", "K-12", "Health Care"]
q2 = st.radio(
    "What is the building type?",
    opts,
    captions=["For all types", "school building", "Health Care"],
    key="q2_state"
)

submit = st.button("Submit")

#### get user selection
res = opts[opts.index(q2)].strip().replace(" ", "").replace("/","_")
if submit:
    st.session_state['q2_state']= res

st.write(f"User selection: {st.session_state['q2_state']}")


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
