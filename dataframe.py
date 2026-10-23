import pandas as pd

# 1. Create a dictionary with sample sales data
data = {
    "Product": ["Laptop", "Smartphone", "Desk Chair", "Monitor", "Keyboard"],
    "Category": ["Electronics", "Electronics", "Furniture", "Electronics", "Electronics"],
    "Price": [1200, 800, 150, 300, 50],
    "Quantity_Sold": [5, 10, 15, 7, 25]
}

# 2. Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)
print("--- Original DataFrame ---")
print(df)
print("\n")

# 3. Add a new column calculated from existing columns
df["Total_Revenue"] = df["Price"] * df["Quantity_Sold"]

# 4. Filter the rows to see only 'Electronics' that generated over $3,000
high_sales_electronics = df[(df["Category"] == "Electronics") & (df["Total_Revenue"] > 3000)]

print("--- High-Revenue Electronics ---")
print(high_sales_electronics)
print("\n")

# 5. Calculate the average price of all items
avg_price = df["Price"].mean()
print(f"Average Product Price: ${avg_price:.2f}")
