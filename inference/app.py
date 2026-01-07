from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title="Bengaluru Traffic Congestion Predictor")

@app.get("/")
def home():
    return {"status": "Traffic AI running"}

model = joblib.load("model_small.pkl")

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return {"predicted_vehicle_count": int(prediction)}
