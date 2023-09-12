import os

# Specify the directory containing the text historic_files
directory = "historic_files"

# Loop through all the historic_files in the directory
for filename in os.listdir(directory):
    # Check if the filename matches the expected format (text historic_files)
    if filename.endswith(".txt"):
        try:
            # Construct the file path
            file_path = os.path.join(directory, filename)

            # Remove the file
            os.remove(file_path)

            print(f"The file {filename} has been removed.")
        except Exception as e:
            print(f"An error occurred while removing the file {filename} (Error: {e})")

print("File removal completed.")
