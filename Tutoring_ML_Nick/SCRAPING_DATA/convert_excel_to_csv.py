import os
import pandas as pd

# Source and destination directories
src_dir = 'MASTER'
dest_dir = 'MASTER2'

# Check if the destination directory exists, if not, create it
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Loop through all files in the source directory
for filename in os.listdir(src_dir):
    # Check if the file is an Excel file
    if filename.endswith('.xls') or filename.endswith('.xlsx'):
        # Construct the file paths
        src_filepath = os.path.join(src_dir, filename)
        # dest_filepath = os.path.join(dest_dir, filename.replace('.xls', '.csv').replace('.xlsx', '.csv'))
        dest_filepath = os.path.join(dest_dir, filename.replace('.xlsx', '.csv'))

        try:
            # Read the Excel file
            df = pd.read_excel(src_filepath, engine='openpyxl')

            # Write the data to a CSV file
            df.to_csv(dest_filepath, index=False)

            print(f"Converted {filename} to CSV.")
        except Exception as e:
            print(f"An error occurred while converting {filename}: {e}")
