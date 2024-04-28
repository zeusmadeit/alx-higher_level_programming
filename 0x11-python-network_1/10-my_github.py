#!/usr/bin/python3
"""
this script uses the GitHub API to display 
a GitHub ID based on given credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))