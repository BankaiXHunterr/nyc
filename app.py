# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit_shadcn_ui as ui
from uniplots import TaxiDataVisualizer

st.set_option('deprecation.showPyplotGlobalUse', False)


# Load the filtered data
@st.cache_data
def load_data():
    # Read the CSV file
    data = pd.read_csv('data/filtered_data.csv')
    # Convert datetime columns to datetime objects
    data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])
    data['tpep_dropoff_datetime'] = pd.to_datetime(data['tpep_dropoff_datetime'])
    # Calculate trip duration in minutes
    data['trip_duration'] = (data['tpep_dropoff_datetime'] - data['tpep_pickup_datetime']).dt.total_seconds() / 60
    # Fill any NaN values in trip duration with 0
    data['trip_duration'].fillna(0, inplace=True)
    return data

# Load the data
df = load_data()

# Streamlit App Title
st.title('NYC Taxi Trips Ending at Crate and Barrel Flagship Store')

# Display filtered data
st.write("Filtered Data")
# st.dataframe(df.head())  # Uncomment this line to display the first few rows of the dataframe

# Sidebar for date range selection
st.sidebar.header('Select Date Range')
min_date = df['tpep_pickup_datetime'].min().date()
max_date = df['tpep_pickup_datetime'].max().date()
start_date = st.sidebar.date_input('Start Date', min_date)
end_date = st.sidebar.date_input('End Date', max_date)

# Time range selection
start_time = st.sidebar.time_input('Start Time', value=pd.Timestamp('00:00:00').time())
end_time = st.sidebar.time_input('End Time', value=pd.Timestamp('23:59:59').time())

# Combine selected date with start and end times to create datetime objects
start_datetime = pd.to_datetime(f"{start_date} {start_time}")
end_datetime = pd.to_datetime(f"{end_date} {end_time}")


# Filter the data based on the selected date range
filtered_df = df[(df['tpep_pickup_datetime'] >= start_datetime) & 
                 (df['tpep_pickup_datetime'] <= end_datetime)]



# Additional analysis: trip duration statistics
short_trips = filtered_df[filtered_df['trip_duration'] < 10].shape[0]
long_trips = filtered_df[filtered_df['trip_duration'] > 61].shape[0]
medium_trips = filtered_df[(filtered_df['trip_duration'] <= 61) & (filtered_df['trip_duration'] >= 10)].shape[0]

# Sidebar for trip duration filter
st.header("Filter Trips by Duration")
min_duration = int(filtered_df['trip_duration'].min())
median = filtered_df['trip_duration'].median()
stddev = filtered_df['trip_duration'].std()
max_duration = int(median+10*stddev)
# Set a default range for the slider
default_min = min_duration
default_max = max_duration

# Adjust the step size based on the range
if max_duration - min_duration > 100:
    step_size = int((max_duration - min_duration) / 100)  # Adjust as needed
else:
    step_size = 1  # Adjust as needed for smaller ranges


# Slider for selecting trip duration range
duration_range = st.slider(
    "Select Duration Range (minutes)",
    min_value=min_duration,
    max_value=max_duration,
    value=(default_min, default_max),
    step=step_size
)

# duration_range = st.slider('Select Trip Duration Range (minutes)', 0, int(filtered_df['trip_duration'].max()), (0, int(filtered_df['trip_duration'].max())))

# Filter data based on selected duration range
filtered_by_duration = filtered_df[(filtered_df['trip_duration'] >= duration_range[0]) & (filtered_df['trip_duration'] <= duration_range[1])]




# Display metrics using metric cards
cols = st.columns(2)

with cols[0]:
    ui.metric_card(title="Total Number of Trips to Crate and Barrel", content=len(filtered_df), description="Total Trips to Crate and Barrel Flagship Store", key="card1")

with cols[1]:
    ui.metric_card(title="Number of trips shorter than 10 minutes to Crate and Barrel", content=short_trips, description=f"{(short_trips/len(filtered_df))*100:.2f}% of all the Trips to Crate and Barrel Flagship Store", key="card2")

cols = st.columns(2)

with cols[0]:
    ui.metric_card(title="Number of trips longer than 61 minutes to Crate and Barrel", content=long_trips, description=f"{(long_trips/len(filtered_df))*100:.2f}% of all the Trips to Crate and Barrel Flagship Store", key="card3")

with cols[1]:
    ui.metric_card(title="Number of trips Between 61 minutes & 10 minutes to Crate and Barrel", content=medium_trips, description=f"{(medium_trips/len(filtered_df))*100:.2f}% of all the Trips to Crate and Barrel Flagship Store", key="card4")


taxi = TaxiDataVisualizer(filtered_by_duration)
taxi.plot_distribution()
