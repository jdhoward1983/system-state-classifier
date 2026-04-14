# System Design Overview

## Purpose

This document outlines the design considerations for the System State Classifier project, focusing on reproducibility, modularity, and future operational integration.

---

## Architecture Overview

The system follows a modular pipeline architecture:

1. Data Generation Layer
2. Model Training Layer
3. Evaluation Layer
4. Prediction Layer

Each stage is implemented as an independent script to support testing, debugging, and future scaling.

---

## Design Principles

### 1. Modularity
Each stage of the pipeline is separated into distinct scripts:
- `make_data.py`
- `train.py`
- `evaluate.py`
- `predict.py`

This allows individual components to be modified or replaced without affecting the entire system.

### 2. Reproducibility
- Controlled dataset generation
- Explicit dependency management (`requirements.txt`)
- Deterministic pipeline structure

### 3. Simplicity
Baseline models are used intentionally to establish a clear performance benchmark before introducing complexity.

### 4. Portability
The system is designed to run in local or constrained environments without external dependencies such as cloud services.

---

## Data Design

The dataset simulates telemetry inputs, including:

- CPU utilization
- Memory usage
- Network latency
- Packet loss
- Error rates

Labels classify system state as:
- Normal
- Degraded

---

## Model Selection

Initial models:
- Logistic Regression
- Random Forest

These models were selected due to:
- Interpretability
- Low computational overhead
- Suitability for baseline classification tasks

---

## Limitations

- Synthetic data may not reflect real-world complexity
- No real-time ingestion pipeline
- No drift detection or retraining mechanism

---

## Future Architecture Expansion

- Real telemetry ingestion pipeline
- Streaming data processing
- REST API or local service deployment
- Integration with monitoring dashboards
- Model versioning and lifecycle management
