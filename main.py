import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("aqi_model.pkl", "rb") as f:
    model = pickle.load(f)

# App Title
st.title("🌍 Air Quality Index Prediction App")
st.write("Enter pollutant levels below to estimate AQI.")

# Input fields
pm25 = st.number_input("PM2.5 (µg/m³)", min_value=0.0, step=0.1)
pm10 = st.number_input("PM10 (µg/m³)", min_value=0.0, step=0.1)
no2 = st.number_input("NO2 (µg/m³)", min_value=0.0, step=0.1)
so2 = st.number_input("SO2 (µg/m³)", min_value=0.0, step=0.1)

# Predict button
if st.button("Predict AQI"):
    features = np.array([[pm25, pm10, no2, so2]])
    prediction = model.predict(features)[0]

    # AQI Meaning
    if prediction <= 50:
        category = "Good"
    elif prediction <= 100:
        category = "Moderate"
    elif prediction <= 150:
        category = "Unhealthy for sensitive groups"
    elif prediction <= 200:
        category = "Unhealthy"
    elif prediction <= 300:
        category = "Very unhealthy"
    else:
        category = "Hazardous"

    st.success(f"Predicted AQI: {prediction:.2f} ({category})")

# Footer
st.markdown("---")
st.markdown("**Created by Muhammad Abdullah**")
