#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge.
   - The first argument will be the repository name.
   - The second argument will be the owner name.
   - You must use the packages requests and sys.
   - You are not allowed to import packages other than requests and sys.
   - You don’t need to check arguments passed to the script(number or type)."""

import sys
import requests

if __name__ == "__main__":
    owner = sys.argv[1]
    re = sys.argv[2]
    limit = 10

    url = "https://api.github.com/repos/{}/{}/commits/{}".format(
            owner, re, limit)
    req = requests.get(url).json()
    for commit in req:
        name = commit.get("commit").get("author").get("name")
        print(f'{commit.get("sha")}: {name}')
