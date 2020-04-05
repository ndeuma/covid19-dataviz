#!/usr/bin/python3.6

import argparse
import json
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
parser.add_argument("county", help="county IDs (AGS) of the counties for which to download data")
args = parser.parse_args()

county = get_county(args.county)

if county is None:
    print(f"Error: No county with ID {args.county} found.")
    exit(1)

print(f"Downloading {county['gen']}")
download(args.county)

