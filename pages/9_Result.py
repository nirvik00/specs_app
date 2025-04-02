import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


####
# OUTPUT_FILE = "output_updated.csv"
OUTPUT_FILE = "output_updated_separation.csv"

#### get data for table
df = pd.read_csv(OUTPUT_FILE)
RESULT_ALL = None


###############################################################
#### every project
####
df = pd.read_csv(OUTPUT_FILE)
df_q0 = df.loc[(df['q_num'] == 0) & (df['answer'] == 'Every_Project')]
# df_q0 = df_q0.sort_values(by='sec_num')
# df_q0.reset_index(drop=True, inplace=True)
# df_q0.index += 1
RESULT_ALL = pd.concat([RESULT_ALL, df_q0])

###############################################################
#### q1
####
df = pd.read_csv(OUTPUT_FILE)
q1_res = st.session_state.q1_state.strip().replace(" ", "").replace("/","_")
df_q1 = df.loc[(df['q_num'] == 1) & (df['answer'] == q1_res)]
# df_q1.reset_index(drop=True, inplace=True)
# df_q1.index += 1
RESULT_ALL = pd.concat([RESULT_ALL, df_q1])

###############################################################
# q2 does not matter
#### q2 :- get data for table
q2_res = st.session_state.q2_state.strip().replace(" ", "").replace("/","_")
if q2_res == "Yes":
    df_q2 = df.loc[df['q_num'] == 2]
    # df_q2.reset_index(drop=True, inplace=True)
    # df_q2.index += 1
    RESULT_ALL = pd.concat([RESULT_ALL, df_q2])

###############################################################
#### q3 :- get data for table
#### 
q3_res = st.session_state.q3_state
df = pd.read_csv(OUTPUT_FILE)
if q3_res == "Yes"  and (st.session_state.q1_state=='NewBuilding' or st.session_state.q1_state=='Addition_Renovation'):
    df_q3 = df.loc[(df["q_num"] == 3) & (df["answer"]=="Yes_NewBuilding_Addition_Addition_Renovation")]
    # df_q3 = df_q3.sort_values(by='sec_num')
    # df_q3.reset_index(drop=True, inplace=True)
    # df_q3.index += 1
    RESULT_ALL = pd.concat([RESULT_ALL, df_q3])
elif q3_res== "Yes" and st.session_state.q1_state=='Renovation':
    df_q3 = df.loc[(df["q_num"] == 3) & (df["answer"]=="Yes_Renovation")]
    # df_q3 = df_q3.sort_values(by="sec_num")
    # df_q3.reset_index(drop=True, inplace=True)
    # df_q3.index +=1
    RESULT_ALL = pd.concat([RESULT_ALL, df_q3])
else:
    pass

###############################################################
#### q4 :- get data for table
####
q4_res = st.session_state.q4_state
result_q4 = None
df = pd.read_csv(OUTPUT_FILE)
for i, e in enumerate(q4_res.split(", ")):
    X = e.replace(" ", "").replace("/","_")
    df_q4 = df.loc[(df['q_num']==4) & (df['answer']==X)]
    RESULT_ALL = pd.concat([RESULT_ALL, df_q4])
try:
    # result_q4 = result_q4.sort_values(by="sec_num")
    # result_q4.reset_index(drop=True, inplace=True)
    # result_q4.index += 1
    RESULT_ALL = pd.concat([RESULT_ALL, df_q4])
except:
    pass

###############################################################
#### q5 :- get data for table 
####
df = pd.read_csv(OUTPUT_FILE)
q5_res = st.session_state.q5_state
if q5_res == "CMU":
    df_q5= df.loc[(df['q_num'] == 5) & (df['answer'] == "CMU")]
    RESULT_ALL = pd.concat([RESULT_ALL, df_q5])

###############################################################
#### q6 :- get data for table 
####
result_q6 = None
df = pd.read_csv(OUTPUT_FILE)
q6_res = st.session_state.q6_state
for i, e in enumerate(q6_res.split(", ")):
    X = e.strip().replace(" ", "")
    df_q6 = df.loc[(df['q_num'] == 6) & (df["answer"] == X)]
    RESULT_ALL = pd.concat([RESULT_ALL, df_q6])
try:
    result_q6.reset_index(drop=True, inplace=True)
    result_q6.index+=1
    RESULT_ALL = pd.concat([RESULT_ALL, df_q6])
except:
    pass
 
###############################################################
#### q7 :- get data for table 
####

df = pd.read_csv(OUTPUT_FILE)
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
    result_q7.index+=1
    RESULT_ALL = pd.concat([RESULT_ALL, result_q7])
except:
    pass





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
    print(sec_num_li)
    for sec_num in sec_num_li:
        df = get_row_from_sec_num(sec_num, df_res, df_inp)
        all_result_df= pd.concat([all_result_df, df])
    return all_result_df

all_result_df  = add_connected_sections(RESULT_ALL)
all_result_df = all_result_df.drop_duplicates(subset=['sec_num'], keep='first')

RESULT_ALL = pd.concat([RESULT_ALL, all_result_df])

###############################################################
####
####        process data 
####


RESULT_ALL = RESULT_ALL.drop_duplicates(subset=["sec_num"], keep="first")
RESULT_ALL.reset_index(drop=True, inplace=True)

st.session_state['result_sec_nums'] = RESULT_ALL['sec_num']
st.session_state['result_sec_names'] = RESULT_ALL['sec_name']

res_df = RESULT_ALL[['sec_num', 'sec_name']]
res_df = res_df.sort_values(by='sec_num')
res_df.reset_index(drop=True, inplace=True)

st.session_state['result_sec_nums'] = res_df['sec_num'].tolist()
st.session_state['result_sec_names'] =  res_df['sec_name'].tolist()

#########################################################################
#
#                       plot barchart
#
#########################################################################
def plot_bar():
    sec_nums = st.session_state['result_sec_nums'] 
    sec_names = st.session_state['result_sec_names']

    # print(sec_nums)

    unique_divs=[]
    for sec_num in sec_nums:
        s = sec_num.split(' ')[0]
        if s not in unique_divs:
            unique_divs.append(s)

    sec_count_in_div=[]
    for e in unique_divs:
        count=0
        for i, sec in enumerate(sec_nums):
            div = sec.split(" ")[0]
            if div== e:
                count+=1
        sec_count_in_div.append(count)


    df = pd.DataFrame({'div_num': unique_divs, 'num_sec_in_div': sec_count_in_div})
    return df

df = plot_bar()
fig = px.bar(df, x="div_num", y="num_sec_in_div", color="num_sec_in_div", title="section/division break-down in each question")

# fig.show()
st.plotly_chart(fig, theme="streamlit")

st.write("viz 1, 2, 3 = work in progress...")

#########################################################################
#
#                       write table
#
#########################################################################

st.dataframe(res_df)

