import streamlit as st
import pandas as pd
from os.path import join

# OUTPUT_FILE = "output_updated.csv"
OUTPUT_FILE = "output_updated_separation.csv"

st.set_page_config(
    page_title="Question 7",
    initial_sidebar_state="expanded"
)

# set state based on session state
previous_selected_index=[]
if 'q7_state' in st.session_state:
    for i, e in enumerate(st.session_state.q7_state.split(", ")):
        previous_selected_index.append(e)

# display ui, radio buttons on screen
st.write("What are the special ceiling materials?")
st.write("Select all that apply")
opts = ["Acoustical Gypsum Board", "Acoustical Baffles", "Wood", "Metal"]
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
    st.switch_page(join('pages', '8_Question_Breakdown.py'))

#### get list of all selected options
res2 =[]
for e in opts:
    r = e.strip().replace(" ", "")
    res2.append(r)

result = None
df = pd.read_csv(OUTPUT_FILE)
for i, e in enumerate(q7):
    if e == True:
        res = res2[i].strip().replace(" ", "").replace("/","_")
        df2 = df.loc[(df['q_num'] == 7) & (df["answer"] == res2[i])]
        result= pd.concat([result, df2])
        result = result.drop_duplicates(subset=["sec_num"], keep="first")

#### write the table if no error
try:
    result = result.sort_values(by='sec_num')
    result.reset_index(drop=True, inplace=True)
    # result.index+=1
    st.dataframe(result)
except:
    pass

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





