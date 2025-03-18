import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Question 6"
)

# set state based on session state
previous_selected_index=0
if 'q6_state' in st.session_state:
    if st.session_state.q6_state == "Cold-Formed Metal Framing":
        previous_selected_index = 0
    elif st.session_state.q6_state == "CMU":
        previous_selected_index = 1
    else:
        previous_selected_index = 0


# display ui, radio buttons on screen
st.write("What is the backup for exterior walls?")
q6 = st.radio(
    "Select one",
    ["Cold-Formed Metal Framing", "CMU"],
    index = previous_selected_index
)
st.write(f"You selected: {q6}")


##### set the session state
button = st.button("Submit")
if button:
    st.session_state.q6_state = q6


#### get data for table 
df = pd.read_csv('output.csv')
if q6 == "Cold-Formed Metal Framing":
    df2= df.loc[(df['q_num'] == 6) & (df['answer'] == "ColdFormedMetalFraming")]
else:
    df2= df.loc[(df['q_num'] == 6) & (df['answer'] == "CMU")]


#### write the table if no error
# st.table(df2)
result=df2
result.reset_index(drop=True, inplace=True)
result.index+=1
st.dataframe(result)


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