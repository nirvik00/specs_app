import streamlit as st
import pandas as pd
import numpy as np



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

####
st.write(f"project name is {st.session_state.proj_name_state}")
st.write(f"project name is {st.session_state.proj_num_state}")

#### get data for table
df = pd.read_csv("output.csv")

#### q1
st.write("question 1: ")
q1_res = st.session_state.q1_state.strip().replace(" ", "").replace("/","_")
df_q1 = df.loc[(df['q_num'] == 1) & (df['answer'] == q1_res)]
df_q1.reset_index(drop=True, inplace=True)
df_q1.index += 1
# st.table(df_q1)
st.dataframe(df_q1)####       output table

# q2 does not matter

#### q3 :- get data for table
st.write("question 3: ")
q3_res = st.session_state.q3_state.strip().replace(" ", "").replace("/","_")
if q3_res == "Yes":
    df_q3 = df.loc[df['q_num'] == 3]
    df_q3.reset_index(drop=True, inplace=True)
    df_q3.index += 1
    # st.table(df_q3)
    st.dataframe(df_q3)####       output table


#### q4 :- get data for table
st.write("question 4: ")
q4_res = st.session_state.q4_state
if q4_res == "Yes - 1":
    df_q4 = df.loc[(df["q_num"] == 4) & (df["answer"]=="Yes_NewBuilding_Addition_Addition/Renovation")]
    df_q4.reset_index(drop=True, inplace=True)
    df_q4.index += 1
    # st.table(df_q3)
    st.dataframe(df_q4)####       output interactive table
elif q4_res == "Yes - 2":
    df_q4 = df.loc[(df["q_num"] == 4) & (df["answer"]=="Yes_Renovation")]
    df_q4.reset_index(drop=True, inplace=True)
    df_q4.index +=1
    # st.table(df2)#### output table
    st.dataframe(df_q4)####     output interactive table


#### q5 :- get data for table
q5_res = st.session_state.q5_state
st.write(f"question 5: ", q5_res)
result_q5 = None
for i, e in enumerate(q5_res.split(", ")):
    X = e.replace(" ", "").replace("/","_")
    df_q5 = df.loc[(df['q_num']==5) & (df['answer']==X)]
    result_q5 = pd.concat([result_q5, df_q5])
try:
    result_q5.reset_index(drop=True, inplace=True)
    result_q5.index += 1
    # st.table(result_q5)#### output table
    st.dataframe(result_q5)#### output table
except:
    pass


#### q6 :- get data for table 
q6_res = st.session_state.q6_state
st.write(f"question 6: ", q6_res)
if q6_res == "Cold-Formed Metal Framing":
    df_q6= df.loc[(df['q_num'] == 6) & (df['answer'] == "ColdFormedMetalFraming")]
else:
    df_q6= df.loc[(df['q_num'] == 6) & (df['answer'] == "CMU")]
st.dataframe(df_q6)

#### q7 :- get data for table 
result_q7 = None
q7_res = st.session_state.q7_state
st.write(f"question 7: ", q7_res)
for i, e in enumerate(q7_res.split(", ")):
    X = e.strip().replace(" ", "")
    df_q7 = df.loc[(df['q_num'] == 7) & (df["answer"] == X)]
    result_q7= pd.concat([result_q7, df_q7])
try:
    result_q7.reset_index(drop=True, inplace=True)
    result_q7.index+=1
    # st.table(result_q7)
    st.dataframe(result_q7)####       output table
except:
    pass


#### q8 :- get data for table 
result_q8 = None
q8_res = st.session_state.q8_state
st.write(f"question 8: ", q8_res)
for i, e in enumerate(q8_res.split(", ")):
    X = e.replace(" ", "")
    if i == 1:
        df2 = df.loc[(df['q_num'] == 8) & (df["answer"] == "AcousticalBaffles")]
    else:
        X = e.replace(" ", "").replace("/","_")
        df2 = df.loc[(df['q_num'] == 8) & (df["answer"] == X)]
    result_q8= pd.concat([result_q8, df2])

try:
    result_q8.reset_index(drop=True, inplace=True)
    result_q8.index+=1
    # st.table(result_q7)
    st.dataframe(result_q8)####       output table
except:
    pass