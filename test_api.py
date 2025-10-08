import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "CustomerId": 15634602,
    "CreditScore": 619,
    "Geography": 1,    # مثال رقمي بدل النص لو كنت مش عامل OneHotEncoding
    "Gender": 1,       # مثلاً 1=Male, 0=Female
    "Age": 42,
    "Tenure": 2,
    "Balance": 0.0,
    "NumOfProducts": 1,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 101348.88
}

response = requests.post(url, json=data)
print(response.json())
