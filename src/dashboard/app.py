import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")
df = pd.read_csv("data/processed/merged_climate_data.csv")

# Filters
year = st.slider("Select Year", int(df['Year'].min()), int(df['Year'].max()))
region = st.selectbox("Region", ['Global', 'Northern Hemisphere'])

# Plot
fig = px.line(df[df['Year'] <= year], x='Year', y='temp_anomaly', 
              title="Temperature Anomaly Over Time")
st.plotly_chart(fig, use_container_width=True)

# Sustainability Calculator
with st.expander("Calculate Your CO2 Impact"):
    electricity = st.number_input("Monthly kWh", value=100)
    miles = st.number_input("Weekly Miles Driven", value=50)
    co2 = (electricity * 0.85) + (miles * 2.31 * 4)
    st.metric("Monthly CO2e", f"{co2:.1f} kg")