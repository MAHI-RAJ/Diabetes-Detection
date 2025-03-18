import pickle
import numpy as np

# Load the trained model
with open("men_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load the scaler
with open("men_scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def predict_disease(input_data):
    """
    Function to predict disease based on input features.
    :param input_data: List of features (Men: [[glucose, bp, skin_thickness, bmi, dpf, age]] or 
                                           Women: [[pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age]])
    :return: Prediction result
    """
    # Convert input into a NumPy array and reshape
    input_data_array = np.array(input_data).reshape(1, -1)

    # Transform input using the trained scaler
    input_data_scaled = scaler.transform(input_data_array)

    # Make prediction
    prediction = model.predict(input_data_scaled)

    # Return a readable result
    return "Disease Detected" if prediction[0] == 1 else "No Disease Detected"
