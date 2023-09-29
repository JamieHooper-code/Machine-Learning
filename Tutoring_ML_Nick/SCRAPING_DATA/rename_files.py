import os

# Specify the directory containing the historic_files_2004
directory = "historic_files_2004"

# Loop through all the historic_files_2004 in the directory
for filename in os.listdir(directory):
    # Check if the filename matches the expected format
    if filename.startswith("statemonthly_") and filename.endswith(".xls"):
        # Extract the year and month from the filename
        year = filename[13:17]
        month = filename[17:19]

        # Construct the new filename
        new_filename = f"{year}-{month}.xls"

        try:
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        except Exception as e:
            print(f"An error occurred while renaming the file: {filename} (Error: {e})")
    else:
        print(f"The file does not match the expected format: {filename}")

print("File renaming completed.")
