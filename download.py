#!/usr/bin/python3.6

import argparse
import urllib.request

API_HOST = "http://covid19-api-backend.herokuapp.com"
API_PATH = "/api/v0.1/"

parser = argparse.ArgumentParser(description="Download COVID-19 case data for German counties")
parser.add_argument("county", help="county IDs (AGS) of the counties for which to download data")
args = parser.parse_args()

download_url = f"{API_HOST}{API_PATH}county/{args.county}/cases/"

try:
    with urllib.request.urlopen(download_url) as response:
        with open(f"{args.county}.json", "w") as jsonFile:
            jsonFile.write(response.read().decode("utf-8"))
except urllib.error.HTTPError as err:
    print(f"JSON file from {download_url} could not be downloaded. HTTP Error Code: {err.code}")            
