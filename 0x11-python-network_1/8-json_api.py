#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request ...
   to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import sys
import requests

if __name__ == "__main__":
    lett = "" if len(sys.argv) == 1 else sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    le = {'q': lett}
    resp = requests.post(url, data=le)

    try:
        per_resp = resp.json()
        if per_resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(per_resp.get("id"), per_resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
