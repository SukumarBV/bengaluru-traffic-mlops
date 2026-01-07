from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title="Bengaluru Traffic Congestion Predictor")

@app.get("/")
def home():
    return {"status": "Traffic AI running"}


import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model_small.pkl")
model = joblib.load(MODEL_PATH)

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return {"predicted_vehicle_count": int(prediction)}
