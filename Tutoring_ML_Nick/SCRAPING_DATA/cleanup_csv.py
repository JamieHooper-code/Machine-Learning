import pandas as pd
import os

# Get the path to the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path to the files directory
files_dir = os.path.join(script_dir, "historic_files_2004")

# Get a list of all CSV files in the files directory
csv_files = [f for f in os.listdir(files_dir) if f.endswith('.csv')]

# Iterate through all the CSV files
for csv_file in csv_files:
    # Construct the file path to the current CSV file
    file_path = os.path.join(files_dir, csv_file)

    # Load the current CSV file
    df = pd.read_csv(file_path)

    # Apply the cleaning operations to all cells in the DataFrame
    df = df.applymap(lambda x: x.strip().replace(' ', '_') if isinstance(x, str) else x)

    # Save the cleaned data back to the current CSV file
    df.to_csv(file_path, index=False)

print("All CSV files in the files directory have been cleaned.")
