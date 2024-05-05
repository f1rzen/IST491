# Data management
import pandas as pd 
import numpy as np

# Web application
import streamlit as st
from streamlit_option_menu import option_menu

# Data visualization
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Operational tools
import warnings
warnings.filterwarnings("ignore")

# WEB APPLICATION COLOR PALETTE
# -----------------------------
#--primary-100:#7E57C2;
#--primary-200:#b085f5;
#--primary-300:#ffe8ff;
#--accent-100:#9575CD;
#--accent-200:#36206d;
#--text-100:#333333;
#--text-200:#5c5c5c;
#--bg-100:#F5F5F5;
#--bg-200:#ebebeb;
#--bg-300:#c2c2c2;
      

st.set_page_config(
    page_title="Lung Cancer",
    page_icon="🫁",
    initial_sidebar_state="expanded",
    layout="centered"
)

# Web application CSS style over here
st.markdown(
    """
    <style>
        .main {background-color: #F5F5F5;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Lung Cancer Level Prediction App')
st.markdown('<span style="color:gray">This app predicts the lung cancer level of a person based on the data provided.</span>', unsafe_allow_html=True)

# Menu selection
menu = option_menu(
    menu_title=None,
    options=["Home", "Dataset", "Prediction", "Contact"],
    icons=["window", "database", "cpu", "envelope"],
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {
            "background-color": "#ebebeb",
            "border-radius": "0px",
            },
        "icon": {}, 
        "nav-link": {
            "font-size": "15px",
            "text-align": "center",
            },
        "nav-link-selected": {
            "background-color": "#7E57C2",
            "color": "white",
            "border-radius": "5px",
            },
    }
)