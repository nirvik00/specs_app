import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Question 4"
)

st.write("Are there multiple stories?")

opts = ["Yes - 1", "Yes - 2",  "No"]
captions = ["NewBuilding, Addition, Addition//Renovation", "Renovation", "Does not have multiple stories"]
q4 = st.radio(
    "Select one",
    opts,
    captions = captions
)

index = opts.index(q4)
st.write(f"You selected: {captions[index]}")
if q4 == "Yes - 1":
    df = pd.read_csv("output.csv")
    df2 = df.loc[(df["q_num"] == 4) & (df["answer"]=="Yes_NewBuilding_Addition_Addition/Renovation")]
    df2['answer'] = "Yes"
    df2.reset_index(drop=True, inplace=True)
    df2.index +=1
    # st.table(styled_df)
    st.table(df2)

elif q4 == "Yes - 2":
    df = pd.read_csv("output.csv")
    df2 = df.loc[(df["q_num"] == 4) & (df["answer"]=="Yes_Renovation")]
    df2['answer'] = "Yes"
    df2.reset_index(drop=True, inplace=True)
    df2.index +=1
    # st.table(styled_df)
    st.table(df2)
