import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import os

def train_co2_lstm():
    # Check if processed data exists
    data_path = "data/processed/merged_climate_data.csv"
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Processed data not found at {data_path}. Run data_processing.py first.")
    
    # Load data
    data = pd.read_csv(data_path)
    co2 = data['co2'].values.reshape(-1, 1)
    
    # Scale data
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(co2)
    
    # Prepare sequences for LSTM
    X, y = [], []
    for i in range(3, len(scaled)):
        X.append(scaled[i-3:i])
        y.append(scaled[i])
    
    X_train, y_train = np.array(X), np.array(y)
    
    # Build LSTM model
    model = Sequential([
        LSTM(50, activation='relu', input_shape=(3, 1)),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    
    # Train model
    print("Training LSTM model...")
    model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=1)
    
    # Save model
    model.save("models/co2_lstm.h5")
    print("Model saved to models/co2_lstm.h5")

# Call the function
if __name__ == "__main__":
    train_co2_lstm()