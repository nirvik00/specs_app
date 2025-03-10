import streamlit as st


st.set_page_config(
    page_title="Specs App"
)

#
st.title("Specs Form")

data={}
with st.form("key=specs_form"):
    name=st.text_input("enter project name")
    num=st.text_input("enter project number")
    data["name"] = name
    data["vision num"] = num
    st.form_submit_button()

with st.sidebar:
    st.header("Specs Result")
    for k, v in data.items():
        st.write(f"{k}:  {v}")
    