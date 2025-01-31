import pandas as pd
import requests
import os

def fetch_nasa_data():
    url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
    try:
        df = pd.read_csv(url, skiprows=1)
        os.makedirs("data/raw", exist_ok=True)
        df.to_csv("data/raw/nasa_temp.csv", index=False)
        print("NASA temperature data saved to data/raw/nasa_temp.csv")
    except Exception as e:
        print(f"Failed to fetch NASA data: {e}")

def fetch_noaa_co2():
    url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_gl.csv"
    try:
        # Fetch data and skip header rows
        df = pd.read_csv(url, skiprows=43, names=['year', 'mean', 'unc'])
        # Keep only 'year' and 'mean' columns
        df = df[['year', 'mean']]
        # Rename 'mean' to 'co2'
        df.rename(columns={'mean': 'co2'}, inplace=True)
        os.makedirs("data/raw", exist_ok=True)
        df.to_csv("data/raw/noaa_co2.csv", index=False)
        print("NOAA CO2 data saved to data/raw/noaa_co2.csv")
    except Exception as e:
        print(f"Failed to fetch NOAA data: {e}")

if __name__ == "__main__":
    fetch_nasa_data()
    fetch_noaa_co2()