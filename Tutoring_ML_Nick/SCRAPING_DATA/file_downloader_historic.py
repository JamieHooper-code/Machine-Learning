import os
import requests
from tqdm import tqdm

# Create a folder named 'historic_files' if it doesn't exist
if not os.path.exists('historic_files'):
    os.makedirs('historic_files')

# Loop through the years and months to construct the URLs and download the historic_files
for year in tqdm(range(2010, 2020)):
    for month in range(1, 13):
        # Construct the URL
        url = f"https://www.census.gov/construction/bps/txt/t2yu{year}{month:02d}.txt"

        # Construct the file path
        file_path = f"SCRAPING_DATA/historic_files/t2yu{year}{month:02d}.txt"

        try:
            # Download the file
            response = requests.get(url)

            # If the response status code is 200 (OK), save the file
            if response.status_code == 200:
                with open(file_path, 'wb') as file:
                    file.write(response.content)
            else:
                print(f"Failed to download file: {url} (Status code: {response.status_code})")
        except Exception as e:
            print(f"An error occurred while downloading the file: {url} (Error: {e})")
