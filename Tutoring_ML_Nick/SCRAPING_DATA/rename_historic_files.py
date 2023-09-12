import os

# Specify the directory containing the historic_files
directory = "historic_files"

# Loop through all the historic_files in the directory
for filename in os.listdir(directory):
    # Check if the filename matches the expected format
    if filename.startswith("t2yu") and len(filename) == 14:
        # Extract the year and month from the filename
        year = filename[4:8]
        month = filename[8:10]

        # Construct the new filename
        new_filename = f"{year}-{month}.txt"

        try:
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        except Exception as e:
            print(f"An error occurred while renaming the file: {filename} (Error: {e})")
    else:
        print(f"The file does not match the expected format: {filename}")

print("File renaming completed.")
