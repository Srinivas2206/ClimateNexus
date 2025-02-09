from tensorflow.keras.models import load_model

# Load model without compiling
model = load_model("models/co2_lstm.h5", compile=False)

# Save the model again to avoid serialization issues
model.save("models/co2_lstm_fixed.h5")
print("✅ Model saved successfully without compilation!")
