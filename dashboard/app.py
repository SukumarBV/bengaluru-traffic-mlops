import streamlit as st
import requests

st.set_page_config(
    page_title="Urban Mobility MLOps",
    layout="wide"
)

st.title("Urban Mobility MLOps Platform")

st.header("Live Traffic Prediction")

API_URL = "https://Sukumarbv-bengaluru-traffic-api.hf.space"


col1, col2, col3, col4 = st.columns(4)

junction = col1.selectbox("Junction", [1, 2, 3, 4])
hour = col2.slider("Hour", 0, 23, 18)
day = col3.slider("Day", 1, 7, 6)
month = col4.slider("Month", 1, 12, 12)

if st.button("Predict"):
    response = requests.post(
        f"{API_URL}/predict",
        json={
            "Junction": junction,
            "hour": hour,
            "day": day,
            "month": month
        }
    )

    if response.status_code == 200:
        st.metric(
            "Predicted Vehicle Count",
            response.json()["predicted_vehicle_count"]
        )
    else:
        st.error("Backend error")
