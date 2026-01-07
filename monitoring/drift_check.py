import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error
import subprocess

model = joblib.load("model.pkl")
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
