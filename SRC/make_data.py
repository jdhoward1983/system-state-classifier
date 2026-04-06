from pathlib import Path
import numpy as np
import pandas as pd


def main() -> None:
    rng = np.random.default_rng(42)
    n_samples = 1000

    cpu_usage = rng.normal(45, 15, n_samples).clip(0, 100)
    memory_usage = rng.normal(50, 18, n_samples).clip(0, 100)
    latency_ms = rng.normal(120, 50, n_samples).clip(10, 1000)
    error_rate = rng.normal(1.5, 1.2, n_samples).clip(0, 20)
    packet_loss = rng.normal(0.8, 1.0, n_samples).clip(0, 15)

    score = (
        0.03 * cpu_usage
        + 0.025 * memory_usage
        + 0.01 * latency_ms
        + 0.8 * error_rate
        + 1.2 * packet_loss
    )

    label = (score > 6.5).astype(int)

    df = pd.DataFrame(
        {
            "cpu_usage": cpu_usage,
            "memory_usage": memory_usage,
            "latency_ms": latency_ms,
            "error_rate": error_rate,
            "packet_loss": packet_loss,
            "label": label,
        }
    )

    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "system_state_data.csv"
    df.to_csv(output_file, index=False)

    print(f"Saved dataset to: {output_file}")
    print(df.head())
    print(df["label"].value_counts())


if __name__ == "__main__":
    main()