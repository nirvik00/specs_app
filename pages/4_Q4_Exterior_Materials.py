import streamlit as st
import pandas as pd
from os.path import join

st.set_page_config(
    page_title="Question 4"
)

# set state based on session state
previous_selected_index=[]
if 'q4_state' in st.session_state:
    for i, e in enumerate(st.session_state.q4_state.split(", ")):
        previous_selected_index.append(e)

# display ui, radio buttons on screen
st.write("What are the opaque Exterior materials? (select all that apply)")
opts = ["Masonry", "Stone", "Metal Panel", "Fiber Cement Panel", "Terra Cotta", "Phenolic Panel", "EIFS", "Precast Concrete", "Cast Stone", "Architectural Concrete"]
q4=[]
for i, e in enumerate(opts):
    if e in previous_selected_index:
        x =st.checkbox(e, value=True)
    else:
        x =st.checkbox(e, value=False)
    q4.append(x)
submit = st.button("Submit")

#
#### GET session state
arr=[]
if submit:
    for i, e in enumerate(q4):
        if e == True:
            arr.append(opts[i])
    st.session_state['q4_state']= ", ".join(arr)
    st.switch_page(join('pages', '5_Q5_Backup_Exterior_Materials.py'))

#### get data for table
res2 =[] # rectified strings for checking against csv output from MW parser
for e in opts:
    r = e.strip().replace(" ", "")
    res2.append(r)

df = pd.read_csv("output.csv")
result= None
s=""
for i, e in enumerate(q4):
    if e == True:
        # s += str(i) + ":" + str(e)+ ", "
        df2 = df.loc[(df['q_num']==4) & (df['answer']==res2[i])]
        result = pd.concat([result, df2])
        result = result.drop_duplicates(subset=["sec_num"], keep="first")

#### output table
try:
    result = result.sort_values(by='sec_num')
    result.reset_index(drop=True, inplace=True)
    result.index += 1
    # st.table(result)#### output table
    st.dataframe(result)#### output table
except:
    pass


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