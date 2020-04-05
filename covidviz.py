#!/usr/bin/python3.6

import argparse
import json
import os.path
import urllib.request

API_HOST = "http://covid19-api-backend.herokuapp.com"
API_PATH = "/api/v0.1/"

COUNTIES_FILE = "counties.json"

def download(county_id):
    """Downloads the cases JSON file for the county with the given ID (AGS)"""
    download_url = f"{API_HOST}{API_PATH}county/{county_id}/cases/"

    try:
        with urllib.request.urlopen(download_url) as response:
            with open(f"{county_id}.json", "w") as jsonFile:
                jsonFile.write(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        print(f"JSON file from {download_url} could not be downloaded. HTTP Error Code: {err.code}") 

def get_county(county_id):
    """Returns the JSON object for the county with the given ID (AGS), or None"""
    with open(COUNTIES_FILE) as countiesFile:
        countiesJson = json.load(countiesFile)       
        for county in countiesJson:
            if county["ags"] == county_id:
                return county
    return None

parser = argparse.ArgumentParser(description="Download COVID-19 case data for German counties")
parser.add_argument("county_ids", nargs="*", help="county IDs (AGS) of the counties for which to download data")
args = parser.parse_args()

for county_id in args.county_ids:
    county = get_county(county_id)    
    if county is None:
        print(f"Error: No county with ID {county_id} found.")
    else:
        name = county["name"]
        if os.path.isfile(f"{county_id}.json"):
            print(f"County with ID {county_id} ({name}) has already been downloaded.")
        else:
            print(f"Downloading county with ID {county_id} ({name})")
            download(county["ags"])

