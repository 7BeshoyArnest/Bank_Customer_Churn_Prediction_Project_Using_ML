import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "CreditScore": 700,
    "Geography": "Germany",
    "Gender": "Male",
    "Age": 35,
    "Tenure": 5,
    "Balance": 25000.0,
    "NumOfProducts": 2,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 90000.0
}

response = requests.post(url, json=data)
print(response.json())

