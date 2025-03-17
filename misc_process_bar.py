import streamlit as st
import plotly.express as px
import pandas as pd

class section:
    def __init__(self, q_num, ans, sec_num, sec_name):
        self.q_num = "q-" + str(q_num)
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

class QObj:
    def __init__(self, q, div_li, num_sec):
        self.q_num = q # int : question_num 
        self.div_in_q= div_li # list : divisions in each question
        self.sec_count_in_each_div = num_sec # list : num of sections in each div
    def __str__(self):
        s = str(self.q_num)
        s += ", ".join(self.div_li)
        str_sec_num_li = [str(sec) for sec in self.sec_count_in_each_div]
        s += str_sec_num_li
        return s

def generate_dataframe(q_obj_li):
    q_num=[]
    div_num =[]
    sec_count_in_div=[]
    for q in q_obj_li:
        num_divs = len(q.div_in_q)
        q_num += [q.q_num] * num_divs
        div_num += q.div_in_q
        sec_count_in_div += q.sec_count_in_each_div
    data = {"q_num": q_num, "num_sec_in_div": div_num, "sec_count_in_div": sec_count_in_div}
    df = pd.DataFrame(data)
    return df        

def generate_q_obj(unique_q_li, unique_div_li, sec_obj_li):
    q_li =[] 
    div_li =[] 
    sec_count_in_div_li=[]
    q_obj_li=[]
    for q in unique_q_li:
        div2_li =[]
        sec2_li=[]
        for div in unique_div_li:
            sec_count = 0
            for sec in sec_obj_li:
                if sec.div_num == div and sec.q_num == q:
                    sec_count+=1
            div2_li.append(div)
            sec2_li.append(sec_count)
        div_num = len(div2_li)
        q_li += ["q-"+str(q)] * div_num
        div_li += div2_li
        sec_count_in_div_li += sec2_li
        
        q = QObj(q, div_li, sec_count_in_div_li)
        q_obj_li.append(q)
    return q_obj_li, q_li, div_li, sec_count_in_div_li

def get_sec_objs():
    with open("output.csv", "r") as f:
        data = f.readlines()
    unique_q_li = []
    unique_div_li = []
    sec_obj_li=[]
    for i, e in enumerate(data):
        if i==0:
            continue
        x = e.split(",")
        q_num = x[0]
        if q_num not in unique_q_li:
            unique_q_li.append(q_num)
        ans = x[1]
        sec_num = x[2]
        div = sec_num.split(" ")[0]
        if div not in unique_div_li:
            unique_div_li.append(div)
        sec_name = x[3]
        sec = section(q_num, ans, sec_num, sec_name)
        sec_obj_li.append(sec)
    return unique_q_li, unique_div_li, sec_obj_li
    
def driver():
    (unique_q_li, unique_div_li, sec_obj_li) = get_sec_objs()
    (q_obj_li, q_li, div_li, sec_count_in_div_li) = generate_q_obj(unique_q_li, unique_div_li, sec_obj_li)
    # df = generate_dataframe(q_obj_li)
    data = {"q_num": q_li, "num_sec_in_div": div_li, "sec_count_in_div": sec_count_in_div_li}
    df = pd.DataFrame(data)
    return df


df= driver()

fig = px.bar(df, x="q_num", y="num_sec_in_div", color="sec_count_in_div", title="section/division break-down in each question")

fig.show()