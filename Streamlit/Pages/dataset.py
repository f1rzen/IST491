# Web application
import streamlit as st

# Data visualization
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

def show_dataset_page(df):
    st.markdown(
        """
        <h2>About Dataset</h2>
        
        <p>
            This dataset contains information on patients with lung cancer, including their age, gender, air pollution exposure, alcohol use, dust allergy, occupational hazards, genetic risk, chronic lung disease, balanced diet, obesity, smoking, passive smoker, chest pain, coughing of blood, fatigue, weight loss ,shortness of breath ,wheezing ,swallowing difficulty ,clubbing of finger nails and snoring
        </p>
        
        <a href="https://www.kaggle.com/datasets/thedevastator/cancer-patients-and-air-pollution-a-new-link?resource=download" target=_blank><p>Click for Data Source</p></a>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <a href="data:file/csv;base64,{data}" download="{file_name}" style="padding: 10px; background-color: #7E57C2; color: white; border-radius: 5px; text-decoration: none;">
                {label}
            </a>
        </div>
        """.format(
            data=df.to_csv(index=False).encode().decode('utf-8').replace('\n', '%0A'),
            file_name='dataset.csv',
            label="Download Dataset"
        ),
        unsafe_allow_html=True
    )
    
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=list(df.columns),
            fill_color='#7E57C2',
            align='left',
            font=dict(color='white', size=12)
        ),
        cells=dict(
            values=[df[col] for col in df.columns],
            fill_color='white',
            align='left',
            font=dict(color='#333333', size=12)
        )
    )])

    fig.update_layout(
        height=720
    )
    
    st.plotly_chart(
        fig,
        use_container_width=True,
        theme='streamlit',
        config={
            'displayModeBar': False
        }
    )