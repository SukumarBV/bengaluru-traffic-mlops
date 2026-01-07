import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("data/bangalore_traffic.csv")

df["DateTime"] = pd.to_datetime(df["DateTime"])
df["hour"] = df["DateTime"].dt.hour
df["day"] = df["DateTime"].dt.day
df["month"] = df["DateTime"].dt.month
df = df.drop(["DateTime", "ID"], axis=1)

X = pd.get_dummies(df.drop("Vehicles", axis=1))
y = df["Vehicles"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "model_cloud.pkl", compress=3)
