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
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Function to handle missing or incomplete inputs
def handle_missing_inputs(fields, default_value=0.5):
    for key in fields:
        if not fields[key]:
            fields[key] = default_value
    st.warning("Some fields were missing. Predicting with default values (0.5). For better accuracy, please provide full information.")

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Getting the input data from the user
    fields = {}
    with st.form(key='diabetes_form'):
        col1, col2, col3 = st.columns(3)
        with col1:
            fields['Pregnancies'] = st.number_input('Number of Pregnancies', min_value=0, step=1)
        with col2:
            fields['Glucose'] = st.number_input('Glucose Level', min_value=0)
        with col3:
            fields['BloodPressure'] = st.number_input('Blood Pressure value', min_value=0)

        with col1:
            fields['SkinThickness'] = st.number_input('Skin Thickness value', min_value=0)
        with col2:
            fields['Insulin'] = st.number_input('Insulin Level', min_value=0)
        with col3:
            fields['BMI'] = st.number_input('BMI value', min_value=0.0)

        with col1:
            fields['DiabetesPedigreeFunction'] = st.number_input('Diabetes Pedigree Function value', min_value=0.0)
        with col2:
            fields['Age'] = st.number_input('Age of the Person', min_value=0)

        submit_button = st.form_submit_button('Diabetes Test Result')

    # Code for Prediction
    if submit_button:
        # Validate and handle missing or incorrect inputs
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
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Getting the input data from the user
    fields = {}
    with st.form(key='heart_disease_form'):
        col1, col2, col3 = st.columns(3)
        with col1:
            fields['age'] = st.number_input('Age', min_value=0, step=1)
        with col2:
            fields['sex'] = st.number_input('Sex', min_value=0, max_value=1, step=1)
        with col3:
            fields['cp'] = st.number_input('Chest Pain types', min_value=0, max_value=3, step=1)

        with col1:
            fields['trestbps'] = st.number_input('Resting Blood Pressure', min_value=0)
        with col2:
            fields['chol'] = st.number_input('Serum Cholestoral in mg/dl', min_value=0)
        with col3:
            fields['fbs'] = st.number_input('Fasting Blood Sugar > 120 mg/dl', min_value=0, max_value=1, step=1)

        with col1:
            fields['restecg'] = st.number_input('Resting Electrocardiographic results', min_value=0, max_value=2, step=1)
        with col2:
            fields['thalach'] = st.number_input('Maximum Heart Rate achieved', min_value=0)
        with col3:
            fields['exang'] = st.number_input('Exercise Induced Angina', min_value=0, max_value=1, step=1)

        with col1:
            fields['oldpeak'] = st.number_input('ST depression induced by exercise', min_value=0.0)
        with col2:
            fields['slope'] = st.number_input('Slope of the peak exercise ST segment', min_value=0, max_value=2, step=1)
        with col3:
            fields['ca'] = st.number_input('Major vessels colored by flourosopy', min_value=0)

        with col1:
            fields['thal'] = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', min_value=0, max_value=2, step=1)

        submit_button = st.form_submit_button('Heart Disease Test Result')

    # Code for Prediction
    if submit_button:
        handle_missing_inputs(fields)
        heart_prediction = heart_disease_model.predict([[fields['age'], fields['sex'], fields['cp'], fields['trestbps'],
                                                         fields['chol'], fields['fbs'], fields['restecg'], fields['thalach'],
                                                         fields['exang'], fields['oldpeak'], fields['slope'], fields['ca'],
                                                         fields['thal']]])

        if heart_prediction[0] == 1:
            st.success('The person is having heart disease')
        else:
            st.success('The person does not have any heart disease')

# Parkinson's Prediction Page
elif selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")

    # Getting the input data from the user
    fields = {}
    with st.form(key='parkinsons_form'):
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            fields['fo'] = st.number_input('MDVP:Fo(Hz)', min_value=0.0)
        with col2:
            fields['fhi'] = st.number_input('MDVP:Fhi(Hz)', min_value=0.0)
        with col3:
            fields['flo'] = st.number_input('MDVP:Flo(Hz)', min_value=0.0)

        with col4:
            fields['Jitter_percent'] = st.number_input('MDVP:Jitter(%)', min_value=0.0)
        with col5:
            fields['Jitter_Abs'] = st.number_input('MDVP:Jitter(Abs)', min_value=0.0)

        with col1:
            fields['RAP'] = st.number_input('MDVP:RAP', min_value=0.0)
        with col2:
            fields['PPQ'] = st.number_input('MDVP:PPQ', min_value=0.0)
        with col3:
            fields['DDP'] = st.number_input('Jitter:DDP', min_value=0.0)

        with col4:
            fields['Shimmer'] = st.number_input('MDVP:Shimmer', min_value=0.0)
        with col5:
            fields['Shimmer_dB'] = st.number_input('MDVP:Shimmer(dB)', min_value=0.0)

        with col1:
            fields['APQ3'] = st.number_input('Shimmer:APQ3', min_value=0.0)
        with col2:
            fields['APQ5'] = st.number_input('Shimmer:APQ5', min_value=0.0)
        with col3:
            fields['APQ'] = st.number_input('MDVP:APQ', min_value=0.0)

        with col4:
            fields['DDA'] = st.number_input('Shimmer:DDA', min_value=0.0)
        with col5:
            fields['NHR'] = st.number_input('NHR', min_value=0.0)

        with col1:
            fields['HNR'] = st.number_input('HNR', min_value=0.0)
        with col2:
            fields['RPDE'] = st.number_input('RPDE', min_value=0.0)
        with col3:
            fields['DFA'] = st.number_input('DFA', min_value=0.0)

        with col4:
            fields['spread1'] = st.number_input('spread1', min_value=0.0)
        with col5:
            fields['spread2'] = st.number_input('spread2', min_value=0.0)

        with col1:
            fields['D2'] = st.number_input('D2', min_value=0.0)
        with col2:
            fields['PPE'] = st.number_input('PPE', min_value=0.0)

        submit_button = st.form_submit_button("Parkinson's Test Result")

    # Code for Prediction
    if submit_button:
        handle_missing_inputs(fields)
        parkinsons_prediction = parkinsons_model.predict([[fields['fo'], fields['fhi'], fields['flo'],
                                                           fields['Jitter_percent'], fields['Jitter_Abs'], fields['RAP'],
                                                           fields['PPQ'], fields['DDP'], fields['Shimmer'],
                                                           fields['Shimmer_dB'], fields['APQ3'], fields['APQ5'],
                                                           fields['APQ'], fields['DDA'], fields['NHR'], fields['HNR'],
                                                           fields['RPDE'], fields['DFA'], fields['spread1'],
                                                           fields['spread2'], fields['D2'], fields['PPE']]])

        if parkinsons_prediction[0] == 1:
            st.success("The person has Parkinson's disease")
        else:
            st.success("The person does not have Parkinson's disease")

# Show footer message
st.markdown('---')
st.info("For more accurate results, please provide full information.")
