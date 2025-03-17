import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Chart"
)
st.write("tentative viz")

class section:
    def __init__(self, q_num, ans, sec_num, sec_name):
        self.q_num = q_num
        self.ans = ans
        self.sec_num = sec_num
        self.sec_name = sec_name
        self.div_num = '100'
        self.get_div_num()

    def get_div_num(self):
        self.div_num = self.sec_num.split(" ")[0]

    def __str__(self):
        s = f"{self.q_num},"
        s += f"{self.div_num},"
        s += f"{self.sec_num}"
        return s

def get_sec_objs():
    with open("output.csv", "r") as f:
        data = f.readlines()
    sec_li=[]
    for i, e in enumerate(data):
        if i==0:
            continue
        x = e.split(",")
        q_num = x[0]
        ans = x[1]
        sec_num = x[2]
        sec_name = x[3]
        sec = section(q_num, ans, sec_num, sec_name)
        sec_li.append(sec)
    return sec_li

def get_unique_divs(inp_sec_obj_li):
    div_li=[]
    sec_obj_li = inp_sec_obj_li[:]
    for e in sec_obj_li:
        div = e.sec_num.split(" ")[0]
        if div not in div_li:
            div_li.append(div)
    return div_li

def get_div(inp_sec_obj_li, num_of_points=20):
    div_li=[]
    unique_div_li = get_unique_divs(inp_sec_obj_li)
    unique_div_li.sort()
    print(unique_div_li)
    sec_li=[]
    sec_obj_li = inp_sec_obj_li[:num_of_points]

    for i, div in enumerate(unique_div_li):
        tmp_div_li=[]
        tmp_sec_li=[]
        count=0
        for e in sec_obj_li:
            if e.sec_num.split(" ")[0] == div:
                tmp_div_li.append(div)
                tmp_sec_li.append(e.sec_num)
                count+=1
        if count>0:
            sec_li.append(div)
            div_li.append("Root")
            sec_li+= tmp_sec_li
            div_li+= tmp_div_li


    return div_li, sec_li

def driver(sec_obj_li, num_of_points=20):
    (div_li, sec_li) = get_div(sec_obj_li, num_of_points)    
    return div_li, sec_li

###############################    functions
SEC_OBJ_LI = get_sec_objs()

##### interactive plotting
NUM_OF_DATA_POINTS = 20
values = st.slider("Select a range of values", 0, len(SEC_OBJ_LI), 10)
st.write("Values:", values)

###############################    functions
(DIV_LI, SEC_LI) = driver(SEC_OBJ_LI, int(values))

data = pd.DataFrame(dict(
    # sec_li=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    # div_li=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
    sec_li = SEC_LI,
    div_li = DIV_LI,
))

fig_sunburst = px.sunburst(
    data,
    names='sec_li',
    parents='div_li',
)

# Plot!
st.plotly_chart(fig_sunburst)
