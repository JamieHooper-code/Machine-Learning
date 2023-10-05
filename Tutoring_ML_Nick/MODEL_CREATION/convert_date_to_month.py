import pandas as pd

# 1. Read the CSV
data = pd.read_csv("v7.csv")

# 2. Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# 3. Convert the 'Date' column to month format (year-month)
data['Date'] = data['Date'].dt.to_period('M')

# 4. Save the modified DataFrame back to a CSV
data.to_csv("v8.csv", index=False)
