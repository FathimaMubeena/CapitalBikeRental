import streamlit as st
import pandas as pd
import joblib

# Load the trained model (pipeline)
model = joblib.load('bike_rental_model.pkl')  # Replace with your model's file name

# Title of the web app
st.title("Capital Bike Rental Prediction")

# Sidebar for user input
st.sidebar.header("User Input Features")

# Function to get user input
def user_input_features():
    season = st.sidebar.selectbox('Season', [1, 2, 3, 4])
    hr = st.sidebar.slider('Hour', 0, 23, 12)
    holiday = st.sidebar.selectbox('Holiday', [0, 1])
    workingday = st.sidebar.selectbox('Working Day', [0, 1])
    weathersit = st.sidebar.selectbox('Weather', [1, 2, 3, 4])
    temp = st.sidebar.slider('Temperature (normalized)', 0.0, 1.0, 0.5)
    atemp = st.sidebar.slider('Feels-like Temperature (normalized)', 0.0, 1.0, 0.5)
    hum = st.sidebar.slider('Humidity (normalized)', 0.0, 1.0, 0.5)
    windspeed = st.sidebar.slider('Windspeed (normalized)', 0.0, 1.0, 0.5)

    data = {
        'season': season,
        'hr': hr,
        'holiday': holiday,
        'workingday': workingday,
        'weathersit': weathersit,
        'temp': temp,
        'atemp': atemp,
        'hum': hum,
        'windspeed': windspeed
    }

    features = pd.DataFrame(data, index=[0])
    return features

# Get user input
input_df = user_input_features()

# Display user input
st.subheader('User Input parameters')
st.write(input_df)

# Make predictions
prediction = model.predict(input_df)


# Display predictions
st.subheader('Prediction')
st.write(f'Predicted Bike Rentals: {int(prediction[0])}')