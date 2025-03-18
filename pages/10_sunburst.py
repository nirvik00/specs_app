import streamlit as st
import plotly.express as px
import pandas as pd
import json


def plot_sunburst():
    sec_nums = st.session_state['result_sec_nums'] 
    sec_names = st.session_state['result_sec_names']
    unique_div_nums = []
    for e in sec_nums:
        f = e.split(" ")[0]
        if f not in unique_div_nums:
            unique_div_nums.append(f)
    parents = [" "]
    child=["root"]
    #
    for e in unique_div_nums:
        parents.append('root')
        child.append(e)
    #
    for e in sec_nums:
        f = e.split(" ")[0]
        if f in unique_div_nums:
            parents.append(f)
            child.append(e)
    #
    return parents, child

(parents, child) = plot_sunburst()

data = dict( child=child, parents=parents)
fig = px.sunburst(data, names = 'child', parents = 'parents')

# Plot!
st.plotly_chart(fig, theme="streamlit")