#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)"""
import requests
import sys

if __name__ == "__main__":
    uname = sys.argv[1]
    passw = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(uname, passw))

    if response.status_code == 200:
        j_data = response.json()
        uid = j_data['id']
        print(uid)
    else:
        print("None")
