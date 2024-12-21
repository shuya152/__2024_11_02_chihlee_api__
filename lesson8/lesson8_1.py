import streamlit as st

# 手動建立counter_key, 並設定初始值為0
if "counter" not in st.session_state:
    # st.session_state['counter'] = 0
    st.session_state.counter = 0

# st.session_state.counter += 1

st.header(f"這個網頁已經執行{st.session_state.counter}次")
button_status = st.button("再執行一次", key="reset") #自動建立reset_key
# st.write(st.session_state)
if button_status:
    st.session_state.counter += 1