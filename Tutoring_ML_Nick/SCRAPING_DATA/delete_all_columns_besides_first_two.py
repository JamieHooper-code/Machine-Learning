import os
import pandas as pd

# Specify the directory where your .xls Excel files are located
excel_files_directory = "new_files"

# Get a list of all .xls Excel files in the directory
excel_files = [f for f in os.listdir(excel_files_directory) if f.endswith('.xls')]

# Iterate through all the .xls Excel files
for excel_file in excel_files:
    # Construct the full file path
    file_path = os.path.join(excel_files_directory, excel_file)

    # Load the .xls Excel file into a DataFrame using the xlrd engine
    df = pd.read_excel(file_path, engine='xlrd')

    # Delete columns beyond the second column (index 2 onwards)
    df = df.iloc[:, :2]

    # Save the modified DataFrame back to the .xls Excel file using the xlwt engine
    df.to_excel(file_path, index=False, engine='xlwt')

print("Columns beyond the second column have been deleted from all .xls Excel files.")
