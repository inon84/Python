#!/usr/bin/env python3
# BundleIDextract.py
"""
A simple script to extract the bundle ID from a json formatted .txt file containing the results of an itunes App ID lookup.
Input Apple App Store ID and output the bundleId.
Input: '1044413150'
Example URL to request: 'https://itunes.apple.com/lookup?id=1044413150&country=us'
a .txt file containing the results of an itunes App ID lookup result will be downloaded from the Apple App Store.
Output bundleId: 'com.clutchpoints.ClutchPoints'
Usage: python3 BundleIDextract.py 1044413150
Author: Inon Moshkowitz
"""

import requests

apple_ids = [357828853,
            389157776,
            909998122,
            521633042,
            545551605,
            1176001245,
            1044413150] # remove when un-needed


def main(apple_ids):
    if len(apple_ids) == 0:
        return 'No input provided'
    else:
        for id in apple_ids:
            with requests.Session() as s:
                url = f'https://itunes.apple.com/lookup?id={id}&country=us'
                r = s.get(url)
                data = r.json()
                if data['resultCount'] == 0:
                    print('No results found, check your input Apple App ID')
                else:
                    bundle = data['results'][0]['bundleId']
                    print(f'AppStoreID: {id}, BundleID: {bundle}')
    
    # '''
    # .TXT file download old version, can use for testing and as separate function / tool
    # '''
    
    # from sys import argv
    # import os
    # import json
    
    # def cwd_and_files():
    #     cwd = os.getcwd() # Get the current working directory (cwd)
    #     files = os.listdir(cwd) # Get all the files in that directory
    #     return(f'Files in {cwd}: {files}')
    
    # def extract_bundleid_from_txt():
    #     file = 'BundleIDextract/no_result_example.txt' # test for no results
    #     file = 'BundleIDextract/1.txt'
    #     with open(file, 'r') as f:
    #         data = json.load(f)
    #         if data['resultCount'] == 0:
    #             print('No results found, check your input Apple App ID')
    #         else:
    #             print(data['results'][0]['bundleId'])

if __name__ == "__main__":
    main(apple_ids)