import streamlit as st
import pandas as pd
from os.path import join


st.set_page_config(
    page_title="Question 7"
)

# set state based on session state
previous_selected_index=[]
if 'q7_state' in st.session_state:
    for i, e in enumerate(st.session_state.q7_state.split(", ")):
        previous_selected_index.append(e)

# display ui, radio buttons on screen
st.write("What are the anticipated floor finishes? (select all that apply)")
opts = ["Carpet", "Resilient Flooring", "Tile", "Wood"]
q7=[]
for i, e in enumerate(opts):
    if e in previous_selected_index:
        x =st.checkbox(e, value=True)
    else:
        x =st.checkbox(e, value=False)        
    q7.append(x)

#### update session state
submit = st.button("Submit")
arr=[]
if submit:
    for i, e in enumerate(q7):
        if e == True:
            arr.append(opts[i])
    st.session_state['q7_state']= ", ".join(arr)
    st.switch_page(join('pages', '8_Q8_Ceiling_Materials.py'))

#### get data for tables
res2 =[]
for e in opts:
    r = e.strip().replace(" ", "")
    res2.append(r)

result = None
df = pd.read_csv("output.csv")
for i, e in enumerate(q7):
    if e == True:
        df2 = df.loc[(df['q_num'] == 7) & (df["answer"] == res2[i])]
        result= pd.concat([result, df2])
        result = result.drop_duplicates(subset=["sec_num"], keep="first")

#### write the table if no error
try:
    result = result.sort_values(by='sec_num')
    result.reset_index(drop=True, inplace=True)
    result.index+=1
    # st.table(result)
    st.dataframe(result)####       output table
except:
    pass

if st.session_state.show_states == True:
    with st.sidebar:
        st.header("Specs Result")
        st.write(f"project name is {st.session_state.proj_name_state}")
        st.write(f"project number is {st.session_state.proj_num_state}")
        st.write(f"q1 - Project type is set to {st.session_state.q1_state}")
        st.write(f"q2 - Typology is set to {st.session_state.q2_state}")
        st.write(f"q3 - Demolition is set to {st.session_state.q3_state}")
        st.write(f"q4 - Mulitple stories is set to {st.session_state.q4_state}")
        st.write(f"q5 - Exterior opaque Materials is set to {st.session_state.q5_state}")
        st.write(f"q6 - Backup for q5 is set to {st.session_state.q6_state}")
        st.write(f"q7 - Anticipated floor finishes is set to {st.session_state.q7_state}")
        st.write(f"q8 - Ceiling materials is set to {st.session_state.q8_state}")