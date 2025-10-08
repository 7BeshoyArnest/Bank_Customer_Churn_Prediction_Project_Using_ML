from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('churn_predict_model')

@app.route('/')
def home():
    return "✅ Bank Customer Churn Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from request
    data = request.get_json()

    # Extract features in the correct order
    features = np.array([[
        data['CustomerId'], 
        data['CreditScore'], 
        data['Geography'], 
        data['Gender'], 
        data['Age'], 
        data['Tenure'], 
        data['Balance'], 
        data['NumOfProducts'], 
        data['HasCrCard'], 
        data['IsActiveMember'], 
        data['EstimatedSalary']
    ]])

    # Make prediction
    prediction = model.predict(features)

    # Return prediction as JSON
    return jsonify({'Exited': int(prediction[0])})

if __name__ == "__main__":
    app.run(port=5000, debug=True)

