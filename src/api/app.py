import os
import streamlit as st
from azure.storage.blob import BlobServiceClient
from tensorflow.keras.models import load_model
import tensorflow.keras.metrics as km  # ✅ Import Keras metrics

# Azure Storage Account details
STORAGE_ACCOUNT_NAME = "climatenexusstorage"
CONTAINER_NAME = "modelcontainer"
BLOB_NAME = "co2_lstm.h5"
LOCAL_MODEL_PATH = "models/co2_lstm.h5"

# Function to download model from Azure Blob Storage
def download_model():
    try:
        blob_service_client = BlobServiceClient.from_connection_string(st.secrets["AZURE_STORAGE_CONNECTION_STRING"])
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=BLOB_NAME)

        os.makedirs("models", exist_ok=True)  # Ensure the models directory exists
        with open(LOCAL_MODEL_PATH, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())

        print("✅ Model downloaded successfully!")
    except Exception as e:
        print(f"❌ Error downloading model: {e}")

# Download model before loading it
download_model()

# ✅ Define custom objects (fix for "Could not locate function 'mse'")
custom_objects = {"mse": km.MeanSquaredError}

# Load the model with custom objects
try:
    model = load_model(LOCAL_MODEL_PATH, custom_objects=custom_objects)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
