import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from azure.storage.blob import BlobServiceClient

# Azure Blob Storage Integration
def fetch_data_from_azure():
    connect_str = st.secrets["AZURE_STORAGE_CONNECTION_STRING"]
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container="climate-data", blob="merged_climate_data.csv")
    data = blob_client.download_blob().readall()
    return pd.read_csv(data)

# Real-Time Prediction
def get_co2_prediction(model_input):
    response = requests.post("http://climate-api:8000/predict", json={"data": model_input})
    return response.json()["prediction"]

# Sustainability Calculator
def calculate_footprint(electricity, miles):
    return (electricity * 0.85) + (miles * 2.31 * 4)

# Blockchain Visualization (Mock)
def display_blockchain_transactions():
    st.write("### Carbon Credit Transactions (Blockchain)")
    transactions = [
        {"User": "Factory A", "Credits": 150, "Date": "2025-01-01"},
        {"User": "City B", "Credits": 75, "Date": "2025-01-02"}
    ]
    st.dataframe(transactions)

# Main Dashboard
def main():
    st.set_page_config(layout="wide")
    st.title("ClimateGuard: Real-Time Climate Analytics")
    
    # Fetch Data
    df = fetch_data_from_azure()
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        year = st.slider("Select Year", int(df['Year'].min()), int(df['Year'].max()))
    with col2:
        region = st.selectbox("Region", ["Global", "Northern Hemisphere"])
    
    # Visualizations
    fig1 = px.line(df[df['Year'] <= year], x='Year', y=['temp_anomaly', 'co2'], 
                   title="Temperature Anomaly vs CO2 Levels")
    st.plotly_chart(fig1, use_container_width=True)
    
    # Prediction Section
    st.subheader("CO2 Level Forecast")
    prediction_input = st.slider("Select future years", 2025, 2050, 2030)
    if st.button("Predict"):
        model_input = [[df['co2'].iloc[-3]], [df['co2'].iloc[-2]], [df['co2'].iloc[-1]]]
        prediction = get_co2_prediction(model_input)
        st.metric(f"Predicted CO2 in {prediction_input}", f"{prediction:.2f} ppm")
    
    # Sustainability Calculator
    with st.expander("Carbon Footprint Calculator"):
        electricity = st.number_input("Monthly kWh", value=300)
        miles = st.number_input("Weekly Miles Driven", value=100)
        footprint = calculate_footprint(electricity, miles)
        st.metric("Your Monthly CO2 Footprint", f"{footprint:.1f} kg CO2e")
    
    # Blockchain Integration
    display_blockchain_transactions()

if __name__ == "__main__":
    main()