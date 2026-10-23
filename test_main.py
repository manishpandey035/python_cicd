cat << 'EOF' > test_main.py
import numpy as np
import pandas as pd

def test_numpy_math():
    # Provide actual numbers [1, 2, 3, 4, 5] for the array
    numbers = np.array([1, 2, 3, 4, 5])
    result = np.mean(numbers)
    assert result == 3.0

def test_pandas_dataframe():
    # Provide actual user counts [100, 200] matching the cities
    data = {"City": ["Bengaluru", "New York"], "Users":}
    df = pd.DataFrame(data)
    
    assert "City" in df.columns
    assert "Users" in df.columns
    
    # Extract the value properly to compare it
    bengaluru_users = df[df["City"] == "Bengaluru"]["Users"].values[0]
    assert bengaluru_users == 100
EOF