import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("v8.csv")
data['Date'] = pd.to_datetime(data['Date']).dt.to_period('M')
data.set_index("Date", inplace=True)
print(data.head())

def plot_state(state, plot_number):
    plt.subplot(2,2,plot_number)
    # Filter data for the selected state
    state_data = data[data['State'] == state].copy()

    # Convert the 'Date' column into a datetime object to allow for plotting
    state_data['Date'] = state_data.index.to_timestamp()

    # Compute 6-month moving average for 'Value'
    state_data['SmoothedValue'] = state_data['Value'].rolling(window=6).mean()

    # Plot the smoothed data
    sns.lineplot(data=state_data, x='Date', y='SmoothedValue')

    plt.title(f"6-Month Avg Value for {state}")



def plot_state_range(state, start_year, end_year, plot_number):
    plt.subplot(2,2,plot_number)
    # Filter by state
    state_data = data[data['State'] == state]

    # Filter by the start year
    state_data = state_data[state_data.index.year >= start_year]

    # Filter by the end year
    state_data = state_data[state_data.index.year <= end_year]

    state_data['Date'] = state_data.index.to_timestamp()
    # Plot the data
    sns.lineplot(data=state_data, x='Date', y='Value')
    plt.title(f"Value for {state} ({start_year}-{end_year})")


# Assuming you have a region_mapping dictionary
# data['Region'] = data['State'].map(region_mapping)

# Plotting by regions
def plot_region(region, plot_number):
    plt.subplot(2, 2, plot_number)

    # Extract the 'Division' data and reset the index to have 'Date' as a column
    division_data = data[data['Division'] == region].reset_index()

    # Ensure the Date column is in datetime format (in case it isn't)
    division_data['Date'] = division_data['Date'].dt.to_timestamp()

    # Aggregate data for the given region
    aggregated_data = division_data.groupby('Date').agg({'Value': 'sum'}).reset_index()

    sns.lineplot(data=aggregated_data, x='Date', y='Value')
    plt.title(f"Total Value over Time for {region} Region")


# Plotting multiple states for comparison
def plot_states_comparison(states_to_compare, plot_number):
    plt.subplot(2, 2, plot_number)

    subset = data[data['State'].isin(states_to_compare)].reset_index()
    subset['Date'] = subset['Date'].dt.to_timestamp()

    # Compute 6-month moving average for 'Value'
    subset['SmoothedValue'] = subset['Value'].rolling(window=9).mean()

    sns.lineplot(data=subset, x='Date', y='SmoothedValue', hue='State')
    plt.title("Value over Time for Multiple States")

# FacetGrid
def plot_facet_grid(plot_number):
    new_data = data.copy()
    new_data['Date'] = data.index.to_timestamp()


    g = sns.FacetGrid(data=new_data, col="State", col_wrap=10, height=4)

    g = g.map(plt.plot, "Date", "Value")
    g.set_titles("{col_name}")
    plt.show()

# Heatmap of lag variables
def plot_heatmap(lag_vars):
    correlation_matrix = data[lag_vars].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.show()

plt.figure(figsize=(10, 10))
# Now call the functions as required
plot_state('Florida', 1)

plot_state_range('Florida', 2018, 2023, 2)

plot_region('East_South_Central', 3)

plot_states_comparison(['Florida', 'Texas', 'California'], 4)

plot_facet_grid(4)

plot_heatmap(['Value', 'Value_Lag_1', 'Value_Lag_2', 'Value_Lag_3', 'Value_Lag_4', 'Value_Lag_5', 'Value_Lag_6'])

plt.show()
