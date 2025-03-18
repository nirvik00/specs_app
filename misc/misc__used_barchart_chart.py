import streamlit as st
import plotly.express as px
import pandas as pd
import json


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
