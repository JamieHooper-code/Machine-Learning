import pandas as pd
import os

# Specify the directory containing your XLS files
directory_path = "new_files"

# Get a list of all .xls files in the directory
xls_files = [f for f in os.listdir(directory_path) if f.endswith('.xls')]

# Iterate through all the .xls files
for xls_file in xls_files:
    # Construct the full path to the current .xls file
    file_path = os.path.join(directory_path, xls_file)

    # Load the spreadsheet into a DataFrame
    df = pd.read_excel(file_path, engine='xlrd')

    # Remove rows where all cells are NA
    df.dropna(how='all', inplace=True)

    # Construct the full path to save the cleaned .xls file
    cleaned_file_path = os.path.join(directory_path, f"{xls_file}")

    # Save the cleaned DataFrame back to a new .xls file
    with pd.ExcelWriter(cleaned_file_path, engine='xlwt') as writer:
        df.to_excel(writer, index=False)

    print(f"Empty rows have been deleted from {xls_file} and the cleaned file has been saved as cleaned_{xls_file}.")

print("Processing completed for all files.")
