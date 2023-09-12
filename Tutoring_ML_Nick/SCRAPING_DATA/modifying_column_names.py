import pandas as pd
from datetime import datetime, timedelta
import os

# Get the path to the parent directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)

# Construct the file path to the Excel file in the parent directory
file_path = os.path.join(parent_dir, "permit_dataset2.xls")

# Load the Excel file
df = pd.read_excel(file_path)

# Generate a list of month-year strings from July 2023 to January 2010
start_date = datetime(2023, 7, 1)
end_date = datetime(2010, 1, 1)
date_list = [start_date - timedelta(days=i*30) for i in range((start_date - end_date).days // 30 + 1)]
date_strings = [date.strftime('%Y-%m') for date in date_list]

# Create new columns with the generated month-year strings
for date_str in date_strings:
    df[date_str] = None

# Construct the file path to save the modified Excel file in the parent directory
output_file_path = os.path.join(parent_dir, "modified_permit_dataset2.xls")

# Save the modified DataFrame back to an Excel file
df.to_excel(output_file_path, index=False)

print("New columns have been created and the modified file has been saved.")
