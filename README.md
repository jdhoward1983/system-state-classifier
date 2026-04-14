# System State Classifier

A lightweight machine learning prototype for classifying system health states using synthetic telemetry data. This project demonstrates an end-to-end, reproducible ML pipeline designed for structured system monitoring and future integration into operational environments.

---

## Project Overview

Modern systems often degrade before outright failure, but those early warning signs can be difficult to detect consistently. This project builds a baseline machine learning pipeline that classifies system states as **normal** or **degraded** using telemetry-style inputs.

The goal is not just model performance, but demonstrating a **reproducible, modular ML workflow** suitable for constrained or security-sensitive environments.

---

## Problem Statement

Operators and engineers need a scalable way to assess system health using measurable indicators such as:

- CPU utilization  
- Memory usage  
- Network latency  
- Packet loss  
- Error rates  

Manual analysis does not scale and may miss subtle degradation patterns. This project addresses that gap by implementing a classification pipeline that can support automated monitoring and anomaly detection.

---

## Pipeline Overview

This project implements a simple, end-to-end machine learning pipeline for system state classification.

**Data Generation**  
Synthetic telemetry is generated to simulate normal and degraded system behavior.

**Model Training**  
Baseline models (Logistic Regression and Random Forest) are trained using scikit-learn.

**Model Evaluation**  
Performance is evaluated using precision, recall, F1-score, and accuracy.

**Prediction**  
The trained model classifies new system states based on telemetry inputs.

---

## Repository Structure
system-state-classifier/
│
├── Data/
│ └── Raw/
│ └── system_state_data.csv
│
├── SRC/
│ ├── make_data.py
│ ├── train.py
│ ├── evaluate.py
│ └── predict.py
│
├── README.md
├── requirements.txt
└── .gitignore


---

## Current Features

- Synthetic telemetry dataset for controlled testing
- End-to-end ML pipeline (data → training → evaluation → prediction)
- Modular Python scripts for each pipeline stage
- Reproducible environment via `requirements.txt`
- Baseline performance metrics for model validation

---

## Technologies Used

- Python  
- scikit-learn  
- pandas  
- NumPy  
- joblib  

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/jdhoward1983/system-state-classifier.git
cd system-state-classifier

### 2. Create and activate virtual environment (Windows)

python -m venv .venv
.venv\Scripts\Activate.ps1

### 3. Install dependencies

pip install -r requirements.txt

### 4. Generate Data Set

python SRC/make_data.py

### 5. Train Model

python SRC/train.py

### 6. Evaluate model

python SRC/evaluate.py

### 7. Run predictions

python SRC/predict.py

Example Use Case

This project serves as a baseline for:

system health monitoring
anomaly detection pipelines
degraded-state alerting
integration with telemetry systems
future real-time monitoring tools
Results

This project establishes a baseline classification pipeline. Model performance metrics are generated via the evaluation script and can be expanded with:

confusion matrices
visualizations
real-time data ingestion
API-based deployment
Future Improvements
Integration with real telemetry sources
Expanded model comparison
Visualization of model performance
API or local service deployment
Drift detection and retraining pipeline
Enhanced documentation for reproducibility
Why This Project Matters

This project demonstrates the ability to:

Define a real-world problem
Build an end-to-end ML pipeline
Structure code for reproducibility
Document technical workflows clearly
Prepare systems for operational AI integration

Author

Jeremy D. Howard

License

This project is licensed under the MIT License.
