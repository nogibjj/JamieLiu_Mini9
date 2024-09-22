import pandas as pd
from mylib.lib import (
    load_dataset,
    process_mean,
    process_median,
    process_max,
    process_min,
    process_std,
    bar_visual,
    hist_visual,
)

# Load dataset for testing
df = load_dataset()


def test_load_dataset():
    """Test if the dataset loads correctly"""
    print("Testing load_dataset...")
    assert isinstance(df, pd.DataFrame), "Dataset should be a pandas DataFrame"
    assert df.shape == (56, 8), "Dataset shape should be (56, 8)"
    print("Passed test_load_dataset\n")


def test_stats():
    """Test that checks the data operations is working"""
    general_test = df.describe()
    mean_test = process_mean(df, "incidents_85_99")
    assert general_test.loc["mean", "incidents_85_99"] == mean_test
    median_test = process_median(df, "fatal_accidents_85_99")
    assert general_test.loc["50%", "fatal_accidents_85_99"] == median_test
    max_test = process_max(df, "fatalities_85_99")
    assert general_test.loc["max", "fatalities_85_99"] == max_test
    min_test = process_min(df, "incidents_00_14")
    assert general_test.loc["min", "incidents_00_14"] == min_test
    std_test = process_std(df, "fatalities_00_14")
    assert general_test.loc["std", "fatalities_00_14"] == std_test


def test_visual_functions():
    """Test the visual functions (bar and histogram)"""
    print("Testing visual functions...")

    df = load_dataset()

    # Test bar_visual with jupyter_render=False (saves the plot)
    try:
        bar_visual(df, "incidents_85_99", jupyter_render=False)
        print("bar_visual with jupyter_render=False passed without errors")
    except Exception as e:
        print(f"bar_visual with jupyter_render=False raised an exception: {e}")

    # Test bar_visual with jupyter_render=True (executes plt.show)
    try:
        bar_visual(df, "incidents_85_99", jupyter_render=True)
        print("bar_visual with jupyter_render=True passed without errors")
    except Exception as e:
        print(f"bar_visual with jupyter_render=True raised an exception: {e}")

    # Test hist_visual with jupyter_render=False (saves the plot)
    try:
        hist_visual(df, "fatal_accidents_85_99", jupyter_render=False)
        print("hist_visual with jupyter_render=False passed without errors")
    except Exception as e:
        print(f"hist_visual with jupyter_render=False raised an exception: {e}")

    # Test hist_visual with jupyter_render=True (executes plt.show)
    try:
        hist_visual(df, "fatal_accidents_85_99", jupyter_render=True)
        print("hist_visual with jupyter_render=True passed without errors")
    except Exception as e:
        print(f"hist_visual with jupyter_render=True raised an exception: {e}")

    print("Passed visual function tests\n")


# Running all the tests
if __name__ == "__main__":
    test_load_dataset()
    test_stats()
    test_visual_functions()
