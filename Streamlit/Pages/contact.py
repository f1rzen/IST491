import streamlit as st

def show_contact_page():
    
    html_path = './ContactPage/index.html'
    
    def get_contact_page(html_path):
        
        with open(html_path, 'r', encoding='utf-8') as f:
            contact_page = f.read()

        return contact_page

    contact_page= get_contact_page(html_path)
    st.markdown(
        f"""
        ## Contact us

        Contact us for your questions.
        {contact_page}
        """,
        unsafe_allow_html=True
    )
