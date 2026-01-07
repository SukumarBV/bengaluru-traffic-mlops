# 🚦 Bengaluru Smart City Traffic Congestion AI

<p align="center">
  <b>Production-Grade MLOps System | Live Smart City Intelligence</b><br>
  🌐 <a href="https://bengaluru-traffic-mlops.onrender.com">Live API</a> • ⚙️ CI/CD • 📊 MLflow • 🤖 Auto-Retraining
</p>

<p align="center">
  <img src="https://img.shields.io/badge/MLOps-Production%20Ready-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/SmartCity-Bengaluru-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Deployment-Live-success?style=for-the-badge">
</p>

---

## 🧠 What This Is

A **live smart-city AI engine** that predicts real-time traffic congestion in Bengaluru and automatically retrains itself when traffic patterns change.

This system simulates how Google Maps, Ola, Uber and Smart City traffic control platforms manage city-scale traffic intelligence.

---

## 🏙 Real-World Impact

| Problem | Solution |
|-------|--------|
| Traffic congestion | Predict congestion in advance |
| Changing patterns | Drift detection |
| Manual retraining | Automated retraining |
| Static models | Self-healing ML system |

---

## 🏗 System Architecture

```mermaid
graph TD
A[Live Traffic Input] --> B[FastAPI ML Service]
B --> C[Congestion Prediction]
C --> D[Drift Monitor]
D -->|Drift Detected| E[Auto Retraining]
E --> F[CI/CD Deployment]
F --> B

🛠 Tech Stack
| Layer      | Tech                   |
| ---------- | ---------------------- |
| ML         | RandomForest           |
| API        | FastAPI                |
| Tracking   | MLflow                 |
| CI/CD      | GitHub Actions         |
| Monitoring | Drift Detection Engine |
| Cloud      | Render                 |

🌐 Live API Demo

Endpoint

POST /predict


Sample Input

{
  "Junction": 1,
  "hour": 18,
  "day": 6,
  "month": 12
}


Output

{
  "predicted_vehicle_count": 41
}

🔁 Self-Healing Logic
| Condition        | Action            |
| ---------------- | ----------------- |
| MAE increases    | Drift detected    |
| Drift detected   | Retrain triggered |
| New model better | Auto deployed     |

👨‍💻 Author

Sukumar BV
3rd Year AIML Student
🔗 https://github.com/SukumarBV
