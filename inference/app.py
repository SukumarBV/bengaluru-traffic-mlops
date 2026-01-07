from fastapi import FastAPI
import joblib
import pandas as pd
import os
import subprocess

app = FastAPI(title="Bengaluru Traffic Congestion Predictor")

@app.get("/")
def home():
    return {"status": "Traffic AI running"}

MODEL_PATH = "model.pkl"

# Auto train if model not found (cloud-safe)
if not os.path.exists(MODEL_PATH):
    subprocess.call(["python", "training/train.py"])

model = joblib.load(MODEL_PATH)

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return {"predicted_vehicle_count": int(prediction)}
