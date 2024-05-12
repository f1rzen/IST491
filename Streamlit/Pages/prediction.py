from git import UnsafeOptionError
import streamlit as st

def show_prediction_page(df, model):
    
    with open('./PredictionPage/col1_page.html', 'r', encoding='utf-8') as f:
        page = f.read()
        f.close()
    
    col1, col2 = st.columns((1,2))

    with col1:
        container = st.container()
        
        container.markdown(
            f"""
            {page}
            """,
            unsafe_allow_html=True
        )
    
    with open('./PredictionPage/col2_page.html', 'r', encoding='utf-8') as f:
        page = f.read()
        f.close()

    with col2:
        container = st.container()
        
        container.markdown(
            f"""
            {page}
            """,
            unsafe_allow_html=True
        )
        
        with open('./PredictionPage/metric_cards.html', 'r', encoding='utf-8') as f:
            page = f.read()
            f.close()
        
        container = st.container()
        
        container.markdown(
            f"""
            {page}
            """,
            unsafe_allow_html=True
        )