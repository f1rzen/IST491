from altair import Predicate
from git import UnsafeOptionError
import streamlit as st
import pandas as pd

def show_prediction_page(df, model, encoder):
    
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
        container = st.container(
            height=245
        )
        
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
    
    st.divider()
    
    col1, col2 = st.columns((2,1))
    
    ### PARAMETERS ###
    with col1:
        container = st.container()
        
        label = 'Fatigue'
        fatigue = container.slider(
            label='Fatigue',
            min_value=df[label].min(),
            max_value=df[label].max(),
            value=df[label].value_counts().index.tolist()[0]
        )
        
        label = 'Clubbing of Finger Nails'
        clubbing_of_finger_nails = container.slider(
            label='Clubbing of Finger Nails',
            min_value=df[label].min(),
            max_value=df[label].max(),
            value=df[label].value_counts().index.tolist()[0],
            help="Nail clubbing is when your nails appear wider, spongelike or swollen, like an upside-down spoon"
        )
            
        label = 'Wheezing'
        wheezing = container.slider(
            label='Wheezing',
            min_value=df[label].min(),
            max_value=df[label].max(),
            value=df[label].value_counts().index.tolist()[0]
        )
        
        label = 'Snoring'
        snoring = container.slider(
            label="Snoring",
            min_value=df[label].min(),
            max_value=df[label].max(),
            value=df[label].value_counts().index.tolist()[0]
        )
            
        with container.expander("Choose Details", expanded=False):
            label = 'Dust Allergy'
            dust_allergy = st.slider(
                label='Dust Allergy',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].value_counts().index.tolist()[0]
            )
            
            label = 'OccuPational Hazards'
            occupational_hazards = st.slider(
                label='Occupational Hazards',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].value_counts().index.tolist()[0]
            )
            
            label = 'Chest Pain'
            chest_pain = st.slider(
                label='Chest Pain',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
            
            label='Age'
            age = st.slider(
                label='Age',
                min_value=18,
                max_value=65,
                value=df[label].mean().astype(int)
            )

            label='Alcohol use'
            alcohol_use = st.slider(
                label="Alcohol Use",
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
            
            label = 'Smoking'
            smoking = st.slider(
                label="Smoking",
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
            
            label = 'Air Pollution'
            air_pollution = st.slider(
                label='Air Pollution',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
            
            label = 'Dry Cough'
            dry_cough = st.slider(
                label='Dry Cough',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
            
            label = 'Frequent Cold'
            frequent_cold = st.slider(
                label='Frequent Cold',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
            
            label = 'Swallowing Difficulty'
            swallowing_difficulty = st.slider(
                label='Swallowing Difficulty',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
            
            label = 'Shortness of Breath'
            shortness_of_breath = st.slider(
                label='Shortness of Breath',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
            
            label = 'Weight Loss'
            weight_loss = st.slider(
                label='Weight Loss',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
            
            label = 'Coughing of Blood'
            coughging_of_blood = st.slider(
                label='Caughing of Blood',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
            
            label = 'Passive Smoker'
            passive_smoker = st.slider(
                label='Passive Smoker',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
            
            label = 'Obesity'
            obesity = st.slider(
                label='Obesity',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
        
            label = 'Balanced Diet'
            balanced_diet = st.slider(
                label='Balanced Diet',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
            
            label = 'chronic Lung Disease'
            chronic_lung_disease = st.slider(
                label='Chronic Lung Disease',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
            
            label = 'Genetic Risk'
            genetic_risk = st.slider(
                label='Genetic Risk',
                min_value=df[label].min(),
                max_value=df[label].max(),
                value=df[label].mean().astype(int)
            )
        
    with col2:
        container = st.container(
            border=True
        )
        
        with open('./PredictionPage/info_card.html', 'r', encoding='utf-8') as f:
            page = f.read()
            f.close()
        
        container.markdown(
            f"""
            {page}
            """,
            unsafe_allow_html=True
        )

        gender_text = container.radio(
            label="Gender",
            options=["Male", "Female"],
            index=0
        )
        gender = 1 if gender_text == "Male" else 0
         
        temp_dataframe = pd.DataFrame({
            'Age': [age],
            'Gender': [gender],
            'Air Pollution': [air_pollution],
            'Alcohol use': [alcohol_use],
            'Dust Allergy': [dust_allergy],
            'OccuPational Hazards': [occupational_hazards],
            'Genetic Risk': [genetic_risk],
            'chronic Lung Disease': [chronic_lung_disease],
            'Balanced Diet': [balanced_diet],
            'Obesity': [obesity],
            'Smoking': [smoking],
            'Passive Smoker': [passive_smoker],
            'Chest Pain': [chest_pain],
            'Coughing of Blood': [coughging_of_blood],
            'Fatigue': [fatigue],
            'Weight Loss': [weight_loss],
            'Shortness of Breath': [shortness_of_breath],
            'Wheezing': [wheezing],
            'Swallowing Difficulty': [swallowing_difficulty],
            'Clubbing of Finger Nails': [clubbing_of_finger_nails],
            'Frequent Cold': [frequent_cold],
            'Dry Cough': [dry_cough],
            'Snoring': [snoring]
        })
        
        prediction = model.predict(temp_dataframe)
        prediction = encoder.inverse_transform(prediction)[0]
        
        result_dataframe = temp_dataframe.copy()
        result_dataframe['Prediction'] = prediction
        
        container.markdown(
            f"""
            <article>Cancer Risk Level
            <br>
            <b>{prediction}<b>
            </article>
            """,
            unsafe_allow_html=True
        )