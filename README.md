# Urban Mobility MLOps Platform
### (Bengaluru Traffic Case Study)

**Production-Grade MLOps Platform for Urban Congestion Prediction**  
Demonstrated using Bengaluru traffic data

[**Deployed API**](#live-api-demo) • [CI/CD](#cicd-pipeline) • [MLflow](#experiment-tracking) • [Drift Monitoring](#drift-monitoring)

---

## Overview

This project is a **production-oriented MLOps platform** designed for predicting and monitoring urban traffic congestion. The system is data-source agnostic and can be adapted to any city given appropriate traffic data.

**Bengaluru traffic data** is used as a case study to demonstrate how such a platform would be trained, deployed, monitored, and maintained in a real-world environment.

> **Note:** The goal of this project is not to control live traffic, but to showcase how city-scale mobility ML systems are architected in production.

---

## What Problem This Addresses

Urban traffic systems face challenges such as:

| Challenge | Platform Capability |
|-----------|---------------------|
| Non-stationary traffic patterns | Drift detection |
| Model performance degradation | Automated retraining |
| Manual ML deployments | CI/CD-driven updates |
| Lack of observability | Experiment tracking & metrics |

This platform demonstrates how these challenges can be handled using modern MLOps practices.

---

## Platform Architecture
```
┌─────────────────────┐
│ Live Traffic Input  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ FastAPI ML Service  │◄─────────┐
└──────────┬──────────┘          │
           │                      │
           ▼                      │
┌─────────────────────┐          │
│Congestion Prediction│          │
└──────────┬──────────┘          │
           │                      │
           ▼                      │
┌─────────────────────┐          │
│   Drift Monitor     │          │
└──────────┬──────────┘          │
           │                      │
     Drift Detected               │
           │                      │
           ▼                      │
┌─────────────────────┐          │
│  Auto Retraining    │          │
└──────────┬──────────┘          │
           │                      │
           ▼                      │
┌─────────────────────┐          │
│ CI/CD Deployment    │──────────┘
└─────────────────────┘
```

### Flow Description

1. **Live Traffic Input** → Real-time traffic data fed into the system
2. **FastAPI ML Service** → REST API serving ML predictions
3. **Congestion Prediction** → Model inference on incoming data
4. **Drift Monitor** → Continuous monitoring of prediction quality
5. **Auto Retraining** → Triggered when drift is detected
6. **CI/CD Deployment** → Automated model deployment pipeline
7. **Feedback Loop** → Updated model replaces the current service

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| ML Model | Random Forest |
| API | FastAPI |
| Tracking | MLflow |
| CI/CD | GitHub Actions |
| Monitoring | Drift Detection Engine |
| Cloud | Render |

---

## Live API Demo --> https://bengaluru-traffic-mlops.onrender.com/

### Endpoint
```
POST /predict
```

### Sample Input
```json
{
  "Junction": 1,
  "hour": 18,
  "day": 6,
  "month": 12
}
```

### Output
```json
{
  "predicted_vehicle_count": 41
}
```

---

## Self-Healing Logic

| Condition | Action |
|-----------|--------|
| MAE increases | Drift detected |
| Drift detected | Retraining triggered |
| New model performs better | Auto deployed |

The platform automatically detects model performance degradation and triggers retraining without manual intervention, ensuring the system remains accurate over time.

---

## Case Study: Bengaluru Traffic Data

Bengaluru traffic data is used as a demonstration dataset to validate the platform's behavior. The same pipeline can be applied to other cities or mobility datasets with minimal changes.

**Key Features:**
- Junction-level traffic prediction
- Time-based feature engineering (hour, day, month)
- Real-world traffic pattern learning
- Scalable to multi-city deployments

---

## Author

**Sukumar BV**  
3rd Year AIML Student  
[https://github.com/SukumarBV](https://github.com/SukumarBV)

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
