#!/usr/bin/python3
"""A script that takes 2 arguments in order to solve this challenge
list 10 commits(from the most recent one) of the repository by the user"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)

    if response.status_code == 200:
        j_data = response.json()
        for commit in j_data[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print("{}: {}".format(sha, author_name))
