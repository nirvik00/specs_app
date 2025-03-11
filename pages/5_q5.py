import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Question 5"
)

st.write("What are the opaque Exterior materials? (select all that apply)")

res = ["Masonry", "Stone", "Metal Panel", "Fiber Cement Panel", "Terra Cotta", "Phenolic Panel", "EIFS", "Precast Concrete", "Cast Stone", "Architectural Concrete"]
res2 =[]
for e in res:
    r = e.strip().replace(" ", "")
    res2.append(r)
st.write(", ".join(res2))
q5=[]
for e in res:
    x =st.checkbox(e)
    q5.append(x)


df = pd.read_csv("output.csv")
result= None
s=""
for i, e in enumerate(q5):
    if e == True:
        s += str(i) + ":" + str(e)+ ", "
        df2 = df.loc[(df['q_num']==5) & (df['answer']==res2[i])]
        result = pd.concat([result, df2])

st.write(s)

result.reset_index(drop=True, inplace=True)
result.index += 1
st.table(result)