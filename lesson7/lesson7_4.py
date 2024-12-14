import streamlit as st
st.title('Counter Example')
if'count'not in st.session_state:
    st.session_state['count']=0
increament=st.button('Increment')
if increament:
    st.session_state['count']+=1
st.write('count=',st.session_state['count'])