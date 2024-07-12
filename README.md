# NYC Taxi Trips Analysis App

This Streamlit application provides an interactive analysis of NYC Yellow Taxi trips, focusing on trips ending at the Crate and Barrel Flagship Store. The app allows users to filter data by date, time, and trip duration, and provides various visualizations and metrics.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Visualizations](#visualizations)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Data Filtering**: Filter trips by date range, time range, and trip duration.
- **Metrics Display**: View key statistics such as total trips, trips shorter than 10 minutes, and trips longer than 61 minutes.
- **Visualizations**: Generate various plots including vendor ID distribution, passenger count distribution, trip distance distribution, and trip duration distribution.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/nyc-taxi-trips-analysis.git
   cd nyc-taxi-trips-analysis
   ```

2. **Install the required packages:**

   Ensure you have Python 3.7 or later installed. Then, install the required packages using:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download the dataset:**

   Download the dataset from [Kaggle](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data) and save it as `filtered_data.csv` in the project directory.

## Usage

To run the Streamlit app, navigate to the project directory and use the following command:

```bash
streamlit run app.py
```

This will start a local web server, and you can view the app in your browser at `http://localhost:8501`.

## Data

The dataset used in this application contains NYC Yellow Taxi trips data for the months of January 2015 and January-March 2016. The dataset includes pickup and dropoff coordinates, allowing for clustering and time-series analysis.

### Data Preparation

- **Datetime Conversion**: Pickup and dropoff times are converted to datetime objects.
- **Trip Duration Calculation**: The trip duration is calculated in minutes.
- **Filtering**: Users can filter data based on date, time, and trip duration.

## Visualizations

The app includes the following visualizations:

1. **Vendor ID Distribution**:
   - Displays a bar plot of the number of trips by vendor ID.

2. **Passenger Count Distribution**:
   - Shows a histogram of the distribution of passenger counts per trip.

3. **Trip Distance Distribution**:
   - Provides a histogram of trip distances, filtered to exclude outliers.

4. **Trip Duration Distribution**:
   - Illustrates a histogram of trip durations, filtered to exclude outliers.

### Metric Cards

The app also displays metric cards for quick insights:

- Total number of trips to Crate and Barrel.
- Number of trips shorter than 10 minutes.
- Number of trips longer than 61 minutes.
- Number of trips with durations between 10 and 61 minutes.
- Median number of passengers per trip and related statistics.
- Median trip distance and related statistics.
- Median trip duration and related statistics.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
