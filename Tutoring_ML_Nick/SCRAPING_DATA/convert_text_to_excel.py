import os
import pandas as pd

# Specify the directory containing the text historic_files_2004
directory = "historic_files_2004"

# Loop through all the historic_files_2004 in the directory
for filename in os.listdir(directory):
    # Check if the filename matches the expected format (text historic_files_2004)
    if filename.endswith(".txt"):
        try:
            # Construct the file path
            file_path = os.path.join(directory, filename)

            # Read the text file line by line
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Find the index of the line containing the word "Total"
            total_index = next((index for index, line in enumerate(lines) if 'Total' in line), None)

            # If the word "Total" is found, extract the lines from that index onwards
            if total_index is not None:
                lines = lines[total_index + 1:]

            # Create a list to store the data
            data = []

            # Loop through the lines and extract the location and total
            for line in lines:
                # Split the line into words
                words = line.split()

                # If there are enough words, extract the location and total
                if len(words) > 1:
                    location = " ".join([word for word in words if not word.isdigit()])
                    total = next((word for word in words if word.isdigit()), None)
                    if total:
                        data.append([location, total])

            # Create a pandas DataFrame from the data
            df = pd.DataFrame(data, columns=['Location', 'Total'])

            # Create a new file name with .xlsx extension
            new_filename = os.path.splitext(filename)[0] + '.xlsx'
            new_file_path = os.path.join(directory, new_filename)

            # Write the DataFrame to an Excel file
            df.to_excel(new_file_path, index=False)

            print(f"The file {filename} has been converted to an Excel file: {new_filename}")
        except Exception as e:
            print(f"An error occurred while converting the file {filename} to Excel (Error: {e})")

print("File conversion completed.")
