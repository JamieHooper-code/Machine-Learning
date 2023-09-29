import pandas as pd

# Load the CSV file
file_path = r'C:\Users\Nate\Desktop\Important\machine_learning\tensorEnv\Tutoring_ML_Nick\master_dataset_v5.csv'
df = pd.read_csv(file_path)

# Use the melt function to convert the DataFrame to long format
# Assuming 'State' and 'Division' are the identifier variables, and the rest are the months and values
long_df = pd.melt(df, id_vars=['State', 'Division'], var_name='Date', value_name='Value')

# Convert the 'Date' column to a period with a monthly frequency
long_df['Date'] = pd.to_datetime(long_df['Date'], errors='coerce').dt.to_period('M')

# Saving the DataFrame back to CSV in the new format
output_path = r'C:\Users\Nate\Desktop\Important\machine_learning\tensorEnv\Tutoring_ML_Nick\master_dataset_v6_long.csv'
long_df.to_csv(output_path, index=False)
