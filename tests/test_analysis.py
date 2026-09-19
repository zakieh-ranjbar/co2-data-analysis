import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))
from src.analysis import load_data, summarize


def test_dataset_shape_and_columns():
    frame = load_data("data/co2.csv")
    assert frame.shape == (500, 4)
    assert list(frame.columns) == ["engine", "cylandr", "fuelcomb", "out1"]
    assert int(frame["out1"].sum()) == 134013


def test_summary_matches_notebook():
    summary = summarize(load_data("data/co2.csv"))
    assert summary["co2_output"]["total_first_500"] == 134013
    assert summary["co2_output"]["average_first_500"] == 268.026
    assert all(value == 0 for value in summary["missing_values"].values())
