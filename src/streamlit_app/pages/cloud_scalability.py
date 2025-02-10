import streamlit as st

st.title("☁️ Cloud Scalability & Storage")
st.write("Explore how cloud computing is used to store and process climate data.")

st.markdown("""
### Cloud Services Used:
- **Azure Blob Storage**: Stores climate datasets for real-time access.
- **Azure Functions**: Processes data without dedicated servers.
- **Azure ML Services**: Runs machine learning models for CO2 predictions.
- **Streamlit App Hosting**: Can be deployed on **Azure App Services**.
""")

st.subheader("📂 Upload Data to Cloud")
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file is not None:
    st.success("File uploaded successfully. It will be processed in Azure.")
