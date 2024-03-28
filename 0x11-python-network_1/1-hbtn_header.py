#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""
from urllib.request import urlopen
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
