#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
