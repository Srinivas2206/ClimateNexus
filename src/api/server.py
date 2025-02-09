from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import keras.losses

# Register custom objects
custom_objects = {"mse": keras.losses.MeanSquaredError()}

# Load the fixed model
MODEL_PATH = "models/co2_lstm_fixed.h5"
model = load_model(MODEL_PATH, custom_objects=custom_objects)

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "CO2 Forecast API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        input_data = np.array(data["features"]).reshape(1, -1, 1)  # Ensure correct input shape
        prediction = model.predict(input_data)
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
