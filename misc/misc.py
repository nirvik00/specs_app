import streamlit as st
import plotly.express as px
import pandas as pd


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
    sec_obj_li = inp_sec_obj_li[:10]
    for e in sec_obj_li:
        div = e.sec_num.split(" ")[0]
        if div not in div_li:
            div_li.append(div)
    return div_li

def get_div(inp_sec_obj_li):
    div_li=[]
    unique_div_li = get_unique_divs(inp_sec_obj_li)

    sec_li=[]
    sec_obj_li = inp_sec_obj_li[:]
    for div in unique_div_li:
        sec_li.append(div)
        div_li.append("Root")
        for e in sec_obj_li:
            if e.sec_num.split(" ")[0] == div:
                div_li.append(div)
                sec_li.append(e.sec_num)

    return div_li, sec_li

def driver():
    sec_obj_li = get_sec_objs()
    (div_li, sec_li) = get_div(sec_obj_li)    
    return div_li, sec_li



(DIV_LI, SEC_LI) = driver()

data = pd.DataFrame(dict(
    sec_li=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    div_li=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
    # sec_li = SEC_LI,
    # div_li = DIV_LI,
))

fig = px.sunburst(
    data,
    names='sec_li',
    parents='div_li',
)

# Plot!
st.plotly_chart(fig)

div = ", ".join(DIV_LI)
sec = ", ".join(SEC_LI)
st.write(f"num divs {len(DIV_LI)}")
st.write(f"num sections {len(SEC_LI)}")
st.write(f"divs = {div}")
st.write(f"sections = {sec}")