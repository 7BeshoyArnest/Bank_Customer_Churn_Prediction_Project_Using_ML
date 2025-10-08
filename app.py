{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3dededd6-ff20-42f7-8684-de0017839913",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [08/Oct/2025 16:07:07] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "# Initialize Flask app\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Load the trained model\n",
    "model = joblib.load('churn_predict_model')\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return \"✅ Bank Customer Churn Prediction API is running!\"\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    # Get JSON data from request\n",
    "    data = request.get_json()\n",
    "\n",
    "    # Extract features in the correct order\n",
    "    features = np.array([[\n",
    "        data['CustomerId'], \n",
    "        data['CreditScore'], \n",
    "        data['Geography'], \n",
    "        data['Gender'], \n",
    "        data['Age'], \n",
    "        data['Tenure'], \n",
    "        data['Balance'], \n",
    "        data['NumOfProducts'], \n",
    "        data['HasCrCard'], \n",
    "        data['IsActiveMember'], \n",
    "        data['EstimatedSalary']\n",
    "    ]])\n",
    "\n",
    "    # Make prediction\n",
    "    prediction = model.predict(features)\n",
    "\n",
    "    # Return prediction as JSON\n",
    "    return jsonify({'Exited': int(prediction[0])})\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(port=5000, debug=True, use_reloader=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc1c9a89-2c63-4d8f-8481-481dcebc3faf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (tf_env)",
   "language": "python",
   "name": "tf_env"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.21"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
