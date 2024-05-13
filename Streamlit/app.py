# Data management
import pandas as pd

# Web application
import streamlit as st
from streamlit_option_menu import option_menu

# Operational tools
import pickle
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
)

# Web application CSS style over here
st.markdown(
    """
    <style>
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Lung Cancer Level Prediction App')
st.markdown('<span style="color:gray">This app predicts the lung cancer level of a person based on the data provided.</span>', unsafe_allow_html=True)

# Menu selection
menu = option_menu(
    menu_title=None,
    options=["Home", "Dataset", "Prediction", "Visualize", "Contact"],
    icons=["window", "database", "cpu", "graph-up", "envelope"],
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {
            "width": "100vw",
            "margin": 0,
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

# Load dataset
df = pd.read_csv("Database/BaseDataframe.csv")
df.drop(['index', 'Patient Id'], axis=1, inplace=True)

# Modeli içe aktar
with open('Model/logistic_regressor_model.pkl', 'rb') as file:
    lr_model = pickle.load(file)


if menu == "Home":
    from Pages import homepage
    homepage.show_home_page()
    
elif menu == "Dataset":
    from Pages import dataset
    dataset.show_data_page()
    
elif menu == "Prediction":
    from Pages import prediction
    prediction.show_prediction_page(df, lr_model)

elif menu == "Contact":
    from Pages import contact
    contact.show_contact_page()
elif menu == "Visualize":
    from Pages import visualization
    visualization.show_visualize_page()
