from fastapi import FastAPI
import joblib
import pandas as pd
import os

app = FastAPI(title="Bengaluru Traffic Congestion Predictor")

@app.get("/")
def home():
    return {"status": "Traffic AI running"}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model_cloud.pkl")
model = joblib.load(MODEL_PATH)

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return {"predicted_vehicle_count": int(prediction)}
