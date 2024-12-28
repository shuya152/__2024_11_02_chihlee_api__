from tools import taipei
import streamlit as st
@st.dialog("網路出現問題")
def vote(erroe):
    st.write(f"{erroe}")
try:
    youbike_data:list[dict]=taipei.get_youbikes()
except Exception as erroe:
    vote(erroe)
    st.write("喝杯咖啡，稍後再試！")
    st.stop()
st.table(youbike_data)