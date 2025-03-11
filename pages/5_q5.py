import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Question 5"
)

st.write("What are the opaque Exterior materials? (select all that apply)")

opts = ["Masonry", "Stone", "Metal Panel", "Fiber Cement Panel", "Terra Cotta", "Phenolic Panel", "EIFS", "Precast Concrete", "Cast Stone", "Architectural Concrete"]
res2 =[]
for e in opts:
    r = e.strip().replace(" ", "")
    res2.append(r)


q5=[]
for e in opts:
    x =st.checkbox(e)
    q5.append(x)

#### GET session state
submit = st.button("Submit")
arr=[]
if submit:
    for i, e in enumerate(q5):
        if e == True:
            arr.append(opts[i])
    st.session_state['q5_state']= ", ".join(arr)

#### get data for table
df = pd.read_csv("output.csv")
result= None
s=""
for i, e in enumerate(q5):
    if e == True:
        # s += str(i) + ":" + str(e)+ ", "
        df2 = df.loc[(df['q_num']==5) & (df['answer']==res2[i])]
        result = pd.concat([result, df2])


#### output table
try:
    result.reset_index(drop=True, inplace=True)
    result.index += 1
    st.table(result)
except:
    pass

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