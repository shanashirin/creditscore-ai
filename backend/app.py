import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("../model/credit_risk_model.pkl")
scaler = joblib.load("../model/scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    features = np.array([
        data["Age"],
        data["CreditAmount"],
        data["Duration"]
    ]).reshape(1,-1)

    features = scaler.transform(features)

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0][1]

    risk = "High Risk" if prediction == 1 else "Low Risk"

    return jsonify({
        "risk": risk,
        "probability": round(probability*100,2)
    })


if __name__ == "__main__":
    app.run(debug=True)