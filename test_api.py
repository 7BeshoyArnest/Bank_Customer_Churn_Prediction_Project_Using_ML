{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ee838eb3-9573-4f53-b0b1-3799b4eef56b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Exited': 1}\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "url = \"http://127.0.0.1:5000/predict\"\n",
    "\n",
    "data = {\n",
    "    \"CustomerId\": 15634602,\n",
    "    \"CreditScore\": 619,\n",
    "    \"Geography\": 1,    # Use numerical values if model expects encoded ones\n",
    "    \"Gender\": 1,       # Example: 1 = Male, 0 = Female\n",
    "    \"Age\": 42,\n",
    "    \"Tenure\": 2,\n",
    "    \"Balance\": 0.0,\n",
    "    \"NumOfProducts\": 1,\n",
    "    \"HasCrCard\": 1,\n",
    "    \"IsActiveMember\": 1,\n",
    "    \"EstimatedSalary\": 101348.88\n",
    "}\n",
    "\n",
    "response = requests.post(url, json=data)\n",
    "print(response.json())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "031cc0f9-2328-400e-80c8-035752c023be",
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
