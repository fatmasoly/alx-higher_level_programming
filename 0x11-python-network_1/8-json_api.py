#!/usr/bin/python3
"""Python script that takes in a letter and sends
    a POST request to http://0.0.0.0:5000/search_user"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
        url = "http://0.0.0.0:5000/search_user"
    try:
        response = requests.post(url, data={'q': letter})
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
