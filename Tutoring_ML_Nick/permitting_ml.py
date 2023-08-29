import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data
data = pd.read_csv('permit_dataset.csv')

print(data.dtypes)

# Convert all columns to numeric
exclude_columns = ['Division', 'State']
columns_to_convert = [col for col in data.columns if col not in exclude_columns]
data[columns_to_convert] = data[columns_to_convert].apply(pd.to_numeric, errors='coerce')

print(data.dtypes)

# Prepare the data
x = data.iloc[0]
x = x.drop(['Division', 'State'])
print(x)


# Plot the data
plt.bar(x.index, x.values)

# Add a title and labels
plt.title('A Simple Plot')
plt.xlabel('x')
plt.ylabel('y')

# Rotate x labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.show()
