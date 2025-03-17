import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Question 8"
)



# set state based on session state
previous_selected_index=[]
if 'q8_state' in st.session_state:
    for i, e in enumerate(st.session_state.q8_state.split(", ")):
        previous_selected_index.append(e)

# display ui, radio buttons on screen
st.write("What are the special ceiling materials?")
st.write("Select all that apply")
opts = ["Acoustical Gypsum Board", "Acoustical Gypsum Baffles", "Linear Wood", "Metal"]
q8=[]
for i, e in enumerate(opts):
    if e in previous_selected_index:
        x =st.checkbox(e, value=True)
    else:
        x =st.checkbox(e, value=False)       
    q8.append(x)

#### update session state
submit = st.button("Submit")
arr=[]
if submit:
    for i, e in enumerate(q8):
        if e == True:
            arr.append(opts[i])
    st.session_state['q8_state']= ", ".join(arr)

#### get list of all selected options
res2 =[]
for e in opts:
    r = e.strip().replace(" ", "")
    res2.append(r)

result = None
df = pd.read_csv("output.csv")
for i, e in enumerate(q8):
    if e == True:
        if i == 1:
            df2 = df.loc[(df['q_num'] == 8) & (df["answer"] == "AcousticalBaffles")]
        else:
            df2 = df.loc[(df['q_num'] == 8) & (df["answer"] == res2[i])]
        result= pd.concat([result, df2])


#### write the table if no error
try:
    result.reset_index(drop=True, inplace=True)
    result.index+=1
    # st.table(result)
    st.dataframe(result)
except:
    pass

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