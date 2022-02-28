#!/usr/bin/env python3
# BundleIDextract.py
"""
A simple script to extract the bundle ID from a json formatted .txt file
Usage: python3 BundleIDextract.py
Author: Inon Moshkowitz
"""

import requests
from sys import argv
import os
import json


def cwd_and_files():
    cwd = os.getcwd() # Get the current working directory (cwd)
    files = os.listdir(cwd) # Get all the files in that directory
    return(f'Files in {cwd}: {files}')


def main():
    # print(cwd_and_files())
    file = 'BundleIDextract/1.txt'
    with open(file, 'r') as f:
        data = json.load(f)
        print(data['results'][0]['bundleId'])

if __name__ == "__main__":
    main()