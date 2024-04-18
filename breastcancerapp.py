import numpy as np
import pickle
import streamlit as st

# Loading the saved model
loaded_model = pickle.load(open(r"C:\Users\LENOVO\OneDrive\Desktop\ML\breastcancer.sav", 'rb'))

def breastprediction(input_data):
    # Changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    ## Reshape the data as we are predicting label for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    if (prediction[0] == 0):
        return 'You are free from Breast Cancer😊'
    else:
        return 'You are at High Risk of breast cancer😒..please start medications ASAP'

def main():
    # Sidebar for navigation
    selected = st.sidebar.radio("Prediction Type", ["Breast Cancer Prediction"])

    # Breast Cancer Prediction Page
    if selected == "Breast Cancer Prediction":
        # Giving a title
        st.title('Breast Cancer Prediction Web App')

        # List of column names
        column_names = [
            'mean radius', 'mean texture', 'mean perimeter', 'mean area',
            'mean smoothness', 'mean compactness', 'mean concavity',
            'mean concave points', 'mean symmetry', 'mean fractal dimension',
            'radius error', 'texture error', 'perimeter error', 'area error',
            'smoothness error', 'compactness error', 'concavity error',
            'concave points error', 'symmetry error', 'fractal dimension error',
            'worst radius', 'worst texture', 'worst perimeter', 'worst area',
            'worst smoothness', 'worst compactness', 'worst concavity',
            'worst concave points', 'worst symmetry', 'worst fractal dimension'
        ]

        # Streamlit text input fields for each column
        input_values = {}
        for column_name in column_names:
            input_values[column_name] = st.text_input(column_name)

        # Code for prediction
        breast_cancer_prediction = ''

        # Creating a button for prediction
        if st.button('Predict Breast Cancer'):
            # Extracting input values as a list
            input_data = [float(input_values[column_name]) for column_name in column_names]
            breast_cancer_prediction = breastprediction(input_data)

        st.success(breast_cancer_prediction)

if __name__ == '__main__':
    main()
