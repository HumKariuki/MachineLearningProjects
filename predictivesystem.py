# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle


import warnings
warnings.filterwarnings('ignore')
loaded_model=pickle.load(open("C:/Users/LENOVO/OneDrive/Desktop/ML/train_model.sav",'rb'))
input_data = (5.2,0.44,0.04,1.4,0.036,43,119,0.9894,3.36,0.33,12.1)

# Changing the input data to numpy array
input_data_asnumpyarray=np.asarray(input_data)

## Reshape the data as we are predicting label for only one instance
input_data_reshaped = input_data_asnumpyarray.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)
if(prediction[0])==1:
    print('This is a good quality wine😊')
else:
    print('This is a poor quality wine😒')