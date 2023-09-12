import os
import re

# Specify the directory containing the historic_files
directory = "TEST_FILES"

# List of strings to replace (case insensitive)
strings_to_replace = [
    "United States",
    "Middle Atlantic",
    "East North Central",
    "West North Central",
    "South Atlantic",
    "East South Central",
    "West South Central",
    "Mountain",
    "Pacific",
    "New England",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "District of Columbia",
    "West Virginia",
    "Total",
    "1 Unit",
    "2 Units",
    "or More"
]

# Loop through all the historic_files in the directory
for filename in os.listdir(directory):
    # Check if the filename matches the expected format (text historic_files)
    if filename.endswith(".txt"):
        try:
            # Construct the file path
            file_path = os.path.join(directory, filename)

            # Read the file content
            with open(file_path, 'r') as file:
                content = file.read()

            # Replace strings with spaces with underscores (case insensitive)
            for string in strings_to_replace:
                content = re.sub(re.compile(re.escape(string), re.IGNORECASE), string.replace(" ", "_"), content)

            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.write(content)

            print(f"Spaces have been replaced with underscores in the file: {filename}")
        except Exception as e:
            print(f"An error occurred while processing the file: {filename} (Error: {e})")

print("File processing completed.")
