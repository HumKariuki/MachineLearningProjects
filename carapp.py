# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:41:57 2024

@author: LENOVO
"""

import numpy as np
import pickle
import streamlit as st

# Loading the saved model
loaded_model = pickle.load(open("carmodel.sav", 'rb'))

def car_price_prediction(input_data):
    # Predict the car price using the loaded model
    predicted_car_price = loaded_model.predict(input_data)
    
    return predicted_car_price[0]

def main():
    # Sidebar for navigation
    selected = st.sidebar.radio("Prediction Type", ["Car Price Prediction"])

    # Car Price Prediction Page
    if selected == "Car Price Prediction":
        # Giving a title
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
        
        # Code for prediction
        prediction = ''

        # Creating a button for prediction
        if st.button('Predict Car Price'):
            input_data = [[year, present_price, kms_driven, fuel_type_numeric, seller_type_numeric, transmission_numeric, owner]]
            prediction = car_price_prediction(input_data)
        
        st.success(f'Predicted Car Price: {prediction}')

if __name__ == '__main__':
    main()
