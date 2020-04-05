#!/usr/bin/python3.6

import argparse

import county as county_service
import download

parser = argparse.ArgumentParser(description="Download COVID-19 case data for German counties")
parser.add_argument("county_ids", nargs="*", help="county IDs (AGS) of the counties for which to download data")
args = parser.parse_args()

downloadable_counties = []
for county_id in args.county_ids:
    county = county_service.get_county(county_id)
    if county is None:
        print(f"Error: No county with ID {county_id} found.")
    else:
        downloadable_counties += [county]

download.ensure_downloaded(downloadable_counties)

