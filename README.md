🏦 Bank Customer Churn Prediction
This project uses machine learning to predict customer churn in a bank. By analyzing customer data, the model determines which clients are likely to leave the bank, helping financial institutions reduce churn and retain valuable customers.

📌 Project Overview
Churn prediction is a crucial task in the banking industry, as acquiring new customers is significantly more costly than retaining existing ones. This project leverages supervised machine learning techniques to:

Understand customer behaviors

Identify patterns leading to churn

Predict whether a customer is likely to leave the bank

🧠 Machine Learning Models Used
Logistic Regression

Random Forest Classifier

Support Vector Machines (SVM)

XGBoost Classifier

The model performance is evaluated using classification metrics such as Accuracy, Precision, Recall, F1 Score, and ROC AUC.

📂 Dataset
The dataset includes information on bank customers such as:

Geography

Gender

Age

Tenure

Balance

Number of Products

Credit Score

Estimated Salary

Exited (target: 1 if the customer left, 0 otherwise)

Dataset Source: Kaggle - Churn Modeling

📊 Exploratory Data Analysis (EDA)
Checked for missing values and outliers

Explored correlation between features

Visualized churn distribution based on key attributes like age, balance, geography, and number of products

🛠️ Preprocessing
Label Encoding & One-Hot Encoding

Feature Scaling using StandardScaler

Data Splitting (Train-Test)

Feature Selection for performance improvement

✅ Evaluation Metrics
Each model's performance is measured using:

Confusion Matrix

Accuracy Score

ROC Curve

Classification Report (Precision, Recall, F1)

🔍 Key Findings
Customers with high balance and low product usage were more likely to churn

Age and geography significantly impacted churn

The Random Forest and XGBoost classifiers showed the best performance

📈 Results
The best model (XGBoost Classifier) achieved:

Accuracy: ~86%

ROC AUC: ~84%

Strong precision-recall balance
