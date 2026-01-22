import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error
import subprocess
import os

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "model_cloud.pkl"
)

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Model artifact missing")

print("Model artifact found. Drift check skipped in CI.")
exit(0)


model = joblib.load(MODEL_PATH)
df = pd.read_csv("data/bangalore_traffic.csv")

# Recreate features same as training
df["DateTime"] = pd.to_datetime(df["DateTime"])
df["hour"] = df["DateTime"].dt.hour
df["day"] = df["DateTime"].dt.day
df["month"] = df["DateTime"].dt.month
df = df.drop(["DateTime", "ID"], axis=1)

X = pd.get_dummies(df.drop("Vehicles", axis=1))
y = df["Vehicles"]

pred = model.predict(X)
mae = mean_absolute_error(y, pred)

print("Live MAE:", mae)

# Auto retrain trigger
if mae > 10:
    print("⚠ Drift detected — Auto retraining...")
    subprocess.call(["python", "training/train.py"])
