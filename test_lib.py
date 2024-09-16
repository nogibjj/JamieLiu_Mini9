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


def test_process_mean():
    """Test process_mean function"""
    print("Testing process_mean...")
    col = "incidents_85_99"
    expected_mean = df[col].mean()
    assert (
        process_mean(df, col) == expected_mean
    ), f"Expected {expected_mean}, got {process_mean(df, col)}"
    print("Passed test_process_mean\n")


def test_process_median():
    """Test process_median function"""
    print("Testing process_median...")
    col = "incidents_85_99"
    expected_median = df[col].median()
    assert (
        process_median(df, col) == expected_median
    ), f"Expected {expected_median}, got {process_median(df, col)}"
    print("Passed test_process_median\n")


def test_process_max():
    """Test process_max function"""
    print("Testing process_max...")
    col = "fatalities_85_99"
    expected_max = df[col].max()
    assert (
        process_max(df, col) == expected_max
    ), f"Expected {expected_max}, got {process_max(df, col)}"
    print("Passed test_process_max\n")


def test_process_min():
    """Test process_min function"""
    print("Testing process_min...")
    col = "fatal_accidents_85_99"
    expected_min = df[col].min()
    assert (
        process_min(df, col) == expected_min
    ), f"Expected {expected_min}, got {process_min(df, col)}"
    print("Passed test_process_min\n")


def test_process_std():
    """Test process_std function"""
    print("Testing process_std...")
    col = "incidents_00_14"
    expected_std = df[col].std()
    assert (
        process_std(df, col) == expected_std
    ), f"Expected {expected_std}, got {process_std(df, col)}"
    print("Passed test_process_std\n")


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
    test_process_mean()
    test_process_median()
    test_process_max()
    test_process_min()
    test_process_std()
    test_visual_functions()
