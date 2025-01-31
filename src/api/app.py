from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
api = Api(app)

# Load the Keras model
model = load_model("models/co2_lstm.h5")

@api.route('/predict')
class Predict(Resource):
    def post(self):
        # Get input data from the request
        data = request.json['data']
        
        # Convert input data to a numpy array and reshape for LSTM
        input_data = np.array(data).reshape(1, 3, 1)
        
        # Make a prediction
        prediction = model.predict(input_data)
        
        # Return the prediction as JSON
        return {'prediction': float(prediction[0][0])}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)