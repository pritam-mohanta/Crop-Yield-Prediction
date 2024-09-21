import streamlit as st
import numpy as np
import pickle

# Load the models
dtr = pickle.load(open('dtr.pkl', 'rb'))
preprocessor = pickle.load(open('preprocesser.pkl', 'rb'))

# Title of the web app
st.title("Crop Yield Prediction Per Country")

# Create input fields for the user to input data
st.header("Input All Features Here")

# Input fields
Year = st.number_input('Year', min_value=1900, max_value=2100, value=2013)
average_rain_fall_mm_per_year = st.number_input('Average Rainfall (mm/year)')
pesticides_tonnes = st.number_input('Pesticides (tonnes)')
avg_temp = st.number_input('Average Temperature (°C)')
Area = st.text_input('Area')
Item = st.text_input('Item')

# Predict button
if st.button('Predict'):
    # Prepare the input features as numpy array
    features = np.array([[Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item]], dtype=object)
    
    # Preprocess the input features
    transformed_features = preprocessor.transform(features)
    
    # Make a prediction
    prediction = dtr.predict(transformed_features).reshape(1, -1)

    # Display the prediction
    st.subheader("Predicted Yield:")
    st.write(prediction[0][0])
