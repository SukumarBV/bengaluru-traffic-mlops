import streamlit as st
import requests
import pandas as pd
import time

TIME_COMPRESSION = 10   # less compression → more variation
MAX_SLEEP = 8           # allow longer visible gaps


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
if "history" not in st.session_state:
    st.session_state.history = []

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
    st.session_state.history.append({
        "DateTime": row["DateTime"],
        "Junction": payload["Junction"],
        "Predicted": result["predicted_vehicle_count"],
        "Observed": int(row["Vehicles"]),
        "Congestion": result["congestion_level"]
    })

    st.session_state.history = st.session_state.history[-30:]

else:
    st.error("Backend error")


# Advance pointer
# Compute time-aware sleep
if st.session_state.idx < len(data) - 1:
    current_time = row["DateTime"]
    next_time = data.iloc[st.session_state.idx + 1]["DateTime"]

    delta_seconds = (next_time - current_time).total_seconds()
    sleep_time = min(delta_seconds / TIME_COMPRESSION, MAX_SLEEP)
else:
    sleep_time = 1

# Advance pointer
st.session_state.idx += 1
if st.session_state.idx >= len(data):
    st.session_state.idx = 0
st.caption(f"Replay sleep: {round(sleep_time, 2)} seconds")

time.sleep(max(sleep_time, 0.1))
st.rerun()

st.divider()
st.subheader("Recent Traffic Trend (Last 30 Events)")

if len(st.session_state.history) >= 2:
    hist_df = pd.DataFrame(st.session_state.history)

    st.line_chart(
        hist_df.set_index("DateTime")[["Predicted", "Observed"]],
        height=300
    )

    with st.expander("View recent data"):
        st.dataframe(hist_df, use_container_width=True)
else:
    st.info("Waiting for more data points…")
