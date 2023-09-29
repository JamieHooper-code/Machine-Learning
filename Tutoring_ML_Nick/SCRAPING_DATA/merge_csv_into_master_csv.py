import pandas as pd
import os

# Function to convert filename to month_year format (e.g., 201012 to 2010–12)
def convert_month_year(filename):
    year = filename[:4]
    month = filename[4:6]
    return f"{year}-{month}"

# Get the path to the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)

# Construct the file path to the master CSV file in the parent directory
master_file_path = os.path.join(parent_dir, "master_dataset_v3.csv")

# Load the master CSV file
master_df = pd.read_csv(master_file_path)

# Explicitly set the index to the 'State' column (change 'State' to your actual column name)
master_df.set_index('State', inplace=True)

# Set the index of the master DataFrame to the state column (second column) for easy updating
# master_df.set_index(master_df.columns[1], inplace=True)

# Get the path to the TEST_FILES directory
test_files_dir = os.path.join(script_dir, "historic_files_2004")

# Get a list of all CSV files in the TEST_FILES directory
csv_files = [f for f in os.listdir(test_files_dir) if f.endswith('.csv')]

# Iterate through all the CSV files
for csv_file in csv_files:
    # Construct the file path to the current CSV file
    file_path = os.path.join(test_files_dir, csv_file)

    # Load the current CSV file
    df = pd.read_csv(file_path)

    # Get the month-year string from the file name
    month_year = convert_month_year(os.path.splitext(csv_file)[0])

    # Create a dictionary to map state names (from column 1 of individual files) to total values
    data_dict = dict(zip(df[df.columns[0]].str.strip(), df['Total']))

    # Print the data dictionary for debugging
    print(f"Data dictionary for {month_year}: {data_dict}")

    # Update the corresponding column in the master DataFrame with the data from the current file
    master_df[month_year] = master_df.index.to_series().map(data_dict)

# Reset the index of the master DataFrame
master_df.reset_index(inplace=True)

# Construct the file path to save the updated master CSV file in the parent directory
output_file_path = os.path.join(parent_dir, "master_dataset_v4.csv")

# Save the updated master DataFrame back to a CSV file
master_df.to_csv(output_file_path, index=False)

print("Data has been merged into the master file. The updated master file has been saved.")
