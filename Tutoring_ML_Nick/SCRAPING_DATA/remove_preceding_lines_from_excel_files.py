import pandas as pd
import os

# Get the path to the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Script Directory: {script_dir}")

# Get the path to the new_files directory
new_files_dir = os.path.join(script_dir, "new_files_test")
print(f"New Files Directory: {new_files_dir}")

# Get a list of all Excel files in the new_files directory
excel_files = [f for f in os.listdir(new_files_dir) if f.endswith(('.xls', '.xlsx'))]
print(f"Files to be opened: {excel_files}")

# Iterate through all the Excel files
for excel_file in excel_files:
    # Construct the file path to the current Excel file
    file_path = os.path.join(new_files_dir, excel_file)

    try:
        # Try reading the file with the openpyxl engine first
        df = pd.read_excel(file_path, engine='openpyxl', header=None)
    except:
        # If that fails, try with the xlrd engine
        df = pd.read_excel(file_path, engine='xlrd', header=None)

    # Find the index of the row that contains the word "Total"
    total_row_index = df[df.apply(lambda row: row.astype(str).str.contains('Total').any(), axis=1)].index[0]

    # Remove all rows before the "Total" row
    df = df.iloc[total_row_index:]

    # Determine the appropriate engine for writing the file
    write_engine = 'openpyxl' if excel_file.endswith('.xlsx') else 'xlwt'

    # Save the cleaned data back to the current Excel file using the appropriate engine
    df.to_excel(file_path, index=False, header=False, engine=write_engine)

print("All Excel files in the new_files directory have been cleaned.")
