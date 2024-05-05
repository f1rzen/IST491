import streamlit as st

def show_contact_page():
    
    html_path = '../Streamlit/ContactPage/index.html'
    css_path = '../Streamlit/ContactPage/style.css'
    
    def get_contact_page(css_path, html_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            contact_page_css = f.read()
        
        with open(html_path, 'r', encoding='utf-8') as f:
            contact_page = f.read()

        return contact_page_css, contact_page

    contact_page, contact_css_file = get_contact_page(html_path, css_path)

    st.markdown(
        f"""
        <style>
            {contact_css_file}
        </style>
        {contact_page}
        """,
        unsafe_allow_html=True
    )