# 執行
# https://docs.streamlit.io/get-started/fundamentals/main-concepts

import streamlit as st
import tools

sitenames:list[str] = tools.get_sitenames(excel_name='aqi.xlsx')
# https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox
# add_selectbox = st.sidebar.selectbox('請點選戰點名稱:',sitenames)
with st.sidebar:
    add_selectbox = st.selectbox('請點選戰點名稱:',sitenames)

    # https://docs.streamlit.io/develop/api-reference/text/st.title
    st.title(f"{add_selectbox}")


allData:list[dict] = tools.get_aqi(excel_name='aqi.xlsx')

# selected_item:list[dict] = []
# for item in allData:
#     if item['sitename'] == add_selectbox:
#         selected_item.append(item)

selected_item:list[dict] = [ item for item in allData if item['sitename'] == add_selectbox ]
st.table(data=selected_item)