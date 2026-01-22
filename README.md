# Urban Mobility MLOps Platform  
### (Bengaluru Traffic Case Study)

<p align="center">
  <b>Production-Grade MLOps Platform for Urban Congestion Prediction</b><br>
  Demonstrated using Bengaluru traffic data
</p>

<p align="center">
  <a href="https://bengaluru-traffic-mlops.onrender.com">Deployed API</a> • CI/CD • MLflow • Drift Monitoring
</p>

---

## Overview

This project is a **production-oriented MLOps platform** designed for predicting and monitoring urban traffic congestion.  
The system is **data-source agnostic** and can be adapted to any city given appropriate traffic data.

Bengaluru traffic data is used as a **case study** to demonstrate how such a platform would be trained, deployed, monitored, and maintained in a real-world environment.

The goal of this project is **not to control live traffic**, but to showcase how city-scale mobility ML systems are architected in production.

---

## What Problem This Addresses

Urban traffic systems face challenges such as:

| Challenge | Platform Capability |
|--------|-------------------|
| Non-stationary traffic patterns | Drift detection |
| Model performance degradation | Automated retraining |
| Manual ML deployments | CI/CD-driven updates |
| Lack of observability | Experiment tracking & metrics |

This platform demonstrates how these challenges can be handled using modern MLOps practices.

---

## Platform Architecture

```mermaid
graph TD
A[Traffic Dataset / Data Source] --> B[Training Pipeline]
B --> C[Trained Model Artifact]
C --> D[FastAPI Inference Service]
D --> E[Prediction Outputs]
E --> F[Drift Monitoring]
F -->|Drift Detected| B

---

##  Tech Stack

| Layer | Technology |
|-----|----------|
| ML Model | Random Forest |
| API | FastAPI |
| Tracking | MLflow |
| CI/CD | GitHub Actions |
| Monitoring | Drift Detection Engine |
| Cloud | Render |

---

##  Live API Demo

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

##  Self-Healing Logic

| Condition | Action |
|---------|------|
| MAE increases | Drift detected |
| Drift detected | Retraining triggered |
| New model performs better | Auto deployed |

---

## Case Study: Bengaluru Traffic Data

Bengaluru traffic data is used as a demonstration dataset to validate the platform’s behavior.
The same pipeline can be applied to other cities or mobility datasets with minimal changes.

---

##  Author

**Sukumar BV**  
3rd Year AIML Student  
🔗 https://github.com/SukumarBV
