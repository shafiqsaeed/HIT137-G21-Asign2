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


import os
import pandas as pd

# Dictionary to map month names to numbers
MONTH_MAP = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

# Function to calculate average seasonal temperatures
def calculate_average_temperatures(data_folder, output_file):
    seasons = {
        "Summer": [1, 2, 12],
        "Autumn": [3, 4, 5],
        "Winter": [6, 7, 8],
        "Spring": [9, 10, 11],
    }
    seasonal_totals = {season: [] for season in seasons}

    # Process each file
    for file in os.listdir(data_folder):
        if file.endswith(".csv"):
            file_path = os.path.join(data_folder, file)
            df = pd.read_csv(file_path)

            # Map months to numbers if necessary
            if "Month" in df.columns:
                df["Month"] = df["Month"].map(MONTH_MAP)

            # Ensure required columns are present
            if {"Month", "Temperature"}.issubset(df.columns):
                for season, months in seasons.items():
                    season_data = df[df["Month"].isin(months)]
                    if not season_data.empty:
                        seasonal_totals[season].append(season_data["Temperature"].mean())

    # Calculate overall averages
    average_seasonal_temps = {
        season: sum(temps) / len(temps) for season, temps in seasonal_totals.items() if temps
    }

    # Save to file
    with open(output_file, "w") as f:
        for season, avg_temp in average_seasonal_temps.items():
            f.write(f"{season}: {avg_temp:.2f}°C\n")

# Function to find the station with the largest temperature range
def find_largest_temp_range_station(data_folder, output_file):
    station_ranges = {}

    # Process each file
    for file in os.listdir(data_folder):
        if file.endswith(".csv"):
            file_path = os.path.join(data_folder, file)
            df = pd.read_csv(file_path)

            # Ensure required columns are present
            if {"Station", "Temperature"}.issubset(df.columns):
                grouped = df.groupby("Station")["Temperature"]
                for station, temps in grouped:
                    temp_range = temps.max() - temps.min()
                    if station not in station_ranges or temp_range > station_ranges[station]:
                        station_ranges[station] = temp_range

    # Find station(s) with largest range
    max_range = max(station_ranges.values())
    stations_with_max_range = [
        station for station, temp_range in station_ranges.items() if temp_range == max_range
    ]

    # Save to file
    with open(output_file, "w") as f:
        f.write(f"Largest Temperature Range: {max_range:.2f}°C\n")
        f.write("Stations:\n")
        for station in stations_with_max_range:
            f.write(f"{station}\n")

# Function to find warmest and coolest stations
def find_warmest_and_coolest_stations(data_folder, output_file):
    station_avg_temps = {}

    # Process each file
    for file in os.listdir(data_folder):
        if file.endswith(".csv"):
            file_path = os.path.join(data_folder, file)
            df = pd.read_csv(file_path)

            # Ensure required columns are present
            if {"Station", "Temperature"}.issubset(df.columns):
                grouped = df.groupby("Station")["Temperature"]
                for station, temps in grouped:
                    avg_temp = temps.mean()
                    station_avg_temps[station] = (
                        station_avg_temps.get(station, 0) + avg_temp
                    )

    # Average across all files
    num_years = len([file for file in os.listdir(data_folder) if file.endswith(".csv")])
    for station in station_avg_temps:
        station_avg_temps[station] /= num_years

    # Find warmest and coolest stations
    max_avg_temp = max(station_avg_temps.values())
    min_avg_temp = min(station_avg_temps.values())
    warmest_stations = [
        station for station, avg_temp in station_avg_temps.items() if avg_temp == max_avg_temp
    ]
    coolest_stations = [
        station for station, avg_temp in station_avg_temps.items() if avg_temp == min_avg_temp
    ]

    # Save to file
    with open(output_file, "w") as f:
        f.write(f"Warmest Temperature: {max_avg_temp:.2f}°C\n")
        f.write("Warmest Stations:\n")
        for station in warmest_stations:
            f.write(f"{station}\n")
        f.write(f"Coolest Temperature: {min_avg_temp:.2f}°C\n")
        f.write("Coolest Stations:\n")
        for station in coolest_stations:
            f.write(f"{station}\n")

# Main function
def main():
    data_folder = "temperature_data"  # Directory containing CSV files

    # Calculate average seasonal temperatures
    calculate_average_temperatures(data_folder, "average_temp.txt")

    # Find station(s) with the largest temperature range
    find_largest_temp_range_station(data_folder, "largest_temp_range_station.txt")

    # Find the warmest and coolest stations
    find_warmest_and_coolest_stations(data_folder, "warmest_and_coolest_station.txt")

main()
