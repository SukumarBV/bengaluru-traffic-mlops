import streamlit as st
import requests
import pandas as pd
import time

API_URL = "https://Sukumarbv-bengaluru-traffic-api.hf.space"

st.set_page_config(
    page_title="Urban Mobility MLOps",
    layout="wide"
)

st.title("Urban Mobility – Live Traffic Simulation")

# Load data once
@st.cache_data
def load_data():
    df = pd.read_csv("data/bangalore_traffic.csv")
    df["DateTime"] = pd.to_datetime(df["DateTime"])
    df["hour"] = df["DateTime"].dt.hour
    df["day"] = df["DateTime"].dt.dayofweek + 1
    df["month"] = df["DateTime"].dt.month
    return df

data = load_data()

# Initialize pointer
if "idx" not in st.session_state:
    st.session_state.idx = 0

st.subheader("Current Traffic State (Simulated Live)")

row = data.iloc[st.session_state.idx]

payload = {
    "Junction": int(row["Junction"]),
    "hour": int(row["hour"]),
    "day": int(row["day"]),
    "month": int(row["month"])
}


response = requests.post(f"{API_URL}/predict", json=payload)

if response.status_code == 200:
    result = response.json()

    col1, col2, col3 = st.columns(3)

    col1.metric("Vehicle Count", result["predicted_vehicle_count"])
    col2.metric("Congestion Level", result["congestion_level"])
    col3.metric("Severity Score", result["severity_score"])

    st.caption(
        f"Junction {payload['Junction']} | "
        f"Time {payload['hour']}:00 | "
        f"Row {st.session_state.idx}"
    )
else:
    st.error("Backend error")

# Advance pointer
st.session_state.idx += 1
if st.session_state.idx >= len(data):
    st.session_state.idx = 0

# Auto-refresh
time.sleep(3)
st.rerun()

