#!/usr/bin/env python

# Modify the townhall.yaml file with the current term's congressional members
# This script will remove any members that are no longer in Congress and add
# stub records for incoming newly elected members.

import requests, json

def run():
    # retreive current members from unitedstates/congress-legislators
    response = requests.get('https://unitedstates.github.io/congress-legislators/legislators-current.json')
    j = json.loads(response.text)
    print(j[0]['id']['bioguide'])

if __name__ == '__main__':
  run()