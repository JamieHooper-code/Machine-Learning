import os

# Specify the directory containing the historic_files
directory = "TEST_FILES"

# Loop through all the historic_files in the directory
for filename in os.listdir(directory):
    # Check if the filename matches the expected format (text historic_files)
    if filename.endswith(".txt"):
        try:
            # Construct the file path
            file_path = os.path.join(directory, filename)

            # Read the file lines into a list
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Find the index of the line containing the word "Total"
            total_index = next((index for index, line in enumerate(lines) if 'Total' in line), None)

            # If the word "Total" is found, keep the lines from that index onwards
            if total_index is not None:
                lines = lines[total_index:]

            # Write the remaining lines back to the file
            with open(file_path, 'w') as file:
                file.writelines(lines)

            print(f"Lines have been removed up to the line containing the word 'Total' in the file: {filename}")
        except Exception as e:
            print(f"An error occurred while processing the file: {filename} (Error: {e})")

print("File processing completed.")
