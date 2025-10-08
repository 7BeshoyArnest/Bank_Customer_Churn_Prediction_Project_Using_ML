from flask import Flask, request, jsonify
import joblib
import numpy as np
from flasgger import Swagger

# Initialize Flask app
app = Flask(__name__)
swagger = Swagger(app)

# Load the trained model
model = joblib.load('churn_predict_model')

@app.route('/')
def home():
    return "✅ Bank Customer Churn Prediction API is running! Visit /apidocs for Swagger UI."

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict whether a customer will churn
    ---
    tags:
      - Bank Churn Prediction
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - CreditScore
            - Geography
            - Gender
            - Age
            - Tenure
            - Balance
            - NumOfProducts
            - HasCrCard
            - IsActiveMember
            - EstimatedSalary
          properties:
            CreditScore:
              type: number
              example: 619
            Geography:
              type: string
              example: "France"
            Gender:
              type: string
              example: "Male"
            Age:
              type: number
              example: 42
            Tenure:
              type: number
              example: 2
            Balance:
              type: number
              example: 0.0
            NumOfProducts:
              type: number
              example: 1
            HasCrCard:
              type: number
              example: 1
            IsActiveMember:
              type: number
              example: 1
            EstimatedSalary:
              type: number
              example: 101348.88
    responses:
      200:
        description: Prediction result
        schema:
          type: object
          properties:
            Exited:
              type: integer
              example: 0
    """
    data = request.get_json()

    # One-hot encode Geography
    geo_germany = 1 if data['Geography'].lower() == 'germany' else 0
    geo_spain = 1 if data['Geography'].lower() == 'spain' else 0

    # Encode Gender
    gender_male = 1 if data['Gender'].lower() == 'male' else 0

    # Arrange features exactly as the model was trained
    features = np.array([[
        data['CreditScore'],
        data['Age'],
        data['Tenure'],
        data['Balance'],
        data['NumOfProducts'],
        data['HasCrCard'],
        data['IsActiveMember'],
        data['EstimatedSalary'],
        geo_germany,
        geo_spain,
        gender_male
    ]])

    # Make prediction
    prediction = model.predict(features)

    return jsonify({'Exited': int(prediction[0])})


if __name__ == "__main__":
    app.run(port=5000, debug=True)




# from flask import Flask, request, jsonify
# import joblib
# import numpy as np

# # Initialize Flask app
# app = Flask(__name__)

# # Load the trained model
# model = joblib.load('churn_predict_model')

# @app.route('/')
# def home():
#     return "✅ Bank Customer Churn Prediction API is running!"

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get JSON data from request
#     data = request.get_json()

#     # One-hot encode Geography (France is baseline → both 0)
#     geo_germany = 1 if data['Geography'].lower() == 'germany' else 0
#     geo_spain = 1 if data['Geography'].lower() == 'spain' else 0

#     # Encode Gender
#     gender_male = 1 if data['Gender'].lower() == 'male' else 0

#     # Arrange features in the same order the model was trained
#     features = np.array([[
#         data['CreditScore'],
#         data['Age'],
#         data['Tenure'],
#         data['Balance'],
#         data['NumOfProducts'],
#         data['HasCrCard'],
#         data['IsActiveMember'],
#         data['EstimatedSalary'],
#         geo_germany,
#         geo_spain,
#         gender_male
#     ]])

#     # Make prediction
#     prediction = model.predict(features)

#     # Return prediction as JSON
#     return jsonify({'Exited': int(prediction[0])})


# if __name__ == "__main__":
#     app.run(port=5000, debug=True)
