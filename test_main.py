import numpy as np
import pandas as pd

def test_numpy_math():
    # We pass a clear list of numbers to numpy
    numbers = np.array([1, 2, 3, 4, 5])
    result = np.mean(numbers)
    assert result == 3.0

def test_pandas_dataframe():
    # We pass a matching list of user numbers for the cities
    data = {
        "City": ["Bengaluru", "New York"], 
        "Users": [100, 200]
    }
    df = pd.DataFrame(data)
    
    assert "City" in df.columns
    assert "Users" in df.columns
    
    bengaluru_users = df[df["City"] == "Bengaluru"]["Users"].values[0]
    assert bengaluru_users == 100
