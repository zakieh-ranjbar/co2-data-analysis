"""Reusable exploratory analysis for the submitted CO2 vehicle dataset."""
from __future__ import annotations
from pathlib import Path
import json
import pandas as pd

RAW_COLUMNS = ["engine", "cylandr", "fuelcomb", "out1"]
RENAME = {"engine": "engine_l", "cylandr": "cylinders", "fuelcomb": "fuel_combined", "out1": "co2_output"}


def load_data(path: str | Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    missing = set(RAW_COLUMNS) - set(frame.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    return frame


def summarize(frame: pd.DataFrame) -> dict:
    numeric = frame[RAW_COLUMNS].describe().round(3)
    correlations = frame[RAW_COLUMNS].corr()["out1"].drop("out1").round(4).to_dict()
    return {
        "rows": int(len(frame)),
        "columns": list(frame.columns),
        "missing_values": {key: int(value) for key, value in frame.isna().sum().items()},
        "co2_output": {
            "total_first_500": int(frame["out1"].head(500).sum()),
            "average_first_500": round(float(frame["out1"].head(500).mean()), 3),
            "min": int(frame["out1"].min()),
            "max": int(frame["out1"].max()),
        },
        "correlation_with_co2_output": correlations,
        "descriptive_statistics": json.loads(numeric.to_json()),
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Summarize the CO2 dataset")
    parser.add_argument("--input", default="data/co2.csv")
    parser.add_argument("--output", default="outputs/summary.json")
    args = parser.parse_args()
    summary = summarize(load_data(args.input))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary["co2_output"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
