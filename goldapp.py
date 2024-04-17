
import numpy as np
import streamlit as st
import joblib

# Loading the saved model using joblib
loaded_model = pickle.load(open("goldmodel.sav", 'rb'))


def gold_price_prediction(input_data):
    # Reshape the input data as we are predicting for only one instance
    input_data_reshaped = np.asarray(input_data).reshape(1, -1)
    
    # Predict the gold price using the loaded model
    predicted_gold_price = loaded_model.predict(input_data_reshaped)
    
    return predicted_gold_price[0]

def main():
    # Sidebar for navigation
    selected = st.sidebar.radio("Prediction Type", ["Gold Price Prediction"])

    # Gold Price Prediction Page
    if selected == "Gold Price Prediction":
        # Giving a title
        st.title('Gold Price Prediction Web App')

        # Input fields for predictors
        spx = st.number_input('SPX')
        usd = st.number_input('USD')
        slv = st.number_input('SLV')
        eur_usd = st.number_input('EUR/USD')
        
        # Code for prediction
        prediction = ''

        # Creating a button for prediction
        if st.button('Predict Gold Price'):
            prediction = gold_price_prediction([spx, usd, slv, eur_usd])
        
        st.success(f'Predicted Gold Price: {prediction}')

if __name__ == '__main__':
    main()




