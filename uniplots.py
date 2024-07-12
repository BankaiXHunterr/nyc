import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit_shadcn_ui as ui
import matplotlib.pyplot as plt
import seaborn as sns

class TaxiDataVisualizer:
    def __init__(self, df):
        self.df = df
        
    def plot_vendor_id(self):
        st.header("Bar Plot For VendorId")
        plt.figure(figsize=(8, 6))
        vendor_counts = self.df['VendorID'].value_counts()  # Calculate counts of each VendorID
        sns.barplot(x=vendor_counts.index, y=vendor_counts.values, palette='viridis')
        plt.xlabel('Vendor ID')
        plt.ylabel('Number of Trips')
        plt.title('Number of Trips by Vendor')
        plt.xticks()  # Rotate x-axis labels if necessary
        plt.tight_layout()
        st.pyplot()  # Use st.pyplot() to display the plot in Streamlit

    
    
    def plot_passenger_count_distribution(self):
        st.header("Histplot Plot For Passanger Count Distribution")

        plt.figure(figsize=(8, 6))
        sns.histplot(self.df['passenger_count'], bins=6, kde=False, color='skyblue')
        plt.xlabel('Number of Passengers')
        plt.ylabel('Number of Trips')
        plt.title('Distribution of Passenger Counts')
        plt.xticks(self.df['passenger_count'].unique())
        plt.tight_layout()
        plt.show()
        st.pyplot()

        median = self.df['passenger_count'].median()
        less_median = len(self.df[self.df['passenger_count']<median])
        greater_median = len(self.df[self.df['passenger_count']>median])
                # Display metrics using metric cards
        cols = st.columns(3)

        with cols[0]:
            ui.metric_card(title="Median Number of Passengers", content=median,
                        description=f"Median number of passengers per trip", key="card5")

        with cols[1]:
            ui.metric_card(title="Trips with Passengers < Median", content=less_median,
                        description=f"Trips where number of passengers is less than the median", key="card6")

        with cols[2]:
            ui.metric_card(title="Trips with Passengers > Median", content=greater_median,
                        description=f"Trips where number of passengers is greater than the median", key="card7")


    def plot_trip_distance_distribution(self):
        mean_value = float(self.df['trip_distance'].mean())
        std_value = float(self.df['trip_distance'].std())
        df = self.df[self.df['trip_distance'] < 2*(mean_value + std_value)]
        
        plt.figure(figsize=(8, 6))
        sns.histplot(df['trip_distance'], bins=50, kde=False,palette='viridis')
        plt.xlabel('Trip Distance (miles)')
        plt.ylabel('Number of Trips')
        plt.title('Distribution of Trip Distances')
        plt.xticks(rotation=45)  # Rotate x-axis labels if necessary
        plt.tight_layout()
        st.pyplot()

        # Calculate and display metrics using metric cards
        median = df['trip_distance'].median()
        less_median = len(df[df['trip_distance'] < median])
        greater_median = len(df[df['trip_distance'] > median])

        cols = st.columns(3)
        with cols[0]:
            ui.metric_card(title="Median Trip Distance", content=median, description=f"{(median / len(df)) * 100:.2f}% of all trips", key="card8")
        with cols[1]:
            ui.metric_card(title="Trips with Distance < Median", content=less_median, description=f"{(less_median / len(df)) * 100:.2f}% of all trips", key="card9")
        with cols[2]:
            ui.metric_card(title="Trips with Distance > Median", content=greater_median, description=f"{(greater_median / len(df)) * 100:.2f}% of all trips", key="card10")



    def plot_trip_duration_distribution(self):
        mean_value = float(self.df['trip_duration'].mean())
        std_value = float(self.df['trip_duration'].std())
        df = self.df[self.df['trip_duration'] < 2*(mean_value + std_value)]
        
        plt.figure(figsize=(8, 6))
        sns.histplot(df['trip_duration'], bins=40, kde=False)
        plt.xlabel('Trip Duration (seconds)')
        plt.ylabel('Number of Trips')
        plt.title('Distribution of Trip Durations')
        plt.xticks(rotation=45)  # Rotate x-axis labels if necessary
        plt.tight_layout()
        st.pyplot()

        # Calculate and display metrics using metric cards
        median = df['trip_duration'].median()
        less_median = len(df[df['trip_duration'] < median])
        greater_median = len(df[df['trip_duration'] > median])

        cols = st.columns(3)
        with cols[0]:
            ui.metric_card(title="Median Trip Duration", content=round(median,2), description=f"{(median / len(df)) * 100:.2f}% of all trips", key="card11")
        with cols[1]:
            ui.metric_card(title="Trips with Duration < Median", content=less_median, description=f"{(less_median / len(df)) * 100:.2f}% of all trips", key="card12")
        with cols[2]:
            ui.metric_card(title="Trips with Duration > Median", content=greater_median, description=f"{(greater_median / len(df)) * 100:.2f}% of all trips", key="card13")
    
    def plot_distribution(self,):
        # Generate and display plots
        self.plot_vendor_id()
        self.plot_passenger_count_distribution()
        self.plot_trip_distance_distribution()
        self.plot_trip_duration_distribution()




