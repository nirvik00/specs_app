import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


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

####

#### get data for table
df = pd.read_csv("output.csv")
RESULT_ALL = None

#### q1
q1_res = st.session_state.q1_state.strip().replace(" ", "").replace("/","_")
df_q1 = df.loc[(df['q_num'] == 1) & (df['answer'] == q1_res)]
df_q1.reset_index(drop=True, inplace=True)
df_q1.index += 1
# st.table(df_q1)
# st.dataframe(df_q1)####       output table
RESULT_ALL = pd.concat([RESULT_ALL, df_q1])

# q2 does not matter

#### q3 :- get data for table
q3_res = st.session_state.q3_state.strip().replace(" ", "").replace("/","_")
if q3_res == "Yes":
    df_q3 = df.loc[df['q_num'] == 3]
    df_q3.reset_index(drop=True, inplace=True)
    df_q3.index += 1
    # st.table(df_q3)
    #st.dataframe(df_q3)####       output table
    RESULT_ALL = pd.concat([RESULT_ALL, df_q3])

#### q4 :- get data for table
q4_res = st.session_state.q4_state
if q4_res == "Yes - 1":
    df_q4 = df.loc[(df["q_num"] == 4) & (df["answer"]=="Yes_NewBuilding_Addition_Addition/Renovation")]
    df_q4.reset_index(drop=True, inplace=True)
    df_q4.index += 1
    # st.table(df_q3)
    # st.dataframe(df_q4)####       output interactive table
    RESULT_ALL = pd.concat([RESULT_ALL, df_q4])
elif q4_res == "Yes - 2":
    df_q4 = df.loc[(df["q_num"] == 4) & (df["answer"]=="Yes_Renovation")]
    df_q4.reset_index(drop=True, inplace=True)
    df_q4.index +=1
    # st.table(df2)#### output table
    # st.dataframe(df_q4)####     output interactive table
    RESULT_ALL = pd.concat([RESULT_ALL, df_q4])

#### q5 :- get data for table
q5_res = st.session_state.q5_state
result_q5 = None
for i, e in enumerate(q5_res.split(", ")):
    X = e.replace(" ", "").replace("/","_")
    df_q5 = df.loc[(df['q_num']==5) & (df['answer']==X)]
    # result_q5 = pd.concat([result_q5, df_q5])
    RESULT_ALL = pd.concat([RESULT_ALL, df_q5])
try:
    result_q5.reset_index(drop=True, inplace=True)
    result_q5.index += 1
    # st.table(result_q5)#### output table
    # st.dataframe(result_q5)#### output table
    RESULT_ALL = pd.concat([RESULT_ALL, df_q5])
except:
    pass

#### q6 :- get data for table 
q6_res = st.session_state.q6_state
if q6_res == "Cold-Formed Metal Framing":
    df_q6= df.loc[(df['q_num'] == 6) & (df['answer'] == "ColdFormedMetalFraming")]
else:
    df_q6= df.loc[(df['q_num'] == 6) & (df['answer'] == "CMU")]
# st.dataframe(df_q6)
RESULT_ALL = pd.concat([RESULT_ALL, df_q6])

#### q7 :- get data for table 
result_q7 = None
q7_res = st.session_state.q7_state
for i, e in enumerate(q7_res.split(", ")):
    X = e.strip().replace(" ", "")
    df_q7 = df.loc[(df['q_num'] == 7) & (df["answer"] == X)]
    # result_q7= pd.concat([result_q7, df_q7])
    RESULT_ALL = pd.concat([RESULT_ALL, df_q7])
try:
    result_q7.reset_index(drop=True, inplace=True)
    result_q7.index+=1
    # st.table(result_q7)
    # st.dataframe(result_q7)####       output table
    RESULT_ALL = pd.concat([RESULT_ALL, df_q7])
except:
    pass
 

#### q8 :- get data for table 
result_q8 = None
q8_res = st.session_state.q8_state
for i, e in enumerate(q8_res.split(", ")):
    X = e.replace(" ", "")
    if i == 1:
        df2 = df.loc[(df['q_num'] == 8) & (df["answer"] == "AcousticalBaffles")]
    else:
        X = e.replace(" ", "").replace("/","_")
        df2 = df.loc[(df['q_num'] == 8) & (df["answer"] == X)]
    result_q8= pd.concat([result_q8, df2])
try:
    # result_q8.reset_index(drop=True, inplace=True)
    # result_q8.index+=1
    # st.table(result_q7)
    # st.dataframe(result_q8)####       output table
    RESULT_ALL = pd.concat([RESULT_ALL, result_q8])
except:
    pass


RESULT_ALL = RESULT_ALL.drop_duplicates(subset=["sec_num"], keep="first")
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

#########################################################################
#
#                       write table
#
#########################################################################

st.dataframe(res_df)

#########################################################################
#
#                       sunburst plot
#
#########################################################################

def plot_sunburst():
    sec_nums = st.session_state['result_sec_nums'] 
    sec_names = st.session_state['result_sec_names']
    unique_div_nums = []
    for e in sec_nums:
        f = e.split(" ")[0]
        if f not in unique_div_nums:
            unique_div_nums.append(f)

    #
    parents = [" "]
    child=["root"]
    count_li=[]
    values=[1]
    for e in unique_div_nums:
        parents.append('root')
        child.append(e)
        values.append(1)
        count=0
        for sec in sec_nums:
            if sec.split(" ")[0] == e:
                count+=1
        count_li.append(count)

    #
    for e in sec_nums:
        f = e.split(" ")[0]
        if f in unique_div_nums:
            parents.append(f)
            child.append(e)
            x = unique_div_nums.index(f)
            values.append(count_li[x])
    #
    return parents, child, values

(parents, child, values) = plot_sunburst()

# df = pd.DataFrame({'child':child, 'parents':parents, 'values': values})
# fig = px.sunburst(df, names = 'child', parents = 'parents', values='values')

data = dict( child=child, parents=parents)
fig = px.sunburst(data, names = 'child', parents = 'parents')

# Plot!
st.plotly_chart(fig, theme='streamlit')