# Crop Yield Prediction

This project is a **Crop Yield Predictor** that estimates the total harvested crop area based on various inputs such as rainfall, temperature, and area. The prediction is made using a machine learning model built with the **Decision Tree algorithm**.

## Project Overview

1. **Input Factors**: The predictor takes input factors such as:
   - Rainfall
   - Temperature
   - Area

2. **Data Cleaning and EDA**:
   - Perform data cleaning to remove inconsistencies.
   - Conduct **Exploratory Data Analysis (EDA)** and plot visualizations using **Matplotlib** and **Seaborn**.

3. **Feature Engineering**:
   - Use **Column Transformation** to transform the data.
   - Apply **One-Hot Encoding** for categorical variables.

4. **Model Building**:
   - Use the **Decision Tree** algorithm to build the predictive model.

5. **Model Saving**: 
   - Save the trained model using **Pickle** for future use.

6. **Web Application**: 
   - Build a web app using **Streamlit** to allow users to input data and predict crop yield.

## Tools & Libraries Used

- **Numpy**: For numerical operations
- **Pandas**: For data manipulation and analysis
- **Matplotlib**: For data visualization
- **Seaborn**: For enhanced data visualizations
- **Pickle**: For saving and loading the model
- **Scikit-learn (sklearn)**:
  - **Column Transformer**: For transforming columns
  - **One-Hot Encoding**: For encoding categorical variables
  - **Decision Tree Classifier**: The machine learning algorithm used for prediction
- **Streamlit**: For building the web application

## Methodology

1. **Data Cleaning**: Clean the dataset to remove missing or inconsistent data.
2. **Exploratory Data Analysis (EDA)**: Explore the dataset and visualize key features using **Matplotlib** and **Seaborn**.
3. **Feature Engineering**: 
   - Apply **Column Transformation** and **One-Hot Encoding** to prepare the data for modeling.
4. **Model Building**: Train the model using the **Decision Tree** algorithm.
5. **Model Saving**: Save the trained model using **Pickle**.
6. **Web App**: Build an interactive web application using **Streamlit** for users to input data and predict crop yield.


