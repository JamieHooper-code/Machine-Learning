import pandas as pd

# Load the data from a CSV file
filepath = 'C:\\Users\\Nate\\Desktop\\Important\\machine_learning\\tensorEnv\\Tutoring_ML_Nick\\Model_Creation\\master_dataset_v6_long.csv'
df = pd.read_csv(filepath)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Function to create lag variables for each group
def create_lag_vars(group):
    for i in range(1, 7):
        group[f'Value_Lag_{i}'] = group['Value'].shift(-i)  # shifting in the opposite direction
    group['Value_Lag_1_Year'] = group['Value'].shift(-12)
    group['Value_Lag_2_Years'] = group['Value'].shift(-24)
    group['Value_Lag_3_Years'] = group['Value'].shift(-36)
    group['Value_Lag_4_Years'] = group['Value'].shift(-48)
    group['Value_Lag_5_Years'] = group['Value'].shift(-60)
    return group

# Group by 'State' and apply the function to each group
df = df.groupby('State').apply(create_lag_vars)

# Reset index
df.reset_index(inplace=True)

# Sort the values by 'State' and 'Date' for aesthetic grouping in the final CSV
df.sort_values(by=['State', 'Date'], inplace=True)

# Save the new DataFrame in the same folder as a CSV file
output_filepath = filepath.rsplit('\\', 1)[0] + '\\master_dataset_v7_long_with_lags.csv'
df.to_csv(output_filepath, index=False)

# Check the new DataFrame
print(df.head())
