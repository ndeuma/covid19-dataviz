import json

COUNTIES_FILE = "counties.json"

def get_county(county_id):
    """Returns the JSON object for the county with the given ID (AGS), or None"""
    with open(COUNTIES_FILE) as countiesFile:
        countiesJson = json.load(countiesFile)       
        for county in countiesJson:
            if county["ags"] == county_id:
                return county
    return None