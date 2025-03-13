import streamlit as st
import plotly.figure_factory as ff
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

def get_div_1(sec_li):
    li = '01 02 03 04 05 06 07 08 09 10 11 12 13 14 31 32 33 34'.split(' ')
    all_div_li=[]
    for div_num in li:
        div_li=[]
        for e in sec_li:
            if e.div_num == div_num:
                if e.sec_num not in div_li: #### there are many duplicates for each section
                    div_li.append(e.sec_num)
        #div_dict={div_num_: div_li}
        # all_div_li.append(div_dict)
        all_div_li.append(div_li)
    return all_div_li

def get_div_2(sec_obj_li):
    div_li=[""]
    sec_li=[]
    for e in sec_obj_li:
        div = e.sec_num.split(" ")[0]
        div_li.append(div)
        sec_li.append(e.sec_num)
    return div_li, sec_li

def driver():
    sec_obj_li = get_sec_objs()
    # ALL_DIV_LI = get_div_1(sec_obj_li)
    # DIV_LI = '"" 01 02 03 04 05 06 07 08 09 10 11 12 13 14 31 32 33 34'.split(' ')
    # return DIV_LI, ALL_DIV_LI
    (div_li, sec_li) = get_div_2(sec_obj_li)
    x = "Root"*len(div_li) 
    return div_li, sec_li

st.set_page_config(
    page_title="Specs App"
)

(DIV_LI, SEC_LI) =driver()
# print(SEC_LI)
data = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    # character=SEC_LI,
    # parent=DIV_LI,
    # character=["1", "2", "3", "3"],
    # parent=["", "1", "1", "2"],
    # value=[10, 10, 10, 10, 10, 10, 10, 10,10]
    )

fig = px.sunburst(
    data,
    names='character',
    parents='parent',
)

# Plot!
st.plotly_chart(fig)


#
st.title("Specs Form")

if 'proj_name_state' not in st.session_state:
    st.session_state['proj_name_state'] = "no name"
if 'proj_num_state' not in st.session_state:
    st.session_state['proj_num_state'] = "no num"
if 'q1_state' not in st.session_state:
    st.session_state['q1_state'] = "New Building"
if 'q2_state' not in st.session_state:
    st.session_state['q2_state'] = "General"
if 'q3_state' not in st.session_state:
    st.session_state['q3_state'] = "Yes"
if 'q4_state' not in st.session_state:
    st.session_state['q4_state'] = "Yes-1"
if 'q5_state' not in st.session_state:
    st.session_state['q5_state'] = "[]"
if 'q6_state' not in st.session_state:
    st.session_state['q6_state'] = "Cold-Formed metal framing"
if 'q7_state' not in st.session_state:
    st.session_state['q7_state'] = "[]"
if 'q8_state' not in st.session_state:
    st.session_state['q8_state'] = "[]"

my_name=st.text_input("enter project name", st.session_state['proj_name_state'])
my_num=st.text_input("enter project number", st.session_state['proj_num_state'])
submit = st.button("Submit")
if submit:
    st.session_state['proj_name_state']= my_name
    st.session_state['proj_num_state']= my_num


with st.sidebar:
    st.write(f"project name is {st.session_state.proj_name_state}")
    st.write(f"project number is {st.session_state.proj_num_state}")
    st.write(f"q1 - Project type is set to {st.session_state.q1_state}")
    st.write(f"q2 - Typology is set to {st.session_state.q2_state}")
    st.write(f"q3 - Demolition is set to {st.session_state.q3_state}")
    st.write(f"q4 - Mulitple stories is set to {st.session_state.q4_state}")
    st.write(f"q5 - Exterior opaque Materials is set to {st.session_state.q5_state}")
    st.write(f"q6 - Backup for q5 is set to {st.session_state.q6_state}")
    st.write(f"q7 - Anticipated floor finishes {st.session_state.q7_state}")
    st.write(f"q8 - Ceiling materials is set to {st.session_state.q8_state}")

# streamlit run specs_app.py