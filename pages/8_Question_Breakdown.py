import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# OUTPUT_FILE = "output_updated.csv"
OUTPUT_FILE = "output_updated_separation.csv"

#### get data for table
df = pd.read_csv(OUTPUT_FILE)

###############################################################
#### every project
####
st.write('Sections included in every project are:')
df = pd.read_csv(OUTPUT_FILE)
df2 = df.loc[(df['q_num'] == 0) & (df['answer'] == 'Every_Project')]
df2 = df2.sort_values(by='sec_num')
df2.reset_index(drop=True, inplace=True)
# df2.index += 1
st.dataframe(df2)#### output table


###############################################################
#### q1
####
st.write("Question 1. What type of project is this?")
st.write(f"Answer. {st.session_state.q1_state}")
q1_res = st.session_state.q1_state.strip().replace(" ", "").replace("/","_")
df_q1 = df.loc[(df['q_num'] == 1) & (df['answer'] == q1_res)]
df_q1 = df_q1.sort_values(by="sec_num")
df_q1.reset_index(drop=True, inplace=True)
# df_q1.index += 1
st.dataframe(df_q1)####       output table

# q2 does not matter
###############################################################
#### q2 :- get data for table
####
st.divider()
st.write("Question 2. Does the project require demolition?")
st.write(f"Answer. {st.session_state.q2_state}")
q2_res = st.session_state.q2_state.strip().replace(" ", "").replace("/","_")
if q2_res == "Yes":
    df_q2 = df.loc[df['q_num'] == 2]
    df_q2 = df_q2.sort_values(by="sec_num")
    df_q2.reset_index(drop=True, inplace=True)
    # df_q2.index += 1
    st.dataframe(df_q2)####       output table

###############################################################
#### q3:- get data for table
####
st.divider()
st.write("Question 3. Are there multiple stories?")
q3_res = st.session_state.q3_state
if q3_res == "Yes"  and (st.session_state.q1_state=='NewBuilding' or st.session_state.q1_state=='Addition_Renovation'):
    st.write(f"Answer. Yes_NewBuilding_Addition_Addition_Renovation")
    df_q3 = df.loc[(df["q_num"] == 3) & (df["answer"]=="Yes_NewBuilding_Addition_Addition_Renovation")]
    df_q3 = df_q3.sort_values(by='sec_num')
    df_q3.reset_index(drop=True, inplace=True)
    # df_q3.index += 1
    st.dataframe(df_q3)####       output interactive table
elif q3_res== "Yes" and st.session_state.q1_state=='Renovation':
    st.write(f"Answer. Yes_Renovation")
    df_q3 = df.loc[(df["q_num"] == 3) & (df["answer"]=="Yes_Renovation")]
    df_q3 = df_q3.sort_values(by="sec_num")
    df_q3.reset_index(drop=True, inplace=True)
    # df_q3.index +=1
    st.dataframe(df_q3)####     output interactive table
else:
    st.write(f"Answer. No")

###############################################################
#### q4 :- get data for table
####
st.divider()
st.write("Question 4. What are the opaque Exterior materials?")
st.write(f"Answer. {st.session_state.q4_state}")
q4_res = st.session_state.q4_state
result_q4 = None
for i, e in enumerate(q4_res.split(", ")):
    X = e.replace(" ", "").replace("/","_")
    df_q4 = df.loc[(df['q_num']==4) & (df['answer']==X)]
    result_q4 = pd.concat([result_q4, df_q4])
    result_q4 = result_q4.drop_duplicates(subset=["sec_num"], keep="first")
try:
    result_q4 = result_q4.sort_values(by="sec_num")
    result_q4.reset_index(drop=True, inplace=True)
    # result_q4.index += 1
    # st.table(result_q4)#### output table
    st.dataframe(result_q4)#### output table
except:
    st.write("error getting results for Q5.")

###############################################################
#### q5 :- get data for table 
####
st.divider()
df = pd.read_csv(OUTPUT_FILE)
st.write("Question 5. Is the backup for exterior walls CMU?")
st.write(f"Answer. {st.session_state.q5_state}")
q5_res = st.session_state.q5_state
df_q5 = None
if q5_res == "Yes":
    df_q5= df.loc[(df['q_num'] == 5) & (df['answer'] == 'CMU')]
    if len(df_q5) > 1:
        df_q5 = df_q5.sort_values(by='sec_num')
        df_q5 = df_q5.reset_index(drop=True, inplace=True)
        # df_q5.index += 1
    elif len(df_q5) == 1:
        sec_num = df_q5['sec_num'].values.tolist()[0]
        sec_name = df_q5['sec_name'].values.tolist()[0]
        q_num = df_q5['q_num'].values.tolist()[0]
        ans = df_q5['answer'].values.tolist()[0]
        df_q5 = pd.DataFrame({'q_num': [q_num], 'answer': [ans], 'sec_num': [sec_num], 'sec_name': [sec_name]})
    st.dataframe(df_q5)

###############################################################
#### q6 :- get data for table 
####
st.divider()
df = pd.read_csv(OUTPUT_FILE)
st.write("Question 6. What are the anticipated floor finishes?")
st.write(f"Answer. {st.session_state.q6_state}")
result_q6 = None
q6_res = st.session_state.q6_state
for i, e in enumerate(q6_res.split(", ")):
    X = e.strip().replace(" ", "")
    df_q6 = df.loc[(df['q_num'] == 6) & (df["answer"] == X)]
    result_q6= pd.concat([result_q6, df_q6])
    result_q6 = result_q6.drop_duplicates(subset=["sec_num"], keep="first")
try:
    result_q6 = result_q6.sort_values(by='sec_num')
    result_q6.reset_index(drop=True, inplace=True)
    # result_q6.index+=1
    # st.table(result_q6)
    st.dataframe(result_q6)####       output table
except:
    pass
 
###############################################################
#### q7 :- get data for table 
####
st.divider()
st.write("Question 7. What are the special ceiling materials?")
st.write(f"Answer. {st.session_state.q7_state}")
result_q7 = None
q7_res = st.session_state.q7_state
for i, e in enumerate(q7_res.split(", ")):
    X = e.strip().replace(" ", "").replace("/","_")
    df2 = df.loc[(df['q_num'] == 7) & (df["answer"] == X)]
    result_q7= pd.concat([result_q7, df2])
    result_q7 = result_q7.drop_duplicates(subset=["sec_num"], keep="first")
try:
    result_q7 = result_q7.sort_values(by='sec_num')
    result_q7.reset_index(drop=True, inplace=True)
    # result_q7.index+=1
    st.dataframe(result_q7)####       output table
except:
    st.write("error retrieving results for Q.7")

 
###############################################################
#### sections in every project
####


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

