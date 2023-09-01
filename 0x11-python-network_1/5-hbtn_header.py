#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if 'X-Request-Id' in response.headers:
        header_id = response.headers['X-Request-Id']
        print(header_id)
