import streamlit as st
st.title('Counter Example')
count=0
increament=st.button('Increment')
if increament:
    count+=1
st.write('count=',count)