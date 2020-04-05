import os.path
import urllib.request

API_HOST = "http://covid19-api-backend.herokuapp.com"
API_PATH = "/api/v0.1/"

def download(county_id):
    """Downloads the cases JSON file for the county with the given ID (AGS)"""
    download_url = f"{API_HOST}{API_PATH}county/{county_id}/cases/"

    try:
        with urllib.request.urlopen(download_url) as response:
            with open(f"{county_id}.json", "w") as jsonFile:
                jsonFile.write(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        print(f"JSON file from {download_url} could not be downloaded. HTTP Error Code: {err.code}") 

def ensure_downloaded(counties):
    for county in counties:        
        county_id = county["ags"]
        name = county["name"]
        if os.path.isfile(f"{county_id}.json"):
            print(f"County with ID {county_id} ({name}) has already been downloaded.")
        else:
            print(f"Downloading county with ID {county_id} ({name})")
            download(county_id)