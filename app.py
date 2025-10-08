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
    return " Bank Customer Churn Prediction API is running! Visit /apidocs for Swagger UI."


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

    # List of required fields
    required_fields = [
        'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure',
        'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary'
    ]

    # Check for missing fields
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

        # Check for empty or null values
        if data[field] is None or (isinstance(data[field], str) and not data[field].strip()):
            return jsonify({"error": f"Field '{field}' cannot be empty"}), 400

    # Type validation
    numeric_fields = [
        'CreditScore', 'Age', 'Tenure', 'Balance',
        'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary'
    ]

    for field in numeric_fields:
        if not isinstance(data[field], (int, float)):
            return jsonify({"error": f"Field '{field}' must be a number"}), 400

    if not isinstance(data['Geography'], str):
        return jsonify({"error": "Field 'Geography' must be a string"}), 400
    if not isinstance(data['Gender'], str):
        return jsonify({"error": "Field 'Gender' must be a string"}), 400

    # Logical range validation
    if not (300 <= data['CreditScore'] <= 850):
        return jsonify({"error": "CreditScore must be between 300 and 850"}), 400
    if not (18 <= data['Age'] <= 100):
        return jsonify({"error": "Age must be between 18 and 100"}), 400
    if not (0 <= data['Tenure'] <= 10):
        return jsonify({"error": "Tenure must be between 0 and 10"}), 400
    if not (0 <= data['Balance']):
        return jsonify({"error": "Balance cannot be negative"}), 400
    if not (1 <= data['NumOfProducts'] <= 4):
        return jsonify({"error": "NumOfProducts must be between 1 and 4"}), 400
    if data['HasCrCard'] not in [0, 1]:
        return jsonify({"error": "HasCrCard must be 0 or 1"}), 400
    if data['IsActiveMember'] not in [0, 1]:
        return jsonify({"error": "IsActiveMember must be 0 or 1"}), 400

    # Validate categorical values
    valid_geos = ['france', 'germany', 'spain']
    valid_genders = ['male', 'female']

    if data['Geography'].lower() not in valid_geos:
        return jsonify({"error": f"Invalid Geography. Must be one of {valid_geos}"}), 400
    if data['Gender'].lower() not in valid_genders:
        return jsonify({"error": f"Invalid Gender. Must be one of {valid_genders}"}), 400

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

    #  Make prediction safely
    try:
        prediction = model.predict(features)
    except Exception as e:
        return jsonify({"error": f"Model prediction failed: {str(e)}"}), 500

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
#     return " Bank Customer Churn Prediction API is running!"

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
