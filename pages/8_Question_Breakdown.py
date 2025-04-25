import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from os.path import join

# OUTPUT_FILE = "output_updated.csv"
OUTPUT_FILE = "output_updated_separation.csv"


st.set_page_config(
    page_title="Results",
    initial_sidebar_state="expanded"
)

RESULT_ALL = None

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
st.dataframe(df2)#### output table

RESULT_ALL = pd.concat([RESULT_ALL, df2])

###############################################################
#### q1
####
st.write("Question 1. What type of project is this?")
st.write(f"Answer. {st.session_state.q1_state}")
q1_res = st.session_state.q1_state.strip().replace(" ", "").replace("/","_")
df_q1 = df.loc[(df['q_num'] == 1) & (df['answer'] == q1_res)]
df_q1 = df_q1.sort_values(by="sec_num")
df_q1.reset_index(drop=True, inplace=True)
st.dataframe(df_q1)####       output table

RESULT_ALL = pd.concat([RESULT_ALL, df_q1])

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
    st.dataframe(df_q2)####       output table
    RESULT_ALL = pd.concat([RESULT_ALL, df_q2])

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
    st.dataframe(df_q3)####       output interactive table
    RESULT_ALL = pd.concat([RESULT_ALL, df_q3])
elif q3_res== "Yes" and st.session_state.q1_state=='Renovation':
    st.write(f"Answer. Yes_Renovation")
    df_q3 = df.loc[(df["q_num"] == 3) & (df["answer"]=="Yes_Renovation")]
    df_q3 = df_q3.sort_values(by="sec_num")
    df_q3.reset_index(drop=True, inplace=True)
    st.dataframe(df_q3)####     output interactive table
    RESULT_ALL = pd.concat([RESULT_ALL, df_q3])
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
    st.dataframe(result_q4)#### output table
    RESULT_ALL = pd.concat([RESULT_ALL, result_q4])
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
    elif len(df_q5) == 1:
        sec_num = df_q5['sec_num'].values.tolist()[0]
        sec_name = df_q5['sec_name'].values.tolist()[0]
        q_num = df_q5['q_num'].values.tolist()[0]
        ans = df_q5['answer'].values.tolist()[0]
        df_q5 = pd.DataFrame({'q_num': [q_num], 'answer': [ans], 'sec_num': [sec_num], 'sec_name': [sec_name]})
    st.dataframe(df_q5)
    RESULT_ALL = pd.concat([RESULT_ALL, df_q5])
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
    st.dataframe(result_q6)####       output table
    RESULT_ALL = pd.concat([RESULT_ALL, df_q6])
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
    st.dataframe(result_q7)####       output table
    RESULT_ALL = pd.concat([RESULT_ALL, result_q7])
except:
    st.write("error retrieving results for Q.7")

RESULT_ALL = RESULT_ALL.sort_values(by='sec_num')
RESULT_ALL.reset_index(drop=True, inplace=True)

###############################################################
####
####                            get connected section numbers
####

def get_sec_name_for_sec_num(a, df_inp):
    x = df_inp.loc[(df_inp['Section Number'] == a)]
    y = x[['Section Number', 'Section Name']].values.tolist()[0]
    return y
    
def get_row_from_sec_num(a, df_res, df_inp):
    sec_num_li = []
    sec_name_li = []
    x = df_res.loc[(df_res['Section Number'] == a)]
    r = x.values.tolist()
    if not r:
        return 
    for e in r[0][2:]:
        try:
            (sec_num, sec_name) = get_sec_name_for_sec_num(e, df_inp)
            sec_num_li.append(sec_num)
            sec_name_li.append(sec_name)
        except:
            pass
    df = pd.DataFrame({'sec_num': sec_num_li, 'sec_name': sec_name_li})
    return df

def add_connected_sections(result_all):
    df_inp = pd.read_csv('mw_spec_toc_updated.csv')
    df_res = df_inp[['Section Number', 
             'Section Name', 
             'Other section that always accompanies this one (1)', 
             'Other section that always accompanies this one (2)', 
             'Other section that always accompanies this one (3)']]
    all_result_df = None
    sec_num_li = result_all['sec_num'].values.tolist()
    for sec_num in sec_num_li:
        df = get_row_from_sec_num(sec_num, df_res, df_inp)
        all_result_df= pd.concat([all_result_df, df])
    return all_result_df

st.divider()
st.write("Connected sections")

all_result_df  = add_connected_sections(RESULT_ALL)
all_result_df = all_result_df.drop_duplicates(subset=['sec_num'], keep='first')
all_result_df.reset_index(drop=True, inplace=True)
st.dataframe(all_result_df)

st.divider()
st.write("Goto results page")
submit = st.button("Submit")
if submit:
    st.switch_page(join('pages', '9_Result.py'))


###############################################################
####
####        sections in sidebar
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

