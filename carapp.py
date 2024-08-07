# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:41:57 2024

@author: LENOVO
"""

import numpy as np
import pickle
import streamlit as st
import os
import traceback

# Function to load the saved model
def load_model(model_path):
    if os.path.exists(model_path):
        try:
            with open(model_path, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            st.error(f"Error loading model: {e}")
            st.error(traceback.format_exc())
            return None
    else:
        st.error("Model file not found. Please ensure the model file exists in the directory.")
        return None

# Load the model
model_path = "ncarmodel.sav"
loaded_model = load_model(model_path)

def car_price_prediction(input_data):
    try:
        if loaded_model is not None:
            predicted_car_price = loaded_model.predict(input_data)
            return predicted_car_price[0]
        else:
            st.error("Model not loaded. Prediction cannot be performed.")
            return None
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        st.error(traceback.format_exc())
        return None

def main():
    st.sidebar.title("Navigation")
    selected = st.sidebar.radio("Prediction Type", ["Car Price Prediction"])

    if selected == "Car Price Prediction":
        st.title('Car Price Prediction Web App')

        # Input fields for predictors
        year = st.number_input('Year', min_value=2000, max_value=2022, step=1)
        present_price = st.number_input('Present Price', min_value=0.0)
        kms_driven = st.number_input('Kms Driven', min_value=0)
        fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
        seller_type = st.selectbox('Seller Type', ['Individual', 'Dealer'])
        transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
        owner = st.number_input('Owner', min_value=0, max_value=3, step=1)
        
        # Convert categorical variables to numerical
        fuel_type_mapping = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
        seller_type_mapping = {'Individual': 0, 'Dealer': 1}
        transmission_mapping = {'Manual': 0, 'Automatic': 1}
        
        fuel_type_numeric = fuel_type_mapping[fuel_type]
        seller_type_numeric = seller_type_mapping[seller_type]
        transmission_numeric = transmission_mapping[transmission]
        
        prediction = ''

        if st.button('Predict Car Price'):
            input_data = np.array([[year, present_price, kms_driven, fuel_type_numeric, seller_type_numeric, transmission_numeric, owner]])
            if loaded_model:
                prediction = car_price_prediction(input_data)
                if prediction is not None:
                    st.success(f'Predicted Car Price: {prediction}')
                else:
                    st.error("Prediction could not be performed.")
            else:
                st.error("Model is not loaded. Please load a valid model.")

if __name__ == '__main__':
    main()
