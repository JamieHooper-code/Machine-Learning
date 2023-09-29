import pandas as pd
import os

# Get the path to the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path to the historic_files_2004 directory
historic_files_dir = os.path.join(script_dir, "historic_files_v3")

# Get a list of all Excel files in the historic_files_2004 directory
excel_files = [f for f in os.listdir(historic_files_dir) if f.endswith(('.xlsx', '.xls'))]

# Iterate through all the Excel files
for excel_file in excel_files:
    # Construct the file path to the current Excel file
    file_path = os.path.join(historic_files_dir, excel_file)

    # Load the current Excel file using the appropriate engine
    engine = 'openpyxl' if excel_file.endswith('.xlsx') else 'xlrd'
    df = pd.read_excel(file_path, engine=engine)

    # Apply the cleaning operations to all cells in the DataFrame
    df = df.applymap(lambda x: x.strip().replace(' ', '_') if isinstance(x, str) else x)

    # Save the cleaned data back to the current Excel file
    df.to_excel(file_path, index=False)

print("All Excel files in the historic_files_2004 directory have been cleaned.")
