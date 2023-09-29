import pandas as pd
import os

# Get the path to the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)

# Construct the file path to the master Excel file in the parent directory
master_file_path = os.path.join(parent_dir, "updated_master_dataset.xlsx")

# Load the master Excel file (no engine specified as it is .xls format)
master_df = pd.read_excel(master_file_path, engine='openpyxl')

# Set the index of the master DataFrame to the state column (second column) for easy updating
master_df.set_index(master_df.columns[1], inplace=True)

# Get the path to the TEST_FILES directory
test_files_dir = os.path.join(script_dir, "new_files_1")

# Get a list of all Excel files in the TEST_FILES directory
excel_files = [f for f in os.listdir(test_files_dir) if f.endswith('.xls') and f.startswith('20')]

# Iterate through all the Excel files
for excel_file in excel_files:
    # Construct the file path to the current Excel file
    file_path = os.path.join(test_files_dir, excel_file)

    # Load the current Excel file using the openpyxl engine (as it is .xlsx format)
    df = pd.read_excel(file_path)

    # Get the month-year string from the file name
    month_year = os.path.splitext(excel_file)[0]

    # Create a dictionary to map state names (from column 1 of individual files) to total values
    data_dict = dict(zip(df[df.columns[0]].str.strip(), df['Total']))

    # Print the data dictionary for debugging
    print(f"Data dictionary for {month_year}: {data_dict}")

    # Update the corresponding column in the master DataFrame with the data from the current file
    # master_df[month_year] = master_df.index.map(data_dict.get)
    master_df[month_year] = master_df.index.to_series().map(data_dict)

# Reset the index of the master DataFrame
master_df.reset_index(inplace=True)

# Construct the file path to save the updated master Excel file in the parent directory
output_file_path = os.path.join(parent_dir, "master_dataset_v0.xlsx")

# Save the updated master DataFrame back to an Excel file
master_df.to_excel(output_file_path, index=False, engine='openpyxl')

print("Data has been merged into the master file. The updated master file has been saved.")
