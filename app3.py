import streamlit as st
import numpy as np
import pickle

# Load the models
dtr = pickle.load(open('dtr.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

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
    
    # Make a prediction in hg/ha
    prediction_hg_ha = dtr.predict(transformed_features).reshape(1, -1)
    
    # Convert hg/ha to pounds per acre (1 hg/ha = 0.892179 lbs/acre)
    prediction_lbs_acre = prediction_hg_ha[0][0] * 0.892179

    # Display the prediction in pounds per acre
    st.subheader("Predicted Yield (lbs/acre):")
    st.write(prediction_lbs_acre)
