import streamlit as st
def show_home_page():
    html_path="./HomePage/index.html"
    def get_home_page(html_path):
        
        with open(html_path, 'r', encoding='utf-8') as f:
            home_page = f.read()

        return home_page
    home_page= get_home_page(html_path)
    st.markdown(
        f"""
        {home_page}
        """,
        unsafe_allow_html=True, 
    )



    
