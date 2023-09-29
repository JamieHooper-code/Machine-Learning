import pandas as pd
from datetime import datetime, timedelta
import os

# Get the path to the parent directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)

# Construct the file path to the CSV file in the parent directory
file_path = os.path.join(parent_dir, "master_dataset_v0.csv")

# Load the CSV file
df = pd.read_csv(file_path)

# Generate a list of month-year strings from July 2023 to January 2010
start_date = datetime(2023, 7, 1)
end_date = datetime(1994, 1, 1)
date_list = [start_date - timedelta(days=i*30) for i in range((start_date - end_date).days // 30 + 1)]
date_strings = [date.strftime('%Y-%m') for date in date_list]

# Create new columns with the generated month-year strings
for date_str in date_strings:
    # Check if the column already exists
    if date_str not in df.columns:
        df[date_str] = None

# Construct the file path to save the modified CSV file in the parent directory
output_file_path = os.path.join(parent_dir, "master_dataset_v1.csv")

# Save the modified DataFrame back to a CSV file
df.to_csv(output_file_path, index=False)

print("New columns have been created and the modified file has been saved.")
