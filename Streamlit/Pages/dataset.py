# Web application
import streamlit as st
def show_data_page():
    html_path="./DataPage/index.html"
    def get_data_page(html_path):
        
        with open(html_path, 'r', encoding='utf-8') as f:
            data_page = f.read()

        return data_page
    data_page= get_data_page(html_path)
    st.markdown(
        f"""
        {data_page}
        """,
        unsafe_allow_html=True, 
    )
