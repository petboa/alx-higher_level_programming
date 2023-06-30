#!/usr/bin/python3

""" Python script that lists 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails” """

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2], sys.argv[1])
    response = requests.get(url)
    for commit in response.json()[:10]:
        print("{}: {}".format(commit.get('sha'), commit.get('commit').get('author').get('name')))
