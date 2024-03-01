#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL...
   and displays the value of the X-Request-Id variable found in ...
   header of the response."""

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
