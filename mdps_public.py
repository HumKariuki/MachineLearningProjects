# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:01:15 2022
@author: siddhardhan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))


# Sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Default values for each prediction category
default_values = {
    'Diabetes': {
        'Pregnancies': 0,
        'Glucose': 100,
        'BloodPressure': 70,
        'SkinThickness': 20,
        'Insulin': 80,
        'BMI': 25.0,
        'DiabetesPedigreeFunction': 0.5,
        'Age': 30
    },
    'Heart Disease': {
        'age': 50,
        'sex': 1,
        'cp': 1,
        'trestbps': 120,
        'chol': 200,
        'fbs': 0,
        'restecg': 0,
        'thalach': 150,
        'exang': 0,
        'oldpeak': 0,
        'slope': 1,
        'ca': 0,
        'thal': 2
    },
    "Parkinson's": {
        'fo': 150,
        'fhi': 200,
        'flo': 120,
        'Jitter_percent': 0.005,
        'Jitter_Abs': 0.00005,
        'RAP': 0.002,
        'PPQ': 0.002,
        'DDP': 0.005,
        'Shimmer': 0.02,
        'Shimmer_dB': 0.5,
        'APQ3': 0.01,
        'APQ5': 0.015,
        'APQ': 0.02,
        'DDA': 0.03,
        'NHR': 0.02,
        'HNR': 15,
        'RPDE': 0.5,
        'DFA': 0.6,
        'spread1': -5,
        'spread2': 0,
        'D2': 2,
        'PPE': 0.5
    }
}


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    
    st.title('Diabetes Prediction using ML')
    
    # Getting the input data from the user
    with st.form(key='diabetes_form'):
        col1, col2, col3 = st.columns(3)
        fields = {}
        for field in ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']:
            with col1 if field in ['Pregnancies', 'SkinThickness', 'DiabetesPedigreeFunction'] else col2 if field in ['Glucose', 'Insulin', 'Age'] else col3:
                fields[field] = st.number_input(f'{field.replace("_", " ")}', value=default_values['Diabetes'].get(field, 0))
        
        submit_button = st.form_submit_button('Diabetes Test Result')
    
    # Code for Prediction
    if submit_button:
        try:
            diab_prediction = diabetes_model.predict([[fields['Pregnancies'], fields['Glucose'], fields['BloodPressure'],
                                                       fields['SkinThickness'], fields['Insulin'], fields['BMI'],
                                                       fields['DiabetesPedigreeFunction'], fields['Age']]])

            if diab_prediction[0] == 1:
                st.success('The person is diabetic')
            else:
                st.success('The person is not diabetic')

        except ValueError as e:
            st.error(f"Error: {e}. Please ensure all input fields are filled correctly.")


# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    
    st.title('Heart Disease Prediction using ML')
    
    # Getting the input data from the user
    with st.form(key='heart_disease_form'):
        col1, col2, col3 = st.columns(3)
        fields = {}
        for field in ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']:
            with col1 if field in ['age', 'trestbps', 'restecg', 'slope', 'thal'] else col2 if field in ['sex', 'chol', 'thalach', 'ca'] else col3:
                fields[field] = st.number_input(f'{field.replace("_", " ")}', value=default_values['Heart Disease'].get(field, 0))
        
        submit_button = st.form_submit_button('Heart Disease Test Result')
    
    # Code for Prediction
    if submit_button:
        try:
            heart_prediction = heart_disease_model.predict([[fields['age'], fields['sex'], fields['cp'], fields['trestbps'],
                                                             fields['chol'], fields['fbs'], fields['restecg'], fields['thalach'],
                                                             fields['exang'], fields['oldpeak'], fields['slope'], fields['ca'], fields['thal']]])

            if heart_prediction[0] == 1:
                st.success('The person is having heart disease')
            else:
                st.success('The person does not have any heart disease')

        except ValueError as e:
            st.error(f"Error: {e}. Please ensure all input fields are filled correctly.")


# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    
    st.title("Parkinson's Disease Prediction using ML")
    
    # Getting the input data from the user
    with st.form(key='parkinsons_form'):
        col1, col2, col3, col4, col5 = st.columns(5)
        fields = {}
        for field in ['fo', 'fhi', 'flo', 'Jitter_percent', 'Jitter_Abs', 'RAP', 'PPQ', 'DDP', 'Shimmer', 'Shimmer_dB',
                      'APQ3', 'APQ5', 'APQ', 'DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE']:
            with col1 if field in ['fo', 'Jitter_percent', 'RAP', 'APQ3', 'APQ', 'RPDE', 'spread1'] else col2 if field in ['fhi', 'Jitter_Abs', 'PPQ', 'APQ5', 'DFA', 'spread2'] else col3 if field in ['flo', 'Shimmer', 'DDP', 'APQ', 'HNR', 'D2'] else col4 if field in ['Shimmer_dB', 'NHR', 'DDA', 'RPDE'] else col5:
                fields[field] = st.number_input(f'{field.replace("_", " ")}', value=default_values["Parkinson's"].get(field, 0))
        
        submit_button = st.form_submit_button("Parkinson's Test Result")
    
    # Code for Prediction
    if submit_button:
        try:
            parkinsons_prediction = parkinsons_model.predict([[
                fields['fo'], fields['fhi'], fields['flo'], fields['Jitter_percent'], fields['Jitter_Abs'], fields['RAP'],
                fields['PPQ'], fields['DDP'], fields['Shimmer'], fields['Shimmer_dB'], fields['APQ3'], fields['APQ5'],
                fields['APQ'], fields['DDA'], fields['NHR'], fields['HNR'], fields['RPDE'], fields['DFA'], fields['spread1'],
                fields['spread2'], fields['D2'], fields['PPE']
            ]])

            if parkinsons_prediction[0] == 1:
                st.success("The person has Parkinson's disease")
            else:
                st.success("The person does not have Parkinson's disease")

        except ValueError as e:
            st.error(f"Error: {e}. Please ensure all input fields are filled correctly.")
