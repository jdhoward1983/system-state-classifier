# System State Classifier v1

## Problem
Manual review of structured system indicators can be inconsistent and slow.

## Solution
This project trains a supervised machine learning model to classify system states as normal or degraded using synthetic tabular data.

## Why AI
A trained classifier can identify multi-variable patterns more consistently than ad hoc manual review or single-threshold checks.

## Tools
- Python
- pandas
- scikit-learn
- matplotlib
- joblib

## Current Status
- Synthetic dataset generation complete
- Baseline model training complete
- Logistic Regression and Random Forest compared

## Next Steps
- Add confusion matrix and plots
- Add formal evaluation script
- Add simple local dashboard