import streamlit as st

st.set_page_config(
    page_title="Urban Mobility MLOps",
    layout="wide"
)

st.title("Urban Mobility MLOps Platform")

st.markdown("""
This dashboard will show:
- Live traffic predictions
- Drift monitoring
- Model information
- System health
""")
