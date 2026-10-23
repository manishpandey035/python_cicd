import numpy as np
import pandas as pd


# Test 1: Verify Numpy is working by calculating a simple mean
def test_numpy_math():
    numbers = np.array([1, 2, 3, 4, 5])
    result = np.mean(numbers)
    assert result == 3.0  # The average must be exactly 3.0


# Test 2: Verify Pandas can create a DataFrame and manipulate data
def test_pandas_dataframe():
    # Create a small dummy dataset
    data = {"City": ["Bengaluru", "New York"], "Users":}
    df = pd.DataFrame(data)

    # Check that the columns match what we defined
    assert "City" in df.columns
    assert "Users" in df.columns

    # Check that data filtering works
    bengaluru_users = df[df["City"] == "Bengaluru"]["Users"].values[0]
    assert bengaluru_users == 100
