import pandas as pd
import os

def process_data():
    # Check if raw data exists
    temp_path = "data/raw/nasa_temp.csv"
    co2_path = "data/raw/noaa_co2.csv"
    if not os.path.exists(temp_path) or not os.path.exists(co2_path):
        raise FileNotFoundError("Raw data files not found. Run data_fetcher.py first.")
    
    # Load raw data
    temp = pd.read_csv(temp_path)
    co2 = pd.read_csv(co2_path)
    
    # Check if required columns exist
    if 'Year' not in temp.columns or 'J-D' not in temp.columns:
        raise ValueError("NASA temperature data is missing required columns ('Year' or 'J-D').")
    if 'year' not in co2.columns or 'co2' not in co2.columns:
        raise ValueError("NOAA CO2 data is missing required columns ('year' or 'co2').")
    
    # Convert 'year' column to integer (if it's a float)
    co2['year'] = co2['year'].astype(int)
    
    # Merge datasets on year
    merged = pd.merge(temp[['Year', 'J-D']], co2, left_on='Year', right_on='year')
    
    # Drop the redundant 'year' column
    merged.drop(columns=['year'], inplace=True)
    
    # Rename columns for clarity
    merged.rename(columns={'J-D': 'temp_anomaly'}, inplace=True)
    
    # Save processed data
    os.makedirs("data/processed", exist_ok=True)
    merged.to_csv("data/processed/merged_climate_data.csv", index=False)
    print("Data processed and saved to data/processed/merged_climate_data.csv")

# Call the function
if __name__ == "__main__":
    process_data()