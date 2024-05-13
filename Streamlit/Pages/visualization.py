import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

@st.cache_data
def load_data():
    data = pd.read_csv("../Database/BaseDataframe.csv")
    return data

data = load_data()
def show_visualize_page():
    st.header("Visualizations")
    col1,col2 = st.columns(2)
    with col1:
        plot_type = st.selectbox("Select a type of plot", ["Histogram", "Pie chart", "Violin plot"])
    with col2:
        feature = st.selectbox("Select a feature:", data.columns)
    col3, col4 = st.columns(2)
    with col3:
        if plot_type == 'Histogram':
            bins = st.slider("Number of bins", 5, 50, 25)
            fig = px.histogram(data, x=feature, nbins=bins)
            st.plotly_chart(fig)
        elif plot_type == 'Pie chart':
            fig = px.pie(data, names=feature)
            st.plotly_chart(fig)
        elif plot_type == 'Violin plot':
            fig = px.violin(data, y=feature)
            st.plotly_chart(fig)
            

    st.write("Summary Statistics")
    desc = data[feature].describe().to_frame()
    st.write(desc.transpose())

    
    



