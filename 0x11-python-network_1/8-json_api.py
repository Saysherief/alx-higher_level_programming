#!/usr/bin/python3
"""A script that takes in a letter and sends a POST request to http://0.0.0.0:
    5000/search_user with the letter as a parameter"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {'q': letter}
    response = requests.post(url, data=data)
    try:
        if response.json():
            j_data = response.json()
            print("[{}] {}".format(j_data['id'], j_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
