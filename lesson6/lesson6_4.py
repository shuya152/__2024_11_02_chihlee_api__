# 執行
# https://docs.streamlit.io/get-started/fundamentals/main-concepts

import streamlit as st
import tools

sitenames:list[str] = tools.get_sitenames(excel_name='aqi.xlsx')
# https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox
add_selectbox = st.sidebar.selectbox(
    '請點選戰點名稱:',
    sitenames
)