import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache
def load_data():
    data = pd.read_csv("../Database/BaseDataframe.csv")
    return data

data = load_data()
def show_visualize_page():
    st.header("Visualizations")

    plot_type = st.selectbox("Select a type of plot", ["Histogram", "Pie chart", "Box plot"])

    if plot_type == 'Histogram':
        feature = st.sidebar.selectbox("Select a feature for histogram", data.columns)
        bins = st.sidebar.slider("Number of bins", 5, 50, 25)
        st.write(sns.histplot(data[feature], bins=bins))
        st.pyplot()

    elif plot_type == 'Pie chart':
        feature = st.sidebar.selectbox("Select a feature for pie chart", data.columns)
        st.write(data[feature].value_counts().plot.pie(autopct="%1.1f%%"))
        st.pyplot()

    elif plot_type == 'Box plot':
        feature = st.sidebar.selectbox("Select a feature for box plot", data.columns)
        st.write(sns.boxplot(x=data[feature]))
        st.pyplot()



