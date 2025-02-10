import streamlit as st
import requests
import numpy as np

st.title("🔮 CO2 Emission Prediction")
st.write("Predict future CO2 emissions using our trained machine learning model.")

# Input fields
features = st.text_area("Enter features as comma-separated values (e.g., 400, 20, 1.2):")

if st.button("Predict"):
    if features:
        try:
            feature_list = [float(x) for x in features.split(",")]
            payload = {"features": feature_list}

            # API request to Flask server
            response = requests.post("http://127.0.0.1:5000/predict", json=payload)

            if response.status_code == 200:
                result = response.json()
                st.success(f"Predicted CO2 Emission: {result['prediction']}")
            else:
                st.error("Error fetching prediction")
        except Exception as e:
            st.error(f"Invalid input: {e}")
    else:
        st.warning("Please enter valid input data.")
