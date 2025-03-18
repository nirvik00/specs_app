import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


#########################################################################
#
#                       sunburst plot
#
#########################################################################

def div_breakdown_sunburst():
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

(parents_div_breakdown, child, values) = div_breakdown_sunburst()

# df = pd.DataFrame({'child':child, 'parents_div_breakdown':parents_div_breakdown, 'values': values})
# fig = px.sunburst(df, names = 'child', parents_div_breakdown = 'parents_div_breakdown', values='values')

data_div_breakdown = dict( child=child, parents_div_breakdown=parents_div_breakdown)
fig_div_brakdown = px.sunburst(data_div_breakdown, names = 'child', parents_div_breakdown = 'parents')

# Plot!
st.write("\ndivision breakdown")
st.plotly_chart(fig_div_brakdown, theme='streamlit')