import pytest
import pandas as pd
from make_functions import (
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


def test_calculate_mean(sample_dataframe):
    mean_test = calculate_mean(sample_dataframe, "A")
    assert mean_test == 3.0


def test_calculate_median(sample_dataframe):
    median_test = calculate_median(sample_dataframe, "A")
    assert median_test == 3.0


def test_calculate_std_dev(sample_dataframe):
    std_dev_test = calculate_std_dev(sample_dataframe, "A")
    assert std_dev_test == pytest.approx(1.5811, rel=1e-4)


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
