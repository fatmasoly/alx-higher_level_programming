#!/bin/bash
# This Bash script takes in a URL, sends a POST request to the passed URL
curl -s -X -d POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
