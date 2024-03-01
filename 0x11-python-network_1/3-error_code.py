#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the ...
   URL and displays the body of the response (decoded in utf-8)."""

import sys
from urllib import request, error

if __name__ == "__main__":
    try:
        url = sys.argv[1]

        with request.urlopen(url) as re:
            print(re.read().decode("utf-8"))
    except error.HTTPError as error:
        print(f"Error code: {error.code}")
