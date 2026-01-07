🚦 Bengaluru Smart City Traffic Congestion Prediction System (MLOps)

Live API:
https://bengaluru-traffic-mlops.onrender.com

An end-to-end production-style MLOps system that predicts real-time traffic congestion across Bengaluru city using machine learning, automated monitoring, retraining, and CI/CD deployment.

This project simulates how Smart City platforms, Google Maps, Ola, and Uber manage city-scale traffic intelligence.

🧠 Problem Statement

Urban traffic congestion causes huge productivity loss and commuter frustration.
Smart cities require intelligent systems that can:

• Predict traffic congestion in advance
• Automatically adapt to changing traffic patterns
• Remain accurate without manual retraining

This project solves that by building a self-healing city traffic AI system.

🏗 System Architecture
Live Traffic Input → FastAPI Prediction Service → Congestion Prediction
                                ↓
                        Drift Monitoring Engine
                                ↓
                    Automated Retraining (CI/CD Pipeline)
                                ↓
                     Updated Model Deployed Automatically

🛠 Tech Stack
Layer	Technology
ML Model	Random Forest Regressor
API	FastAPI
MLOps Tracking	MLflow
CI/CD	GitHub Actions
Monitoring	Custom Drift Detection
Deployment	Render Cloud
Dataset	Bengaluru Government Traffic Dataset
🚀 Key Features

✔ Live public prediction API
✔ Smart city–scale congestion forecasting
✔ Automated drift detection
✔ Automatic retraining when accuracy drops
✔ Continuous integration & deployment
✔ Cloud-hosted production service

🌐 Live API Usage

Endpoint

POST /predict


Request

{
  "Junction": 2,
  "hour": 18,
  "day": 6,
  "month": 12
}


Response

{
  "predicted_vehicle_count": 39
}

🔁 Auto Retraining Logic
Condition	Action
Prediction MAE increases	Drift detected
Drift detected	Model retrains automatically
New model performs better	Deployed via CI/CD

👨‍💻 Author

Sukumar BV
3rd Year AIML Student
GitHub: https://github.com/SukumarBV
