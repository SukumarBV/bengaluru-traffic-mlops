from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title="Bengaluru Traffic Congestion Predictor")

model = joblib.load("model.pkl")

# These must match training columns
FEATURE_COLUMNS = ['Junction', 'hour', 'day', 'month']

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    df = df[FEATURE_COLUMNS]
    prediction = model.predict(df)[0]
    return {"predicted_vehicle_count": int(prediction)}
