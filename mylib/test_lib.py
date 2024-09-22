import pytest
import pandas as pd
from make_functions import (
    load_dataset,
    calculate_mean,
    calculate_median,
    calculate_std_dev,
    bar_plot,
    pie_chart,
)


# Sample DataFrame for testing
@pytest.fixture
def sample_dataframe():
    data = {"A": [1, 2, 3, 4, 5], "B": [5, 4, 3, 2, 1]}
    return pd.DataFrame(data)


def test_load_dataset(monkeypatch):
    # Mocking pandas read_csv
    def mock_read_csv(filepath):
        return pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

    monkeypatch.setattr(pd, "read_csv", mock_read_csv)
    df = load_dataset("dummy_path")
    assert df.shape == (3, 2)
    assert list(df.columns) == ["A", "B"]


def test_calculate_mean(sample_dataframe):
    mean_A = calculate_mean(sample_dataframe, "A")
    assert mean_A == 3.0


def test_calculate_median(sample_dataframe):
    median_A = calculate_median(sample_dataframe, "A")
    assert median_A == 3.0


def test_calculate_std_dev(sample_dataframe):
    std_dev_A = calculate_std_dev(sample_dataframe, "A")
    assert std_dev_A == pytest.approx(1.5811, rel=1e-4)


def test_empty_column():
    empty_df = pd.DataFrame({"A": []})
    assert calculate_mean(empty_df, "A") is None
    assert calculate_median(empty_df, "A") is None
    assert calculate_std_dev(empty_df, "A") is None


def test_bar_plot(sample_dataframe):
    try:
        bar_plot(
            sample_dataframe, "A", "B", "Test Bar Plot", "X", "Y", jupyter_render=True
        )
    except Exception as e:
        pytest.fail(f"bar_plot raised an exception: {e}")


def test_pie_chart(sample_dataframe):
    try:
        pie_chart(sample_dataframe, "A", "Test Pie Chart", jupyter_render=True)
    except Exception as e:
        pytest.fail(f"pie_chart raised an exception: {e}")
