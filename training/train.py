import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib
import mlflow

df = pd.read_csv("data/bangalore_traffic.csv")

# Convert time into ML features
df["DateTime"] = pd.to_datetime(df["DateTime"])
df["hour"] = df["DateTime"].dt.hour
df["day"] = df["DateTime"].dt.day
df["month"] = df["DateTime"].dt.month

# Drop useless columns
df = df.drop(["DateTime", "ID"], axis=1)

X = df.drop("Vehicles", axis=1)
y = df["Vehicles"]

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

with mlflow.start_run():
    model = RandomForestRegressor(n_estimators=150)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)

    print("Traffic Prediction MAE:", mae)
    mlflow.log_metric("MAE", mae)

    joblib.dump(model, "model.pkl")
