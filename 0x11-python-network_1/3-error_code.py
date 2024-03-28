#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""
from urllib.request import urlopen
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
