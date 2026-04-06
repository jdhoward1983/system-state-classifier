from pathlib import Path
import json

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split


def evaluate_model(name: str, model, x_test, y_test) -> dict:
    y_pred = model.predict(x_test)
    return {
        "model": name,
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
    }


def main() -> None:
    data_path = Path("data/raw/system_state_data.csv")
    df = pd.read_csv(data_path)

    x = df.drop(columns=["label"])
    y = df["label"]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )

    models = {
        "logistic_regression": LogisticRegression(max_iter=1000),
        "random_forest": RandomForestClassifier(random_state=42),
    }

    results = []

    best_model_name = None
    best_model = None
    best_f1 = -1.0

    for name, model in models.items():
        model.fit(x_train, y_train)
        metrics = evaluate_model(name, model, x_test, y_test)
        results.append(metrics)

        if metrics["f1"] > best_f1:
            best_f1 = metrics["f1"]
            best_model_name = name
            best_model = model

    models_dir = Path("models")
    models_dir.mkdir(parents=True, exist_ok=True)
    model_path = models_dir / "best_model.joblib"
    joblib.dump(best_model, model_path)

    metrics_dir = Path("outputs/metrics")
    metrics_dir.mkdir(parents=True, exist_ok=True)
    metrics_path = metrics_dir / "training_metrics.json"
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"Best model: {best_model_name}")
    print(f"Saved model to: {model_path}")
    print(f"Saved metrics to: {metrics_path}")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()