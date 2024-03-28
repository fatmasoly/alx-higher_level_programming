#!/usr/bin/python3
"""Python script that takes in a URL and an email,
    sends a POST request to the passed URL"""
from urllib.request import urlopen, Request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = Request(url, data)
    with urlopen(request) as response:
        print(response.read().decode("utf-8"))
