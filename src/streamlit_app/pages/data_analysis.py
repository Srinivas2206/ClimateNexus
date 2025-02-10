import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Climate Data Analysis")
st.write("Explore historical climate trends using visualizations.")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/merged_climate_data.csv")  # Make sure to have the dataset
    return df

df = load_data()

# Show dataset preview
if st.checkbox("Show raw data"):
    st.write(df.head())

# Data visualization
st.subheader("CO2 Emissions Over Time")
plt.figure(figsize=(10, 5))
sns.lineplot(x=df["Year"], y=df["co2"], marker="o", color="red")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions (Million Metric Tons)")
st.pyplot(plt)

st.subheader("Temperature Rise Over the Years")
plt.figure(figsize=(10, 5))
sns.lineplot(x=df["Year"], y=df["temp_anomaly"], marker="o", color="blue")
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
st.pyplot(plt)

