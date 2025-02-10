import streamlit as st

st.set_page_config(page_title="Climate Change Analysis", layout="wide")

st.sidebar.title("Navigation")
st.sidebar.markdown("### Select a Page")
st.sidebar.page_link("pages/home.py", label="🏠 Home")
st.sidebar.page_link("pages/data_analysis.py", label="📊 Data Analysis")
st.sidebar.page_link("pages/prediction.py", label="🔮 CO2 Prediction")
st.sidebar.page_link("pages/cloud_scalability.py", label="☁️ Cloud & Scalability")
st.sidebar.page_link("pages/sustainable_solutions.py", label="🌱 Sustainable Solutions")

st.title("Climate Change Analysis & Solutions")
st.write("Use the sidebar to navigate between different features of the project.")
