# HIT 137 Software Now 

# Assignment 2

# Group: CAS/DAN 21
# Abu Saeed Md Shafiqur Rahman (Shafiq Rahman) - S386795
# Annafi Bin Alam (Rafin Alam) - S387086
# Neville James Doyle (Nev Doyle) - S371207
# Yuvraj Singh (Yuvraj Singh) - S383324

# GitHub Repository: https://github.com/shafiqsaeed/HIT137-G21-Assign2

# Submitted: 17 January 2025


# Question 2 - Weather data analysis 
# This program analyses the temperature data stored in CSV files, 
# calculate the requested statistics, 
# and save the results to the specified text files.


# NOTE: Place the temperature_data folder in the working directory.
# NOTE: Install pandas if not already installed using pip install pandas.


import os
import pandas as pd

# Define paths
TEMPERATURES_FOLDER = "temperature_data"
AVERAGE_TEMP_FILE = "average_temp.txt"
LARGEST_TEMP_RANGE_FILE = "largest_temp_range_station.txt"
WARMEST_AND_COOLEST_FILE = "warmest_and_coolest_station.txt"

# Define season mapping
SEASON_MAP = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"],
}

def process_temperature_data():
    # Data containers
    seasonal_temps = {season: [] for season in SEASON_MAP.keys()}
    station_temps = {}

    # Process all CSV files in the folder
    for file_name in os.listdir(TEMPERATURES_FOLDER):
        if file_name.endswith(".csv"):
            file_path = os.path.join(TEMPERATURES_FOLDER, file_name)
            data = pd.read_csv(file_path)

            # Ensure necessary columns exist
            if not {"STATION_NAME", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"}.issubset(data.columns):
                continue

            # Iterate through the rows
            for _, row in data.iterrows():
                station = row["STATION_NAME"]

                # Aggregate temperatures by season
                for season, months in SEASON_MAP.items():
                    temps = [row[month] for month in months if pd.notnull(row[month])]
                    seasonal_temps[season].extend(temps)

                # Collect all temperatures for each station
                if station not in station_temps:
                    station_temps[station] = []
                station_temps[station].extend(
                    [row[month] for month in data.columns[4:] if pd.notnull(row[month])]
                )

    # Task 1: Calculate average temperatures for each season
    average_seasonal_temps = {
        season: (sum(temps) / len(temps)) if temps else 0.0
        for season, temps in seasonal_temps.items()
    }
    with open(AVERAGE_TEMP_FILE, "w") as file:
        file.write("Average Temperatures by Season:\n")
        for season, avg_temp in average_seasonal_temps.items():
            file.write(f"{season}: {avg_temp:.2f}°C\n")

    # Task 2: Find station(s) with the largest temperature range
    temp_ranges = {
        station: max(temps) - min(temps) if temps else 0.0
        for station, temps in station_temps.items()
    }
    max_range = max(temp_ranges.values())
    largest_range_stations = [
        station for station, range_ in temp_ranges.items() if range_ == max_range
    ]
    with open(LARGEST_TEMP_RANGE_FILE, "w") as file:
        file.write("Station(s) with Largest Temperature Range:\n")
        for station in largest_range_stations:
            file.write(f"{station}: {max_range:.2f}°C\n")

    # Task 3: Find warmest and coolest stations (using actual temperature extremes)
    warmest_stations = []
    coolest_stations = []
    max_temp = float('-inf')
    min_temp = float('inf')

    for station, temps in station_temps.items():
        if temps:
            station_max = max(temps)
            station_min = min(temps)
            if station_max > max_temp:
                max_temp = station_max
                warmest_stations = [station]
            elif station_max == max_temp:
                warmest_stations.append(station)
            if station_min < min_temp:
                min_temp = station_min
                coolest_stations = [station]
            elif station_min == min_temp:
                coolest_stations.append(station)

    with open(WARMEST_AND_COOLEST_FILE, "w") as file:
        file.write("Warmest Station(s):\n")
        for station in warmest_stations:
            file.write(f"{station}: {max_temp:.2f}°C\n")
        file.write("\nCoolest Station(s):\n")
        for station in coolest_stations:
            file.write(f"{station}: {min_temp:.2f}°C\n")

    print("Analysis complete. Results written to files.")

# Run the analysis
process_temperature_data()
